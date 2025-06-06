import json
# exploration.py
from typing import Dict, List, Any, Optional # Added Optional
from player import Player
from ui import UI
import tags # For INHERITABLE_TAGS
from npc_generation import generate_npcs_for_location # For process_travel

from locations import Location, LocationManager

#from locations import LOCATIONS, Location, RAW_LOCATION_DATA_MAP # Added Location, RAW_LOCATION_DATA_MAP

#_ALL_LOCATIONS_EXPLORATION = LOCATIONS
#_LOCATION_BY_ID_EXPLORATION = {}
#_LOCATION_BY_NAME_EXPLORATION = {}

#def _build_exploration_location_maps(loc_list):
#    by_id = {}
#    by_name = {}
#    def recurse(loc):
#        by_id[loc["id"]] = loc
#        by_name[loc["name"]] = loc
#        for sub in loc.get("sub_locations", []):
#            recurse(sub)
#    for top in loc_list:
#        recurse(top)
#    return by_id, by_name

#_LOCATION_BY_ID_EXPLORATION, _LOCATION_BY_NAME_EXPLORATION = _build_exploration_location_maps(_ALL_LOCATIONS_EXPLORATION)


def get_hold_by_id(hold_id: int) -> Dict[str, Any] | None:
    """Finds a hold by its ID from ALL_LOCATIONS."""
    location_manager = LocationManager()
    for loc in location_manager.locations.values():
        if loc.id == hold_id and "hold" in loc.tags:
            return {"id": loc.id, "name": loc.name, "tags": loc.tags}
    return None

def get_known_holds(player: Player) -> List[Dict[str, Any]]:
    """Returns a sorted list of Hold location objects known by the player."""
    known_holds = []
    location_manager = LocationManager()
    for loc_id in player.known_location_ids:
        loc_obj = location_manager.get_location(loc_id)
        if loc_obj and "hold" in loc_obj.tags:
            known_holds.append({"id": loc_obj.id, "name": loc_obj.name, "tags": loc_obj.tags})
    return sorted(known_holds, key=lambda x: x.get("name", ""))

def get_known_primary_locations_in_hold(player: Player, hold_id: int) -> List[Dict[str, Any]]:
    """
    Returns a list of known primary locations (cities, towns, standalone dungeons, etc.)
    that are direct children of the specified hold.
    """
    known_locs_in_hold = []
    hold_obj = get_hold_by_id(hold_id)
    if not hold_obj:
        return []

    location_manager = LocationManager()
    for loc_id, loc_obj in location_manager.locations.items():
        if loc_obj.parent_id == hold_id and loc_obj.id in player.known_location_ids:
            known_locs_in_hold.append({"id": loc_obj.id, "name": loc_obj.name, "tags": loc_obj.tags})
    
    return sorted(known_locs_in_hold, key=lambda x: x.get("name", ""))

def get_known_sub_locations(player: Player, parent_loc_id: int) -> List[Dict[str, Any]]:
    """
    Returns a list of known sub-locations (e.g., venues in a city)
    for a given parent location ID.
    """
    known_subs = []
    location_manager = LocationManager()
    parent_loc_obj = location_manager.get_location(parent_loc_id)
    if not parent_loc_obj:
        return []

    for sub_loc_id in parent_loc_obj.sub_locations:
        sub_loc_obj = location_manager.get_location(sub_loc_id)
        if sub_loc_obj and sub_loc_obj.id in player.known_location_ids:
            known_subs.append({"id": sub_loc_obj.id, "name": sub_loc_obj.name, "tags": sub_loc_obj.tags})
            
    return sorted(known_subs, key=lambda x: x.get("name", ""))

