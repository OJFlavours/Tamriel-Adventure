# combat_npc_actions.py
import random
from typing import TYPE_CHECKING, List

from ui import UI
from combat_targeting import get_target_logic
from damage_utils import calculate_damage_logic
from combat_logic import apply_and_log_weapon_effects_logic

if TYPE_CHECKING:
    from player import Player
    from npc_entities import NPC
    from combat import Combat

def handle_npc_turn(combat_instance: 'Combat', npc: 'NPC') -> bool:
    player = combat_instance.player
    ui_instance = UI

    if not npc.stats.is_alive():
        return True

    ui_instance.print_subheading(f"{npc.name}'s Turn")
    # Add safety checks for stats attributes
    if hasattr(npc, 'stats') and hasattr(npc.stats, 'current_health'):
        ui_instance.print_info(f"Health: {npc.stats.current_health}/{npc.stats.max_health} | Magicka: {npc.stats.current_magicka}/{npc.stats.max_magicka}")

    npc_tags_category = npc.tags.get("npc", {})
    npc_attitude_value = npc_tags_category.get("attitude", "neutral")

    if npc_attitude_value == "hostile":
        # Simplified action choice for now
        chosen_npc_action = "attack"
        damage = 0

        # NPC spell logic
        can_cast_spell = False
        selected_npc_spell = None
        if hasattr(npc, 'known_spells') and npc.known_spells:
            castable_npc_spells = [sp for sp in npc.known_spells if npc.stats.current_magicka >= sp.cost]
            if castable_npc_spells:
                can_cast_spell = True
                selected_npc_spell = random.choice(castable_npc_spells)
                chosen_npc_action = "spell"

        if chosen_npc_action == "spell" and selected_npc_spell:
            npc.stats.current_magicka -= selected_npc_spell.cost
            ui_instance.slow_print(f"{npc.name} casts {selected_npc_spell.name}!")
            
            potential_targets = [p for p in [player] + combat_instance.allies if p.stats.is_alive()]
            target_for_spell = get_target_logic(npc, potential_targets, ui_instance, player, combat_instance.allies, combat_instance.player_summons)

            if target_for_spell:
                spell_damage = random.randint(selected_npc_spell.base_damage_min, selected_npc_spell.base_damage_max)
                target_for_spell.stats.take_damage(spell_damage)
                ui_instance.slow_print(f"{selected_npc_spell.name} hits {target_for_spell.name} for {spell_damage} {selected_npc_spell.damage_type} damage!")

        else: # Default to attack if not casting spell
            target_for_attack = get_target_logic(npc, [player] + combat_instance.allies, ui_instance, player, combat_instance.allies, combat_instance.player_summons)
            if not target_for_attack:
                ui_instance.slow_print(f"{npc.name} looks for a target but finds none.")
                return True

            is_npc_ranged_attack = combat_instance.is_ranged_attack(npc)
            damage = calculate_damage_logic(npc, target_for_attack, ui_instance, 0, False, is_ranged=is_npc_ranged_attack)
            
            dodged_this_attack = False
            if hasattr(target_for_attack, 'is_dodging') and target_for_attack.is_dodging:
                dodge_chance = 0.3 + (target_for_attack.stats.agility / 200) - (npc.stats.agility / 200)
                if random.random() < dodge_chance:
                    ui_instance.slow_print(f"{target_for_attack.name} deftly dodges {npc.name}'s attack!")
                    dodged_this_attack = True
                target_for_attack.is_dodging = False

            if not dodged_this_attack:
                target_for_attack.stats.take_damage(damage)
                ui_instance.slow_print(f"{npc.name} hits {target_for_attack.name} for {damage} damage!")
                apply_and_log_weapon_effects_logic(npc, target_for_attack, ui_instance, is_npc_ranged_attack)

        if not player.stats.is_alive():
            ui_instance.slow_print(f"You have been defeated by {npc.name}!")
            return False
    else:
        ui_instance.slow_print(f"{npc.name} seems uncertain and takes no action.")

    return True