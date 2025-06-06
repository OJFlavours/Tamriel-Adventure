# combat.py

import random
from typing import List, Dict, Optional
from datetime import datetime

from ui import UI
from items import Item, generate_random_item
from player import Player
from npc_entities import NPC  # Corrected import for NPC
from tags import get_tags  # Corrected import for get_tags
from spells import Spell
from status_effects import StatusEffect, StatusEffectType, WeaponEffect
from combat_logic import (
    apply_and_log_weapon_effects_logic,
    # handle_counter_attack_logic, # This was in combat_logic.py but not used in the original Combat class run loop
    # handle_complex_scenario,
    # handle_dynamic_event,
    apply_event_effects,
)
from combat_targeting import get_target_logic, get_body_part_choice
from combat_player_actions import handle_player_turn
from combat_npc_actions import handle_npc_turn
from combat_utils import Combo, create_dynamic_interaction

# Helper function
def get_weapon_damage(character) -> int:
    weapon_damage = 0
    if hasattr(character, 'equipment'):
        for item in character.equipment:
            if item.category == "weapon" and hasattr(item, 'base_damage'):
                if isinstance(item.base_damage, (list, tuple)):
                    weapon_damage += random.randint(item.base_damage[0], item.base_damage[1])
                else:
                    weapon_damage += item.base_damage
    return weapon_damage


# Helper function
def has_elemental_weapon(character, element_type: str) -> bool:
    if not hasattr(character, 'equipment'):
        return False
    return any(item.category == "weapon" and
                hasattr(item, 'enchantment') and
                element_type in item.enchantment.lower()
                for item in character.equipment)


def handle_complex_scenario(attacker, defender, scenario_type: str):
    ui_instance = UI
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
        elif scenario_type == "environmental_effect":
            # Apply a random environmental effect
            effect = random.choice(["fire", "frost", "poison"])
            ui_instance.slow_print(f"The environment unleashes a {effect} effect!")
            if effect == "fire":
                defender.stats.take_damage(10)
                ui_instance.slow_print(f"{defender.name} takes 10 fire damage!")
            elif effect == "frost":
                defender.stats.agility -= 5
                ui_instance.slow_print(f"{defender.name}'s agility is reduced by 5!")
            elif effect == "poison":
                defender.stats.take_damage(10)
                ui_instance.slow_print(f"{defender.name} takes 5 poison damage!")
    except Exception as e:
        print(f"Error handling complex scenario: {e}")


def handle_dynamic_event(attacker, defender, event_type: str):
    ui_instance = UI
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
        elif event_type == "item_drop":
            # Drop a random item
            dropped_item = generate_random_item("misc", self.player.level)
            if dropped_item:
                ui_instance.slow_print(f"{defender.name} dropped {dropped_item.name}!")
                self.player.add_item(dropped_item)
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


def _handle_combat_rewards(self):
    UI.print_heading("Combat Rewards")

    # Use self.defeated_in_this_combat for rewards
    if not self.defeated_in_this_combat:
        UI.slow_print("No enemies were defeated for rewards.")  # Or some other message
        return

    base_gold = sum(enemy.level * 10 for enemy in self.defeated_in_this_combat)
    luck_bonus = self.player.stats.luck / 100
    total_gold = int(base_gold * (1 + luck_bonus))

    if total_gold > 0:
        self.player.stats.gold += total_gold
        UI.slow_print(f"You found {total_gold} gold!")

    for enemy in self.defeated_in_this_combat:
        # Loot equipment
        if hasattr(enemy, 'equipment'):
            for item in list(enemy.equipment):  # Iterate copy if items are removed upon looting
                if random.random() < 0.4:  # Chance to loot equipped item
                    if self.player.add_item(item):
                        UI.slow_print(f"You loot {item.name} from {enemy.name}'s corpse.")
                        # Optionally remove from enemy's equipment if it matters post-combat
                    else:
                        UI.slow_print(f"You found {item.name} on {enemy.name}, but your inventory is full!")
        # Loot inventory
        if hasattr(enemy.stats, 'inventory'):
            for item in list(enemy.stats.inventory):  # Iterate copy
                if random.random() < 0.3:  # Chance to loot inventory item
                    if self.player.add_item(item):
                        UI.slow_print(f"You find {enemy.name} in {enemy.name}'s belongings.")
                    # No "inventory full" message here as it's less critical than equipped gear
        # Chance for a generic random drop
        if random.random() < 0.15:  # Lowered chance for generic item if specific loot exists
            dropped_item = generate_random_item("misc", self.player.level)
            if dropped_item and self.player.add_item(item):
                UI.slow_print(f"{enemy.name} also dropped: {dropped_item.name}!")

