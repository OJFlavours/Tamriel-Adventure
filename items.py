import random
from ui import UI
import tags
import flavor

# Mapping for specific initial inventory items to their properties
# This allows game.py to request items by a simple key (e.g., "iron_sword")
# and this function will know how to construct the actual Item object.
INITIAL_INVENTORY_MAPPING = {
    "iron_sword": {"category": "weapon", "name": "Iron Sword", "material": "Iron", "base_damage": (3, 7)},
    "hide_shield": {"category": "armor", "name": "Hide Shield", "material": "Hide", "armor_rating": 5},
    "iron_battleaxe": {"category": "weapon", "name": "Iron Battleaxe", "material": "Iron", "base_damage": (5, 10)},
    "hide_armor": {"category": "armor", "name": "Hide Cuirass", "material": "Hide", "armor_rating": 8},
    "steel_sword": {"category": "weapon", "name": "Steel Sword", "material": "Steel", "base_damage": (4, 8)},
    "apprentice_tome_flames": {"category": "scroll", "name": "Apprentice Tome of Flames", "material": "Paper"}, # Scrolls don't have damage/armor
    "steel_plate_armor": {"category": "armor", "name": "Steel Plate Cuirass", "material": "Steel", "armor_rating": 15},
    "steel_shield": {"category": "armor", "name": "Steel Shield", "material": "Steel", "armor_rating": 10},
    "dragonbone_greatsword": {"category": "weapon", "name": "Dragonbone Greatsword", "material": "Dragonbone", "base_damage": (15, 25)},
    "amulet_of_mara": {"category": "jewelry", "name": "Amulet of Mara", "material": "Gold"},
    "novice_robes": {"category": "armor", "name": "Novice Robes", "material": "Linen", "armor_rating": 2}, # Robes as light armor
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
        self.tags = {}  # Initialize the tags dictionary
        self.add_tag("item", "type", category)
        self.add_tag("item", "material", material)
        # Derived attributes
        self.weight = self.calculate_weight()
        self.value = self.calculate_value()
        # For consumables, set effect automatically, but only if not already specifically named
        if self.category in ["potion", "ingredient", "food"]:
            self._assign_consumable_effect()

    def add_tag(self, tag_category, tag_type, tag):
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag
        # Removed redundant calls to tags.add_tag as Item.tags is managed internally
        # tags.add_tag(self, tag_category, tag_type)
        # tags.add_tag(self, tag_category, tag)

    def __str__(self) -> str:
       flavor_texts = flavor.get_flavor(self)
       description = f"{self.material} {self.name} [{self.category}]"
       if flavor_texts:
            description += f"{' '.join(flavor_texts)}"
       else:
           parts = [f"{self.material} {self.name} [{self.category}]"]
           if self.enchantment:
               parts.append(f"Enchanted with {self.enchantment}")
           if self.category in ["weapon", "armor"]:
               parts.append(f"Durability: {self.durability}/{self.max_durability}")
           description =  ", ".join(parts)
       return description

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
            "Daedric": 2.8, "Stalhrim": 1.9, "Chitin": 0.8,
            "Wood": 1.0, "Common": 0.5 # Added Wood and Common for new items
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
            "Book": 1.0, "Map": 0.2, "Lute": 3.0 # Added Lute
        }
        material_mult = weight_mult.get(self.material, 1.0)
        type_weight = base_weights.get(self.name.split(" ")[-1], 1.0) # Use last word of name for base weight
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
            "Stalhrim": 4.5, "Chitin": 1.3,
            "Wood": 0.5, "Common": 0.5 # Added Wood and Common
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
            "Book": 80, "Map": 50, "Lute": 75 # Added Lute
        }
        mult = value_mult.get(self.material, 1.0)
        type_value = base_values.get(self.name.split(" ")[-1], 10) # Use last word of name for base value
        enchant_bonus = 1.5 if self.enchantment else 1.0
        return int(mult * type_value * enchant_bonus)

    def _assign_consumable_effect(self):
        """
        Internal: assign effect and magnitude for consumable items.
        If self.name is already a specific item name (from INITIAL_INVENTORY_MAPPING),
        it will use that to look up its effect. Otherwise, it will randomize.
        """
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

        # If the item already has a specific name from the mapping, use its effect if available
        if self.name in pool:
            chosen_effect_data = pool[self.name]
        else: # Otherwise, pick a random one from the category's pool
            chosen_name = random.choice(list(pool.keys()))
            self.name = chosen_name # Overwrite the name with the specific item
            chosen_effect_data = pool[chosen_name]

        self.properties["effect"] = chosen_effect_data["effect"]
        magnitude = chosen_effect_data["magnitude"]
        if isinstance(magnitude, tuple):
            min_mag, max_mag = magnitude
            self.properties["magnitude"] = random.randint(min_mag, max_mag)
        else:
            self.properties["magnitude"] = magnitude


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
                player.stats.restore_magicka(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} magicka.")
            elif eff == "restore_fatigue":
                player.stats.restore_fatigue(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} stamina.")
            elif eff == "cure_poison":
                # Assuming clear_status method exists in Stats
                # player.stats.clear_status("poison")
                UI.slow_print(f"You consume the {self.name}, curing poison (effect not yet implemented).")
            elif eff == "resist_fire":
                # Assuming apply_resistance method exists in Stats
                # player.stats.apply_resistance("fire", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% fire resistance (effect not yet implemented).")
            elif eff == "resist_frost":
                # player.stats.apply_resistance("frost", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% frost resistance (effect not yet implemented).")
            elif eff == "resist_shock":
                # player.stats.apply_resistance("shock", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, granting {total_mag}% shock resistance (effect not yet implemented).")
            elif eff == "fortify_strength":
                # player.stats.fortify_attribute("strength", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, fortifying strength by {total_mag} (effect not yet implemented).")
            elif eff == "damage_health":
                player.stats.take_damage(total_mag) # Damage type not needed here
                UI.slow_print(f"You consume the {self.name}, taking {total_mag} poison damage!")
            elif eff == "damage_speed":
                # player.stats.apply_debuff("speed", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, reducing speed by {total_mag} (effect not yet implemented)!")
            elif eff == "damage_magicka":
                # player.stats.apply_debuff("magicka", total_mag, self.name)
                UI.slow_print(f"You consume the {self.name}, reducing magicka by {total_mag} (effect not yet implemented)!")
            player.remove_item(self) # Use player's remove_item to update encumbrance
            player.improve_skill("alchemy", 1)
        elif self.category == "weapon":
            UI.slow_print(f"You swing the {self.name} dealing damage.")
        elif self.category == "armor":
            UI.slow_print(f"You equip the {self.name}, increasing defense.")
        elif self.category == "scroll":
            UI.slow_print(f"You read the {self.name} and cast a spell! (Spell casting not fully implemented)") #Implement spell casting later
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
        flavor_texts = flavor.get_flavor(self)
        description = f"{self.material} {self.name}:"
        if flavor_texts:
            description += f"{' '.join(flavor_texts)}"
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
            description = " | ".join(desc)
        return description

