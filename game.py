import time
import random
import traceback
from datetime import datetime, timezone

try:
    from locations import LOCATIONS
    from stats import Player, Stats, RACES, CLASSES  # Import RACES and CLASSES directly from stats
    from npc import NPC, FRIENDLY_ROLES, HOSTILE_ROLES, NAME_POOLS
    from combat import Combat
    from ui import UI
    from items import generate_random_item, Item, generate_item_from_key  # Import generate_item_from_key
    from events import trigger_random_event, explore_location
    from quests import (
        list_player_quests,
        QuestLog,  # Import QuestLog directly
        generate_location_appropriate_quest,
        generate_reward  # Now used for generating quest rewards
    )
    import tags
    import flavor

except ImportError as e:
    print(f"Error importing modules: {e}")
    input("Press Enter to exit...")
    exit(1)

# Globals
known_locations = set()
npc_registry = {}
current_location = None  # This global will be updated by being returned from functions
random_encounters = {}
game_start_time = None

ALL_LOCATIONS = LOCATIONS

ENCOUNTER_NAMES = {
    "city": [
        {"name": "Street Urchin", "desc": "A nimble child attempts to pickpocket you.", "type": "thieves"},
        {"name": "Drunkard", "desc": "A staggering drunkard accosts you for coin.", "type": "social"},
    ],
    "forest": [
        {"name": "Wolf Pack", "desc": "A pack of wolves circles, seeking prey.", "type": "hostile"},
        {"name": "Lost Traveler", "desc": "A lost traveler asks for directions.", "type": "social"},
    ],
}


# Utility functions
def clear_screen():
    UI.clear_screen()


def slow_print(text, delay=0.03):
    UI.slow_print(text, speed=delay)


def get_flavor_text(tags_list_param, category, ensure_vignette=False):  # Renamed tags_list to tags_list_param
    """Gets flavor text from the flavor module based on a list of tags."""
    if not tags_list_param:
        return ""

    # Ensure tags_list_param is a list of strings
    tags_filtered = [tag for tag in tags_list_param if isinstance(tag, str)]
    
    class DummyEntity:
        def __init__(self, tags_list_for_dummy, category_for_dummy):
            self.tags = {}
            if category_for_dummy == "location_tags":
                # Map general tags to specific flavor categories if possible
                # This is a heuristic; a more robust system would categorize tags
                # before passing them to flavor.get_flavor.
                environment_tags = [t for t in tags_list_for_dummy if t in tags.LOCATIONS["environment"]]
                climate_tags = [t for t in tags_list_for_dummy if t in tags.LOCATIONS["climate"]]
                terrain_tags = [t for t in tags_list_for_dummy if t in tags.LOCATIONS["terrain"]]
                structure_tags = [t for t in tags_list_for_dummy if t in tags.LOCATIONS["structure"]]
                magical_tags = [t for t in tags_list_for_dummy if t in tags.LOCATIONS["magical"]]

                if environment_tags: self.tags.setdefault("location", {})["environment"] = environment_tags
                if climate_tags: self.tags.setdefault("location", {})["climate"] = climate_tags
                if terrain_tags: self.tags.setdefault("location", {})["terrain"] = terrain_tags
                if structure_tags: self.tags.setdefault("location", {})["structure"] = structure_tags
                if magical_tags: self.tags.setdefault("location", {})["magical"] = magical_tags
            else:
                self.tags[category_for_dummy] = tags_list_for_dummy 

    dummy_entity = DummyEntity(tags_filtered, category)
    flavor_vignettes = flavor.get_flavor(dummy_entity)

    # Check if any available_text exists in flavor_vignettes
    if not flavor_vignettes and ensure_vignette:
        return "The air is thick with untold stories."

    # Select a random flavor from the available vignettes
    if flavor_vignettes:
        return random.choice(flavor_vignettes)
    else:
        return ""


def discover_connected_locations(location):
    global known_locations
    if "travel" in location:
        for path_type in ["roads", "paths"]:
            if path_type in location["travel"]:
                for dest in location["travel"][path_type]:
                    dest_loc = next(
                        (loc for loc in ALL_LOCATIONS if loc["name"] == dest), None
                    )
                    if dest_loc:
                        known_locations.add(dest_loc["id"])


