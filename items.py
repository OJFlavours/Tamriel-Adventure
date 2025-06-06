# items.py

__all__ = [
    "Item",
    "Torch",
    "generate_random_item",
    "generate_item_from_key",
    "generate_item",
    "INITIAL_INVENTORY_MAPPING",
    "MATERIALS",
    "WEAPONS",
    "ARMORS",
    "JEWELRY",
    "FOODS",
    "POTIONS",
    "INGREDIENTS",
    "SCROLLS",
    "SOUL_GEMS",
    "MISC",
    "TOMES"
]

# Import classes from item_definitions.py
from item_definitions import Item, Torch

# Import utility functions from item_utils.py
from item_utils import generate_random_item, generate_item_from_key

# Import data from items_data.py (which now includes more data)
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
    TOMES,
    # The following are now also in items_data.py but not typically re-exported
    # WEIGHT_MULTIPLIERS,
    # BASE_WEIGHTS,
    # VALUE_MULTIPLIERS,
    # BASE_VALUES,
    # CONSUMABLE_EFFECT_POOLS
)

# Any high-level logic or orchestration related to items that doesn't fit
# into definitions or utils could potentially reside here in the future.
# For now, this module primarily serves as an aggregator and public interface.

def generate_item(name: str, category: str, material: str, equipment_tag: str = None, base_damage: tuple = None, armor_rating: int = None, enchantment: str = None, durability: int = 100, properties: dict = None) -> Item:
    """Generates an item with specified attributes."""
    try:
        item = Item(name, category, material, equipment_tag=equipment_tag,
                    base_damage=base_damage, armor_rating=armor_rating, enchantment=enchantment, durability=durability, properties=properties)
        return item
    except Exception as e:
        print(f"Error in generate_item: {e}")
        return Item("Default Item", "misc", "Common")

# Create falmer_armor_basic item
falmer_armor_basic = generate_item("falmer_armor_basic", "Falmer Armor", "armor", "chitin", armor_rating=5, properties={})
