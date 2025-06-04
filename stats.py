# stats.py
import random
from typing import Dict, List, Any, Set  # Import Set for type hinting

# Assuming QuestLog is in quests.py and Item is in items.py
# We import them here to avoid circular dependencies where possible
# and for type hinting clarity.
from quests import QuestLog, Quest  # Import Quest for type hinting in QuestLog and Player
from items import Item  # Import Item for type hinting in inventory and equipment
from ui import UI  # For UI messages within Player/Stats methods


class Stats:
    """
    Encapsulates player or NPC stats, attributes, and derived combat values for Skyrim Adventure.
    """

    def __init__(self,
                 strength: int = 40, intelligence: int = 40, willpower: int = 40, agility: int = 40,
                 speed: int = 40,
                 endurance: int = 40, personality: int = 40, luck: int = 40, charisma: int = 40,
                 perception: int = 40,
                 max_health: int | None = None, max_magicka: int | None = None, max_fatigue: int | None = None,
                 current_health: int | None = None, current_magicka: int | None = None,
                 current_fatigue: int | None = None,
                 poison_resist: int = 0, magic_resist: int = 0, frost_resist: int = 0,
                 shock_resist: int = 0, fire_resist: int = 0,
                 inventory: List[Item] | None = None,  # Should be list of Item objects
                 gold: int = 0, level: int = 1):
        # Attributes
        self.strength = strength
        self.intelligence = intelligence
        self.willpower = willpower
        self.agility = agility
        self.speed = speed
        self.endurance = endurance
        self.personality = personality
        self.luck = luck
        self.charisma = charisma
        self.perception = perception

        self.level = level
        self.gold = gold

        # Experience for leveling
        self.experience = 0
        self.next_level_exp = self._calculate_next_level_exp(self.level)

        # Resistances
        self.poison_resist = poison_resist
        self.magic_resist = magic_resist
        self.frost_resist = frost_resist
        self.shock_resist = shock_resist
        self.fire_resist = fire_resist

        # Derived Stats (set after attributes)
        try:
            self.max_health = int(
                max_health if max_health is not None else 100 + (self.endurance * 2) + (self.level * 5))
            self.max_magicka = int(
                max_magicka if max_magicka is not None else 50 + (self.intelligence * 1.5) + (self.level * 3))
            self.max_fatigue = int(
                max_fatigue if max_fatigue is not None else 100 + (self.endurance * 1.5) + (self.level * 4))
        except Exception as e:
            UI.print_error(f"Error calculating derived stats: {e}")
            self.max_health = 100
            self.max_magicka = 50
            self.max_fatigue = 100

        # Current stats default to max if not specified
        self.current_health = int(current_health if current_health is not None else self.max_health)
        self.current_magicka = int(current_magicka if current_magicka is not None else self.max_magicka)
        self.current_fatigue = int(current_fatigue if current_fatigue is not None else self.max_fatigue)

        self.inventory = inventory if inventory is not None else []
        self.encumbrance_limit = 100 + (self.strength * 2)
        self.current_encumbrance = self.calculate_current_encumbrance()

        # Stat Effects
        self.effects: Dict[str, int] = {}  # Stores active effects and their modifiers

    def _calculate_next_level_exp(self, current_level: int) -> int:
        """Calculates the experience needed for the next level based on current level."""
        try:
            return int(100 * (current_level ** 1.7))  # Adjusted exponential scaling
        except Exception as e:
            UI.print_error(f"Error calculating next level experience: {e}")
            return 1000

    def calculate_current_encumbrance(self) -> float:
        """Calculates the total weight of items in the inventory."""
        return sum(item.weight for item in self.inventory if hasattr(item, 'weight'))

    def add_to_inventory(self, item: Item) -> bool:
        """Adds an item to the inventory if there's enough encumbrance capacity."""
        if not hasattr(item, 'weight'):
            UI.print_warning(
                f"Item {getattr(item, 'name', 'Unknown item')} has no weight attribute, cannot add to inventory.")
            return False
        if self.current_encumbrance + item.weight <= self.encumbrance_limit:
            self.inventory.append(item)
            self.current_encumbrance = self.calculate_current_encumbrance()
            return True
        else:
            UI.slow_print(f"Cannot carry {item.name}, you are too encumbered!")
            return False

    def remove_from_inventory(self, item: Item) -> bool:
        """Removes an item from the inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_encumbrance = self.calculate_current_encumbrance()
            return True
        return False

    def is_alive(self) -> bool:
        """Checks if the character is alive."""
        return self.current_health > 0

    def take_damage(self, amount: int) -> bool:
        """Applies damage to the character's health."""
        self.current_health = max(0, self.current_health - amount)
        return self.current_health == 0  # Returns True if dead

    def heal(self, amount: int) -> None:
        """Restores health to the character."""
        self.current_health = min(self.max_health, self.current_health + amount)

    def restore_magicka(self, amount: int) -> None:
        """Restores magicka to the character."""
        self.current_magicka = min(self.max_magicka, self.current_magicka + amount)

    def restore_fatigue(self, amount: int) -> None:
        """Restores fatigue (stamina) to the character."""
        self.current_fatigue = min(self.max_fatigue, self.current_fatigue + amount)

    def update_encumbrance(self) -> None:
        """Recalculates current encumbrance."""
        self.current_encumbrance = self.calculate_current_encumbrance()

    def level_up(self) -> None:
        """Increases character's level and recalculates derived stats."""
        self.level += 1
        UI.print_system_message(f"CONGRATULATIONS! You have reached LEVEL {self.level}!")

        attribute_increase = random.randint(3, 5)
        self.strength += attribute_increase
        self.intelligence += attribute_increase
        self.willpower += attribute_increase
        self.agility += attribute_increase
        self.speed += attribute_increase
        self.endurance += attribute_increase
        self.personality += attribute_increase
        self.luck += attribute_increase
        self.charisma += attribute_increase
        self.perception += attribute_increase

        try:
            self.max_health = int(100 + (self.endurance * 2) + (self.level * 5))
            self.max_magicka = int(50 + (self.intelligence * 1.5) + (self.level * 3))
            self.max_fatigue = int(100 + (self.endurance * 1.5) + (self.level * 4))

            self.current_health = self.max_health
            self.current_magicka = self.max_magicka
            self.current_fatigue = self.max_fatigue

            self.next_level_exp = self._calculate_next_level_exp(self.level)
            self.experience = 0
            UI.slow_print("Your attributes and skills have grown stronger!")
            UI.press_enter()
        except Exception as e:
            UI.print_error(f"Error during level up: {e}")

    def apply_effect(self, effect_name: str, modifier: int, duration: int) -> None:
        """Applies a temporary effect to a stat."""
        if effect_name in self.effects:
            self.effects[effect_name] += modifier
        else:
            self.effects[effect_name] = modifier

        # TODO: Implement duration and effect removal
        UI.print_system_message(f"{effect_name} modified by {modifier} (Duration: {duration})")