# Helper lists for random generation
MATERIALS = ["Iron", "Steel", "Silver", "Gold", "Glass", "Ebony", "Dragonbone",
             "Orcish", "Dwarven", "Elven", "Falmer", "Nordic", "Leather",
             "Hide", "Fur", "Chitin", "Daedric", "Stalhrim", "Wood", "Paper", "Linen", "Common"] # Added Wood, Paper, Linen, Common
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
MISC = ["Lockpick", "Book", "Map", "Lute"] #Added Lute

def generate_random_item(category: str, level: int = 1) -> Item:
    """
    Factory function to generate a random item for loot or shop.
    """
    material = random.choice(MATERIALS)
    enchant = random.choice([None, "Fire", "Frost", "Shock", "Poison"]) if category in ["weapon", "armor", "jewelry"] else None
    
    name = "Unknown Item" # Default name
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
    
    # Create the item instance
    item = Item(name, category, material, equipment_tag=equipment_tag,
                base_damage=base_damage, armor_rating=armor_rating, enchantment=enchant)
    
    # Consumable effects are assigned in Item.__init__ if category matches
    
    return item

def generate_item_from_key(item_key: str, level: int = 1) -> Item:
    """
    Generates a specific item based on a predefined key from INITIAL_INVENTORY_MAPPING.
    This is used for player starting inventory or specific quest items.
    """
    item_info = INITIAL_INVENTORY_MAPPING.get(item_key)
    if not item_info:
        UI.print_failure(f"Error: Item key '{item_key}' not found in INITIAL_INVENTORY_MAPPING. Generating generic item.")
        return generate_random_item("misc", level) # Fallback to a random misc item

    name = item_info["name"]
    category = item_info["category"]
    material = item_info["material"]
    
    base_damage = item_info.get("base_damage")
    armor_rating = item_info.get("armor_rating")
    enchantment = item_info.get("enchantment")
    equipment_tag = item_info.get("equipment_tag", category)

    # Adjust damage/armor based on level if they are not fixed in the mapping
    if base_damage and isinstance(base_damage, tuple):
        base_damage = (base_damage[0] + level // 2, base_damage[1] + level // 2) # Scale with level
    if armor_rating is not None:
        armor_rating += level // 2 # Scale with level

    item = Item(name, category, material, equipment_tag=equipment_tag,
                base_damage=base_damage, armor_rating=armor_rating, enchantment=enchantment)
    
    # For consumables, the effect is assigned in Item.__init__ based on its specific name
    # if it's found in the pool, otherwise it picks a random one.
    
    return item
