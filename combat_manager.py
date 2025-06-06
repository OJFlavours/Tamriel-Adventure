# combat_manager.py
import random
from typing import List, Optional, Dict

from ui import UI
from items import Item, generate_random_item
from player import Player
from npc_entities import NPC
from status_effects import StatusEffect
from damage_utils import calculate_damage_logic
from combat_targeting import get_target_logic
from combat_player_actions import handle_player_turn
from combat_npc_actions import handle_npc_turn
from combat_utils import Combo, create_dynamic_interaction

class Combat:
    """Handles combat encounters between player and NPCs"""
    def __init__(self, player: Player, enemies: List[NPC], location: Dict):
        self.player = player
        self.initial_enemies = list(enemies)
        self.enemies = [e for e in enemies if e.stats.is_alive()]
        self.location = location
        self.allies: List[NPC] = [ally for ally in player.followers if ally.stats.is_alive()]
        self.player_summons: List[NPC] = []
        self.turn = 0
        self.combat_log: List[str] = []
        self.last_attacker: Optional[NPC] = None
        self.combo_counter = 0
        self.available_combos = [
            Combo("Quick Strike", ["attack", "attack"], 1.2, 15),
            Combo("Heavy Blow", ["attack", "block", "attack"], 1.5, 25),
        ]
        self.defeated_in_this_combat: List[NPC] = []

        ui_instance = UI
        def counterattack_effect(attacker, defender):
            damage = calculate_damage_logic(attacker, defender, ui_instance, 0, False)
            defender.stats.take_damage(damage)
            return f"{attacker.name} executes a swift counterattack, hitting {defender.name} for {damage} damage!"

        self.counterattack = create_dynamic_interaction(
            "Counterattack",
            lambda attacker, defender: attacker.is_blocking and self.last_attacker is not None,
            counterattack_effect
        )

        all_participants = [self.player] + self.enemies + self.allies + self.player_summons
        for char in all_participants:
            if not hasattr(char, 'status_effects'):
                char.status_effects = []
            if hasattr(char, 'summon_duration') and char.summon_duration is None and char in self.player_summons:
                char.summon_duration = 3

    def _apply_status_effects(self, character):
        messages = []
        if not hasattr(character, 'status_effects'):
            return messages
        
        effects_to_keep = []
        for effect in character.status_effects:
            messages.extend(effect.apply(character))
            if not effect.tick():
                effects_to_keep.append(effect)
            else:
                messages.append(f"{character.name}'s {effect.effect_type.value} effect wears off.")
        character.status_effects = effects_to_keep
        return messages

    def get_power_attack_cost(self) -> int:
        return 25

    def get_dodge_cost(self) -> int:
        return 20

    def run(self):
        UI.print_heading(f"Combat at {self.location['name']}")
        player_action_result = True

        while self.player.stats.is_alive() and self.enemies:
            self.turn += 1
            UI.print_heading(f"Turn {self.turn}")

            # Apply status effects for all combatants
            all_combatants = [self.player] + self.allies + self.player_summons + self.enemies
            for combatant in all_combatants:
                if combatant.stats.is_alive():
                    status_messages = self._apply_status_effects(combatant)
                    for msg in status_messages:
                        UI.slow_print(msg)
                    if not combatant.stats.is_alive():
                        UI.slow_print(f"{combatant.name} has succumbed to their afflictions!")
                        if combatant in self.enemies and combatant not in self.defeated_in_this_combat:
                            self.defeated_in_this_combat.append(combatant)

            # Refresh lists of living combatants
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            self.allies = [a for a in self.allies if a.stats.is_alive()]
            self.player_summons = [s for s in self.player_summons if s.stats.is_alive()]

            if not self.player.stats.is_alive() or not self.enemies:
                break

            # Player's Turn
            self.player.is_blocking = False
            player_action_result = handle_player_turn(self)
            if not player_action_result: # Player fled
                break

            # Check for defeated enemies after player's turn
            newly_defeated = [e for e in self.enemies if not e.stats.is_alive() and e not in self.defeated_in_this_combat]
            self.defeated_in_this_combat.extend(newly_defeated)
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]

            if not self.enemies:
                break

            # Allies' Turn
            for ally in self.allies + self.player_summons:
                if ally.stats.is_alive() and self.enemies:
                     handle_npc_turn(self, ally) # Allies use the same turn logic as enemies
                     self.enemies = [e for e in self.enemies if e.stats.is_alive()]
                     if not self.enemies:
                         break
            if not self.enemies:
                break
            
            # Enemies' Turn
            for enemy in self.enemies:
                if enemy.stats.is_alive():
                    self.last_attacker = enemy
                    handle_npc_turn(self, enemy)
                    if not self.player.stats.is_alive():
                        break
            if not self.player.stats.is_alive():
                break

        # Combat End
        self.player.combat = None
        UI.print_heading("Combat Ended")
        if self.player.stats.is_alive() and player_action_result:
            UI.slow_print("You are victorious!")
            self._handle_combat_rewards()
        elif not self.player.stats.is_alive():
            UI.slow_print("Darkness takes you... You have been defeated.")
        else:
            UI.slow_print("You escape to fight another day.")
            
    def _handle_combat_rewards(self):
        UI.print_heading("Combat Rewards")
        if not self.defeated_in_this_combat:
            UI.slow_print("No enemies were defeated for rewards.")
            return

        total_xp = sum(enemy.level * 10 for enemy in self.defeated_in_this_combat)
        self.player.gain_experience(total_xp)

        base_gold = sum(enemy.level * 5 for enemy in self.defeated_in_this_combat)
        luck_bonus = 1 + (self.player.stats.luck / 100)
        total_gold = int(base_gold * luck_bonus)
        
        if total_gold > 0:
            self.player.stats.gold += total_gold
            UI.slow_print(f"You loot {total_gold} gold.")

        for enemy in self.defeated_in_this_combat:
            if hasattr(enemy.stats, 'inventory'):
                for item in enemy.stats.inventory:
                    if random.random() < 0.35: # 35% chance to drop each item
                        if self.player.add_item(item):
                            UI.slow_print(f"You find a(n) {item.name} on {enemy.name}'s remains.")
                        else:
                             UI.slow_print(f"You find {item.name}, but your inventory is full!")
def apply_weapon_effects(attacker, defender, weapon):
    messages = []
    messages.append(f"{attacker.name}'s {weapon.name} applies its special effect to {defender.name}!")
    return messages
def apply_and_log_weapon_effects_logic(attacker, defender, ui_instance: UI, is_ranged: bool = False):
    if attacker.equipment:
        weapon_to_check = None
        if is_ranged:
            weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and item.equipment_tag == "ranged"), None) or None
        else:
            weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and (item.equipment_tag == "main_hand" or item.equipment_tag == "two_handed")), None) or None

        if weapon_to_check:
            messages = apply_weapon_effects(attacker, defender, weapon_to_check)
            for msg in messages:
                ui_instance.slow_print(msg)
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