# items.py

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

__all__ = [
    # Classes
    "Item",
    "Torch",
    # Utility Functions
    "generate_random_item",
    "generate_item_from_key",
    # Data (primarily for external use, like populating loot tables or shops)
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

# Any high-level logic or orchestration related to items that doesn't fit
# into definitions or utils could potentially reside here in the future.
# For now, this module primarily serves as an aggregator and public interface.
