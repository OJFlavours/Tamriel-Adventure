# game.py

import time
import random
import traceback
from datetime import datetime, timezone

try:
    from locations import LOCATIONS, Location
    from player import Player # Import Player from player.py
    from stats import Stats, RACES, CLASSES # Import Stats, RACES, CLASSES from stats.py
    from npc import NPC, FRIENDLY_ROLES, HOSTILE_ROLES, NAME_POOLS
    from combat import Combat
    from ui import UI
    from items import generate_random_item, Item, generate_item_from_key, Torch
    from events import trigger_random_event, explore_location # Now triggers events with more detail
    from quests import (
        QuestLog,
        generate_location_appropriate_quest,
        process_quest_rewards,
        list_player_quests_for_display,
        Quest # Import Quest class
    )
    import tags
    import flavor
    from rumors import generate_rumor # for generating rumors in NPC dialogue
except ImportError as e:
    print(f"Error importing modules: {e}")
    traceback.print_exc()
    input("Press Enter to exit...")
    exit(1)

# Globals
# known_locations and known_locations_objects are now player attributes
npc_registry = {}
game_start_time = None

ALL_LOCATIONS = LOCATIONS

# --- Utility & Helper Functions ---

def _build_location_maps(loc_list):
    by_id = {}
    by_name = {}
    def recurse(loc):
        by_id[loc["id"]] = loc
        by_name[loc["name"]] = loc
        for sub in loc.get("sub_locations", []):
            recurse(sub)
    for top in loc_list:
        recurse(top)
    return by_id, by_name

LOCATION_BY_ID, LOCATION_BY_NAME = _build_location_maps(ALL_LOCATIONS)

ENCOUNTER_NAMES = { # This is from your original game.py, may not be fully used with new event system
    "city": [
        {"name": "Street Urchin", "desc": "A nimble child attempts to pickpocket you.", "type": "thieves_encounter"},
        {"name": "Drunkard",    "desc": "A staggering drunkard accosts you for coin.", "type": "social_encounter"},
    ],
    "forest": [
        {"name": "Wolf Pack",     "desc": "A pack of wolves circles, seeking prey.", "type": "hostile_creatures"},
        {"name": "Lost Traveler", "desc": "A lost traveler asks for directions.", "type": "social_encounter"},
    ],
    "plains": [
        {"name": "Merchant Caravan", "desc": "A well-guarded merchant caravan passes by.", "type": "neutral_encounter"},
        {"name": "Lone Elk", "desc": "A majestic elk grazes peacefully.", "type": "neutral_creature"}
    ],
    "mountain": [
        {"name": "Rockslide", "desc": "The ground trembles as rocks tumble down a nearby slope!", "type": "hazard_event"},
        {"name": "Goat Herd", "desc": "A herd of mountain goats skillfully navigates the cliffs.", "type": "neutral_creature"}
    ],
    "cave": [
        {"name": "Bear", "desc": "A large bear growls from the darkness.", "type": "hostile_creature"},
        {"name": "Lost Explorer's Note", "desc": "You find a tattered note, the last words of a lost explorer.", "type": "lore_find"}
    ],
    "ruin": [
        {"name": "Restless Spirit", "desc": "A ghostly figure materializes, bound to these ancient stones.", "type": "undead_encounter"},
        {"name": "Ancient Trap", "desc": "You narrowly avoid an ancient, cunningly hidden trap.", "type": "hazard_event"}
    ],
}

def clear_screen():
    UI.clear_screen()

def get_flavor_text(tags_list_param, category, ensure_vignette=False):
    if not tags_list_param:
        return ""
    tags_filtered = [t for t in tags_list_param if isinstance(t, (str, int, float))]

    class DummyEntity:
        def __init__(self, final_tags_list, category_):
            self.tags = {}
            # Use specific TAGS categories for correct flavor retrieval
            if category_ == "location_tags" and hasattr(tags, 'LOCATIONS'):
                self.tags['location'] = {}
                for tag_type, possible_values in tags.LOCATIONS.items():
                    found_tags = [t for t in final_tags_list if t in possible_values]
                    if found_tags:
                        self.tags['location'][tag_type] = found_tags
            elif category_ == "npc_tags" and hasattr(tags, 'NPCS'):
                self.tags['npc'] = {}
                for tag_type, possible_values in tags.NPCS.items():
                    found_tags = [t for t in final_tags_list if t in possible_values]
                    if found_tags:
                        self.tags['npc'][tag_type] = found_tags
            # Add other categories if needed, e.g., "item_tags", "quest_tags", etc.
            else:
                # Fallback for generic tag handling if category not specific
                self.tags[category_] = final_tags_list
    
    entity = DummyEntity(tags_filtered, category)
    vignettes = flavor.get_flavor(entity) if hasattr(flavor, 'get_flavor') else []
    if not vignettes and ensure_vignette:
        return "The air is thick with untold stories."
    return random.choice(vignettes) if vignettes else ""

def _find_hierarchy(loc_id):
    target_loc = LOCATION_BY_ID.get(loc_id)
    if not target_loc: return None, None

    for hold_candidate in ALL_LOCATIONS:
        if hold_candidate["id"] == loc_id:
            return hold_candidate, None

    for hold in ALL_LOCATIONS:
        for city in hold.get("sub_locations", []):
            if city["id"] == loc_id:
                return hold, city
            for venue in city.get("sub_locations", []):
                if venue["id"] == loc_id:
                    return hold, city
    return None, None

# --- Location, Exploration & Travel Functions ---

def get_hold_by_id(hold_id: int) -> Dict[str, Any] | None:
    """Finds a hold by its ID from ALL_LOCATIONS."""
    for loc in ALL_LOCATIONS:
        if loc.get("id") == hold_id and "hold" in loc.get("tags", []):
            return loc
    return None

def get_known_holds(player: Player) -> List[Dict[str, Any]]:
    """Returns a sorted list of Hold location objects known by the player."""
    known_holds = []
    for loc_id in player.known_location_ids:
        loc_obj = LOCATION_BY_ID.get(loc_id)
        if loc_obj and "hold" in loc_obj.get("tags", []):
            known_holds.append(loc_obj)
    return sorted(known_holds, key=lambda x: x.get("name", ""))

def get_known_primary_locations_in_hold(player: Player, hold_id: int) -> List[Dict[str, Any]]:
    """
    Returns a list of known primary locations (cities, towns, standalone dungeons, etc.)
    that are direct children of the specified hold.
    """
    known_locs_in_hold = []
    hold_obj = get_hold_by_id(hold_id) # Ensure we are working with the Hold object
    if not hold_obj:
        return []

    for sub_loc_candidate in hold_obj.get("sub_locations", []):
        if sub_loc_candidate["id"] in player.known_location_ids:
            known_locs_in_hold.append(sub_loc_candidate)
    
    return sorted(known_locs_in_hold, key=lambda x: x.get("name", ""))

def get_known_sub_locations(player: Player, parent_loc_id: int) -> List[Dict[str, Any]]:
    """
    Returns a list of known sub-locations (e.g., venues in a city)
    for a given parent location ID.
    """
    known_subs = []
    parent_loc_obj = LOCATION_BY_ID.get(parent_loc_id)
    if not parent_loc_obj:
        return []

    for sub_loc_candidate in parent_loc_obj.get("sub_locations", []):
        if sub_loc_candidate["id"] in player.known_location_ids:
            known_subs.append(sub_loc_candidate)
            
    return sorted(known_subs, key=lambda x: x.get("name", ""))

