# combat.py

import random
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime
from ui import UI
from items import Item, generate_random_item
from player import Player
from npc import NPC, get_tags

class StatusEffectType(Enum):
    BLEEDING = "Bleeding"
    BURNING = "Burning"
    FROZEN = "Frozen"
    POISONED = "Poisoned"
    STUNNED = "Stunned"

class StatusEffect:
    def __init__(self, effect_type: StatusEffectType, duration: int, potency: float):
        self.effect_type = effect_type
        self.duration = duration
        self.potency = potency
        
    def apply(self, character) -> List[str]:
        """Apply effect based on character's existing Stats attributes"""
        messages = []
        if self.effect_type == StatusEffectType.BLEEDING:
            damage = int(character.stats.max_health * 0.05 * self.potency)
            character.stats.current_health = max(1, character.stats.current_health - damage)
            messages.append(f"{character.name} bleeds for {damage} damage!")
            
        elif self.effect_type == StatusEffectType.BURNING:
            damage = int(10 * self.potency * (1 - character.stats.fire_resist/100))
            character.stats.current_health = max(1, character.stats.current_health - damage)
            messages.append(f"{character.name} burns for {damage} damage!")
            character.stats.current_fatigue = max(0, character.stats.current_fatigue - 5)
            
        elif self.effect_type == StatusEffectType.FROZEN:
            reduction = int(10 * self.potency * (1 - character.stats.frost_resist/100))
            character.stats.speed = max(1, character.stats.speed - reduction)
            character.stats.agility = max(1, character.stats.agility - reduction)
            messages.append(f"{character.name}'s movement is slowed by frost!")
            
        elif self.effect_type == StatusEffectType.POISONED:
            damage = int(8 * self.potency * (1 - character.stats.poison_resist/100))
            character.stats.current_health = max(1, character.stats.current_health - damage)
            messages.append(f"{character.name} takes {damage} poison damage!")
            
        elif self.effect_type == StatusEffectType.STUNNED:
            messages.append(f"{character.name} is stunned and loses their next action!")
            
        return messages

    def tick(self) -> bool:
        """Returns True if effect should be removed"""
        self.duration -= 1
        return self.duration <= 0

class WeaponEffect:
    def __init__(self, name: str, trigger_chance: float, effect: StatusEffectType, duration: int, potency: float):
        self.name = name
        self.trigger_chance = trigger_chance
        self.effect = effect
        self.duration = duration
        self.potency = potency

