import random
from tags import TAGS
from ui import UI

class Item:
    """
    Base class for all items in the Skyrim Adventure game.
    Handles core attributes like name, category, material, and common behaviors.
    """
    def __init__(
        self,
        name: str,
        category: str,
        material: str,
        equipment_tag: str = None,
        base_damage: tuple = None,
        armor_rating: int = None,
        enchantment: str = None,
        durability: int = 100,
        properties: dict = None
    ):
        self.name = name
        self.category = category  # e.g., weapon, armor, potion, food, ingredient, jewelry, scroll, soul_gem
        self.material = material  # e.g., Iron, Steel, Ebony, etc.
        self.equipment_tag = equipment_tag or category
        self.base_damage = base_damage
        self.armor_rating = armor_rating
        self.enchantment = enchantment
        self.durability = durability
        self.max_durability = durability
        self.properties = properties.copy() if properties else {}
        # Derived attributes
        self.weight = self.calculate_weight()
        self.value = self.calculate_value()
        # Assign tags based on category
        self.tags = TAGS.get(self.category, [])
        # For consumables, set effect automatically
        if self.category in ["potion", "ingredient", "food"]:
            self._assign_consumable_effect()

    def __str__(self) -> str:
        parts = [f"{self.material} {self.name} [{self.category}]"]
        if self.enchantment:
            parts.append(f"Enchanted with {self.enchantment}")
        if self.category in ["weapon", "armor"]:
            parts.append(f"Durability: {self.durability}/{self.max_durability}")
        return ", ".join(parts)

    def calculate_weight(self) -> float:
        """
        Calculate weight based on material and base type.
        """
        weight_mult = {
            "Iron": 1.0, "Steel": 1.2, "Silver": 1.5, "Gold": 1.8,
            "Glass": 0.8, "Ebony": 2.0, "Dragonbone": 2.5,
            "Orcish": 1.3, "Dwarven": 1.4, "Elven": 0.9,
            "Falmer": 1.1, "Nordic": 1.6, "Leather": 0.7,
            "Hide": 0.6, "Fur": 0.5, "Linen": 0.4, "Paper": 0.3,
            "Daedric": 2.8, "Stalhrim": 1.9, "Chitin": 0.8
        }
        base_weights = {
            "Sword": 5.0, "Axe": 7.0, "Mace": 8.0,
            "Dagger": 2.0, "Bow": 4.0, "Staff": 6.0, "Greatsword": 9.0,
            "Warhammer": 12.0, "Battleaxe": 10.0, "Arrow": 0.1,
            "Helmet": 3.0, "Cuirass": 10.0, "Gauntlets": 2.0,
            "Greaves": 5.0, "Boots": 3.0, "Shield": 7.0,
            "Ring": 0.1, "Amulet": 0.2,
            "Bread": 0.5, "Cheese": 0.3, "Ale": 1.0, "Sweetroll": 0.4,
            "Cabbage": 0.6, "Potato": 0.7, "Venison": 1.2,
            "Potion": 0.2, "Ingredient": 0.1,
            "Scroll": 0.1, "Soul Gem": 0.3, "Lockpick": 0.05,
            "Book": 1.0, "Map": 0.2
        }
        material_mult = weight_mult.get(self.material, 1.0)
        type_weight = base_weights.get(self.name, 1.0)
        return round(material_mult * type_weight, 2)

    def calculate_value(self) -> int:
        """
        Calculate market value based on material rarity and base item value.
        """
        value_mult = {
            "Iron": 1.0, "Steel": 1.5, "Silver": 2.0,
            "Gold": 2.5, "Glass": 3.0, "Ebony": 4.0,
            "Dragonbone": 5.0, "Orcish": 1.8, "Dwarven": 2.2,
            "Elven": 2.5, "Falmer": 2.0, "Nordic": 2.8,
            "Leather": 0.8, "Hide": 0.7, "Fur": 0.6,
            "Linen": 1.2, "Paper": 1.5, "Daedric": 6.0,
            "Stalhrim": 4.5, "Chitin": 1.3
        }
        base_values = {
            "Sword": 50, "Axe": 60, "Mace": 70,
            "Dagger": 40, "Bow": 80, "Staff": 90, "Greatsword": 100,
            "Warhammer": 120, "Battleaxe": 110, "Arrow": 2,
            "Helmet": 40, "Cuirass": 120, "Gauntlets": 50,
            "Greaves": 70, "Boots": 50, "Shield": 80,
            "Ring": 100, "Amulet": 150,
            "Bread": 5, "Cheese": 8, "Ale": 12, "Sweetroll": 15,
            "Cabbage": 3, "Potato": 4, "Venison": 20,
            "Potion": 60, "Ingredient": 30,
            "Scroll": 100, "Soul Gem": 200, "Lockpick": 25,
            "Book": 80, "Map": 50
        }
        mult = value_mult.get(self.material, 1.0)
        base = base_values.get(self.name, 10)
        enchant_bonus = 1.5 if self.enchantment else 1.0
        return int(mult * base * enchant_bonus)

    def _assign_consumable_effect(self):
        """
        Internal: assign effect and magnitude for consumable items.
        """
        if self.category == "potion":
            pool = {
                "Potion of Minor Healing": {"effect": "restore_health", "magnitude": (10, 15)},
                "Potion of Healing": {"effect": "restore_health", "magnitude": (20, 30)},
                "Potion of Greater Healing": {"effect": "restore_health", "magnitude": (35, 45)},
                "Potion of Minor Magicka": {"effect": "restore_magicka", "magnitude": (10, 15)},
                "Potion of Magicka": {"effect": "restore_magicka", "magnitude": (20, 30)},
                "Potion of Greater Magicka": {"effect": "restore_magicka", "magnitude": (35, 45)},
                "Potion of Minor Stamina": {"effect": "restore_fatigue", "magnitude": (10, 15)},
                "Potion of Stamina": {"effect": "restore_fatigue", "magnitude": (20, 30)},
                "Potion of Greater Stamina": {"effect": "restore_fatigue", "magnitude": (35, 45)},
                "Potion of Resist Fire": {"effect": "resist_fire", "magnitude": (20, 30)},
                "Potion of Resist Frost": {"effect": "resist_frost", "magnitude": (20, 30)},
                "Potion of Resist Shock": {"effect": "resist_shock", "magnitude": (20, 30)},
                "Potion of Cure Poison": {"effect": "cure_poison", "magnitude": 0}
            }
        elif self.category == "ingredient":
            pool = {
                "Blue Mountain Flower": {"effect": "restore_health", "magnitude": (2, 4)},
                "Imp Stool": {"effect": "damage_health", "magnitude": (1, 3)},
                "Blisterwort": {"effect": "fortify_strength", "magnitude": (2, 5)},
                "Deathbell": {"effect": "damage_speed", "magnitude": (2, 4)},
                "Nightshade": {"effect": "damage_magicka", "magnitude": (3, 5)},
                "Jazbay Grapes": {"effect": "restore_magicka", "magnitude": (3, 7)},
                "Garlic": {"effect": "resist_poison", "magnitude": (5, 10)}
            }
        elif self.category == "food":
            pool = {
                "Bread": {"effect": "restore_fatigue", "magnitude": (5, 8)},
                "Cheese Wheel": {"effect": "restore_fatigue", "magnitude": (10, 15)},
                "Ale": {"effect": "restore_fatigue", "magnitude": (10, 12)},
                "Sweetroll": {"effect": "restore_fatigue", "magnitude": (12, 15)},
                "Cabbage": {"effect": "restore_fatigue", "magnitude": (3, 5)},
                "Potato": {"effect": "restore_fatigue", "magnitude": (4, 6)},
                "Venison Steak": {"effect": "restore_fatigue", "magnitude": (15, 20)},
                "Apple": {"effect": "restore_health", "magnitude": (3, 5)}
            }
        else:
            return
        choice_name = random.choice(list(pool.keys()))
        self.name = choice_name #Overwrite the name with the specific item
        self.properties["effect"] = pool[choice_name]["effect"]
        min_mag, max_mag = pool[choice_name]["magnitude"]
        self.properties["magnitude"] = random.randint(min_mag, max_mag)

    def use(self, player) -> None:
        """
        Apply the item's primary effect to the player.
        Consumes or applies status depending on category.
        """
        if self.category in ["potion", "ingredient", "food"] and self.properties:
            eff = self.properties.get("effect")
            mag = self.properties.get("magnitude", 0)
            skill_bonus = player.skills.get("alchemy", 0) / 100 if self.category != "food" else 0
            total_mag = int(mag * (1 + skill_bonus))
            if eff == "restore_health":
                player.stats.heal(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} health.")
            elif eff == "restore_magicka":
                player.stats.regenerate_magicka(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} magicka.")
            elif eff == "restore_fatigue":
                player.stats.regenerate_fatigue(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} stamina.")
            elif eff == "cure_poison":
                player.stats.clear_status("poison")
                UI.slow_print(f"You consume the {self.name}, curing poison.")
            elif eff == "resist_fire":
                player.stats.apply_resistance("fire", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% fire resistance.")
            elif eff == "resist_frost":
                player.stats.apply_resistance("frost", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% frost resistance.")
            elif eff == "resist_shock":
                player.stats.apply_resistance("shock", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% shock resistance.")
            elif eff == "fortify_strength":
                player.stats.fortify_attribute("strength", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, fortifying strength by {total_mag}.")
            elif eff == "damage_health":
                player.stats.take_damage(total_mag, "poison")
                UI.slow_print(f"You consume the {self.name}, taking {total_mag} poison damage!")
            elif eff == "damage_speed":
                player.stats.apply_debuff("speed", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, reducing speed by {total_mag}!")
            elif eff == "damage_magicka":
                player.stats.apply_debuff("magicka", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, reducing magicka by {total_mag}!")
            player.inventory.remove(self)
            player.improve_skill("alchemy", 1)
        elif self.category == "weapon":
            UI.slow_print(f"You swing the {self.name} dealing damage.")
        elif self.category == "armor":
            UI.slow_print(f"You equip the {self.name}, increasing defense.")
        elif self.category == "scroll":
            UI.slow_print(f"You read the {self.name} and cast a spell!") #Implement spell casting later
        else:
            UI.slow_print(f"The {self.name} cannot be used directly.")

    def damage(self, amount: int) -> None:
        """
        Apply durability damage to weapon or armor.
        """
        if self.category in ["weapon", "armor"]:
            self.durability = max(0, self.durability - amount)
            if self.durability == 0:
                UI.slow_print(f"Your {self.name} has broken!")
                if self.category == "weapon":
                    self.base_damage = (1, 1)
                else:
                    self.armor_rating = 0

    def repair(self, player) -> None:
        """
        Repair an item based on the player's armorer skill.
        """
        skill = player.skills.get("armorer", 0)
        amt = max(1, int(skill / 5))
        self.durability = min(self.max_durability, self.durability + amt)
        UI.slow_print(f"You repair {self.name} to {self.durability}/{self.max_durability} durability.")
        player.improve_skill("armorer", 1)

    def get_description(self) -> str:
        """
        Returns a detailed description for UI display.
        """
        desc = [f"{self.material} {self.name}:"]
        desc.append(f" Value: {self.value} gold, Weight: {self.weight}")
        if self.category in ["weapon", "armor"]:
            desc.append(f" Stats: Damage {self.base_damage}" if self.category=="weapon" else f" Armor {self.armor_rating}")
        if self.enchantment:
            desc.append(f" Enchantment: {self.enchantment}")
        if "effect" in self.properties:
            desc.append(f" Effect: {self.properties['effect']} ({self.properties.get('magnitude', '')})")
        return " | ".join(desc)

# Helper lists for random generation
MATERIALS = ["Iron", "Steel", "Silver", "Gold", "Glass", "Ebony", "Dragonbone",
             "Orcish", "Dwarven", "Elven", "Falmer", "Nordic", "Leather",
             "Hide", "Fur", "Chitin", "Daedric", "Stalhrim"]
WEAPONS = ["Sword", "Axe", "Mace", "Dagger", "Bow", "Staff", "Greatsword",
           "Warhammer", "Battleaxe"]
ARMORS = ["Helmet", "Cuirass", "Gauntlets", "Greaves", "Boots", "Shield"]
JEWELRY = ["Ring", "Amulet"]
FOODS = ["Bread", "Cheese Wheel", "Ale", "Sweetroll", "Cabbage", "Potato", "Venison Steak", "Apple"]
POTIONS = ["Potion of Minor Healing", "Potion of Healing", "Potion of Greater Healing",
           "Potion of Minor Magicka", "Potion of Magicka", "Potion of Greater Magicka",
           "Potion of Minor Stamina", "Potion of Stamina", "Potion of Greater Stamina",
           "Potion of Resist Fire", "Potion of Resist Frost", "Potion of Resist Shock",
           "Potion of Cure Poison"]
INGREDIENTS = ["Blue Mountain Flower", "Imp Stool", "Blisterwort", "Deathbell",
               "Nightshade", "Jazbay Grapes", "Garlic"]
SCROLLS = ["Scroll of Fireball", "Scroll of Frost", "Scroll of Healing",
           "Scroll of Courage", "Scroll of Soul Trap"]
SOUL_GEMS = ["Petty Soul Gem", "Lesser Soul Gem", "Common Soul Gem", "Greater Soul Gem",
             "Grand Soul Gem", "Black Soul Gem"]
MISC = ["Lockpick", "Book", "Map"] #Added misc items

def generate_random_item(category: str, level: int = 1) -> Item:
    """
    Factory function to generate a random item for loot or shop.
    """
    material = random.choice(MATERIALS)
    enchant = random.choice([None, "Fire", "Frost", "Shock", "Poison"]) if category in ["weapon", "armor", "jewelry"] else None
    if category == "weapon":
        name = random.choice(WEAPONS)
        dmg = (random.randint(1, 3)+level, random.randint(4, 6)+level)
        item = Item(name, category, material, equipment_tag="weapon", base_damage=dmg, enchantment=enchant)
        item.properties.update({"damage": dmg})
    elif category == "armor":
        name = random.choice(ARMORS)
        ar = random.randint(2, 4) + level
        item = Item(name, category, material, equipment_tag="armor", armor_rating=ar, enchantment=enchant)
        item.properties.update({"armor": ar})
    elif category == "jewelry":
        name = random.choice(JEWELRY)
        item = Item(name, category, material, equipment_tag="jewelry", enchantment=enchant)
        item.properties.update({"effect": enchant or "none"})
    elif category == "food":
        name = random.choice(FOODS)
        item = Item(name, category, material)
        # consumable effect assigned in __init__
    elif category == "potion":
        name = random.choice(POTIONS)
        item = Item(name, category, material)
    elif category == "ingredient":
        name = random.choice(INGREDIENTS)
        item = Item(name, category, material)
    elif category == "scroll":
        name = random.choice(SCROLLS)
        item = Item(name, category, material)
    elif category == "soul_gem":
        name = random.choice(SOUL_GEMS)
        item = Item(name, category, material)
    elif category == "misc":
        name = random.choice(MISC)
        item = Item(name, category, material)
    else:
        return Item("Unknown", category, material)
    return item