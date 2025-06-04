# combat_logic.py

import random
from typing import List, Optional, Dict
from datetime import datetime

from ui import UI
from items import Item, generate_random_item
from status_effects import StatusEffect, StatusEffectType
from player import Player
from npc_entities import NPC  # Corrected import for NPC
from tags import get_tags  # Corrected import for get_tags
from spells import Spell
from combat_targeting import get_target_logic, get_body_part_choice
from combat_player_actions import handle_player_turn
from combat_npc_actions import handle_npc_turn
from combat_interactions import Combo, create_dynamic_interaction

# Helper function, was _is_two_handed_weapon in Combat class
# def is_two_handed_weapon(character) -> bool:
#     if not hasattr(character, 'equipment'):
#         return False
#     return any(item.category == "weapon" and
#                 hasattr(item, 'equipment_tag') and
#                 item.equipment_tag == "two_handed"
#                 for item in character.equipment)

# # Helper function, was _get_weapon_damage in Combat class
# def get_weapon_damage(character) -> int:
#     weapon_damage = 0
#     if hasattr(character, 'equipment'):
#         for item in character.equipment:
#             if item.category == "weapon" and hasattr(item, 'base_damage'):
#                 if isinstance(item.base_damage, (list, tuple)):
#                     weapon_damage += random.randint(item.base_damage[0], item.base_damage[1])
#                 else:
#                     weapon_damage += item.base_damage
#     return weapon_damage

# # Helper function, was _has_elemental_weapon in Combat class
# def has_elemental_weapon(character, element_type: str) -> bool:
#     if not hasattr(character, 'equipment'):
#         return False
#     return any(item.category == "weapon" and
#                 hasattr(item, 'enchantment') and
#                 element_type in item.enchantment.lower()
#                 for item in character.equipment)

def apply_weapon_effects(attacker, defender, weapon: Optional[Item]) -> List[str]:
    messages = []
    if not weapon or not hasattr(weapon, 'properties'):
        return messages

    if "enchantment" in weapon.properties:
        effect_type = None
        if "fire" in weapon.properties["enchantment"].lower():
            effect_type = StatusEffectType.BURNING
        elif "frost" in weapon.properties["enchantment"].lower():
            effect_type = StatusEffectType.FROZEN
        elif "poison" in weapon.properties["enchantment"].lower():
            effect_type = StatusEffectType.POISONED

        if effect_type and random.random() < 0.3:
            effect = StatusEffect(effect_type, duration=2, potency=1.0)
            if not hasattr(defender, 'status_effects'): # Ensure defender has status_effects list
                defender.status_effects = []
            defender.status_effects.append(effect)
            messages.extend(effect.apply(defender))
    return messages

def apply_and_log_weapon_effects_logic(attacker, defender, ui_instance: UI, is_ranged: bool = False):
    if attacker.equipment:
        weapon_to_check = None
        if is_ranged:
            weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and item.equipment_tag == "ranged"), None)
        else:
            weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and (item.equipment_tag == "main_hand" or item.equipment_tag == "two_handed")), None)

        if weapon_to_check:
            messages = apply_weapon_effects(attacker, defender, weapon_to_check)
            for msg in messages:
                ui_instance.slow_print(msg)

# def calculate_damage_logic(attacker, defender, ui_instance: UI, combo_counter: int, player_is_power_attacking: bool, is_ranged: bool = False, body_part: str = None) -> int:
#     if is_ranged:
#         base_damage = attacker.stats.agility // 3
#         skill_modifier = attacker.skills.get("archery", 0) // 4
#     else:
#         base_damage = attacker.stats.strength // 3
#         weapon_type_skill = "two_handed" if is_two_handed_weapon(attacker) else "one_handed"
#         skill_modifier = attacker.skills.get(weapon_type_skill, 0) // 4

#     weapon_dmg = get_weapon_damage(attacker)
#     total_damage = base_damage + weapon_dmg + skill_modifier

#     crit_chance = attacker.stats.luck // 3
#     if is_ranged:
#         crit_chance += attacker.skills.get("archery", 0) // 4
#     else:
#         crit_chance += attacker.skills.get(weapon_type_skill, 0) // 4

#     if random.randint(1, 100) <= crit_chance:
#         total_damage = int(total_damage * 1.5)
#         ui_instance.slow_print(f"{attacker.name} lands a critical hit!")

#     # Assuming combo_counter and player_is_power_attacking are passed for the player
#     # For NPCs, these specific player-only mechanics won't apply or will be 0/False.
#     if combo_counter > 0 and not player_is_power_attacking: # Check if attacker is the one with combo
#         combo_bonus = min(combo_counter * 0.1, 0.5)
#         total_damage = int(total_damage * (1 + combo_bonus))
#         ui_instance.slow_print(f"Combo x{combo_counter}! ({int(combo_bonus*100)}% bonus damage)")

#     armor_reduction = defender.stats.armor_rating if hasattr(defender.stats, 'armor_rating') else 0

