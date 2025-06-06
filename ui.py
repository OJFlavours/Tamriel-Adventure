import time
import sys
import textwrap
from colorama import Fore, Back, Style, init
from typing import List, Dict, Any, Optional

# Initialize colorama for cross-platform ANSI escape codes
init(autoreset=True)

# --- Configuration ---
LINE_WIDTH = 120
SLOW_PRINT_SPEED = 0.0001# Adjust for faster/slower text crawl
HEADING_COLOR = Fore.CYAN + Style.BRIGHT
SUBHEADING_COLOR = Fore.GREEN + Style.BRIGHT
PROMPT_COLOR = Fore.YELLOW + Style.BRIGHT
INFO_COLOR = Fore.WHITE
SUCCESS_COLOR = Fore.GREEN
FAILURE_COLOR = Fore.RED
MENU_COLOR = Fore.MAGENTA + Style.BRIGHT
HIGHLIGHT_COLOR = Fore.YELLOW
COMBAT_TEXT_COLOR = Fore.RED
SYSTEM_MESSAGE_COLOR = Fore.BLUE + Style.BRIGHT # Used for debug messages
EVENT_MESSAGE_COLOR = Fore.MAGENTA + Style.BRIGHT # Color for event messages

class UI:
    """
    Provides static methods for all user interface interactions,
    including formatted text output, prompts, and screen clearing.
    """

    @staticmethod
    def clear_screen():
        """Clears the console screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_line(char='=', width=LINE_WIDTH):
        """Prints a horizontal line."""
        print()
        print(Fore.WHITE + char * width + Style.RESET_ALL)
        print()

    @staticmethod
    def slow_print(text, speed=SLOW_PRINT_SPEED, end='\n', width=LINE_WIDTH):
        """Prints text character by character with a delay, wrapping at the specified width."""
        wrapped_lines = textwrap.wrap(text, width=width)
        for i, line in enumerate(wrapped_lines):
            for char_index, char in enumerate(line):
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            # Add a newline after each line, except possibly the last one if 'end' is different
            if i < len(wrapped_lines) - 1:
                sys.stdout.write('\n')
                sys.stdout.flush()
            elif end == '\n': # Ensure the specified 'end' is honored for the very last line
                 sys.stdout.write('\n')
                 sys.stdout.flush()

        # If the original text didn't end with a newline and the specified 'end' is not a newline,
        # and the wrapped output also didn't end with a newline (which it should now),
        # this part might need adjustment. But the loop above should handle newlines correctly.
        # The original logic for 'end' might be redundant if textwrap always ensures lines.
        # However, if 'end' is something other than '\n', we should respect it for the final output.
        if end != '\n' and wrapped_lines and not wrapped_lines[-1].endswith('\n'):
             sys.stdout.write(end)
             sys.stdout.flush()


    @staticmethod
    def wrap_text(text, width=LINE_WIDTH):
        """Wraps text to a specified width."""
        return textwrap.fill(text, width=width)

    @staticmethod
    def print_heading(text):
        """Prints a formatted heading, centered."""
        print()
        UI.print_line()
        print()
        print()
        wrapped_text = UI.wrap_text(text.upper())
        padding = " " * ((LINE_WIDTH - len(wrapped_text)) // 2)
        print(f"{HEADING_COLOR}{padding}{wrapped_text}{Style.RESET_ALL}")
        print()
        print()
        UI.print_line()
        print()
        print()

    @staticmethod
    def print_subheading(text):
        """Prints a formatted subheading, centered."""
        wrapped_text = UI.wrap_text(text, width=LINE_WIDTH)
        padding = " " * ((LINE_WIDTH - len(wrapped_text)) // 2)
        print(f"\n\n{SUBHEADING_COLOR}{padding}{wrapped_text}{Style.RESET_ALL}\n\n")

    @staticmethod
    def print_prompt(text):
        """Prints a formatted prompt for user input, ensuring wrapping."""
        # Print the wrapped prompt text first, without a trailing newline from print()
        wrapped_prompt_text = UI.wrap_text(text)
        print(f"{PROMPT_COLOR}{wrapped_prompt_text}{Style.RESET_ALL}", end="")
        # Then, get input with a minimal actual prompt for the input() function itself
        return input(f"{PROMPT_COLOR}: {Style.RESET_ALL}")

    @staticmethod
    def print_info(text):
        """Prints informational text."""
        print(f"{INFO_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")
        print()
        print()
        print()

    @staticmethod
    def print_success(text):
        """Prints a success message."""
        print(f"{SUCCESS_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_failure(text):
        """Prints a failure message."""
        print(f"{FAILURE_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_warning(text):
        """Prints a warning message."""
        # Using YELLOW for warnings, similar to HIGHLIGHT_COLOR
        print(f"{HIGHLIGHT_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_menu(options):
        """Prints a formatted menu of options."""
        print()
        print(Fore.YELLOW + "Choose your path:" + Style.RESET_ALL)
        print()
        print()
        for i, option in enumerate(options):
            print(f"{MENU_COLOR}  [{i + 1}] {UI.wrap_text(option)}{Style.RESET_ALL}")
        print()
        print()
        print()

    @staticmethod
    def print_highlight(text):
        """Prints text with highlighting."""
        print(f"{HIGHLIGHT_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_combat_text(text):
        """Prints text specifically for combat events."""
        print(f"{COMBAT_TEXT_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_system_message(text):
        """Prints important system messages (including debug messages)."""
        print(f"{SYSTEM_MESSAGE_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_event_message(text):
        """Prints messages related to game events, often with a distinct style."""
        print(f"{EVENT_MESSAGE_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def capitalize_dialogue(text: str) -> str:
        """
        Capitalizes the first letter of sentences and fixes standalone 'i' to 'I'.
        Assumes basic sentence structure.
        """
        if not text:
            return ""
        
        # Replace standalone 'i' or 'i ' with 'I' or 'I '
        processed_text = text.replace(" i ", " I ").replace(" i'", " I'").replace("i'm", "I'm").replace("i've", "I've")
        if processed_text.startswith("i "): # Catch initial 'i ' at the very start
            processed_text = "I" + processed_text[1:]

        # Capitalize the first letter of the overall string
        if processed_text: # Ensure string is not empty before attempting to capitalize
            processed_text = processed_text[0].upper() + processed_text[1:]

        # Capitalize after sentence-ending punctuation.
        punctuations = ['.', '!', '?']
        for punc in punctuations:
            parts = processed_text.split(punc)
            for i, part in enumerate(parts):
                stripped_part = part.strip()
                if stripped_part:
                    # Keep original leading/trailing spaces for proper re-joining
                    original_leading_spaces = part[:(len(part) - len(part.lstrip()))]
                    original_trailing_spaces = part[len(part.rstrip()):]
                    
                    capitalized_stripped = stripped_part[0].upper() + stripped_part[1:]
                    parts[i] = original_leading_spaces + capitalized_stripped + original_trailing_spaces
            processed_text = punc.join(parts)
        
        return processed_text

    @staticmethod
    def display_player_stats(player):
        """Displays the player's current stats in a formatted way."""
        UI.print_subheading("Player Stats")
        # Ensure 'character_class' is an attribute of player or player.stats
        # For now, using player.subclass as a fallback if character_class is not set
        class_display = getattr(player, 'character_class', player.subclass if hasattr(player, 'subclass') else 'Adventurer')
        race_name = player.race.replace("_", " ").title()
        UI.print_info(f"Name: {player.full_name}, Level: {player.level} {race_name} {class_display.capitalize()}")
        UI.print_info(f"Health: {player.stats.current_health}/{player.stats.max_health}")
        UI.print_info(f"Magicka: {player.stats.current_magicka}/{player.stats.max_magicka}")
        UI.print_info(f"Fatigue: {player.stats.current_fatigue}/{player.stats.max_fatigue}")
        UI.print_info(f"Gold: {player.stats.gold}")
        UI.print_info(f"Encumbrance: {player.stats.current_encumbrance}/{player.stats.encumbrance_limit}")
        if player.equipment:
            equipped_items = ", ".join([item.name for item in player.equipment])
            UI.print_info(f"Equipped: {equipped_items}")
        else:
            UI.print_info("Equipped: Nothing")
        print()

    @staticmethod
    def display_location_info(location):
        """Displays information about the current location."""
        if isinstance(location, dict):
            UI.print_subheading(f"Current Location: {location['name']}")
            UI.print_info(UI.wrap_text(location['description']))
            if 'exits' in location and location['exits']:
                exit_names = ", ".join(location['exits'].keys())
                UI.print_info(f"Available Exits: {exit_names}")
        else:
            UI.print_subheading(f"Current Location: {location.name}")
            UI.print_info(UI.wrap_text(location.description))
            if hasattr(location, 'exits') and location.exits:
                exit_names = ", ".join(location.exits.keys())
                UI.print_info(f"Available Exits: {exit_names}")
        print()

    @staticmethod
    def display_inventory(player):
        """Displays the player's inventory."""
        UI.print_subheading("Inventory")
        if player.stats.inventory: # Changed from player.inventory to player.stats.inventory
            for i, item in enumerate(player.stats.inventory):
                UI.print_info(f"[{i + 1}] {item.name} ({item.weight} lbs, Value: {item.value} gold)")
        else:
            UI.print_info("Your inventory is empty.")
        print()

    @staticmethod
    def display_quest_log(player):
        """Displays the player's current quest log."""
        UI.print_subheading("Quest Log")
        if hasattr(player, 'quest_log') and player.quest_log:
            quests = player.quest_log.list_quests()
            if quests:
                for i, quest in enumerate(quests):
                    UI.print_info(f"[{i + 1}] {quest.title}: {UI.wrap_text(quest.description, width=UI.LINE_WIDTH - 4)}")
            else:
                UI.print_info("You have no active quests.")
        else:
            UI.print_info("You have no active quests.") # Redundant, but harmless
        print()

    @staticmethod
    def press_enter():
        """Prompts the user to press Enter to continue."""
        input(f"{PROMPT_COLOR}Press Enter to continue...{Style.RESET_ALL}")

    @staticmethod
    def select_from_paginated_list(options: List[Dict[str, Any]], prompt_message: str, page_size: int = 7) -> Any | None:
        """
        Displays a list of options in a paginated format and allows the user to select one.
        Each option in the 'options' list is expected to be a dictionary with at least a 'name' key.
        Returns the selected option (dictionary) or None if the user cancels or input is invalid.
        """
        if not options:
            UI.print_info("No options available.")
            return None

        current_page = 0
        total_pages = (len(options) + page_size - 1) // page_size

        while True:
            UI.clear_screen()
            UI.print_subheading(prompt_message)
            
            start_index = current_page * page_size
            end_index = start_index + page_size
            current_options_page = options[start_index:end_index]

            for i, option_item in enumerate(current_options_page):
                # Ensure option_item is a dict and has 'name'
                item_name = option_item.get('name', 'Unnamed Option') if isinstance(option_item, dict) else str(option_item)
                UI.print_info(f"  [{start_index + i + 1}] {item_name}")
            
            UI.print_line('-')
            page_info = f"Page {current_page + 1} of {total_pages}"
            nav_prompt = "Enter number, (N)ext, (P)revious, or (0) to Cancel: "
            
            if total_pages == 1: # No pagination needed for a single page
                nav_prompt = "Enter number or (0) to Cancel: "
                UI.print_info(page_info) # Still show page info for consistency
            elif current_page == 0: # First page
                nav_prompt = "Enter number, (N)ext, or (0) to Cancel: "
                UI.print_info(f"{page_info} (N for Next)")
            elif current_page == total_pages - 1: # Last page
                nav_prompt = "Enter number, (P)revious, or (0) to Cancel: "
                UI.print_info(f"{page_info} (P for Previous)")
            else: # Middle pages
                UI.print_info(f"{page_info} (N for Next, P for Previous)")

            choice_input = UI.print_prompt(nav_prompt).strip().lower()

            if choice_input == 'n':
                if current_page < total_pages - 1:
                    current_page += 1
                else:
                    UI.print_warning("Already on the last page.")
                    UI.press_enter()
            elif choice_input == 'p':
                if current_page > 0:
                    current_page -= 1
                else:
                    UI.print_warning("Already on the first page.")
                    UI.press_enter()
            elif choice_input == '0':
                return None # Cancel
            elif choice_input.isdigit():
                try:
                    selection_num = int(choice_input)
                    if 1 <= selection_num <= len(options):
                        # Adjust for 0-based indexing from 1-based user input
                        return options[selection_num - 1]
                    else:
                        UI.print_warning("Invalid selection number.")
                        UI.press_enter()
                except ValueError:
                    UI.print_warning("Invalid input. Please enter a number, N, P, or 0.")
                    UI.press_enter()
            else:
                UI.print_warning("Invalid command.")
                UI.press_enter()

