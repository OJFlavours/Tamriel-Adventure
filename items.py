import random
from ui import UI
import tags
import flavor

INITIAL_INVENTORY_MAPPING = {
    "iron_sword": {"category": "weapon", "name": "Iron Sword", "material": "Iron", "base_damage": (3, 7)},
    "hide_shield": {"category": "armor", "name": "Hide Shield", "material": "Hide", "armor_rating": 5},
    "iron_battleaxe": {"category": "weapon", "name": "Iron Battleaxe", "material": "Iron", "base_damage": (5, 10)},
    "hide_armor": {"category": "armor", "name": "Hide Cuirass", "material": "Hide", "armor_rating": 8},
    "steel_sword": {"category": "weapon", "name": "Steel Sword", "material": "Steel", "base_damage": (4, 8)},
    "apprentice_tome_flames": {"category": "scroll", "name": "Apprentice Tome of Flames", "material": "Paper"},
    "steel_plate_armor": {"category": "armor", "name": "Steel Plate Cuirass", "material": "Steel", "armor_rating": 15},
    "steel_shield": {"category": "armor", "name": "Steel Shield", "material": "Steel", "armor_rating": 10},
    "dragonbone_greatsword": {"category": "weapon", "name": "Dragonbone Greatsword", "material": "Dragonbone", "base_damage": (15, 25)},
    "amulet_of_mara": {"category": "jewelry", "name": "Amulet of Mara", "material": "Gold"},
    "novice_robes": {"category": "armor", "name": "Novice Robes", "material": "Linen", "armor_rating": 2},
    "apprentice_tome_firebolt": {"category": "scroll", "name": "Apprentice Tome of Firebolt", "material": "Paper"},
    "priest_robes": {"category": "armor", "name": "Priest Robes", "material": "Linen", "armor_rating": 3},
    "apprentice_tome_healing": {"category": "scroll", "name": "Apprentice Tome of Healing", "material": "Paper"},
    "apprentice_robes": {"category": "armor", "name": "Apprentice Robes", "material": "Linen", "armor_rating": 4},
    "apprentice_tome_conjure_familiar": {"category": "scroll", "name": "Apprentice Tome of Conjure Familiar", "material": "Paper"},
    "dark_brotherhood_robes": {"category": "armor", "name": "Dark Brotherhood Robes", "material": "Leather", "armor_rating": 6},
    "iron_dagger": {"category": "weapon", "name": "Iron Dagger", "material": "Iron", "base_damage": (2, 4)},
    "fine_clothes": {"category": "armor", "name": "Fine Clothes", "material": "Linen", "armor_rating": 1},
    "lockpick": {"category": "misc", "name": "Lockpick", "material": "Iron"},
    "hunting_bow": {"category": "weapon", "name": "Hunting Bow", "material": "Wood", "base_damage": (4, 8)},
    "lute": {"category": "misc", "name": "Lute", "material": "Wood"},
    "fur_armor": {"category": "armor", "name": "Fur Armor", "material": "Fur", "armor_rating": 7},
    "iron_axe": {"category": "weapon", "name": "Iron Axe", "material": "Iron", "base_damage": (4, 9)},
    "venison_steak": {"category": "food", "name": "Venison Steak", "material": "Common"},
    "alchemist_robes": {"category": "armor", "name": "Alchemist Robes", "material": "Linen", "armor_rating": 3},
    "scroll_of_soul_trap": {"category": "scroll", "name": "Scroll of Soul Trap", "material": "Paper"},
    "jester_outfit": {"category": "armor", "name": "Jester Outfit", "material": "Linen", "armor_rating": 2},
    "scroll_of_calm": {"category": "scroll", "name": "Scroll of Calm", "material": "Paper"},
}

MATERIALS = ["Iron", "Steel", "Silver", "Gold", "Glass", "Ebony", "Dragonbone",
             "Orcish", "Dwarven", "Elven", "Falmer", "Nordic", "Leather",
             "Hide", "Fur", "Chitin", "Daedric", "Stalhrim", "Wood", "Paper", "Linen", "Common"]
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
MISC = ["Lockpick", "Book", "Map", "Lute"]

