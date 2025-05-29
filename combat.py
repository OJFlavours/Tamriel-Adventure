# combat.py

import random
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime

from ui import UI
from items import Item, generate_random_item
from player import Player
from npc import NPC, get_tags
from spells import Spell # Import Spell for type hinting and use

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
        self.enemies = [e for e in enemies if e.stats.is_alive()] 
        self.location = location
        self.allies: List[NPC] = [ally for ally in player.followers if ally.stats.is_alive()] 
        self.player_summons: List[NPC] = [] 
        self.turn = 0
        self.combat_log = []
        self.combo_counter = 0
        self.last_attack_time = datetime.utcnow()
        
        all_participants = [self.player] + self.enemies + self.allies + self.player_summons
        for char in all_participants:
            if not hasattr(char, 'status_effects'):
                char.status_effects = []
            if hasattr(char, 'summon_duration') and char.summon_duration is None and char in self.player_summons : 
                char.summon_duration = 3


    def _apply_status_effects(self, character) -> List[str]:
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

    def get_power_attack_cost(self) -> int:
        return 25

    def get_dodge_cost(self) -> int:
        return 20

    def apply_and_log_weapon_effects(self, attacker, defender, is_ranged: bool = False):
        if attacker.equipment:
            weapon_to_check = None
            if is_ranged:
                weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and item.equipment_tag == "ranged"), None)
            else:
                weapon_to_check = next((item for item in attacker.equipment if item.category == "weapon" and (item.equipment_tag == "main_hand" or item.equipment_tag == "two_handed")), None)
            
            if weapon_to_check:
                messages = self._apply_weapon_effects(attacker, defender, weapon_to_check)
                for msg in messages:
                    UI.slow_print(msg)

    def _is_ranged_attack(self, character) -> bool:
        if hasattr(character, 'equipment'):
            return any(item.category == "weapon" and item.equipment_tag == "ranged" for item in character.equipment)
        return False

    def _calculate_damage(self, attacker, defender, is_ranged: bool = False) -> int:
        if is_ranged:
            base_damage = attacker.stats.agility // 5 
            skill_modifier = attacker.skills.get("archery", 0) // 4 
        else:
            base_damage = attacker.stats.strength // 5 
            weapon_type = "two_handed" if self._is_two_handed_weapon(attacker) else "one_handed"
            skill_modifier = attacker.skills.get(weapon_type, 0) // 4 

        weapon_damage = self._get_weapon_damage(attacker) 
        total_damage = base_damage + weapon_damage + skill_modifier

        crit_chance = attacker.stats.luck // 2  
        if is_ranged:
            crit_chance += attacker.skills.get("archery", 0) // 4
        else:
            crit_chance += attacker.skills.get(weapon_type, 0) // 4
            
        if random.randint(1, 100) <= crit_chance:
            total_damage = int(total_damage * 1.5)
            UI.slow_print(f"{attacker.name} lands a critical hit!")

        if attacker == self.player and hasattr(self, 'combo_counter') and self.combo_counter > 0 and not self.player.is_power_attacking: 
            combo_bonus = min(self.combo_counter * 0.1, 0.5)  
            total_damage = int(total_damage * (1 + combo_bonus))
            UI.slow_print(f"Combo x{self.combo_counter}! ({int(combo_bonus*100)}% bonus damage)")

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
            UI.slow_print(f"{defender.name} blocks, reducing damage by {damage_reduction_from_block} ({int(block_effectiveness_percent*100)}%)!")
            
            if hasattr(defender, 'improve_skill'): 
                defender.improve_skill("block", 1)
            
            if hasattr(defender.stats, 'current_fatigue'): 
                block_stamina_cost = 5 
                defender.stats.current_fatigue = max(0, defender.stats.current_fatigue - block_stamina_cost)

        final_damage = max(0, total_damage - armor_reduction)

        if self._has_elemental_weapon(attacker, "fire"):
            final_damage *= (100 - defender.stats.fire_resist) / 100
        if self._has_elemental_weapon(attacker, "frost"):
            final_damage *= (100 - defender.stats.frost_resist) / 100
        if self._has_elemental_weapon(attacker, "shock"):
            final_damage *= (100 - defender.stats.shock_resist) / 100

        return int(final_damage)

    def _get_weapon_damage(self, character) -> int:
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
        if not hasattr(character, 'equipment'):
            return False
        return any(item.category == "weapon" and 
                  hasattr(item, 'equipment_tag') and 
                  item.equipment_tag == "two_handed" 
                  for item in character.equipment)

    def _has_elemental_weapon(self, character, element_type: str) -> bool:
        if not hasattr(character, 'equipment'):
            return False
        return any(item.category == "weapon" and 
                  hasattr(item, 'enchantment') and 
                  element_type in item.enchantment.lower() 
                  for item in character.equipment)

    def _get_target(self, attacker, target_list: List) -> Optional[object]:
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
        else: # NPC targeting
            if self.player.stats.is_alive():
                return self.player
            living_allies = [ally for ally in self.allies if ally.stats.is_alive()]
            if living_allies:
                return random.choice(living_allies)
            living_summons = [summon for summon in self.player_summons if summon.stats.is_alive()]
            if living_summons:
                return random.choice(living_summons)
            return None 

    def _handle_counter_attack(self, defender, attacker):
        if hasattr(defender, 'is_blocking') and defender.is_blocking:
            block_skill = defender.skills.get("block", 0)
            counter_chance = block_skill / 200  
            
            if random.random() < counter_chance:
                UI.slow_print(f"{defender.name} performs a perfect block and counter-attacks!")
                counter_damage = self._calculate_damage(defender, attacker) // 2
                attacker.stats.current_health -= counter_damage
                UI.slow_print(f"Counter-attack deals {counter_damage} damage!")
                
                if defender == self.player:
                    defender.improve_skill("block", 1)

    def _apply_weapon_effects(self, attacker, defender, weapon: Optional[Item]) -> List[str]:
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
                defender.status_effects.append(effect)
                messages.extend(effect.apply(defender))
                
        return messages

    def player_turn(self) -> bool: # Return type can be bool or str ("REPROMPT_PLAYER_ACTION")
        UI.print_subheading(f"{self.player.full_name}'s Turn")
        UI.print_info(f"Health: {self.player.stats.current_health}/{self.player.stats.max_health}")
        UI.print_info(f"Magicka: {self.player.stats.current_magicka}/{self.player.stats.max_magicka}")
        UI.print_info(f"Stamina: {self.player.stats.current_fatigue}/{self.player.stats.max_fatigue}")
        
        UI.print_info("\nEnemies:")
        for i, enemy in enumerate(self.enemies, 1):
            UI.print_info(f"[{i}] {enemy.name} (Health: {enemy.stats.current_health}/{enemy.stats.max_health})")

        options = []
        current_key = 1

        options.append({"key": str(current_key), "text": "Melee Attack"})
        current_key += 1

        if any(item.category == "weapon" and item.equipment_tag == "ranged" for item in self.player.equipment):
            options.append({"key": str(current_key), "text": "Ranged Attack"})
            current_key += 1
        
        options.append({"key": str(current_key), "text": f"Power Attack (Cost: {self.get_power_attack_cost()} Stamina)"})
        current_key += 1
        
        options.append({"key": str(current_key), "text": "Cast Spell"})
        current_key += 1

        options.append({"key": str(current_key), "text": "Use Item"})
        current_key += 1

        options.append({"key": str(current_key), "text": "Block"})
        current_key += 1
        
        options.append({"key": str(current_key), "text": f"Dodge (Cost: {self.get_dodge_cost()} Stamina)"})
        current_key += 1

        options.append({"key": str(current_key), "text": "Flee"})
        
        UI.print_line()
        UI.slow_print(" ".join([f"[{opt['key']}] {opt['text']}" for opt in options]))
        choice = input("Your action? ")

        self.player.is_power_attacking = False 

        chosen_action_text = ""
        for opt in options:
            if opt["key"] == choice:
                chosen_action_text = opt["text"].split(" (")[0] 
                break
        
        if chosen_action_text == "Melee Attack":
            self.player.is_blocking = False # Attacking overrides blocking for the turn
            self.player.is_dodging = False # Attacking overrides dodging
            target = self._get_target(self.player, self.enemies)
            if target:
                damage = self._calculate_damage(self.player, target)
                target.stats.take_damage(damage)
                UI.slow_print(f"You attack {target.name} for {damage} damage!")
                self.apply_and_log_weapon_effects(self.player, target)
                self.combo_counter += 1
                if not target.stats.is_alive():
                    UI.slow_print(f"You defeated {target.name}!")
                return True # Turn consumed
            else: return "REPROMPT_PLAYER_ACTION" 

        elif chosen_action_text == "Ranged Attack":
            self.player.is_blocking = False
            self.player.is_dodging = False
            target = self._get_target(self.player, self.enemies)
            if target:
                damage = self._calculate_damage(self.player, target, is_ranged=True)
                target.stats.take_damage(damage)
                UI.slow_print(f"You shoot {target.name} for {damage} damage!")
                self.apply_and_log_weapon_effects(self.player, target, is_ranged=True)
                self.combo_counter = 0
                if not target.stats.is_alive():
                    UI.slow_print(f"You defeated {target.name}!")
                return True
            else: return "REPROMPT_PLAYER_ACTION"

        elif chosen_action_text == "Power Attack":
            self.player.is_blocking = False
            self.player.is_dodging = False
            power_attack_cost = self.get_power_attack_cost()
            if self.player.stats.current_fatigue >= power_attack_cost:
                target = self._get_target(self.player, self.enemies)
                if target:
                    self.player.stats.current_fatigue -= power_attack_cost
                    self.player.is_power_attacking = True
                    damage = self._calculate_damage(self.player, target)
                    damage = int(damage * 1.75)
                    target.stats.take_damage(damage) 
                    UI.slow_print(f"You unleash a Power Attack on {target.name} for {damage} damage!")
                    self.apply_and_log_weapon_effects(self.player, target)
                    self.combo_counter = 0
                    if not target.stats.is_alive():
                        UI.slow_print(f"You defeated {target.name}!")
                    return True
                else: return "REPROMPT_PLAYER_ACTION" 
            else:
                UI.slow_print(f"Not enough stamina for a power attack (Need {power_attack_cost}, Have {self.player.stats.current_fatigue}).")
                UI.press_enter()
                return "REPROMPT_PLAYER_ACTION"


        elif chosen_action_text == "Cast Spell":
            self.player.is_blocking = False
            self.player.is_dodging = False
            if not self.player.known_spells:
                UI.slow_print("You know no spells to cast.")
                UI.press_enter()
                return "REPROMPT_PLAYER_ACTION"

            UI.print_subheading("Known Spells:")
            castable_spells_map = {} 
            display_index = 1
            for spell_obj in self.player.known_spells:
                cost_indicator = ""
                can_cast = self.player.stats.current_magicka >= spell_obj.cost
                if not can_cast:
                    cost_indicator = " (Too Costly)"
                
                if can_cast:
                    castable_spells_map[str(display_index)] = spell_obj
                
                UI.print_info(f"[{display_index}] {spell_obj}{cost_indicator}")
                display_index +=1
            
            if not castable_spells_map: 
                UI.slow_print("Not enough Magicka to cast any of your known spells.")
                UI.press_enter() 
                return "REPROMPT_PLAYER_ACTION"

            spell_choice_input = UI.print_prompt("Choose spell to cast (0 to cancel): ")
            if not spell_choice_input.isdigit():
                UI.slow_print("Invalid input.")
                UI.press_enter()
                return "REPROMPT_PLAYER_ACTION"
            
            spell_choice_key = spell_choice_input
            if spell_choice_key == "0":
                return "REPROMPT_PLAYER_ACTION"

            if spell_choice_key in castable_spells_map:
                selected_spell = castable_spells_map[spell_choice_key]
                
                target = None
                if selected_spell.effect_properties.get("target_self"):
                    target = self.player 
                else:
                    target = self._get_target(self.player, self.enemies) 
                
                if target: 
                    self.player.stats.current_magicka -= selected_spell.cost
                    UI.slow_print(f"You cast {selected_spell.name}!") 
                    
                    if selected_spell.effect_properties.get("target_self"):
                        if selected_spell.damage_type == "healing":
                             heal_amount = random.randint(selected_spell.base_damage_min, selected_spell.base_damage_max)
                             self.player.stats.current_health = min(self.player.stats.max_health, self.player.stats.current_health + heal_amount)
                             UI.slow_print(f"You heal yourself for {heal_amount} health!")
                        if selected_spell.effect_properties.get("armor_bonus"):
                            UI.slow_print(f"Your skin hardens like oak! (Armor +{selected_spell.effect_properties['armor_bonus']})")
                            # TODO: Implement temporary status effect for armor bonus
                    elif selected_spell.damage_type and selected_spell.damage_type != "healing": 
                        UI.slow_print(f"You cast {selected_spell.name} on {target.name}!") 
                        spell_damage = random.randint(selected_spell.base_damage_min, selected_spell.base_damage_max)
                        skill_level = self.player.skills.get(selected_spell.school.lower(), 0)
                        skill_bonus = skill_level // 3 
                        spell_damage += skill_bonus
                        
                        if selected_spell.damage_type == "fire":
                            spell_damage = int(spell_damage * (1 - target.stats.fire_resist / 100))
                        elif selected_spell.damage_type == "frost":
                             spell_damage = int(spell_damage * (1 - target.stats.frost_resist / 100))
                        elif selected_spell.damage_type == "shock":
                            spell_damage = int(spell_damage * (1 - target.stats.shock_resist / 100))
                            magicka_dmg = int(spell_damage * selected_spell.effect_properties.get("magicka_damage_ratio", 0))
                            if magicka_dmg > 0:
                                target.stats.current_magicka = max(0, target.stats.current_magicka - magicka_dmg)
                                UI.slow_print(f"The shock also drains {magicka_dmg} of {target.name}'s Magicka!")


                        target.stats.take_damage(spell_damage) 
                        UI.slow_print(f"{selected_spell.name} deals {spell_damage} {selected_spell.damage_type} damage!")
                    
                    if selected_spell.effect_properties and "summon_key" in selected_spell.effect_properties:
                        summon_key = selected_spell.effect_properties["summon_key"]
                        if summon_key == "spectral_wolf":
                            summon_level = self.player.level // 2 + 1
                            summoned_creature = NPC(name="Spectral Wolf", race="spirit_wolf", 
                                                    role="spectral_ally", level=summon_level)
                            summoned_creature.summon_duration = selected_spell.duration 
                            self.player_summons.append(summoned_creature)
                            UI.slow_print(f"A {summoned_creature.name} appears to aid you!")
                    
                    self.player.improve_skill(selected_spell.school.lower(), 1)
                    self.combo_counter = 0
                    if target and target != self.player and not target.stats.is_alive(): 
                        UI.slow_print(f"You defeated {target.name} with {selected_spell.name}!")
                    return True # Spell casting consumes the turn
                else: 
                    return "REPROMPT_PLAYER_ACTION" # Target selection cancelled
            else:
                UI.slow_print("Invalid spell choice.")
                UI.press_enter()
                return "REPROMPT_PLAYER_ACTION"


        elif chosen_action_text == "Use Item":
            self.player.is_blocking = False
            self.player.is_dodging = False
            if self.player.inventory:
                UI.print_subheading("Your inventory:")
                usable_items = [item for item in self.player.inventory 
                              if item.category in ["potion", "food", "scroll"]]
                
                if not usable_items:
                    UI.slow_print("You have no usable items.")
                    UI.press_enter()
                    return "REPROMPT_PLAYER_ACTION"
                    
                for i, item in enumerate(usable_items, 1):
                    UI.print_info(f"[{i}] {item.name} ({item.category})")
                    
                try:
                    item_choice_str = input("Use which item? (0 to cancel): ")
                    if not item_choice_str.isdigit():
                        UI.slow_print("Invalid input.")
                        UI.press_enter()
                        return "REPROMPT_PLAYER_ACTION"
                    item_choice = int(item_choice_str)
                    
                    if item_choice == 0:
                        return "REPROMPT_PLAYER_ACTION"
                        
                    if 1 <= item_choice <= len(usable_items):
                        item = usable_items[item_choice - 1]
                        if hasattr(item, 'use'):
                            item.use(self.player) 
                            return True # Using an item consumes the turn
                        else:
                            UI.slow_print(f"Cannot use {item.name} right now.")
                            return "REPROMPT_PLAYER_ACTION" 
                    else:
                        UI.slow_print("Invalid item number.")
                        UI.press_enter()
                        return "REPROMPT_PLAYER_ACTION"
                except ValueError: 
                    UI.slow_print("Please enter a number.")
                    UI.press_enter()
                    return "REPROMPT_PLAYER_ACTION"
            else:
                UI.slow_print("Your inventory is empty.")
                UI.press_enter()
                return "REPROMPT_PLAYER_ACTION"

        elif chosen_action_text == "Block":
            UI.slow_print("You raise your defenses, ready to block the next melee attack!")
            self.player.is_blocking = True
            self.player.is_dodging = False 
            self.combo_counter = 0
            return True # Blocking now consumes the turn


        elif chosen_action_text == "Dodge":
            dodge_cost = self.get_dodge_cost()
            if self.player.stats.current_fatigue >= dodge_cost:
                self.player.stats.current_fatigue -= dodge_cost
                UI.slow_print(f"You spend {dodge_cost} stamina preparing to dodge!")
                self.player.is_dodging = True
                self.player.is_blocking = False 
                self.combo_counter = 0
                return True # Dodging now consumes the turn
            else:
                UI.slow_print(f"Not enough stamina to dodge (Need {dodge_cost}, Have {self.player.stats.current_fatigue}).")
                UI.press_enter()
                return "REPROMPT_PLAYER_ACTION" 


        elif chosen_action_text == "Flee":
            self.player.is_blocking = False
            self.player.is_dodging = False
            UI.slow_print("You attempt to flee!")
            flee_chance = 0.5 + (self.player.stats.agility / 200)  
            if random.random() < flee_chance:
                UI.slow_print("You successfully fled from combat!")
                return False 
            else:
                UI.slow_print("You failed to flee!")
                self.combo_counter = 0  
                return True 

        else:
            UI.slow_print("Invalid action.")
            return "REPROMPT_PLAYER_ACTION" 
            
        return True 

    def npc_turn(self, npc: NPC) -> bool:
        if not npc.stats.is_alive():
            return True

        UI.print_subheading(f"{npc.name}'s Turn")
        UI.print_info(f"Health: {npc.stats.current_health}/{npc.stats.max_health} | Magicka: {npc.stats.current_magicka}/{npc.stats.max_magicka}")
        
        npc_tags_category = npc.tags.get("npc", {})
        npc_attitude_value = npc_tags_category.get("attitude", "neutral") 
        npc_class_value = npc_tags_category.get("role_primary", "") 

        if npc_attitude_value == "hostile":
            if npc.stats.current_health < npc.stats.max_health * 0.3 and random.random() < 0.4:
                UI.slow_print(f"{npc.name} attempts to flee!")
                if random.random() < 0.6:
                    UI.slow_print(f"{npc.name} successfully fled!")
                    self.enemies.remove(npc)
                    return True # NPC fled, turn ends for this NPC
                else:
                    UI.slow_print(f"{npc.name} failed to flee!")

            chosen_npc_action = "attack" 
            damage = 0 
            archetype = npc.combat_archetype if hasattr(npc, 'combat_archetype') else "StandardMelee"
            
            can_cast_spell = False
            castable_npc_spells = []
            if hasattr(npc, 'known_spells') and npc.known_spells:
                castable_npc_spells = [sp for sp in npc.known_spells if npc.stats.current_magicka >= sp.cost]
                if castable_npc_spells:
                    can_cast_spell = True

            selected_npc_spell = None 
            if archetype == "CautiousMage" and can_cast_spell and random.random() < 0.75: 
                chosen_npc_action = "spell"
                selected_npc_spell = random.choice(castable_npc_spells)
            elif archetype == "SupportPriest" and can_cast_spell and random.random() < 0.7:
                healing_spells = [s for s in castable_npc_spells if s.damage_type == "healing" and s.effect_properties.get("target_self")]
                if healing_spells and npc.stats.current_health < npc.stats.max_health * 0.6:
                    selected_npc_spell = random.choice(healing_spells)
                    chosen_npc_action = "spell"
                elif castable_npc_spells: 
                    selected_npc_spell = random.choice(castable_npc_spells)
                    chosen_npc_action = "spell"
            elif archetype == "AggressiveWarrior" and npc.stats.current_fatigue >= 15 and random.random() < 0.35: 
                chosen_npc_action = "power_attack"
            elif archetype == "SkirmisherArcher":
                if self._is_ranged_attack(npc) and random.random() < 0.8: 
                    chosen_npc_action = "ranged_attack" 
                elif random.random() < 0.2 and npc.stats.current_health < npc.stats.max_health * 0.4: 
                    UI.slow_print(f"{npc.name} tries to disengage!")
                    if random.random() < 0.5: 
                        UI.slow_print(f"{npc.name} creates some distance!")
                        return True 
                    else:
                        UI.slow_print(f"{npc.name} fails to disengage!")
                        chosen_npc_action = "attack" # Fallback if disengage fails
            elif archetype == "AggressiveCreature": # Ensure creatures attack
                chosen_npc_action = "attack"
            elif archetype == "StandardMelee" and npc.stats.current_fatigue >= 15 and random.random() < 0.20:
                chosen_npc_action = "power_attack"
            
            if chosen_npc_action == "attack" and archetype == "AggressiveSummon" and can_cast_spell and random.random() < 0.5:
                 chosen_npc_action = "spell"
                 if castable_npc_spells : selected_npc_spell = random.choice(castable_npc_spells)


            if chosen_npc_action == "spell":
                if not selected_npc_spell and castable_npc_spells: 
                    selected_npc_spell = random.choice(castable_npc_spells)

                if not selected_npc_spell: 
                    UI.slow_print(f"{npc.name} tries to cast a spell but fizzles...")
                    chosen_npc_action = "attack" # Fallback to attack if spell selection failed
                    damage = self._calculate_damage(npc, self.player) # Recalculate damage for attack
                else:
                    npc.stats.current_magicka -= selected_npc_spell.cost
                    UI.slow_print(f"{npc.name} casts {selected_npc_spell.name}!")
                    
                    target_for_spell = self._get_target(npc, [self.player] + self.allies + self.player_summons) 
                    if not target_for_spell: target_for_spell = self.player 

                    if selected_npc_spell.effect_properties.get("target_self"):
                        target_for_spell = npc 
                        if selected_npc_spell.damage_type == "healing":
                             heal_amount = random.randint(selected_npc_spell.base_damage_min, selected_npc_spell.base_damage_max)
                             npc.stats.current_health = min(npc.stats.max_health, npc.stats.current_health + heal_amount)
                             UI.slow_print(f"{npc.name} heals for {heal_amount} health!")
                        if selected_npc_spell.effect_properties.get("armor_bonus"):
                            UI.slow_print(f"{npc.name} bolsters their defenses!")
                    elif selected_npc_spell.damage_type and selected_npc_spell.damage_type != "healing": 
                        spell_damage = random.randint(selected_npc_spell.base_damage_min, selected_npc_spell.base_damage_max)
                        skill_bonus = npc.skills.get(selected_npc_spell.school.lower(), 0) // 3 
                        spell_damage += skill_bonus
                        
                        if selected_npc_spell.damage_type == "fire": spell_damage = int(spell_damage * (1 - target_for_spell.stats.fire_resist / 100))
                        elif selected_npc_spell.damage_type == "frost": spell_damage = int(spell_damage * (1 - target_for_spell.stats.frost_resist / 100))
                        elif selected_npc_spell.damage_type == "shock": 
                            spell_damage = int(spell_damage * (1 - target_for_spell.stats.shock_resist / 100))
                            magicka_dmg = int(spell_damage * selected_npc_spell.effect_properties.get("magicka_damage_ratio", 0))
                            if magicka_dmg > 0:
                                target_for_spell.stats.current_magicka = max(0, target_for_spell.stats.current_magicka - magicka_dmg)
                                UI.slow_print(f"The shock also drains {magicka_dmg} of {target_for_spell.name}'s Magicka!")
                        
                        dodged_spell = False
                        if target_for_spell == self.player and self.player.is_dodging:
                            player_dodge_score = self.player.stats.agility + self.player.skills.get("light_armor", 0) * 0.5 
                            npc_attack_score = npc.stats.intelligence + npc.skills.get(selected_npc_spell.school.lower(),0) * 0.5
                            dodge_chance = 0.15 + (player_dodge_score - npc_attack_score) / 150.0 
                            dodge_chance = max(0.01, min(dodge_chance, 0.50))
                            if random.random() < dodge_chance:
                                UI.slow_print(f"You manage to sidestep {npc.name}'s {selected_npc_spell.name}!")
                                dodged_spell = True
                            else:
                                UI.slow_print(f"You try to avoid the {selected_npc_spell.name}, but it hits!")
                            self.player.is_dodging = False 

                        if not dodged_spell:
                            target_for_spell.stats.take_damage(spell_damage)
                            UI.slow_print(f"{selected_npc_spell.name} hits {target_for_spell.name} for {spell_damage} {selected_npc_spell.damage_type} damage!")
            
            if chosen_npc_action == "power_attack": # Ensure damage is set for power attack if spell failed
                npc.stats.current_fatigue -= 15 
                damage = self._calculate_damage(npc, self.player) 
                damage = int(damage * 1.6) 
                UI.slow_print(f"{npc.name} unleashes a powerful attack!")
            
            elif chosen_npc_action == "ranged_attack": 
                damage = self._calculate_damage(npc, self.player, is_ranged=True)
                UI.slow_print(f"{npc.name} fires at you!")

            elif chosen_npc_action == "attack": # Default or fallback from failed spell
                damage = self._calculate_damage(npc, self.player)
            
            if chosen_npc_action in ["attack", "power_attack", "ranged_attack"]:
                dodged_this_attack = False
                is_npc_ranged_attack = (chosen_npc_action == "ranged_attack") or self._is_ranged_attack(npc)

                if self.player.is_dodging: 
                    player_dodge_score = self.player.stats.agility + self.player.skills.get("light_armor", 0) * 0.75
                    npc_attack_score = npc.stats.agility + npc.skills.get("one_handed" if not is_npc_ranged_attack else "archery", 0) * 0.5
                    dodge_chance = 0.3 + (player_dodge_score - npc_attack_score) / 100.0
                    dodge_chance = max(0.05, min(dodge_chance, 0.75)) 

                    if random.random() < dodge_chance:
                        UI.slow_print(f"You deftly dodge {npc.name}'s attack!")
                        damage = 0 
                        dodged_this_attack = True
                        self.player.improve_skill("light_armor", 1) 
                    else:
                        UI.slow_print(f"You attempt to dodge but {npc.name}'s attack connects!")
                    self.player.is_dodging = False 

                if not dodged_this_attack:
                    if self.player.is_blocking and is_npc_ranged_attack: 
                         UI.slow_print(f"Your block is ineffective against {npc.name}'s ranged attack!")
                    
                    if damage > 0 : 
                        self.player.stats.take_damage(damage) 
                        UI.slow_print(f"{npc.name} hits you for {damage} damage!")
                    elif not dodged_this_attack and self.player.is_blocking and not is_npc_ranged_attack: 
                        pass 
                    elif not dodged_this_attack: 
                         UI.slow_print(f"{npc.name}'s attack glances off harmlessly!")
                
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
        UI.print_heading(f"Combat at {self.location['name']}")
        player_action_result = True # Initialize to True, will be False if player flees

        while self.player.stats.is_alive() and self.enemies:
            self.turn += 1
            UI.print_heading(f"Turn {self.turn}")

            all_combatants = [self.player] + self.allies + self.player_summons + self.enemies
            for combatant in all_combatants:
                if combatant.stats.is_alive(): 
                    messages = self._apply_status_effects(combatant)
                    for msg in messages:
                        UI.slow_print(msg)
            
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            self.allies = [a for a in self.allies if a.stats.is_alive()]
            self.player_summons = [s for s in self.player_summons if s.stats.is_alive()]

            if not self.player.stats.is_alive():
                UI.slow_print("You succumbed to your wounds!")
                break
            if not self.enemies:
                UI.slow_print("All enemies have been defeated!")
                break

            # --- Player's Turn ---
            self.player.is_blocking = False 
            # self.player.is_dodging is reset after each dodge attempt.

            player_action_result = self.player_turn() 
            while player_action_result == "REPROMPT_PLAYER_ACTION":
                player_action_result = self.player_turn()

            if player_action_result is False: # Player Fled
                break 
            
            self.enemies = [e for e in self.enemies if e.stats.is_alive()]
            if not self.enemies:
                break
            
            # --- Allies' (Followers & Summons) Turn ---
            current_allies_in_combat = self.allies + self.player_summons
            if current_allies_in_combat:
                UI.print_subheading("Allies' Turn:")
                for ally_npc in current_allies_in_combat[:]: 
                    if not ally_npc.stats.is_alive():
                        if ally_npc in self.allies: 
                            UI.slow_print(f"{ally_npc.name} has fallen!")
                            self.allies.remove(ally_npc)
                        elif ally_npc in self.player_summons:
                             self.player_summons.remove(ally_npc) 
                        continue
                    
                    if hasattr(ally_npc, 'summon_duration'):
                        ally_npc.summon_duration -= 1
                        if ally_npc.summon_duration <= 0:
                            UI.slow_print(f"{ally_npc.name} (Summon) vanishes as its energy fades.")
                            if ally_npc in self.player_summons: self.player_summons.remove(ally_npc)
                            if ally_npc in self.allies: self.allies.remove(ally_npc) 
                            continue
                    
                    if self.enemies:
                        target_enemy = self._get_target(ally_npc, self.enemies) # Allies target enemies
                        if target_enemy:
                            ally_damage = self._calculate_damage(ally_npc, target_enemy)
                            target_enemy.stats.take_damage(ally_damage)
                            UI.slow_print(f"{ally_npc.name} attacks {target_enemy.name} for {ally_damage} damage!")
                            if not target_enemy.stats.is_alive():
                                UI.slow_print(f"{target_enemy.name} was defeated by {ally_npc.name}!")
                                self.enemies = [e for e in self.enemies if e.stats.is_alive()]
                                if not self.enemies:
                                    UI.slow_print("All enemies have been defeated by your allies!")
                                    break 
                        else: 
                            UI.slow_print(f"{ally_npc.name} looks for a target but finds none.")
                    else:
                        UI.slow_print(f"{ally_npc.name} stands ready, but all foes are vanquished.")
                        break 
            
            if not self.enemies: 
                break

            # --- Enemy Turns ---
            for enemy_npc in self.enemies[:]:  
                if not enemy_npc.stats.is_alive(): continue 
                if not self.player.stats.is_alive(): break 
                
                if not self.npc_turn(enemy_npc): # npc_turn returns False if player defeated
                    break 
            
            if not self.player.stats.is_alive(): 
                break

        self.player.combat = None
        UI.print_heading("Combat Ended")

        if self.player.stats.is_alive() and player_action_result is True: 
            self._handle_combat_rewards()
        elif player_action_result is False: 
            UI.slow_print("You receive no rewards for fleeing.")


    def _handle_combat_rewards(self):
        UI.print_heading("Combat Rewards")
        
        # Ensure we only consider enemies that were part of the combat and are now dead
        # The self.enemies list might have had NPCs flee, so we use the initial list passed to __init__
        # and check their current status. This is a bit complex if enemies can flee and then re-engage.
        # For simplicity, we'll base rewards on enemies that are currently in self.enemies and are dead.
        # This means if an enemy fled, they are not in self.enemies for reward calculation.
        defeated_enemies_for_reward = [e for e in self.enemies if not e.stats.is_alive()]

        base_gold = sum(enemy.level * 10 for enemy in defeated_enemies_for_reward) 
        luck_bonus = self.player.stats.luck / 100
        total_gold = int(base_gold * (1 + luck_bonus))
        
        if total_gold > 0:
            self.player.stats.gold += total_gold
            UI.slow_print(f"You found {total_gold} gold!")
        
        for enemy in defeated_enemies_for_reward: 
            for item in enemy.equipment:
                if random.random() < 0.4:  
                    if self.player.add_item(item):
                        UI.slow_print(f"You loot {item.name} from {enemy.name}")
                    else:
                        UI.slow_print(f"You found {item.name}, but your inventory is full!")
            
            for item in enemy.stats.inventory:
                if random.random() < 0.3:  
                    if self.player.add_item(item):
                        UI.slow_print(f"You loot {item.name} from {enemy.name}")
            
            if random.random() < 0.4:
                dropped_item = generate_random_item("misc", self.player.level)
                if self.player.add_item(dropped_item):
                    UI.slow_print(f"You found: {dropped_item.name}!")