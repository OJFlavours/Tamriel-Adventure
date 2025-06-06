# combat_logic.py
import random
from typing import List, Optional

from ui import UI
from items import Item
from status_effects import StatusEffect, StatusEffectType
from damage_utils import calculate_damage_logic

def apply_weapon_effects(attacker, defender, weapon: Optional[Item]) -> List[str]:
    messages = []
    if not weapon or not hasattr(weapon, 'properties'):
        return messages

    if "enchantment" in weapon.properties and weapon.properties["enchantment"]:
        effect_type = None
        enchantment_lower = weapon.properties["enchantment"].lower()
        if "fire" in enchantment_lower:
            effect_type = StatusEffectType.BURNING
        elif "frost" in enchantment_lower:
            effect_type = StatusEffectType.FROZEN
        elif "poison" in enchantment_lower:
            effect_type = StatusEffectType.POISONED

        if effect_type and random.random() < 0.3:
            effect = StatusEffect(effect_type, duration=2, potency=1.0)
            if not hasattr(defender, 'status_effects'):
                defender.status_effects = []
            defender.status_effects.append(effect)
            messages.extend(effect.apply(defender))
    return messages

def apply_and_log_weapon_effects_logic(attacker, defender, ui_instance: UI, is_ranged: bool = False):
    if hasattr(attacker, 'equipment') and attacker.equipment:
        weapon_to_check = None
        if is_ranged:
            weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and hasattr(item, 'equipment_tag') and item.equipment_tag == "ranged"), None)
        else:
            weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and hasattr(item, 'equipment_tag') and (item.equipment_tag == "main_hand" or item.equipment_tag == "two_handed")), None)

        if weapon_to_check:
            messages = apply_weapon_effects(attacker, defender, weapon_to_check)
            for msg in messages:
                ui_instance.slow_print(msg)

def handle_counter_attack_logic(defender, attacker, ui_instance: UI, combo_counter: int, player_is_power_attacking: bool):
    if hasattr(defender, 'is_blocking') and defender.is_blocking:
        block_skill = defender.skills.get("block", 0)
        counter_chance = block_skill / 200.0

        if random.random() < counter_chance:
            ui_instance.slow_print(f"{defender.name} performs a perfect block and counter-attacks!")
            counter_damage = calculate_damage_logic(defender, attacker, ui_instance, 0, False) // 2
            attacker.stats.take_damage(counter_damage)
            ui_instance.slow_print(f"Counter-attack deals {counter_damage} damage!")

        if hasattr(defender, 'improve_skill'):
            defender.improve_skill("block", 1)

def handle_complex_scenario(attacker, defender, scenario_type: str, ui_instance: UI):
    try:
        if scenario_type == "ambush":
            ui_instance.slow_print("The attacker ambushes the defender, gaining a surprise attack!")
            attacker.temp_damage_bonus = 20
        elif scenario_type == "siege":
            ui_instance.slow_print("The defender is sieged, suffering a defense penalty!")
            defender.temp_armor_penalty = 10
        elif scenario_type == "boss_battle":
            ui_instance.slow_print("A boss battle begins! The boss has increased stats.")
            attacker.stats.max_health += 50
            attacker.stats.current_health += 50
            attacker.temp_damage_bonus = 15
    except Exception as e:
        print(f"Error handling complex scenario: {e}")

def handle_dynamic_event(attacker, defender, event_type: str, ui_instance: UI):
    from items import generate_random_item # Local import
    try:
        if event_type == "environmental_hazard":
            ui_instance.slow_print("A sudden environmental hazard strikes!")
            damage = random.randint(5, 10)
            attacker.stats.take_damage(damage)
            if defender: defender.stats.take_damage(damage)
            ui_instance.slow_print(f"Both combatants take {damage} damage!")
        elif event_type == "npc_reinforcements":
            ui_instance.slow_print("NPC reinforcements arrive!")
            pass
        elif event_type == "item_drop":
            dropped_item = generate_random_item("misc", attacker.level)
            if dropped_item:
                ui_instance.slow_print(f"{defender.name} dropped {dropped_item.name}!")
                attacker.add_item(dropped_item)
    except Exception as e:
        print(f"Error handling dynamic event: {e}")

def apply_event_effects(attacker, defender, event_type: str):
    try:
        if event_type == "environmental_change":
            pass
        elif event_type == "npc_reinforcements":
            pass
    except Exception as e:
        print(f"Error handling event effects: {e}")