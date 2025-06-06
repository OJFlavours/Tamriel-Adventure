# items_data.py

INITIAL_INVENTORY_MAPPING = {
    # Warrior Gear
    "iron_sword": {"category": "weapon", "name": "Iron Sword", "material": "Iron", "base_damage": (8, 12), "equipment_tag": "main_hand"},
    "hide_shield": {"category": "armor", "name": "Hide Shield", "material": "Hide", "armor_rating": 5, "equipment_tag": "off_hand"},
    "iron_battleaxe": {"category": "weapon", "name": "Iron Battleaxe", "material": "Iron", "base_damage": (10, 18), "equipment_tag": "two_handed"},
    "hide_armor": {"category": "armor", "name": "Hide Cuirass", "material": "Hide", "armor_rating": 8, "equipment_tag": "chest"},
    
    # Mage Gear
    "novice_robes": {"category": "armor", "name": "Novice Robes", "material": "Linen", "armor_rating": 2, "equipment_tag": "chest"},
    "apprentice_tome_firebolt": {"category": "tome", "name": "Tome: Firebolt", "material": "Paper", "properties": {"spell_key": "firebolt"}},
    
    # Thief Gear
    "leather_armor": {"category": "armor", "name": "Leather Armor", "material": "Leather", "armor_rating": 10, "equipment_tag": "chest"},
    "dark_brotherhood_robes": {"category": "armor", "name": "Dark Brotherhood Robes", "material": "Linen", "armor_rating": 12, "equipment_tag": "chest"},
    "iron_dagger": {"category": "weapon", "name": "Iron Dagger", "material": "Iron", "base_damage": (5, 8), "equipment_tag": "main_hand"},
    
    # Adventurer Gear
    "lute": {"category": "misc", "name": "Lute", "material": "Wood"},
    "fur_armor": {"category": "armor", "name": "Fur Armor", "material": "Fur", "armor_rating": 7, "equipment_tag": "chest"},
    
    "iron_axe": {"category": "weapon", "name": "Iron Axe", "material": "Iron", "base_damage": (6, 10), "equipment_tag": "main_hand"},
    "venison_steak": {"category": "food", "name": "Venison Steak", "material": "Meat", "properties": {"effect": "restore_health", "magnitude": 7}},
"steel_sword": {"category": "weapon", "name": "Steel Sword", "material": "Steel", "base_damage": (10, 14), "equipment_tag": "main_hand"},
    "apprentice_tome_flames": {"category": "tome", "name": "Tome: Flames", "material": "Paper", "properties": {"spell_key": "flames"}},
    "steel_plate_armor": {"category": "armor", "name": "Steel Plate Armor", "material": "Steel", "armor_rating": 15, "equipment_tag": "chest"},
    "steel_shield": {"category": "armor", "name": "Steel Shield", "material": "Steel", "armor_rating": 8, "equipment_tag": "off_hand"},
    "dragonbone_greatsword": {"category": "weapon", "name": "Dragonbone Greatsword", "material": "Dragonbone", "base_damage": (20, 30), "equipment_tag": "two_handed"},
    "amulet_of_mara": {"category": "jewelry", "name": "Amulet of Mara", "material": "Silver", "properties": {"effect": "restore_health", "magnitude": 10}},
    "priest_robes": {"category": "armor", "name": "Priest Robes", "material": "Linen", "armor_rating": 5, "equipment_tag": "chest"},
    "apprentice_tome_healing": {"category": "tome", "name": "Tome: Healing", "material": "Paper", "properties": {"spell_key": "healing"}},
    "apprentice_robes": {"category": "armor", "name": "Apprentice Robes", "material": "Linen", "armor_rating": 3, "equipment_tag": "chest"},
    "apprentice_tome_conjure_familiar": {"category": "tome", "name": "Tome: Conjure Familiar", "material": "Paper", "properties": {"spell_key": "conjure_familiar"}},
    "fine_clothes": {"category": "armor", "name": "Fine Clothes", "material": "Silk", "armor_rating": 1, "equipment_tag": "chest"},
    "apprentice_tome_courage": {"category": "tome", "name": "Tome: Courage", "material": "Paper", "properties": {"spell_key": "courage"}},
    "alchemist_robes": {"category": "armor", "name": "Alchemist Robes", "material": "Linen", "armor_rating": 4, "equipment_tag": "chest"},
    "scroll_of_soul_trap": {"category": "scroll", "name": "Scroll of Soul Trap", "material": "Parchment", "properties": {"spell_key": "soul_trap"}},
    "lockpick": {"category": "misc", "name": "Lockpick", "material": "Iron"},
    "hunting_bow": {"category": "weapon", "name": "Hunting Bow", "material": "Wood", "base_damage": (6, 9), "equipment_tag": "two_handed"},
    "jester_outfit": {"category": "armor", "name": "Jester Outfit", "material": "Cloth", "armor_rating": 2, "equipment_tag": "chest"},
    "scroll_of_calm": {"category": "scroll", "name": "Scroll of Calm", "material": "Parchment", "properties": {"spell_key": "calm"}},
}

