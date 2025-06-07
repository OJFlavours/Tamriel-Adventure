# game.py
import random
import logging
from datetime import datetime, timezone, timedelta
import time
import traceback
import json
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# --- Main Game Imports ---
try:
    from locations import Location, LocationManager #
    from player import Player #
    from combat import Combat #
    from ui import UI #
    from quests import generate_location_appropriate_quest, Quest #
    from character_creation import initialize_player #
    from npc_generation import generate_npcs_for_location #
    from exploration import display_world_map, explore_and_travel_menu #
    from combat_interactions import combat_demo, list_npcs_at_location #
    from game_events import check_and_trigger_events, initialize_game_events #
    from events import explore_location #
    from inventory_manager import handle_inventory_menu, handle_item_use #
    import tags #
    import flavor #
    from rumors import generate_rumor #
    from npc_dialogue_logic import handle_npc_dialogue #
    from stats import Stats, RACES, CLASSES #
    from npc_entities import NPC #
    from items import generate_random_item, Item, generate_item_from_key, Torch #
    from quests import QuestLog, process_quest_rewards #


except ImportError as e:
    print(f"Error importing modules: {e}")
    traceback.print_exc()
    input("Press Enter to exit...")
    exit(1)

# Globals
npc_registry = {}
location_manager = LocationManager() # Initialize the manager
GAME_LOCATIONS_MAP = location_manager.locations # Will store Location objects, keyed by ID

action_time_map = {
    "travel": 120, "search": 45, "rest": 480, "craft": 360, "combat": 30,
    "dialogue": 5, "wait / pass time": 60, "look around the area": 15
}

# --- Utility & Helper Functions ---

def clear_screen():
    UI.clear_screen()

def _find_hierarchy(loc_id_or_obj):
    target_loc_obj = loc_id_or_obj if isinstance(loc_id_or_obj, Location) else location_manager.get_location(loc_id_or_obj) #
    if not target_loc_obj:
        return None, None, None

    lineage = []
    current = target_loc_obj
    while current:
        lineage.append(current)
        current = location_manager.get_location(current.parent_id) if current.parent_id else None #
    lineage.reverse()

    hold_obj = lineage[0] if lineage else None
    primary_obj = lineage[1] if len(lineage) > 1 else hold_obj
    specific_obj = target_loc_obj # The target location is always the specific one

    return hold_obj, primary_obj, specific_obj


