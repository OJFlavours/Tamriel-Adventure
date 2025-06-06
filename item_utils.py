# item_utils.py
import random
from item_definitions import Item
from items_data import (
    INITIAL_INVENTORY_MAPPING,
    MATERIALS,
    WEAPONS,
    ARMORS,
    JEWELRY,
    FOODS,
    POTIONS,
    INGREDIENTS,
    SCROLLS,
    SOUL_GEMS,
    MISC,
    TOMES
)
ITEM_MAPPING = {key: item for key, item in INITIAL_INVENTORY_MAPPING.items()}
# from ui import UI # Not strictly needed here if errors are handled or logged differently

import os
import importlib.util

CUSTOM_UTILITIES = {}

def load_custom_utilities(filepath: str) -> None:
    """Loads custom utility functions from a specified file."""
    if not os.path.exists(filepath):
        print(f"Warning: Custom utility file '{filepath}' not found.")
        return

    try:
        spec = importlib.util.spec_from_file_location("custom_item_utils", filepath)
        if spec is None:
            print(f"Warning: Could not load custom utility file '{filepath}'. Invalid file specification.")
            return
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        for name in dir(module):
            if name.startswith("custom_"):
                CUSTOM_UTILITIES[name] = getattr(module, name)
        print(f"Loaded {len(CUSTOM_UTILITIES)} custom utility functions from '{filepath}'.")

    except Exception as e:
        print(f"Error loading custom utilities from '{filepath}': {e}")

# Example usage: load_custom_utilities("custom_item_utils.py")