def generate_random_encounter(tags_list):
    """Generates a random encounter based on tags."""
    if not tags_list:
        return None

    # Ensure tags_list is a list of strings
    tags = [tag for tag in tags_list if isinstance(tag, str)]

    available_encounters = [
        enc for tag in tags if tag in ENCOUNTER_NAMES for enc in ENCOUNTER_NAMES[tag]
    ]
    if available_encounters:
        encounter = random.choice(available_encounters)
        return {
            "id": random.randint(10000, 99999),
            "name": encounter["name"],
            "desc": encounter["desc"],
            "tags": tags + [encounter["type"]],
        }
    return None


# Game logic functions
def list_locations():
    clear_screen()
    UI.print_heading("Known Realms")
    if not known_locations:
        UI.slow_print("Your map remains blank, awaiting discovery.")
        UI.print_line()
        return

    # Sort locations to display them consistently
    sorted_known_locations = sorted(
        [l for l in ALL_LOCATIONS if l["id"] in known_locations],
        key=lambda x: x["name"]
    )

    displayed_ids = set()
    for loc in sorted_known_locations:
        # Avoid re-displaying sub-locations that are already listed under their parent
        if loc["id"] in displayed_ids:
            continue
        
        brief_desc = loc["desc"].split(".")[0] + "."
        UI.print_info(f"[{loc['id']:>2}] {loc['name']:<30} — {brief_desc}")
        displayed_ids.add(loc["id"])

        # Display sub-locations if any
        if "sub_locations" in loc:
            for sub_loc in sorted(loc["sub_locations"], key=lambda x: x["name"]):
                if sub_loc["id"] in known_locations and sub_loc["id"] not in displayed_ids:
                    sub_brief_desc = sub_loc["desc"].split(".")[0] + "."
                    UI.print_info(f"   [{sub_loc['id']:>2}] {sub_loc['name']:<28} — {sub_brief_desc}")
                    displayed_ids.add(sub_loc["id"])
    UI.print_line()


def travel_menu(player, current_location_param):  # current_location passed as parameter
    try:
        clear_screen()
        UI.print_heading("Chart a Course")
        
        reachable_locations = []
        travel_options_map = {}  # Map input choice to location object

        # Determine if current_location_param is a sub-location
        is_sub_location = False
        parent_loc_obj = None
        for hold_or_city in ALL_LOCATIONS:  # Iterate through top-level holds/cities
            if "sub_locations" in hold_or_city:
                for sub_l in hold_or_city["sub_locations"]:
                    if sub_l["id"] == current_location_param["id"]:
                        is_sub_location = True
                        parent_loc_obj = hold_or_city  # This is the parent hold or city
                        break
                if is_sub_location:
                    break
        
        # Option to go up to parent location if currently in a sub-location
        if is_sub_location and parent_loc_obj and parent_loc_obj["id"] in known_locations:
            reachable_locations.append({"id": parent_loc_obj["id"], "name": f"Up to {parent_loc_obj['name']}", "desc": parent_loc_obj["desc"], "type": "parent"})
            travel_options_map[str(parent_loc_obj["id"])] = parent_loc_obj
        
        # Add sub-locations of the current city/hold
        if "sub_locations" in current_location_param:
            for sub_loc in current_location_param["sub_locations"]:
                if sub_loc["id"] in known_locations and sub_loc["id"] != current_location_param["id"]:
                    reachable_locations.append(sub_loc)
                    travel_options_map[str(sub_loc["id"])] = sub_loc
        
        # Add direct travel connections (roads/paths) from current_location or its parent if in sub-location
        effective_location_for_travel = parent_loc_obj if is_sub_location and parent_loc_obj else current_location_param

        if "travel" in effective_location_for_travel:
            for path_type in ["roads", "paths"]:
                if path_type in effective_location_for_travel["travel"]:
                    for dest_name in effective_location_for_travel["travel"][path_type]:
                        dest_loc = next((loc for loc in ALL_LOCATIONS if loc["name"] == dest_name), None)
                        if dest_loc and dest_loc["id"] in known_locations and dest_loc["id"] != current_location_param["id"]:
                            # Avoid adding if it's already a sub_location of the current hold, or the parent itself
                            if not any(loc_item.get("id") == dest_loc["id"] for loc_item in reachable_locations):
                                reachable_locations.append(dest_loc)
                                travel_options_map[str(dest_loc["id"])] = dest_loc
        
        # Sort reachable locations for consistent display: Parents first, then by name
        reachable_locations.sort(key=lambda x: (x.get("type") != "parent", x["name"]))

        if not reachable_locations:
            UI.slow_print("There are no immediate destinations known from here.")
            UI.print_line()
            return current_location_param  # Return current_location_param unchanged

        for loc_option in reachable_locations:
            brief_desc = loc_option["desc"].split(".")[0] + "."
            UI.print_info(f"[{loc_option['id']:>2}] {loc_option['name']:<30} — {brief_desc}")
            # travel_options_map is already correctly populated above

        if current_location_param and current_location_param["id"] in random_encounters:
            UI.print_subheading("\n-- Nearby Encounters --")
            for i, encounter in enumerate(
                random_encounters[current_location_param["id"]], 1
            ):
                UI.print_info(
                    f"[R{i:>1}] {encounter['name']:<30} — {encounter['desc'].split('.')[0]}."
                )
        UI.print_line()

        sel = UI.print_prompt("Whither do you journey? (0 to remain)").strip()

        if sel == "0":
            return current_location_param  # Return current_location_param unchanged

        if sel.startswith("R"):
            return handle_encounter_selection(sel, player, current_location_param)  # Pass current_location_param

        try:
            loc_id = int(sel)
            if str(loc_id) in travel_options_map:
                selected_loc_obj = travel_options_map[str(loc_id)]
                if selected_loc_obj.get("type") == "parent":
                    # If "Up to Parent" was selected, return the actual parent object
                    return parent_loc_obj  # Return the parent object
                else:
                    # For all other valid selections, pass to handle_location_selection
                    # This now handles both direct travel to a non-hold/city location
                    # and selection of a sub-location from the current hold/city's menu.
                    return handle_location_selection(loc_id, player, selected_loc_obj)  # Pass the selected_loc_obj
            else:
                UI.slow_print("That destination is not currently reachable or known.")
                return current_location_param  # Return current_location_param unchanged
        except ValueError:
            UI.slow_print("Your intent is unclear.")
            return current_location_param  # Return current_location_param unchanged

    except Exception as e:
        UI.print_failure(f"Error in travel_menu: {e}")
        traceback.print_exc()
        return current_location_param  # Always return current_location_param


