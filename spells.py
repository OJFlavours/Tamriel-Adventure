# spells.py
from typing import Tuple

class Spell:
    def __init__(self, name: str, description: str, school: str, cost: int, 
                 damage_type: str | None = None, 
                 base_damage_min: int = 0, base_damage_max: int = 0,
                 duration: int = 0, # For effects like buffs/debuffs or damage over time
                 effect_properties: dict | None = None): # For more complex effects
        self.name = name
        self.description = description
        self.school = school.capitalize()
        self.cost = cost
        self.damage_type = damage_type.lower() if damage_type else None
        self.base_damage_min = base_damage_min
        self.base_damage_max = base_damage_max
        self.duration = duration
        self.effect_properties = effect_properties if effect_properties else {}

    def get_effect_description(self) -> str:
        """Returns a concise description of the spell's primary effect."""
        if self.damage_type and self.base_damage_max > 0:
            return f"Deals {self.base_damage_min}-{self.base_damage_max} {self.damage_type} damage."
        elif self.damage_type == "healing":
            return f"Restores {self.base_damage_min}-{self.base_damage_max} Health."
        # Add more descriptions for other types of effects (buffs, debuffs, summons)
        return self.description # Fallback to full description

    def __str__(self):
        return f"{self.name} ({self.school}) - Cost: {self.cost} MP. {self.get_effect_description()}"

# Predefined Spell Templates
SPELL_TEMPLATES: dict[str, dict] = {
    "flames": {
        "name": "Flames",
        "description": "A gout of fire that inflicts ongoing fire damage.",
        "school": "Destruction", "cost": 14, "damage_type": "fire",
        "base_damage_min": 10, "base_damage_max": 16, "duration": 1 # Increased
    },
    "firebolt": {
        "name": "Firebolt",
        "description": "A bolt of fire that explodes on impact, dealing fire damage.",
        "school": "Destruction", "cost": 25, "damage_type": "fire",
        "base_damage_min": 25, "base_damage_max": 35 # Increased
    },
    "healing": {
        "name": "Healing",
        "description": "Heals the caster.",
        "school": "Restoration", "cost": 15, "damage_type": "healing",
        "base_damage_min": 20, "base_damage_max": 30 # Increased
    },
    "lesser_ward": {
        "name": "Lesser Ward",
        "description": "Increases Armor Rating and negates some spell damage.",
        "school": "Alteration", "cost": 30, "duration": 3, # Lasts 3 turns
        "effect_properties": {"armor_bonus": 40, "spell_negation_chance": 0.25}
    },
    "conjure_familiar": {
        "name": "Conjure Familiar",
        "description": "Summons a spectral wolf to fight for you for a short time.",
        "school": "Conjuration", "cost": 50, "duration": 5, # Lasts 5 turns
        "effect_properties": {"summon_key": "spectral_wolf"}
    },
    "courage": {
        "name": "Courage",
        "description": "Target won't flee for 60 seconds and gets some extra health and stamina.",
        "school": "Illusion", "cost": 20, "duration": 5, # Lasts 5 turns
        "effect_properties": {"buff_health": 20, "buff_stamina": 20, "prevents_flee": True}
    },
    "frostbite": {
        "name": "Frostbite",
        "description": "A blast of icy cold that deals frost damage and may slow targets.",
        "school": "Destruction", "cost": 18, "damage_type": "frost",
        "base_damage_min": 8, "base_damage_max": 14,
        "effect_properties": {"slow_chance": 0.3, "slow_potency": 0.25, "slow_duration": 2} # 30% chance to slow by 25% for 2 turns
    },
    "sparks": {
        "name": "Sparks",
        "description": "Lightning that does shock damage to Health and Magicka.",
        "school": "Destruction", "cost": 16, "damage_type": "shock",
        "base_damage_min": 7, "base_damage_max": 11, # Lower health damage, but also hits Magicka
        "effect_properties": {"magicka_damage_ratio": 0.5} # Deals 50% of health damage to Magicka
    },
    "oakflesh": {
        "name": "Oakflesh",
        "description": "Improves the caster's armor rating by 40 points for 60 seconds.",
        "school": "Alteration", "cost": 25, "duration": 3, # Duration in combat turns
        "effect_properties": {"armor_bonus": 40, "buff": True, "target_self": True}
    }
    # TODO: Add more spells: Healing Hands, Candlelight, etc.
}

def get_spell(spell_key: str) -> Spell | None:
    """Creates a Spell instance from the templates."""
    template = SPELL_TEMPLATES.get(spell_key.lower())
    if template:
        return Spell(**template)
    return None