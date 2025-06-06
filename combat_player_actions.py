import logging

logging.basicConfig(level=logging.DEBUG, filename='debug.log')

logging.debug("combat_player_actions.py is being imported")

from damage_utils import calculate_damage_logic
from status_effects import StatusEffect
import status_effects
from ui import UI
from combat_targeting import get_target_logic
# from combat import Combat # For type hinting 'Combat', use string literal to avoid circular import
import random

def handle_attack_action(player, target, combat_log):
    """Handles a standard attack action."""
    damage = calculate_damage_logic(player, target, combat_log, 0, False)
    if damage is not None and damage > 0:
        target.stats.take_damage(damage)
        combat_log.append(f"{player.name}'s attack hits {target.name} for {damage} damage.")
    elif damage == 0:
        combat_log.append(f"{player.name}'s attack misses or is blocked by {target.name}.")
    else:
        combat_log.append(f"{player.name}'s attack against {target.name} has an unexpected outcome.")

def handle_power_attack_action(player, target, combat_log):
    """Handles a power attack action."""
    damage = calculate_damage_logic(player, target, combat_log, 0, True)
    if damage is not None and damage > 0:
        target.stats.take_damage(damage)
        combat_log.append(f"{player.name}'s power attack hits {target.name} for {damage} damage!")
    elif damage == 0:
        combat_log.append(f"{player.name}'s power attack misses or is blocked by {target.name}.")
    else:
        combat_log.append(f"{player.name}'s power attack against {target.name} has an unexpected outcome.")

def handle_block_action(player, target, combat_log):
    """Handles a block action."""
    player.is_blocking = True
    combat_log.append(f"{player.name} raises their shield, preparing to block.")

def handle_dodge_action(player, target, combat_log):
    """Handles a dodge action."""
    player.is_dodging = True
    combat_log.append(f"{player.name} attempts to dodge the incoming attack.")

def handle_cast_spell_action(player, target, spell, combat_log):
    """Handles casting a spell during combat."""
    if player.mana >= spell.mana_cost:
        player.mana -= spell.mana_cost
        combat_log.append(f"{player.name} casts {spell.name} at {target.name}!")
        spell.apply_effect(player, target, combat_log)
    else:
        combat_log.append(f"{player.name} does not have enough mana to cast {spell.name}!")

def handle_use_item_action(player, target, item, combat_log):
    """Handles using an item during combat."""
    if item in player.inventory:
        player.inventory.remove(item)
        combat_log.append(f"{player.name} uses {item.name}.")
        item.apply_effect(player, target, combat_log)
    else:
        combat_log.append(f"{player.name} does not have {item.name} in their inventory!")

def handle_apply_status_effect_action(player, target, status_effect_name, combat_log):
    """Handles applying a status effect to a target."""
    status_effect_class = getattr(status_effects, status_effect_name, None)
    if status_effect_class:
        if hasattr(target, 'apply_status_effect') and hasattr(target, 'stats'):
            combat_log.append(f"{player.name} applies {status_effect_name} to {target.name}.")
            # Assuming constructor of status effect class might take target or be parameterless
            # and then applied. For StatusEffect(target=target) or similar.
            try:
                effect_instance = status_effect_class(target=target) 
            except TypeError: # If constructor doesn't take target
                effect_instance = status_effect_class()
            target.apply_status_effect(effect_instance)
        else:
            combat_log.append(f"Target {target.name} cannot have status effects applied or lacks stats.")
    else:
        combat_log.append(f"Status effect {status_effect_name} not found.")