def determine_city_type(city_obj: Dict[str, Any]) -> str:
    """Determines the display type string for a city-level location."""
    loc_tags = city_obj.get("tags", []) # Renamed to avoid conflict with tags module
    if "city" in loc_tags: return "City"
    if "town" in loc_tags: return "Town"
    if "village" in loc_tags: return "Village"
    if "barrow" in loc_tags or "nordic_ruin" in loc_tags: return "Ruin/Barrow"
    if "cave" in loc_tags: return "Cave System"
    if "mine" in loc_tags: return "Mine"
    if "camp" in loc_tags: return "Camp"
    if "watchtower" in loc_tags: return "Watchtower"
    if "fort" in loc_tags and "ruined" not in loc_tags : return "Fort"
    if "dungeon" in loc_tags : return "Dungeon Site"
    return "Settlement"

def determine_venue_type(venue_obj: Dict[str, Any]) -> str:
    """Determines the display type string for a venue-level location."""
    loc_tags = venue_obj.get("tags", []) # Renamed to avoid conflict with tags module
    if "tavern" in loc_tags or "inn" in loc_tags: return "Tavern/Inn"
    if "shop" in loc_tags and "alchemy" in loc_tags : return "Apothecary"
    if "shop" in loc_tags and "blacksmith" in loc_tags : return "Smithy"
    if "shop" in loc_tags: return "Shop"
    if "keep" in loc_tags or ("jarls_seat" in loc_tags and "palace" not in loc_tags and "longhouse" not in loc_tags): return "Keep"
    if "palace" in loc_tags or ("jarls_seat" in loc_tags and ("palace" in loc_tags or "longhouse" in loc_tags)): return "Palace/Longhouse"
    if "temple" in loc_tags: return "Temple"
    if "guild" in loc_tags or "college" in loc_tags or "meadhall" in loc_tags : return "Guild/College Hall"
    if "residence" in loc_tags: return "Residence"
    if "market" in loc_tags : return "Market Area"
    if "docks" in loc_tags: return "Docks"
    if "catacombs" in loc_tags or "hall_of_the_dead" in loc_tags : return "Catacombs"
    return "Point of Interest"

from typing import Optional # Add Optional to existing typing imports if not already present
# If Location or RAW_LOCATION_DATA_MAP are not imported at the top, add:
# from locations import Location, RAW_LOCATION_DATA_MAP

def display_world_map(player: Player, game_locations_map: Dict[int, Location]): # game_locations_map is the main map from game.py
    UI.clear_screen()
    UI.print_heading("World Map - Known Locations")

    if not player.known_locations_objects:
        UI.print_info("You haven't discovered any locations yet.")
        UI.press_enter()
        return

    known_locs_map: Dict[int, Location] = {loc.id: loc for loc in player.known_locations_objects if isinstance(loc, Location)}

    children_by_parent_id: Dict[Optional[int], List[Location]] = {}
    for loc_id, loc_obj in known_locs_map.items():
        pid = loc_obj.parent_id
        if pid not in children_by_parent_id:
            children_by_parent_id[pid] = []
        children_by_parent_id[pid].append(loc_obj)

    for pid_key in children_by_parent_id:
        children_by_parent_id[pid_key].sort(key=lambda x: x.name)
    
    processed_ids = set()

    def _get_loc_type_str(loc_data_dict: Dict[str, Any]) -> str:
        type_str = determine_city_type(loc_data_dict) # Uses existing function in exploration.py
        if type_str == "Settlement": 
            type_str = determine_venue_type(loc_data_dict) # Uses existing function
            if type_str == "Point of Interest":
                 if "hold" in loc_data_dict.get("tags", []): return "(Hold)"
                 return ""
        return f"({type_str})"

    def _recursive_print(parent_id: Optional[int], indent_level: int):
        if parent_id not in children_by_parent_id:
            return

        for child_loc in children_by_parent_id[parent_id]:
            if child_loc.id in processed_ids:
                continue
            
            indent = "  " * indent_level
            # RAW_LOCATION_DATA_MAP should be imported from locations module
            #raw_data_for_type = RAW_LOCATION_DATA_MAP.get(child_loc.id, {})
            raw_data_for_type = {"tags": child_loc.tags, "travel_desc": child_loc.travel_desc, "desc": child_loc.description}
            type_display_str = _get_loc_type_str(raw_data_for_type)
            travel_desc = raw_data_for_type.get("travel_desc", raw_data_for_type.get("desc", ""))

            UI.print_info(f"{indent}- {child_loc.name} {type_display_str} - {travel_desc}")
            processed_ids.add(child_loc.id)
            _recursive_print(child_loc.id, indent_level + 1)

    root_locations_to_print: List[Location] = []
    for loc_id, loc_obj in known_locs_map.items():
        is_true_root = loc_obj.parent_id is None
        is_orphaned_known_root = loc_obj.parent_id is not None and loc_obj.parent_id not in known_locs_map
        
        if is_true_root or is_orphaned_known_root:
            if loc_obj.id not in processed_ids:
                 root_locations_to_print.append(loc_obj)
    
    # Sort roots: Holds first, then by name
    root_locations_to_print.sort(key=lambda x: (
        not (x.tags and "hold" in x.tags),
        x.name
    ))

    for root_loc in root_locations_to_print:
        if root_loc.id not in processed_ids:
            #raw_data_for_type = RAW_LOCATION_DATA_MAP.get(root_loc.id, {})
            raw_data_for_type = {"tags": root_loc.tags, "travel_desc": root_loc.travel_desc, "desc": root_loc.description}
            type_display_str = _get_loc_type_str(raw_data_for_type)
            travel_desc = raw_data_for_type.get("travel_desc", raw_data_for_type.get("desc", ""))
            UI.print_info(f"- {root_loc.name} {type_display_str} - {travel_desc}")
            processed_ids.add(root_loc.id)
            _recursive_print(root_loc.id, 1)

    UI.press_enter()
