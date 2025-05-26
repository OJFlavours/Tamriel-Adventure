# game.py

import time
import random
import traceback
from datetime import datetime, timezone

try:
    from locations import LOCATIONS
    from stats import Player, Stats, RACES, CLASSES
    from npc import NPC, FRIENDLY_ROLES, HOSTILE_ROLES, NAME_POOLS # Ensure NAME_POOLS is available if NPC needs it directly
    from combat import Combat
    from ui import UI
    from items import generate_random_item, Item, generate_item_from_key
    from events import trigger_random_event, explore_location # Make sure explore_location is correctly used/defined
    from quests import (
        # list_player_quests, # This function was noted as possibly redundant if using player.quest_log directly
        QuestLog,
        generate_location_appropriate_quest,
        generate_reward
    )
    import tags # Ensure tags.py is correctly imported and used
    import flavor # Ensure flavor.py is correctly imported and used
except ImportError as e:
    print(f"Error importing modules: {e}")
    traceback.print_exc() # Print full traceback for import errors
    input("Press Enter to exit...")
    exit(1)

# Globals
known_locations = set()
npc_registry = {}
# random_encounters = {} # This seemed to be a placeholder; dynamic encounters are now handled differently
game_start_time = None

ALL_LOCATIONS = LOCATIONS

# Build lookups for fast name/id resolution
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

ENCOUNTER_NAMES = {
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
    # Add more encounter types based on location tags
}
# Utility
def clear_screen():
    UI.clear_screen()

def get_flavor_text(tags_list_param, category, ensure_vignette=False):
    if not tags_list_param:
        return ""
    tags_filtered = [t for t in tags_list_param if isinstance(t, (str, int, float))]

    class DummyEntity:
        def __init__(self, final_tags_list, category_):
            self.tags = {}
            # Try to match structure expected by flavor.py, based on provided tags.py
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
            else: # Generic fallback
                self.tags[category_] = final_tags_list
    
    entity = DummyEntity(tags_filtered, category)
    vignettes = flavor.get_flavor(entity) if hasattr(flavor, 'get_flavor') else []
    if not vignettes and ensure_vignette:
        return "The air is thick with untold stories."
    return random.choice(vignettes) if vignettes else ""


def discover_connected_locations(location):
    global known_locations
    for mode in ("roads", "paths"):
        for dest_name in location.get("travel", {}).get(mode, []):
            dest_loc = LOCATION_BY_NAME.get(dest_name)
            if dest_loc:
                known_locations.add(dest_loc["id"])

def generate_random_encounter(location_tags_list):
    if not location_tags_list:
        return None
    
    string_tags = [t for t in location_tags_list if isinstance(t, str) and t in ENCOUNTER_NAMES]
    pool = []
    for t in string_tags:
        pool.extend(ENCOUNTER_NAMES[t])
        
    if not pool:
        if any(fallback_tag in location_tags_list for fallback_tag in ["wilderness", "forest", "mountain", "plains"]):
             pool.extend(ENCOUNTER_NAMES.get("forest", []) + ENCOUNTER_NAMES.get("plains", []))

    if not pool:
        return None
        
    enc_data = random.choice(pool)
    return {
        "id": f"enc_{random.randint(10000, 99999)}",
        "name": enc_data["name"],
        "desc": enc_data["desc"],
        "tags": list(set(location_tags_list + [enc_data["type"]])),
        "is_encounter": True 
    }

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


def explore_and_travel_menu(player, current_location_param):
    """
    Displays all known locations hierarchically.
    Allows player to select a location to either examine in detail or travel to.
    """
    while True: 
        clear_screen()
        UI.print_heading("Explore Known World (Map & Travel)")
        UI.print_info(f"You are currently at: {current_location_param['name']}")
        UI.print_line()

        if not known_locations:
            UI.slow_print("Your map remains blank, a world yet to be charted.")
            UI.print_line()
            UI.press_enter()
            return current_location_param

        display_map = {} 
        details_map = {} 

        sorted_known_holds = sorted(
            (loc for loc in ALL_LOCATIONS if "hold" in loc.get("tags", []) and loc["id"] in known_locations),
            key=lambda x: x["name"]
        )

        major_loc_counter = 0
        for hold_obj in sorted_known_holds:
            major_loc_counter += 1
            hold_num_str = str(major_loc_counter)
            display_map[hold_num_str] = hold_obj
            details_map[hold_num_str] = {"parent_name": None, "type": "Hold"}

            city_counter = 0
            sorted_cities_in_hold = sorted(
                (sub for sub in hold_obj.get("sub_locations", []) if sub["id"] in known_locations),
                key=lambda x: x["name"]
            )
            for city_obj in sorted_cities_in_hold:
                city_counter += 1
                city_num_str = f"{hold_num_str}.{city_counter}"
                display_map[city_num_str] = city_obj
                city_type = "City" # Default
                if "town" in city_obj.get("tags", []): city_type = "Town"
                elif "village" in city_obj.get("tags", []): city_type = "Village"
                elif any(t in city_obj.get("tags", []) for t in ["dungeon", "barrow", "cave", "ruin", "camp", "mine"]): city_type = "Site"
                details_map[city_num_str] = {"parent_name": hold_obj["name"], "type": city_type}

                venue_counter = 0
                sorted_venues_in_city = sorted(
                    (v for v in city_obj.get("sub_locations", []) if v["id"] in known_locations),
                    key=lambda x: x["name"]
                )
                for venue_obj in sorted_venues_in_city:
                    venue_counter += 1
                    venue_num_str = f"{city_num_str}.{venue_counter}"
                    display_map[venue_num_str] = venue_obj
                    venue_type = "Point of Interest" # Default
                    if "tavern" in venue_obj.get("tags", []): venue_type = "Tavern"
                    elif "shop" in venue_obj.get("tags", []): venue_type = "Shop"
                    elif "keep" in venue_obj.get("tags", []): venue_type = "Keep"
                    elif "temple" in venue_obj.get("tags", []): venue_type = "Temple"
                    details_map[venue_num_str] = {"parent_name": city_obj["name"], "type": venue_type}
        
        if not display_map:
            UI.slow_print("You know of no specific mapped locations beyond your immediate surroundings.")
            UI.press_enter()
            return current_location_param

        UI.print_subheading("Known Locations:")
        try:
            sorted_map_keys = sorted(display_map.keys(), key=lambda x: tuple(map(int, x.split('.'))))
        except ValueError: # Handle cases like "enc_1" if they sneak in
            sorted_map_keys = sorted(display_map.keys())


        for num_str in sorted_map_keys:
            loc_obj_to_display = display_map[num_str]
            indent_level = num_str.count('.')
            indent = "  " * indent_level 
            brief_desc = loc_obj_to_display["desc"].split(".")[0] + "."
            type_display = details_map[num_str]["type"]
            UI.print_info(f"{indent}[{num_str}] {loc_obj_to_display['name']:<30} ({type_display}) — {brief_desc}")
        UI.print_line()

        loc_choice_str = UI.print_prompt("Enter location number to interact with (or 0 to go back)")

        if loc_choice_str == "0":
            return current_location_param 

        if loc_choice_str in display_map:
            selected_loc_obj_for_action = display_map[loc_choice_str]
            selected_loc_details_for_action = details_map[loc_choice_str]
            
            action_result_loc = prompt_examine_or_travel(
                selected_loc_obj_for_action,
                selected_loc_details_for_action,
                player,
                current_location_param,
                loc_choice_str 
            )
            
            if action_result_loc == "REPROMPT_MAP": 
                continue 
            elif isinstance(action_result_loc, dict) and "id" in action_result_loc: 
                return action_result_loc 
            # else if None or error, loop to reprompt map implicitly
        else:
            UI.slow_print("Invalid location number. Please try again.")
            UI.press_enter()

