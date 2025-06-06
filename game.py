import random
import logging
from datetime import datetime, timezone, timedelta
import time
import traceback

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

def add_random_item_with_rarity(player, category, rarity):
    """Adds a random item of a specified category and rarity to the player's inventory."""
    item = generate_random_item(category, rarity=rarity)
    if hasattr(player, 'add_item'): # Prefer using an add_item method if available
        player.add_item(item)
    elif hasattr(player, 'stats') and hasattr(player.stats, 'inventory'):
        player.stats.inventory.append(item)
    elif hasattr(player, 'inventory'): # Fallback, though less ideal
        player.inventory.append(item)
    else:
        print("Player has no inventory.")
    print(f"Added {item.name} to inventory.")

# game.py

import time
import traceback
from datetime import datetime, timezone, timedelta

# --- Main Game Imports (Corrected) ---
try:
    from locations import Location, LocationManager
    from player import Player
    from stats import Stats, RACES, CLASSES
    from npc_entities import NPC
    from combat import Combat  # CORRECT: Imports the main Combat class
    from ui import UI
    from items import generate_random_item, Item, generate_item_from_key, Torch
    from events import trigger_random_event
    from quests import QuestLog, generate_location_appropriate_quest, Quest, process_quest_rewards
    from character_creation import initialize_player
    from npc_generation import generate_npcs_for_location
    from exploration import display_world_map, explore_and_travel_menu
    from inventory_manager import handle_inventory_menu, handle_item_use
    from combat_interactions import combat_demo, list_npcs_at_location  # CORRECT: Imports from combat_interactions
    from npc_dialogue_logic import handle_npc_dialogue
    from game_events import initialize_game_events, check_and_trigger_events
    from events import explore_location
    import tags
    import flavor
    from rumors import generate_rumor

except ImportError as e:
    print(f"Error importing modules: {e}")
    traceback.print_exc()
    input("Press Enter to exit...")
    exit(1)


# Globals
npc_registry = {}
location_manager = LocationManager()
GAME_LOCATIONS_MAP = location_manager.locations # Will store Location objects, keyed by ID
action_time_map = {
    "travel": 120,
    "search": 45,
    "rest": 480,
    "craft": 360,
    "combat": 30,
    "dialogue": 5,
    "wait / pass time": 60,
    "look around the area": 15
}

