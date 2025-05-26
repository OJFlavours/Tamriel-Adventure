# items.py
import random
from ui import UI
import tags # Assuming tags.py exists and is used by Item class
import flavor # Crucial for item flavor text
from colorama import Fore, Style # For colored/styled output in descriptions

INITIAL_INVENTORY_MAPPING = {
    # Warrior Gear
    "iron_sword": {"category": "weapon", "name": "Iron Sword", "material": "Iron", "base_damage": (3, 7), "equipment_tag": "main_hand"},
    "hide_shield": {"category": "armor", "name": "Hide Shield", "material": "Hide", "armor_rating": 5, "equipment_tag": "off_hand"},
    "iron_battleaxe": {"category": "weapon", "name": "Iron Battleaxe", "material": "Iron", "base_damage": (5, 10), "equipment_tag": "two_handed"},
    "hide_armor": {"category": "armor", "name": "Hide Cuirass", "material": "Hide", "armor_rating": 8, "equipment_tag": "chest"},
    "steel_sword": {"category": "weapon", "name": "Steel Sword", "material": "Steel", "base_damage": (4, 8), "equipment_tag": "main_hand"},
    "apprentice_tome_flames": {"category": "scroll", "name": "Apprentice Tome of Flames", "material": "Paper"},
    "steel_plate_armor": {"category": "armor", "name": "Steel Plate Cuirass", "material": "Steel", "armor_rating": 15, "equipment_tag": "chest"},
    "steel_shield": {"category": "armor", "name": "Steel Shield", "material": "Steel", "armor_rating": 10, "equipment_tag": "off_hand"},
    "dragonbone_greatsword": {"category": "weapon", "name": "Dragonbone Greatsword", "material": "Dragonbone", "base_damage": (15, 25), "equipment_tag": "two_handed"},
    "amulet_of_mara": {"category": "jewelry", "name": "Amulet of Mara", "material": "Gold", "equipment_tag": "amulet"},

    # Mage Gear
    "novice_robes": {"category": "armor", "name": "Novice Robes", "material": "Linen", "armor_rating": 2, "equipment_tag": "chest"},
    "apprentice_tome_firebolt": {"category": "scroll", "name": "Apprentice Tome of Firebolt", "material": "Paper"},
    "priest_robes": {"category": "armor", "name": "Priest Robes", "material": "Linen", "armor_rating": 3, "equipment_tag": "chest"},
    "apprentice_tome_healing": {"category": "scroll", "name": "Apprentice Tome of Healing", "material": "Paper"},
    "apprentice_robes": {"category": "armor", "name": "Apprentice Robes", "material": "Linen", "armor_rating": 4, "equipment_tag": "chest"},
    "apprentice_tome_conjure_familiar": {"category": "scroll", "name": "Apprentice Tome of Conjure Familiar", "material": "Paper"},
    "fine_clothes": {"category": "armor", "name": "Fine Clothes", "material": "Linen", "armor_rating": 1, "equipment_tag": "chest"},
    "apprentice_tome_courage": {"category": "scroll", "name": "Apprentice Tome of Courage", "material": "Paper"},
    "alchemist_robes": {"category": "armor", "name": "Alchemist Robes", "material": "Linen", "armor_rating": 3, "equipment_tag": "chest"},
    "scroll_of_soul_trap": {"category": "scroll", "name": "Scroll of Soul Trap", "material": "Paper"},

    # Thief Gear
    "leather_armor": {"category": "armor", "name": "Leather Armor", "material": "Leather", "armor_rating": 10, "equipment_tag": "chest"},
    "iron_dagger": {"category": "weapon", "name": "Iron Dagger", "material": "Iron", "base_damage": (2, 4), "equipment_tag": "main_hand"},
    "dark_brotherhood_robes": {"category": "armor", "name": "Dark Brotherhood Robes", "material": "Leather", "armor_rating": 6, "equipment_tag": "chest"},
    "lockpick": {"category": "misc", "name": "Lockpick", "material": "Iron"},
    "hunting_bow": {"category": "weapon", "name": "Hunting Bow", "material": "Wood", "base_damage": (4, 8), "equipment_tag": "two_handed"},
    "jester_outfit": {"category": "armor", "name": "Jester Outfit", "material": "Linen", "armor_rating": 2, "equipment_tag": "chest"},
    "scroll_of_calm": {"category": "scroll", "name": "Scroll of Calm", "material": "Paper"},
    
    # Adventurer Gear
    "lute": {"category": "misc", "name": "Lute", "material": "Wood"},
    "fur_armor": {"category": "armor", "name": "Fur Armor", "material": "Fur", "armor_rating": 7, "equipment_tag": "chest"},
    "iron_axe": {"category": "weapon", "name": "Iron Axe", "material": "Iron", "base_damage": (4, 9), "equipment_tag": "main_hand"},
    "venison_steak": {"category": "food", "name": "Venison Steak", "material": "Common"},
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
           "Scroll of Courage", "Scroll of Soul Trap", "Scroll of Calm"]
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
        self.equipment_tag = equipment_tag if equipment_tag is not None else category
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
            "Iron": 1.0, "Steel": 1.2, "Gold": 1.8, "Glass": 0.8, "Ebony": 2.0, "Daedric": 2.8,
            "Leather": 0.5, "Hide": 0.7, "Fur": 0.6, "Linen": 0.2, "Paper": 0.1, "Wood": 0.8, "Dragonbone": 1.5,
            "Common": 0.3 # For things like food
        }
        base_weights = {
            "Sword": 5.0, "Axe": 6.0, "Battleaxe": 12.0, "Greatsword": 10.0, "Dagger": 1.0, "Bow": 4.0, "Staff": 3.0,
            "Helmet": 3.0, "Cuirass": 10.0, "Gauntlets": 2.0, "Greaves": 4.0, "Boots": 3.0, "Shield": 6.0,
            "Robes": 3.0, "Clothes": 2.0, "Outfit": 3.0, "Ring": 0.1, "Amulet": 0.2,
            "Tome": 1.0, "Scroll": 0.1, "Lockpick": 0.1, "Lute": 2.0, "Book": 1.0, "Map": 0.2,
            "Potion": 0.5, "Ingredient": 0.1, "Food": 0.5, "Venison Steak": 0.7, "Apple": 0.3
        }
        material_multiplier = weight_mult.get(self.material, 1.0)
        
        type_w = 1.0 
        for type_key, weight_val in base_weights.items():
            if type_key.lower() in self.name.lower():
                type_w = weight_val
                break
        
        if self.category == "weapon": type_w = max(type_w, 3.0)
        elif self.category == "armor": type_w = max(type_w, 2.0)
        elif self.category == "jewelry": type_w = max(type_w, 0.1)

        return round(material_multiplier * type_w, 1)

    def calculate_value(self) -> int:
        value_mult = {
            "Iron": 10, "Steel": 20, "Silver": 50, "Gold": 100, "Glass": 150, "Ebony": 300, "Daedric": 500,
            "Leather": 5, "Hide": 3, "Fur": 8, "Linen": 2, "Paper": 1, "Wood": 5, "Dragonbone": 400,
            "Common": 1
        }
        base_values = {
            "Sword": 20, "Axe": 25, "Battleaxe": 40, "Greatsword": 50, "Dagger": 10, "Bow": 30, "Staff": 35,
            "Helmet": 15, "Cuirass": 50, "Gauntlets": 10, "Greaves": 20, "Boots": 15, "Shield": 25,
            "Robes": 15, "Clothes": 10, "Outfit": 20, "Ring": 75, "Amulet": 100,
            "Tome": 25, "Scroll": 10, "Potion": 15, "Ingredient": 2, "Food": 3, "Lute": 15, "Book": 5,
            "Lockpick": 2, "Venison Steak": 5, "Apple": 1
        }
        material_base_value = value_mult.get(self.material, 5)
        
        type_v = 5
        for type_key, val in base_values.items():
            if type_key.lower() in self.name.lower():
                type_v = val
                break
        
        if self.category == "weapon": type_v = max(type_v, 15)
        elif self.category == "armor": type_v = max(type_v, 10)
        elif self.category == "jewelry": type_v = max(type_v, 50)
        
        enchant_bonus_mult = 1.0
        if self.enchantment:
            enchant_bonus_mult = 2.0 
            if "Greater" in self.name or "Grand" in self.name: enchant_bonus_mult = 3.0
            elif "Minor" in self.name: enchant_bonus_mult = 1.5

        return int( (material_base_value + type_v) * enchant_bonus_mult )

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
                "Potion of Resist Fire": {"effect": "resist_fire", "magnitude": (15, 25)},
                "Potion of Resist Frost": {"effect": "resist_frost", "magnitude": (15, 25)},
                "Potion of Resist Shock": {"effect": "resist_shock", "magnitude": (15, 25)},
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
            if pool:
                chosen_name_for_effect = random.choice(list(pool.keys()))
                chosen_effect_data = pool[chosen_name_for_effect]
            else:
                return

        self.properties["effect"] = chosen_effect_data["effect"]
        magnitude_data = chosen_effect_data["magnitude"]
        if isinstance(magnitude_data, tuple):
            min_mag, max_mag = magnitude_data
            self.properties["magnitude"] = random.randint(min_mag, max_mag)
        else:
            self.properties["magnitude"] = magnitude_data

    def use(self, player) -> None:
        if self.category in ["potion", "ingredient", "food"] and "effect" in self.properties:
            eff = self.properties.get("effect")
            mag = self.properties.get("magnitude", 0)
            
            alchemy_skill = player.skills.get("alchemy", 0) if hasattr(player, 'skills') else 0
            skill_bonus = alchemy_skill / 100.0 if self.category != "food" else 0.0
            total_mag = int(mag * (1 + skill_bonus))

            consumed = True
            if eff == "restore_health":
                player.stats.heal(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} health.")
            elif eff == "restore_magicka":
                player.stats.restore_magicka(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} magicka.")
            elif eff == "restore_fatigue":
                player.stats.restore_fatigue(total_mag)
                UI.slow_print(f"You consume the {self.name}, restoring {total_mag} stamina.")
            elif eff == "cure_poison": UI.slow_print(f"You consume the {self.name}, curing poison (Effect TODO).")
            elif eff == "resist_fire": UI.slow_print(f"You consume the {self.name}, gaining {total_mag}% Fire Resist (Effect TODO).")
            elif eff == "damage_health":
                player.stats.take_damage(total_mag)
                UI.slow_print(f"You consume the {self.name}, taking {total_mag} damage!")
            else:
                UI.slow_print(f"You consume the {self.name}. Effect: {eff.replace('_',' ').title()} by {total_mag} (Effect TODO).")
                consumed = False

            if consumed:
                if hasattr(player, 'remove_item'):
                    player.remove_item(self)
                elif hasattr(player, 'stats') and hasattr(player.stats, 'remove_from_inventory'):
                    player.stats.remove_from_inventory(self)
                else:
                    UI.print_warning(f"Could not remove {self.name} from inventory after use.")

            if self.category in ["potion", "ingredient"] and hasattr(player, 'improve_skill'):
                player.improve_skill("alchemy", random.randint(1,2))

        elif self.category == "scroll":
            UI.slow_print(f"You read the {self.name} and a magical effect unfolds! (Spell effects from scrolls TODO).")
            if hasattr(player, 'remove_item'): player.remove_item(self)
            elif hasattr(player.stats, 'remove_from_inventory'): player.stats.remove_from_inventory(self)

        else:
            UI.slow_print(f"The {self.name} cannot be 'used' in this manner. Perhaps equip or examine it?")

    def damage(self, amount: int) -> None:
        if self.category in ["weapon", "armor"]:
            self.durability = max(0, self.durability - amount)
            UI.slow_print(f"{self.name} takes {amount} damage. Durability: {self.durability}/{self.max_durability}")
            if self.durability == 0:
                UI.slow_print(f"Your {self.name} has broken!")
                if self.category == "weapon" and self.base_damage:
                    self.base_damage = (self.base_damage[0]//2, self.base_damage[1]//2)
                elif self.category == "armor" and self.armor_rating is not None:
                    self.armor_rating = self.armor_rating // 2
                self.add_tag("item", "condition", "broken")

    def repair(self, player) -> None:
        if self.durability < self.max_durability:
            armorer_skill = player.skills.get("armorer", 0) if hasattr(player, 'skills') else 0
            repair_amount = max(1, int(armorer_skill / 4) + random.randint(10, 25))
            
            self.durability = min(self.max_durability, self.durability + repair_amount)
            if "broken" in self.tags.get("item", {}).get("condition", "") and self.durability > 0:
                self.tags["item"].pop("condition", None)
                # TODO: Restore original damage/armor if it was halved. This needs storing original values.

            UI.slow_print(f"You attempt to repair {self.name}. Durability: {self.durability}/{self.max_durability}.")
            if hasattr(player, 'improve_skill'):
                player.improve_skill("armorer", random.randint(1,2))
        else:
            UI.slow_print(f"{self.name} is already in perfect condition.")

    def get_description(self) -> str:
        description_parts = []
        
        base_name = self.name
        display_title = base_name
        if self.material and \
           self.material not in ["Paper", "Common", "Linen", "Wood"] and \
           self.category not in ["scroll", "food", "ingredient", "potion", "misc", "jewelry"] and \
           not base_name.lower().startswith(self.material.lower()):
            display_title = f"{self.material} {base_name}"
        
        description_parts.append(Style.BRIGHT + display_title + Style.RESET_ALL)

        try:
            flavor_texts_list = []
            if hasattr(flavor, 'get_flavor'): # Check if flavor module and get_flavor exist
                retrieved_flavor = flavor.get_flavor(self) # Pass the item instance
                if isinstance(retrieved_flavor, list) and all(isinstance(ft, str) for ft in retrieved_flavor):
                    flavor_texts_list = retrieved_flavor
                elif isinstance(retrieved_flavor, str) and retrieved_flavor:
                    flavor_texts_list = [retrieved_flavor]
            
            if flavor_texts_list: # Specific flavor text from flavor.py found
                description_parts.append("") 
                for ft_line in flavor_texts_list:
                    description_parts.append(Fore.LIGHTBLACK_EX + UI.wrap_text(f"\"{ft_line}\"") + Style.RESET_ALL)
            else: # Fallback to varied generic observations
                generic_observations = [
                    "\"You note its craftsmanship and apparent age.\"",
                    "\"A standard item of its type, serving its purpose well.\"",
                    "\"It seems sturdy and has been reasonably maintained.\"",
                    "\"There's a faint, unidentifiable scent clinging to it.\"",
                    "\"You ponder the journeys this item might have undertaken.\""
                ]
                description_parts.append("")
                description_parts.append(Fore.LIGHTBLACK_EX + UI.wrap_text(random.choice(generic_observations)) + Style.RESET_ALL)
        except Exception as e:
            description_parts.append("")
            description_parts.append(Fore.LIGHTBLACK_EX + UI.wrap_text("\"Its story remains veiled for now.\"") + Style.RESET_ALL)
            # print(f"Debug: Error in get_flavor for {self.name}: {e}") # Optional for debugging

        stats_lines = ["", Fore.CYAN + "--- Details ---" + Style.RESET_ALL]
        stats_lines.append(f"Category: {self.category.capitalize()}")
        if self.material:
             stats_lines.append(f"Material: {self.material}")
        stats_lines.append(f"Value: {self.value} gold")
        stats_lines.append(f"Weight: {self.weight} lbs")

        if self.category == "weapon" and self.base_damage:
            stats_lines.append(f"Damage: {self.base_damage[0]}-{self.base_damage[1]}")
        elif self.category == "armor" and self.armor_rating is not None:
            stats_lines.append(f"Armor Rating: {self.armor_rating}")
        
        if self.category in ["weapon", "armor"] and hasattr(self, 'durability') and hasattr(self, 'max_durability'):
             stats_lines.append(f"Durability: {self.durability}/{self.max_durability}")

        if self.enchantment:
            stats_lines.append(f"Enchantment: {self.enchantment}")

        if "effect" in self.properties:
            effect_name = self.properties['effect'].replace('_', ' ').title()
            magnitude_str = ""
            if self.properties.get('magnitude') and self.properties['magnitude'] != 0:
                magnitude_str = f" (Magnitude: {self.properties['magnitude']})"
            stats_lines.append(f"Effect: {effect_name}{magnitude_str}")
        
        description_parts.extend(stats_lines)

        if self.tags:
            tag_display_lines = ["", Fore.CYAN + "--- Tags ---" + Style.RESET_ALL]
            has_actual_tags = False
            for tag_category, tag_types_dict in self.tags.items():
                type_value_pairs = []
                for tag_type, tag_value in tag_types_dict.items():
                    if tag_category.lower() == "item" and tag_type.lower() == "type" and tag_value.lower() == self.category.lower(): continue
                    if tag_category.lower() == "item" and tag_type.lower() == "material" and tag_value.lower() == self.material.lower(): continue
                    type_value_pairs.append(f"{tag_type.replace('_',' ').capitalize()}: {tag_value}")
                if type_value_pairs:
                    tag_display_lines.append(f"{tag_category.capitalize()}: {', '.join(type_value_pairs)}")
                    has_actual_tags = True
            
            if has_actual_tags:
                description_parts.extend(tag_display_lines)
        
        return "\n".join(description_parts)


def generate_random_item(category: str, level: int = 1) -> Item:
    material = random.choice(MATERIALS) if MATERIALS else "Common"
    enchant = random.choice([None, "Fire", "Frost", "Shock", "Poison", "Absorb Health", "Turn Undead"]) if category in ["weapon", "armor", "jewelry"] and random.random() < 0.15 else None
    
    name = "Generic Item"
    base_damage = None
    armor_rating = None
    equipment_tag = category 

    if category == "weapon":
        name_base = random.choice(WEAPONS) if WEAPONS else "Blade"
        name = f"{material} {name_base}"
        if "Staff" in name_base:
            base_damage = (1 + level//2, 3 + level//2) 
            enchant = enchant or random.choice(["Fire", "Frost", "Shock", "Fear"])
        else:
            base_damage = (random.randint(1, 3) + level, random.randint(4, 6) + level + (level // 2))
        
        if "bow" in name_base.lower() or "greatsword" in name_base.lower() or "battleaxe" in name_base.lower() or "warhammer" in name_base.lower():
            equipment_tag = "two_handed"
        else:
            equipment_tag = "main_hand"
    elif category == "armor":
        name_base = random.choice(ARMORS) if ARMORS else "Gear"
        name = f"{material} {name_base}"
        armor_rating = random.randint(2, 4) + level + (level // 2)
        if "helmet" in name_base.lower(): equipment_tag = "head"
        elif "cuirass" in name_base.lower() or "robes" in name_base.lower() or "armor" in name_base.lower() or "outfit" in name_base.lower(): equipment_tag = "chest"
        elif "gauntlets" in name_base.lower() or "gloves" in name_base.lower(): equipment_tag = "hands"
        elif "greaves" in name_base.lower() or "boots" in name_base.lower(): equipment_tag = "feet"
        elif "shield" in name_base.lower(): equipment_tag = "off_hand"
        else: equipment_tag = "chest" 
    elif category == "jewelry":
        name_base = random.choice(JEWELRY) if JEWELRY else "Trinket"
        name = f"{material} {name_base}"
        if "ring" in name_base.lower(): equipment_tag = "ring"
        elif "amulet" in name_base.lower(): equipment_tag = "amulet"
        else: equipment_tag = "jewelry" 
    elif category == "food": name = random.choice(FOODS) if FOODS else "Rations"
    elif category == "potion": name = random.choice(POTIONS) if POTIONS else "Concoction"
    elif category == "ingredient": name = random.choice(INGREDIENTS) if INGREDIENTS else "Herb"
    elif category == "scroll": name = random.choice(SCROLLS) if SCROLLS else "Parchment"
    elif category == "soul_gem": name = random.choice(SOUL_GEMS) if SOUL_GEMS else "Mystic Stone"
    elif category == "misc": name = random.choice(MISC) if MISC else "Trinket"
    else:
        name = f"{material} {category.capitalize()} Item"
        category = "misc"
        equipment_tag = "misc"

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
    equipment_tag = item_info.get("equipment_tag")
    properties = item_info.get("properties")
    
    if base_damage and isinstance(base_damage, tuple):
        base_damage = (base_damage[0] + level // 4, base_damage[1] + level // 4)
    if armor_rating is not None:
        armor_rating += level // 4

    item = Item(name, category, material, equipment_tag=equipment_tag,
                base_damage=base_damage, armor_rating=armor_rating, enchantment=enchantment, properties=properties)
    return item