class Item:
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
        self.category = category
        self.material = material
        self.equipment_tag = equipment_tag or category
        self.base_damage = base_damage
        self.armor_rating = armor_rating
        self.enchantment = enchantment
        self.durability = durability
        self.max_durability = durability
        self.properties = properties.copy() if properties else {}
        self.tags = {}
        self.add_tag("item", "type", category)
        self.add_tag("item", "material", material)
        self.weight = self.calculate_weight()
        self.value = self.calculate_value()
        if self.category in ["potion", "ingredient", "food"]:
            self._assign_consumable_effect()

    def add_tag(self, tag_category, tag_type, tag):
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag

    def calculate_weight(self) -> float:
        weight_mult = {
            "Iron": 1.0, "Steel": 1.2, "Gold": 1.8, "Glass": 0.8, "Ebony": 2.0, "Daedric": 2.8
        }
        base_weights = {
            "Sword": 5.0, "Helmet": 3.0, "Cuirass": 10.0
        }
        material_mult = weight_mult.get(self.material, 1.0)
        type_weight = base_weights.get(self.name.split(" ")[-1], 1.0)
        return round(material_mult * type_weight, 2)

    def calculate_value(self) -> int:
        value_mult = {
            "Iron": 1.0, "Steel": 1.5, "Gold": 2.5, "Glass": 3.0, "Ebony": 4.0, "Daedric": 6.0
        }
        base_values = {
            "Sword": 50, "Helmet": 40, "Cuirass": 120
        }
        mult = value_mult.get(self.material, 1.0)
        type_value = base_values.get(self.name.split(" ")[-1], 10)
        enchant_bonus = 1.5 if self.enchantment else 1.0
        return int(mult * type_value * enchant_bonus)

    def _assign_consumable_effect(self):
        pool = {}
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

        if self.name in pool:
            chosen_effect_data = pool[self.name]
        else:
            chosen_name = random.choice(list(pool.keys()))
            self.name = chosen_name
            chosen_effect_data = pool[chosen_name]

        self.properties["effect"] = chosen_effect_data["effect"]
        magnitude = chosen_effect_data["magnitude"]
        if isinstance(magnitude, tuple):
            min_mag, max_mag = magnitude
            self.properties["magnitude"] = random.randint(min_mag, max_mag)
        else:
            self.properties["magnitude"] = magnitude

    def use(self, player) -> None:
        if self.category in ["potion", "ingredient", "food"] and self.properties:
            eff = self.properties.get("effect")
            mag = self.properties.get("magnitude", 0)
            skill_bonus = player.skills.get("alchemy", 0) / 100 if self.category != "food" else 0
            total_mag = int(mag * (1 + skill_bonus))
            if eff == "restore_health":
                player.stats.heal(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} health.")
            elif eff == "restore_magicka":
                player.stats.restore_magicka(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} magicka.")
            elif eff == "restore_fatigue":
                player.stats.restore_fatigue(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} stamina.")
            elif eff == "cure_poison":
                UI.slow_print(f"You consume the {self.name}, curing poison (effect not yet implemented).")
            elif eff == "resist_fire":
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% fire resistance (effect not yet implemented).")
            elif eff == "resist_frost":
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% frost resistance (effect not yet implemented).")
            elif eff == "resist_shock":
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% shock resistance (effect not yet implemented).")
            elif eff == "fortify_strength":
                UI.slow_print(f"You consume the {self.name}, fortifying strength by {total_mag} (effect not yet implemented).")
            elif eff == "damage_health":
                player.stats.take_damage(total_mag)
                UI.slow_print(f"You consume the {self.name}, taking {total_mag} poison damage!")
            elif eff == "damage_speed":
                UI.slow_print(f"You consume the {self.name}, reducing speed by {total_mag} (effect not yet implemented)!")
            elif eff == "damage_magicka":
                UI.slow_print(f"You consume the {self.name}, reducing magicka by {total_mag} (effect not yet implemented)!")
            player.remove_item(self)
            player.improve_skill("alchemy", 1)
        elif self.category == "weapon":
            UI.slow_print(f"You swing the {self.name} dealing damage.")
        elif self.category == "armor":
            UI.slow_print(f"You equip the {self.name}, increasing defense.")
        elif self.category == "scroll":
            UI.slow_print(f"You read the {self.name} and cast a spell! (Spell casting not fully implemented)")
        else:
            UI.slow_print(f"The {self.name} cannot be used directly.")

    def damage(self, amount: int) -> None:
        if self.category in ["weapon", "armor"]:
            self.durability = max(0, self.durability - amount)
            if self.durability == 0:
                UI.slow_print(f"Your {self.name} has broken!")
                if self.category == "weapon":
                    self.base_damage = (1, 1)
                else:
                    self.armor_rating = 0

    def repair(self, player) -> None:
        skill = player.skills.get("armorer", 0)
        amt = max(1, int(skill / 5))
        self.durability = min(self.max_durability, self.durability + amt)
        UI.slow_print(f"You repair {self.name} to {self.durability}/{self.max_durability} durability.")
        player.improve_skill("armorer", 1)

    def get_description(self) -> str:
        flavor_texts = flavor.get_flavor(self)
        description = f"{self.material} {self.name}:"
        if flavor_texts:
            description += f" {' '.join(flavor_texts)}"
        else:
            desc = [f"{self.material} {self.name}"]
            desc.append(f"Value: {self.value} gold, Weight: {self.weight} lbs")
            if self.category == "weapon" and self.base_damage:
                desc.append(f"Damage: {self.base_damage[0]}-{self.base_damage[1]}")
            elif self.category == "armor" and self.armor_rating is not None:
                desc.append(f"Armor: {self.armor_rating}")
            if self.enchantment:
                desc.append(f"Enchantment: {self.enchantment}")
            if "effect" in self.properties:
                magnitude_str = f"({self.properties.get('magnitude', '')})" if self.properties.get('magnitude') else ""
                desc.append(f"Effect: {self.properties['effect'].replace('_', ' ').title()} {magnitude_str}")
            if self.tags:
                tag_lines = [f"{category.capitalize()}: {', '.join(values.values())}" for category, values in self.tags.items()]
                desc.extend(tag_lines)
            description = " | ".join(desc)
        return description