# Adding missing item definitions
INITIAL_INVENTORY_MAPPING["iron_mace_rusty"] = {"category": "weapon", "name": "Rusty Iron Mace", "material": "Iron", "base_damage": (4, 8), "equipment_tag": "main_hand", "properties": {"is_rusty": True}}
INITIAL_INVENTORY_MAPPING["ancient_nord_armor_piece"] = {"category": "armor", "name": "Ancient Nord Armor Piece", "material": "Ancient Nord Metal", "armor_rating": 12, "equipment_tag": "chest", "properties": {"is_ancient": True}}

CONSUMABLE_EFFECT_POOLS = {
    "potion": {
        "Potion of Minor Healing": {"effect": "restore_health", "magnitude": (10, 15)},
        "Potion of Healing": {"effect": "restore_health", "magnitude": (20, 30)},
        "Potion of Greater Healing": {"effect": "restore_health", "magnitude": (40, 60)},
        "Potion of Minor Magicka": {"effect": "restore_magicka", "magnitude": (10, 15)},
        "Potion of Magicka": {"effect": "restore_magicka", "magnitude": (20, 30)},
        "Potion of Greater Magicka": {"effect": "restore_magicka", "magnitude": (40, 60)},
        "Potion of Minor Stamina": {"effect": "restore_fatigue", "magnitude": (10, 15)},
        "Potion of Stamina": {"effect": "restore_fatigue", "magnitude": (20, 30)},
        "Potion of Greater Stamina": {"effect": "restore_fatigue", "magnitude": (40, 60)},
        "Potion of Resist Fire": {"effect": "resist_fire", "magnitude": 25},
        "Potion of Resist Frost": {"effect": "resist_frost", "magnitude": 25},
        "Potion of Resist Shock": {"effect": "resist_shock", "magnitude": 25},
        "Potion of Cure Poison": {"effect": "cure_poison", "magnitude": 0},
        "Potent (Non-Lethal) Poison": {"effect": "damage_health", "magnitude": (5, 10)},
        "Superior Potion of Resist Frost": {"effect": "resist_frost", "magnitude": 50}
    },
    "ingredient": {
        "Blue Mountain Flower": {"effect": "restore_health", "magnitude": (1, 3)},
        "Imp Stool": {"effect": "damage_health", "magnitude": (1, 2)},
        "Blisterwort": {"effect": "fortify_onehanded", "magnitude": (1, 2)},
        "Deathbell": {"effect": "damage_stamina", "magnitude": (2, 4)},
        "Nightshade": {"effect": "damage_health", "magnitude": (3, 5)},
        "Jazbay Grapes": {"effect": "restore_magicka", "magnitude": (2, 3)},
        "Garlic": {"effect": "resist_poison", "magnitude": 5},
        "Rat Poison Ingredients": {"effect": "damage_health", "magnitude": (4, 6)},
        "Rare Glowing Fungus": {"effect": "restore_magicka", "magnitude": (3, 5)},
        "Pure Void Salts": {"effect": "restore_magicka", "magnitude": (5, 7)},
        "Potent Deathbell Sample": {"effect": "damage_health", "magnitude": (5, 7)}
    },
    "food": {
        "Bread": {"effect": "restore_fatigue", "magnitude": 2},
        "Cheese Wheel": {"effect": "restore_health", "magnitude": 5},
        "Ale": {"effect": "restore_fatigue", "magnitude": 3},
        "Sweetroll": {"effect": "restore_health", "magnitude": 4},
        "Cabbage": {"effect": "restore_fatigue", "magnitude": 2},
        "Potato": {"effect": "restore_health", "magnitude": 3},
        "Venison Steak": {"effect": "restore_health", "magnitude": 7},
        "Apple": {"effect": "restore_fatigue", "magnitude": 1}
    }
}

MATERIALS = ["Iron", "Steel", "Silver", "Gold", "Glass", "Ebony", "Dragonbone",
             "Orcish", "Dwarven", "Elven", "Falmer", "Nordic", "Leather",
             "Hide", "Fur", "Chitin", "Daedric", "Stalhrim", "Wood", "Paper", "Linen", "Common", "Ancient", "Exotic", "Bone", "Organic", "Liquid", "Crystalline", "Stone", "Parchment", "Ancient Nord Metal", "Ancient Nord Gold", "Forsworn Hide", "Dwarven Metal", "Gold Ore", "Ebony Ore", "Daedric Artifact", "Misc"]

WEAPONS = ["Sword", "Axe", "Mace", "Dagger", "Bow", "Staff", "Greatsword",
           "Warhammer", "Battleaxe", "Cleaver", "War Axe"]

