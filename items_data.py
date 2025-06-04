# items_data.py

INITIAL_INVENTORY_MAPPING = {
    # Warrior Gear
    "iron_sword": {"category": "weapon", "name": "Iron Sword", "material": "Iron", "base_damage": (8, 12), "equipment_tag": "main_hand"},
    "hide_shield": {"category": "armor", "name": "Hide Shield", "material": "Hide", "armor_rating": 5, "equipment_tag": "off_hand"},
    "iron_battleaxe": {"category": "weapon", "name": "Iron Battleaxe", "material": "Iron", "base_damage": (10, 18), "equipment_tag": "two_handed"},
    "hide_armor": {"category": "armor", "name": "Hide Cuirass", "material": "Hide", "armor_rating": 8, "equipment_tag": "chest"},
    "steel_sword": {"category": "weapon", "name": "Steel Sword", "material": "Steel", "base_damage": (10, 15), "equipment_tag": "main_hand"},
    "apprentice_tome_flames": {"category": "tome", "name": "Tome: Flames", "material": "Paper", "properties": {"spell_key": "flames"}},
    "steel_plate_armor": {"category": "armor", "name": "Steel Plate Cuirass", "material": "Steel", "armor_rating": 15, "equipment_tag": "chest"},
    "steel_shield": {"category": "armor", "name": "Steel Shield", "material": "Steel", "armor_rating": 10, "equipment_tag": "off_hand"},
    "dragonbone_greatsword": {"category": "weapon", "name": "Dragonbone Greatsword", "material": "Dragonbone", "base_damage": (25, 35), "equipment_tag": "two_handed"},
    "amulet_of_mara": {"category": "jewelry", "name": "Amulet of Mara", "material": "Gold", "equipment_tag": "amulet"},

    # Mage Gear
    "novice_robes": {"category": "armor", "name": "Novice Robes", "material": "Linen", "armor_rating": 2, "equipment_tag": "chest"},
    "apprentice_tome_firebolt": {"category": "tome", "name": "Tome: Firebolt", "material": "Paper", "properties": {"spell_key": "firebolt"}},
    "priest_robes": {"category": "armor", "name": "Priest Robes", "material": "Linen", "armor_rating": 3, "equipment_tag": "chest"},
    "apprentice_tome_healing": {"category": "tome", "name": "Tome: Healing", "material": "Paper", "properties": {"spell_key": "healing"}},
    "apprentice_robes": {"category": "armor", "name": "Apprentice Robes", "material": "Linen", "armor_rating": 4, "equipment_tag": "chest"},
    "apprentice_tome_conjure_familiar": {"category": "tome", "name": "Tome: Conjure Familiar", "material": "Paper", "properties": {"spell_key": "conjure_familiar"}},
    "fine_clothes": {"category": "armor", "name": "Fine Clothes", "material": "Linen", "armor_rating": 1, "equipment_tag": "chest"},
    "apprentice_tome_courage": {"category": "tome", "name": "Tome: Courage", "material": "Paper", "properties": {"spell_key": "courage"}},
    "alchemist_robes": {"category": "armor", "name": "Alchemist Robes", "material": "Linen", "armor_rating": 3, "equipment_tag": "chest"},
    "scroll_of_soul_trap": {"category": "scroll", "name": "Scroll of Soul Trap", "material": "Paper"},

    # Thief Gear
    "leather_armor": {"category": "armor", "name": "Leather Armor", "material": "Leather", "armor_rating": 10, "equipment_tag": "chest"},
    "iron_dagger": {"category": "weapon", "name": "Iron Dagger", "material": "Iron", "base_damage": (5, 8), "equipment_tag": "main_hand"},
    "dark_brotherhood_robes": {"category": "armor", "name": "Dark Brotherhood Robes", "material": "Leather", "armor_rating": 6, "equipment_tag": "chest"},
    "lockpick": {"category": "misc", "name": "Lockpick", "material": "Iron"},
    "hunting_bow": {"category": "weapon", "name": "Hunting Bow", "material": "Wood", "base_damage": (7, 12), "equipment_tag": "two_handed"},
    "jester_outfit": {"category": "armor", "name": "Jester Outfit", "material": "Linen", "armor_rating": 2, "equipment_tag": "chest"},
    "scroll_of_calm": {"category": "scroll", "name": "Scroll of Calm", "material": "Paper"},
    
    # Adventurer Gear
    "lute": {"category": "misc", "name": "Lute", "material": "Wood"},
    "fur_armor": {"category": "armor", "name": "Fur Armor", "material": "Fur", "armor_rating": 7, "equipment_tag": "chest"},
    "iron_axe": {"category": "weapon", "name": "Iron Axe", "material": "Iron", "base_damage": (9, 14), "equipment_tag": "main_hand"},
    "venison_steak": {"category": "food", "name": "Venison Steak", "material": "Common"},

    # NPC/Enemy Specific Gear
    "steel_axe_old": {"category": "weapon", "name": "Old Steel Axe", "material": "Steel", "base_damage": (8, 13), "equipment_tag": "main_hand"},
    "iron_mace_rusty": {"category": "weapon", "name": "Rusty Iron Mace", "material": "Iron", "base_damage": (7, 11), "equipment_tag": "main_hand"},
    "ancient_nord_sword_chipped": {"category": "weapon", "name": "Chipped Ancient Nord Sword", "material": "Iron", "base_damage": (8, 12), "equipment_tag": "main_hand"},
    "falmer_sword_crude": {"category": "weapon", "name": "Crude Falmer Sword", "material": "Chitin", "base_damage": (7, 10), "equipment_tag": "main_hand"},
    "hide_armor_scraps": {"category": "armor", "name": "Hide Armor Scraps", "material": "Hide", "armor_rating": 4, "equipment_tag": "chest"},
    "iron_armor_dented": {"category": "armor", "name": "Dented Iron Armor", "material": "Iron", "armor_rating": 7, "equipment_tag": "chest"},
    "ancient_nord_armor_piece": {"category": "armor", "name": "Ancient Nord Armor Piece", "material": "Iron", "armor_rating": 6, "equipment_tag": "chest"},
    "falmer_armor_basic": {"category": "armor", "name": "Basic Falmer Armor", "material": "Chitin", "armor_rating": 5, "equipment_tag": "chest"},
    "gem_flawless_diamond": {"category": "misc", "name": "Flawless Diamond", "material": "Misc"},
    "gem_flawless_ruby": {"category": "misc", "name": "Flawless Ruby", "material": "Misc"},
    "silver_ingot_pure": {"category": "misc", "name": "Silver Ingot", "material": "Silver"},
    "imperial_dispatch_sealed_bloodied": {"category": "misc", "name": "Bloodied Imperial Dispatch", "material": "Paper"},
    "bandit_missive": {"category": "misc", "name": "Bandit Missive", "material": "Paper", "properties": {"readable": True, "content_key": "bandit_missive_content"}},
    "wolf_trap": {"category": "misc", "name": "Wolf Trap", "material": "Iron", "properties": {"deployable": True}},
    "torn_clothing_fragment": {"category": "misc", "name": "Torn Clothing Fragment", "material": "Linen", "properties": {"quest_item": True}},
    "rat_poison_ingredients": {"category": "ingredient", "name": "Rat Poison Ingredients", "material": "Misc", "properties": {"crafting_component": True}},
    "caravan_manifest": {"category": "misc", "name": "Caravan Manifest", "material": "Paper", "properties": {"readable": True, "content_key": "caravan_manifest_content"}},
    "stolen_cult_artifact": {"category": "misc", "name": "Stolen Cult Artifact", "material": "Ancient", "properties": {"quest_item": True, "value_modifier": 1.5}},
    "rare_trade_item": {"category": "misc", "name": "Rare Trade Good", "material": "Exotic", "properties": {"value_modifier": 2.0}},
    "apprentice_tome_random": {"category": "tome", "name": "Apprentice Random Tome", "material": "Paper", "properties": {"spell_key": "random_apprentice_spell"}}, 
    "beast_fang_trophy": {"category": "misc", "name": "Beast Fang Trophy", "material": "Bone", "properties": {"quest_item": True}},
    "steel_sword": {"category": "weapon", "name": "Steel Sword", "material": "Steel", "base_damage": (10,15), "equipment_tag": "main_hand"}, 
    "cleansing_ritual_scroll": {"category": "scroll", "name": "Scroll of Cleansing Ritual", "material": "Paper", "properties": {"spell_effect": "area_cleanse_undead"}},
    "power_siphon_tome": {"category": "tome", "name": "Tome of Power Siphoning", "material": "Paper", "properties": {"spell_key": "power_siphon_self"}},
    "amulet_of_mara": {"category": "jewelry", "name": "Amulet of Mara", "material": "Silver", "equipment_tag": "amulet", "properties": {"effect": "speech_boost", "magnitude": 5}}, 
    "staff_of_nightmares": {"category": "weapon", "name": "Staff of Nightmares", "material": "Ebony", "base_damage": (8,12), "equipment_tag": "two_handed", "enchantment": "Fear", "properties": {"spell_on_hit": "fear_lvl_10"}},
    "troll_skull_trophy": {"category": "misc", "name": "Troll Skull Trophy", "material": "Bone", "properties": {"quest_item": True}},
    "glyph_of_unraveling": {"category": "misc", "name": "Glyph of Unraveling", "material": "Stone", "properties": {"quest_item": True, "arcane_significance": True}},
    "glowing_fungus_rare": {"category": "ingredient", "name": "Rare Glowing Fungus", "material": "Organic", "properties": {"alchemy_effect_1": "fortify_magicka"}},
    "enchanted_ring_magicka": {"category": "jewelry", "name": "Ring of Minor Magicka", "material": "Silver", "equipment_tag": "ring", "enchantment": "Fortify Magicka", "properties": {"magicka_boost": 20}},
    "vampire_bane_dagger": {"category": "weapon", "name": "Vampire's Bane Dagger", "material": "Silver", "base_damage": (7,10), "equipment_tag": "main_hand", "enchantment": "Damage Undead", "properties": {"bonus_vs_vampires": 10}},
    "horn_of_jurgen_windcaller": {"category": "misc", "name": "Horn of Jurgen Windcaller", "material": "Ancient Nord Metal", "properties": {"quest_item": True, "historical_artifact": True}},
    "shout_knowledge_scroll": {"category": "scroll", "name": "Scroll of Dragon Shout Insight", "material": "Paper", "properties": {"unlocks_word_knowledge": True}}, 
    "silver_locket_ancient_cursed_sorrow": {"category": "jewelry", "name": "Cursed Silver Locket", "material": "Silver", "equipment_tag": "amulet", "properties": {"cursed": True, "quest_item": True}},
    "amulet_of_arkay": {"category": "jewelry", "name": "Amulet of Arkay", "material": "Silver", "equipment_tag": "amulet", "properties": {"effect": "health_boost", "magnitude": 10}},
    "shrouded_armor_set": {"category": "armor", "name": "Shrouded Armor Set Piece", "material": "Leather", "armor_rating": 7, "equipment_tag": "chest", "properties": {"stealth_bonus": True}}, 
    "silver_blood_goblet": {"category": "misc", "name": "Silver-Blood Goblet", "material": "Silver", "properties": {"quest_item": True, "valuable": True}},
    "orc_sacred_totem": {"category": "misc", "name": "Orc Sacred Totem", "material": "Wood", "properties": {"quest_item": True, "tribal_significance": True}},
    "orcish_weapon_masterwork": {"category": "weapon", "name": "Masterwork Orcish War Axe", "material": "Orcish", "base_damage": (14,20), "equipment_tag": "main_hand", "properties": {"quality": "masterwork"}},
    "amulet_of_arvak": {"category": "jewelry", "name": "Amulet of Arvak", "material": "Bone", "equipment_tag": "amulet", "properties": {"quest_item": True, "necromantic_aura": True}}, 
    "butchers_blade_unique": {"category": "weapon", "name": "The Butcher's Cleaver", "material": "Iron", "base_damage": (10,14), "equipment_tag": "main_hand", "properties": {"unique": True, "bleed_damage": 3}},
    "pure_ebony_vein": {"category": "misc", "name": "Pure Ebony Vein Sample", "material": "Ebony", "properties": {"quest_item": True, "valuable_ore": True}},
    "orcish_malacath_blade": {"category": "weapon", "name": "Blade of Malacath's Fury", "material": "Orcish", "base_damage": (16,24), "equipment_tag": "two_handed", "enchantment": "Absorb Stamina", "properties": {"unique": True, "orc_blessing": True}},
    "rare_alchemy_ingredients_bundle": {"category": "misc", "name": "Bundle of Rare Alchemy Ingredients", "material": "Organic", "properties": {"contains_multiple_ingredients": True}},
    "stolen_ring_planted": {"category": "jewelry", "name": "Stolen Silver Ring", "material": "Silver", "equipment_tag": "ring", "properties": {"quest_item": True, "evidence": True}},
    "thieves_guild_armor_set_basic": {"category": "armor", "name": "Thieves Guild Armor Piece", "material": "Leather", "armor_rating": 8, "equipment_tag": "chest", "properties": {"stealth_bonus": True, "faction_gear": "thieves_guild"}},
    "maven_black_briar_ledger": {"category": "misc", "name": "Maven Black-Briar's Ledger", "material": "Paper", "properties": {"readable": True, "incriminating_evidence": True}},
    "potent_nonlethal_poison": {"category": "potion", "name": "Potent (Non-Lethal) Poison", "material": "Liquid", "properties": {"effect": "sickness", "duration": "1_day"}},
    "black_briar_secret_mead_recipe": {"category": "misc", "name": "Black-Briar Secret Mead Recipe", "material": "Paper", "properties": {"readable": True, "trade_secret": True}},
    "unique_black_briar_mead_bottle_empty": {"category": "misc", "name": "Empty Black-Briar Reserve Bottle", "material": "Glass", "properties": {"collectible": True}},
    "hafjorgs_mining_journal": {"category": "misc", "name": "Hafjorg's Mining Journal", "material": "Paper", "properties": {"readable": True, "quest_item": True}},
    "gold_ore_samples_large": {"category": "misc", "name": "Large Gold Ore Samples", "material": "Gold Ore", "properties": {"valuable_resource": True}},
    "king_olafs_verse_lost": {"category": "misc", "name": "King Olaf's Verse (Lost)", "material": "Parchment", "properties": {"quest_item": True, "historical_document": True}},
    "bards_college_tunic_fine": {"category": "armor", "name": "Fine Bards College Tunic", "material": "Linen", "armor_rating": 2, "equipment_tag": "chest", "properties": {"faction_gear": "bards_college", "speech_boost": 5}},
    "thalmor_intelligence_dossier_skyrim": {"category": "misc", "name": "Thalmor Intelligence Dossier", "material": "Paper", "properties": {"readable": True, "sensitive_information": True}},
    "elven_dagger_enchanted_soul_trap": {"category": "weapon", "name": "Elven Dagger of Soul Snaring", "material": "Elven", "base_damage": (8,11), "equipment_tag": "main_hand", "enchantment": "Soul Trap"},
    "pirate_coded_message_eec": {"category": "misc", "name": "Coded Pirate Message", "material": "Parchment", "properties": {"readable_encrypted": True}},
    "stolen_eec_shipment_manifest": {"category": "misc", "name": "Stolen EEC Shipment Manifest", "material": "Paper", "properties": {"readable": True, "evidence_theft": True}},
    "east_empire_pendant_valuable": {"category": "jewelry", "name": "East Empire Company Pendant", "material": "Gold", "equipment_tag": "amulet", "properties": {"valuable": True, "faction_symbol": "east_empire_company"}},
    "skull_of_corruption": {"category": "misc", "name": "Skull of Corruption", "material": "Daedric Artifact", "properties": {"daedric_artifact": True, "unique": True, "spell_on_use": "corruption_dream"}},
    "potion_resist_frost_superior": {"category": "potion", "name": "Superior Potion of Resist Frost", "material": "Liquid", "properties": {"effect": "resist_frost", "magnitude": 50}},
    "amulet_of_jyrik_gauldurson": {"category": "jewelry", "name": "Amulet of Jyrik Gauldurson", "material": "Ancient Nord Gold", "equipment_tag": "amulet", "properties": {"quest_item": True, "magicka_drain_aura": True}}, 
    "adept_destruction_robe": {"category": "armor", "name": "Adept Robes of Destruction", "material": "Linen", "armor_rating": 3, "equipment_tag": "chest", "enchantment": "Fortify Destruction", "properties": {"magicka_regen_bonus": 75}},
    "void_salts_pure": {"category": "ingredient", "name": "Pure Void Salts", "material": "Crystalline", "properties": {"alchemy_effect_1": "resist_shock", "alchemy_effect_2": "damage_magicka"}},
    "deathbell_potent_sample": {"category": "ingredient", "name": "Potent Deathbell Sample", "material": "Organic", "properties": {"alchemy_effect_1": "damage_health", "alchemy_effect_2": "slow"}},
    "enchanted_ring_conjuration": {"category": "jewelry", "name": "Ring of Minor Conjuration", "material": "Silver", "equipment_tag": "ring", "enchantment": "Fortify Conjuration", "properties": {"conjuration_skill_boost": 5}},
    "silver_sword_enchanted_undead": {"category": "weapon", "name": "Silver Sword of Undead Smiting", "material": "Silver", "base_damage": (9,13), "equipment_tag": "main_hand", "enchantment": "Turn Undead Lesser"},
    "note_from_friend_horn_location": {"category": "misc", "name": "Note from a Friend (Horn)", "material": "Paper", "properties": {"readable": True, "quest_item": True}},
    "horn_of_jurgen_windcaller_actual": {"category": "misc", "name": "Horn of Jurgen Windcaller", "material": "Ancient Nord Metal", "properties": {"quest_item": True, "historical_artifact": True, "shout_related": True}}, 
    "silver_locket_kael_cursed": {"category": "jewelry", "name": "Kael's Cursed Locket", "material": "Silver", "equipment_tag": "amulet", "properties": {"cursed": True, "quest_item": True, "emits_sorrow": True}},
    "amulet_of_arkay_enhanced": {"category": "jewelry", "name": "Blessed Amulet of Arkay", "material": "Silver", "equipment_tag": "amulet", "enchantment": "Fortify Health", "properties": {"health_boost": 25, "undead_turn_chance": 0.05}},
    "butchers_journal_set": {"category": "misc", "name": "Butcher's Journal", "material": "Paper", "properties": {"readable": True, "incriminating_evidence": True, "quest_item": True}}, 
    "strange_amulet_necromancer": {"category": "jewelry", "name": "Strange Necromantic Amulet", "material": "Bone", "equipment_tag": "amulet", "properties": {"quest_item": True, "dark_magic_aura": True}},
    "necromancer_amulet_true_or_hjerm_key": {"category": "jewelry", "name": "Necromancer's Amulet", "material": "Ebony", "equipment_tag": "amulet", "enchantment": "Fortify Conjuration & Magicka", "properties": {"unique": True, "conjuration_skill_boost": 15, "magicka_boost": 50, "health_regen_penalty": -25}}, 
    "heart_of_ebony_pure": {"category": "misc", "name": "Heart of Pure Ebony", "material": "Ebony", "properties": {"quest_item": True, "valuable_crafting_material": True, "malacath_offering": True}},
    "orcish_battleaxe_ebony_infused": {"category": "weapon", "name": "Ebony-Infused Orcish Battleaxe", "material": "Orcish", "base_damage": (18,28), "equipment_tag": "two_handed", "properties": {"unique": True, "ebony_core_strength": True}},
    "hagraven_ritual_altar": {"category": "misc", "name": "Hagraven Ritual Altar (Destroyable)", "material": "Stone", "properties": {"interactable_quest_objective": True}}, 
    "madesis_silver_ring_stolen": {"category": "jewelry", "name": "Madesi's Silver Ring", "material": "Silver", "equipment_tag": "ring", "properties": {"quest_item": True, "stolen_goods": True}},
    "armor_of_the_old_gods_set": {"category": "armor", "name": "Armor of the Old Gods Piece", "material": "Forsworn Hide", "armor_rating": 10, "equipment_tag": "chest", "enchantment": "Fortify Light Armor & Magic Resist", "properties": {"forsworn_leader_gear": True}},
    "silver_blood_family_ring_enchanted": {"category": "jewelry", "name": "Silver-Blood Family Signet Ring", "material": "Silver", "equipment_tag": "ring", "enchantment": "Fortify Speech", "properties": {"speech_boost": 10, "faction_symbol": "silver_blood"}},
    "gold_ingot_pile": {"category": "misc", "name": "Pile of Gold Ingots", "material": "Gold", "properties": {"currency_large_amount": True, "value_raw": 500}},
    "forgemasters_fingers_tongs": {"category": "misc", "name": "Forgemaster's Fingers", "material": "Dwarven Metal", "properties": {"quest_item": True, "orc_artifact": True, "smithing_tool_sacred": True}},
    "orcish_armor_improved_set_piece": {"category": "armor", "name": "Improved Orcish Armor Piece", "material": "Orcish", "armor_rating": 18, "equipment_tag": "chest", "properties": {"quality": "improved", "faction_gear": "orc_stronghold"}},
# New Items
    "stormfang": {"category": "weapon", "name": "Stormfang", "material": "Elven", "base_damage": (10, 15), "equipment_tag": "main_hand", "enchantment": "Shock Damage", "properties": {"unique": True}},
    "nightweave_cloak": {"category": "armor", "name": "Nightweave Cloak", "material": "Linen", "armor_rating": 5, "equipment_tag": "chest", "properties": {"stealth_bonus": True, "rare": True}},
    "ring_of_whispers": {"category": "jewelry", "name": "Ring of Whispers", "material": "Silver", "equipment_tag": "ring", "enchantment": "Fortify Illusion", "properties": {"illusion_boost": 10}},
"amulet_of_protection": {"category": "jewelry", "name": "Amulet of Protection", "material": "Silver", "equipment_tag": "amulet", "properties": {"armor_boost": 5}},
    "elixir_of_shadows": {"category": "potion", "name": "Elixir of Shadows", "material": "Liquid", "properties": {"effect": "invisibility", "duration": 30}},
}