def prompt_examine_or_travel(loc_to_interact, loc_details, player, current_location, selection_prefix_str):
    """
    Prompts player to either Examine or Travel to the selected location.
    Returns new current_location if travel occurs, "REPROMPT_MAP" to show map again, or current_location if no change.
    """
    while True:
        clear_screen()
        UI.print_heading(f"Location: {loc_to_interact['name']}")
        UI.print_info(f"Type: {loc_details['type']}")
        if loc_details['parent_name']:
            UI.print_info(f"Part of: {loc_details['parent_name']}")
        UI.print_line('-')
        UI.slow_print(loc_to_interact['desc']) 
        UI.print_line('-')

        UI.print_menu([
            "Examine in More Detail",
            "Travel to this Location",
            "Back to Map"
        ])
        action_choice = UI.print_prompt("Choose action (1, 2, or 0)")

        if action_choice == "1": 
            clear_screen()
            UI.print_heading(f"Examining: {loc_to_interact['name']}")
            UI.print_info(f"Full Description: {loc_to_interact['desc']}")
            UI.print_info(f"Tags: {', '.join(loc_to_interact.get('tags', []))}")
            if loc_details['parent_name']:
                UI.print_info(f"Context: Located within {loc_details['parent_name']}.")

            known_sub_locations_names = [
                sub['name'] for sub in loc_to_interact.get("sub_locations", []) if sub["id"] in known_locations
            ]
            if known_sub_locations_names:
                UI.print_subheading("Known Sub-Locations / Points of Interest Here:")
                for name in known_sub_locations_names:
                    UI.print_info(f"- {name}")
            
            npcs_at_this_loc = [npc.name for npc in npc_registry.get(loc_to_interact["id"], []) if npc.stats.is_alive()]
            if npcs_at_this_loc:
                UI.print_subheading("Known Souls Present:")
                for name in npcs_at_this_loc:
                    UI.print_info(f"- {name}")
            else:
                UI.print_info("You observe no one of particular note here at the moment.")
            
            UI.press_enter()
            return "REPROMPT_MAP" 

        elif action_choice == "2": 
            return enter_location_or_prompt_sub(loc_to_interact, player, current_location, selection_prefix_str)

        elif action_choice == "0": 
            return "REPROMPT_MAP"
        else:
            UI.slow_print("Invalid choice. Please select an option.")
            UI.press_enter()


