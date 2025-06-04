# combat_npc_actions.py
import random
from typing import TYPE_CHECKING, List

from ui import UI
from combat_targeting import get_target_logic
from combat_logic import calculate_damage_logic, apply_and_log_weapon_effects_logic

if TYPE_CHECKING:
    from player import Player
    from npc import NPC
    from combat import Combat # To avoid circular import

def handle_npc_turn(combat_instance: 'Combat', npc: 'NPC') -> bool:
    player = combat_instance.player
    ui_instance = UI

    if not npc.stats.is_alive():
        return True

    ui_instance.print_subheading(f"{npc.name}'s Turn")
    ui_instance.print_info(f"Health: {npc.stats.current_health}/{npc.stats.max_health} | Magicka: {npc.stats.current_magicka}/{npc.stats.max_magicka}")

    npc_tags_category = npc.tags.get("npc", {})
    npc_attitude_value = npc_tags_category.get("attitude", "neutral")
    # npc_class_value = npc_tags_category.get("role_primary", "") # Not directly used in original logic for action choice

    if npc_attitude_value == "hostile":
        chosen_npc_action = "attack"
        damage = 0  # Initialize damage
        archetype = npc.combat_archetype if hasattr(npc, 'combat_archetype') else "StandardMelee"

        can_cast_spell = False
        castable_npc_spells = []
        if hasattr(npc, 'known_spells') and npc.known_spells:
            castable_npc_spells = [sp for sp in npc.known_spells if npc.stats.current_magicka >= sp.cost]
            if castable_npc_spells:
                can_cast_spell = True

                # Prioritize spells based on effectiveness and cost
                best_spell = None
                best_spell_score = -1

                for spell in castable_npc_spells:
                    spell_score = 0

                    # Consider damage potential
                    if spell.damage_type != "healing":
                        spell_score += (spell.base_damage_max + spell.base_damage_min) / 2 * 0.7

                    # Consider healing potential
                    if spell.damage_type == "healing":
                        spell_score += (spell.base_damage_max + spell.base_damage_min) / 2 * 0.9

                    # Consider magicka cost
                    spell_score -= spell.cost * 0.3

                    if spell_score > best_spell_score:
                        best_spell = spell
                        best_spell_score = spell_score

                if best_spell:
                    selected_npc_spell = best_spell
                    chosen_npc_action = "spell"
                else:
                    chosen_npc_action = "attack"  # Fallback to attack
            else:
                chosen_npc_action = "attack"  # No spells available, attack

        try:
            if chosen_npc_action == "spell":
                if not selected_npc_spell and castable_npc_spells:
                    selected_npc_spell = random.choice(castable_npc_spells)

                if not selected_npc_spell:
                    ui_instance.slow_print(f"{npc.name} tries to cast a spell but fizzles...")
                    chosen_npc_action = "attack"
                    damage = calculate_damage_logic(npc, player, ui_instance, 0, False)
                else:
                    npc.stats.current_magicka -= selected_npc_spell.cost
                    ui_instance.slow_print(f"{npc.name} casts {selected_npc_spell.name}!")
                    
                    potential_targets_for_spell = [t for t in [player] + combat_instance.allies + combat_instance.player_summons if t.stats.is_alive()]
                    target_for_spell = get_target_logic(npc, potential_targets_for_spell, ui_instance, player, combat_instance.allies, combat_instance.player_summons)

                    if not target_for_spell and not selected_npc_spell.effect_properties.get("target_self"):
                        target_for_spell = player 

                    if selected_npc_spell.effect_properties.get("target_self"):
                        target_for_spell = npc
                        if selected_npc_spell.damage_type == "healing":
                             heal_amount = random.randint(selected_npc_spell.base_damage_min, selected_npc_spell.base_damage_max)
                             npc.stats.current_health = min(npc.stats.max_health, npc.stats.current_health + heal_amount)
                             ui_instance.slow_print(f"{npc.name} heals for {heal_amount} health!")
                        if selected_npc_spell.effect_properties.get("armor_bonus"):
                            ui_instance.slow_print(f"{npc.name} bolsters their defenses!")
                    elif target_for_spell and selected_npc_spell.damage_type and selected_npc_spell.damage_type != "healing": # Ensure target_for_spell is not None
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
                                ui_instance.slow_print(f"The shock also drains {magicka_dmg} of {target_for_spell.name}'s Magicka!")

                        dodged_spell = False
                        if target_for_spell == player and player.is_dodging:
                            player_dodge_score = player.stats.agility + player.skills.get("light_armor", 0) * 0.5
                            npc_attack_score = npc.stats.intelligence + npc.skills.get(selected_npc_spell.school.lower(),0) * 0.5
                            dodge_chance = 0.15 + (player_dodge_score - npc_attack_score) / 150.0
                            dodge_chance = max(0.01, min(dodge_chance, 0.50))
                            if random.random() < dodge_chance:
                                ui_instance.slow_print(f"You manage to sidestep {npc.name}'s {selected_npc_spell.name}!")
                                dodged_spell = True
                            else:
                                ui_instance.slow_print(f"You try to avoid the {selected_npc_spell.name}, but it hits!")
                            player.is_dodging = False

                        if not dodged_spell:
                            target_for_spell.stats.take_damage(spell_damage)
                            ui_instance.slow_print(f"{selected_npc_spell.name} hits {target_for_spell.name} for {spell_damage} {selected_npc_spell.damage_type} damage!")
                    elif not target_for_spell: # Case where NPC tried to cast offensive spell but no valid targets
                        ui_instance.slow_print(f"{npc.name} looks around but finds no suitable target for {selected_npc_spell.name}.")

        except Exception as e:
            ui_instance.slow_print(f"An error occurred while casting a spell: {e}")
            chosen_npc_action = "attack" # Fallback to attack

        try:
            if chosen_npc_action == "power_attack":
                npc.stats.current_fatigue -= 15
                damage = calculate_damage_logic(npc, player, ui_instance, 0, True)
                damage = int(damage * 1.5)
                ui_instance.slow_print(f"{npc.name} unleashes a powerful attack!")

            elif chosen_npc_action == "ranged_attack":
                damage = calculate_damage_logic(npc, player, ui_instance, 0, False, is_ranged=True)
                ui_instance.slow_print(f"{npc.name} fires at you!")

            elif chosen_npc_action == "attack":
                damage = calculate_damage_logic(npc, player, ui_instance, 0, False)
            
            # This block executes if an attack action was chosen (normal, power, or ranged)
            # It won't execute if a spell was successfully cast (unless spell casting failed and fell back to attack)
            if chosen_npc_action in ["attack", "power_attack", "ranged_attack"]:
                target_for_attack = player # NPCs primarily attack the player with physical attacks
                dodged_this_attack = False
                is_npc_ranged_attack = (chosen_npc_action == "ranged_attack") or combat_instance._is_ranged_attack(npc)

                if target_for_attack.is_dodging: # Check if player is dodging
                    player_dodge_score = target_for_attack.stats.agility + target_for_attack.skills.get("light_armor", 0) * 0.75
                    npc_attack_score = npc.stats.agility + npc.skills.get("one_handed" if not is_npc_ranged_attack else "archery", 0) * 0.5
                    dodge_chance = 0.3 + (player_dodge_score - npc_attack_score) / 100.0
                    dodge_chance = max(0.05, min(dodge_chance, 0.75))

                if random.random() < dodge_chance:
                    ui_instance.slow_print(f"You deftly dodge {npc.name}'s attack!")
                    damage = 0
                    dodged_this_attack = True
                    target_for_attack.improve_skill("light_armor", 1)
                else:
                    ui_instance.slow_print(f"You attempt to dodge but {npc.name}'s attack connects!")
                target_for_attack.is_dodging = False

                if not dodged_this_attack:
                    try:
                        if target_for_attack.is_blocking and is_npc_ranged_attack:
                            ui_instance.slow_print(f"Your block is ineffective against {npc.name}'s ranged attack!")

                        if damage > 0 :
                            if target_for_attack.is_blocking and not is_npc_ranged_attack:
                                ui_instance.slow_print(f"You block {npc.name}'s attack, reducing the damage!")
                                damage = int(damage * 0.5) # Reduce damage by 50% when blocking

                                # Check for counterattack dynamic interaction
                                if combat_instance.last_attacker == npc and player.is_blocking:
                                    result = combat_instance.counterattack(player, npc)
                                    if result:
                                        ui_instance.slow_print(result)

                            target_for_attack.stats.take_damage(damage)
                            ui_instance.slow_print(f"{npc.name} hits you for {damage} damage!")
                        elif not dodged_this_attack and target_for_attack.is_blocking and not is_npc_ranged_attack:
                            pass # Blocked, damage already reduced by calculate_damage_logic
                        elif not dodged_this_attack:
                             ui_instance.slow_print(f"{npc.name}'s attack glances off harmlessly!")

                        apply_and_log_weapon_effects_logic(npc, target_for_attack, ui_instance, is_npc_ranged_attack)
                    except Exception as e:
                        ui_instance.slow_print(f"An error occurred during counterattack: {e}")

        except Exception as e:
            ui_instance.slow_print(f"An error occurred during the attack: {e}")

        if not player.stats.is_alive():
            ui_instance.slow_print(f"You have been defeated by {npc.name}!")
            return False # Player defeated
    else:
        ui_instance.slow_print(f"{npc.name} seems uncertain and takes no action.")

    return True # Turn completed, player still alive or NPC took no action