def look_around_area(player, current_location_obj: Location, npc_registry_param, game_loc_map_param, ui_param):
    UI.slow_print(f"You take a moment to observe your surroundings in {current_location_obj.name}...") #
    
    # Display the deep description if available, otherwise fallback to general description
    if current_location_obj.deep_description: #
        UI.slow_print(current_location_obj.deep_description) #
    else:
        UI.slow_print(current_location_obj.description) #

    # Note: Secret descriptions would need explicit triggers, not just general 'look around'
    # For example, if there's a specific item to interact with, or a rumor.

    # Original explore_location logic for events/flavor
    explore_location(player, current_location_obj, {}, npc_registry_param, game_loc_map_param, ui_param) # Passing empty dict for encounters as it's not directly used here

    # Check for new quests (existing logic)
    if random.random() < 0.25:
        new_quest = generate_location_appropriate_quest(player.level, current_location_obj, None) #
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

    # Input parsing logic
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
        UI.print_heading(f"Travel from {current_loc_obj.name}") #
        if current_loc_obj.exits: #
            UI.slow_print("Available destinations:")
            exit_options = list(current_loc_obj.exits.items()) #
            for i, (direction, dest_loc_obj) in enumerate(exit_options):
                formatted_direction = ' '.join(word.capitalize() for word in direction.split())
                # Use travel_desc if available, otherwise fall back to general description
                description_to_display = dest_loc_obj.travel_desc if dest_loc_obj.travel_desc else dest_loc_obj.description #
                UI.slow_print(f"{i+1}. {formatted_direction} - {description_to_display}")
            
            travel_choice_str = UI.print_prompt("Where to? (Enter number or 'cancel') ").strip().lower()
            if travel_choice_str != 'cancel':
                try:
                    travel_choice_idx = int(travel_choice_str) - 1
                    if 0 <= travel_choice_idx < len(exit_options):
                        _, new_dest_obj = exit_options[travel_choice_idx]
                        new_current_location_obj = new_dest_obj
                        UI.slow_print(f"Traveling to {new_current_location_obj.name}...")
                        new_current_location_obj.enter(player) #
                        generate_npcs_for_location(location_obj=new_current_location_obj, npc_registry=npc_registry, find_hierarchy_func=_find_hierarchy, location_manager=location_manager) #
                        # Use actual travel_time from location object, default to 60 if not set
                        time_advance_minutes = getattr(new_dest_obj, 'travel_time', 60) #
                    else:
                        UI.slow_print("Invalid choice.")
                except ValueError:
                    UI.slow_print("Invalid input.")
        else:
            UI.slow_print("There are no obvious exits from here.")

    elif action == "parley with souls":
        time_advance_minutes = action_time_map.get(action, 5)
        if current_loc_obj:
            list_npcs_at_location(current_loc_obj, player, npc_registry) #
        else:
            UI.slow_print("You must first be somewhere to find others.")
        # If no new location, ensure time still advances
        if new_current_location_obj == current_loc_obj:
            return "NO_EVENT_THIS_TURN", game_time_obj + timedelta(minutes=time_advance_minutes)

    elif action == "behold thy spirit":
        UI.display_player_stats(player)
        return "STATS_MENU_ACTION", game_time_obj 

    elif action == "test thy steel":
        time_advance_minutes = action_time_map.get(action, 30)
        new_current_location_obj = combat_demo(player, current_loc_obj, _find_hierarchy, npc_registry) #

    elif action == "inspect thy possessions":
        handle_inventory_menu(player) #

    elif action == "look around the area":
        new_current_location_obj = look_around_area(player, current_loc_obj, npc_registry, GAME_LOCATIONS_MAP, UI) #
        time_advance_minutes = action_time_map.get(action, 15)

    elif action == "review quest log":
        UI.display_quest_log(player) #
        time_advance_minutes = action_time_map.get(action, 5)

    elif action == "view world map":
        display_world_map(player, GAME_LOCATIONS_MAP) #

    elif action == "use item from inventory":
        handle_item_use(player) #

    elif action == "wait / pass time":
        UI.slow_print("Time passes...")
        time_advance_minutes = action_time_map.get(action, 60)
        # Restore player resources based on time passed
        for _ in range(time_advance_minutes // 60): # Restore hourly
            player.stats.restore_fatigue(max(1, player.stats.level // 2) * 2)
            player.stats.restore_magicka(max(1, player.stats.level // 3) * 2)
        UI.slow_print("You feel somewhat rested.")

    elif action == "depart this realm":
        pass # Handled by return "QUIT_GAME_SIGNAL"

    else:
        UI.slow_print("Your will wavers, or perhaps the spirits muddle your intent.")

    # Prevent immediate "Press Enter" if a menu or complex interaction just occurred
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
    # Get all locations that have the 'tavern' tag
    all_taverns = [loc for loc in location_manager.locations.values() if "tavern" in loc.tags] #
    if not all_taverns:
        UI.print_warning("No taverns found. Starting in a generic location.")
        starting_loc_obj = location_manager.get_location(10) # Fallback to Whiterun (ID 10)
    else:
        starting_loc_obj = random.choice(all_taverns) #
    
    # Generate NPCs for the starting location
    generate_npcs_for_location(location_obj=starting_loc_obj, npc_registry=npc_registry, find_hierarchy_func=_find_hierarchy, location_manager=location_manager) #
    # Ensure the player 'enters' the starting location to trigger any entry effects
    starting_loc_obj.enter(player) #
    return starting_loc_obj

def start_game():
    logging.debug("Greeting printed")
    UI.print_heading("Welcome to Tamriel Adventure!") # Changed this line
    logging.debug("Heading printed")
    player = initialize_player()
    game_time = datetime(4, 1, 1, 6, 0, 0, tzinfo=timezone.utc) # Start game at 4E 1, Morning Star 1, 6:00 AM

    current_location = initialize_starting_location(player)

    initialize_game_events() # Initialize global game events

    while True:
        clear_screen()
        UI.display_player_stats(player)
        UI.display_location_info(current_location)
        UI.print_info(get_current_game_time_string(game_time))

        main_menu_options = [
            "Explore Known World (Travel)",
            "Parley with Souls (Dialogue with NPCs)",
            "Behold Thy Spirit (View Stats)",
            "Inspect Thy Possessions (Inventory)",
            "Look Around The Area (Examine Surroundings)",
            "Review Quest Log",
            "View World Map",
            "Use Item from Inventory",
            "Wait / Pass Time",
            "Depart This Realm (Quit Game)"
        ]
        UI.print_menu(main_menu_options)
        
        choice = UI.print_prompt("What is your will, adventurer? ").strip()

        new_location, new_game_time = handle_player_choice(choice, player, current_location, main_menu_options, game_time)

        if new_location == "QUIT_GAME_SIGNAL":
            UI.slow_print("Farewell, adventurer. May your next journey be as grand.")
            logging.info(f"Game ended at {get_current_game_time_string(new_game_time)}. Player: {player.name}")
            break

        current_location = new_location
        game_time = new_game_time
        
        # Check and trigger random events after each player action that advances time
        if new_location != "NO_EVENT_THIS_TURN": # Avoid triggering if only displaying stats or opening inventory
            check_and_trigger_events(player, current_location, game_time, npc_registry, location_manager.locations) #
            
        logging.info(f"Player at: {current_location.name} at {get_current_game_time_string(game_time)}")
        # Simulate time passing more realistically
        time.sleep(0.5)

if __name__ == "__main__":
    start_game()