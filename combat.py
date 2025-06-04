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
from combat_interactions import Combo, create_dynamic_interaction


class Combat:
    """Handles combat encounters between player and NPCs"""
    def __init__(self, player: Player, enemies: List[NPC], location: Dict):
        self.player = player
        # Store the initial list of enemies for reward calculation, as self.enemies can change (e.g. flee)
        self.initial_enemies = list(enemies) # Make a copy
        self.enemies = [e for e in enemies if e.stats.is_alive()]
        self.location = location
        self.allies: List[NPC] = [ally for ally in player.followers if ally.stats.is_alive()]
        self.player_summons: List[NPC] = []
        self.turn = 0
        self.combat_log = [] # Consider using this to log events
        self.last_attacker: Optional[NPC] = None
        self.combo_counter = 0
        self.last_attack_time = datetime.utcnow()
        self.available_combos = [
            Combo("Quick Strike", ["attack", "attack"], 1.2, 15),
            Combo("Heavy Blow", ["attack", "block", "attack"], 1.5, 25),
        ]

        ui_instance = UI # Assuming UI is a class with static methods or a global instance

        def counterattack_effect(attacker, defender):
            damage = calculate_damage_logic(attacker, defender, ui_instance, 0, False)
            defender.stats.take_damage(damage)
            return f"{attacker.name} executes a swift counterattack, hitting {defender.name} for {damage} damage!"

        self.counterattack = create_dynamic_interaction(
            "Counterattack",
            lambda attacker, defender: attacker.is_blocking and self.last_attacker != None,
            counterattack_effect
        )

        all_participants = [self.player] + self.enemies + self.allies + self.player_summons
        for char in all_participants:
            if not hasattr(char, 'status_effects'):
                char.status_effects = []
            if hasattr(char, 'summon_duration') and char.summon_duration is None and char in self.player_summons :
                char.summon_duration = 3 # Default summon duration if not set by spell


    def _apply_status_effects(self, character) -> List[str]:
        messages = []
        new_effects = [] # Effects that persist

        # Iterate over a copy if effects can be removed during iteration (though current logic appends to new_effects)
        for effect in list(character.status_effects): # Iterate copy in case effect.apply modifies list
            messages.extend(effect.apply(character)) # Apply effect (damage, stat changes)
            if not effect.tick(): # Decrease duration, check if expired
                new_effects.append(effect)
            else:
                messages.append(f"{character.name}'s {effect.effect_type.value} effect wears off.")

        character.status_effects = new_effects
        return messages

    def get_power_attack_cost(self) -> int:
        return 25

    def get_dodge_cost(self) -> int:
        return 20

    def _is_ranged_attack(self, character) -> bool: # Used by NPC logic to determine if it *can* make a ranged attack
        if hasattr(character, 'equipment'):
            return any(item.category == "weapon" and item.equipment_tag == "ranged" for item in character.equipment)
        return False

    # Helper function, was _is_two_handed_weapon in Combat class
    def is_two_handed_weapon(self, character) -> bool:
        if not hasattr(character, 'equipment'):
            return False
        return any(item.category == "weapon" and
                    hasattr(item, 'equipment_tag') and
                    item.equipment_tag == "two_handed"
                    for item in character.equipment)

    # Helper function, was _get_weapon_damage in Combat class
    def get_weapon_damage(self, character) -> int:
        weapon_damage = 0
        if hasattr(character, 'equipment'):
            for item in character.equipment:
                if item.category == "weapon" and hasattr(item, 'base_damage'):
                    if isinstance(item.base_damage, (list, tuple)):
                        weapon_damage += random.randint(item.base_damage[0], item.base_damage[1])
                    else:
                        weapon_damage += item.base_damage
        return weapon_damage

    # Helper function, was _has_elemental_weapon in Combat class
    def has_elemental_weapon(self, character, element_type: str) -> bool:
        if not hasattr(character, 'equipment'):
            return False
        return any(item.category == "weapon" and
                    hasattr(item, 'enchantment') and
                    element_type in item.enchantment.lower()
                    for item in character.equipment)

    def handle_complex_scenario(self, attacker, defender, scenario_type: str):
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
                    defender.stats.take_damage(5)
                    ui_instance.slow_print(f"{defender.name} takes 5 poison damage!")
        except Exception as e:
            print(f"Error handling complex scenario: {e}")

    def handle_dynamic_event(self, attacker, defender, event_type: str):
        ui_instance = UI
        try:
            if event_type == "environmental_hazard":
                ui_instance.slow_print("A sudden environmental hazard strikes!")
                # Apply damage to both combatants
                damage = random.randint(5, 10)
                attacker.stats.take_damage(damage)
                defender.stats.take_damage(damage)
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

    def apply_event_effects(self, attacker, defender, event_type: str):
        try:
            if event_type == "environmental_change":
                # Change the environment
                pass
            elif event_type == "npc_reinforcements":
                # Add NPC reinforcements
                pass
        except Exception as e:
            print(f"Error handling event effects: {e}")

    # player_turn and npc_turn are now imported functions

    def run(self):
        UI.print_heading(f"Combat at {self.location['name']}")
        player_action_result = True # True if turn taken, False if fled, "REPROMPT" if invalid action

        # Store enemies defeated during *this* combat instance for accurate rewards
        self.defeated_in_this_combat: List[NPC] = []

        # Complex Scenario Handling
        scenario_type = random.choice(["ambush", "siege", "boss_battle", "environmental_effect", None])  # Randomly choose a scenario
        if scenario_type:
            self.handle_complex_scenario(self.player, self.enemies[0] if self.enemies else None, scenario_type)

        while self.player.stats.is_alive() and self.enemies:
            self.turn += 1
            UI.print_heading(f"Turn {self.turn}")

            # Dynamic Event Handling
            event_type = random.choice(["environmental_hazard", "npc_reinforcements", "item_drop", None])  # Randomly choose an event
            if event_type:
                self.handle_dynamic_event(self.player, self.enemies[0] if self.enemies else None, event_type)
                self.apply_event_effects(self.player, self.enemies[0] if self.enemies else None, event_type)

            # Apply status effects at the start of each combatant's "upkeep" phase or turn
            # Order: Player, Allies, Summons, Enemies
            all_current_combatants = [self.player] + self.allies + self.player_summons + self.enemies
            for combatant in all_current_combatants:
                if combatant.stats.is_alive(): # Only apply to living combatants
                    messages = self._apply_status_effects(combatant)
                    for msg in messages:
                        UI.slow_print(msg)
                    # Check if status effects defeated someone
                    if not combatant.stats.is_alive():
                        UI.slow_print(f"{combatant.name} succumbed to their afflictions!")
                        if combatant != self.player and combatant not in self.defeated_in_this_combat:
                             self.defeated_in_this_combat.append(combatant)


            # Refresh enemy, ally, summon lists based on who is still alive
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            self.allies = [a for a in self.allies if a.stats.is_alive()]
            self.player_summons = [s for s in self.player_summons if s.stats.is_alive()]


            if not self.player.stats.is_alive():
                # UI.slow_print("You succumbed to your wounds!") # Message handled by status effect or attack
                break
            if not self.enemies:
                UI.slow_print("All enemies have been defeated!")
                break

            # --- Player's Turn ---
            self.player.is_blocking = False # Reset block status at start of player's turn
            # player.is_dodging is handled within handle_player_turn

            try:
                player_action_result = handle_player_turn(self) # Pass self (the combat_instance)
                while player_action_result == "REPROMPT_PLAYER_ACTION":
                    player_action_result = handle_player_turn(self)

                if player_action_result is False: # Player Fled
                    break # Exit combat loop
            except Exception as e:
                UI.slow_print(f"Error during player turn: {e}")
                break

            # Check if player's action defeated enemies
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            for enemy in list(self.initial_enemies): # Check against original list
                if not enemy.stats.is_alive() and enemy not in self.defeated_in_this_combat:
                    self.defeated_in_this_combat.append(enemy)
            if not self.enemies: break


            # --- Allies' (Followers & Summons) Turn ---
            current_allies_and_summons = self.allies + self.player_summons
            if current_allies_and_summons:
                UI.print_subheading("Allies' Turn:")
                for ally_npc in current_allies_and_summons[:]: # Iterate copy as list might change
                    if not ally_npc.stats.is_alive():
                        if ally_npc in self.allies: self.allies.remove(ally_npc)
                        if ally_npc in self.player_summons: self.player_summons.remove(ally_npc)
                        continue

                    if hasattr(ally_npc, 'summon_duration'):
                        ally_npc.summon_duration -= 1
                        if ally_npc.summon_duration <= 0:
                            UI.slow_print(f"{ally_npc.name} (Summon) vanishes as its energy fades.")
                            if ally_npc in self.player_summons: self.player_summons.remove(ally_npc)
                            # Do not remove from self.allies here if it was a follower that got summoned then duration expired
                            continue

                    if self.enemies:
                        target_enemy = get_target_logic(ally_npc, self.enemies, UI, self.player, self.allies, self.player_summons)
                        if target_enemy:
                            ally_damage = calculate_damage_logic(ally_npc, target_enemy, UI, 0, False) # Allies don't use combo/power attack
                            target_enemy.stats.take_damage(ally_damage)
                            UI.slow_print(f"{ally_npc.name} attacks {target_enemy.name} for {ally_damage} damage!")
                            apply_and_log_weapon_effects_logic(ally_npc, target_enemy, UI) # Allies can have weapon effects

                            if not target_enemy.stats.is_alive():
                                UI.slow_print(f"{target_enemy.name} was defeated by {ally_npc.name}!")
                                if target_enemy not in self.defeated_in_this_combat:
                                    self.defeated_in_this_combat.append(target_enemy)
                                self.enemies = [e for e in self.enemies if e.stats.is_alive()]
                                if not self.enemies: break # Break from ally turns if all enemies down
                        else:
                            UI.slow_print(f"{ally_npc.name} looks for a target but finds none.")
                    else:
                        # UI.slow_print(f"{ally_npc.name} stands ready, but all foes are vanquished.")
                        break # Break from ally turns
                if not self.enemies: break # Break from main combat loop

            # --- Enemy Turns ---
            for enemy_npc in self.enemies[:]: # Iterate copy as list might change (e.g. enemy flees)
                if not enemy_npc.stats.is_alive(): continue # Already defeated this turn (e.g. by ally)
                if not self.player.stats.is_alive(): break # Player was defeated

                # Store the last attacker
                self.last_attacker = enemy_npc

                try:
                    if not handle_npc_turn(self, enemy_npc): # Pass self (combat_instance) and enemy_npc
                        # Player was defeated by this NPC's turn
                        break # Break from enemy turns

                    # Handle counter-attack logic
                    if hasattr(self.player, 'is_blocking') and self.player.is_blocking:
                        from combat_logic import handle_counter_attack_logic
                        handle_counter_attack_logic(self.player, enemy_npc, UI, self.combo_counter, False)

                except Exception as e:
                    UI.slow_print(f"Error during enemy turn: {e}")
                    break

            if not self.player.stats.is_alive():
                break # Break from main combat loop

        # Combat End
        self.player.combat = None # Clear player's combat status
        UI.print_heading("Combat Ended")

        if self.player.stats.is_alive() and player_action_result is True: # Player won and didn't flee
            self._handle_combat_rewards()
        elif player_action_result is False: # Player fled
            UI.slow_print("You receive no rewards for fleeing.")
        else: # Player was defeated
            UI.slow_print("Darkness takes you... You have been defeated.")


    def _handle_combat_rewards(self):
        UI.print_heading("Combat Rewards")

        # Use self.defeated_in_this_combat for rewards
        if not self.defeated_in_this_combat:
            UI.slow_print("No enemies were defeated for rewards.") # Or some other message
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
                for item in list(enemy.equipment): # Iterate copy if items are removed upon looting
                    if random.random() < 0.4: # Chance to loot equipped item
                        if self.player.add_item(item):
                            UI.slow_print(f"You loot {item.name} from {enemy.name}'s corpse.")
                            # Optionally remove from enemy's equipment if it matters post-combat
                        else:
                            UI.slow_print(f"You found {item.name} on {enemy.name}, but your inventory is full!")
            # Loot inventory
            if hasattr(enemy.stats, 'inventory'):
                for item in list(enemy.stats.inventory): # Iterate copy
                    if random.random() < 0.3: # Chance to loot inventory item
                        if self.player.add_item(item):
                            UI.slow_print(f"You find {item.name} in {enemy.name}'s belongings.")
                        # No "inventory full" message here as it's less critical than equipped gear
            # Chance for a generic random drop
            if random.random() < 0.15: # Lowered chance for generic item if specific loot exists
                dropped_item = generate_random_item("misc", self.player.level)
                if dropped_item and self.player.add_item(dropped_item):
                    UI.slow_print(f"{enemy.name} also dropped: {dropped_item.name}!")


