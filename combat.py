# combat.py
import random
from enum import Enum
from typing import List, Dict, Optional
from items import Item, generate_random_item # Import generate_random_item
from tags import TAGS, get_tags # Import TAGS dictionary and get_tags function
from npc import NPC
from stats import Player, Stats
from ui import UI
import flavor # Import flavor module directly

class ActionType(Enum):
    ATTACK = "attack"
    RANGED_ATTACK = "ranged_attack"
    BLOCK = "block"
    DODGE = "dodge"
    CAST_SPELL = "cast_spell"
    USE_ITEM = "use_item"
    FLEE = "flee"

class MagicSchool(Enum):
    DESTRUCTION = "destruction"
    RESTORATION = "restoration"
    ALTERATION = "alteration"
    CONJURATION = "conjuration"
    ILLUSION = "illusion"
    MYSTICISM = "mysticism"

class StatusEffectType(Enum):
    POISON = "poison"
    PARALYSIS = "paralysis"
    FROST = "frost"
    SHOCK = "shock"
    FIRE = "fire"
    SILENCE = "silence"
    WEAKNESS = "weakness"
    BLEEDING = "bleeding" # Added new status effect

class StatusEffect:
    def __init__(self, effect_type: StatusEffectType, duration: int, potency: float, source: str):
        self.effect_type = effect_type
        self.duration = duration
        self.potency = potency
        self.source = source

    def apply(self, target):
        """
        Applies the status effect to the target.
        Returns a list of messages describing the effect.
        """
        messages = []
        if self.effect_type == StatusEffectType.POISON:
            damage = int(self.potency)
            target.stats.current_health -= damage
            messages.append(f"{target.name} is poisoned and takes {damage} damage!")
        elif self.effect_type == StatusEffectType.PARALYSIS:
            messages.append(f"{target.name} is paralyzed and cannot act!")
            # This effect would typically be handled in the turn logic to skip actions
        elif self.effect_type == StatusEffectType.FROST:
            target.stats.speed = max(0, target.stats.speed - int(self.potency)) # Ensure speed doesn't go below 0
            messages.append(f"{target.name} is slowed by frost!")
        elif self.effect_type == StatusEffectType.SHOCK:
            target.stats.current_magicka = max(0, target.stats.current_magicka - int(self.potency))
            messages.append(f"{target.name} loses magicka due to shock!")
        elif self.effect_type == StatusEffectType.FIRE:
            damage = int(self.potency)
            target.stats.current_health -= damage
            messages.append(f"{target.name} is burning and takes {damage} fire damage!")
        elif self.effect_type == StatusEffectType.SILENCE:
            messages.append(f"{target.name} is silenced and cannot cast spells!")
            # This effect would typically be handled in the turn logic to prevent spellcasting
        elif self.effect_type == StatusEffectType.WEAKNESS:
            target.stats.armor_rating = max(0, target.stats.armor_rating - int(self.potency))
            messages.append(f"{target.name} is weakened, reducing their armor!")
        elif self.effect_type == StatusEffectType.BLEEDING:
            damage = int(self.potency)
            target.stats.current_health -= damage
            messages.append(f"{target.name} is bleeding and takes {damage} damage!")
        return messages

    def tick(self):
        """Decrements the duration of the effect. Returns True if the effect has worn off."""
        self.duration -= 1
        return self.duration <= 0