def enter_location_or_prompt_sub(chosen_destination, player, previous_location, selection_prefix):
    global known_locations 

    known_locations.add(chosen_destination["id"])
    discover_connected_locations(chosen_destination) 

    known_sub_locs = [
        sub for sub in chosen_destination.get("sub_locations", []) if sub["id"] in known_locations
    ]

    if known_sub_locs: 
        clear_screen()
        UI.print_heading(f"Realms Within {chosen_destination['name']}")
        
        sub_option_map = {}
        explore_container_option_num = f"{selection_prefix}.0"
        UI.print_info(f"[{explore_container_option_num}] Explore {chosen_destination['name']} itself")
        sub_option_map[explore_container_option_num] = chosen_destination

        sorted_known_sub_locs = sorted(known_sub_locs, key=lambda x: x["name"])
        for i, sub_loc_item in enumerate(sorted_known_sub_locs, start=1):
            display_num = f"{selection_prefix}.{i}"
            brief_desc = sub_loc_item["desc"].split(".")[0] + "."
            
            sub_loc_type = "Point of Interest" # Default type for sub-locations
            if "tavern" in sub_loc_item.get("tags",[]): sub_loc_type = "Tavern"
            elif "shop" in sub_loc_item.get("tags",[]): sub_loc_type = "Shop"
            elif "keep" in sub_loc_item.get("tags",[]): sub_loc_type = "Keep"
            elif "temple" in sub_loc_item.get("tags",[]): sub_loc_type = "Temple"
            elif "guild" in sub_loc_item.get("tags",[]): sub_loc_type = "Guild Hall"


            UI.print_info(f"[{display_num}] {sub_loc_item['name']:<30} ({sub_loc_type}) — {brief_desc}")
            sub_option_map[display_num] = sub_loc_item
        UI.print_line()

        sub_sel = UI.print_prompt(f"Your choice? (00 to cancel and return to {previous_location['name']})").strip()

        if sub_sel == "00":
            return previous_location

        if sub_sel in sub_option_map:
            final_destination = sub_option_map[sub_sel]
            
            if final_destination["id"] == chosen_destination["id"]: 
                UI.slow_print(f"You focus your attention on {final_destination['name']}.")
            else: 
                UI.slow_print(f"You venture into {final_destination['name']} (within {chosen_destination['name']}).")
            
            UI.slow_print(final_destination["desc"])

            tags_for_final_dest = list(final_destination.get("tags", [])) 
            inheritable = {"nordic","imperial","stormcloak","thieves","corrupt","military","bards","city","town","village","hold", "plains", "central", "snow", "coastal", "magic", "marsh", "swamp", "forest", "southern", "mountain", "dwemer", "volcanic", "water"}

            immediate_parent_for_tags = None
            if final_destination["id"] != chosen_destination["id"]:
                immediate_parent_for_tags = chosen_destination
            else:
                parent_hold, parent_city = _find_hierarchy(final_destination["id"])
                if parent_city and parent_city["id"] == final_destination["id"]: 
                    immediate_parent_for_tags = parent_hold 
            
            if immediate_parent_for_tags:
                tags_for_final_dest.extend([t for t in immediate_parent_for_tags.get("tags", []) if t in inheritable])
            tags_for_final_dest = list(set(tags_for_final_dest))

            UI.slow_print(get_flavor_text(tags_for_final_dest, "location_tags", ensure_vignette=True))
            trigger_random_event(tags_for_final_dest, player, UI, final_destination)
            generate_npcs_for_location(final_destination) 
            return final_destination
        else: # Invalid sub-selection, land them in the container
            UI.slow_print(f"Path unknown within {chosen_destination['name']}. You remain in {chosen_destination['name']} for now.")
            # UI.slow_print(chosen_destination["desc"]) # Already printed if they selected it.
            
            parent_hold_for_container, _ = _find_hierarchy(chosen_destination["id"])
            container_tags = list(chosen_destination.get("tags", []))
            inheritable = {"nordic","imperial","stormcloak","thieves","corrupt","military","bards","city","town","village","hold", "plains", "central", "snow", "coastal", "magic", "marsh", "swamp", "forest", "southern", "mountain", "dwemer", "volcanic", "water"}
            if parent_hold_for_container and parent_hold_for_container["id"] != chosen_destination["id"]:
                 container_tags.extend([t for t in parent_hold_for_container.get("tags", []) if t in inheritable])
            container_tags = list(set(container_tags))

            UI.slow_print(get_flavor_text(container_tags, "location_tags", ensure_vignette=True))
            trigger_random_event(container_tags, player, UI, chosen_destination)
            generate_npcs_for_location(chosen_destination)
            return chosen_destination
            
    else: 
        UI.slow_print(f"You travel to {chosen_destination['name']}.")
        UI.slow_print(chosen_destination["desc"])

        parent_hold, parent_city = _find_hierarchy(chosen_destination["id"])
        tags_for_chosen_dest = list(chosen_destination.get("tags", []))
        inheritable = {"nordic","imperial","stormcloak","thieves","corrupt","military","bards","city","town","village","hold", "plains", "central", "snow", "coastal", "magic", "marsh", "swamp", "forest", "southern", "mountain", "dwemer", "volcanic", "water"}
        
        primary_parent_for_tags = None
        if parent_city and parent_city["id"] != chosen_destination["id"] and any(sub["id"] == chosen_destination["id"] for sub in parent_city.get("sub_locations",[])):
            primary_parent_for_tags = parent_city
        elif parent_hold and parent_hold["id"] != chosen_destination["id"] and any(sub["id"] == chosen_destination["id"] for sub in parent_hold.get("sub_locations",[])):
            primary_parent_for_tags = parent_hold
        
        if primary_parent_for_tags:
             tags_for_chosen_dest.extend([t for t in primary_parent_for_tags.get("tags", []) if t in inheritable])
        tags_for_chosen_dest = list(set(tags_for_chosen_dest))

        UI.slow_print(get_flavor_text(tags_for_chosen_dest, "location_tags", ensure_vignette=True))
        trigger_random_event(tags_for_chosen_dest, player, UI, chosen_destination)
        generate_npcs_for_location(chosen_destination)
        return chosen_destination

# NPC generation functions
def generate_npcs_for_location(location_obj): 
    try:
        if location_obj.get("is_encounter"): 
            return

        # Check if NPCs should be (re)generated based on a timer or visit count, for now, only once.
        if location_obj["id"] in npc_registry and npc_registry[location_obj["id"]]: # If NPCs exist, don't regenerate unless logic changes
            return

        npc_registry[location_obj["id"]] = [] 
        
        parent_hold, parent_city = _find_hierarchy(location_obj["id"])
        combined_tags_for_npc_gen = list(location_obj.get("tags", []))
        inheritable_npc_context_tags = {
            "nordic", "imperial", "stormcloak", "thieves", "corrupt", "college", "companions", "darkbrotherhood",
            "military", "bards", "city", "town", "village", "hold", "dwemer", "forsworn", "undead", "vampire", "mage_guild"
        } 

        contextual_parent = None
        if parent_city and parent_city["id"] != location_obj["id"] and any(sub_loc["id"] == location_obj["id"] for sub_loc in parent_city.get("sub_locations", [])): 
            contextual_parent = parent_city
        elif parent_hold and parent_hold["id"] != location_obj["id"] and any(sub_loc["id"] == location_obj["id"] for sub_loc in parent_hold.get("sub_locations", [])): 
            contextual_parent = parent_hold

        if contextual_parent:
            combined_tags_for_npc_gen.extend([
                t for t in contextual_parent.get("tags", []) if t in inheritable_npc_context_tags
            ])
        combined_tags_for_npc_gen = list(set(combined_tags_for_npc_gen)) # Remove duplicates
        
        demographics_source = location_obj
        if not demographics_source.get("demographics"):
            if contextual_parent and contextual_parent.get("demographics"):
                demographics_source = contextual_parent
            elif parent_hold and parent_hold.get("demographics"):
                 demographics_source = parent_hold
        demographics = demographics_source.get("demographics", {"Nord": 100}) 

        npc_count = determine_npc_count(combined_tags_for_npc_gen)
        
        role_pool = set(FRIENDLY_ROLES) 
        hostile_location_indicators = ["bandit", "dungeon", "ruin", "forsworn", "necromancer", "vampire_lair", "monster_den", "lair"]
        if any(indicator in combined_tags_for_npc_gen for indicator in hostile_location_indicators) or \
           any(indicator in location_obj.get("name","").lower() for indicator in hostile_location_indicators): # Check name too
            role_pool.update(HOSTILE_ROLES)
        if "city" not in combined_tags_for_npc_gen and "town" not in combined_tags_for_npc_gen: 
            role_pool = role_pool - {"merchant", "noble", "bard", "scholar"} # More rural/wild roles


        if "tavern" in combined_tags_for_npc_gen or "inn" in combined_tags_for_npc_gen :
            generate_tavern_npcs(location_obj, combined_tags_for_npc_gen, demographics)
        else:
            generate_standard_npcs(location_obj, combined_tags_for_npc_gen, npc_count, role_pool, demographics)

    except Exception as e:
        UI.print_failure(f"Error in generate_npcs_for_location for {location_obj.get('name', 'Unknown Location')}: {e}")
        # traceback.print_exc() # Comment out for less verbose error in game, but useful for debugging