def calculate_damage_logic(attacker, defender, ui_instance: UI, combo_counter: int, player_is_power_attacking: bool, is_ranged: bool = False, body_part: str = None) -> int:
    if is_ranged:
        base_damage = attacker.stats.agility // 3
        skill_modifier = attacker.skills.get("archery", 0) // 4
    else:
        base_damage = attacker.stats.strength // 3
        weapon_type_skill = "two_handed" if is_two_handed_weapon(attacker) else "one_handed"
        skill_modifier = attacker.skills.get(weapon_type_skill, 0) // 4

    weapon_dmg = get_weapon_damage(attacker)
    total_damage = base_damage + weapon_dmg + skill_modifier

    crit_chance = attacker.stats.luck // 3
    if is_ranged:
        crit_chance += attacker.skills.get("archery", 0) // 4
    else:
        crit_chance += attacker.skills.get(weapon_type_skill, 0) // 4

    if random.randint(1, 100) <= crit_chance:
        total_damage = int(total_damage * 1.5)
        ui_instance.slow_print(f"{attacker.name} lands a critical hit!")

    # Assuming combo_counter and player_is_power_attacking are passed for the player
    # For NPCs, these specific player-only mechanics won't apply or will be 0/False.
    if combo_counter > 0 and not player_is_power_attacking: # Check if attacker is the one with combo
        combo_bonus = min(combo_counter * 0.1, 0.5)
        total_damage = int(total_damage * (1 + combo_bonus))
        ui_instance.slow_print(f"Combo x{combo_counter}! ({int(combo_bonus*100)}% bonus damage)")

    armor_reduction = defender.stats.armor_rating if hasattr(defender.stats, 'armor_rating') else 0

    if hasattr(defender, 'is_blocking') and defender.is_blocking and not is_ranged:
        block_skill = defender.skills.get("block", 0)
        shield_bonus = 0
        equipped_shield = next((item for item in defender.equipment if item.equipment_tag == "off_hand" and item.category == "armor"), None)
        if equipped_shield:
            shield_bonus = equipped_shield.armor_rating

        block_effectiveness_percent = min( (block_skill * 0.6 + shield_bonus * 0.4) / 100, 0.85)
        damage_reduction_from_block = int(total_damage * block_effectiveness_percent)
        total_damage = max(0, total_damage - damage_reduction_from_block)
        ui_instance.slow_print(f"{defender.name} blocks, reducing damage by {damage_reduction_from_block} ({int(block_effectiveness_percent*100)}%)!")

        if hasattr(defender, 'improve_skill'):
            defender.improve_skill("block", 1)

        if hasattr(defender.stats, 'current_fatigue'):
            block_stamina_cost = 5
            defender.stats.current_fatigue = max(0, defender.stats.current_fatigue - block_stamina_cost)

    # Body Part Targeting
    if body_part:
        if body_part == "Head":
            total_damage = int(total_damage * 1.5)  # Headshots do 1.5x damage
            ui_instance.slow_print("Headshot!")
        elif body_part in ["Left Arm", "Right Arm"]:
            total_damage = int(total_damage * 0.75)  # Arm shots do 0.75x damage
            ui_instance.slow_print("Hit the arm!")
        elif body_part in ["Left Leg", "Right Leg"]:
            total_damage = int(total_damage * 0.75)  # Leg shots do 0.75x damage
            defender.stats.agility = max(0, defender.stats.agility - 2)  # Reduce agility
            ui_instance.slow_print("Hit the leg! Agility reduced.")

    final_damage = max(0, total_damage - armor_reduction)

    if has_elemental_weapon(attacker, "fire"):
        final_damage *= (100 - defender.stats.fire_resist) / 100
    if has_elemental_weapon(attacker, "frost"):
        final_damage *= (100 - defender.stats.frost_resist) / 100
    if has_elemental_weapon(attacker, "shock"):
        final_damage *= (100 - defender.stats.shock_resist) / 100

    return int(final_damage)

# Helper function, was _is_two_handed_weapon in Combat class
def is_two_handed_weapon(character) -> bool:
    if not hasattr(character, 'equipment'):
        return False
    return any(item.category == "weapon" and
                hasattr(item, 'equipment_tag') and
                item.equipment_tag == "two_handed"
                for item in character.equipment)

# Helper function, was _get_weapon_damage in Combat class
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

# Helper function, was _has_elemental_weapon in Combat class
def has_elemental_weapon(character, element_type: str) -> bool:
    if not hasattr(character, 'equipment'):
        return False
    return any(item.category == "weapon" and
                hasattr(item, 'enchantment') and
                element_type in item.enchantment.lower()
                for item in character.equipment)