def discover_connected_locations(player: Player, location_data: dict, location_by_name_map: Dict[str, Any]):
    """
    Discovers locations connected to the given location_data and updates
    the player's known_location_ids and known_locations_objects.
    """
    for mode in ("roads", "paths"):
        for dest_name in location_data.get("travel", {}).get(mode, []):
            dest_loc_obj = location_by_name_map.get(dest_name)
            if dest_loc_obj:
                if dest_loc_obj["id"] not in player.known_location_ids:
                    player.known_location_ids.add(dest_loc_obj["id"])
                    if dest_loc_obj not in player.known_locations_objects:
                        player.known_locations_objects.append(dest_loc_obj)

def process_travel(player: Player, destination_loc_obj: Dict[str, Any], previous_location_obj: Dict[str, Any],
                   find_hierarchy_func, get_flavor_text_func, npc_registry_arg, 
                   generate_npcs_func, discover_connected_locations_func, 
                   location_by_name_map, exploration_events) -> Dict[str, Any]:
    UI.clear_screen()
    UI.print_heading(f"Traveling to {destination_loc_obj['name']}")

    player.current_location_obj = destination_loc_obj
    player.update_current_location_for_quest(destination_loc_obj)

    if "sub_locations" in destination_loc_obj:
        for sub_loc_to_discover in destination_loc_obj.get("sub_locations", []):
            if sub_loc_to_discover["id"] not in player.known_location_ids:
                player.known_location_ids.add(sub_loc_to_discover["id"])
                if sub_loc_to_discover not in player.known_locations_objects:
                    player.known_locations_objects.append(sub_loc_to_discover)
    
    discover_connected_locations_func(player, destination_loc_obj, location_by_name_map)

    UI.slow_print(f"You arrive at {destination_loc_obj['name']}.")
    UI.slow_print(destination_loc_obj.get('TRAVEL DESCRIPTION', destination_loc_obj['desc']))

    tags_for_dest = list(destination_loc_obj.get("tags", []))
    inheritable = tags.INHERITABLE_TAGS if hasattr(tags, 'INHERITABLE_TAGS') else set()
    
    parent_hold, parent_city = find_hierarchy_func(destination_loc_obj["id"])
    contextual_parent = None
    if parent_city and parent_city["id"] != destination_loc_obj["id"]:
        contextual_parent = parent_city
    elif parent_hold and parent_hold["id"] != destination_loc_obj["id"]:
        contextual_parent = parent_hold
    
    if contextual_parent:
        tags_for_dest.extend([t for t in contextual_parent.get("tags", []) if t in inheritable])
    tags_for_dest = list(set(tags_for_dest))

    UI.slow_print(get_flavor_text_func(tags_for_dest, "location_tags", ensure_vignette=True))
    
    generate_npcs_func(destination_loc_obj, npc_registry_arg, find_hierarchy_func)

    # Trigger exploration event
    trigger_exploration_event(player, destination_loc_obj["id"], exploration_events)

    return destination_loc_obj