def determine_npc_count(tags_list):
    if any(t in tags_list for t in ["city", "capital"]): # "major_city" was too specific
        return random.randint(4, 8) 
    elif any(t in tags_list for t in ["town", "village", "tavern", "inn", "market", "keep"]): # Added market/keep
        return random.randint(2, 5)
    elif any(t in tags_list for t in ["camp", "dungeon", "ruin", "mine", "watchtower", "lair"]): 
        return random.randint(1, 4)
    else: 
        return random.randint(0, 2) 

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

    if random.random() < 0.7 and "bards" not in patron_role_pool: # 70% chance of a bard if not already likely
        bard_culture = determine_npc_culture(demographics)
        bard_race = bard_culture if bard_culture else "Nord"
        bard = NPC(name=None, race=bard_race, role="bard", level=random.randint(2,6))
        npc_registry[location["id"]].append(bard)

def generate_standard_npcs(location, tags_list, npc_count, role_pool, demographics):
    for _ in range(npc_count):
        role = determine_npc_role(tags_list, role_pool)
        culture = determine_npc_culture(demographics)
        npc_race = culture if culture else random.choice(list(RACES.keys())) 
        
        if npc_race == "dwemer" and role not in ["dwemer_construct", "dwemer_ghost", "ancient_scholar_spirit"]:
            role = random.choice(["dwemer_construct", "dwemer_ghost"]) if random.random() < 0.7 else "lingering_echo" 

        npc_level_min, npc_level_max = location.get("level_range",(1,5)) # Default level range
        npc_level = random.randint(npc_level_min, npc_level_max)
        npc_level = max(1, npc_level + random.randint(-1,1)) # Slight variation based on player or world level if implemented

        npc = NPC(name=None, race=npc_race, role=role, level=npc_level) 
        npc_registry[location["id"]].append(npc)

def determine_npc_role(tags_list, base_role_pool):    
    # Enhanced role determination based on multiple tags
    # Example: a "ruined" "temple" with "undead" tags might spawn "skeleton_guardian" or "ghostly_priest"
    # This requires more granular role definitions and HOSTILE_ROLES updates.

    # Priority roles based on specific location tags
    if "college" in tags_list or "mage_guild" in tags_list:
        return random.choice(["mage_apprentice", "scholar", "magic_lecturer", "college_guard"])
    if "companions" in tags_list: # Jorrvaskr
        return random.choice(["companion_warrior", "new_blood", "circle_member"])
    if "thieves_guild_den" in tags_list or ("thieves" in tags_list and "underground" in tags_list):
        return random.choice(["thief_lookout", "pickpocket", "guild_rogue"])
    if "darkbrotherhood_sanctuary" in tags_list:
        return random.choice(["db_assassin", "db_initiate", "sanctuary_speaker"])
    if "dwemer_ruin" in tags_list:
        if random.random() < 0.6: return random.choice(["dwarven_sphere_damaged", "dwarven_spider_worker", "falmer_skulker"])
        else: return "explorer" # Non-hostile explorer sometimes
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
    if "shop" in tags_list or "market" in tags_list: # General shop/market
        return random.choice(["merchant", "stall_owner", "shop_assistant", "city_guard_patrolling"])
    if "port" in tags_list:
        return random.choice(["sailor", "dock_worker", "ship_captain_ashore", "fishmonger"])


    if not base_role_pool: 
        return random.choice(list(FRIENDLY_ROLES | HOSTILE_ROLES)) # Absolute fallback
        
    return random.choice(list(base_role_pool)) # Fallback to general pool


def determine_npc_culture(demographics):
    culture_weights = []
    cultures = []
    for race_name_key, percentage in demographics.items():
        valid_race_key = race_name_key.lower()
        if valid_race_key in RACES and valid_race_key != "others": 
            cultures.append(valid_race_key)
            culture_weights.append(percentage)

    if not cultures: 
        # UI.print_warning("Warning: No valid cultures from demographics, defaulting to random known race.") # Debug
        return random.choice(list(RACES.keys())) 
    try:
        return random.choices(cultures, weights=culture_weights, k=1)[0]
    except ValueError: # Weights might not sum to positive, or empty lists
        # UI.print_warning(f"Warning: Value error in random.choices for NPC culture. Demographics: {demographics}, Cultures: {cultures}, Weights: {culture_weights}. Defaulting.") # Debug
        return random.choice(list(RACES.keys())) if cultures else "nord" # Fallback


# Interaction functions
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
            # Use npc.tags which should be populated by NPC.__init__
            npc_info_tags = npc.tags.get("npc", {}) # get_tags(npc) is from tags.py, npc.tags is direct
            attitude_display_val = npc_info_tags.get("attitude", "neutral") 
            attitude_display = f"({attitude_display_val.capitalize()})" if attitude_display_val else ""
            UI.print_info(f"[{i}] {npc.name} — {npc.role.capitalize()} ({npc.race.capitalize()}) {attitude_display}")
        UI.print_line()

        sel = UI.print_prompt("With whom do you wish to parley? (0 to pass)").strip()
        if sel.isdigit():
            choice_index = int(sel)
            if 1 <= choice_index <= len(active_npcs):
                selected_npc = active_npcs[choice_index - 1]
                
                selected_npc_attitude_tags = selected_npc.tags.get("npc", {}).get("attitude", "") # Direct access
                
                # Ensure hostility check is robust
                is_hostile = "hostile" in selected_npc_attitude_tags or \
                              selected_npc.role in HOSTILE_ROLES or \
                              any(ht in selected_npc.role.lower() for ht in ["bandit", "draugr", "skeleton", "vampire", "wolf", "bear", "spider", "chaurus", "falmer", "forsworn_hostile_variant"]) # Add more role keywords

                if is_hostile and player.combat is None: # Check if player already in combat
                    UI.slow_print(f"{selected_npc.name} snarls and lunges with clear hostile intent!")
                    combat_instance = Combat(player, [selected_npc], location)
                    player.combat = combat_instance 
                    combat_instance.run()
                elif player.combat is not None:
                     UI.slow_print("You are already engaged in combat!")
                else: # Not hostile or already in combat (dialogue still proceeds)
                    selected_npc.dialogue(player, location) 
            elif choice_index != 0:
                UI.slow_print("No such soul stands before you.")
    except Exception as e:
        UI.print_failure(f"Error in list_npcs_at_location: {e}")
        # traceback.print_exc()