def generate_random_item(category: str, level: int = 1, rarity: str = "common") -> Item:
    """Generates a random item of a specified category and rarity."""
    try:
        # Pre-calculate material choices and enchant chances based on rarity
        if rarity == "common":
            material_choices = ["Iron", "Hide", "Wood", "Linen", "Paper", "Common"]
            enchant_chance = 0.0
        elif rarity == "uncommon":
            material_choices = ["Steel", "Leather", "Silver"] + MATERIALS[:]
            enchant_chance = 0.25
        elif rarity == "rare":
            material_choices = ["Elven", "Dwarven", "Orcish", "Glass"] + MATERIALS[:]
            enchant_chance = 0.5
        elif rarity == "legendary":
            material_choices = ["Ebony", "Stalhrim", "Dragonbone", "Daedric"] + MATERIALS[:]
            enchant_chance = 0.75
        else:
            material_choices = MATERIALS[:]
            enchant_chance = 0.0

        unique_enchant = None
        if rarity == "rare":
            unique_enchant = random.choice(["Drain Health", "Paralyze", "Silence"])
        elif rarity == "legendary":
            unique_enchant = random.choice(["Absorb Magicka", "Chaos Damage", "Soul Trap"])

        material = random.choice(material_choices) if material_choices else "Common"

        enchant = None
        if category in ["weapon", "armor", "jewelry"] and random.random() < enchant_chance:
            if unique_enchant:
                enchant = unique_enchant
            else:
                enchant = random.choice([None, "Fire Damage", "Frost Damage", "Shock Damage", "Absorb Health",
                                         "Turn Undead", "Fortify Health", "Fortify Magicka", "Fortify Stamina",
                                         "Resist Fire", "Resist Frost", "Resist Shock"])
        name = "Generic Item"
        base_damage = None
        armor_rating = None
        equipment_tag = category
        properties = {}

        if category == "weapon":
            name_base = random.choice(WEAPONS) if WEAPONS else "Blade"
            name = f"{material} {name_base}"
            if "Staff" in name_base:
                base_damage = (5 + level, 10 + level + (level // 2))
                enchant = enchant or random.choice(["Fire Damage", "Frost Damage", "Shock Damage", "Fear"])
                properties["magical_focus"] = True
            else:
                base_min = 5 + level + (MATERIALS.index(material) // 3 if material in MATERIALS else 0)
                base_max = 10 + level + (level // 2) + (MATERIALS.index(material) // 2 if material in MATERIALS else 0)
                if "Dagger" in name_base:
                    base_min, base_max = max(1, base_min // 2), max(2, base_max // 2)
                elif any(wt in name_base for wt in ["Greatsword", "Battleaxe", "Warhammer"]):
                    base_min, base_max = int(base_min * 1.3), int(base_max * 1.3)
                base_damage = (random.randint(base_min, base_min + 3), random.randint(base_max, base_max + 5))

            if any(tag in name_base for tag in ["Bow", "Greatsword", "Battleaxe", "Warhammer", "Staff"]):
                equipment_tag = "two_handed"
            else:
                equipment_tag = "main_hand"
        elif category == "armor":
            name_base = random.choice(ARMORS) if ARMORS else "Gear"
            name = f"{material} {name_base}"
            armor_rating = random.randint(2, 4) + level + (level // 2) + (
                MATERIALS.index(material) // 2 if material in MATERIALS else 0)
            if "Helmet" in name_base:
                equipment_tag = "head"
            elif any(tag in name_base for tag in ["Cuirass", "Robes", "Armor", "Outfit", "Tunic"]):
                equipment_tag = "chest"
            elif any(tag in name_base for tag in ["Gauntlets", "Gloves"]):
                equipment_tag = "hands"
            elif any(tag in name_base for tag in ["Greaves", "Boots"]):
                equipment_tag = "feet"
            elif "Shield" in name_base:
                equipment_tag = "off_hand"
            else:
                equipment_tag = "chest"
        elif category == "jewelry":
            name_base = random.choice(JEWELRY) if JEWELRY else "Trinket"
            name = f"{material} {name_base}"
            if "Ring" in name_base:
                equipment_tag = "ring"
            elif any(tag in name_base for tag in ["Amulet", "Locket", "Pendant"]):
                equipment_tag = "amulet"
            else:
                equipment_tag = "jewelry"
            enchant = enchant or random.choice(["Fortify Health", "Fortify Magicka", "Fortify Stamina",
                                                 "Resist Magic"])
        elif category == "food":
            name = random.choice(FOODS) if FOODS else "Rations"
        elif category == "potion":
            name = random.choice(POTIONS) if POTIONS else "Concoction"
        elif category == "ingredient":
            name = random.choice(INGREDIENTS) if INGREDIENTS else "Herb"
        elif category == "scroll":
            name = random.choice(SCROLLS) if SCROLLS else "Parchment"
        elif category == "soul_gem":
            name = random.choice(SOUL_GEMS) if SOUL_GEMS else "Mystic Stone"
        elif category == "tome":
            name = random.choice(TOMES) if TOMES else "Book of Spells"
            if name == "Book of Spells" or name == "Apprentice Random Tome": 
                from spells import SPELL_REGISTRY 
                if SPELL_REGISTRY:
                    properties["spell_key"] = random.choice(list(SPELL_REGISTRY.keys()))
                    name = f"Tome: {properties['spell_key'].replace('_', ' ').title()}"
        elif category == "misc":
            name = random.choice(MISC) if MISC else "Trinket"
        else: 
            name = f"{material} {category.capitalize()} Item"
            category = "misc" 
            equipment_tag = "misc"

        if rarity != "common" and not name.startswith(rarity.capitalize()):
            name = f"{rarity.capitalize()} {name}"

        item = Item(name, category, material, equipment_tag=equipment_tag,
                    base_damage=base_damage, armor_rating=armor_rating, enchantment=enchant, properties=properties)
        return item
    except Exception as e:
        print(f"Error in generate_random_item: {e}")
        print(f"Warning: Item key 'Returning default Item.")
        return Item("Default Item", "misc", "Common")

def generate_item_from_key(item_key: str, level: int = 1) -> Item | None:
    """Generates an item from a given item key using a dictionary lookup."""
    try:
        item_info = ITEM_MAPPING.get(item_key.lower())
        if not item_info:
            # print(f"Warning: Item key '{item_key}' not found. Returning None.") # Optional: log or handle differently
            print(f"Warning: Item key '{item_key}' not found. Returning default Item.")
            return Item("Default Item", "misc", "Common")

        name = item_info["name"]
        category = item_info["category"]
        material = item_info["material"]
        base_damage = item_info.get("base_damage")
        armor_rating = item_info.get("armor_rating")
        enchantment = item_info.get("enchantment")
        equipment_tag = item_info.get("equipment_tag")
        properties = item_info.get("properties", {})

        if base_damage and isinstance(base_damage, tuple):
            lvl_bonus_min = level // 5
            lvl_bonus_max = level // 4
            base_damage = (base_damage[0] + lvl_bonus_min, base_damage[1] + lvl_bonus_max)
        if armor_rating is not None:
            armor_rating += level // 4

        item = Item(name, category, material, equipment_tag=equipment_tag,
                    base_damage=base_damage, armor_rating=armor_rating, enchantment=enchantment, properties=properties)
        return item
    except Exception as e:
        print(f"Error in generate_item_from_key: {e}")
        print(f"Warning: Item key '{item_key}' not found. Returning default Item.")
        return Item("Default Item", "misc", "Common")

def get_item_value(item: Item) -> int:
    """Calculates the value of an item based on its rarity, material, and enchantments."""
    try:
        if "custom_get_item_value" in CUSTOM_UTILITIES:
            return CUSTOM_UTILITIES["custom_get_item_value"](item)
        value = 10  # Base value
        if item.enchantment:
            value += 20
        # Add more logic to calculate value based on rarity and material
        return value
    except Exception as e:
        print(f"Error in get_item_value: {e}")
        return 0

def is_item_equippable(item: Item) -> bool:
    """Checks if an item can be equipped."""
    try:
        if "custom_is_item_equippable" in CUSTOM_UTILITIES:
            return CUSTOM_UTILITIES["custom_is_item_equippable"](item)
        return item.equipment_tag is not None
    except Exception as e:
        print(f"Error in is_item_equippable: {e}")
        return False

def get_item_effects(item: Item, target, context=None) -> dict:
    """Returns a dictionary of effects the item has on a target (player or NPC)."""
    try:
        if "custom_get_item_effects" in CUSTOM_UTILITIES:
            return CUSTOM_UTILITIES["custom_get_item_effects"](item, target, context)
        effects = {}
        if item.enchantment == "Fire Damage":
            effects["fire_damage"] = 5
        # Add more logic to determine effects based on item properties
        return effects
    except Exception as e:
        print(f"Error in get_item_effects: {e}")
        return {}

def apply_item_bonuses(item: Item, target) -> None:
    """Applies the bonuses of an item to a target."""
    try:
        if "custom_apply_item_bonuses" in CUSTOM_UTILITIES:
            CUSTOM_UTILITIES["custom_apply_item_bonuses"](item, target)
            return
        if item.equipment_tag == "ring":
            target.max_health += 10
        # Add more logic to apply bonuses based on item properties
        
    except Exception as e:
        print(f"Error in apply_item_bonuses: {e}")

def remove_item_bonuses(item: Item, target) -> None:
    """Removes the bonuses of an item from a target."""
    try:
        if "custom_remove_item_bonuses" in CUSTOM_UTILITIES:
            CUSTOM_UTILITIES["custom_remove_item_bonuses"](item, target)
            return
        if item.equipment_tag == "ring":
            target.max_health -= 10
        # Add more logic to remove bonuses based on item properties
    except Exception as e:
        print(f"Error in remove_item_bonuses: {e}")

def repair_item(item: Item, repair_amount: int) -> None:
    """Repairs an item by a certain amount."""
    try:
        if "custom_repair_item" in CUSTOM_UTILITIES:
            CUSTOM_UTILITIES["custom_repair_item"](item, repair_amount)
            return
        if hasattr(item, "durability"):
            item.durability = min(item.durability + repair_amount, item.max_durability)
    except Exception as e:
        print(f"Error in repair_item: {e}")

def get_item_durability(item: Item) -> int:
    """Returns the durability of an item."""
    try:
        if "custom_get_item_durability" in CUSTOM_UTILITIES:
            return CUSTOM_UTILITIES["custom_get_item_durability"](item)
        if hasattr(item, "durability"):
            return item.durability
        return 100  # Default durability
    except Exception as e:
        print(f"Error in get_item_durability: {e}")
        return 100

def damage_item(item: Item, damage_amount: int) -> None:
    """Damages an item by a certain amount."""
    try:
        if "custom_damage_item" in CUSTOM_UTILITIES:
            CUSTOM_UTILITIES["custom_damage_item"](item, damage_amount)
            return
        if hasattr(item, "durability"):
            item.durability -= damage_amount
            if item.durability <= 0:
                print(f"{item.name} has broken!")
                # Implement item breaking logic here
    except Exception as e:
        print(f"Error in damage_item: {e}")

def test_item_generation():
    from items_data import INITIAL_INVENTORY_MAPPING
    for key in INITIAL_INVENTORY_MAPPING:
        item = generate_item_from_key(key)
        print(f'{key}: {item.name} ({item.category})')