def load_exploration_events(file_path: str) -> List[Dict[str, Any]]:
    """Loads exploration events from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            events = json.load(f)
        return events
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}.")
        return []

def trigger_exploration_event(player: Player, location_id: str, exploration_events: List[Dict[str, Any]]):
    """Triggers an exploration event based on the location and player's stats."""
    import random
    eligible_events = [
        event for event in exploration_events
        if event["location_id"] == location_id
    ]

    if not eligible_events:
        return

    for event in eligible_events:
        # Check triggers
        triggers_met = True
        for trigger in event.get("triggers", []):
            if trigger["type"] == "skill_check":
                skill = trigger["skill"]
                threshold = trigger["threshold"]
                if player.get_skill_value(skill) < threshold:
                    triggers_met = False
                    break
            elif trigger["type"] == "random":
                probability = trigger["probability"]
                if random.random() > probability:
                    triggers_met = False
                    break
            elif trigger["type"] == "location_visited":
                # Check if the player has visited the location before
                location_id_to_check = trigger.get("location_id")
                if location_id_to_check not in player.known_location_ids:
                    triggers_met = False
                    break

        if triggers_met:
            UI.clear_screen()
            UI.print_info(event["description"])

            # Handle challenges
            for challenge in event.get("challenges", []):
                if challenge["type"] == "puzzle":
                    UI.print_info(challenge["description"])
                    # Implement puzzle logic here (e.g., ask the player a question)
                    player_answer = UI.get_player_input("What is your answer? ")
                    if player_answer.lower() == "the answer":  # Replace with actual answer
                        UI.print_info("You solved the puzzle!")
                    else:
                        UI.print_info("Incorrect answer.")
                        return
                elif challenge["type"] == "trap":
                    UI.print_info(challenge["description"])
                    # Implement trap logic here (e.g., skill check to avoid trap)
                    if random.random() < 0.5:
                        UI.print_info("You avoided the trap!")
                    else:
                        UI.print_info("You fell into the trap and took some damage!")
                        player.take_damage(10)  # Example damage
                        return
                elif challenge["type"] == "combat":
                    UI.print_info("You are attacked!")
                    # Implement combat logic here
                    # This is a placeholder, replace with actual combat implementation
                    return

            # Handle rewards
            for reward in event.get("rewards", []):
                if reward["type"] == "item":
                    item_id = reward["item_id"]
                    quantity = reward["quantity"]
                    player.add_item(item_id, quantity)
                    UI.print_info(f"You received {quantity} {item_id}!")
                elif reward["type"] == "experience":
                    amount = reward["amount"]
                    player.add_experience(amount)
                    UI.print_info(f"You gained {amount} experience!")
                elif reward["type"] == "access":
                    area_id = reward["area_id"]
                    # Implement access logic here (e.g., unlock a new area)
                    UI.print_info(f"You gained access to {area_id}!")

            UI.press_enter()
            return

