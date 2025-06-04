from combat import calculate_damage_logic
from status_effects import StatusEffect
from combat_interactions import deal_damage
import status_effects

def handle_attack_action(player, target, combat_log):
    """Handles a standard attack action."""
    
    damage = calculate_damage_logic(player, target, combat_log, 0, False)
    deal_damage(target, damage, combat_log)

def handle_power_attack_action(player, target, combat_log):
    """Handles a power attack action."""
    
    damage = calculate_damage_logic(player, target, combat_log, 0, True)
    deal_damage(target, damage, combat_log)

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
    status_effect = getattr(status_effects, status_effect_name, None)
    if status_effect:
        combat_log.append(f"{player.name} applies {status_effect_name} to {target.name}.")
        target.apply_status_effect(status_effect(target))  # Instantiate the status effect
    else:
        combat_log.append(f"Status effect {status_effect_name} not found.")