# --- Utility & Helper Functions ---
ENCOUNTER_NAMES = {
    "city": [
        {"name": "Street Urchin", "desc": "A nimble child attempts to pickpocket you.", "type": "thieves_encounter"},
        {"name": "Drunkard",    "desc": "A staggering drunkard accosts you for coin.", "type": "social_encounter"},
        {"name": "Wolf Pack",     "desc": "A pack of wolves circles, seeking prey.", "type": "hostile_creatures"},
        {"name": "Lost Traveler", "desc": "A lost traveler asks for directions.", "type": "social_encounter"},
    ],
    "forest": [
        {"name": "Merchant Caravan", "desc": "A well-guarded merchant caravan passes by.", "type": "neutral_encounter"},
        {"name": "Lone Elk", "desc": "A majestic elk grazes peacefully.", "type": "neutral_creature"}
    ],
    "plains": [
        {"name": "Rockslide", "desc": "The ground trembles as rocks tumble down a nearby slope!", "type": "hazard_event"},
        {"name": "Goat Herd", "desc": "A herd of mountain goats skillfully navigates the cliffs.", "type": "neutral_creature"}
    ],
    "mountain": [
        {"name": "Bear", "desc": "A large bear growls from the darkness.", "type": "hostile_creatures"},
        {"name": "Lost Explorer's Note", "desc": "You find a tattered note, the last words of a lost explorer.", "type": "lore_find"}
    ],
    "cave": [
        {"name": "Restless Spirit", "desc": "A ghostly figure materializes, bound to these ancient stones.", "type": "undead_encounter"},
        {"name": "Ancient Trap", "desc": "You narrowly avoid an ancient, cunningly hidden trap.", "type": "hazard_event"}
    ],
    "ruin": [
        {"name": "Street Urchin", "desc": "A nimble child attempts to pickpocket you.", "type": "thieves_encounter"},
        {"name": "Drunkard",    "desc": "A staggering drunkard accosts you for coin.", "type": "social_encounter"},
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
            else:
                self.tags[category_] = final_tags_list
    entity = DummyEntity(tags_filtered, category)
    vignettes = flavor.get_flavor(entity) if hasattr(flavor, 'get_flavor') else []
    if not vignettes and ensure_vignette:
        return "The air is thick with untold stories."
    return random.choice(vignettes) if vignettes else ""

def get_location_obj_by_name(name):
    for loc_obj in GAME_LOCATIONS_MAP.values():
        if loc_obj.name == name:
            return loc_obj
    return None

def get_location_raw_data(loc_id):
    location = GAME_LOCATIONS_MAP.get(loc_id)
    if location:
        return {
            "id": location.id,
            "name": location.name,
            "desc": location.description,
            "travel_desc": location.travel_desc,
            "tags": location.tags,
            "demographics": location.demographics,
            "density": location.density,
            "is_dark": location.is_dark,
            "travel": location.travel,
            "sub_locations": location.sub_locations
        }
    return None

def _find_hierarchy(loc_id_or_obj):
    if isinstance(loc_id_or_obj, Location):
        target_loc_obj = loc_id_or_obj
    else:
        target_loc_obj = GAME_LOCATIONS_MAP.get(loc_id_or_obj)
    if not target_loc_obj:
        return None, None, None
    lineage = []
    current = target_loc_obj
    while current:
        lineage.append(current)
        if current.parent_id:
            current = GAME_LOCATIONS_MAP.get(current.parent_id)
        else:
            break
    lineage.reverse()
    hold_obj = lineage[0] if len(lineage) > 0 else None
    primary_obj = lineage[1] if len(lineage) > 1 else hold_obj
    specific_obj = lineage[2] if len(lineage) > 2 else (primary_obj if len(lineage) > 1 else hold_obj)
    if target_loc_obj == hold_obj:
        return hold_obj, hold_obj, hold_obj
    if target_loc_obj == primary_obj:
        return hold_obj, primary_obj, primary_obj
    return hold_obj, primary_obj, specific_obj

def look_around_area(player, current_location_obj: Location, npc_registry_param, game_loc_map_param, ui_param):
    UI.slow_print(f"You take a moment to observe your surroundings in {current_location_obj.name if current_location_obj.name else 'A mysterious place'}...")
    #current_loc_raw_data = get_location_raw_data(current_location_obj.id)
    #if not current_loc_raw_data:
    #    UI.print_warning(f"Could not find raw data for {current_location_obj.name}")
    #    current_loc_raw_data = {"name": current_location_obj.name, "desc": current_location_obj.description, "tags": [], "id": current_location_obj.id}
    explore_location(player, current_location_obj, {}, npc_registry_param, game_loc_map_param, ui_param)
    location_tags = current_location_obj.tags
    if random.random() < 0.25:
        new_quest = generate_location_appropriate_quest(player.level, current_location_obj, None)
        if new_quest:
            UI.slow_print("\nSomething catches your eye... it seems to be a new undertaking!")
            UI.slow_print(f"Quest: {new_quest.title}")
            UI.slow_print(f"Objective: {new_quest.description}")
            if new_quest.current_stage:
                UI.slow_print(f"Current Tasks:")
                for obj in new_quest.current_stage.get("objectives", []):
                    UI.slow_print(f"  - {obj.get('note', 'A task awaits.')}")
            else:
                UI.slow_print("(You feel you should find a way to record such tasks.)")
    return current_location_obj

def handle_player_choice(choice, player, current_loc_obj: Location, menu_options_list, game_time_obj_param):
    action = None
    new_current_location_obj = current_loc_obj
    time_advance_minutes = 0
    game_time_obj = game_time_obj_param

    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(menu_options_list):
            action_text = menu_options_list[choice_num - 1]
            action = action_text.split("(")[0].strip().lower()
            if action == "depart this realm":
                return "QUIT_GAME_SIGNAL", game_time_obj
    else:
        action_input_lower = choice.lower()
        for opt_text in menu_options_list:
            opt_action_part = opt_text.split("(")[0].strip().lower()
            if action_input_lower == opt_action_part or action_input_lower in opt_text.lower():
                action = opt_action_part
                if action == "depart this realm":
                    return "QUIT_GAME_SIGNAL", game_time_obj
                break
    
    if action in action_time_map:
        time_advance_minutes = action_time_map[action]
    
    clear_screen()

    if action == "explore known world":
        UI.print_heading(f"Travel from {current_loc_obj.name}")
        if current_loc_obj.exits:
            UI.slow_print("Available destinations:")
            exit_options = list(current_loc_obj.exits.items())
            for i, (direction, dest_loc_obj) in enumerate(exit_options):
                formatted_direction = ' '.join(word.capitalize() for word in direction.split())
                #description_to_display = RAW_LOCATION_DATA_MAP.get(dest_loc_obj.id, {}).get('travel_desc', RAW_LOCATION_DATA_MAP.get(dest_loc_obj.id, {}).get('desc'))
                description_to_display = dest_loc_obj.travel_desc if hasattr(dest_loc_obj, 'travel_desc') else dest_loc_obj.description
                UI.slow_print(f"{i+1}. {formatted_direction} - {description_to_display}")
            
            travel_choice_str = UI.print_prompt("Where to? (Enter number or 'cancel') ").strip().lower()
            if travel_choice_str != 'cancel':
                try:
                    travel_choice_idx = int(travel_choice_str) - 1
                    if 0 <= travel_choice_idx < len(exit_options):
                        _, new_dest_obj = exit_options[travel_choice_idx]
                        new_current_location_obj = new_dest_obj
                        UI.slow_print(f"Traveling to {new_current_location_obj.name}...")
                        new_current_location_obj.enter(player)
                        generate_npcs_for_location(new_current_location_obj, npc_registry, _find_hierarchy)
                        time_advance_minutes = getattr(new_dest_obj, 'travel_time', 60)
                    else:
                        UI.slow_print("Invalid choice.")
                except ValueError:
                    UI.slow_print("Invalid input.")
        else:
            UI.slow_print("There are no obvious exits from here.")
    elif action == "parley with souls":
        time_advance_minutes = action_time_map.get(action, 5)
        if current_loc_obj:
            list_npcs_at_location(current_loc_obj, player, npc_registry) 
        else:
            UI.slow_print("You must first be somewhere to find others.")
        if new_current_location_obj == current_loc_obj:
            return "NO_EVENT_THIS_TURN", game_time_obj + timedelta(minutes=time_advance_minutes)
    elif action == "behold thy spirit":
        UI.display_player_stats(player)
        return "STATS_MENU_ACTION", game_time_obj 
    elif action == "test thy steel":
        time_advance_minutes = action_time_map.get(action, 30)
        new_current_location_obj = combat_demo(player, current_loc_obj, _find_hierarchy, npc_registry)
    elif action == "inspect thy possessions":
        handle_inventory_menu(player)
    elif action == "look around the area":
        new_current_location_obj = look_around_area(player, current_loc_obj, npc_registry, GAME_LOCATIONS_MAP, UI)
        time_advance_minutes = action_time_map.get(action, 15)
    elif action == "review quest log":
        UI.display_quest_log(player)
        time_advance_minutes = action_time_map.get(action, 5)
    elif action == "view world map":
        display_world_map(player, GAME_LOCATIONS_MAP)
    elif action == "use item from inventory":
        handle_item_use(player)
    elif action == "wait / pass time":
        UI.slow_print("Time passes...")
        time_advance_minutes = action_time_map.get(action, 60)
        for _ in range(time_advance_minutes // 60):
            player.stats.restore_fatigue(max(1, player.stats.level // 2) * 2)
            player.stats.restore_magicka(max(1, player.stats.level // 3) * 2)
        UI.slow_print("You feel somewhat rested.")
    elif action == "depart this realm":
        pass
    else:
        UI.slow_print("Your will wavers, or perhaps the spirits muddle your intent.")

    actions_that_handle_own_prompts = [
        "explore known world", "parley with souls", "inspect thy possessions", 
        "use item from inventory", "depart this realm"
    ]
    if action not in actions_that_handle_own_prompts and action is not None:
        UI.press_enter()

    if time_advance_minutes > 0:
        game_time_obj += timedelta(minutes=time_advance_minutes)
        
    return new_current_location_obj, game_time_obj

def get_current_game_time_string(game_time_obj):
    months = ["Morning Star", "Sun's Dawn", "First Seed", "Rain's Hand", 
              "Second Seed", "Midyear", "Sun's Height", "Last Seed", 
              "Hearthfire", "Frostfall", "Sun's Dusk", "Evening Star"]
    day = game_time_obj.day
    month_name = months[game_time_obj.month - 1]
    year = game_time_obj.year
    hour = game_time_obj.hour
    minute = game_time_obj.minute
    time_of_day_str = "Night"
    if 5 <= hour < 12: time_of_day_str = "Morning"
    elif 12 <= hour < 17: time_of_day_str = "Afternoon"
    elif 17 <= hour < 21: time_of_day_str = "Evening"
    return f"{month_name} {day}, {year} 4E, {hour:02d}:{minute:02d} ({time_of_day_str})"

def initialize_starting_location(player: Player):
    all_taverns = []
    #for loc_id, raw_data in RAW_LOCATION_DATA_MAP.items():
    for loc_id, location_obj in GAME_LOCATIONS_MAP.items():
        #if any(tag in raw_data.get("tags", []) for tag in ["tavern", "inn", "structure_type_inn_building", "settlement_features_tavern"]):
        if any(tag in location_obj.tags for tag in ["tavern", "inn", "structure_type_inn_building", "settlement_features_tavern"]):
            #location_obj = GAME_LOCATIONS_MAP.get(loc_id)
            if location_obj:
                all_taverns.append(location_obj)
    starting_loc_obj = None
    if all_taverns:
        starting_loc_obj = random.choice(all_taverns)
    else:
        UI.print_warning("No taverns found for random start. Defaulting to first available location.")
        if GAME_LOCATIONS_MAP:
            starting_loc_obj = next(iter(GAME_LOCATIONS_MAP.values()))
        else:
            UI.print_failure("FATAL: No locations found in GAME_LOCATIONS_MAP. Cannot start game.")
            return None
    if not starting_loc_obj:
        UI.print_failure("FATAL: Could not determine a starting location.")
        return None
    current_for_discovery = starting_loc_obj
    discovered_for_startup = []
    while current_for_discovery:
        if current_for_discovery.id not in player.known_location_ids:
            player.known_location_ids.add(current_for_discovery.id)
            if not any(obj.id == current_for_discovery.id for obj in player.known_locations_objects):
                player.known_locations_objects.append(current_for_discovery)
            discovered_for_startup.append(current_for_discovery.name if current_for_discovery.name else "A mysterious place")
        if current_for_discovery.parent_id:
            parent_location = GAME_LOCATIONS_MAP.get(current_for_discovery.parent_id)
            if parent_location:
                current_for_discovery = parent_location
            else:
                break
        else:
            break
    hold_obj, city_obj, _ = _find_hierarchy(starting_loc_obj)
    hold_name_display = hold_obj.name if hold_obj else "an unknown hold"
    city_name_display = city_obj.name if city_obj else "an unknown city"
    starting_location_name = starting_loc_obj.name if starting_loc_obj.name else "A mysterious place"
    if city_obj and starting_loc_obj.name == city_name_display:
        message = f"You awaken in {starting_location_name}, a seemingly cozy establishment within the lands of {hold_name_display}..."
    else:
        message = f"You awaken in {starting_location_name}, a seemingly cozy establishment in {city_name_display}, within the lands of {hold_name_display}."
    wrapped_message = UI.wrap_text(message, width=120)
    padding = " " * ((120 - len(wrapped_message)) // 2)
    UI.slow_print(padding + wrapped_message)
    centered_text = "Your journey begins..."
    wrapped_centered_text = UI.wrap_text(centered_text, width=120)
    padding = " " * ((120 - len(wrapped_centered_text)) // 2)
    UI.slow_print(padding + wrapped_centered_text)
    text_to_center = "The warm fire crackles. A few patrons murmur over their drinks. Adventure awaits."
    wrapped_centered_text = UI.wrap_text(text_to_center, width=120)
    centered_text = " " * ((120 - len(wrapped_centered_text)) // 2) + wrapped_centered_text
    UI.slow_print(centered_text)
    generate_npcs_for_location(starting_loc_obj, npc_registry, _find_hierarchy)
    return starting_loc_obj

def initialize_game_state(player: Player):
    logging.debug("Before initialize_game_state")
    global npc_registry
    player.known_location_ids.clear()
    player.known_locations_objects.clear()
    npc_registry.clear()
    initialize_game_events()

def start_game():
    global GAME_LOCATIONS_MAP
    current_location_global_obj: Location = None
    game_time = datetime(201, 1, 1, 8, 0, 0, tzinfo=timezone.utc)

    try:
        try:
            #GAME_LOCATIONS_MAP = initialize_skyrim_map()
            GAME_LOCATIONS_MAP = location_manager.locations
            UI.print_system_message("initialize_skyrim_map() completed successfully.")
        except Exception as e:
            UI.print_failure(f"Failed to initialize Skyrim map: {e}. Exiting.")
            traceback.print_exc()
            return
        except:
            pass

        player = initialize_player()
        if not player:
            UI.print_failure("Failed to initialize player. Exiting.")
            return

        initialize_game_state(player)
        logging.debug("After initialize_game_state")

        current_location_global_obj = initialize_starting_location(player)
        logging.debug("After initialize_starting_location")
        if not current_location_global_obj:
            UI.print_failure("Failed to set starting location. Exiting.")
            return
        player.update_current_location_for_quest(current_location_global_obj)
        
        main_loop_running = True
        while main_loop_running:
            logging.debug("Inside main_loop_running loop")
            try:
                if not player.stats.is_alive():
                    UI.print_heading("Your Legend Ends Here")
                    UI.slow_print(f"{player.full_name} has fallen...")
                    break

                player.stats.restore_fatigue(max(1, player.stats.level // 2))
                player.stats.restore_magicka(max(1, player.stats.level // 3))

                check_and_trigger_events(game_time, player, current_location_global_obj, npc_registry, GAME_LOCATIONS_MAP, UI)

                for quest in player.quest_log.active_quests:
                    if quest.current_stage and not quest.check_all_current_stage_objectives_met(player):
                        for obj in quest.current_stage.get("objectives", []):
                            quest.check_objective_met(obj, player)
                    if quest.check_all_current_stage_objectives_met(player):
                        if quest.current_stage_index + 1 < len(quest.stages):
                            UI.print_system_message(f"QUEST STAGE COMPLETE for '{quest.title}'! Advancing to next stage.")
                            quest.advance_quest_stage()
                        else:
                            turn_in_loc_name = "your quest giver"
                            turn_in_loc_id_str = quest.turn_in_npc_id.split('_')[0]
                            if turn_in_loc_id_str.isdigit():
                                turn_in_loc_id = int(turn_in_loc_id_str)
                                turn_in_loc_obj = GAME_LOCATIONS_MAP.get(turn_in_loc_id)
                                if turn_in_loc_obj:
                                    turn_in_loc_name = turn_in_loc_obj.name
                            UI.print_system_message(f"QUEST OBJECTIVES MET for '{quest.title}'! Return to {turn_in_loc_name} to turn in.")
                            quest.status = "completed"

                if player.stats.current_encumbrance > player.stats.encumbrance_limit:
                    UI.slow_print("Your heavy load weighs you down.", speed=0.005)
                    
                UI.print_line('=')
                UI.slow_print(current_location_global_obj.description if current_location_global_obj else "A mysterious place.")
                UI.print_line('=')
                UI.print_info(f"Location: {current_location_global_obj.name if current_location_global_obj else 'None'} | {get_current_game_time_string(game_time)}\nHP: {player.stats.current_health}/{player.stats.max_health} | MP: {player.stats.current_magicka}/{player.stats.max_magicka} | FP: {player.stats.current_fatigue}/{player.stats.max_fatigue}")
                    
                menu_options = [
                    "Explore Known World", "Parley with Souls", "Behold Thy Spirit",
                    "Test Thy Steel", "Inspect Thy Possessions", "Look Around The Area",
                    "Review Quest Log", "View World Map", "Use Item from Inventory",
                    "Wait / Pass Time", "Depart This Realm (Quit)"
                ]
                UI.print_menu(menu_options)
                player_input = UI.print_prompt("Your choice: ")

                action_result, game_time = handle_player_choice(player_input, player, current_location_global_obj, menu_options, game_time)

                check_and_trigger_events(game_time, player, current_location_global_obj, npc_registry, GAME_LOCATIONS_MAP, UI)

                if action_result == "QUIT_GAME_SIGNAL":
                    main_loop_running = False
                elif action_result == "STATS_MENU_ACTION" or action_result == "NO_EVENT_THIS_TURN":
                    pass 
                elif isinstance(action_result, Location):
                    new_loc_obj = action_result
                    if new_loc_obj and new_loc_obj != current_location_global_obj:
                        current_location_global_obj = new_loc_obj
                        player.update_current_location_for_quest(current_location_global_obj)
                        #current_location_raw_data = get_location_raw_data(current_location_global_obj.id)
                        location_tags = current_location_global_obj.tags
                        trigger_random_event(location_tags, player, UI, current_location_global_obj)
                elif isinstance(action_result, tuple) and len(action_result) == 2 and isinstance(action_result[0], Location):
                     new_loc_obj_from_tuple = action_result[0]
                     if new_loc_obj_from_tuple and new_loc_obj_from_tuple != current_location_global_obj:
                         current_location_global_obj = new_loc_obj_from_tuple
                         player.update_current_location_for_quest(current_location_global_obj)
                         #current_location_raw_data = get_location_raw_data(current_location_global_obj.id)
                         location_tags = current_location_global_obj.tags
                         trigger_random_event(location_tags, player, UI, current_location_global_obj)

            except Exception as e:
                UI.print_failure(f"UNEXPECTED ERROR IN MAIN LOOP: {e}")
                traceback.print_exc()
                UI.press_enter()
                main_loop_running = False

        UI.slow_print("The threads of fate have been severed. Until we meet again...")

    except Exception as e:
        print(f"--- A CRITICAL ERROR OCCURRED IN START_GAME ---")
        traceback.print_exc()
        print(f"ERROR DETAILS: {e}")
    except:
        pass
    finally:
        print("--- SCRIPT EXECUTION FINISHING. PAUSING... ---")
        input("Script has finished or errored. Press Enter to exit.")

if __name__ == "__main__":
    print("--- ENTERING MAIN EXECUTION BLOCK (__name__ == '__main__') ---")
    start_game()
    print("--- START_GAME() COMPLETED ---")
    logging.debug("--- START_GAME() COMPLETED ---")