def explore_and_travel_menu(player: Player, current_location_param: Dict[str, Any], 
                            process_travel_func, find_hierarchy_func, get_flavor_text_func, 
                            npc_registry_arg, generate_npcs_func, discover_connected_locations_func, 
                            location_by_name_map) -> Dict[str, Any]:
    while True:
        known_holds = get_known_holds(player)
        if not known_holds:
            UI.clear_screen()
            UI.print_heading("World Map")
            UI.print_info("You have not yet discovered any major Holds in Skyrim.")
            UI.press_enter()
            return current_location_param

        selected_hold = UI.select_from_paginated_list(
            options=[{"name": h["name"], "id": h["id"], "obj": h} for h in known_holds],
            prompt_message="Select a Hold to view its locations (or 0 to cancel):"
        )
        if not selected_hold:
            return current_location_param
        
        selected_hold_obj = selected_hold["obj"]

        while True:
            known_primary_locs = get_known_primary_locations_in_hold(player, selected_hold_obj["id"])
            
            if not known_primary_locs:
                UI.clear_screen()
                UI.print_heading(f"Locations in {selected_hold_obj['name']}")
                UI.print_info(f"You have not discovered any specific locations within {selected_hold_obj['name']} yet, beyond the Hold itself.")
                options_for_empty_hold = [{"name": f"Explore {selected_hold_obj['name']} (General Area)", "id": selected_hold_obj["id"], "obj": selected_hold_obj, "is_general_hold": True}]
                
                chosen_action_for_empty_hold = UI.select_from_paginated_list(
                    options=options_for_empty_hold,
                    prompt_message=f"Choose an action for {selected_hold_obj['name']} (or 0 to go back to Hold selection):"
                )
                if not chosen_action_for_empty_hold:
                    break 
                
                if chosen_action_for_empty_hold.get("is_general_hold"):
                    if current_location_param["id"] == selected_hold_obj["id"]:
                        UI.print_info(f"You are already in the general area of {selected_hold_obj['name']}.")
                        UI.press_enter()
                        break
                    else:
                        return process_travel_func(player, selected_hold_obj, current_location_param, 
                                                 find_hierarchy_func, get_flavor_text_func, 
                                                 npc_registry_arg, generate_npcs_func, 
                                                 discover_connected_locations_func, location_by_name_map,load_exploration_events("exploration_events.json"))
                else:
                    break

            primary_loc_options = [{"name": f"{loc['name']} ({determine_city_type(loc)})", "id": loc["id"], "obj": loc} for loc in known_primary_locs]
            
            selected_primary_loc_choice = UI.select_from_paginated_list(
                options=primary_loc_options,
                prompt_message=f"Locations in {selected_hold_obj['name']} (or 0 to go back to Hold selection):"
            )

            if not selected_primary_loc_choice:
                break 
            
            selected_primary_loc_obj = selected_primary_loc_choice["obj"]
            final_destination_obj = selected_primary_loc_obj

            known_sub_locs = get_known_sub_locations(player, selected_primary_loc_obj["id"])
            
            if known_sub_locs:
                sub_loc_options = [{"name": f"{sub['name']} ({determine_venue_type(sub)})", "id": sub["id"], "obj": sub} for sub in known_sub_locs]
                sub_loc_options.insert(0, {"name": f"{selected_primary_loc_obj['name']} (Main Area)", "id": selected_primary_loc_obj["id"], "obj": selected_primary_loc_obj, "is_main_area": True})

                selected_sub_loc_choice = UI.select_from_paginated_list(
                    options=sub_loc_options,
                    prompt_message=f"Specific places within {selected_primary_loc_obj['name']} (or 0 to go back to locations in {selected_hold_obj['name']}):"
                )

                if not selected_sub_loc_choice:
                    continue 
                
                final_destination_obj = selected_sub_loc_choice["obj"]
            
            if current_location_param["id"] == final_destination_obj["id"]:
                UI.clear_screen()
                UI.print_info(f"You are already at {final_destination_obj['name']}.")
                UI.press_enter()
                return current_location_param
            else:
                return process_travel_func(player, final_destination_obj, current_location_param,
                                         find_hierarchy_func, get_flavor_text_func,
                                         npc_registry_arg, generate_npcs_func,
                                         discover_connected_locations_func, location_by_name_map,load_exploration_events("exploration_events.json"))
    return current_location_param