def handle_encounter_selection(sel, player, current_location_param):  # current_location passed as parameter
    try:
        encounter_index = int(sel[1:]) - 1
        if (
            current_location_param
            and current_location_param["id"] in random_encounters
            and 0 <= encounter_index < len(random_encounters[current_location_param["id"]])
        ):
            encounter = random_encounters[current_location_param["id"]][encounter_index]
            # current_location is updated locally and returned
            new_current_location = encounter
            known_locations.add(new_current_location["id"])

            UI.slow_print(f"You have ventured to {new_current_location['name']}.\n")
            UI.slow_print(
                get_flavor_text(new_current_location["tags"], "location_tags", ensure_vignette=True)
            )
            trigger_random_event(new_current_location["tags"], player, UI, new_current_location)
            generate_npcs_for_location(new_current_location)
            return new_current_location
        else:
            UI.slow_print("That place remains shrouded in mystery or lies beyond your reach.")
            return current_location_param  # Return current_location_param unchanged
    except ValueError:
        UI.slow_print("Invalid encounter selection.")
        return current_location_param  # Return current_location_param unchanged


def handle_location_selection(loc_id, player, current_location_param):  # current_location passed as parameter
    # current_location is not declared global here, it's passed as a parameter
    # and the new value will be returned.

    if loc_id not in known_locations:
        UI.slow_print("That land is unknown to you, adventurer.")
        return current_location_param  # Return current_location_param unchanged

    # The selected 'loc_obj' is now passed directly as current_location_param if it's already a known object.
    # If loc_id was passed from travel_menu that selected a non-parent/non-sublocation, find it:
    loc = next((l for l in ALL_LOCATIONS if l["id"] == loc_id), None)
    if not loc:  # Fallback if loc_id somehow invalid
        return current_location_param

    # If the selected location is the current location, and it's a hold/city, offer sub-locations.
    if loc["id"] == current_location_param["id"] and "sub_locations" in loc:
        return handle_sublocation_selection(loc, player, current_location_param)

    # If the selected location is a HOLD (has sub_locations), and it's *not* the current location,
    # set it as current and then offer its sub-locations.
    # This path is typically taken when selecting a new Hold from the travel_menu.
    if "sub_locations" in loc and loc["sub_locations"] and loc["id"] != current_location_param["id"]:
        new_current_location = loc
        known_locations.add(new_current_location["id"])
        discover_connected_locations(new_current_location)  # Discover connections of the hold itself

        UI.slow_print(f"You have ventured to {new_current_location['name']}.")
        UI.slow_print(get_flavor_text(new_current_location["tags"], "location_tags", ensure_vignette=True))

        # Now, present the sub-locations for selection
        return handle_sublocation_selection(new_current_location, player, new_current_location)  # Pass new_current_location
    
    # Normal travel to a non-hold location, or a sub-location directly selected
    new_current_location = loc
    known_locations.add(new_current_location["id"])
    discover_connected_locations(new_current_location)
    UI.slow_print(f"You have ventured to {new_current_location['name']}.\n")
    UI.slow_print(get_flavor_text(new_current_location["tags"], "location_tags", ensure_vignette=True))
    trigger_random_event(new_current_location["tags"], player, UI, new_current_location)
    generate_npcs_for_location(new_current_location)
    return new_current_location