# --- Example Usage (can be removed later) ---
if __name__ == "__main__":
    UI.clear_screen()
    UI.print_heading("Welcome to Tamriel Adventure!")

    UI.slow_print("A land of mystery and danger awaits you...")
    time.sleep(0.5)

    print()
    UI.print_subheading("A New Day Dawns")
    print()
    UI.print_info("The crisp morning air fills your lungs as you awaken.\n\nThe sounds of a nearby town drift towards you.")

    # Example of capitalizing dialogue using the new method
    test_dialogue_1 = "i think i've heard that rumor before. it's quite interesting, isn't it?"
    test_dialogue_2 = "a dark shadow falls over the land! what will you do?"
    test_dialogue_3 = "hello. what do you want?"

    UI.slow_print(f"Test 1: \"{UI.capitalize_dialogue(test_dialogue_1)}\"")
    UI.slow_print(f"Test 2: \"{UI.capitalize_dialogue(test_dialogue_2)}\"")
    UI.slow_print(f"Test 3: \"{UI.capitalize_dialogue(test_dialogue_3)}\"")

    player_name = UI.print_prompt("Enter your name")
    UI.print_info(f"Greetings, {player_name}!")

    UI.print_menu(["Explore the town", "Check your inventory", "View quest log", "Quit"])
    action = UI.print_prompt("What will you do")

    if action == "1":
        UI.print_highlight("You decide to explore the town.")
    elif action == "2":
        UI.print_failure("Your inventory is currently empty.")
    elif action == "3":
        UI.print_info("You have no active quests.")
    elif action == "4":
        UI.print_system_message("Exiting game.")
    else:
        UI.print_failure("Invalid choice.")

    UI.print_combat_text("\nA ferocious wolf attacks!")
    UI.print_success("You strike the wolf with your sword!")
    UI.print_failure("The wolf bites you!")

    UI.print_system_message("\n--- End of Example ---")
    UI.press_enter() # Added for example flow