def handle_player_turn(combat_instance: 'Combat') -> bool: # Type hint for Combat using string literal
    """
    Handles the player's turn in combat.
    Presents options, gets player input, and calls appropriate action handlers.
    Returns True if an action is taken (or flee fails), False if player successfully flees.
    The combat loop in combat.py expects a boolean or "REPROMPT_PLAYER_ACTION".
    This implementation loops internally for invalid choices, returning True/False.
    """
    player = combat_instance.player
    enemies = combat_instance.enemies # Active enemies
    combat_log = combat_instance.combat_log
    # ui_instance = UI # UI is used directly as static methods, e.g., UI.slow_print

    player.is_dodging = False # Reset dodge status at the start of choosing an action

    while True: # Loop for player action choice until a valid action is performed or flee
        UI.print_heading(f"{player.name}'s Turn ({player.stats.current_health}/{player.stats.max_health} HP, {player.stats.current_mana}/{player.stats.max_mana} MP, {player.stats.current_stamina}/{player.stats.max_stamina} SP)")
        if enemies:
            UI.slow_print("Enemies:")
            for i, enemy in enumerate(enemies):
                if enemy.stats.is_alive():
                    UI.slow_print(f"  {i+1}. {enemy.name} ({enemy.stats.current_health}/{enemy.stats.max_health} HP)")
        else:
            UI.slow_print("No enemies remain.") # Should be caught by main combat loop, but good check
            return True # No action to take if no enemies, effectively ends turn

        options = ["Attack", "Power Attack", "Block", "Dodge"]
        if player.spells:
            options.append("Cast Spell")
        if any(hasattr(item, 'apply_effect') for item in player.inventory): # Basic check for usable items
            options.append("Use Item")
        options.append("Flee")
        
        choice = UI.get_player_choice("Choose your action:", options)

        if choice == "Attack":
            if not enemies:
                UI.slow_print("No enemies to attack.")
                continue
            target = get_target_logic(player, enemies, UI, player, combat_instance.allies, combat_instance.player_summons)
            if target:
                handle_attack_action(player, target, combat_log)
                return True # Action taken
            else:
                UI.slow_print("No target selected or available.")
                continue # Re-prompt

        elif choice == "Power Attack":
            if not enemies:
                UI.slow_print("No enemies for a power attack.")
                continue
            power_attack_cost = combat_instance.get_power_attack_cost()
            if player.stats.current_stamina >= power_attack_cost:
                target = get_target_logic(player, enemies, UI, player, combat_instance.allies, combat_instance.player_summons)
                if target:
                    player.stats.current_stamina -= power_attack_cost
                    handle_power_attack_action(player, target, combat_log)
                    combat_log.append(f"{player.name} used {power_attack_cost} stamina for a power attack. ({player.stats.current_stamina} SP remaining)")
                    return True # Action taken
                else:
                    UI.slow_print("No target selected or available for power attack.")
                    continue # Re-prompt
            else:
                UI.slow_print(f"Not enough stamina for a power attack! (Needs {power_attack_cost}, Has {player.stats.current_stamina})")
                continue # Re-prompt

        elif choice == "Block":
            handle_block_action(player, None, combat_log) # Target not strictly needed for block message
            return True # Action taken

        elif choice == "Dodge":
            dodge_cost = combat_instance.get_dodge_cost()
            if player.stats.current_stamina >= dodge_cost:
                player.stats.current_stamina -= dodge_cost
                handle_dodge_action(player, None, combat_log) # Target not strictly needed
                combat_log.append(f"{player.name} used {dodge_cost} stamina to dodge. ({player.stats.current_stamina} SP remaining)")
                return True # Action taken
            else:
                UI.slow_print(f"Not enough stamina to dodge! (Needs {dodge_cost}, Has {player.stats.current_stamina})")
                continue # Re-prompt

        elif choice == "Cast Spell":
            if not player.spells: # Should not happen if option wasn't shown
                UI.slow_print("You don't know any spells.")
                continue

            spell_options = [(f"{s.name} (Cost: {s.mana_cost} MP)") for s in player.spells]
            spell_choice_prompt = UI.get_player_choice("Choose a spell:", spell_options + ["Cancel"])

            if spell_choice_prompt == "Cancel" or not spell_choice_prompt:
                continue

            chosen_spell_name = spell_choice_prompt.split(" (Cost:")[0]
            chosen_spell = next((s for s in player.spells if s.name == chosen_spell_name), None)
            
            if not chosen_spell:
                UI.slow_print("Invalid spell choice.") 
                continue

            if player.stats.current_mana >= chosen_spell.mana_cost:
                target = None
                spell_target_type = getattr(chosen_spell, 'target_type', 'enemy') # e.g., "self", "enemy", "ally"

                if spell_target_type == "self":
                    target = player
                elif spell_target_type == "enemy":
                    if not enemies:
                        UI.slow_print(f"No enemies to target with {chosen_spell.name}.")
                        continue
                    target = get_target_logic(player, enemies, UI, player, combat_instance.allies, combat_instance.player_summons)
                    if not target:
                        UI.slow_print(f"No target selected for {chosen_spell.name}.")
                        continue
                elif spell_target_type == "ally":
                    # This would require listing allies and player_summons as potential targets
                    potential_ally_targets = [p_ally for p_ally in combat_instance.allies if p_ally.stats.is_alive()] + \
                                             [p_sum for p_sum in combat_instance.player_summons if p_sum.stats.is_alive()]
                    if not potential_ally_targets:
                        UI.slow_print(f"No allies to target with {chosen_spell.name}.")
                        continue
                    target = get_target_logic(player, potential_ally_targets, UI, player, combat_instance.allies, combat_instance.player_summons, prompt_message=f"Target ally for {chosen_spell.name}:")
                    if not target:
                        UI.slow_print(f"No ally selected for {chosen_spell.name}.")
                        continue
                else: # Default or unknown, or requires specific handling (e.g. AoE)
                    UI.slow_print(f"Spell '{chosen_spell.name}' has an unsupported target type: {spell_target_type}. Assuming enemy target for now.")
                    if not enemies:
                        UI.slow_print(f"No enemies to target with {chosen_spell.name}.")
                        continue
                    target = get_target_logic(player, enemies, UI, player, combat_instance.allies, combat_instance.player_summons)
                    if not target:
                        UI.slow_print(f"No target selected for {chosen_spell.name}.")
                        continue
                
                # Mana deduction is now handled within handle_cast_spell_action
                handle_cast_spell_action(player, target, chosen_spell, combat_log)
                return True # Action taken
            else:
                UI.slow_print(f"Not enough mana to cast {chosen_spell.name}. (Needs {chosen_spell.mana_cost}, Has {player.stats.current_mana})")
                continue

        elif choice == "Use Item":
            combat_items = [item for item in player.inventory if hasattr(item, 'apply_effect') and getattr(item, 'usable_in_combat', True)]
            if not combat_items: # Should not happen if option wasn't shown
                UI.slow_print("You have no usable items in combat.")
                continue

            item_options = [item.name for item in combat_items]
            item_choice_str = UI.get_player_choice("Choose an item to use:", item_options + ["Cancel"])

            if item_choice_str == "Cancel" or not item_choice_str:
                continue

            chosen_item = next((item for item in combat_items if item.name == item_choice_str), None)
            if not chosen_item:
                UI.slow_print("Invalid item choice.")
                continue
            
            target = None
            item_target_type = getattr(chosen_item, 'target_type', 'self') # e.g., "self", "enemy"

            if item_target_type == "self":
                target = player
            elif item_target_type == "enemy":
                if not enemies:
                    UI.slow_print(f"No enemies to target with {chosen_item.name}.")
                    continue
                target = get_target_logic(player, enemies, UI, player, combat_instance.allies, combat_instance.player_summons)
                if not target:
                    UI.slow_print(f"No target selected for {chosen_item.name}.")
                    continue
            # If item_target_type is 'none', target remains None.
            # item.apply_effect must handle target=None if applicable.
            
            # Inventory removal and effect application is handled in handle_use_item_action
            handle_use_item_action(player, target, chosen_item, combat_log)
            return True # Action taken

        elif choice == "Flee":
            flee_chance = 0.3 + (player.stats.agility / 200) # Base 30% + agility bonus (e.g. 50 agility = +25% = 55%)
            flee_chance = min(max(flee_chance, 0.1), 0.9) # Clamp between 10% and 90%

            if random.random() < flee_chance:
                UI.slow_print(f"You successfully flee from combat! (Chance: {flee_chance*100:.0f}%)")
                return False # Player fled
            else:
                UI.slow_print(f"You try to flee, but fail! (Chance: {flee_chance*100:.0f}%)")
                return True # Failed to flee, turn ends

        else: # Should not be reached if get_player_choice is robust
            UI.slow_print("Invalid action. Please try again.")
            # No return here, loop will continue to re-prompt
