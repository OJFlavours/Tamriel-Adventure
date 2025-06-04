# combat_player_actions.py
import random
from typing import TYPE_CHECKING, List, Dict

from ui import UI
from spells import Spell
from combat_targeting import get_target_logic
from combat_logic import calculate_damage_logic, apply_and_log_weapon_effects_logic
from status_effects import StatusEffect  # Import StatusEffect

if TYPE_CHECKING:
    from player import Player
    from npc import NPC
    from combat import Combat # To avoid circular import, only for type hinting

def handle_player_turn(combat_instance: 'Combat') -> bool: # Return type can be bool or str ("REPROMPT_PLAYER_ACTION")
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI # Assuming UI is a class with static methods or a global instance

    ui_instance.print_subheading(f"{player.full_name}'s Turn")
    ui_instance.print_info(f"Health: {player.stats.current_health}/{player.stats.max_health}")
    ui_instance.print_info(f"Magicka: {player.stats.current_magicka}/{player.stats.max_magicka}")
    ui_instance.print_info(f"Stamina: {player.stats.current_fatigue}/{player.stats.max_fatigue}")

    ui_instance.print_info("\nEnemies:")
    for i, enemy in enumerate(enemies, 1):
        ui_instance.print_info(f"[{i}] {enemy.name} (Health: {enemy.stats.current_health}/{enemy.stats.max_health})")

    options = []
    current_key = 1

    options.append({"key": str(current_key), "text": "Melee Attack"})
    current_key += 1

    if any(item.category == "weapon" and item.equipment_tag == "ranged" for item in player.equipment):
        options.append({"key": str(current_key), "text": "Ranged Attack"})
    current_key += 1

    options.append({"key": str(current_key), "text": f"Power Attack (Cost: {combat_instance.get_power_attack_cost()} Stamina)"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Cast Spell"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Use Combo"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Use Item"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Block"})
    current_key += 1

    options.append({"key": str(current_key), "text": f"Dodge (Cost: {combat_instance.get_dodge_cost()} Stamina)"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Flee"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Taunt"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Observe"})
    current_key += 1

    options.append({"key": str(current_key), "text": "Wait"})
    current_key += 1

    # Dynamic Actions
    if "berserk" in [effect.name.lower() for effect in player.status_effects]:
        options.append({"key": str(current_key), "text": "Rage Attack"})
        current_key += 1

    if player.skills.get("alchemy", 0):
        options.append({"key": str(current_key), "text": "Brew Potion"})
    current_key += 1

    ui_instance.print_line()
    ui_instance.slow_print(" ".join([f"[{opt['key']}] {opt['text']}" for opt in options]))
    choice = input("Your action? ")

    player.is_power_attacking = False
    player.is_blocking = False
    player.is_dodging = False

    chosen_action_text = ""
    for opt in options:
        if opt["key"] == choice:
            chosen_action_text = opt["text"].split(" (")[0]
            break

    action_map: Dict[str, callable] = {
        "Melee Attack": handle_melee_attack,
        "Ranged Attack": handle_ranged_attack,
        "Power Attack": handle_power_attack,
        "Cast Spell": handle_cast_spell,
        "Use Item": handle_use_item,
        "Block": handle_block,
        "Dodge": handle_dodge,
        "Flee": handle_flee,
        "Taunt": handle_taunt,
        "Observe": handle_observe,
        "Wait": handle_wait,
        "Use Combo": handle_use_combo,
        "Rage Attack": handle_rage_attack,
        "Brew Potion": handle_brew_potion,
    }

    if chosen_action_text in action_map:
        try:
            return action_map[chosen_action_text](combat_instance)
        except Exception as e:
            ui_instance.slow_print(f"An error occurred during {chosen_action_text}: {e}")
            return "REPROMPT_PLAYER_ACTION"
    else:
        ui_instance.slow_print("Invalid action.")
        return "REPROMPT_PLAYER_ACTION"

def handle_melee_attack(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI
    try:
        target_info = get_target_logic(player, enemies, ui_instance, player, combat_instance.allies, combat_instance.player_summons)
        if target_info:
            target, body_part = target_info
            damage = calculate_damage_logic(player, target, ui_instance, combat_instance.combo_counter, player.is_power_attacking, body_part=body_part)
            target.stats.take_damage(damage)
            ui_instance.slow_print(f"You attack {target.name} for {damage} damage!")
            apply_and_log_weapon_effects_logic(player, target, ui_instance)
            combat_instance.combo_counter += 1
            if not target.stats.is_alive():
                ui_instance.slow_print(f"You defeated {target.name}!")
            return True
        else:
            return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during melee attack: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_ranged_attack(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI
    try:
        target_info = get_target_logic(player, enemies, ui_instance, player, combat_instance.allies, combat_instance.player_summons)
        if target_info:
            target, body_part = target_info
            damage = calculate_damage_logic(player, target, ui_instance, combat_instance.combo_counter, player.is_power_attacking, is_ranged=True, body_part=body_part)
            target.stats.take_damage(damage)
            ui_instance.slow_print(f"You shoot {target.name} for {damage} damage!")
            apply_and_log_weapon_effects_logic(player, target, ui_instance, is_ranged=True)
            combat_instance.combo_counter = 0
            if not target.stats.is_alive():
                ui_instance.slow_print(f"You defeated {target.name}!")
                return True
        else:
            return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during ranged attack: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_power_attack(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI
    try:
        power_attack_cost = combat_instance.get_power_attack_cost()
        if player.stats.current_fatigue >= power_attack_cost:
            target = get_target_logic(player, enemies, ui_instance, player, combat_instance.allies, combat_instance.player_summons)
            if target:
                player.stats.current_fatigue -= power_attack_cost
                player.is_power_attacking = True
                damage = calculate_damage_logic(player, target, ui_instance, combat_instance.combo_counter, player.is_power_attacking)
                damage = int(damage * 1.5)
                target.stats.take_damage(damage)
                ui_instance.slow_print(f"You unleash a Power Attack on {target.name} for {damage} damage!")
                apply_and_log_weapon_effects_logic(player, target, ui_instance)
                combat_instance.combo_counter = 0
                if not target.stats.is_alive():
                    ui_instance.slow_print(f"You defeated {target.name}!")
                return True
            else:
                return "REPROMPT_PLAYER_ACTION"
        else:
            ui_instance.slow_print(f"Not enough stamina for a power attack (Need {power_attack_cost}, Have {player.stats.current_fatigue}).")
            ui_instance.press_enter()
            return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during power attack: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_cast_spell(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI
    try:
        if not player.known_spells:
            ui_instance.slow_print("You know no spells to cast.")
            ui_instance.press_enter()
            return "REPROMPT_PLAYER_ACTION"

        ui_instance.print_subheading("Known Spells:")
        castable_spells_map = {}
        display_index = 1
        for spell_obj in player.known_spells: # type: Spell
            cost_indicator = ""
            can_cast = player.stats.current_magicka >= spell_obj.cost
            if not can_cast:
                cost_indicator = " (Too Costly)"
            if can_cast:
                castable_spells_map[str(display_index)] = spell_obj
            ui_instance.print_info(f"[{display_index}] {spell_obj}{cost_indicator}")
            display_index +=1

        if not castable_spells_map:
            ui_instance.slow_print("Not enough Magicka to cast any of your known spells.")
            ui_instance.press_enter()
            return "REPROMPT_PLAYER_ACTION"

        spell_choice_input = ui_instance.print_prompt("Choose spell to cast (0 to cancel): ")
        if not spell_choice_input.isdigit():
            ui_instance.slow_print("Invalid input.")
            ui_instance.press_enter()
            return "REPROMPT_PLAYER_ACTION"

        spell_choice_key = spell_choice_input
        if spell_choice_key == "0":
            return "REPROMPT_PLAYER_ACTION"

        if spell_choice_key in castable_spells_map:
            selected_spell = castable_spells_map[spell_choice_key]
            target = None
            if selected_spell.effect_properties.get("target_self"):
                target = player
            else:
                target = get_target_logic(player, enemies, ui_instance, player, combat_instance.allies, combat_instance.player_summons)

            if target:
                player.stats.current_magicka -= selected_spell.cost
                ui_instance.slow_print(f"You cast {selected_spell.name}!")

                if selected_spell.effect_properties.get("target_self"):
                    if selected_spell.damage_type == "healing":
                         heal_amount = random.randint(selected_spell.base_damage_min, selected_spell.base_damage_max)
                         player.stats.current_health = min(player.stats.max_health, player.stats.current_health + heal_amount)
                         ui_instance.slow_print(f"You heal yourself for {heal_amount} health!")
                    if selected_spell.effect_properties.get("armor_bonus"):
                        ui_instance.slow_print(f"Your skin hardens like oak! (Armor +{selected_spell.effect_properties['armor_bonus']})")
                        # TODO: Implement temporary status effect for armor bonus
                elif selected_spell.damage_type and selected_spell.damage_type != "healing":
                    ui_instance.slow_print(f"You cast {selected_spell.name} on {target.name}!")
                    spell_damage = random.randint(selected_spell.base_damage_min, selected_spell.base_damage_max)
                    skill_level = player.skills.get(selected_spell.school.lower(), 0)
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
                        ui_instance.slow_print(f"The shock also drains {magicka_dmg} of {target.name}'s Magicka!")

                target.stats.take_damage(spell_damage)
                ui_instance.slow_print(f"{selected_spell.name} deals {spell_damage} {selected_spell.damage_type} damage!")

            if selected_spell.effect_properties and "summon_key" in selected_spell.effect_properties:
                summon_key = selected_spell.effect_properties["summon_key"]
                if summon_key == "spectral_wolf":
                    # Need NPC class to create a summon
                    from npc import NPC as NPC_class # Local import to avoid circular dependency at module level
                    summon_level = player.level // 2 + 1
                    summoned_creature = NPC_class(name="Spectral Wolf", race="spirit_wolf",
                                            role="spectral_ally", level=summon_level)
                    summoned_creature.summon_duration = selected_spell.duration
                    combat_instance.player_summons.append(summoned_creature)
                    ui_instance.slow_print(f"A {summoned_creature.name} appears to aid you!")

            player.improve_skill(selected_spell.school.lower(), 1)
            combat_instance.combo_counter = 0
            if target and target != player and not target.stats.is_alive():
                ui_instance.slow_print(f"You defeated {target.name} with {selected_spell.name}!")
            return True
        else:
            return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during cast spell: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_use_item(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    ui_instance = UI
    try:
        if player.inventory:
            ui_instance.print_subheading("Your inventory:")
            usable_items = [item for item in player.inventory
                          if item.category in ["potion", "food", "scroll"]]
            if not usable_items:
                ui_instance.slow_print("You have no usable items.")
                ui_instance.press_enter()
                return "REPROMPT_PLAYER_ACTION"
            for i, item in enumerate(usable_items, 1):
                ui_instance.print_info(f"[{i}] {item.name} ({item.category})")
            try:
                item_choice_str = input("Use which item? (0 to cancel): ")
                if not item_choice_str.isdigit():
                    ui_instance.slow_print("Invalid input.")
                    ui_instance.press_enter()
                    return "REPROMPT_PLAYER_ACTION"
                item_choice = int(item_choice_str)
                if item_choice == 0:
                    return "REPROMPT_PLAYER_ACTION"
                if 1 <= item_choice <= len(usable_items):
                    item = usable_items[item_choice - 1]
                    if hasattr(item, 'use'):
                        item.use(player) # Item use might affect player stats directly
                        return True
                    else:
                        ui_instance.slow_print(f"Cannot use {item.name} right now.")
                        return "REPROMPT_PLAYER_ACTION"
                else:
                    ui_instance.slow_print("Invalid item number.")
                    ui_instance.press_enter()
                    return "REPROMPT_PLAYER_ACTION"
            except ValueError:
                ui_instance.slow_print("Please enter a number.")
                ui_instance.press_enter()
                return "REPROMPT_PLAYER_ACTION"
        else:
            ui_instance.slow_print("Your inventory is empty.")
            ui_instance.press_enter()
        return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during use item: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_block(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    ui_instance = UI
    try:
        ui_instance.slow_print("You raise your defenses, ready to block the next melee attack!")
        player.is_blocking = True
        combat_instance.combo_counter = 0
        return True
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during block: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_dodge(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    ui_instance = UI
    try:
        dodge_cost = combat_instance.get_dodge_cost()
        if player.stats.current_fatigue >= dodge_cost:
            player.stats.current_fatigue -= dodge_cost
            ui_instance.slow_print(f"You spend {dodge_cost} stamina preparing to dodge!")
            player.is_dodging = True
            combat_instance.combo_counter = 0
            return True
        else:
            ui_instance.slow_print(f"Not enough stamina to dodge (Need {dodge_cost}, Have {player.stats.current_fatigue}).")
            ui_instance.press_enter()
            return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during dodge: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_flee(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    ui_instance = UI
    try:
        ui_instance.slow_print("You attempt to flee!")
        flee_chance = 0.5 + (player.stats.agility / 200)
        if random.random() < flee_chance:
            ui_instance.slow_print("You successfully fled from combat!")
            return False # Flee successful, combat ends for player
        else:
            ui_instance.slow_print("You failed to flee!")
            combat_instance.combo_counter = 0
            return True # Turn consumed, flee failed
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during flee: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_taunt(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI
    try:
        target = get_target_logic(player, enemies, ui_instance, player, combat_instance.allies, combat_instance.player_summons)
        if target:
            ui_instance.slow_print(f"You taunt {target.name}!")
            # Apply a "Taunted" status effect to the target
            taunted_effect = StatusEffect(name="Taunted", duration=2, description=f"Taunted by {player.name}, likely to attack them.")
            target.apply_status_effect(taunted_effect)
            return True
        else:
            return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during taunt: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_observe(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI
    try:
        ui_instance.slow_print("You take a moment to observe your surroundings and the enemies.")
        for enemy in enemies:
            ui_instance.slow_print(f"{enemy.name}: Health - {enemy.stats.current_health}/{enemy.stats.max_health}, Level - {enemy.level}")
            # You could add more detailed information here, like resistances, equipped items, etc.
        return True
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during observe: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_wait(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    ui_instance = UI
    try:
        ui_instance.slow_print("You wait and see what happens.")
        return True
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during wait: {e}")
        return "REPROMPT_PLAYER_ACTION"

def handle_use_combo(combat_instance: 'Combat') -> bool:
    player = combat_instance.player
    enemies = combat_instance.enemies
    ui_instance = UI
    try:
        if not combat_instance.available_combos:
            ui_instance.slow_print("You have no combos available.")
            ui_instance.press_enter()
            return "REPROMPT_PLAYER_ACTION"

        ui_instance.print_subheading("Available Combos:")
        for i, combo in enumerate(combat_instance.available_combos, 1):
            ui_instance.print_info(f"[{i}] {combo.name} (Stamina Cost: {combo.stamina_cost})")

        try:
            combo_choice_str = input("Choose a combo (0 to cancel): ")
            if not combo_choice_str.isdigit():
                ui_instance.slow_print("Invalid input.")
                ui_instance.press_enter()
                return "REPROMPT_PLAYER_ACTION"

            combo_choice = int(combo_choice_str)
            if combo_choice == 0:
                return "REPROMPT_PLAYER_ACTION"

            if 1 <= combo_choice <= len(combat_instance.available_combos):
                selected_combo = combat_instance.available_combos[combo_choice - 1]
                if player.stats.current_fatigue >= selected_combo.stamina_cost:
                    pass
                else:
                    ui_instance.slow_print("Not enough stamina to use this combo.")
                    ui_instance.press_enter()
                    return "REPROMPT_PLAYER_ACTION"
        except Exception as e:
            ui_instance.slow_print(f"An error occurred during combo choice: {e}")
            return "REPROMPT_PLAYER_ACTION"
    except Exception as e:
        ui_instance.slow_print(f"An error occurred during use combo: {e}")
        return "REPROMPT_PLAYER_ACTION"