def process_travel(player: Player, destination_loc_obj: Dict[str, Any], previous_location_obj: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handles the logic for a player arriving at a new location.
    - Updates player's current location.
    - Prints travel messages.
    - Discovers connected and sub-locations.
    - Handles tag inheritance for flavor text.
    - Generates NPCs.
    - Updates quest log.
    Returns the destination_loc_obj.
    """
    UI.clear_screen()
    UI.print_heading(f"Traveling to {destination_loc_obj['name']}")
    # time.sleep(0.5) # Brief pause for travel feel

    player.current_location_obj = destination_loc_obj
    player.update_current_location_for_quest(destination_loc_obj)

    # Auto-discover immediate sub-locations of the destination
    if "sub_locations" in destination_loc_obj:
        for sub_loc_to_discover in destination_loc_obj.get("sub_locations", []):
            if sub_loc_to_discover["id"] not in player.known_location_ids:
                player.known_location_ids.add(sub_loc_to_discover["id"])
                if sub_loc_to_discover not in player.known_locations_objects:
                    player.known_locations_objects.append(sub_loc_to_discover)
    
    discover_connected_locations(player, destination_loc_obj)

    UI.slow_print(f"You arrive at {destination_loc_obj['name']}.")
    UI.slow_print(destination_loc_obj['desc'])

    tags_for_dest = list(destination_loc_obj.get("tags", []))
    inheritable = tags.INHERITABLE_TAGS if hasattr(tags, 'INHERITABLE_TAGS') else set()
    
    parent_hold, parent_city = _find_hierarchy(destination_loc_obj["id"])
    contextual_parent = None
    if parent_city and parent_city["id"] != destination_loc_obj["id"]:
        contextual_parent = parent_city
    elif parent_hold and parent_hold["id"] != destination_loc_obj["id"]:
        contextual_parent = parent_hold
    
    if contextual_parent:
        tags_for_dest.extend([t for t in contextual_parent.get("tags", []) if t in inheritable])
    tags_for_dest = list(set(tags_for_dest))

    UI.slow_print(get_flavor_text(tags_for_dest, "location_tags", ensure_vignette=True))
    
    generate_npcs_for_location(destination_loc_obj)
    
    return destination_loc_obj

def discover_connected_locations(player: Player, location_data: dict):
    """
    Discovers locations connected to the given location_data and updates
    the player's known_location_ids and known_locations_objects.
    """
    for mode in ("roads", "paths"):
        for dest_name in location_data.get("travel", {}).get(mode, []):
            dest_loc_obj = LOCATION_BY_NAME.get(dest_name)
            if dest_loc_obj:
                if dest_loc_obj["id"] not in player.known_location_ids:
                    player.known_location_ids.add(dest_loc_obj["id"])
                    if dest_loc_obj not in player.known_locations_objects: # Ensure no duplicates in list
                        player.known_locations_objects.append(dest_loc_obj)

def determine_city_type(city_obj):
    """Determines the display type string for a city-level location."""
    tags = city_obj.get("tags", [])
    if "city" in tags: return "City"
    if "town" in tags: return "Town"
    if "village" in tags: return "Village"
    if "barrow" in tags or "nordic_ruin" in tags: return "Ruin/Barrow"
    if "cave" in tags: return "Cave System"
    if "mine" in tags: return "Mine"
    if "camp" in tags: return "Camp"
    if "watchtower" in tags: return "Watchtower"
    if "fort" in tags and "ruined" not in tags : return "Fort"
    if "dungeon" in tags : return "Dungeon Site"
    return "Settlement"

def determine_venue_type(venue_obj):
    """Determines the display type string for a venue-level location."""
    tags = venue_obj.get("tags", [])
    if "tavern" in tags or "inn" in tags: return "Tavern/Inn"
    if "shop" in tags and "alchemy" in tags : return "Apothecary"
    if "shop" in tags and "blacksmith" in tags : return "Smithy"
    if "shop" in tags: return "Shop"
    if "keep" in tags or ("jarls_seat" in tags and "palace" not in tags and "longhouse" not in tags): return "Keep"
    if "palace" in tags or ("jarls_seat" in tags and ("palace" in tags or "longhouse" in tags)): return "Palace/Longhouse"
    if "temple" in tags: return "Temple"
    if "guild" in tags or "college" in tags or "meadhall" in tags : return "Guild/College Hall"
    if "residence" in tags: return "Residence"
    if "market" in tags : return "Market Area"
    if "docks" in tags: return "Docks"
    if "catacombs" in tags or "hall_of_the_dead" in tags : return "Catacombs"
    return "Point of Interest"

def explore_and_travel_menu(player: Player, current_location_param: Dict[str, Any]) -> Dict[str, Any]:
    """
    New menu for exploring known locations and traveling, categorized by Hold.
    """
    while True: # Main travel loop (allows returning to Hold selection)
        known_holds = get_known_holds(player)
        if not known_holds:
            UI.clear_screen()
            UI.print_heading("World Map")
            UI.print_info("You have not yet discovered any major Holds in Skyrim.")
            UI.press_enter()
            return current_location_param

        # Stage 1: Select a Hold
        selected_hold = UI.select_from_paginated_list(
            options=[{"name": h["name"], "id": h["id"], "obj": h} for h in known_holds],
            prompt_message="Select a Hold to view its locations (or 0 to cancel):"
        )
        if not selected_hold: # Player cancelled Hold selection
            return current_location_param
        
        selected_hold_obj = selected_hold["obj"]

        while True: # Loop for selecting locations within the chosen Hold
            known_primary_locs = get_known_primary_locations_in_hold(player, selected_hold_obj["id"])
            
            if not known_primary_locs:
                UI.clear_screen()
                UI.print_heading(f"Locations in {selected_hold_obj['name']}")
                UI.print_info(f"You have not discovered any specific locations within {selected_hold_obj['name']} yet, beyond the Hold itself.")
                # Option to "explore" the Hold generally, or travel to it if not already there.
                options_for_empty_hold = [{"name": f"Explore {selected_hold_obj['name']} (General Area)", "id": selected_hold_obj["id"], "obj": selected_hold_obj, "is_general_hold": True}]
                
                # Add "Back to Hold Selection"
                # No, select_from_paginated_list handles cancel with '0' which will break this inner loop.

                chosen_action_for_empty_hold = UI.select_from_paginated_list(
                    options=options_for_empty_hold,
                    prompt_message=f"Choose an action for {selected_hold_obj['name']} (or 0 to go back to Hold selection):"
                )
                if not chosen_action_for_empty_hold: # Cancelled from empty hold options
                    break # Break from inner loop, back to Hold selection
                
                # If "Explore General Area" is chosen
                if chosen_action_for_empty_hold.get("is_general_hold"):
                    if current_location_param["id"] == selected_hold_obj["id"]:
                        UI.print_info(f"You are already in the general area of {selected_hold_obj['name']}.")
                        UI.press_enter()
                        # Stay in this menu, perhaps allow re-selection or examining the hold itself.
                        # For now, just break to re-prompt hold selection.
                        break
                    else:
                        return process_travel(player, selected_hold_obj, current_location_param)
                else: # Should not happen with current logic for empty hold
                    break

            # Stage 2: Select a Primary Location within the Hold
            primary_loc_options = [{"name": f"{loc['name']} ({determine_city_type(loc)})", "id": loc["id"], "obj": loc} for loc in known_primary_locs]
            
            selected_primary_loc_choice = UI.select_from_paginated_list(
                options=primary_loc_options,
                prompt_message=f"Locations in {selected_hold_obj['name']} (or 0 to go back to Hold selection):"
            )

            if not selected_primary_loc_choice: # Player cancelled primary location selection
                break # Break from inner loop, back to Hold selection
            
            selected_primary_loc_obj = selected_primary_loc_choice["obj"]
            final_destination_obj = selected_primary_loc_obj # Default to this

            # Stage 3: Select a Sub-Location (if applicable)
            known_sub_locs = get_known_sub_locations(player, selected_primary_loc_obj["id"])
            
            if known_sub_locs:
                sub_loc_options = [{"name": f"{sub['name']} ({determine_venue_type(sub)})", "id": sub["id"], "obj": sub} for sub in known_sub_locs]
                # Add option to select the parent primary location itself
                sub_loc_options.insert(0, {"name": f"{selected_primary_loc_obj['name']} (Main Area)", "id": selected_primary_loc_obj["id"], "obj": selected_primary_loc_obj, "is_main_area": True})

                selected_sub_loc_choice = UI.select_from_paginated_list(
                    options=sub_loc_options,
                    prompt_message=f"Specific places within {selected_primary_loc_obj['name']} (or 0 to go back to locations in {selected_hold_obj['name']}):"
                )

                if not selected_sub_loc_choice: # Player cancelled sub-location selection
                    continue # Continue inner loop (back to primary location selection for this hold)
                
                final_destination_obj = selected_sub_loc_choice["obj"]
            
            # Now, travel to final_destination_obj
            if current_location_param["id"] == final_destination_obj["id"]:
                UI.clear_screen()
                UI.print_info(f"You are already at {final_destination_obj['name']}.")
                UI.press_enter()
                # Player is already at the location. We can either return them to the game loop
                # or allow them to re-select. For now, let's return to the game loop.
                return current_location_param
            else:
                return process_travel(player, final_destination_obj, current_location_param)
        # End of inner while loop (location selection within a hold)
    # End of outer while loop (hold selection)
    return current_location_param # Should be unreachable if logic is correct, but as a fallback.


def look_around_area(player, current_location_param, npc_registry_param, all_locs_param, ui_param):
    UI.slow_print(f"You take a moment to observe your surroundings in {current_location_param['name']}...")
    
    # Pass player to explore_location
    explore_location(player, current_location_param, {}, npc_registry_param, all_locs_param, ui_param)
    
    # Original random quest generation logic
    if random.random() < 0.25:
        # Pass quest_giver_id as None because this quest isn't from a specific NPC interaction initially
        new_quest = generate_location_appropriate_quest(player.level, current_location_param.get("tags", []), None)
        if new_quest:
            UI.slow_print("\nSomething catches your eye... it seems to be a new undertaking!")
            UI.slow_print(f"Quest: {new_quest.title}")
            UI.slow_print(f"Objective: {new_quest.description}") # Main quest description
            
            # Display current stage objectives
            if new_quest.current_stage:
                UI.slow_print(f"Current Tasks:")
                for obj in new_quest.current_stage.get("objectives", []):
                    UI.slow_print(f"  - {obj.get('note', 'A task awaits.')}")


            reward_parts = []
            if isinstance(new_quest.reward, dict):
                for r_type, r_value in new_quest.reward.items():
                    if isinstance(r_value, Item):
                        reward_parts.append(f"{r_value.name} ({r_value.category.capitalize()})")
                    else:
                        reward_parts.append(f"{r_value} {r_type.capitalize()}")
            else:
                reward_parts.append(str(new_quest.reward))

            UI.slow_print(f"Reward: {', '.join(reward_parts) if reward_parts else 'A fair compensation'}")
            
            if hasattr(player, 'quest_log') and player.quest_log is not None:
                player.quest_log.add_quest(new_quest)
                UI.slow_print("The details have been noted in your journal.")
            else:
                UI.slow_print("(You feel you should find a way to record such tasks.)")
    return current_location_param

# --- NPC Generation Functions ---

def determine_npc_count(tags_list):
    # Increased NPC counts for more lively locations
    if any(t in tags_list for t in ["city", "capital"]):
        return random.randint(8, 15) # Increased range for cities
    elif any(t in tags_list for t in ["tavern", "inn"]):
         return random.randint(5, 10) # Increased range for taverns/inns
    elif any(t in tags_list for t in ["town", "village", "market", "keep"]):
        return random.randint(4, 8) # Increased range for towns/villages/markets/keeps
    elif any(t in tags_list for t in ["camp", "dungeon", "ruin", "mine", "watchtower", "lair"]):
        return random.randint(2, 6) # Slightly increased range for dangerous/remote locations
    else:
        return random.randint(1, 3) # Slightly increased range for other locations

def determine_npc_culture(demographics):
    culture_weights = []
    cultures = []
    for race_name_key, percentage in demographics.items():
        valid_race_key = race_name_key.lower()
        if valid_race_key in RACES and valid_race_key != "others":
            cultures.append(valid_race_key)
            culture_weights.append(percentage)

    if not cultures:
        return random.choice(list(RACES.keys()))
    try:
        return random.choices(cultures, weights=culture_weights, k=1)[0]
    except ValueError:
        return random.choice(list(RACES.keys())) if cultures else "nord"

def determine_npc_role(tags_list, base_role_pool):
    if "college" in tags_list or "mage_guild" in tags_list:
        return random.choice(["mage_apprentice", "scholar", "magic_lecturer", "college_guard"])
    if "companions" in tags_list:
        return random.choice(["companion_warrior", "new_blood", "circle_member"])
    if "thieves_guild_den" in tags_list or ("thieves" in tags_list and "underground" in tags_list):
        return random.choice(["thief_lookout", "pickpocket", "guild_rogue"])
    if "darkbrotherhood_sanctuary" in tags_list:
        return random.choice(["db_assassin", "db_initiate", "sanctuary_speaker"])
    if "dwemer_ruin" in tags_list:
        if random.random() < 0.6: return random.choice(["dwarven_sphere_damaged", "dwarven_spider_worker", "falmer_skulker"])
        else: return "explorer"
    if "mine" in tags_list and "abandoned" not in tags_list and "infested" not in tags_list:
        return "miner" if random.random() < 0.7 else "mine_foreman"
    if "bandit_camp" in tags_list or ("camp" in tags_list and "bandit" in tags_list) or "bandit_hideout" in tags_list:
        return random.choice(["bandit", "bandit_thug", "bandit_archer", "bandit_leader"])
    if "forsworn_camp" in tags_list or "forsworn_redoubt" in tags_list:
        return random.choice(["forsworn_raider", "forsworn_shaman", "forsworn_briarheart"])
    if ("temple" in tags_list or "shrine" in tags_list) and "ruined" not in tags_list and "abandoned" not in tags_list:
        return random.choice(["priest", "pilgrim", "temple_guardian", "healer"])
    if "military_fort" in tags_list or "watchtower_manned" in tags_list:
        faction = "stormcloak_soldier" if "stormcloak_controlled" in tags_list else "imperial_soldier"
        if "officer_quarters" in tags_list: faction = faction.replace("soldier","officer")
        return faction
    if "farm" in tags_list:
        return random.choice(["farmer", "farm_hand", "farmer_spouse"])
    if "shop" in tags_list or "market" in tags_list:
        return random.choice(["merchant", "stall_owner", "shop_assistant", "city_guard_patrolling"])
    if "port" in tags_list:
        return random.choice(["sailor", "dock_worker", "ship_captain_ashore", "fishmonger"])

    if not base_role_pool:
        return random.choice(list(FRIENDLY_ROLES | HOSTILE_ROLES))
        
    return random.choice(list(base_role_pool))

def generate_tavern_npcs(location, tags_list, demographics):
    culture_for_innkeeper = determine_npc_culture(demographics)
    innkeeper_race = culture_for_innkeeper if culture_for_innkeeper else "Nord"
    innkeeper = NPC(name=None, race=innkeeper_race, role="innkeeper", level=random.randint(3,7))
    npc_registry[location["id"]].append(innkeeper)

    patron_count = random.randint(1, 4)
    patron_role_pool = {"adventurer", "farmer", "hunter", "traveler", "local", "mercenary"}
    if "trade" in tags_list or "city" in tags_list or "market" in tags_list: patron_role_pool.add("merchant")
    if "companions" in tags_list: patron_role_pool.add("warrior")
    if "stormcloak" in tags_list: patron_role_pool.add("stormcloak_supporter")
    if "imperial" in tags_list: patron_role_pool.add("imperial_citizen")
    if "bards_college_nearby" in tags_list or "bards" in tags_list: patron_role_pool.add("bard_student")

    for _ in range(patron_count):
        patron_culture = determine_npc_culture(demographics)
        patron_race = patron_culture if patron_culture else "Nord"
        patron_role = random.choice(list(patron_role_pool)) if patron_role_pool else "local"
        patron = NPC(name=None, race=patron_race, role=patron_role, level=random.randint(1,5))
        npc_registry[location["id"]].append(patron)

    if random.random() < 0.7 and "bards" not in patron_role_pool:
        bard_culture = determine_npc_culture(demographics)
        bard_race = bard_culture if bard_culture else "Nord"
        bard = NPC(name=None, race=bard_race, role="bard", level=random.randint(2,6))
        npc_registry[location["id"]].append(bard)

def generate_standard_npcs(location, tags_list, npc_count, role_pool, demographics):
    generated_names = set() # Keep track of names generated for this location
    for _ in range(npc_count):
        role = determine_npc_role(tags_list, role_pool)
        culture = determine_npc_culture(demographics)
        npc_race = culture if culture else random.choice(list(RACES.keys()))
        
        if npc_race == "dwemer" and role not in ["dwemer_construct", "dwemer_ghost", "ancient_scholar_spirit"]:
            role = random.choice(["dwemer_construct", "dwemer_ghost"]) if random.random() < 0.7 else "lingering_echo"

        npc_level_min, npc_level_max = location.get("level_range",(1,5))
        npc_level = random.randint(npc_level_min, npc_level_max)
        npc_level = max(1, npc_level + random.randint(-1,1))

        # Attempt to generate a unique name for this location
        attempts = 0
        new_npc = None
        while attempts < 5: # Try up to 5 times to get a unique name
            new_npc = NPC(name=None, race=npc_race, role=role, level=npc_level)
            if new_npc.name not in generated_names:
                generated_names.add(new_npc.name)
                break
            attempts += 1
            # If attempts fail, the last generated NPC (potentially with a duplicate name) will be used.
            # This is a fallback to ensure NPCs are still generated even if name pools are small.

        if new_npc:
             npc_registry[location["id"]].append(new_npc)


def generate_npcs_for_location(location_obj):
    try:
        if location_obj.get("is_encounter"):
            return

        # Only generate if the location doesn't have NPCs yet
        if location_obj["id"] in npc_registry and npc_registry[location_obj["id"]]:
            return

        npc_registry[location_obj["id"]] = []
        
        parent_hold, parent_city = _find_hierarchy(location_obj["id"])
        combined_tags_for_npc_gen = list(location_obj.get("tags", []))
        inheritable_npc_context_tags = {
            "nordic", "imperial", "stormcloak", "thieves", "corrupt", "college", "companions", "darkbrotherhood",
            "military", "bards", "city", "town", "village", "hold", "dwemer", "forsworn", "undead", "vampire", "mage_guild"
        }

        contextual_parent = None
        # Check if the location is a direct sub-location of a city
        if parent_city and parent_city["id"] != location_obj["id"] and any(sub_loc["id"] == location_obj["id"] for sub_loc in parent_city.get("sub_locations", [])):
            contextual_parent = parent_city
        # Check if the location is a direct sub-location of a hold (but not a city)
        elif parent_hold and parent_hold["id"] != location_obj["id"] and any(sub_loc["id"] == location_obj["id"] for sub_loc in parent_hold.get("sub_locations", [])):
             contextual_parent = parent_hold
        # If the location is a city, its contextual parent for tags is the hold
        elif "city" in combined_tags_for_npc_gen and parent_hold and parent_hold["id"] != location_obj["id"]:
             contextual_parent = parent_hold


        if contextual_parent:
            combined_tags_for_npc_gen.extend([
                t for t in contextual_parent.get("tags", []) if t in inheritable_npc_context_tags
            ])
        combined_tags_for_npc_gen = list(set(combined_tags_for_npc_gen))
        
        # --- Demographics Inheritance Logic ---
        demographics_source = location_obj
        # If location has no demographics, check parent city
        if not demographics_source.get("demographics") and contextual_parent and contextual_parent.get("demographics"):
             demographics_source = contextual_parent
        # If still no demographics, check parent hold
        if not demographics_source.get("demographics") and parent_hold and parent_hold.get("demographics"):
             demographics_source = parent_hold

        # Use found demographics or default to Nord
        demographics = demographics_source.get("demographics", {"Nord": 100})

        npc_count = determine_npc_count(combined_tags_for_npc_gen)
        
        role_pool = set(FRIENDLY_ROLES)
        hostile_location_indicators = ["bandit", "dungeon", "ruin", "forsworn", "necromancer", "vampire_lair", "monster_den", "lair"]
        if any(indicator in combined_tags_for_npc_gen for indicator in hostile_location_indicators) or \
           any(indicator in location_obj.get("name","").lower() for indicator in hostile_location_indicators):
            role_pool.update(HOSTILE_ROLES)
        if "city" not in combined_tags_for_npc_gen and "town" not in combined_tags_for_npc_gen:
            role_pool = role_pool - {"merchant", "noble", "bard", "scholar"}

        if "tavern" in combined_tags_for_npc_gen or "inn" in combined_tags_for_npc_gen :
            generate_tavern_npcs(location_obj, combined_tags_for_npc_gen, demographics)
        else:
            generate_standard_npcs(location_obj, combined_tags_for_npc_gen, npc_count, role_pool, demographics)

    except Exception as e:
        UI.print_failure(f"Error in generate_npcs_for_location for {location_obj.get('name', 'Unknown Location')}: {e}")

# --- NPC Interaction & Combat ---

def list_npcs_at_location(location, player):
    try:
        npcs_here = npc_registry.get(location["id"], [])
        if not npcs_here:
            UI.slow_print("No souls linger here, save the whispers of the wind.")
            return

        UI.print_heading(f"Souls at {location['name']}")
        active_npcs = [npc for npc in npcs_here if npc.stats.is_alive()]

        if not active_npcs:
            UI.slow_print("Only the fallen remain here.")
            return

        for i, npc in enumerate(active_npcs, 1):
            npc_info_tags = npc.tags.get("npc", {})
            attitude_display_val = npc_info_tags.get("attitude", "neutral")
            attitude_display = f"({attitude_display_val.capitalize()})" if attitude_display_val else ""
            # npc.full_name is already correctly capitalized from NPC.__init__
            UI.print_info(f"[{i}] {npc.full_name} — {npc.role.replace('_', ' ').capitalize()} ({npc.race.capitalize()}) {attitude_display}")
        UI.print_line()

        sel = UI.print_prompt("With whom do you wish to parley? (0 to pass)").strip()
        if sel.isdigit():
            choice_index = int(sel)
            if 1 <= choice_index <= len(active_npcs):
                selected_npc = active_npcs[choice_index - 1]
                selected_npc_attitude_tags = selected_npc.tags.get("npc", {}).get("attitude", "")
                
                is_hostile = "hostile" in selected_npc_attitude_tags or \
                              selected_npc.role in HOSTILE_ROLES or \
                              any(ht in selected_npc.role.lower() for ht in ["bandit", "draugr", "skeleton", "vampire", "wolf", "bear", "spider", "chaurus", "falmer", "forsworn_hostile_variant"])

                if is_hostile and player.combat is None:
                    UI.slow_print(f"{selected_npc.name} snarls and lunges with clear hostile intent!")
                    combat_instance = Combat(player, [selected_npc], location)
                    player.combat = combat_instance
                    combat_instance.run()
                elif player.combat is not None:
                     UI.slow_print("You are already engaged in combat!")
                else:
                    selected_npc.dialogue(player, location)
            elif choice_index != 0:
                UI.slow_print("No such soul stands before you.")
    except Exception as e:
        UI.print_failure(f"Error in list_npcs_at_location: {e}")

def combat_demo(player, current_location_obj):
    try:
        enemy_level = player.level + random.randint(-1, 1)
        enemy_level = max(1, enemy_level)
        
        parent_hold, parent_city = _find_hierarchy(current_location_obj["id"])
        demographics_source = current_location_obj
        if parent_city and not demographics_source.get("demographics"): demographics_source = parent_city
        if parent_hold and not demographics_source.get("demographics"): demographics_source = parent_hold
        
        loc_tags = current_location_obj.get("tags", [])
        enemy_role = "bandit_raider"
        enemy_unique_id = "bandit_raider_generic" # Default generic ID for tracking
        
        if "undead" in loc_tags or "barrow" in loc_tags or "graveyard" in loc_tags:
            enemy_role = random.choice(["draugr_restless", "skeleton_warrior", "ghost_ancient"])
            enemy_unique_id = enemy_role
        elif "cave" in loc_tags and "animal_den" in loc_tags:
            enemy_role = random.choice(["cave_bear_young", "wolf_alpha", "giant_spider_cave"])
            enemy_unique_id = enemy_role
        elif "dwemer_ruin" in loc_tags:
            enemy_role = random.choice(["dwarven_sphere_guardian", "falmer_warrior", "chaurus_hunter_small"])
            enemy_unique_id = enemy_role

        enemy_race = determine_npc_culture(demographics_source.get("demographics", {"Nord": 50, "Orc": 20, "Dunmer": 15, "Khajiit":15 }))

        if "draugr" in enemy_role: enemy_race = "undead_nord"
        elif "skeleton" in enemy_role: enemy_race = "undead_skeleton"
        elif "ghost" in enemy_role: enemy_race = "spirit"
        elif "falmer" in enemy_role: enemy_race = "falmer"
        elif "dwarven" in enemy_role: enemy_race = "dwemer_construct_race"
        elif "wolf" in enemy_role or "bear" in enemy_role or "spider" in enemy_role or "chaurus" in enemy_role:
             enemy_race = enemy_role.split('_')[0] + "_creature"

        enemy = NPC(
            name=None,
            level=enemy_level,
            race=enemy_race,
            role=enemy_role
        )
        enemy.unique_id = f"{enemy_role}_{random.randint(1000,9999)}" # More unique ID for demo enemies
        
        if "bandit" in enemy_role or "draugr" in enemy_role or "skeleton" in enemy_role or "falmer" in enemy_role:
            weapon_keys = ["iron_sword", "steel_axe_old", "iron_mace_rusty", "ancient_nord_sword_chipped", "falmer_sword_crude"]
            armor_keys = ["hide_armor_scraps", "iron_armor_dented", "ancient_nord_armor_piece", "falmer_armor_basic"]
            
            if random.random() < 0.8:
                enemy_weapon = generate_item_from_key(random.choice(weapon_keys), enemy.level)
                if enemy_weapon: enemy.stats.inventory.append(enemy_weapon)
            if random.random() < 0.6:
                enemy_armor = generate_item_from_key(random.choice(armor_keys), enemy.level)
                if enemy_armor: enemy.stats.inventory.append(enemy_armor)
        
        enemies_for_combat = [enemy]
        num_additional_enemies = random.randint(0, 2) # Spawn 0 to 2 additional enemies

        for _ in range(num_additional_enemies):
            additional_enemy_level = max(1, player.level + random.randint(-2, 0))
            # Slightly vary additional enemy roles/races for more dynamic encounters
            additional_enemy_role = random.choice(["bandit_thug", "bandit_scout", "wolf_creature"]) # Example roles
            additional_enemy_race = determine_npc_culture(demographics_source.get("demographics", {"Nord": 70, "Orc": 15, "Khajiit":15 }))
            if "wolf" in additional_enemy_role: additional_enemy_race = "wolf_creature"

            additional_enemy = NPC(
                name=None, # Let NPC class generate a name
                level=additional_enemy_level,
                race=additional_enemy_race,
                role=additional_enemy_role
            )
            additional_enemy.unique_id = f"{additional_enemy_role}_{random.randint(1000,9999)}"
            enemies_for_combat.append(additional_enemy)

        enemy_names = ", ".join([e.name for e in enemies_for_combat])
        UI.slow_print(f"Suddenly, hostile figures emerge: {enemy_names}!")

        if player.combat is None:
            combat_instance = Combat(player, enemies_for_combat, current_location_obj)
            player.combat = combat_instance # Assign combat instance to player
            combat_instance.run()
            
            # Grant XP for all defeated enemies in this combat session
            for defeated_enemy in enemies_for_combat:
                if not defeated_enemy.stats.is_alive():
                    player.update_defeated_enemies_tracker(defeated_enemy.unique_id)
                    player.gain_experience(defeated_enemy.level * 10)
        else:
            # This call to print_warning was the source of the error.
            # UI.print_warning is now defined.
            UI.print_warning("Cannot initiate demo combat: Player already in combat.")
        
        return current_location_obj
    except Exception as e:
        UI.print_failure(f"Error in combat_demo: {e}") # This will now use the defined UI.print_failure
        return current_location_obj

# --- Inventory & Item Functions ---

def display_inventory_with_equipped(player):
    UI.print_subheading("Inventory")
    if not player.stats.inventory and not player.equipment:
        UI.slow_print("Your satchel is empty, and you wear nothing but your conviction.")
        return []

    display_list_for_selection = []
    current_selection_idx = 1

    UI.print_info("--- Equipped ---")
    if not player.equipment:
        UI.print_info("Nothing equipped.")
    else:
        for item_obj in player.equipment:
            desc_preview = item_obj.get_description().split('\n')[0]
            for slot, Gitem in player.slots.items():
                if Gitem == item_obj:
                     desc_preview += f" (Slot: {slot.capitalize()})"
                     break
            UI.print_info(f"[{current_selection_idx}] {item_obj.name} (Equipped) - {desc_preview}")
            display_list_for_selection.append({"item": item_obj, "equipped": True, "original_index": -1})
            current_selection_idx +=1
    
    UI.print_info("\n--- Carried in Satchel ---")
    carried_items_display = []
    for item_obj in player.stats.inventory:
        is_also_equipped = any(equipped_item == item_obj for equipped_item in player.equipment)
        if not is_also_equipped:
            carried_items_display.append(item_obj)

    if not carried_items_display:
        UI.print_info("Carrying nothing else in your satchel.")
    else:
        for item_obj in carried_items_display:
            desc_preview = item_obj.get_description().split('\n')[0]
            UI.print_info(f"[{current_selection_idx}] {item_obj.name} - {desc_preview}")
            display_list_for_selection.append({"item": item_obj, "equipped": False, "original_index": -1})
            current_selection_idx += 1
        
    return display_list_for_selection


def handle_inventory_menu(player):
    while True:
        clear_screen()
        UI.print_heading("Possessions")
        
        display_entries = display_inventory_with_equipped(player)

        if not display_entries:
            UI.press_enter()
            break
        
        UI.print_line()
        item_choice_input = UI.print_prompt("Select an item to interact with (Number or 0 to go back):")
        
        if not item_choice_input.isdigit():
            UI.slow_print("Invalid input. Please enter a number.")
            UI.press_enter()
            continue

        item_choice_idx_user = int(item_choice_input)
        if item_choice_idx_user == 0:
            break
        
        actual_item_idx_list = item_choice_idx_user - 1

        if 0 <= actual_item_idx_list < len(display_entries):
            selected_entry = display_entries[actual_item_idx_list]
            selected_item_obj = selected_entry["item"]
            is_equipped_flag = selected_entry["equipped"]

            clear_screen()
            UI.print_heading(f"Item Details: {selected_item_obj.name} {'(Equipped)' if is_equipped_flag else ''}")
            print(selected_item_obj.get_description())
            UI.print_line()

            options = []
            if is_equipped_flag:
                options.append("Unequip")
            else:
                options.append("Equip")
                if selected_item_obj.category in ["potion", "food", "scroll", "ingredient"]:
                    options.append("Use")
            
            if not is_equipped_flag:
                options.append("Drop")

            options.append("Back to Inventory List")
            
            UI.print_menu(options)
            action_choice_str = UI.print_prompt("Your choice?")

            chosen_action_text = None
            if action_choice_str.isdigit():
                action_num = int(action_choice_str)
                if 1 <= action_num <= len(options):
                    chosen_action_text = options[action_num-1]
            
            action_performed_this_loop = False
            if chosen_action_text == "Unequip":
                player.unequip_item(selected_item_obj)
                action_performed_this_loop = True
            elif chosen_action_text == "Equip":
                player.equip_item(selected_item_obj)
                action_performed_this_loop = True
            elif chosen_action_text == "Use":
                if selected_item_obj.category in ["potion", "food", "scroll", "ingredient"]:
                    player.use_item(selected_item_obj)
                else:
                    UI.slow_print(f"{selected_item_obj.name} cannot be 'used' in this way now.")
                action_performed_this_loop = True
            elif chosen_action_text == "Drop":
                if not is_equipped_flag:
                    player.drop_item(selected_item_obj)
                else:
                    UI.slow_print(f"You must unequip {selected_item_obj.name} first.")
                action_performed_this_loop = True
            elif chosen_action_text == "Back to Inventory List":
                continue
            else:
                UI.slow_print("Invalid action or choice.")
                action_performed_this_loop = True
            
            if action_performed_this_loop:
                UI.press_enter()
        else:
            UI.slow_print("Invalid selection number.")
            UI.press_enter()

def sort_inventory_menu(player): # This function is not called in game.py from what I can see
    UI.print_subheading("Sort Inventory")
    sort_choice = UI.print_prompt("Sort inventory by [1] Name [2] Category")
    if sort_choice == "1":
        player.stats.inventory.sort(key=lambda item: item.name.lower())
        UI.slow_print("Inventory sorted by name.")
    elif sort_choice == "2":
        player.stats.inventory.sort(key=lambda item: item.category.lower())
        UI.slow_print("Inventory sorted by category.")
    else:
        UI.slow_print("Invalid choice.")
    UI.press_enter()


def handle_item_use(player):
    UI.print_subheading("Use Item from Inventory")
    if not player.stats.inventory:
        UI.slow_print("Your inventory is empty.")
        UI.press_enter()
        return

    usable_items = [item for item in player.stats.inventory if item.category in ["potion", "food", "scroll", "ingredient"]]
    
    if not usable_items:
        UI.slow_print("You have no items that can be readily used in this way.")
        UI.press_enter()
        return

    UI.slow_print("Usable items in your inventory:")
    for i, item in enumerate(usable_items, 1):
        UI.print_info(f"[{i}] {item.name} - Desc: {item.get_description()}")

    try:
        item_choice_input = UI.print_prompt(
            "Which item do you wish to use? (Enter number, 0 to cancel)"
        )
        if not item_choice_input.isdigit():
            UI.slow_print("Invalid input.")
            UI.press_enter()
            return

        item_choice_idx = int(item_choice_input)
        if item_choice_idx == 0:
            UI.slow_print("No item used.")
            UI.press_enter()
            return
        
        if 1 <= item_choice_idx <= len(usable_items):
            selected_item = usable_items[item_choice_idx - 1]
            UI.slow_print(f"You use {selected_item.name}...")
            selected_item.use(player)
        else:
            UI.slow_print("Invalid item number.")
    except ValueError:
        UI.slow_print("Invalid input. Please enter a number.")
    except Exception as e:
        UI.print_failure(f"An error occurred while using item: {e}")
    UI.press_enter()

# --- Player Action Dispatcher ---

def handle_player_choice(choice, player, current_loc_param, menu_options_list):
    action = None
    new_current_location = current_loc_param

    # Determine the action from numeric or text input
    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(menu_options_list):
            action_text = menu_options_list[choice_num - 1]
            action = action_text.split("(")[0].strip().lower()
            if action == "depart this realm":
                return "QUIT_GAME_SIGNAL"
    else:
        action_input_lower = choice.lower()
        for opt_text in menu_options_list:
            opt_action_part = opt_text.split("(")[0].strip().lower()
            if action_input_lower == opt_action_part or action_input_lower in opt_text.lower():
                action = opt_action_part
                if action == "depart this realm":
                    return "QUIT_GAME_SIGNAL"
                break
    
    clear_screen()

    if action == "explore known world":
        new_current_location = explore_and_travel_menu(player, current_loc_param) # Calls the new menu
    elif action == "parley with souls":
        if current_loc_param:
            list_npcs_at_location(current_loc_param, player)
        else:
            UI.slow_print("You must first be somewhere to find others.")
    elif action == "behold thy spirit":
        UI.display_player_stats(player)
    elif action == "test thy steel":
        new_current_location = combat_demo(player, current_loc_param)
    elif action == "inspect thy possessions":
        handle_inventory_menu(player)
    elif action == "look around the area":
        # Pass player to look_around_area
        new_current_location = look_around_area(player, current_loc_param, npc_registry, ALL_LOCATIONS, UI)
    elif action == "review quest log":
        UI.display_quest_log(player)
    elif action == "use item from inventory":
        handle_item_use(player)
    elif action == "wait / pass time":
        UI.slow_print("Time passes...")
        for _ in range(3):
            player.stats.restore_fatigue(max(1, player.stats.level // 2) * 2)
            player.stats.restore_magicka(max(1, player.stats.level // 3) * 2)
        UI.slow_print("You feel somewhat rested.")
    elif action == "depart this realm":
        UI.slow_print(
            "To depart, select the explicit 'Depart This Realm' option "
            "(usually 0 or the last number in the menu)."
        )
        return "QUIT_GAME_SIGNAL"
    else:
        UI.slow_print("Your will wavers, or perhaps the spirits muddle your intent.")

    actions_that_handle_own_prompts = [
        "explore known world",
        "parley with souls",
        "inspect thy possessions",
        "use item from inventory",
        "depart this realm"
    ]
    if action not in actions_that_handle_own_prompts and action is not None:
        UI.press_enter()
        
    return new_current_location


# --- Initialization Functions ---

def initialize_player():
    try:
        clear_screen()
        UI.print_heading("Forge Your Legend")
        UI.slow_print("The scrolls have foretold your arrival, yet your path remains unwritten...")

        # --- Quick-Start / Manual Choice ---
        UI.print_line()
        UI.print_menu(["Manual Character Creation", "Quick Start (Random Character)"])
        creation_choice = UI.print_prompt("Choose your path (1 or 2)")

        # --- Character Creation Logic Starts Here ---
        # The following code will be made conditional based on the choice above.

        player_race_str = "nord"
        player_gender = "male"
        player_name = ""
        selected_class_key = "warrior"
        selected_subclass_key_actual = ""

        if creation_choice == "2": # Quick Start
            UI.slow_print("\nForging a legend from the ether...")

            # Randomly select Race
            race_options = list(RACES.keys())
            player_race_str = random.choice(race_options)
            UI.print_success(f"Lineage: {player_race_str.capitalize()}")

            # Randomly select Gender
            player_gender = random.choice(["male", "female"])
            UI.print_success(f"Form: {player_gender.capitalize()}")

            # Randomly select Name Type and Name
            from npc import NAME_POOLS # Import here to avoid circular dependency
            name_types = ["noble", "commoner"] # Exclude custom for quick start
            random_name_type = random.choice(name_types)
            
            available_ids = NAME_POOLS.get(player_race_str, {}).get(random_name_type, {}).get(player_gender, [])
            if available_ids:
                selected_name_id = random.choice(available_ids)
                player_name = selected_name_id.split('_')[0].capitalize() # Use the name part
                #UI.print_success(f"Name: '{player_name}'") #moved to after surname
            # Randomly select Surname (if applicable to race)
            player_surname = ""
            if player_race_str in NAME_POOLS and (
                "noble_surnames" in NAME_POOLS[player_race_str].get(random_name_type, {})
                or "commoner_surnames" in NAME_POOLS[player_race_str].get(random_name_type, {})
            ):
                available_surnames = [sname.split('_')[0] for sname in NAME_POOLS[player_race_str].get(random_name_type, {}).get(f"{random_name_type}_surnames", [])]
                if available_surnames:
                    player_surname = random.choice(available_surnames)
                    player_name = f"{player_name} {player_surname.capitalize()}"
                    UI.print_success(f"Name: '{player_name}'")
                else:
                    UI.slow_print(f"{player_race_str.capitalize()} do not traditionally use surnames.")
            else:
                UI.print_success(f"Name: '{player_name}'")

            # Randomly select Class
            class_options_keys = list(CLASSES.keys())
            selected_class_key = random.choice(class_options_keys)
            selected_class_data = CLASSES[selected_class_key]
            UI.print_success(f"Path of Skill: {selected_class_data['name']}")

            # Randomly select Sub-class
            subclass_options_keys = list(selected_class_data["subclasses"].keys())
            selected_subclass_key_actual = random.choice(subclass_options_keys)
            selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
            UI.print_success(f"Specialization: {selected_subclass_final_data['name']}")

        else: # Manual Character Creation (Existing Logic)
            UI.slow_print("\nFrom which lineage do you hail?")
            race_options = list(RACES.keys())
            for i, race_name_key in enumerate(race_options):
                race_display_name = race_name_key.capitalize()
                race_bonuses = RACES[race_name_key]
                bonus_descs = []
                if race_bonuses.get("strength_mod"): bonus_descs.append(f"+{race_bonuses['strength_mod']} STR")
                if race_bonuses.get("intelligence_mod"): bonus_descs.append(f"+{race_bonuses['intelligence_mod']} INT")
                if race_bonuses.get("luck_mod"): bonus_descs.append(f"+{race_bonuses['luck_mod']} LCK")
                if race_bonuses.get("magicka_mod"): bonus_descs.append(f"+{race_bonuses['magicka_mod']} Max Magicka")
                if race_bonuses.get("poison_resist",0) > 0: bonus_descs.append(f"{race_bonuses['poison_resist']}% Poison Resist")
                if race_bonuses.get("fire_resist",0) > 0: bonus_descs.append(f"{race_bonuses['fire_resist']}% Fire Resist")
                for key, value in race_bonuses.items():
                    if key.endswith("_skill") and value > 0:
                        bonus_descs.append(f"+{value} {key.replace('_mod','').replace('_skill','').capitalize()}")
                bonus_str = f" ({', '.join(bonus_descs)})" if bonus_descs else ""
                UI.slow_print(f"[{i+1}] {race_display_name}{bonus_str}", speed=0.005)

            while True:
                race_choice_input = UI.print_prompt("Enter the number of your chosen race")
                try:
                    race_index = int(race_choice_input) - 1
                    if 0 <= race_index < len(race_options):
                        player_race_str = race_options[race_index]
                        break
                    else: UI.slow_print("Invalid choice.")
                except ValueError: UI.slow_print("Invalid input.")
            UI.print_success(f"A {player_race_str.capitalize()} you are. Your ancestors watch over you.")

            # 2. Choose Gender
            UI.slow_print("\nWhat is your form?")
            UI.print_menu(["Male", "Female"])

            while player_gender not in ["male", "female"]:
                gender_choice_input = UI.print_prompt("Enter your choice (1 or 2)")
                if gender_choice_input == "1":
                    player_gender = "male"
                elif gender_choice_input == "2":
                    player_gender = "female"
                else:
                    UI.slow_print("Invalid choice. Please enter 1 for Male or 2 for Female.")
            
            UI.print_success(f"You have chosen the form of a {player_gender.capitalize()}.")

            # 3. Choose Social Standing / Name Type
            player_name_type = ""
            while player_name_type not in ["noble", "commoner", "custom"]:
                UI.slow_print("\nName by lineage, common tongue, or your own legend?")
                UI.print_menu(["Noble (names of influence)", "Commoner (everyday names)", "Forge my own name (Custom)"])
                name_type_choice_input = UI.print_prompt("Enter your choice (1, 2, or 3)").strip()

                if name_type_choice_input == "1":
                    player_name_type = "noble"
                elif name_type_choice_input == "2":
                    player_name_type = "commoner"
                elif name_type_choice_input == "3":
                    player_name_type = "custom"
                else:
                    UI.slow_print("Invalid choice. Please select 1, 2, or 3.")
            
            if player_name_type == "custom":
                while not player_name:
                    player_name = UI.print_prompt("Speak your true name, wanderer")
                    if not player_name:
                        UI.slow_print("A name is your first step into legend. Choose wisely.", speed=0.02)
            else:
                # Temporarily pull names from NAME_POOLS for display, extract just the name part
                from npc import NAME_POOLS # Import here to avoid circular dependency
                available_ids = NAME_POOLS.get(player_race_str, {}).get(player_name_type, {}).get(player_gender, [])
                display_names = [name_id.split('_')[0].capitalize() for name_id in available_ids] # Display only the name part
                
                if not display_names:
                    UI.slow_print(f"\nNo specific {player_name_type} names found for a {player_race_str.capitalize()} {player_gender}.")
                    UI.slow_print("You may choose your own name instead.")
                    while True:
                        player_name = UI.print_prompt("Speak your true name, wanderer")
                        if player_name:
                            break
                        else:
                            UI.slow_print("A name is your first step into legend. Choose wisely.", speed=0.02)
                else:
                    UI.slow_print(f"\nNames of your people ({player_name_type} {player_gender}):")
                    for i, name_opt in enumerate(display_names):
                        UI.slow_print(f"[{i+1}] {name_opt}", speed=0.005)
                    UI.slow_print(f"[{len(display_names)+1}] Choose my own name (Custom)")

                    while True:
                        name_choice_input = UI.print_prompt("Enter the number of your chosen name")
                        try:
                            name_index = int(name_choice_input) - 1
                            if 0 <= name_index < len(display_names):
                                player_name = display_names[name_index]
                                break
                            elif name_index == len(display_names):
                                player_name = UI.print_prompt("Speak your true name, wanderer")
                                if not player_name:
                                    UI.slow_print("A name is your first step into legend. Choose wisely.", speed=0.02)
                                else:
                                    break
                            else:
                                UI.slow_print("Invalid choice. Please enter a number from the list.")
                        except ValueError:
                            UI.slow_print("Invalid input. Please enter a number.")
                    player_name = player_name.capitalize() # Capitalize the chosen name

            # 3a. Choose Surname (if applicable to race)
            player_surname = ""
            if player_race_str in NAME_POOLS and any([
                "noble_surnames" in NAME_POOLS[player_race_str].get(player_name_type, {})
                or "commoner_surnames" in NAME_POOLS[player_race_str].get(player_name_type, {})
            ]):
                UI.slow_print("\nChoose your family's legacy, or forge a new one:")
                surname_type = player_name_type  # Use the same name type (noble/commoner) for surnames
                available_surnames = (
                    NAME_POOLS[player_race_str]
                    .get(surname_type, {})
                    .get(f"{surname_type}_surnames", [])
                )
                display_surnames = [surname.replace('_',' ').title().split(' ')[0] for surname in available_surnames]
                if not display_surnames:
                    UI.slow_print(
                        f"\nNo specific {surname_type} surnames found for a {player_race_str.capitalize()}."
                    )
                    player_surname = UI.print_prompt("What surname will you carry?")
                else:
                    UI.slow_print(f"\nSurnames of your people ({surname_type} lineage):")
                    for i, surname_opt in enumerate(display_surnames):
                        UI.slow_print(f"[{i+1}] {surname_opt}", speed=0.005)
                    UI.slow_print(f"[{len(display_surnames)+1}] Choose my own surname (Custom)")

                    while True:
                        surname_choice_input = UI.print_prompt("Enter the number of your chosen surname")
                        try:
                            surname_index = int(surname_choice_input) - 1
                            if 0 <= surname_index < len(display_surnames):
                                player_surname = display_surnames[surname_index]
                            elif surname_index == len(display_surnames):
                                player_surname = UI.print_prompt("Speak your family's name, wanderer")
                            else:
                                UI.slow_print("Invalid choice. Please enter a number from the list.")
                        except ValueError:
                            UI.slow_print("Invalid input. Please enter a number.")
                        break # Exit loop after a valid choice or custom input
            else:
                UI.slow_print(f"\n{player_race_str.capitalize()} do not traditionally use surnames.")

            if player_surname:
                player_surname = player_surname.capitalize()
                player_name = f"{player_name} {player_surname}"
                UI.print_success(f"'{player_name}'... a name that will be whispered through the ages.")
            else:
                UI.print_success(f"'{player_name}'... a name carried with honor.")

            # 4. Choose Class (Path of Skill)
            UI.slow_print("\nWhat path of skill do you tread?")
            class_options_keys = list(CLASSES.keys())
            for i, class_id_key in enumerate(class_options_keys):
                class_data = CLASSES[class_id_key]
                UI.slow_print(f"[{i+1}] {class_data['name']} - {class_data['desc']}", speed=0.005)

            selected_class_key = "warrior"
            selected_class_data = CLASSES[selected_class_key]
            while True:
                class_choice_input = UI.print_prompt("Choice")
                try:
                    class_index = int(class_choice_input) - 1
                    if 0 <= class_index < len(class_options_keys):
                        selected_class_key = class_options_keys[class_index]
                        selected_class_data = CLASSES[selected_class_key]
                        break
                    else: UI.slow_print("Invalid choice.")
                except ValueError: UI.slow_print("Invalid input.")
            UI.print_success(f"The path of the {selected_class_data['name']} chosen.")

            UI.slow_print(f"\nWithin {selected_class_data['name']}, which specialization calls?")
            subclass_options_map = {str(idx+1): sc_key for idx, sc_key in enumerate(selected_class_data["subclasses"].keys())}
            for display_num, sc_id_key in subclass_options_map.items():
                subclass_item_data = selected_class_data["subclasses"][sc_id_key]
                attr_str = ", ".join([f"{k.capitalize()[:3]}: {v}" for k,v in subclass_item_data["attributes"].items()])
                skill_str = ", ".join([f"{k.replace('_',' ').capitalize()}: {v}" for k,v in subclass_item_data["skills"].items()])
                inv_str = ", ".join([name.replace('_', ' ').title() for name in subclass_item_data["inventory"]])
                UI.slow_print(f"[{display_num}] {subclass_item_data['name']}", speed=0.005)
                UI.slow_print(f"    Attrs: {attr_str}", speed=0.005)
                UI.slow_print(f"    Skills: {skill_str}", speed=0.005)
                UI.slow_print(f"    Gear: {inv_str}", speed=0.005)

            selected_subclass_key_actual = list(selected_class_data["subclasses"].keys())[0]
            selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
            while True:
                subclass_choice_input_str = UI.print_prompt("Choice")
                if subclass_choice_input_str in subclass_options_map:
                    selected_subclass_key_actual = subclass_options_map[subclass_choice_input_str]
                    selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
                    break
                else: UI.slow_print("Invalid choice.")
            UI.print_success(f"You are now a {selected_subclass_final_data['name']}.")

        # Create Player instance using selected data
        selected_class_data = CLASSES[selected_class_key] # Ensure this is set correctly after choice
        selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual] # Ensure this is set correctly after choice

        base_stats_params = selected_class_data.get("attributes", {}).copy()
        base_stats_params.update(selected_subclass_final_data["attributes"])

        # Apply racial modifiers
        race_mods = RACES[player_race_str]
        for attr, mod_val in race_mods.items():
            if attr.endswith("_mod") and attr.replace("_mod","") in base_stats_params:
                stat_name = attr.replace("_mod","")
                base_stats_params[stat_name] = base_stats_params.get(stat_name, 40) + mod_val
            elif attr.endswith("_resist"):
                base_stats_params[attr] = mod_val
            elif attr == "magicka_mod":
                base_stats_params["max_magicka_bonus"] = mod_val

        player_stats_instance = Stats(
            strength=base_stats_params.get("strength", 40),
            intelligence=base_stats_params.get("intelligence", 40),
            willpower=base_stats_params.get("willpower", 40),
            agility=base_stats_params.get("agility", 40),
            speed=base_stats_params.get("speed", 40),
            endurance=base_stats_params.get("endurance", 40),
            personality=base_stats_params.get("personality", 40),
            luck=base_stats_params.get("luck", 40),
            poison_resist=base_stats_params.get("poison_resist",0),
            magic_resist=base_stats_params.get("magic_resist",0),
            frost_resist=base_stats_params.get("frost_resist",0),
            shock_resist=base_stats_params.get("shock_resist",0),
            fire_resist=base_stats_params.get("fire_resist",0),
            level=1, gold=50
        )
        if "max_magicka_bonus" in base_stats_params:
            player_stats_instance.max_magicka += base_stats_params["max_magicka_bonus"]
            player_stats_instance.current_magicka = player_stats_instance.max_magicka


        player_skills = selected_subclass_final_data["skills"].copy()
        # Apply racial skill bonuses
        for skill_key, bonus_value in race_mods.items():
            if skill_key.endswith("_skill"):
                actual_skill_name = skill_key.replace("_skill", "")
                player_skills[actual_skill_name] = player_skills.get(actual_skill_name, 5) + bonus_value

        starting_spell_keys_for_subclass = selected_subclass_final_data.get("starting_spells", [])

        player = Player(
            name=player_name,
            race=player_race_str,
            subclass_name=selected_subclass_final_data["name"], # Pass subclass_name
            stats_instance=player_stats_instance,
            skills=player_skills,
            starting_spell_keys=starting_spell_keys_for_subclass # Pass starting spell keys
        )
        player.combat = None
        # Initialize player's known locations (will be populated by initialize_starting_location)
        player.known_location_ids = set()
        player.known_locations_objects = []


        UI.slow_print("Preparing your starting gear...")
        for item_key_from_subclass in selected_subclass_final_data["inventory"]:
           item_instance = generate_item_from_key(item_key_from_subclass, player.stats.level)
           if item_instance:
                if player.add_item(item_instance):
                    if item_instance.category in ["weapon", "armor"]:
                        player.equip_item(item_instance)
                else:
                    UI.print_warning(f"Could not add starting item {item_instance.name} (inventory full or error).")
           else:
                UI.print_warning(f"Could not generate starting item for key: {item_key_from_subclass}")

        if player.stats.inventory: UI.slow_print(f"In your satchel: {', '.join([item.name for item in player.stats.inventory if item not in player.equipment])}.", speed=0.01)
        if player.equipment: UI.slow_print(f"Equipped: {', '.join([eq.name for eq in player.equipment])}.", speed=0.01)
        else: UI.slow_print("You start with no items equipped.", speed=0.01)

        player.quest_log = QuestLog()
        UI.print_line()
        UI.slow_print("Your journey begins...", speed=0.02)
        UI.press_enter()
        return player

    except Exception as e:
        UI.print_failure(f"Error in initialize_player: {e}")
        traceback.print_exc()
        return None

def initialize_starting_location(player: Player): # Pass player object
    # global known_locations, known_locations_objects, ALL_LOCATIONS # Globals no longer needed here for known_locations
    start_tavern_name = "The Bannered Mare"
    start_city_name = "Whiterun"
    start_hold_name = "Whiterun Hold"

    starting_loc_obj = None
    parent_city_obj = None
    parent_hold_obj = None

    # Find parent hold
    parent_hold_obj = next((h for h in ALL_LOCATIONS if h["name"] == start_hold_name), None)
    if not parent_hold_obj:
        UI.print_warning(f"Starting hold '{start_hold_name}' not found. Defaulting.")
        parent_hold_obj = ALL_LOCATIONS[0] # Fallback

    # Find parent city within the hold
    if parent_hold_obj and "sub_locations" in parent_hold_obj:
        parent_city_obj = next((c for c in parent_hold_obj["sub_locations"] if c["name"] == start_city_name), None)
    
    if not parent_city_obj: # Fallback if city not found in hold, or hold had no sub_locations
        UI.print_warning(f"Starting city '{start_city_name}' in {parent_hold_obj['name']} not found. Defaulting to hold or first city.")
        # Ensure parent_city_obj is a location dictionary even in fallback
        parent_city_obj = parent_hold_obj.get("sub_locations", [parent_hold_obj])[0] if parent_hold_obj.get("sub_locations") else parent_hold_obj


    # Find starting location (tavern) within the city
    if parent_city_obj and "sub_locations" in parent_city_obj:
        starting_loc_obj = next((v for v in parent_city_obj["sub_locations"] if v["name"] == start_tavern_name), None)
    
    if not starting_loc_obj: # Fallback if tavern not found in city, or city had no sub_locations
        UI.print_warning(f"Starting tavern '{start_tavern_name}' in {parent_city_obj['name']} not found. Starting in city.")
        starting_loc_obj = parent_city_obj

    # --- Initial Discovery Enhancement ---
    # Always add the hold, city, and specific start point
    # Populate player's known locations directly
    for loc_obj in [parent_hold_obj, parent_city_obj, starting_loc_obj]:
        if loc_obj and loc_obj["id"] not in player.known_location_ids:
            player.known_location_ids.add(loc_obj["id"])
            if loc_obj not in player.known_locations_objects:
                 player.known_locations_objects.append(loc_obj)

   



    # Discover locations connected by travel from the hold and city
    if parent_hold_obj:
        discover_connected_locations(player, parent_hold_obj)

    # If the city itself has travel links
    if parent_city_obj and parent_city_obj["id"] != parent_hold_obj["id"]:
        discover_connected_locations(player, parent_city_obj)

    # Discover all sub-locations within the starting city
    if parent_city_obj and "sub_locations" in parent_city_obj:
        for sub_loc_in_city in parent_city_obj["sub_locations"]:
            if sub_loc_in_city["id"] not in player.known_location_ids:
                player.known_location_ids.add(sub_loc_in_city["id"])
                if sub_loc_in_city not in player.known_locations_objects:
                    player.known_locations_objects.append(sub_loc_in_city)

    # Discover all direct sub-locations of the starting Hold
    if parent_hold_obj and "sub_locations" in parent_hold_obj:
        for sub_loc_in_hold in parent_hold_obj["sub_locations"]:
            if sub_loc_in_hold["id"] not in player.known_location_ids:
                player.known_location_ids.add(sub_loc_in_hold["id"])
                if sub_loc_in_hold not in player.known_locations_objects: # Ensure no duplicates in list
                    player.known_locations_objects.append(sub_loc_in_hold)

    # Discover connections from the specific starting location
    if starting_loc_obj and starting_loc_obj["id"] != parent_city_obj["id"]:
         discover_connected_locations(player, starting_loc_obj)


    message = f"You awaken in {starting_loc_obj['name']}, a seemingly cozy establishment in {parent_city_obj['name']}, within the lands of {parent_hold_obj['name']}..."
    UI.slow_print(message)
    
    UI.slow_print(starting_loc_obj['desc'])
    UI.slow_print("The warm fire crackles. A few patrons murmur over their drinks. Adventure awaits.")
    
    generate_npcs_for_location(starting_loc_obj) #
    return starting_loc_obj

def initialize_game_state(player: Player): # Pass player to clear its known locations
    global game_start_time, npc_registry # npc_registry is still global for now
    game_start_time = datetime.now(timezone.utc)
    player.known_location_ids.clear()
    player.known_locations_objects.clear()
    npc_registry.clear()

# --- Main Game Loop ---

def start_game():
    current_location_global = None
    try:
        player = initialize_player() # Player is created first
        if not player:
            UI.print_failure("Failed to initialize player. Exiting.")
            return

        initialize_game_state(player) # Then game state (including player's known locs) is cleared/set up

        current_location_global = initialize_starting_location(player) # Pass player to init starting loc
        player.update_current_location_for_quest(current_location_global)
        # player.known_locations_objects is already managed by the player object itself now.
        
        main_loop_running = True
        while main_loop_running:
            if not player.stats.is_alive():
                UI.print_heading("Your Legend Ends Here")
                UI.slow_print(f"{player.full_name} has fallen...")
                break

            player.stats.restore_fatigue(max(1, player.stats.level // 2))
            player.stats.restore_magicka(max(1, player.stats.level // 3))

            # Check active quests for completion at the start of each turn
            for quest in player.quest_log.active_quests:
                # Update current stage progress based on player's current state
                if quest.current_stage and not quest.check_all_current_stage_objectives_met(player):
                    for obj in quest.current_stage.get("objectives", []):
                        quest.check_objective_met(obj, player) # Update progress for each objective

                if quest.check_all_current_stage_objectives_met(player):
                    if quest.current_stage_index + 1 < len(quest.stages):
                        UI.print_system_message(f"QUEST STAGE COMPLETE for '{quest.title}'! Advancing to next stage.")
                        quest.advance_quest_stage()
                    else:
                        UI.print_system_message(f"QUEST OBJECTIVES MET for '{quest.title}'! Return to {LOCATION_BY_ID.get(quest.turn_in_npc_id.split('_')[0],{}).get('name', 'your quest giver')} to turn in.")
                        quest.status = "completed" # Explicitly set status to completed after all stages are met

            if player.stats.current_encumbrance > player.stats.encumbrance_limit:
                UI.slow_print("Your heavy load weighs you down.", speed=0.005)
            
            UI.print_line('=')
            time_now = datetime.now(timezone.utc)
            game_elapsed_seconds = (time_now - game_start_time).total_seconds()
            game_days = int(game_elapsed_seconds // (60*5))
            game_hours = int((game_elapsed_seconds % (60*5)) // (60*5/24))
            time_of_day_str = "Morning"
            if 5 <= game_hours < 12: time_of_day_str = "Morning"
            elif 12 <= game_hours < 17: time_of_day_str = "Afternoon"
            elif 17 <= game_hours < 21: time_of_day_str = "Evening"
            else: time_of_day_str = "Night"

            UI.print_info(f"Location: {current_location_global['name']} | Day: {game_days+1}, {time_of_day_str}")
            UI.print_info(f"HP: {player.stats.current_health}/{player.stats.max_health} MP: {player.stats.current_magicka}/{player.stats.max_magicka} ST: {player.stats.current_fatigue}/{player.stats.max_fatigue}")
            UI.print_info(f"XP: {player.experience}/{player.next_level_exp} | Level: {player.level}")
            UI.print_line('=')

            menu_options = [
                "Explore Known World (Map & Travel)",
                "Parley with Souls (Interact)",
                "Behold Thy Spirit (Stats)",
                "Test Thy Steel (Combat Demo)",
                "Inspect Thy Possessions (Inv)",
                "Look Around the Area",
                "Review Quest Log",
                "Use Item from Inventory",
                "Wait / Pass Time",
                "Depart This Realm (Quit)"
            ]
            UI.print_menu(menu_options)

            choice = UI.print_prompt(f"{player.name}, what is your will? ").strip()

            is_quit_option = False
            numeric_choice = -1
            if choice.isdigit():
                numeric_choice = int(choice)

            if choice == "0" or (numeric_choice == len(menu_options) and "depart this realm" in menu_options[-1].lower()):
                is_quit_option = True
            
            if is_quit_option:
                UI.slow_print("Farewell, until the stars call you back to Skyrim!")
                main_loop_running = False
                continue

            new_location_or_state = handle_player_choice(choice, player, current_location_global, menu_options)
            
            if new_location_or_state == "QUIT_GAME_SIGNAL":
                UI.slow_print("Farewell, until the stars call you back to Skyrim!")
                main_loop_running = False
                continue
            elif isinstance(new_location_or_state, dict) and "id" in new_location_or_state :
                 current_location_global = new_location_or_state
            
            player.update_current_location_for_quest(current_location_global) # Update player's current location object
            
            # Simplified event trigger: still calls trigger_random_event
            if main_loop_running and current_location_global and random.random() < 0.10:
                UI.print_line('.')
                UI.slow_print("The winds of fate shift...")
                # The trigger_random_event function itself should handle UI and potential effects
                trigger_random_event(current_location_global.get("tags",[]), player, UI, current_location_global)
                UI.press_enter()

    except KeyboardInterrupt:
        UI.print_system_message("\nJourney paused by the threads of fate. Farewell for now.")
    except Exception as e:
        UI.print_failure(f"\nA catastrophic tear in the fabric of Mundus! Error: {e}")
        traceback.print_exc()
    finally:
        UI.print_system_message("The world fades... Press Enter to return to reality.")
        input()
        
if __name__ == "__main__":
    start_game()
