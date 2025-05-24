import time
import sys
import os
import random

class UI:
    @staticmethod
    def top_border(width=50):
        """Generates a thick top border."""
        try:
            pattern = "════╦════"
            repeat = width // 8
            remainder = width % 8
            return "╔" + pattern * repeat + "═" * remainder + "╗"
        except Exception as e:
            print(f"Error in top_border: {e}")
            return "=" * width

    @staticmethod
    def bottom_border(width=50):
        """Generates a thick bottom border."""
        try:
            pattern = "════╩════"
            repeat = width // 8
            remainder = width % 8
            return "╚" + pattern * repeat + "═" * remainder + "╝"
        except Exception as e:
            print(f"Error in bottom_border: {e}")
            return "=" * width

    @staticmethod
    def middle_border(width=50):
        """Generates a thick middle border."""
        try:
            pattern = "════╬════"
            repeat = width // 8
            remainder = width % 8
            return "╠" + pattern * repeat + "═" * remainder + "╣"
        except Exception as e:
            print(f"Error in middle_border: {e}")
            return "=" * width

    @staticmethod
    def slow_print(text, delay=0.015):
        """Prints text character by character with a delay for dramatic effect."""
        try:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            print()  # Newline at the end
        except Exception as e:
            print(f"Error in slow_print: {e}")
            print(text)

    @staticmethod
    def clear():
        """Clears the console screen (works on Windows and Unix-based systems)."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def header(text):
        """Displays a header with a thick border."""
        try:
            width = 50
            print("\n" + UI.top_border(width))
            padded_text = f"  {text.center(width - 4)}  "
            print(f"║{padded_text}║")
            print(UI.bottom_border(width))
        except Exception as e:
            print(f"Error in header: {e}")
            print(f"\n===== {text} =====")

    @staticmethod
    def divider():
        """Prints a single-line thick divider."""
        try:
            width = 50
            print(UI.middle_border(width))
        except Exception as e:
            print(f"Error in divider: {e}")
            print("=" * 50)

    @staticmethod
    def stylized(text):
        """Displays text with a stylized border."""
        try:
            width = 50
            text_width = len(text) + 4
            if text_width > width - 2:
                text = text[:width - 6]  # Truncate if too long
                text_width = width - 2
            padding = (width - text_width) // 2
            print(f"\n{UI.top_border(width)}")
            print(f"║{' ' * padding}~ {text} ~{' ' * (width - text_width - padding)}║")
            print(UI.bottom_border(width))
        except Exception as e:
            print(f"Error in stylized: {e}")
            print(f"\n~ {text} ~")

    @staticmethod
    def format_npc_entry(index, npc):
        """Formats an NPC entry for display with borders."""
        try:
            alignment = npc.alignment.capitalize()
            entry = f"[{index:>2}] {npc.name:<20} — {npc.culture_tag.capitalize()} {npc.role_tag.capitalize()} ({alignment})"
            width = 50
            if len(entry) > width - 4:
                entry = entry[:width - 7] + "..."  # Truncate if too long
            padded_entry = f"  {entry:<{width - 4}}  "
            return f"║{padded_entry}║"
        except Exception as e:
            print(f"Error in format_npc_entry: {e}")
            return f"[{index}] {npc.name} ({npc.role_tag})"

    @staticmethod
    def show_stats(player):
        """Displays player stats with borders."""
        try:
            width = 50
            print("\n" + UI.top_border(width))
            print(f"║{'Thy Spirit\'s Essence'.center(width - 2)}║")
            print(UI.middle_border(width))
            stats_lines = [
                f"Name: {player.name}",
                f"Race: {player.race}",
                f"Class: {player.character_class}",
                f"Level: {player.level}",
                f"Attributes: {player.attributes}",
                f"Skills: {player.skills}",
                f"Stats: {player.stats}" # Show the new stats
            ]
            for line in stats_lines:
                padded_line = f"  {line:<{width - 4}}  "
                print(f"║{padded_line}║")
            print(UI.bottom_border(width))
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error in show_stats: {e}")
            UI.slow_print("Thy essence remains unseen by mortal eyes.")

    @staticmethod
    def show_inventory(player):
        """Displays player inventory with borders."""
        try:
            width = 50
            print("\n" + UI.top_border(width))
            print(f"║{'Thy Possessions'.center(width - 2)}║")
            print(UI.middle_border(width))
            print(f"║  Carry Weight: {player.stats.carry_weight:.2f} / {player.stats.max_carry_weight:.2f} ║")
            if not player.inventory:
                padded_line = f"  {'Thy pack is empty, as barren as the tundra.':<{width - 4}}  "
                print(f"║{padded_line}║")
            else:
                for i, item in enumerate(player.inventory, 1):
                    item_str = f"[{i:>2}] - {item} (Weight: {item.weight:.2f}, Value: {item.value})"
                    if len(item_str) > width - 4:
                        item_str = item_str[:width - 7] + "..."  # Truncate if too long
                    padded_line = f"  {item_str:<{width - 4}}  "
                    print(f"║{padded_line}║")
            print(UI.bottom_border(width))
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Error in show_inventory: {e}")
            UI.slow_print("Thy possessions fade into the mists of fate.")

    @staticmethod
    def themed_tip():
        """Displays a random tip or rumor with borders."""
        try:
            from tags import RUMOR_POOL
            available_rumors = []
            for tag in RUMOR_POOL:
                available_rumors.extend(RUMOR_POOL[tag])
            width = 50
            print("\n" + UI.top_border(width))
            print(f"║{'A Whispered Rumor'.center(width - 2)}║")
            print(UI.middle_border(width))
            if available_rumors:
                rumor = random.choice(available_rumors)
                while len(rumor) > width - 4:
                    rumor = rumor[:width - 7] + "..."  # Truncate if too long
                padded_rumor = f"  {rumor:<{width - 4}}  "
                print(f"║{padded_rumor}║")
            else:
                padded_line = f"  {'The winds carry no whispers this day.':<{width - 4}}  "
                print(f"║{padded_line}║")
            print(UI.bottom_border(width))
        except Exception as e:
            print(f"Error in themed_tip: {e}")
            UI.slow_print("A whisper of forgotten lore fades into silence.")

    @staticmethod
    def press_enter():
        """Prompts the user to press Enter."""
        input("Press Enter to continue...")

    @staticmethod
    def npc_greeting(npc):
        """Displays a greeting from the NPC."""
        try:
            width = 50
            print("\n" + UI.top_border(width))
            greeting = f"{npc.name} says: \"{npc.greeting}\""
            if len(greeting) > width - 4:
                greeting = greeting[:width - 7] + "..."
            padded_greeting = f"  {greeting:<{width - 4}}  "
            print(f"║{padded_greeting}║")
            print(UI.bottom_border(width))
        except Exception as e:
            print(f"Error in npc_greeting: {e}")
            UI.slow_print(f"{npc.name} nods in your direction.")

    @staticmethod
    def local_information(location):
        """Provides information about the current location."""
        try:
            width = 50
            print("\n" + UI.top_border(width))
            info = f"Local lore suggests: {location['desc']}"
            if len(info) > width - 4:
                info = info[:width - 7] + "..."
            padded_info = f"  {info:<{width - 4}}  "
            print(f"║{padded_info}║")
            print(UI.bottom_border(width))
        except Exception as e:
            print(f"Error in local_information: {e}")
            UI.slow_print("The area is silent, its secrets closely guarded.")

    @staticmethod
    def npc_purpose(npc):
        """Explains the NPC's purpose or role."""
        try:
            width = 50
            print("\n" + UI.top_border(width))
            purpose = f"{npc.name} says: \"I am a {npc.role_tag}, here to {npc.purpose}\""
            if len(purpose) > width - 4:
                purpose = purpose[:width - 7] + "..."
            padded_purpose = f"  {purpose:<{width - 4}}  "
            print(f"║{padded_purpose}║")
            print(UI.bottom_border(width))
        except Exception as e:
            print(f"Error in npc_purpose: {e}")
            UI.slow_print(f"{npc.name} remains silent about their intentions.")

    @staticmethod
    def farewell(npc):
        """Displays a farewell message from the NPC."""
        try:
            width = 50
            print("\n" + UI.top_border(width))
            farewell_msg = f"{npc.name} says: \"{npc.farewell}\""
            if len(farewell_msg) > width - 4:
                farewell_msg = farewell_msg[:width - 7] + "..."
            padded_farewell = f"  {farewell_msg:<{width - 4}}  "
            print(f"║{padded_farewell}║")
            print(UI.bottom_border(width))
        except Exception as e:
            print(f"Error in farewell: {e}")
            UI.slow_print(f"{npc.name} gives you a curt nod.")