#     if hasattr(defender, 'is_blocking') and defender.is_blocking and not is_ranged:
#         block_skill = defender.skills.get("block", 0)
#         shield_bonus = 0
#         equipped_shield = next((item for item in defender.equipment if item.equipment_tag == "off_hand" and item.category == "armor"), None)
#         if equipped_shield:
#             shield_bonus = equipped_shield.armor_rating

#         block_effectiveness_percent = min( (block_skill * 0.6 + shield_bonus * 0.4) / 100, 0.85)
#         damage_reduction_from_block = int(total_damage * block_effectiveness_percent)
#         total_damage = max(0, total_damage - damage_reduction_from_block)
#         ui_instance.slow_print(f"{defender.name} blocks, reducing damage by {damage_reduction_from_block} ({int(block_effectiveness_percent*100)}%)!")

#     if hasattr(defender, 'improve_skill'):
#         defender.improve_skill("block", 1)

#     if hasattr(defender.stats, 'current_fatigue'):
#         block_stamina_cost = 5
#         defender.stats.current_fatigue = max(0, defender.stats.current_fatigue - block_stamina_cost)

#     # Body Part Targeting
#     if body_part:
#         if body_part == "Head":
#             total_damage = int(total_damage * 1.5)  # Headshots do 1.5x damage
#             ui_instance.slow_print("Headshot!")
#         elif body_part in ["Left Arm", "Right Arm"]:
#             total_damage = int(total_damage * 0.75)  # Arm shots do 0.75x damage
#             ui_instance.slow_print("Hit the arm!")
#         elif body_part in ["Left Leg", "Right Leg"]:
#             total_damage = int(total_damage * 0.75)  # Leg shots do 0.75x damage
#             defender.stats.agility = max(0, defender.stats.agility - 2)  # Reduce agility
#             ui_instance.slow_print("Hit the leg! Agility reduced.")

#     final_damage = max(0, total_damage - armor_reduction)

#     if has_elemental_weapon(attacker, "fire"):
#         final_damage *= (100 - defender.stats.fire_resist) / 100
#     if has_elemental_weapon(attacker, "frost"):
#         final_damage *= (100 - defender.stats.frost_resist) / 100
#     if has_elemental_weapon(attacker, "shock"):
#         final_damage *= (100 - defender.stats.shock_resist) / 100

#     return int(final_damage)

def handle_counter_attack_logic(defender, attacker, ui_instance: UI, combo_counter: int, player_is_power_attacking: bool):
    if hasattr(defender, 'is_blocking') and defender.is_blocking:
        block_skill = defender.skills.get("block", 0)
        counter_chance = block_skill / 200

        if random.random() < counter_chance:
            ui_instance.slow_print(f"{defender.name} performs a perfect block and counter-attacks!")
            # For counter-attack, combo_counter and player_is_power_attacking for the 'defender' (who is now attacking) would be 0/False
            # from combat_logic import calculate_damage_logic
            from combat import calculate_damage_logic
            counter_damage = calculate_damage_logic(defender, attacker, ui_instance, 0, False) // 2
            attacker.stats.current_health -= counter_damage
            ui_instance.slow_print(f"Counter-attack deals {counter_damage} damage!")

        if hasattr(defender, 'improve_skill'): # Assuming defender is player for skill improvement
            defender.improve_skill("block", 1)

def handle_complex_scenario(attacker, defender, scenario_type: str, ui_instance: UI):
    try:
        if scenario_type == "ambush":
            ui_instance.slow_print("The attacker ambushes the defender, gaining a surprise attack!")
            # Increase attacker's damage for the first turn
            attacker.temp_damage_bonus = 20  # Example bonus
        elif scenario_type == "siege":
            ui_instance.slow_print("The defender is sieged, suffering a defense penalty!")
            # Decrease defender's armor rating for the first turn
            defender.temp_armor_penalty = 10  # Example penalty
        elif scenario_type == "boss_battle":
            ui_instance.slow_print("A boss battle begins! The boss has increased stats.")
            # Increase boss's health and damage
            attacker.stats.max_health += 50
            attacker.stats.current_health += 50
            attacker.temp_damage_bonus = 15
    except Exception as e:
        print(f"Error handling complex scenario: {e}")

def handle_dynamic_event(attacker, defender, event_type: str, ui_instance: UI):
    try:
        if event_type == "environmental_hazard":
            ui_instance.slow_print("A sudden environmental hazard strikes!")
            # Apply damage to both combatants
            damage = random.randint(5, 10)
            attacker.stats.current_health -= damage
            defender.stats.current_health -= damage
            ui_instance.slow_print(f"Both combatants take {damage} damage!")
        elif event_type == "npc_reinforcements":
            ui_instance.slow_print("NPC reinforcements arrive!")
            # Add new NPCs to the combat
            # This would require more complex integration with the game's NPC management system
            pass
    except Exception as e:
        print(f"Error handling dynamic event: {e}")

def apply_event_effects(attacker, defender, event_type: str):
    try:
        if event_type == "environmental_change":
            # Change the environment
            pass
        elif event_type == "npc_reinforcements":
            # Add NPC reinforcements
            pass
    except Exception as e:
        print(f"Error handling event effects: {e}")