def handle_sublocation_selection(parent_loc, player, current_location_param):  # current_location passed as parameter
    # current_location is not declared global here, it's passed as a parameter
    # and the new value will be returned.

    sub_locs = parent_loc.get("sub_locations", [])
    # Only list sub-locations that are known
    known_sub_locs = [sl for sl in sub_locs if sl["id"] in known_locations]

    if not known_sub_locs:
        UI.slow_print(f"There are no known sub-locations within {parent_loc['name']} to explore further.")
        UI.print_line()
        return current_location_param  # Return current_location_param unchanged

    # Prompt for selection within the current parent location (if current_location is a hold)
    UI.print_heading(f"Realms Within {parent_loc['name']}")
    for sub_loc in sorted(known_sub_locs, key=lambda x: x["name"]):  # Display known sub-locations only
        brief_desc = sub_loc["desc"].split(".")[0] + "."
        UI.print_info(f"[{sub_loc['id']:>2}] {sub_loc['name']:<30} — {brief_desc}")
    UI.print_line()

    try:
        sub_id = int(UI.print_prompt("Which haven within do you seek? (0 to linger)"))
        if sub_id == 0:
            return current_location_param  # Return current_location_param unchanged
    except ValueError:
        UI.slow_print("Your path is obscured.")
        return current_location_param  # Return current_location_param unchanged

    sub_loc = next((sl for sl in known_sub_locs if sl["id"] == sub_id), None)  # Check against known_sub_locs
    if sub_loc:
        new_current_location = sub_loc
        UI.slow_print(f"You have ventured to {new_current_location['name']} in {parent_loc['name']}.\n")
        # discover_connected_locations(parent_loc) # Already discovered when entering parent hold
        
        inheritable_tags = {
            "nordic", "imperial", "stormcloak", "thieves", "corrupt",
            "military", "bards", "city", "town", "village"
        }
        combined_tags = new_current_location.get("tags", []) + [t for t in parent_loc["tags"] if t in inheritable_tags]

        UI.slow_print(
            get_flavor_text(combined_tags, "location_tags", ensure_vignette=True)
        )
        trigger_random_event(combined_tags, player, UI, new_current_location)
        generate_npcs_for_location(new_current_location)
        return new_current_location
    else:
        UI.slow_print("That place holds no welcome for you.")
        return current_location_param  # Return current_location_param unchanged


# NPC generation functions
def generate_npcs_for_location(location):
    try:
        if location["id"] in npc_registry:
            return

        npc_registry[location["id"]] = []
        parent_loc = next(
            (
                loc
                for loc in ALL_LOCATIONS
                if any(
                    sub_loc["id"] == location["id"]
                    for sub_loc in loc.get("sub_locations", [])
                )
            ),
            None,
        )

        if parent_loc:
            inheritable_tags = {
                "nordic",
                "imperial",
                "stormcloak",
                "thieves",
                "corrupt",
                "military",
                "bards",
            }
            if "tavern" not in location.get("tags", []):
                inheritable_tags.add("city")
            filtered_loc_tags = [t for t in parent_loc["tags"] if t in inheritable_tags]
            tags_list = location.get("tags", []) + filtered_loc_tags
            demographics = parent_loc.get("demographics", {"Nord": 100})
        else:
            tags_list = location.get("tags", [])
            demographics = location.get("demographics", {"Nord": 100})

        npc_count = determine_npc_count(tags_list)
        role_pool = FRIENDLY_ROLES if "tavern" in tags_list else (FRIENDLY_ROLES | HOSTILE_ROLES)

        if "tavern" in tags_list:
            generate_tavern_npcs(location, tags_list)
        else:
            generate_standard_npcs(location, tags_list, npc_count, role_pool, demographics)

    except Exception as e:
        UI.print_failure(f"Error in generate_npcs_for_location: {e}")
        traceback.print_exc()


