# damage_utils.py
import logging
import random

logging.basicConfig(level=logging.DEBUG, filename='debug.log')

def is_two_handed_weapon(character) -> bool:
    if not hasattr(character, 'equipment'):
        return False
    return any(item.category == "weapon" and
                hasattr(item, 'equipment_tag') and
                item.equipment_tag == "two_handed"
                for item in character.equipment)

def get_weapon_damage(character) -> int:
    weapon_damage = 0
    if hasattr(character, 'equipment'):
        for item in character.equipment:
            if item.category == "weapon" and hasattr(item, 'base_damage'):
                if isinstance(item.base_damage, (list, tuple)):
                    weapon_damage += random.randint(item.base_damage[0], item.base_damage[1])
                else:
                    weapon_damage += item.base_damage
    return weapon_damage

def has_elemental_weapon(character, element_type: str) -> bool:
    if not hasattr(character, 'equipment'):
        return False
    return any(item.category == "weapon" and
                hasattr(item, 'enchantment') and
                item.enchantment and
                element_type in item.enchantment.lower()
                for item in character.equipment)

def calculate_damage_logic(attacker, defender, ui_instance, combo_counter: int, player_is_power_attacking: bool, is_ranged: bool = False, body_part: str = None) -> int:
    """
    Calculates the damage dealt by an attacker to a defender.
    This is a more complete implementation.
    """
    from ui import UI # Local import to avoid circular dependency issues at the module level

    logging.debug(f"calculate_damage_logic called by {attacker.name if hasattr(attacker, 'name') else 'Unknown Attacker'} against {defender.name if hasattr(defender, 'name') else 'Unknown Defender'}")

    if is_ranged:
        base_damage = attacker.stats.agility // 3
        skill_modifier = attacker.skills.get("archery", 0) // 4
    else:
        base_damage = attacker.stats.strength // 3
        weapon_type_skill = "two_handed" if is_two_handed_weapon(attacker) else "one_handed"
        skill_modifier = attacker.skills.get(weapon_type_skill, 0) // 4

    weapon_dmg = get_weapon_damage(attacker)
    total_damage = base_damage + weapon_dmg + skill_modifier

    crit_chance = attacker.stats.luck // 3
    if is_ranged:
        crit_chance += attacker.skills.get("archery", 0) // 4
    else:
        crit_chance += attacker.skills.get(weapon_type_skill, 0) // 4

    if random.randint(1, 100) <= crit_chance:
        total_damage = int(total_damage * 1.5)
        ui_instance.slow_print(f"{attacker.name} lands a critical hit!")

    if combo_counter > 0 and not player_is_power_attacking:
        combo_bonus = min(combo_counter * 0.1, 0.5)
        total_damage = int(total_damage * (1 + combo_bonus))
        ui_instance.slow_print(f"Combo x{combo_counter}! ({int(combo_bonus*100)}% bonus damage)")

    if player_is_power_attacking:
        total_damage = int(total_damage * 1.5) # Power attacks do 50% more damage
        logging.debug(f"Power attack bonus applied. Damage is now: {total_damage}")

    armor_reduction = defender.stats.armor_rating if hasattr(defender.stats, 'armor_rating') else 0

    if hasattr(defender, 'is_blocking') and defender.is_blocking and not is_ranged:
        block_skill = defender.skills.get("block", 0)
        shield_bonus = 0
        equipped_shield = next((item for item in defender.equipment if hasattr(item, 'equipment_tag') and item.equipment_tag == "off_hand" and item.category == "armor"), None)
        if equipped_shield and hasattr(equipped_shield, 'armor_rating'):
            shield_bonus = equipped_shield.armor_rating

        block_effectiveness_percent = min( (block_skill * 0.6 + shield_bonus * 0.4) / 100, 0.85)
        damage_reduction_from_block = int(total_damage * block_effectiveness_percent)
        total_damage = max(0, total_damage - damage_reduction_from_block)
        ui_instance.slow_print(f"{defender.name} blocks, reducing damage by {damage_reduction_from_block} ({int(block_effectiveness_percent*100)}%)!")

        if hasattr(defender, 'improve_skill'):
            defender.improve_skill("block", 1)

        if hasattr(defender.stats, 'current_fatigue'):
            block_stamina_cost = 5
            defender.stats.current_fatigue = max(0, defender.stats.current_fatigue - block_stamina_cost)

    if body_part:
        if body_part == "Head":
            total_damage = int(total_damage * 1.5)
            ui_instance.slow_print("Headshot!")
        elif body_part in ["Left Arm", "Right Arm"]:
            total_damage = int(total_damage * 0.75)
            ui_instance.slow_print("Hit the arm!")
        elif body_part in ["Left Leg", "Right Leg"]:
            total_damage = int(total_damage * 0.75)
            defender.stats.agility = max(0, defender.stats.agility - 2)
            ui_instance.slow_print("Hit the leg! Agility reduced.")

    final_damage = max(0, total_damage - armor_reduction)

    if has_elemental_weapon(attacker, "fire"):
        final_damage *= (100 - defender.stats.fire_resist) / 100
    if has_elemental_weapon(attacker, "frost"):
        final_damage *= (100 - defender.stats.frost_resist) / 100
    if has_elemental_weapon(attacker, "shock"):
        final_damage *= (100 - defender.stats.shock_resist) / 100

    logging.debug(f"Final damage calculated: {int(final_damage)}")
    return int(final_damage)