def list_npcs_at_location(location_obj, player, npc_registry_param):
    try:
        if not location_obj:
            UI.slow_print("You are nowhere in particular.")
            return

        npcs_here = npc_registry_param.get(location_obj.id, [])
        if not npcs_here:
            UI.slow_print("No souls linger here, save the whispers of the wind.")
            return

        UI.print_heading(f"Souls at {location_obj.name}")
        active_npcs = [npc for npc in npcs_here if npc.stats.is_alive()]

        if not active_npcs:
            UI.slow_print("Only the fallen remain here.")
            return

        for i, npc in enumerate(active_npcs, 1):
            npc_info_tags = npc.tags.get("npc", {})
            attitude_display_val = npc_info_tags.get("attitude", "neutral")
            attitude_display = f"({attitude_display_val.capitalize()})" if attitude_display_val else ""
            role_display = 'Server' if npc.role == 'server' else npc.role.replace('_', ' ').title()
            UI.print_info(f"[{i}] {npc.full_name} — {role_display} ({npc.race.capitalize()}) {attitude_display}")
        UI.print_line()

        sel = UI.print_prompt("With whom do you wish to parley? (0 to pass)").strip()
        if sel.isdigit():
            choice_index = int(sel)
            if 1 <= choice_index <= len(active_npcs):
                selected_npc = active_npcs[choice_index - 1]
                selected_npc_attitude_tags = selected_npc.tags.get("npc", {}).get("attitude", "")
                
                is_hostile = "hostile" in selected_npc_attitude_tags or \
                              selected_npc.role in HOSTILE_ROLES or \
                              any(ht in selected_npc.role.lower() for ht in ["bandit", "draugr", "skeleton", "vampire", "wolf", "bear", "spider", "chaurus", "falmer", "forsworn_hostile_variant"])
                if is_hostile and player.combat is None:
                    print(f"DEBUG: is_hostile = {is_hostile}")
                    UI.slow_print(f"{selected_npc.name} snarls and lunges with clear hostile intent!")
                    combat_instance = Combat(player, [selected_npc], location_obj)
                    player.combat = combat_instance
                    combat_instance.run()
            elif player.combat is not None:
                 UI.slow_print("You are already engaged in combat!")
            else:
                handle_npc_dialogue(selected_npc, player, location_obj)
        elif choice_index != 0:
            UI.slow_print("No such soul stands before you.")
    except Exception as e:
        UI.print_failure(f"Error in list_npcs_at_location: {e}")

# Helper function
def is_two_handed_weapon(character) -> bool:
    if not hasattr(character, 'equipment'):
        return False
    return any(item.category == "weapon" and
                hasattr(item, 'equipment_tag') and
                item.equipment_tag == "two_handed"
                for item in character.equipment)

# Helper function
def get_weapon_damage(character) -> int:
    weapon_damage = 0
    if hasattr(character, 'equipment'):
        for item in character.equipment:
            if item.category == "weapon" and hasattr(item, 'base_damage'):
                if isinstance(item.base_damage, (list, tuple)):
                    weapon_damage += random.randint(item.base_damage[0], item.base_damage[1])
                else:
                    weapon_damage += item.base_damage
    return weapon_damage

# Helper function
def has_elemental_weapon(character) -> bool:
    if not hasattr(character, 'equipment'):
        return False
    return any(item.category == "weapon" and
                hasattr(item, 'enchantment') and
                element_type in item.enchantment.lower()
                for item in character.equipment)