def determine_npc_count(tags_list):
    if "city" in tags_list or "tavern" in tags_list:
        return random.randint(6, 12)
    elif "village" in tags_list or "town" in tags_list:
        return random.randint(3, 6)
    else:
        return random.randint(1, 3)


def generate_tavern_npcs(location, tags_list):
    innkeeper = NPC(name="Innkeeper", race="Nord", role="innkeeper", level=random.randint(1,5))  # Added name, race, level
    npc_registry[location["id"]].append(innkeeper)

    patron_count = random.randint(3, 8)
    patron_roles = ["merchant", "adventurer", "hunter", "farmer"]
    for _ in range(patron_count):
        patron = NPC(name="Patron", race="Nord", role=random.choice(patron_roles), level=random.randint(1,5))  # Added name, race, level
        npc_registry[location["id"]].append(patron)

    bard = NPC(name="Bard", race="Nord", role="bard", level=random.randint(1,5))  # Added name, race, level
    npc_registry[location["id"]].append(bard)


def generate_standard_npcs(location, tags_list, npc_count, role_pool, demographics):
    for _ in range(npc_count):
        role = determine_npc_role(tags_list, role_pool)
        culture = determine_npc_culture(demographics)
        # NPC names are now generated within the NPC class itself, so we pass None
        npc = NPC(name=None, race=culture, role=role, level=random.randint(1,5))  # Pass None for name, as NPC class generates it
        npc_registry[location["id"]].append(npc)


def determine_npc_role(tags_list, role_pool):
    tag_roles = {
        "companions": ["warrior"] * 3 + ["blacksmith"],
        "thieves": ["rogue"] * 3 + ["merchant"],
        "college": ["mage"] * 3 + ["scholar"],
        "temple": ["priest"] * 2 + ["healer"],
        "stormcloak": ["soldier"] * 3 + ["scout"],
        "imperial": ["soldier"] * 3 + ["officer"],
        "darkbrotherhood": ["assassin"] * 2,
        "forsworn": ["barbarian"] * 2 + ["shaman"],
    }

    tag_role_pool = []
    for tag in tags_list:
        if tag in tag_roles:
            tag_role_pool.extend(tag_roles[tag])

    if tag_role_pool and random.random() < 0.5:
        return random.choice(tag_role_pool)
    return random.choice(list(role_pool))


def determine_npc_culture(demographics):
    culture_weights = []
    cultures = []

    for race, percentage in demographics.items():
        race_key = race.lower()
        if race_key != "others":
            cultures.append(race_key)
            culture_weights.append(percentage)

    if not cultures:
        return "nord"

    return random.choices(cultures, weights=culture_weights, k=1)[0]


# Interaction functions
def list_npcs_at_location(location, player):
    try:
        npcs = npc_registry.get(location["id"], [])
        if not npcs:
            UI.slow_print("No souls linger here, save the whispers of the wind.")
            return

        UI.print_heading("Kindred Spirits Nearby")
        for i, npc in enumerate(npcs, 1):
            UI.print_info(f"[{i}] {npc.name} — {npc.role.capitalize()} ({npc.race.capitalize()})")  # Improved NPC display
        UI.print_line()

        sel = UI.print_prompt("With whom do you wish to parley? (0 to pass)").strip()
        if sel.isdigit():
            i = int(sel)
            if 1 <= i <= len(npcs):
                npc = npcs[i - 1]
                if npc.tags.get("npc", {}).get("attitude") == "hostile":  # Check attitude from tags
                    UI.slow_print(f"{npc.name} draws steel, their eyes burning with malice!")
                    combat = Combat(player, [npc], location)
                    combat.run()
                else:
                    npc.dialogue(player, location)
            elif i != 0:
                UI.slow_print("No such soul stands before you.")
    except Exception as e:
        UI.print_failure(f"Error in list_npcs_at_location: {e}")
        traceback.print_exc()


def share_random_rumor(current_location_param):
    try:
        if not current_location_param:
            return
        # Removed RUMOR_POOL as it's not defined and flavor module handles this
        UI.slow_print("You hear a faint whisper of a rumor...")
        # A more robust implementation would fetch a relevant rumor from flavor.py
    except Exception as e:
        UI.print_failure(f"Error in share_random_rumor: {e}")