def combat_demo(player, current_location_obj): 
    try:
        enemy_level = player.level + random.randint(-1, 1) # Closer to player level
        enemy_level = max(1, enemy_level) 
        
        parent_hold, parent_city = _find_hierarchy(current_location_obj["id"])
        demographics_source = current_location_obj
        if parent_city and not demographics_source.get("demographics"): demographics_source = parent_city
        if parent_hold and not demographics_source.get("demographics"): demographics_source = parent_hold
        
        # Choose an enemy type appropriate for current location tags or a generic bandit
        loc_tags = current_location_obj.get("tags", [])
        enemy_role = "bandit_raider" # Default
        if "undead" in loc_tags or "barrow" in loc_tags or "graveyard" in loc_tags:
            enemy_role = random.choice(["draugr_restless", "skeleton_warrior", "ghost_ancient"])
        elif "cave" in loc_tags and "animal_den" in loc_tags:
            enemy_role = random.choice(["cave_bear_young", "wolf_alpha", "giant_spider_cave"])
        elif "dwemer_ruin" in loc_tags:
            enemy_role = random.choice(["dwarven_sphere_guardian", "falmer_warrior", "chaurus_hunter_small"])
        
        enemy_race = determine_npc_culture(demographics_source.get("demographics", {"Nord": 50, "Orc": 20, "Dunmer": 15, "Khajiit":15 })) # More varied bandit demographics

        # Adjust race if role implies a specific creature type
        if "draugr" in enemy_role: enemy_race = "undead_nord" # Placeholder race
        elif "skeleton" in enemy_role: enemy_race = "undead_skeleton"
        elif "ghost" in enemy_role: enemy_race = "spirit"
        elif "falmer" in enemy_role: enemy_race = "falmer"
        elif "dwarven" in enemy_role: enemy_race = "dwemer_construct_race" # Placeholder for constructs
        elif "wolf" in enemy_role or "bear" in enemy_role or "spider" in enemy_role or "chaurus" in enemy_role:
             enemy_race = enemy_role.split('_')[0] + "_creature" # e.g. wolf_creature

        enemy = NPC(
            name=None, 
            level=enemy_level, 
            race=enemy_race, 
            role=enemy_role 
        )
        
        # Equip demo enemy (simplified)
        if "bandit" in enemy_role or "draugr" in enemy_role or "skeleton" in enemy_role or "falmer" in enemy_role:
            weapon_keys = ["iron_sword", "steel_axe_old", "iron_mace_rusty", "ancient_nord_sword_chipped", "falmer_sword_crude"] # Need definitions
            armor_keys = ["hide_armor_scraps", "iron_armor_dented", "ancient_nord_armor_piece", "falmer_armor_basic"] # Need definitions
            
            if random.random() < 0.8: # 80% chance of weapon
                enemy_weapon = generate_item_from_key(random.choice(weapon_keys), enemy.level)
                if enemy_weapon: enemy.equipment.append(enemy_weapon)
            if random.random() < 0.6: # 60% chance of armor
                enemy_armor = generate_item_from_key(random.choice(armor_keys), enemy.level)
                if enemy_armor: enemy.equipment.append(enemy_armor)
        
        UI.slow_print(f"Suddenly, a hostile {enemy.name} ({enemy.race} {enemy.role}) emerges from the shadows and attacks!")

        if player.combat is None:
            combat_instance = Combat(player, [enemy], current_location_obj)
            player.combat = combat_instance
            combat_instance.run()
        else:
            UI.print_warning("Cannot initiate demo combat: Player already in combat.")
        
        return current_location_obj 
    except Exception as e:
        UI.print_failure(f"Error in combat_demo: {e}")
        # traceback.print_exc()
        return current_location_obj

def look_around_area(player, current_location_param, npc_registry_param, all_locs_param, ui_param):
    UI.slow_print(f"You take a moment to observe your surroundings in {current_location_param['name']}...")
    
    # Pass actual npc_registry, not the global 'random_encounters' which was a placeholder
    explore_location(player, current_location_param, {}, npc_registry_param, all_locs_param, ui_param) 
    
    if random.random() < 0.25: # Reduced chance slightly
        new_quest = generate_location_appropriate_quest(player.level, current_location_param.get("tags", [])) 
        if new_quest:
            ui_param.slow_print("\nSomething catches your eye... it seems to be a new undertaking!") # More flavor
            ui_param.slow_print(f"Quest: {new_quest.title}")
            ui_param.slow_print(f"Objective: {new_quest.description}") # Description as objective
            
            reward_parts = []
            if isinstance(new_quest.reward, dict):
                for r_type, r_value in new_quest.reward.items():
                    if isinstance(r_value, Item): # Check if r_value is an Item instance
                        reward_parts.append(f"{r_value.name} ({r_value.category.capitalize()})")
                    else:
                        reward_parts.append(f"{r_value} {r_type.capitalize()}")
            else: 
                reward_parts.append(str(new_quest.reward))

            ui_param.slow_print(f"Reward: {', '.join(reward_parts) if reward_parts else 'A fair compensation'}")
            
            if hasattr(player, 'quest_log') and player.quest_log is not None:
                player.quest_log.add_quest(new_quest)
                ui_param.slow_print("The details have been noted in your journal.")
            else:
                ui_param.slow_print("(You feel you should find a way to record such tasks.)") 
    return current_location_param 


