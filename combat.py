# combat.py
import random
from typing import List, Dict, Optional
from datetime import datetime

from ui import UI
from items import Item, generate_random_item
from player import Player
from npc_entities import NPC
from spells import Spell
from status_effects import StatusEffect
from combat_utils import Combo, create_dynamic_interaction
from combat_logic import (
    apply_and_log_weapon_effects_logic,
    handle_counter_attack_logic,
    handle_complex_scenario,
    handle_dynamic_event,
    apply_event_effects,
)
from damage_utils import calculate_damage_logic
from combat_targeting import get_target_logic
from combat_player_actions import handle_player_turn
from combat_npc_actions import handle_npc_turn

class Combat:
    """Handles combat encounters between player and NPCs."""
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

        # Initialize status effects and summon durations for all participants
        all_participants = [self.player] + self.enemies + self.allies + self.player_summons
        for char in all_participants:
            if not hasattr(char, 'status_effects'):
                char.status_effects = []
            if hasattr(char, 'summon_duration') and char.summon_duration is None and char in self.player_summons:
                char.summon_duration = 3

    def _apply_status_effects(self, character) -> List[str]:
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
        
    def is_ranged_attack(self, character) -> bool:
        if hasattr(character, 'equipment'):
            return any(item.category == "weapon" and hasattr(item, 'equipment_tag') and item.equipment_tag == "ranged" for item in character.equipment)
        return False

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
            if not player_action_result:
                break

            newly_defeated_player = [e for e in self.enemies if not e.stats.is_alive() and e not in self.defeated_in_this_combat]
            self.defeated_in_this_combat.extend(newly_defeated_player)
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            if not self.enemies: break

            # Allies' Turn
            for ally in self.allies + self.player_summons:
                if ally.stats.is_alive() and self.enemies:
                     handle_npc_turn(self, ally)
                     if not self.player.stats.is_alive(): break
            if not self.player.stats.is_alive(): break

            newly_defeated_ally = [e for e in self.enemies if not e.stats.is_alive() and e not in self.defeated_in_this_combat]
            self.defeated_in_this_combat.extend(newly_defeated_ally)
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            if not self.enemies: break

            # Enemies' Turn
            for enemy in self.enemies:
                if enemy.stats.is_alive():
                    self.last_attacker = enemy
                    handle_npc_turn(self, enemy)
                    if not self.player.stats.is_alive():
                        break
            if not self.player.stats.is_alive(): break

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
            # Loot inventory (includes equipped items for NPCs)
            if hasattr(enemy.stats, 'inventory'):
                for item in enemy.stats.inventory:
                    if random.random() < 0.35:
                        if self.player.add_item(item):
                            UI.slow_print(f"You find a(n) {item.name} on {enemy.name}'s remains.")
                        else:
                             UI.slow_print(f"You find {item.name}, but your inventory is full!")