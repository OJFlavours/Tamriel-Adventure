import random
from quests import QuestLog # Import QuestLog

class Stats:
    """
    Encapsulates player or NPC stats, attributes, and derived combat values for Skyrim Adventure.
    """
    def __init__(self,
                 strength=40, intelligence=40, willpower=40, agility=40, speed=40,
                 endurance=40, personality=40, luck=40,
                 max_health=None, max_magicka=None, max_fatigue=None,
                 current_health=None, current_magicka=None, current_fatigue=None,
                 poison_resist=0, magic_resist=0, frost_resist=0,
                 shock_resist=0, fire_resist=0,
                 inventory=None,
                 gold=0, level=1):
        # Attributes
        self.strength = strength
        self.intelligence = intelligence
        self.willpower = willpower
        self.agility = agility
        self.speed = speed
        self.endurance = endurance
        self.personality = personality
        self.luck = luck

        self.level = level
        self.gold = gold

        # Resistances
        self.poison_resist = poison_resist
        self.magic_resist = magic_resist
        self.frost_resist = frost_resist
        self.shock_resist = shock_resist
        self.fire_resist = fire_resist

        # Core stats (set after attributes)
        self.max_health = max_health if max_health is not None else 100 + (self.endurance * 2)
        self.max_magicka = max_magicka if max_magicka is not None else 50 + (self.intelligence * 1.5)
        self.max_fatigue = max_fatigue if max_fatigue is not None else 100 + (self.endurance * 1.5)

        self.current_health = current_health if current_health is not None else self.max_health
        self.current_magicka = current_magicka if current_magicka is not None else self.max_magicka
        self.current_fatigue = current_fatigue if current_fatigue is not None else self.max_fatigue

        # Inventory and Encumbrance (moved from Player to Stats for better encapsulation)
        self.inventory = inventory if inventory is not None else []
        self.encumbrance_limit = 100 + (self.strength * 2) # Base limit + strength bonus
        self.current_encumbrance = self.calculate_current_encumbrance()

    def calculate_current_encumbrance(self):
        """Calculates the total weight of items in the inventory."""
        return sum(item.weight for item in self.inventory)

    def add_to_inventory(self, item):
        """Adds an item to the inventory if encumbrance limit is not exceeded."""
        if self.current_encumbrance + item.weight <= self.encumbrance_limit:
            self.inventory.append(item)
            self.current_encumbrance = self.calculate_current_encumbrance()
            return True
        return False

    def remove_from_inventory(self, item):
        """Removes an item from the inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_encumbrance = self.calculate_current_encumbrance()
            return True
        return False

    def is_alive(self):
        """Checks if the character is alive."""
        return self.current_health > 0

    def take_damage(self, amount):
        """Reduces current health by the given amount."""
        self.current_health = max(0, self.current_health - amount)
        return self.current_health == 0

    def heal(self, amount):
        """Increases current health by the given amount, up to max health."""
        self.current_health = min(self.max_health, self.current_health + amount)

    def restore_magicka(self, amount):
        """Increases current magicka by the given amount, up to max magicka."""
        self.current_magicka = min(self.max_magicka, self.current_magicka + amount)

    def restore_fatigue(self, amount):
        """Increases current fatigue by the given amount, up to max fatigue."""
        self.current_fatigue = min(self.max_fatigue, self.current_fatigue + amount)

    def update_encumbrance(self):
        """Recalculates encumbrance after equipment changes."""
        self.current_encumbrance = self.calculate_current_encumbrance()


RACES = {
    "nord": {"strength_mod": 10, "endurance_mod": 10, "frost_resist": 50},
    "imperial": {"personality_mod": 10, "luck_mod": 5},
    "breton": {"intelligence_mod": 10, "magic_resist": 25},
    "redguard": {"agility_mod": 10, "speed_mod": 10},
    "dunmer": {"intelligence_mod": 5, "agility_mod": 5, "fire_resist": 50},
    "altmer": {"intelligence_mod": 15, "magicka_mod": 50},
    "bosmer": {"agility_mod": 15, "archery_skill": 10},
    "orc": {"strength_mod": 15, "endurance_mod": 5},
    "argonian": {"speed_mod": 10, "poison_resist": 50},
    "khajiit": {"agility_mod": 10, "luck_mod": 10},
}

CLASSES = {
    "warrior": {
        "name": "Warrior",
        "desc": "A master of arms, favoring strength and direct combat.",
        "subclasses": {
            "1": {"name": "Blademaster", "attributes": {"strength": 50, "endurance": 50}, "skills": {"one_handed": 20, "heavy_armor": 20}, "inventory": ["iron_sword", "hide_shield"]},
            "2": {"name": "Berserker", "attributes": {"strength": 60, "speed": 40}, "skills": {"two_handed": 20, "light_armor": 15}, "inventory": ["iron_battleaxe", "hide_armor"]},
            "3": {"name": "Spellblade", "attributes": {"strength": 45, "intelligence": 45}, "skills": {"one_handed": 15, "destruction": 15}, "inventory": ["steel_sword", "apprentice_tome_flames"]},
            "4": {"name": "Knight", "attributes": {"endurance": 55, "personality": 40}, "skills": {"heavy_armor": 20, "block": 15}, "inventory": ["steel_plate_armor", "steel_shield"]},
            "5": {"name": "Dragonslayer", "attributes": {"strength": 55, "willpower": 45}, "skills": {"two_handed": 25, "restoration": 10}, "inventory": ["dragonbone_greatsword", "amulet_of_mara"]}
        },
        "inventory": ["iron_sword", "hide_shield"] # Default inventory for class
    },
    "mage": {
        "name": "Mage",
        "desc": "A scholar of the arcane arts, wielding powerful spells.",
        "subclasses": {
            "1": {"name": "Sorcerer", "attributes": {"intelligence": 50, "willpower": 50}, "skills": {"destruction": 20, "alteration": 15}, "inventory": ["novice_robes", "apprentice_tome_firebolt"]},
            "2": {"name": "Cleric", "attributes": {"willpower": 50, "personality": 50}, "skills": {"restoration": 20, "heavy_armor": 15}, "inventory": ["priest_robes", "apprentice_tome_healing"]},
            "3": {"name": "Conjurer", "attributes": {"intelligence": 45, "willpower": 45}, "skills": {"conjuration": 20, "alteration": 10}, "inventory": ["apprentice_robes", "apprentice_tome_conjure_familiar"]},
            "4": {"name": "Illusionist", "attributes": {"intelligence": 40, "personality": 55}, "skills": {"illusion": 20, "sneak": 10}, "inventory": ["fine_clothes", "apprentice_tome_courage"]},
            "5": {"name": "Mystic", "attributes": {"intelligence": 55, "luck": 40}, "skills": {"mysticism": 20, "alchemy": 15}, "inventory": ["alchemist_robes", "scroll_of_soul_trap"]}
        },
        "inventory": ["novice_robes", "apprentice_tome_firebolt"] # Default inventory for class
    },
    "thief": {
        "name": "Thief",
        "desc": "A master of stealth and subterfuge, relying on cunning.",
        "subclasses": {
            "1": {"name": "Assassin", "attributes": {"agility": 50, "speed": 50}, "skills": {"sneak": 20, "one_handed": 15}, "inventory": ["leather_armor", "iron_dagger"]},
            "2": {"name": "Nightblade", "attributes": {"agility": 40, "intelligence": 40}, "skills": {"sneak": 15, "illusion": 20}, "inventory": ["dark_brotherhood_robes", "iron_dagger"]},
            "3": {"name": "Rogue", "attributes": {"agility": 45, "personality": 45}, "skills": {"pickpocket": 20, "speech": 15}, "inventory": ["fine_clothes", "lockpick"]},
            "4": {"name": "Scout", "attributes": {"speed": 55, "endurance": 40}, "skills": {"light_armor": 20, "archery": 15}, "inventory": ["hide_armor", "hunting_bow"]},
            "5": {"name": "Trickster", "attributes": {"luck": 50, "agility": 40}, "skills": {"alteration": 15, "speech": 20}, "inventory": ["jester_outfit", "scroll_of_calm"]}
        },
        "inventory": ["leather_armor", "iron_dagger"] # Default inventory for class
    },
    "adventurer": {
        "name": "Adventurer",
        "desc": "A versatile explorer, comfortable in many situations.",
        "subclasses": {
            "1": {"name": "Explorer", "attributes": {"endurance": 50, "luck": 50}, "skills": {"light_armor": 15, "speech": 15}, "inventory": ["leather_armor", "hunting_bow"]},
            "2": {"name": "Bard", "attributes": {"personality": 50, "intelligence": 40}, "skills": {"speech": 20, "illusion": 15}, "inventory": ["fine_clothes", "lute"]},
            "3": {"name": "Survivalist", "attributes": {"endurance": 55, "strength": 40}, "skills": {"block": 15, "one_handed": 15}, "inventory": ["fur_armor", "iron_axe", "venison_steak"]}
        },
        "inventory": ["leather_armor", "hunting_bow"] # Default inventory for class
    }
}

class Player:
    def __init__(self, name, race, subclass, stats, skills):
        self.name = name
        self.race = race
        self.subclass = subclass
        self.stats = stats
        self.skills = skills

    def equip_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.equipment.append(item)
            UI.slow_print(f"{item.name} has been equipped.")
        else:
            UI.slow_print(f"{item.name} is not in your inventory.")

    def unequip_item(self, item):
        if item in self.equipment:
            self.equipment.remove(item)
            self.inventory.append(item)
            UI.slow_print(f"{item.name} has been unequipped.")
        else:
            UI.slow_print(f"{item.name} is not equipped.")

    def examine_item(self, item):
        UI.slow_print(item.get_description())

    def use_item(self, item):
        if item.category in ["potion", "food", "scroll"]:  # Expand categories as needed
            item.use(self)  # Assuming `use` is already implemented in the Item class
        else:
            UI.slow_print(f"{item.name} cannot be used directly.")

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            UI.slow_print(f"You dropped {item.name}.")
        else:
            UI.slow_print(f"{item.name} is not in your inventory.")

    def sort_inventory(self, key="name"):
        self.inventory.sort(key=lambda item: getattr(item, key, "").lower())
        UI.slow_print(f"Inventory sorted by {key}.")

    def inspect_equipped_items(self):
        if not self.equipment:
            UI.slow_print("You have no items equipped.")
            return
        for item in self.equipment:
            UI.print_info(f"{item.name} - {item.get_description()}")