# --- Racial Modifiers --- (from original - unchanged)
RACES = {
    "nord": {"strength_mod": 10, "endurance_mod": 10, "frost_resist": 50, "two_handed_skill": 5, "block_skill": 5,
             "display_name": "Nord"},
    "imperial": {"personality_mod": 10, "luck_mod": 5, "restoration_skill": 5, "heavy_armor_skill": 5,
                 "display_name": "Imperial"},
    "breton": {"intelligence_mod": 10, "willpower_mod": 5, "magic_resist": 25, "conjuration_skill": 10,
               "display_name": "Breton"},
    "redguard": {"agility_mod": 10, "speed_mod": 10, "one_handed_skill": 10, "archery_skill": 5,
                 "display_name": "Redguard"},
    "dunmer": {"intelligence_mod": 5, "agility_mod": 5, "fire_resist": 50, "destruction_skill": 10, "sneak_skill": 5,
              "display_name": "Dark Elf / Dunmer"},
    "altmer": {"intelligence_mod": 15, "magicka_mod": 50, "illusion_skill": 10, "alteration_skill": 5,
              "display_name": "High Elf / Altmer"},
    "bosmer": {"agility_mod": 15, "archery_skill": 10, "sneak_skill": 5, "light_armor_skill": 5,
              "display_name": "Wood Elf / Bosmer"},
    "orc": {"strength_mod": 15, "endurance_mod": 5, "heavy_armor_skill": 10, "smithing_skill": 5,
            "display_name": "Orc / Orsimer"},
    "argonian": {"speed_mod": 10, "poison_resist": 75, "disease_resist": 50, "alteration_skill": 5,
                 "light_armor_skill": 5, "display_name": "Argonian"},
    "khajiit": {"agility_mod": 10, "luck_mod": 10, "sneak_skill": 10, "pickpocket_skill": 5,
                "display_name": "Khajiit"},
}

