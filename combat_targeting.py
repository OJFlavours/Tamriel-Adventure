# combat_targeting.py
import random
from typing import List, Optional
from ui import UI # Assuming UI is in the same directory or accessible

# Forward declaration for Player and NPC to avoid circular imports if they use Combat or vice-versa
# This is a common pattern. Actual instances will be passed at runtime.
class Player: pass
class NPC: pass

def get_target_logic(attacker, target_list: List, ui_instance: UI, player_instance: Optional[Player], all_allies: List[NPC], all_player_summons: List[NPC]) -> Optional[object]:
    if not target_list:
        return None

    if attacker == player_instance:
        ui_instance.print_subheading("Choose your target:")
        for i, enemy in enumerate(target_list, 1):
            ui_instance.print_info(f"[{i}] {enemy.name} (Health: {enemy.stats.current_health}/{enemy.stats.max_health})")

        while True:
            try:
                choice_str = ui_instance.print_prompt("Enter target number (0 to cancel): ")
                if not choice_str.isdigit():
                    ui_instance.slow_print("Please enter a valid number.")
                    continue
                choice = int(choice_str)
                if choice == 0:
                    return None
                if 1 <= choice <= len(target_list):
                    target = target_list[choice - 1]
                    body_part = get_body_part_choice(target, ui_instance)
                    if body_part:
                        target_score = 0  # Initialize target_score
                        if has_status_effect(target, "poisoned"):
                            target_score += 50
                        return (target, body_part, target_score)
                    else:
                        return None
                ui_instance.slow_print("Invalid target number.")
            except ValueError: # Should be caught by isdigit, but as a fallback
                ui_instance.slow_print("Please enter a number.")
def get_body_part_choice(target, ui_instance: UI):
    body_parts = ["Head", "Torso", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
    ui_instance.print_subheading(f"Choose body part to target on {target.name}:")
    for i, part in enumerate(body_parts, 1):
        ui_instance.print_info(f"[{i}] {part}")

    while True:
        try:
            choice_str = ui_instance.print_prompt("Enter body part number (0 to cancel): ")
            if not choice_str.isdigit():
                ui_instance.slow_print("Please enter a valid number.")
                continue
            choice = int(choice_str)
            if choice == 0:
                return None
            if 1 <= choice <= len(body_parts):
                return body_parts[choice - 1]
            ui_instance.slow_print("Invalid body part number.")
        except ValueError:
            ui_instance.slow_print("Please enter a number.")
        except Exception as e:
            ui_instance.slow_print(f"An unexpected error occurred: {e}")
            return None
def has_status_effect(target, status_effect: str) -> bool:
    if not hasattr(target, 'status_effects'):
        return False
    return status_effect in target.status_effects