def combat_demo(player, current_location_param):
    try:
        enemy = NPC(
            name="Bandit Raider", level=player.level, race="Nord", role="bandit"  # Added race
        )
        combat = Combat(player, [enemy], current_location_param)  # Changed npc to enemy, use current_location_param
        combat.run()
    except Exception as e:
        UI.print_failure(f"Error in combat_demo: {e}")
        traceback.print_exc()


def look_around_area(player, current_location_param, random_encounters, npc_registry, LOCATIONS, UI):
    """
    A new function to allow the player to 'look around' their current location.
    This will trigger exploration results and potentially random events/quests.
    """
    # current_location is passed as a parameter, no global declaration needed
    UI.slow_print(f"You take a moment to observe your surroundings in {current_location_param['name']}...")
    explore_location(player, current_location_param, random_encounters, npc_registry, LOCATIONS, UI)
    
    # After exploring, there's a chance to trigger a quest from the environment
    if random.random() < 0.3:  # 30% chance to find a quest by looking around
        new_quest = generate_location_appropriate_quest(player.level, current_location_param["tags"])
        if new_quest:
            UI.slow_print("\nYou notice something that piques your interest. A new quest appears!")
            UI.slow_print(f"Quest: {new_quest.title} - {new_quest.description}")  # Display title and description
            
            # Format reward display
            reward_parts = []
            for r_type, r_value in new_quest.reward.items():
                if isinstance(r_value, Item):
                    reward_parts.append(f"{r_value.name} (Item)")
                else:
                    reward_parts.append(f"{r_value} {r_type.capitalize()}")
            UI.slow_print(f"Reward: {', '.join(reward_parts)}")
            
            player.quest_log.add_quest(new_quest)
    return current_location_param  # Return current_location_param


# Initialization functions
def initialize_player():
    try:
        UI.slow_print("Choose your race:")
        # Display race options using the keys of the RACES dictionary
        race_options = list(RACES.keys())
        for i, race_name in enumerate(race_options):
            UI.slow_print(f"[{i+1}] {race_name.capitalize()}")

        player_race_str = "nord"  # Default to lowercase for consistency with RACES keys
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
        UI.slow_print(f"You have chosen to be a {player_race_str.capitalize()}.")


        UI.slow_print("\nChoose your class:")
        class_options_keys = list(CLASSES.keys())
        for i, class_id in enumerate(class_options_keys):
            class_data = CLASSES[class_id]
            UI.slow_print(f"[{i+1}] {class_data['name']} - {class_data['desc']}")

        selected_class_data = CLASSES["warrior"]  # Default to Warrior data
        selected_class_name = "Warrior"  # Default to Warrior name
        while True:
            class_choice_input = UI.print_prompt("Enter the number of your chosen class")
            try:
                class_index = int(class_choice_input) - 1
                if 0 <= class_index < len(class_options_keys):
                    chosen_class_key = class_options_keys[class_index]
                    selected_class_data = CLASSES[chosen_class_key]
                    selected_class_name = selected_class_data['name']
                    break
                else:
                    UI.slow_print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                UI.slow_print("Invalid input. Please enter a number.")
        UI.slow_print(f"You have chosen the {selected_class_name} class.")


        UI.slow_print(f"\nChoose your {selected_class_name} subclass:")
        subclass_options_keys = list(selected_class_data["subclasses"].keys())
        for i, subclass_id in enumerate(subclass_options_keys):
            subclass_data = selected_class_data["subclasses"][subclass_id]
            UI.slow_print(f"[{i+1}] {subclass_data['name']}")

        selected_subclass_data = list(selected_class_data["subclasses"].values())[0]  # Default to first subclass
        selected_subclass_name = selected_subclass_data['name']  # Default to first subclass name
        while True:
            subclass_choice_input = UI.print_prompt("Enter the number of your chosen subclass")
            try:
                subclass_index = int(subclass_choice_input) - 1
                if 0 <= subclass_index < len(subclass_options_keys):
                    chosen_subclass_key = subclass_options_keys[subclass_index]
                    selected_subclass_data = selected_class_data["subclasses"][chosen_subclass_key]
                    selected_subclass_name = selected_subclass_data['name']
                    break
                else:
                    UI.slow_print("Invalid choice. Please. enter a number from the list.")
            except ValueError:
                UI.slow_print("Invalid input. Please enter a number.")
        UI.slow_print(f"You have chosen the {selected_subclass_name} subclass.")


        player_name = ""
        while not player_name:
            player_name = UI.print_prompt("Speak your name, traveler")
            if not player_name:
                UI.slow_print(
                    "A name is required for your legend to be sung in the halls of Sovngarde."
                )

        player = Player(
            player_name,
            player_race_str,  # Pass the string name of the race
            selected_class_name,  # Pass the string name of the class
            selected_subclass_name,
            attributes=selected_subclass_data["attributes"],
            skills=selected_subclass_data["skills"],
        )

        for item_name in selected_subclass_data["inventory"]:  # Use selected_subclass_data for initial inventory
            # Use generate_item_from_key for specific starting items
            item = generate_item_from_key(item_name.lower().replace(" ", "_"), player.level)
            player.add_item(item)
            if item.category in ["weapon", "armor"]:
                player.equip_item(item)

        player.quest_log = QuestLog()  # Ensure QuestLog is initialized here
        return player

    except Exception as e:
        UI.print_failure(f"Error in initialize_player: {e}")
        traceback.print_exc()
        return None


