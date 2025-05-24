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
            "Falmer": 1.1, "Nordic": 1.6
        }
        base_weights = {
            "Sword": 5.0, "Axe": 7.0, "Mace": 8.0,
            "Dagger": 2.0, "Bow": 4.0, "Staff": 6.0,
            "Helmet": 3.0, "Cuirass": 10.0,
            "Gauntlets": 2.0, "Greaves": 5.0,
            "Boots": 3.0, "Shield": 7.0,
            "Ring": 0.1, "Amulet": 0.2,
            "Bread": 0.5, "Cheese": 0.3, "Ale": 1.0,
            "Potion": 0.2, "Ingredient": 0.1,
            "Scroll": 0.1, "Soul Gem": 0.3
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
            "Elven": 2.5, "Falmer": 2.0, "Nordic": 2.8
        }
        base_values = {
            "Sword": 50, "Axe": 60, "Mace": 70,
            "Dagger": 40, "Bow": 80, "Staff": 90,
            "Helmet": 40, "Cuirass": 120, "Gauntlets": 50,
            "Greaves": 70, "Boots": 50, "Shield": 80,
            "Ring": 100, "Amulet": 150,
            "Bread": 5, "Cheese": 8, "Ale": 12,
            "Potion": 60, "Ingredient": 30,
            "Scroll": 100, "Soul Gem": 200
        }
        mult = value_mult.get(self.material, 1.0)
        base = base_values.get(self.name, 10)
        return int(mult * base)

    def _assign_consumable_effect(self):
        """
        Internal: assign effect and magnitude for consumable items.
        """
        if self.category == "potion":
            pool = {
                "Health Potion": {"effect": "restore_health", "magnitude": 25},
                "Magicka Potion": {"effect": "restore_magicka", "magnitude": 25},
                "Stamina Potion": {"effect": "restore_fatigue", "magnitude": 25},
                "Antidote": {"effect": "cure_poison", "magnitude": 0}
            }
        elif self.category == "ingredient":
            pool = {
                "Healing Herb": {"effect": "restore_health", "magnitude": 10},
                "Wormwood": {"effect": "damage_health", "magnitude": 5},
                "Fortify Root": {"effect": "fortify_strength", "magnitude": 5}
            }
        elif self.category == "food":
            pool = {
                "Bread": {"effect": "restore_fatigue", "magnitude": 15},
                "Cheese": {"effect": "restore_fatigue", "magnitude": 10},
                "Ale": {"effect": "restore_fatigue", "magnitude": 20}
            }
        else:
            return
        choice_name = random.choice(list(pool.keys()))
        self.properties["effect"] = pool[choice_name]["effect"]
        self.properties["magnitude"] = pool[choice_name]["magnitude"]

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
            player.inventory.remove(self)
            player.improve_skill("alchemy", 1)
        elif self.category == "weapon":
            UI.slow_print(f"You swing the {self.name} dealing damage.")
        elif self.category == "armor":
            UI.slow_print(f"You equip the {self.name}, increasing defense.")
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
             "Orcish", "Dwarven", "Elven", "Falmer", "Nordic"]
WEAPONS = ["Sword", "Axe", "Mace", "Dagger", "Bow", "Staff"]
ARMORS = ["Helmet", "Cuirass", "Gauntlets", "Greaves", "Boots", "Shield"]
JEWELRY = ["Ring", "Amulet"]
FOODS = ["Bread", "Cheese", "Ale"]
POTIONS = ["Health Potion", "Magicka Potion", "Stamina Potion", "Antidote"]
INGREDIENTS = ["Healing Herb", "Wormwood", "Fortify Root"]
SCROLLS = ["Scroll of Fireball", "Scroll of Frost", "Scroll of Healing"]
SOUL_GEMS = ["Petty Soul Gem", "Lesser Soul Gem", "Common Soul Gem", "Greater Soul Gem"]


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
    else:
        return Item("Unknown", category, material)
    return item