INITIAL_INVENTORY_MAPPING.update({
    "steel_sword_enchanted": {"category": "weapon", "name": "Enchanted Steel Sword", "material": "Steel", "base_damage": (12, 17), "equipment_tag": "main_hand", "enchantment": "Fire Damage"},
    "hide_shield_reinforced": {"category": "armor", "name": "Reinforced Hide Shield", "material": "Hide", "armor_rating": 7, "equipment_tag": "off_hand"},
    "elven_dagger_swift": {"category": "weapon", "name": "Swift Elven Dagger", "material": "Elven", "base_damage": (9, 12), "equipment_tag": "main_hand", "enchantment": "Paralyze"},
    "dwarven_armor_resilient": {"category": "armor", "name": "Resilient Dwarven Armor", "material": "Dwarven", "armor_rating": 18, "equipment_tag": "chest", "enchantment": "Resist Magic"},
    "dragonbone_greatsword_soul": {"category": "weapon", "name": "Soulrend Dragonbone Greatsword", "material": "Dragonbone", "base_damage": (28, 38), "equipment_tag": "two_handed", "enchantment": "Soul Trap", "properties": {"unique": True}},
    "daedric_armor_immortal": {"category": "armor", "name": "Immortality Daedric Armor", "material": "Daedric", "armor_rating": 25, "equipment_tag": "chest", "enchantment": "Absorb Health", "properties": {"unique": True}},
})

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
    "Bread": 0.5, "Cheese Wheel": 1.0, "Ale": 1.0, "Sweetroll": 0.3, "Cabbage": 0.7,
    "Potato": 0.4, "Venison Steak": 0.6, "Apple": 0.3
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
    "Ring": 50, "Amulet": 75, "Locket": 60, "Pendant": 40, "Shield": 35,
    "Bread": 2, "Cheese Wheel": 5, "Ale": 3, "Sweetroll": 4, "Cabbage": 1,
    "Potato": 1, "Venison Steak": 6, "Apple": 2
}

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
        "Imp Stool": {"effect": "damage_health", "magnitude": (2, 4)},
        "Blisterwort": {"effect": "fortify_strength", "magnitude": (1, 2)},
        "Deathbell": {"effect": "damage_health", "magnitude": (3, 5)},
        "Nightshade": {"effect": "damage_health", "magnitude": (4, 6)},
        "Jazbay Grapes": {"effect": "restore_magicka", "magnitude": (2, 4)},
        "Garlic": {"effect": "resist_poison", "magnitude": 5},
        "Rat Poison Ingredients": {"effect": "damage_health", "magnitude": (6, 8)},
        "Rare Glowing Fungus": {"effect": "fortify_magicka", "magnitude": (3, 5)},
        "Pure Void Salts": {"effect": "resist_shock", "magnitude": 10},
        "Potent Deathbell Sample": {"effect": "damage_health", "magnitude": (7, 9)}
    },
    "food": {
        "Bread": {"effect": "restore_fatigue", "magnitude": (1, 2)},
        "Cheese Wheel": {"effect": "restore_health", "magnitude": (3, 5)},
        "Ale": {"effect": "restore_fatigue", "magnitude": (2, 4)},
        "Sweetroll": {"effect": "restore_health", "magnitude": (4, 6)},
        "Cabbage": {"effect": "restore_fatigue", "magnitude": (1, 3)},
        "Potato": {"effect": "restore_health", "magnitude": (2, 4)},
        "Venison Steak": {"effect": "restore_health", "magnitude": (5, 7)},
        "Apple": {"effect": "restore_fatigue", "magnitude": (3, 5)}
    }
}
WEIGHT_MULTIPLIERS = {
    "Iron": 1.0, "Steel": 1.2, "Gold": 1.8, "Glass": 0.8, "Ebony": 2.0, "Daedric": 2.8,
}