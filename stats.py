import random

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
        self.max_health = max_health if max_health is not None else self._calculate_max_health()
        self.max_magicka = max_magicka if max_magicka is not None else self._calculate_max_magicka()
        self.max_fatigue = max_fatigue if max_fatigue is not None else self._calculate_max_fatigue()
        self.current_health = current_health if current_health is not None else self.max_health
        self.current_magicka = current_magicka if current_magicka is not None else self.max_magicka
        self.current_fatigue = current_fatigue if current_fatigue is not None else self.max_fatigue

        # Encumbrance system
        self.encumbrance_limit = self._calculate_encumbrance_limit()
        self.current_encumbrance = 0  # Will be updated after inventory is set

        # Combat-related stats
        self.weapon_damage_min = 1
        self.weapon_damage_max = 4
        self.critical_multiplier = 1.5
        self.block_chance = 0.10
        self.dodge_chance = 0.07

        # For tracking
        self.inventory = inventory or []
        self.update_encumbrance()  # Initialize encumbrance with inventory

    def _calculate_max_health(self):
        return 50 + self.endurance * 2 + self.strength

    def _calculate_max_magicka(self):
        return 40 + self.intelligence * 2 + self.willpower

    def _calculate_max_fatigue(self):
        return 40 + self.strength + self.willpower + self.agility + self.endurance

    def _calculate_encumbrance_limit(self):
        # Standard Elder Scrolls logic: e.g., Strength x 5 + Endurance x 2
        return int(self.strength * 5 + self.endurance * 2)

    def update_encumbrance(self):
        """Updates current_encumbrance to reflect the inventory contents."""
        self.current_encumbrance = sum(getattr(item, "weight", 0) for item in self.inventory)

    def can_carry(self, weight):
        return (self.current_encumbrance + weight) <= self.encumbrance_limit

    def add_to_inventory(self, item):
        """Adds an item if it can be carried, and updates encumbrance."""
        if self.can_carry(getattr(item, "weight", 0)) :
            self.inventory.append(item)
            self.update_encumbrance()
            return True
        return False

    def remove_from_inventory(self, item):
        """Removes item and updates encumbrance."""
        if item in self.inventory:
            self.inventory.remove(item)
            self.update_encumbrance()
            return True
        return False

    def heal(self, amount):
        self.current_health = min(self.current_health + amount, self.max_health)

    def regenerate_magicka(self, amount):
        self.current_magicka = min(self.current_magicka + amount, self.max_magicka)

    def regenerate_fatigue(self, amount):
        self.current_fatigue = min(self.current_fatigue + amount, self.max_fatigue)

    def take_damage(self, amount, damage_type="physical"):
        self.current_health = max(self.current_health - int(amount), 0)

    def is_alive(self):
        return self.current_health > 0

    def roll_to_hit(self, skill, defender_stats):
        # Simple formula, you can expand this for realism
        hit_chance = 60 + (skill - 15) * 2 + (self.agility - defender_stats.agility) * 0.5
        hit_chance = max(min(hit_chance, 99), 5)
        return random.randint(1, 100) <= hit_chance

    def roll_spell_success(self, skill):
        # Simple magicka success check
        base_chance = 60 + (skill - 15) * 2 + (self.intelligence - 40) * 0.5
        base_chance = max(min(base_chance, 99), 10)
        return random.randint(1, 100) <= base_chance

    def roll_critical(self):
        # Critical based on luck and agility
        crit_chance = 3 + int((self.luck + self.agility) / 40)
        return random.randint(1, 100) <= crit_chance

    def update_combat_stats(self):
        # Use to update weapon/armor bonuses if desired
        pass

    def __str__(self):
        return (f"HP:{self.current_health}/{self.max_health} | MP:{self.current_magicka}/{self.max_magicka} | "
                f"Fatigue:{self.current_fatigue}/{self.max_fatigue} | Encumbrance:{self.current_encumbrance}/{self.encumbrance_limit} | "
                f"STR:{self.strength} END:{self.endurance} INT:{self.intelligence} AGI:{self.agility} SPD:{self.speed} PER:{self.personality} LUCK:{self.luck}")

# Example Player wrapper
class Player:
    def __init__(self, name, race, character_class, level=1, attributes=None, skills=None, inventory=None, equipment=None):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        # Initialize attributes with default speed if not provided
        self.attributes = attributes or {"speed": 40, "strength": 40, "agility": 40}  # Include other base attributes
        self.skills = skills or {}
        self.stats = Stats(level=level, strength=self.attributes["strength"], agility=self.attributes["agility"]) # Pass attributes to stats
        self.inventory = inventory or []
        self.equipment = equipment or [] # Initialize equipment
        self.quest_log = []
        self.combat = None

    def is_alive(self):
        return self.stats.is_alive()

    def add_item(self, item):
        if self.stats.add_to_inventory(item):
            return True
        else:
            print("You are over-encumbered!")
            return False

    def remove_item(self, item):
        return self.stats.remove_from_inventory(item)

    def improve_skill(self, skill, amt=1):
        if skill in self.skills:
            self.skills[skill] += amt
        else:
            self.skills[skill] = 15 + amt

    def equip_item(self, item):
        """Equips an item, adding it to the equipment list."""
        if item in self.inventory:
            self.equipment.append(item)
            self.inventory.remove(item)
            self.stats.update_encumbrance()  # Update encumbrance after equipping
            return True
        return False

    def unequip_item(self, item):
        """Unequips an item, adding it back to the inventory."""
        if item in self.equipment:
            self.equipment.remove(item)
            self.inventory.append(item)
            self.stats.update_encumbrance()  # Update encumbrance after unequipping
            return True
        return False

    def __str__(self):
        return f"{self.name} the {self.race} {self.character_class}, Level {self.level}"