# --- Class Definitions --- (from original - unchanged)
CLASSES = {
    "warrior": {
        "name": "Warrior",
        "desc": "A master of arms, favoring strength and direct combat.",
        "subclasses": {
            "1": {"name": "Blademaster", "attributes": {"strength": 50, "endurance": 50},
                  "skills": {"one_handed": 20, "heavy_armor": 20}, "inventory": ["iron_sword", "hide_shield"],
                  "starting_spells": []},
            "2": {"name": "Berserker", "attributes": {"strength": 60, "speed": 40},
                  "skills": {"two_handed": 20, "light_armor": 15}, "inventory": ["iron_battleaxe", "hide_armor"],
                  "starting_spells": []},
            "3": {"name": "Spellblade", "attributes": {"strength": 45, "intelligence": 45},
                  "skills": {"one_handed": 15, "destruction": 15}, "inventory": ["steel_sword",
                                                                                     "apprentice_tome_flames"],
                  "starting_spells": ["flames"]},
            "4": {"name": "Knight", "attributes": {"endurance": 55, "personality": 40},
                  "skills": {"heavy_armor": 20, "block": 15}, "inventory": ["steel_plate_armor", "steel_shield"],
                  "starting_spells": []},
            "5": {"name": "Dragonslayer", "attributes": {"strength": 55, "willpower": 45},
                  "skills": {"two_handed": 25, "restoration": 10}, "inventory": ["dragonbone_greatsword",
                                                                                     "amulet_of_mara"],
                  "starting_spells": ["healing"]}
        }, "inventory": ["iron_sword", "hide_shield"], "starting_spells": []
    },
    "mage": {
        "name": "Mage", "desc": "A scholar of the arcane arts, wielding powerful spells.",
        "subclasses": {
            "1": {"name": "Sorcerer", "attributes": {"intelligence": 50, "willpower": 50},
                  "skills": {"destruction": 20, "alteration": 15}, "inventory": ["novice_robes",
                                                                                     "apprentice_tome_firebolt"],
                  "starting_spells": ["firebolt", "flames"]},
            "2": {"name": "Cleric", "attributes": {"willpower": 50, "personality": 50},
                  "skills": {"restoration": 20, "heavy_armor": 15}, "inventory": ["priest_robes",
                                                                                     "apprentice_tome_healing"],
                  "starting_spells": ["healing", "lesser_ward"]},
            "3": {"name": "Conjurer", "attributes": {"intelligence": 45, "willpower": 45},
                  "skills": {"conjuration": 20, "alteration": 10}, "inventory": ["apprentice_robes",
                                                                                     "apprentice_tome_conjure_familiar"],
                  "starting_spells": ["conjure_familiar"]},
            "4": {"name": "Illusionist", "attributes": {"intelligence": 40, "personality": 55},
                  "skills": {"illusion": 20, "sneak": 10}, "inventory": ["fine_clothes", "apprentice_tome_courage"],
                  "starting_spells": ["courage"]},
            "5": {"name": "Mystic", "attributes": {"intelligence": 55, "luck": 40},
                  "skills": {"mysticism": 20, "alchemy": 15}, "inventory": ["alchemist_robes", "scroll_of_soul_trap"],
                  "starting_spells": []}  # Mystics might rely on scrolls/alchemy
        }, "inventory": ["novice_robes", "apprentice_tome_firebolt"], "starting_spells": ["firebolt"]
    },
    "thief": {
        "name": "Thief", "desc": "A master of stealth and subterfuge, relying on cunning.",
        "subclasses": {
            "1": {"name": "Assassin", "attributes": {"agility": 50, "speed": 50},
                  "skills": {"sneak": 20, "one_handed": 15}, "inventory": ["leather_armor", "iron_dagger"],
                  "starting_spells": []},
            "2": {"name": "Nightblade", "attributes": {"agility": 40, "intelligence": 40},
                  "skills": {"sneak": 15, "illusion": 20}, "inventory": ["dark_brotherhood_robes", "iron_dagger"],
                  "starting_spells": ["courage"]},  # Example illusion spell
            "3": {"name": "Rogue", "attributes": {"agility": 45, "personality": 45},
                  "skills": {"pickpocket": 20, "speech": 15}, "inventory": ["fine_clothes", "lockpick"],
                  "starting_spells": []},
            "4": {"name": "Scout", "attributes": {"speed": 55, "endurance": 40},
                  "skills": {"light_armor": 20, "archery": 15}, "inventory": ["hide_armor", "hunting_bow"],
                  "starting_spells": []},
            "5": {"name": "Trickster", "attributes": {"luck": 50, "agility": 40},
                  "skills": {"alteration": 15, "speech": 20}, "inventory": ["jester_outfit", "scroll_of_calm"],
                  "starting_spells": []}
        }, "inventory": ["leather_armor", "iron_dagger"], "starting_spells": []
    },
    "adventurer": {
        "name": "Adventurer", "desc": "A versatile explorer, comfortable in many situations.",
        "subclasses": {
            "1": {"name": "Explorer", "attributes": {"endurance": 50, "luck": 50},
                  "skills": {"light_armor": 15, "speech": 15}, "inventory": ["leather_armor", "hunting_bow"],
                  "starting_spells": []},
            "2": {"name": "Bard", "attributes": {"personality": 50, "intelligence": 40},
                  "skills": {"speech": 20, "illusion": 15}, "inventory": ["fine_clothes", "lute"],
                  "starting_spells": ["courage"]},
            "3": {"name": "Survivalist", "attributes": {"endurance": 55, "strength": 40},
                  "skills": {"block": 15, "one_handed": 15}, "inventory": ["fur_armor", "iron_axe", "venison_steak"],
                  "starting_spells": []}
        }, "inventory": ["leather_armor", "hunting_bow"], "starting_spells": []
    }
}

# Player class has been moved to player.py