# Initialization functions
def initialize_player():
    try:
        clear_screen()
        UI.print_heading("Forge Your Legend")
        UI.slow_print("The scrolls have foretold your arrival, yet your path remains unwritten...")

        # 1. Choose Race First
        UI.slow_print("\nFrom which lineage do you hail?")
        race_options = list(RACES.keys())
        for i, race_name_key in enumerate(race_options):
            race_display_name = race_name_key.capitalize()
            race_bonuses = RACES[race_name_key]
            bonus_descs = []
            if race_bonuses.get("strength_mod"): bonus_descs.append(f"+{race_bonuses['strength_mod']} STR")
            if race_bonuses.get("intelligence_mod"): bonus_descs.append(f"+{race_bonuses['intelligence_mod']} INT")
            if race_bonuses.get("willpower_mod"): bonus_descs.append(f"+{race_bonuses['willpower_mod']} WIL")
            if race_bonuses.get("agility_mod"): bonus_descs.append(f"+{race_bonuses['agility_mod']} AGI")
            if race_bonuses.get("speed_mod"): bonus_descs.append(f"+{race_bonuses['speed_mod']} SPD")
            if race_bonuses.get("endurance_mod"): bonus_descs.append(f"+{race_bonuses['endurance_mod']} END")
            if race_bonuses.get("personality_mod"): bonus_descs.append(f"+{race_bonuses['personality_mod']} PER")
            if race_bonuses.get("luck_mod"): bonus_descs.append(f"+{race_bonuses['luck_mod']} LCK")
            if race_bonuses.get("magicka_mod"): bonus_descs.append(f"+{race_bonuses['magicka_mod']} Max Magicka")
            if race_bonuses.get("poison_resist",0) > 0: bonus_descs.append(f"{race_bonuses['poison_resist']}% Poison Resist")
            if race_bonuses.get("magic_resist",0) > 0: bonus_descs.append(f"{race_bonuses['magic_resist']}% Magic Resist")
            if race_bonuses.get("frost_resist",0) > 0: bonus_descs.append(f"{race_bonuses['frost_resist']}% Frost Resist")
            if race_bonuses.get("shock_resist",0) > 0: bonus_descs.append(f"{race_bonuses['shock_resist']}% Shock Resist")
            if race_bonuses.get("fire_resist",0) > 0: bonus_descs.append(f"{race_bonuses['fire_resist']}% Fire Resist")
            for key, value in race_bonuses.items():
                if key.endswith("_skill") and value > 0:
                    bonus_descs.append(f"+{value} {key.replace('_mod','').replace('_skill','').capitalize()}")

            bonus_str = f" ({', '.join(bonus_descs)})" if bonus_descs else ""
            UI.slow_print(f"[{i+1}] {race_display_name}{bonus_str}", speed=0.005)

        player_race_str = "nord" 
        while True:
            race_choice_input = UI.print_prompt("Enter the number of your chosen race")
            try:
                race_index = int(race_choice_input) - 1
                if 0 <= race_index < len(race_options):
                    player_race_str = race_options[race_index]
                    break
                else:
                    UI.slow_print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                UI.slow_print("Invalid input. Please enter a number.")
        UI.print_success(f"A {player_race_str.capitalize()} you are. Your ancestors watch over you.")

        # 2. Choose Gender
        player_gender = ""
        while player_gender not in ["male", "female"]:
            gender_choice = UI.print_prompt("Are you Male or Female?").lower()
            if gender_choice.startswith("m"):
                player_gender = "male"
            elif gender_choice.startswith("f"):
                player_gender = "female"
            else:
                UI.slow_print("Invalid choice. Please enter 'Male' or 'Female'.")

        # 3. Choose Social Standing / Name Type
        player_name_type = ""
        while player_name_type not in ["noble", "commoner", "custom"]:
            UI.slow_print("\nDo you come from a noble lineage, a common background, or will you forge your own name?")
            UI.print_menu(["Noble (names of influence)", "Commoner (everyday names)", "Forge my own name"])
            name_type_choice = UI.print_prompt("Enter your choice").strip()

            if name_type_choice == "1":
                player_name_type = "noble"
            elif name_type_choice == "2":
                player_name_type = "commoner"
            elif name_type_choice == "3":
                player_name_type = "custom"
            else:
                UI.slow_print("Invalid choice. Please select from the options.")
        
        player_name = ""
        if player_name_type == "custom":
            while not player_name:
                player_name = UI.print_prompt("Speak your true name, wanderer")
                if not player_name:
                    UI.slow_print("A name is your first step into legend. Choose wisely.", speed=0.02)
        else:
            # Get names from NPC.NAME_POOLS
            available_names = NAME_POOLS.get(player_race_str, {}).get(player_name_type, {}).get(player_gender, ["Nameless Hero"])
            
            if not available_names:
                UI.slow_print(f"\nNo specific {player_name_type} {player_gender} names found for {player_race_str.capitalize()}.")
                UI.slow_print("You may choose your own name instead.")
                player_name_type = "custom" # Fallback to custom if no names available
                while not player_name:
                    player_name = UI.print_prompt("Speak your true name, wanderer")
                    if not player_name:
                        UI.slow_print("A name is your first step into legend. Choose wisely.", speed=0.02)
            else:
                UI.slow_print(f"\nHere are some {player_name_type} names for a {player_race_str.capitalize()} {player_gender}:")
                for i, name in enumerate(available_names):
                    UI.slow_print(f"[{i+1}] {name}", speed=0.005)
                UI.slow_print(f"[{len(available_names)+1}] Choose my own name")

                while True:
                    name_choice_input = UI.print_prompt("Enter the number of your chosen name")
                    try:
                        name_index = int(name_choice_input) - 1
                        if 0 <= name_index < len(available_names):
                            player_name = available_names[name_index]
                            break
                        elif name_index == len(available_names): # Choose custom name option
                            while not player_name:
                                player_name = UI.print_prompt("Speak your true name, wanderer")
                                if not player_name:
                                    UI.slow_print("A name is your first step into legend. Choose wisely.", speed=0.02)
                            break
                        else:
                            UI.slow_print("Invalid choice. Please enter a number from the list.")
                    except ValueError:
                        UI.slow_print("Invalid input. Please enter a number.")

        UI.print_success(f"'{player_name}'... a name that will echo in time.")


        UI.slow_print("\nWhat path of skill do you tread?")
        class_options_keys = list(CLASSES.keys())
        for i, class_id_key in enumerate(class_options_keys):
            class_data = CLASSES[class_id_key]
            UI.slow_print(f"[{i+1}] {class_data['name']} - {class_data['desc']}", speed=0.005)

        selected_class_key = "warrior" 
        selected_class_data = CLASSES[selected_class_key]
        while True:
            class_choice_input = UI.print_prompt("Enter the number of your chosen class")
            try:
                class_index = int(class_choice_input) - 1
                if 0 <= class_index < len(class_options_keys):
                    selected_class_key = class_options_keys[class_index]
                    selected_class_data = CLASSES[selected_class_key]
                    break
                else:
                    UI.slow_print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                UI.slow_print("Invalid input. Please enter a number.")
        UI.print_success(f"The path of the {selected_class_data['name']} unfolds before you.")

        UI.slow_print(f"\nWithin {selected_class_data['name']}, which specialization calls to you?")
        subclass_options_map = {str(idx+1): sc_key for idx, sc_key in enumerate(selected_class_data["subclasses"].keys())}

        for display_num, sc_id_key in subclass_options_map.items():
            subclass_item_data = selected_class_data["subclasses"][sc_id_key]
            attr_str = ", ".join([f"{k.capitalize()[:3]}: {v}" for k,v in subclass_item_data["attributes"].items()]) # Abbreviate attributes
            skill_str = ", ".join([f"{k.replace('_',' ').capitalize()}: {v}" for k,v in subclass_item_data["skills"].items()])
            inv_str = ", ".join([name.replace('_', ' ').title() for name in subclass_item_data["inventory"]])
            UI.slow_print(f"[{display_num}] {subclass_item_data['name']}", speed=0.005)
            UI.slow_print(f"    Attrs: {attr_str}", speed=0.005) 
            UI.slow_print(f"    Skills: {skill_str}", speed=0.005)
            UI.slow_print(f"    Gear: {inv_str}", speed=0.005)

        selected_subclass_key_actual = list(selected_class_data["subclasses"].keys())[0] # Default
        selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
        while True:
            subclass_choice_input_str = UI.print_prompt("Enter the number of your chosen subclass")
            if subclass_choice_input_str in subclass_options_map:
                selected_subclass_key_actual = subclass_options_map[subclass_choice_input_str]
                selected_subclass_final_data = selected_class_data["subclasses"][selected_subclass_key_actual]
                break
            else:
                UI.slow_print("Invalid choice. Please enter a number from the list.")
        UI.print_success(f"You are now a {selected_subclass_final_data['name']}, a {selected_class_data['name']} of unique talents.")

        player = Player(
            race=selected_class_data["race"],  # Use the correct variable
            subclass=selected_class_data["name"],
            stats=selected_class_data["stats"].copy(),
            skills=selected_class_data["skills"].copy(),
        )  

        initial_items_added_names = []
        UI.slow_print("Preparing your starting gear...")
        for item_key_from_subclass in selected_subclass_final_data["inventory"]:
            item_instance = generate_item_from_key(item_key_from_subclass, player.level) 
            if item_instance:
                if player.add_item(item_instance):
                    initial_items_added_names.append(item_instance.name)
                    current_tags_equipped = [eq.equipment_tag for eq in player.equipment if eq.equipment_tag]
                    can_equip_new = True
                    if item_instance.equipment_tag in current_tags_equipped and item_instance.equipment_tag not in ["ring", "amulet"]:
                         can_equip_new = False
                        
                    if can_equip_new:
                         player.equip_item(item_instance)
                else:
                    UI.print_warning(f"Could not add starting item {item_instance.name} (inventory full or error).")
            else:
                UI.print_warning(f"Could not generate starting item for key: {item_key_from_subclass}")

        if initial_items_added_names: UI.slow_print(f"In your satchel, you were given: {', '.join(initial_items_added_names)}.", speed=0.01) 
        if player.equipment: UI.slow_print(f"You have equipped: {', '.join([eq.name for eq in player.equipment])}.", speed=0.01)
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