def initialize_starting_location():
    # current_location is initialized globally and returned
    # No global declaration needed here, as it's assigned once and then returned.
    
    hold_locations = [
        loc
        for loc in ALL_LOCATIONS
        if "hold" in loc.get("tags", []) and "sub_locations" in loc
    ]

    if not hold_locations:
        UI.slow_print("No suitable holds found. Defaulting to Whiterun.")
        default_location = next(
            (loc for loc in ALL_LOCATIONS if loc["name"] == "Whiterun Hold"),
            ALL_LOCATIONS[0],
        )
        # current_location is assigned here, but it's the *initial* assignment, not a modification within a loop
        # so global keyword is not strictly required if it's only assigned once and then returned.
        # For consistency with the new pattern, we'll return it.
        new_current_location = default_location
        known_locations.add(new_current_location["id"])
        discover_connected_locations(new_current_location)
        generate_npcs_for_location(new_current_location)
        return new_current_location  # Return the initialized location

    # Find cities within the holds
    city_locations = []
    for hold in hold_locations:
        for sub_loc in hold.get("sub_locations", []):
            if "city" in sub_loc.get("tags", []):
                city_locations.append(sub_loc)

    if not city_locations:
        UI.slow_print("No suitable cities found. Defaulting to Whiterun.")
        default_location = next(
            (loc for loc in ALL_LOCATIONS if loc["name"] == "Whiterun Hold"),
            ALL_LOCATIONS[0],
        )
        new_current_location = default_location
        known_locations.add(new_current_location["id"])
        discover_connected_locations(new_current_location)
        generate_npcs_for_location(new_current_location)
        return new_current_location  # Return the initialized location

    start_city = random.choice(city_locations)
    tavern_locations = [
        sub_loc
        for sub_loc in start_city.get("sub_locations", [])
        if any(tag.lower() in ["tavern", "inn"] for tag in sub_loc.get("tags", []))
    ]

    if not tavern_locations:
        UI.slow_print(f"No taverns found in {start_city['name']}. Defaulting to Whiterun.")
        default_location = next(
            (loc for loc in ALL_LOCATIONS if loc["name"] == "Whiterun Hold"),
            ALL_LOCATIONS[0],
        )
        new_current_location = default_location
        known_locations.add(new_current_location["id"])
        discover_connected_locations(new_current_location)
        generate_npcs_for_location(new_current_location)
        return new_current_location  # Return the initialized location

    new_current_location = random.choice(tavern_locations)
    
    # Find the parent hold and add it to known locations if not already
    parent_hold = next((hold for hold in ALL_LOCATIONS if start_city in hold.get("sub_locations", [])), None)
    if parent_hold:
        known_locations.add(parent_hold["id"])
        discover_connected_locations(parent_hold)  # Discover from the hold
    
    known_locations.add(start_city["id"])  # Add the city
    known_locations.add(new_current_location["id"])  # Add the tavern
    
    # Also discover connections directly from the starting city
    discover_connected_locations(start_city)

    message = f"You awaken in {new_current_location['name']}, a cozy tavern in {start_city['name']}..."
    UI.slow_print(message.replace("tavernrn", "tavern"))
    
    UI.slow_print("The warm fire crackles as patrons share tales over mugs of mead.")
    return new_current_location  # Return the initialized location