class Combat:
    def __init__(self, player: Player, enemies: List[NPC], location: Dict):
        self.player = player
        self.enemies = enemies
        self.location = location
        self.turn = 0
        self.combat_log = []

    def _apply_status_effects(self, character):
        """
        Applies and ticks down status effects for a character.
        Removes effects that have worn off.
        """
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

    def _get_target(self, attacker, target_list):
        """Helper to get a target from a list, prompting the player if the attacker is the player."""
        if not target_list:
            return None
        if attacker == self.player:
            UI.slow_print("Choose a target:")
            for i, enemy in enumerate(target_list):
                UI.slow_print(f"[{i+1}] {enemy.name} (Health: {enemy.stats.current_health}/{enemy.stats.max_health})")
            while True:
                try:
                    choice = int(input("Enter target number: ")) - 1
                    if 0 <= choice < len(target_list):
                        return target_list[choice]
                    else:
                        UI.slow_print("Invalid target.")
                except ValueError:
                    UI.slow_print("Invalid input. Please enter a number.")
        else:
            # NPCs target the player by default in this simplified example
            return self.player

    def _calculate_damage(self, attacker, defender, is_ranged=False):
        """
        Calculates damage based on attacker's stats, equipped items, and defender's armor/resistances.
        Includes basic critical hit chance and skill modifiers.
        """
        base_damage = 0
        # Determine base damage based on attacker's primary combat stat
        if is_ranged:
            base_damage = attacker.stats.agility // 10
            skill_modifier = attacker.skills.get("archery", 0) // 10
        else:
            base_damage = attacker.stats.strength // 10
            skill_modifier = attacker.skills.get("one_handed", 0) // 10 if not attacker.equipment or not any(item.category == "weapon" and item.equipment_tag == "two_handed" for item in attacker.equipment) else attacker.skills.get("two_handed", 0) // 10

        # Add weapon damage if equipped
        weapon_damage = 0
        if attacker.equipment:
            for item in attacker.equipment:
                if item.category == "weapon" and item.base_damage:
                    weapon_damage += random.randint(item.base_damage[0], item.base_damage[1])
        base_damage += weapon_damage + skill_modifier

        # Apply enchantment damage if any
        enchantment_damage = 0
        if attacker.equipment:
            for item in attacker.equipment:
                if item.enchantment:
                    if "fire" in item.enchantment.lower():
                        enchantment_damage += random.randint(5, 15)
                    elif "frost" in item.enchantment.lower():
                        enchantment_damage += random.randint(5, 15)
                    elif "shock" in item.enchantment.lower():
                        enchantment_damage += random.randint(5, 15)

        total_damage = base_damage + enchantment_damage

        # Critical hit chance (Luck based)
        if random.randint(1, 100) <= attacker.stats.luck // 2: # 0.5% chance per point of luck
            total_damage = int(total_damage * 1.5) # 50% extra damage for critical hit
            UI.slow_print(f"{attacker.name} lands a critical hit!")
        # Armor reduction
        armor_reduction = defender.stats.armor_rating
        final_damage = max(0, total_damage - armor_reduction)

        # Apply elemental resistances
        if "fire" in (item.enchantment.lower() for item in attacker.equipment if item.enchantment) if attacker.equipment else False:
            final_damage *= (100 - defender.stats.fire_resist) / 100
        if "frost" in (item.enchantment.lower() for item in attacker.equipment if item.enchantment) if attacker.equipment else False:
            final_damage *= (100 - defender.stats.frost_resist) / 100
        if "shock" in (item.enchantment.lower() for item in attacker.equipment if item.enchantment) if attacker.equipment else False:
            final_damage *= (100 - defender.stats.shock_resist) / 100

        # Apply magic resistance for spells (if implemented)
        # if is_spell:
        #     final_damage *= (100 - defender.stats.magic_resist) / 100

        return int(final_damage)

    def _handle_player_item_use(self, item: Item):
        """Handles the effects of using an item."""
        messages = []
        if item.category == "potion":
            if "health" in item.name.lower():
                heal_amount = random.randint(20, 50) # Example heal
                self.player.stats.current_health = min(self.player.stats.max_health, self.player.stats.current_health + heal_amount)
                messages.append(f"You used a {item.name} and restored {heal_amount} health.")
            elif "magicka" in item.name.lower():
                restore_amount = random.randint(20, 50) # Example restore
                self.player.stats.current_magicka = min(self.player.stats.max_magicka, self.player.stats.current_magicka + restore_amount)
                messages.append(f"You used a {item.name} and restored {restore_amount} magicka.")
            elif "stamina" in item.name.lower():
                restore_amount = random.randint(20, 50) # Example restore
                self.player.stats.current_fatigue = min(self.player.stats.max_fatigue, self.player.stats.current_fatigue + restore_amount)
                messages.append(f"You used a {item.name} and restored {restore_amount} stamina.")
            # Add more potion types as needed
            self.player.remove_item(item)
        elif item.category == "food":
            heal_amount = random.randint(10, 30)
            self.player.stats.current_health = min(self.player.stats.max_health, self.player.stats.current_health + heal_amount)
            messages.append(f"You ate {item.name} and restored {heal_amount} health.")
            self.player.remove_item(item)
        elif item.category == "scroll":
            # Example: A scroll of Fireball
            if "fireball" in item.name.lower():
                target = self._get_target(self.player, self.enemies)
                if target:
                    spell_damage = random.randint(25, 40)
                    target.stats.current_health -= spell_damage
                    messages.append(f"You cast a powerful Fireball from the {item.name} on {target.name} for {spell_damage} damage!")
                    if not target.stats.is_alive():
                        messages.append(f"You defeated {target.name}!")
            self.player.remove_item(item)
        else:
            messages.append(f"You can't use {item.name} in combat right now.")
        return messages


    def player_turn(self):
        """Handles the player's combat turn, offering more actions."""
        UI.slow_print(f"\n{self.player.name}'s turn (Health: {self.player.stats.current_health}/{self.player.stats.max_health}, Magicka: {self.player.stats.current_magicka}/{self.player.stats.max_magicka}, Fatigue: {self.player.stats.current_fatigue}/{self.player.stats.max_fatigue})") #cite: 1
        UI.slow_print("Enemies remaining:") #cite: 1
        for i, enemy in enumerate(self.enemies): #cite: 1
            UI.slow_print(f"  [{i+1}] {enemy.name} (Health: {enemy.stats.current_health}/{enemy.stats.max_health})") #cite: 1

        options = {
            "1": "Attack",
            "2": "Cast Spell",
            "3": "Use Item",
            "4": "Block",
            "5": "Dodge",
            "6": "Flee"
        }
        # Check for ranged weapon to add ranged attack option
        if any(item.category == "weapon" and item.equipment_tag == "ranged" for item in self.player.equipment):
            options["1.5"] = "Ranged Attack"

        sorted_options = sorted(options.items(), key=lambda item: float(item[0]))
        UI.slow_print(" ".join([f"[{k}] {v}" for k, v in sorted_options])) #cite: 1
        choice = input("What will you do? ") #cite: 1

        if choice == "1": # Melee Attack
            target = self._get_target(self.player, self.enemies)
            if target:
                damage = self._calculate_damage(self.player, target, is_ranged=False)
                target.stats.current_health -= damage
                UI.slow_print(f"You attack {target.name} for {damage} damage!") #cite: 1
                if not target.stats.is_alive():
                    UI.slow_print(f"You defeated {target.name}!") #cite: 1
                    return True
        elif choice == "1.5": # Ranged Attack
            target = self._get_target(self.player, self.enemies)
            if target:
                damage = self._calculate_damage(self.player, target, is_ranged=True)
                target.stats.current_health -= damage
                UI.slow_print(f"You launch a ranged attack at {target.name} for {damage} damage!") #cite: 1
                if not target.stats.is_alive():
                    UI.slow_print(f"You defeated {target.name}!") #cite: 1
                    return True
        elif choice == "2": # Cast Spell
            # Simplified spell casting. In a full game, this would involve spell selection, mana cost, etc.
            if self.player.stats.current_magicka >= 20: # Example cost for a basic spell
                target = self._get_target(self.player, self.enemies)
                if target:
                    spell_damage = random.randint(15, 35) + (self.player.skills.get("destruction", 0) // 5)
                    target.stats.current_health -= spell_damage
                    self.player.stats.current_magicka -= 20
                    UI.slow_print(f"You cast a Destruction spell on {target.name} for {spell_damage} damage!") #cite: 1
                    if not target.stats.is_alive():
                        UI.slow_print(f"You defeated {target.name}!") #cite: 1
                        return True
            else:
                UI.slow_print("Not enough magicka!") #cite: 1
        elif choice == "3": # Use Item
            if self.player.inventory:
                UI.slow_print("Your inventory:") #cite: 1
                usable_items = [item for item in self.player.inventory if item.category in ["potion", "food", "scroll"]]
                if not usable_items:
                    UI.slow_print("You have no usable items in your inventory.") #cite: 1
                    return True # Allow player to choose another action
                for i, item in enumerate(usable_items):
                    UI.slow_print(f"[{i+1}] {item.name} ({item.category})") #cite: 1
                item_choice = input("Which item do you want to use? (Enter number, 0 to cancel): ") #cite: 1
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(usable_items):
                        item_to_use = usable_items[item_index]
                        messages = self._handle_player_item_use(item_to_use)
                        for msg in messages:
                            UI.slow_print(msg) #cite: 1
                        # Re-check if target died if item was a damaging scroll
                        if item_to_use.category == "scroll" and "fireball" in item_to_use.name.lower():
                            self.enemies = [enemy for enemy in self.enemies if enemy.stats.is_alive()]
                            if not self.enemies:
                                UI.slow_print("You defeated all enemies with your scroll!") #cite: 1
                                return True
                    elif item_index == -1: # Cancel
                        UI.slow_print("Item usage cancelled.") #cite: 1
                        return True
                    else:
                        UI.slow_print("Invalid item choice.") #cite: 1
                except ValueError:
                    UI.slow_print("Invalid input.") #cite: 1
            else:
                UI.slow_print("Your inventory is empty.") #cite: 1
        elif choice == "4": # Block
            UI.slow_print("You ready your defenses, preparing to block incoming attacks.") #cite: 1
            self.player.is_blocking = True # Set a flag for the next enemy turn
        elif choice == "5": # Dodge
            UI.slow_print("You prepare to dodge, aiming to evade incoming attacks.") #cite: 1
            self.player.is_dodging = True # Set a flag for the next enemy turn
        elif choice == "6": # Flee
            UI.slow_print("You attempt to flee!") #cite: 1
            if random.random() < (0.5 + (self.player.stats.agility / 200)): # Agility improves flee chance
                UI.slow_print("You successfully fled from combat!") #cite: 1
                return False # Combat ends
            else:
                UI.slow_print("You failed to flee!") #cite: 1
        else:
            UI.slow_print("Invalid action.") #cite: 1
        return True # Continue combat

    def npc_turn(self, npc: NPC):
        """Handles an NPC's combat turn with more varied actions."""
        if not npc.stats.is_alive():
            return True # Skip if dead

        UI.slow_print(f"\n{npc.name}'s turn (Health: {npc.stats.current_health}/{npc.stats.max_health})") #cite: 1

        # Reset player's blocking/dodging flags for this turn
        self.player.is_blocking = False
        self.player.is_dodging = False

        # NPCs can have different behaviors based on their role or disposition
        npc_attitude = get_tags(npc).get("attitude", [])
        npc_class = get_tags(npc).get("class", [])

        if "hostile" in npc_attitude:
            # Hostile NPCs: Prioritize attack, then spell if mage, then flee if low health
            if npc.stats.current_health < npc.stats.max_health * 0.3 and random.random() < 0.4: # 40% chance to flee if low
                UI.slow_print(f"{npc.name} attempts to flee!") #cite: 1
                if random.random() < 0.6: # NPC flee chance
                    UI.slow_print(f"{npc.name} successfully fled!") #cite: 1
                    self.enemies.remove(npc) # Remove fleeing NPC
                    return True
                else:
                    UI.slow_print(f"{npc.name} failed to flee!") #cite: 1

            if "mage" in npc_class and npc.stats.current_magicka >= 15 and random.random() < 0.6: # Mages cast spells
                spell_damage = random.randint(10, 25)
                self.player.stats.current_health -= spell_damage
                npc.stats.current_magicka -= 15
                UI.slow_print(f"{npc.name} casts a spell on you for {spell_damage} damage!") #cite: 1
            else: # Default to attack
                damage = self._calculate_damage(npc, self.player)

                # Check if player blocked or dodged
                if hasattr(self.player, 'is_blocking') and self.player.is_blocking:
                    block_reduction = random.randint(damage // 2, damage) # Reduce damage by 50-100%
                    damage = max(0, damage - block_reduction)
                    UI.slow_print("You successfully blocked the attack!") #cite: 1
                elif hasattr(self.player, 'is_dodging') and self.player.is_dodging:
                    if random.random() < (self.player.stats.agility / 100): # Agility based dodge chance
                        UI.slow_print("You successfully dodged the attack!") #cite: 1
                        damage = 0 # No damage taken
                    else:
                        UI.slow_print("You failed to dodge the attack!") #cite: 1

                self.player.stats.current_health -= damage
                UI.slow_print(f"{npc.name} attacks you for {damage} damage!") #cite: 1

            if not self.player.stats.is_alive():
                UI.slow_print(f"You have been defeated by {npc.name}!") #cite: 1
                return False # Combat ends
        else:
            # Non-hostile NPCs might try to flee or do nothing
            UI.slow_print(f"{npc.name} seems confused and doesn't attack.") #cite: 1
        return True

    def run(self):
        """Runs the combat encounter until player or all enemies are defeated."""
        UI.slow_print(f"Entering combat at {self.location['name']}!") #cite: 1
        while self.player.stats.is_alive() and self.enemies:
            self.turn += 1
            UI.slow_print(f"\n--- Turn {self.turn} ---") #cite: 1

            # Apply status effects to player
            messages = self._apply_status_effects(self.player)
            for msg in messages:
                UI.slow_print(msg) #cite: 1

            # Apply status effects to enemies
            for enemy in self.enemies:
                messages = self._apply_status_effects(enemy)
                for msg in messages:
                    UI.slow_print(msg) #cite: 1

            # Player turn
            if not self.player.stats.is_alive(): # Check if player died from status effects
                UI.slow_print("You have been defeated by a lingering effect!") #cite: 1
                break
            if not self.player_turn():
                break # Combat ends if player fled

            # Check if any enemies died during player's turn
            self.enemies = [enemy for enemy in self.enemies if enemy.stats.is_alive()]
            if not self.enemies:
                UI.slow_print("You have defeated all your enemies!") #cite: 1
                break

            # Enemy turns
            # Iterate over a copy to allow removal during loop (e.g., if an NPC flees)
            for enemy in self.enemies[:]:
                if not self.npc_turn(enemy):
                    break # Combat ends if player was defeated by an NPC

            # Re-check if player died or enemies are all defeated after enemy turns
            if not self.player.stats.is_alive():
                UI.slow_print("You have been defeated!") #cite: 1
                break
            if not self.enemies:
                UI.slow_print("You have defeated all your enemies!") #cite: 1
                break

        # Cleanup after combat
        self.player.combat = None # Clear combat instance from player
        UI.slow_print("Combat ended.") #cite: 1

        # Post-combat rewards/drops
        if not self.player.stats.is_alive():
            UI.slow_print("You have fallen in battle...") #cite: 1
        else:
            UI.slow_print("\n--- Combat Rewards ---") #cite: 1
            gold_reward = random.randint(10 * self.player.level, 30 * self.player.level)
            self.player.stats.gold += gold_reward
            UI.slow_print(f"You gained {gold_reward} gold!") #cite: 1

            # Chance for item drops from defeated enemies
            for _ in range(random.randint(0, len(self.enemies))): # Up to one item per defeated enemy
                if random.random() < 0.4: # 40% chance for an item drop
                    # Assuming generate_random_item in items.py can take level
                    dropped_item = generate_random_item("misc", self.player.level) # Specify category as misc or based on enemy
                    if self.player.add_item(dropped_item):
                        UI.slow_print(f"You found: {dropped_item.name}!") #cite: 1
                    else:
                        UI.slow_print(f"You found {dropped_item.name}, but your inventory is full!") #cite: 1