class Combat:
    """Handles combat encounters between player and NPCs"""
    def __init__(self, player: Player, enemies: List[NPC], location: Dict):
        self.player = player
        self.enemies = enemies
        self.location = location
        self.turn = 0
        self.combat_log = []
        self.combo_counter = 0
        self.last_attack_time = datetime.utcnow()
        
        # Initialize status effects lists if they don't exist
        if not hasattr(self.player, 'status_effects'):
            self.player.status_effects = []
        for enemy in self.enemies:
            if not hasattr(enemy, 'status_effects'):
                enemy.status_effects = []

    def _apply_status_effects(self, character) -> List[str]:
        """Applies and ticks down status effects for a character"""
        messages = []
        new_effects = []
        
        for effect in character.status_effects:
            messages.extend(effect.apply(character))
            if not effect.tick():
                new_effects.append(effect)
            else:
                messages.append(f"{character.name}'s {effect.effect_type.value} effect wears off.")
        
        character.status_effects = new_effects
        return messages

    def _calculate_damage(self, attacker, defender, is_ranged: bool = False) -> int:
        """Enhanced damage calculation using existing stats system"""
        # Base damage from stats
        if is_ranged:
            base_damage = attacker.stats.agility // 10
            skill_modifier = attacker.skills.get("archery", 0) // 10
        else:
            base_damage = attacker.stats.strength // 10
            weapon_type = "two_handed" if self._is_two_handed_weapon(attacker) else "one_handed"
            skill_modifier = attacker.skills.get(weapon_type, 0) // 10

        # Weapon damage
        weapon_damage = self._get_weapon_damage(attacker)
        total_damage = base_damage + weapon_damage + skill_modifier

        # Critical hit system
        crit_chance = attacker.stats.luck // 2  # Base 0.5% per luck point
        if is_ranged:
            crit_chance += attacker.skills.get("archery", 0) // 4
        else:
            crit_chance += attacker.skills.get(weapon_type, 0) // 4
            
        if random.randint(1, 100) <= crit_chance:
            total_damage = int(total_damage * 1.5)
            UI.slow_print(f"{attacker.name} lands a critical hit!")

        # Combo system (only for player)
        if attacker == self.player and hasattr(self, 'combo_counter') and self.combo_counter > 0:
            combo_bonus = min(self.combo_counter * 0.1, 0.5)  # Max 50% bonus
            total_damage = int(total_damage * (1 + combo_bonus))
            UI.slow_print(f"Combo x{self.combo_counter}! ({int(combo_bonus*100)}% bonus damage)")

        # Defense calculations
        armor_reduction = defender.stats.armor_rating if hasattr(defender.stats, 'armor_rating') else 0
        final_damage = max(0, total_damage - armor_reduction)

        # Apply resistances for enchanted weapons
        if self._has_elemental_weapon(attacker, "fire"):
            final_damage *= (100 - defender.stats.fire_resist) / 100
        if self._has_elemental_weapon(attacker, "frost"):
            final_damage *= (100 - defender.stats.frost_resist) / 100
        if self._has_elemental_weapon(attacker, "shock"):
            final_damage *= (100 - defender.stats.shock_resist) / 100

        return int(final_damage)

    def _get_weapon_damage(self, character) -> int:
        """Get base weapon damage from equipped items"""
        weapon_damage = 0
        if hasattr(character, 'equipment'):
            for item in character.equipment:
                if item.category == "weapon" and hasattr(item, 'base_damage'):
                    if isinstance(item.base_damage, (list, tuple)):
                        weapon_damage += random.randint(item.base_damage[0], item.base_damage[1])
                    else:
                        weapon_damage += item.base_damage
        return weapon_damage

    def _is_two_handed_weapon(self, character) -> bool:
        """Check if character is using a two-handed weapon"""
        if not hasattr(character, 'equipment'):
            return False
        return any(item.category == "weapon" and 
                  hasattr(item, 'equipment_tag') and 
                  item.equipment_tag == "two_handed" 
                  for item in character.equipment)

    def _has_elemental_weapon(self, character, element_type: str) -> bool:
        """Check if character has a weapon with specified elemental enchantment"""
        if not hasattr(character, 'equipment'):
            return False
        return any(item.category == "weapon" and 
                  hasattr(item, 'enchantment') and 
                  element_type in item.enchantment.lower() 
                  for item in character.equipment)

    def _get_target(self, attacker, target_list: List) -> Optional[object]:
        """Helper to get a target from a list"""
        if not target_list:
            return None
        
        if attacker == self.player:
            UI.print_subheading("Choose your target:")
            for i, enemy in enumerate(target_list, 1):
                UI.print_info(f"[{i}] {enemy.name} (Health: {enemy.stats.current_health}/{enemy.stats.max_health})")
            
            while True:
                try:
                    choice = int(input("Enter target number (0 to cancel): "))
                    if choice == 0:
                        return None
                    if 1 <= choice <= len(target_list):
                        return target_list[choice - 1]
                    UI.slow_print("Invalid target number.")
                except ValueError:
                    UI.slow_print("Please enter a number.")
        else:
            return self.player  # NPCs target the player by default

    def _handle_counter_attack(self, defender, attacker):
        """Handle counter-attack mechanics"""
        if hasattr(defender, 'is_blocking') and defender.is_blocking:
            block_skill = defender.skills.get("block", 0)
            counter_chance = block_skill / 200  # 0.5% per block skill point
            
            if random.random() < counter_chance:
                UI.slow_print(f"{defender.name} performs a perfect block and counter-attacks!")
                counter_damage = self._calculate_damage(defender, attacker) // 2
                attacker.stats.current_health -= counter_damage
                UI.slow_print(f"Counter-attack deals {counter_damage} damage!")
                
                # Improve block skill for player
                if defender == self.player:
                    defender.improve_skill("block", 1)

    def _apply_weapon_effects(self, attacker, defender, weapon: Optional[Item]) -> List[str]:
        """Apply weapon special effects"""
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
                
            if effect_type and random.random() < 0.3:  # 30% chance to apply effect
                effect = StatusEffect(effect_type, duration=2, potency=1.0)
                defender.status_effects.append(effect)
                messages.extend(effect.apply(defender))
                
        return messages

    def player_turn(self) -> bool:
        """Handles the player's combat turn"""
        UI.print_subheading(f"{self.player.name}'s Turn")
        UI.print_info(f"Health: {self.player.stats.current_health}/{self.player.stats.max_health}")
        UI.print_info(f"Magicka: {self.player.stats.current_magicka}/{self.player.stats.max_magicka}")
        UI.print_info(f"Fatigue: {self.player.stats.current_fatigue}/{self.player.stats.max_fatigue}")
        
        UI.print_info("\nEnemies:")
        for i, enemy in enumerate(self.enemies, 1):
            UI.print_info(f"[{i}] {enemy.name} (Health: {enemy.stats.current_health}/{enemy.stats.max_health})")

        options = {
            "1": "Melee Attack",
            "2": "Cast Spell",
            "3": "Use Item",
            "4": "Block",
            "5": "Dodge",
            "6": "Flee"
        }

        # Add ranged attack option if player has ranged weapon
        if any(item.category == "weapon" and item.equipment_tag == "ranged" 
               for item in self.player.equipment):
            options["1.5"] = "Ranged Attack"

        UI.print_line()
        sorted_options = sorted(options.items(), key=lambda x: float(x[0]))
        UI.slow_print(" ".join([f"[{k}] {v}" for k, v in sorted_options]))
        choice = input("Your action? ")

        if choice == "1":  # Melee Attack
            target = self._get_target(self.player, self.enemies)
            if target:
                damage = self._calculate_damage(self.player, target)
                target.stats.current_health -= damage
                UI.slow_print(f"You attack {target.name} for {damage} damage!")
                
                # Apply weapon effects
                if self.player.equipment:
                    for item in self.player.equipment:
                        if item.category == "weapon":
                            messages = self._apply_weapon_effects(self.player, target, item)
                            for msg in messages:
                                UI.slow_print(msg)
                
                # Update combo counter
                self.combo_counter += 1
                
                if not target.stats.is_alive():
                    UI.slow_print(f"You defeated {target.name}!")
                    return True

        elif choice == "1.5":  # Ranged Attack
            target = self._get_target(self.player, self.enemies)
            if target:
                damage = self._calculate_damage(self.player, target, is_ranged=True)
                target.stats.current_health -= damage
                UI.slow_print(f"You shoot {target.name} for {damage} damage!")
                
                # Apply weapon effects
                if self.player.equipment:
                    for item in self.player.equipment:
                        if item.category == "weapon" and item.equipment_tag == "ranged":
                            messages = self._apply_weapon_effects(self.player, target, item)
                            for msg in messages:
                                UI.slow_print(msg)
                
                if not target.stats.is_alive():
                    UI.slow_print(f"You defeated {target.name}!")
                    return True

        elif choice == "2":  # Cast Spell
            if self.player.stats.current_magicka >= 20:
                target = self._get_target(self.player, self.enemies)
                if target:
                    spell_damage = random.randint(15, 35) + (self.player.skills.get("destruction", 0) // 5)
                    target.stats.current_health -= spell_damage
                    self.player.stats.current_magicka -= 20
                    UI.slow_print(f"You cast a Destruction spell at {target.name} for {spell_damage} damage!")
                    
                    # Improve destruction skill
                    self.player.improve_skill("destruction", 1)
                    
                    if not target.stats.is_alive():
                        UI.slow_print(f"You defeated {target.name}!")
                        return True
            else:
                UI.slow_print("Not enough magicka!")

        elif choice == "3":  # Use Item
            if self.player.inventory:
                UI.print_subheading("Your inventory:")
                usable_items = [item for item in self.player.inventory 
                              if item.category in ["potion", "food", "scroll"]]
                
                if not usable_items:
                    UI.slow_print("You have no usable items.")
                    return True
                    
                for i, item in enumerate(usable_items, 1):
                    UI.print_info(f"[{i}] {item.name} ({item.category})")
                    
                try:
                    item_choice = int(input("Use which item? (0 to cancel): "))
                    if item_choice == 0:
                        return True
                        
                    if 1 <= item_choice <= len(usable_items):
                        item = usable_items[item_choice - 1]
                        if hasattr(item, 'use'):
                            item.use(self.player)
                        else:
                            UI.slow_print(f"Cannot use {item.name} right now.")
                    else:
                        UI.slow_print("Invalid item number.")
                except ValueError:
                    UI.slow_print("Please enter a number.")
            else:
                UI.slow_print("Your inventory is empty.")

        elif choice == "4":  # Block
            UI.slow_print("You raise your defenses, ready to block!")
            self.player.is_blocking = True
            self.combo_counter = 0  # Reset combo when blocking

        elif choice == "5":  # Dodge
            UI.slow_print("You prepare to dodge incoming attacks!")
            self.player.is_dodging = True
            self.combo_counter = 0  # Reset combo when dodging

        elif choice == "6":  # Flee
            UI.slow_print("You attempt to flee!")
            flee_chance = 0.5 + (self.player.stats.agility / 200)  # Base 50% + 0.5% per agility
            if random.random() < flee_chance:
                UI.slow_print("You successfully fled from combat!")
                return False
            else:
                UI.slow_print("You failed to flee!")
                self.combo_counter = 0  # Reset combo on failed flee

        else:
            UI.slow_print("Invalid action.")
            
        return True

    def npc_turn(self, npc: NPC) -> bool:
        """Handles an NPC's combat turn"""
        if not npc.stats.is_alive():
            return True

        UI.print_subheading(f"{npc.name}'s Turn")
        UI.print_info(f"Health: {npc.stats.current_health}/{npc.stats.max_health}")

        # Reset player's defensive flags
        self.player.is_blocking = False
        self.player.is_dodging = False

        # Get NPC's traits
        npc_attitude = get_tags(npc).get("attitude", [])
        npc_class = get_tags(npc).get("class", [])
        
        if "hostile" in npc_attitude:
            # Check for fleeing when low health
            if npc.stats.current_health < npc.stats.max_health * 0.3 and random.random() < 0.4:
                UI.slow_print(f"{npc.name} attempts to flee!")
                if random.random() < 0.6:
                    UI.slow_print(f"{npc.name} successfully fled!")
                    self.enemies.remove(npc)
                    return True
                else:
                    UI.slow_print(f"{npc.name} failed to flee!")

            # Mages prefer spell casting
            if "mage" in npc_class and npc.stats.current_magicka >= 15 and random.random() < 0.6:
                spell_damage = random.randint(10, 25)
                self.player.stats.current_health -= spell_damage
                npc.stats.current_magicka -= 15
                UI.slow_print(f"{npc.name} casts a spell at you for {spell_damage} damage!")
            else:
                # Regular attack
                damage = self._calculate_damage(npc, self.player)

                # Check player defenses
                if self.player.is_blocking:
                    block_reduction = random.randint(damage // 2, damage)
                    damage = max(0, damage - block_reduction)
                    UI.slow_print("You block part of the attack!")
                    self._handle_counter_attack(self.player, npc)
                    
                elif self.player.is_dodging:
                    if random.random() < (self.player.stats.agility / 100):
                        UI.slow_print("You successfully dodge the attack!")
                        damage = 0
                        self.player.improve_skill("light_armor", 1)  # Improve evasion skill
                    else:
                        UI.slow_print("You fail to dodge the attack!")

                self.player.stats.current_health -= damage
                UI.slow_print(f"{npc.name} attacks you for {damage} damage!")

                # Apply weapon effects
                if npc.equipment:
                    for item in npc.equipment:
                        if item.category == "weapon":
                            messages = self._apply_weapon_effects(npc, self.player, item)
                            for msg in messages:
                                UI.slow_print(msg)

            if not self.player.stats.is_alive():
                UI.slow_print(f"You have been defeated by {npc.name}!")
                return False
        else:
            UI.slow_print(f"{npc.name} seems uncertain and takes no action.")
            
        return True

    def run(self):
        """Main combat loop"""
        UI.print_heading(f"Combat at {self.location['name']}")
        
        while self.player.stats.is_alive() and self.enemies:
            self.turn += 1
            UI.print_heading(f"Turn {self.turn}")

            # Apply status effects
            messages = self._apply_status_effects(self.player)
            for msg in messages:
                UI.slow_print(msg)

            for enemy in self.enemies:
                messages = self._apply_status_effects(enemy)
                for msg in messages:
                    UI.slow_print(msg)

            # Check if anyone died from status effects
            if not self.player.stats.is_alive():
                UI.slow_print("You succumbed to your wounds!")
                break

            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            if not self.enemies:
                UI.slow_print("All enemies have been defeated!")
                break

            # Player turn
            if not self.player_turn():
                break  # Combat ends if player fled

            # Update enemy list after player's turn
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            if not self.enemies:
                UI.slow_print("All enemies have been defeated!")
                break

            # Enemy turns
            for enemy in self.enemies[:]:  # Use a copy to allow removal during iteration
                if not self.npc_turn(enemy):
                    break  # Combat ends if player was defeated

        # Combat cleanup
        self.player.combat = None
        UI.print_heading("Combat Ended")

        # Handle rewards if player survived
        if self.player.stats.is_alive():
            self._handle_combat_rewards()

    def _handle_combat_rewards(self):
        """Handle post-combat rewards"""
        UI.print_heading("Combat Rewards")
        
        # Gold reward based on enemy levels and luck
        base_gold = sum(enemy.level * 10 for enemy in self.enemies)
        luck_bonus = self.player.stats.luck / 100
        total_gold = int(base_gold * (1 + luck_bonus))
        
        self.player.stats.gold += total_gold
        UI.slow_print(f"You found {total_gold} gold!")
        
        # Item drops from defeated enemies
        for enemy in self.enemies:
            if not enemy.stats.is_alive():
                # Chance to drop equipped items
                for item in enemy.equipment:
                    if random.random() < 0.4:  # 40% chance per equipped item
                        if self.player.add_item(item):
                            UI.slow_print(f"You loot {item.name} from {enemy.name}")
                        else:
                            UI.slow_print(f"You found {item.name}, but your inventory is full!")
                
                # Chance to drop inventory items
                for item in enemy.stats.inventory:
                    if random.random() < 0.3:  # 30% chance per inventory item
                        if self.player.add_item(item):
                            UI.slow_print(f"You loot {item.name} from {enemy.name}")
                
                # Random additional loot
                if random.random() < 0.4:
                    dropped_item = generate_random_item("misc", self.player.level)
                    if self.player.add_item(dropped_item):
                        UI.slow_print(f"You found: {dropped_item.name}!")