def initialize_game_state():
    global game_start_time, known_locations, npc_registry, random_encounters  # Declare all global variables modified here
    game_start_time = datetime.now(timezone.utc)

    known_locations.clear()
    npc_registry.clear()
    random_encounters.clear()


# Main game loop
def start_game():
    global current_location  # Declare global here to modify it based on function returns
    try:
        initialize_game_state()

        player = initialize_player()
        if not player:
            return

        current_location = initialize_starting_location()  # Assign the returned location

        if current_location["id"] not in random_encounters:
            random_encounters[current_location["id"]] = []
            for _ in range(random.randint(1, 3)):
                encounter = generate_random_encounter(current_location["tags"])
                if encounter:
                    random_encounters[current_location["id"]].append(encounter)

        # Removed automatic quest assignment at startup

        while True:
            # Fix: Use restore_fatigue and restore_magicka
            player.stats.restore_fatigue(5)
            player.stats.restore_magicka(5)

            if player.stats.current_encumbrance > player.stats.encumbrance_limit:
                player.stats.speed = max(10, player.stats.speed - 10)
                player.stats.dodge_chance = max(0.05, player.stats.dodge_chance - 0.1)
                UI.slow_print("Your heavy load slows your steps and hinders your agility.")
            else:
                # Revert speed/dodge to base attributes if encumbrance isn't an issue
                # This needs proper base values to be stored in player.stats or attributes
                # For simplicity, if they aren't penalized, they are at full capacity.
                # A more robust system would re-calculate from base attributes.
                pass 

            UI.print_menu([
                "Seek Known Realms",
                "Journey Forth",
                "Parley with Souls",
                "Behold Thy Spirit",
                "Test Thy Steel",
                "Inspect Thy Possessions",
                "Look Around the Area",  # Added new menu option
                "Review Quest Log",
                "Use Item",
                "Depart This Realm"
            ])

            choice = UI.print_prompt("What is your will? ").strip()

            if choice == "0":
                UI.slow_print("Farewell, until the stars call you back!")
                break

            # handle_player_choice now returns the potentially updated current_location
            current_location = handle_player_choice(choice, player, current_location)

            # Random event after each action, but only with a chance
            if current_location and random.random() < 0.25:  # 25% chance for a random event each turn
                trigger_random_event(current_location["tags"], player, UI, current_location)


    except Exception as e:
        UI.print_failure(f"Error in start_game: {e}")
        traceback.print_exc()
    finally:
        input("Press Enter to exit...")


def handle_player_choice(choice, player, current_location_param):  # current_location passed as parameter
    # current_location is not declared global here, it's passed as a parameter
    # and the new value will be returned.
    
    new_current_location = current_location_param  # Initialize with current value

    if choice == "1":
        list_locations()
    elif choice == "2":
        new_current_location = travel_menu(player, current_location_param)  # Pass and receive
    elif choice == "3":
        if current_location_param:
            list_npcs_at_location(current_location_param, player)
        else:
            UI.slow_print("First, you must tread a path to meet the living.")
    elif choice == "4":
        UI.display_player_stats(player)  # Use UI method
    elif choice == "5":
        new_current_location = combat_demo(player, current_location_param)  # Pass and receive
    elif choice == "6":
        UI.display_inventory(player)  # Use UI method
    elif choice == "7":  # Mapped to "Look Around the Area"
        new_current_location = look_around_area(player, current_location_param, random_encounters, npc_registry, LOCATIONS, UI)  # Pass and receive
    elif choice == "8":
        UI.display_quest_log(player)  # Use UI method
    elif choice == "9":
        handle_item_use(player)
    else:
        UI.slow_print("Your will wavers.")
        
    return new_current_location  # Return the potentially updated location


def handle_item_use(player):
    UI.slow_print("Inventory:")
    if not player.inventory:
        UI.slow_print("Your inventory is empty.")
        return

    for i, item in enumerate(player.inventory, 1):
        UI.slow_print(f"[{i}] {item.get_description()}")  # Use get_description for detailed view

    item_index = UI.print_prompt(
        "Which item do you want to use? (Enter the item number, 0 to cancel)"
    )
    if item_index.isdigit():
        item_index = int(item_index) - 1
        if 0 <= item_index < len(player.inventory):
            item = player.inventory[item_index]
            item.use(player)
            # item.use() now handles removal and encumbrance update internally
        else:
            UI.slow_print("Invalid item number.")
    else:
        UI.slow_print("Invalid input.")


if __name__ == "__main__":
    start_game()