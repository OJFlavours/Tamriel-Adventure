# status_effects.py

from enum import Enum
from typing import List

class StatusEffectType(Enum):
    BLEEDING = "Bleeding"
    BURNING = "Burning"
    FROZEN = "Frozen"
    POISONED = "Poisoned"
    STUNNED = "Stunned"
    SILENCED = "Silenced"
    VULNERABLE = "Vulnerable"

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
            
        elif self.effect_type == StatusEffectType.SILENCED:
            character.can_cast_spells = False
            messages.append(f"{character.name} is silenced and cannot cast spells!")

        elif self.effect_type == StatusEffectType.VULNERABLE:
            character.stats.incoming_damage_multiplier += self.potency
            messages.append(f"{character.name} is vulnerable and takes increased damage!")
            
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