def generate_random_item(category: str, level: int = 1) -> Item:
    material = random.choice(MATERIALS)
    enchant = random.choice([None, "Fire", "Frost", "Shock", "Poison"]) if category in ["weapon", "armor", "jewelry"] else None
    name = "Unknown Item"
    base_damage = None
    armor_rating = None
    equipment_tag = category
    if category == "weapon":
        name = random.choice(WEAPONS)
        base_damage = (random.randint(1, 3)+level, random.randint(4, 6)+level)
        equipment_tag = "weapon"
    elif category == "armor":
        name = random.choice(ARMORS)
        armor_rating = random.randint(2, 4) + level
        equipment_tag = "armor"
    elif category == "jewelry":
        name = random.choice(JEWELRY)
        equipment_tag = "jewelry"
    elif category == "food":
        name = random.choice(FOODS)
    elif category == "potion":
        name = random.choice(POTIONS)
    elif category == "ingredient":
        name = random.choice(INGREDIENTS)
    elif category == "scroll":
        name = random.choice(SCROLLS)
    elif category == "soul_gem":
        name = random.choice(SOUL_GEMS)
    elif category == "misc":
        name = random.choice(MISC)
    item = Item(name, category, material, equipment_tag=equipment_tag,
                base_damage=base_damage, armor_rating=armor_rating, enchantment=enchant)
    return item

def generate_item_from_key(item_key: str, level: int = 1) -> Item:
    item_info = INITIAL_INVENTORY_MAPPING.get(item_key)
    if not item_info:
        UI.print_failure(f"Error: Item key '{item_key}' not found in INITIAL_INVENTORY_MAPPING. Generating generic item.")
        return generate_random_item("misc", level)
    name = item_info["name"]
    category = item_info["category"]
    material = item_info["material"]
    base_damage = item_info.get("base_damage")
    armor_rating = item_info.get("armor_rating")
    enchantment = item_info.get("enchantment")
    equipment_tag = item_info.get("equipment_tag", category)
    if base_damage and isinstance(base_damage, tuple):
        base_damage = (base_damage[0] + level // 2, base_damage[1] + level // 2)
    if armor_rating is not None:
        armor_rating += level // 2
    item = Item(name, category, material, equipment_tag=equipment_tag,
                base_damage=base_damage, armor_rating=armor_rating, enchantment=enchantment)
    return item