def initialize_starting_location():
    # Default start: The Bannered Mare in Whiterun, Whiterun Hold
    start_tavern_name = "The Bannered Mare" 
    start_city_name = "Whiterun"
    start_hold_name = "Whiterun Hold"

    starting_loc_obj = None
    parent_city_obj = None
    parent_hold_obj = None

    parent_hold_obj = next((h for h in ALL_LOCATIONS if h["name"] == start_hold_name), None)
    if not parent_hold_obj:
        UI.print_warning(f"Starting hold '{start_hold_name}' not found. Defaulting.")
        parent_hold_obj = ALL_LOCATIONS[0] 

    parent_city_obj = next((c for c in parent_hold_obj.get("sub_locations", []) if c["name"] == start_city_name), None)
    if not parent_city_obj:
        UI.print_warning(f"Starting city '{start_city_name}' in {parent_hold_obj['name']} not found. Defaulting.")
        parent_city_obj = parent_hold_obj.get("sub_locations", [parent_hold_obj])[0] # Fallback

    if "sub_locations" in parent_city_obj:
        starting_loc_obj = next((v for v in parent_city_obj.get("sub_locations", []) if v["name"] == start_tavern_name), None)
    
    if not starting_loc_obj: # If tavern not found, default to the city itself
        UI.print_warning(f"Starting tavern '{start_tavern_name}' in {parent_city_obj['name']} not found. Starting in city.")
        starting_loc_obj = parent_city_obj 

    # Add initial locations to known_locations
    known_locations.add(parent_hold_obj["id"])
    discover_connected_locations(parent_hold_obj)
    if parent_city_obj["id"] != parent_hold_obj["id"]: 
        known_locations.add(parent_city_obj["id"])
        discover_connected_locations(parent_city_obj)
    if starting_loc_obj["id"] != parent_city_obj["id"]: 
        known_locations.add(starting_loc_obj["id"])
        # Venues typically don't have their own broad travel links to discover

    message = f"You awaken in {starting_loc_obj['name']}, a seemingly cozy establishment in {parent_city_obj['name']}, within the lands of {parent_hold_obj['name']}..."
    UI.slow_print(message)
    
    UI.slow_print(starting_loc_obj['desc'])
    UI.slow_print("The warm fire crackles. A few patrons murmur over their drinks. Adventure awaits.")
    
    generate_npcs_for_location(starting_loc_obj) 
    return starting_loc_obj

def initialize_game_state():
    global game_start_time, known_locations, npc_registry
    game_start_time = datetime.now(timezone.utc)
    known_locations.clear()
    npc_registry.clear()
    # random_encounters.clear() # Removed as it's not used this way anymore

