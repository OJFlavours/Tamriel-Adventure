import time
import sys
import textwrap
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform ANSI escape codes
init(autoreset=True)

# --- Configuration ---
LINE_WIDTH = 70
SLOW_PRINT_SPEED = 0.0001# Adjust for faster/slower text crawl
HEADING_COLOR = Fore.CYAN + Style.BRIGHT
SUBHEADING_COLOR = Fore.GREEN + Style.BRIGHT
PROMPT_COLOR = Fore.YELLOW + Style.BRIGHT
INFO_COLOR = Fore.WHITE
SUCCESS_COLOR = Fore.GREEN
FAILURE_COLOR = Fore.RED
MENU_COLOR = Fore.MAGENTA
HIGHLIGHT_COLOR = Fore.YELLOW
COMBAT_TEXT_COLOR = Fore.RED
SYSTEM_MESSAGE_COLOR = Fore.BLUE + Style.BRIGHT # Used for debug messages

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
    def print_line(char='-', width=LINE_WIDTH):
        """Prints a horizontal line."""
        print(char * width)

    @staticmethod
    def slow_print(text, speed=SLOW_PRINT_SPEED, end='\n'):
        """Prints text character by character with a delay for dramatic effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        # Ensure a newline is printed at the end, but avoid double newlines
        if not text.endswith('\n'):
            sys.stdout.write(end)
            sys.stdout.flush()

    @staticmethod
    def wrap_text(text, width=LINE_WIDTH):
        """Wraps text to a specified width."""
        return textwrap.fill(text, width=width)

    @staticmethod
    def print_heading(text):
        """Prints a formatted heading."""
        print()
        UI.print_line()
        print(f"{HEADING_COLOR}{UI.wrap_text(text.upper())}{Style.RESET_ALL}")
        UI.print_line()
        print()

    @staticmethod
    def print_subheading(text):
        """Prints a formatted subheading."""
        print(f"\n{SUBHEADING_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_prompt(text):
        """Prints a formatted prompt for user input."""
        return input(f"{PROMPT_COLOR}{UI.wrap_text(text)}: {Style.RESET_ALL}")

    @staticmethod
    def print_info(text):
        """Prints informational text."""
        print(f"{INFO_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_success(text):
        """Prints a success message."""
        print(f"{SUCCESS_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_failure(text):
        """Prints a failure message."""
        print(f"{FAILURE_COLOR}{UI.wrap_text(text)}{Style.RESET_ALL}")

    @staticmethod
    def print_menu(options):
        """Prints a formatted menu of options."""
        print(MENU_COLOR)
        for i, option in enumerate(options):
            print(f"  [{i + 1}] {UI.wrap_text(option)}")
        print(Style.RESET_ALL)

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
        UI.print_info(f"Name: {player.full_name}, Level: {player.level} {player.race.capitalize()} {class_display.capitalize()}")
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
        UI.print_subheading(f"Current Location: {location['name']}")
        UI.print_info(UI.wrap_text(location['description']))
        if 'exits' in location and location['exits']:
            exit_names = ", ".join(location['exits'].keys())
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

# --- Example Usage (can be removed later) ---
if __name__ == "__main__":
    UI.clear_screen()
    UI.print_heading("Welcome to Tamriel Adventure!")

    UI.slow_print("A land of mystery and danger awaits you...")
    time.sleep(0.5)

    UI.print_subheading("A New Day Dawns")
    UI.print_info("The crisp morning air fills your lungs as you awaken. The sounds of a nearby town drift towards you.")

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