ARMORS = ["Helmet", "Cuirass", "Gauntlets", "Greaves", "Boots", "Shield", "Robes", "Clothes", "Outfit", "Tunic", "Armor Piece"]

JEWELRY = ["Ring", "Amulet", "Locket", "Pendant"]

FOODS = ["Bread", "Cheese Wheel", "Ale", "Sweetroll", "Cabbage", "Potato", "Venison Steak", "Apple"]

POTIONS = ["Potion of Minor Healing", "Potion of Healing", "Potion of Greater Healing",
           "Potion of Minor Magicka", "Potion of Magicka", "Potion of Greater Magicka",
           "Potion of Minor Stamina", "Potion of Stamina", "Potion of Greater Stamina",
           "Potion of Resist Fire", "Potion of Resist Frost", "Potion of Resist Shock",
           "Potion of Cure Poison", "Potent (Non-Lethal) Poison", "Superior Potion of Resist Frost"]

INGREDIENTS = ["Blue Mountain Flower", "Imp Stool", "Blisterwort", "Deathbell",
               "Nightshade", "Jazbay Grapes", "Garlic", "Rat Poison Ingredients", "Rare Glowing Fungus", "Pure Void Salts", "Potent Deathbell Sample"]

SCROLLS = ["Scroll of Fireball", "Scroll of Frost", "Scroll of Healing",
           "Scroll of Courage", "Scroll of Soul Trap", "Scroll of Calm", "Scroll of Cleansing Ritual", "Scroll of Dragon Shout Insight"]

SOUL_GEMS = ["Petty Soul Gem", "Lesser Soul Gem", "Common Soul Gem", "Greater Soul Gem",
             "Grand Soul Gem", "Black Soul Gem"]

MISC = ["Lockpick", "Book", "Map", "Lute", "Bandit Missive", "Wolf Trap", "Torn Clothing Fragment", "Caravan Manifest", "Stolen Cult Artifact", "Rare Trade Good", "Beast Fang Trophy", "Troll Skull Trophy", "Glyph of Unraveling", "Horn of Jurgen Windcaller", "Shout Knowledge Scroll", "Silver-Blood Goblet", "Orc Sacred Totem", "Amulet of Arvak", "Butcher's Journal", "Strange Necromantic Amulet", "Pure Ebony Vein Sample", "Heart of Pure Ebony", "Bundle of Rare Alchemy Ingredients", "Stolen Silver Ring", "Maven Black-Briar's Ledger", "Black-Briar Secret Mead Recipe", "Empty Black-Briar Reserve Bottle", "Hafjorg's Mining Journal", "Large Gold Ore Samples", "King Olaf's Verse (Lost)", "Thalmor Intelligence Dossier", "Coded Pirate Message", "Stolen EEC Shipment Manifest", "Skull of Corruption", "Amulet of Jyrik Gauldurson", "Note from a Friend (Horn)", "Horn of Jurgen Windcaller", "Pile of Gold Ingots", "Forgemaster's Fingers", "Flawless Diamond", "Flawless Ruby", "Silver Ingot", "Bloodied Imperial Dispatch"]

TOMES = ["Tome: Flames", "Tome: Firebolt", "Tome: Healing", "Tome: Conjure Familiar", "Tome: Courage", "Apprentice Random Tome", "Tome of Power Siphoning"]


# Data moved from items.py
BASE_WEIGHTS = {
    "Sword": 3.0, "Axe": 4.0, "Mace": 5.0, "Dagger": 1.0, "Bow": 2.0, "Staff": 2.5,
    "Helmet": 2.0, "Cuirass": 7.0, "Gauntlets": 1.5, "Greaves": 3.0, "Boots": 2.0,
    "Ring": 0.1, "Amulet": 0.1, "Locket": 0.1, "Pendant": 0.1, "Shield": 5.0,
    "Bread": 0.5, "Cheese Wheel": 5.0, "Ale": 3, "Sweetroll": 0.3, "Cabbage": 0.7,
    "Potato": 0.4, "Venison Steak": 0.6, "Apple": 2
}

VALUE_MULTIPLIERS = {
    "Iron": 1.0, "Steel": 1.5, "Silver": 2.0, "Gold": 3.0, "Glass": 2.5, "Ebony": 4.0,
    "Dragonbone": 6.0, "Orcish": 3.5, "Dwarven": 3.0, "Elven": 4.5, "Falmer": 2.0,
    "Nordic": 2.5, "Leather": 0.8, "Hide": 0.5, "Fur": 0.7, "Chitin": 1.2,
    "Daedric": 8.0, "Stalhrim": 5.0
}

BASE_VALUES = {
    "Sword": 20, "Axe": 22, "Mace": 25, "Dagger": 10, "Bow": 30, "Staff": 40,
    "Helmet": 30, "Cuirass": 50, "Gauntlets": 20, "Greaves": 30, "Boots": 20,
    "Ring": 50, "Amulet": 75, "Locket": 60, "Pendant": 40
}