# Main game loop
def start_game():
    current_location_global = None 
    try:
        initialize_game_state()
        player = initialize_player()
        if not player:
            UI.print_failure("Failed to initialize player. Exiting.")
            return

        current_location_global = initialize_starting_location() 
        
        main_loop_running = True
        while main_loop_running:
            if not player.is_alive():
                UI.print_heading("Your Legend Ends Here")
                UI.slow_print(f"{player.name} has fallen. The bards may sing of your deeds, or perhaps your tale will fade into an unmarked grave...")
                UI.slow_print("Skyrim is a harsh land. May your next journey be more fortunate.")
                break 

            player.stats.restore_fatigue(max(1, player.level // 2)) 
            player.stats.restore_magicka(max(1, player.level // 3))

            if player.stats.current_encumbrance > player.stats.encumbrance_limit:
                UI.slow_print("Your heavy load weighs you down.", speed=0.005)
            
            UI.print_line('=')
            time_now = datetime.now(timezone.utc)
            # Simulate in-game time passing - very basic
            game_elapsed_seconds = (time_now - game_start_time).total_seconds()
            game_days = int(game_elapsed_seconds // (60*5)) # 1 game day = 5 real minutes (example)
            game_hours = int((game_elapsed_seconds % (60*5)) // (60*5/24))
            time_of_day_str = "Morning"
            if 5 <= game_hours < 12: time_of_day_str = "Morning"
            elif 12 <= game_hours < 17: time_of_day_str = "Afternoon"
            elif 17 <= game_hours < 21: time_of_day_str = "Evening"
            else: time_of_day_str = "Night"

            UI.print_info(f"Location: {current_location_global['name']} | Day: {game_days+1}, {time_of_day_str}") 
            UI.print_info(f"HP: {player.stats.current_health}/{player.stats.max_health} MP: {player.stats.current_magicka}/{player.stats.max_magicka} ST: {player.stats.current_fatigue}/{player.stats.max_fatigue}")
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

            # Handle quit explicitly via "0" or if it's the last option number
            is_quit_option = False
            if choice == "0":
                is_quit_option = True
            elif choice.isdigit() and int(choice) == len(menu_options) and "depart this realm" in menu_options[-1].lower():
                is_quit_option = True
            
            if is_quit_option:
                UI.slow_print("Farewell, until the stars call you back to Skyrim!")
                main_loop_running = False
                continue

            new_location_or_state = handle_player_choice(choice, player, current_location_global, menu_options)
            
            if isinstance(new_location_or_state, dict) and "id" in new_location_or_state : 
                 current_location_global = new_location_or_state
            
            if main_loop_running and current_location_global and random.random() < 0.10:
                UI.print_line('.')
                UI.slow_print("The winds of fate shift...")
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

def handle_player_choice(choice, player, current_loc_param, menu_options_list): 
    action = None
    new_current_location = current_loc_param

    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(menu_options_list):
            action_text = menu_options_list[choice_num - 1]
            action = action_text.split("(")[0].strip().lower()
            if "depart this realm" in action:
                return "QUIT_GAME_SIGNAL"
    else:
        action_input_lower = choice.lower()
        for opt_text in menu_options_list:
            opt_action_part = opt_text.split("(")[0].strip().lower()
            if action_input_lower == opt_action_part or action_input_lower in opt_text.lower():
                action = opt_action_part
                break
    
    if action == "explore known world": 
        new_current_location = explore_and_travel_menu(player, current_loc_param)
    elif action == "parley with souls":
        if current_loc_param: list_npcs_at_location(current_loc_param, player)
        else: UI.slow_print("You must first be somewhere to find others.")
    elif action == "behold thy spirit":
        UI.display_player_stats(player) 
    elif action == "test thy steel":
        new_current_location = combat_demo(player, current_loc_param) 
    elif action == "inspect thy possessions":
        UI.display_inventory(player)
    elif action == "look around the area":
        new_current_location = look_around_area(player, current_loc_param, npc_registry, ALL_LOCATIONS, UI)
    elif action == "review quest log":
        UI.display_quest_log(player)
    elif action == "use item from inventory": 
        handle_item_use(player) 
    elif action == "wait / pass time":
        UI.slow_print("Time passes...")
        global game_start_time
        for _ in range(3):
            player.stats.restore_fatigue(max(1,player.level // 2) * 2)
            player.stats.restore_magicka(max(1,player.level // 3) * 2)
        UI.slow_print("You feel somewhat rested.")

    elif action == "depart this realm": 
        UI.slow_print("To depart, select the explicit 'Depart This Realm' option (usually 0 or last number).")
    else:
        UI.slow_print("Your will wavers, or perhaps the spirits muddle your intent.")
    
    if new_current_location["id"] == current_loc_param["id"] and action and action != "depart this realm":
        if action not in ["behold thy spirit", "inspect thy possessions", "review quest log"]:
            UI.press_enter()
    elif new_current_location["id"] != current_loc_param["id"]:
         UI.press_enter()

    return new_current_location
def display_inventory_with_equipped(player):
    UI.print_subheading("Inventory")
    if not player.inventory and not player.equipment:
        UI.slow_print("Your inventory is empty.")
        return

    # Combine inventory and equipped items for display
    all_items = player.inventory + [{"item": item, "equipped": True} for item in player.equipment]
    for i, entry in enumerate(all_items, 1):
        item = entry if isinstance(entry, dict) else {"item": entry, "equipped": False}
        equipped_flag = " (Equipped)" if item["equipped"] else ""
        UI.print_info(f"[{i}] {item['item'].name}{equipped_flag} - Desc: {item['item'].get_description()}")

def handle_inventory_menu(player):
    while True:
        display_inventory_with_equipped(player)
        item_choice_input = UI.print_prompt("Select an item to interact with (Enter number, 0 to cancel):")
        if not item_choice_input.isdigit():
            UI.slow_print("Invalid input.")
            continue

        item_choice_idx = int(item_choice_input)
        if item_choice_idx == 0:
            UI.slow_print("Exiting inventory menu.")
            break

        try:
            selected_entry = player.inventory[item_choice_idx - 1]
            if isinstance(selected_entry, dict) and selected_entry.get("equipped"):
                equipped_item = selected_entry["item"]
                UI.slow_print(f"{equipped_item.name} is equipped.")
                action_choice = UI.print_prompt("What would you like to do? [1] Examine [2] Unequip")
                if action_choice == "1":
                    player.examine_item(equipped_item)
                elif action_choice == "2":
                    player.unequip_item(equipped_item)
                else:
                    UI.slow_print("Invalid choice.")
            else:
                selected_item = selected_entry
                UI.slow_print(f"Selected {selected_item.name}.")
                action_choice = UI.print_prompt("What do you want to do? [1] Examine [2] Equip [3] Use [4] Drop")
                if action_choice == "1":
                    player.examine_item(selected_item)
                elif action_choice == "2":
                    player.equip_item(selected_item)
                elif action_choice == "3":
                    player.use_item(selected_item)
                elif action_choice == "4":
                    player.drop_item(selected_item)
                else:
                    UI.slow_print("Invalid choice.")
        except IndexError:
            UI.slow_print("Invalid selection.")

def sort_inventory_menu(player):
    UI.print_subheading("Sort Inventory")
    sort_choice = UI.print_prompt("Sort inventory by [1] Name [2] Category")
    if sort_choice == "1":
        player.sort_inventory("name")
    elif sort_choice == "2":
        player.sort_inventory("category")
    else:
        UI.slow_print("Invalid choice.")

def handle_item_use(player):
    UI.print_subheading("Use Item")
    if not player.inventory:
        UI.slow_print("Your inventory is empty.")
        return

    usable_items = [item for item in player.inventory if item.category in ["potion", "food", "scroll", "ingredient"]] 
    
    if not usable_items:
        UI.slow_print("You have no items that can be readily used in this way.")
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
            return

        item_choice_idx = int(item_choice_input)
        if item_choice_idx == 0:
            UI.slow_print("No item used.")
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


if __name__ == "__main__":
    start_game()