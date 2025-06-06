WHITERUN_CITY_LOCATION_DATA = {
    "id": 10,
    "name": "Whiterun",
    "desc": "A thriving trade city built around the great keep Dragonsreach, seat of Jarl Balgruuf the Greater. Its bustling market and legendary mead hall form the heart of the hold.",
    "travel_desc": "A thriving trade city built around the great keep Dragonsreach.",
    "tags": ["populated_city", "city_affiliation_whiterun_hold_capital", "economic_activity_trade_hub_major", "settlement_features_market_square", "settlement_features_jarls_longhouse", "settlement_features_companions_guild_hall", "settlement_features_temple_divines", "imperial_influence_strong", "cultural_historical_significance_nordic_settlement_ancient", "structure_type_fortified_city_wall", "cultural_historical_significance_ysgramor_related_site", "urban_issues_or_atmosphere_bustling_trade_atmosphere", "unique_landmark_iconic_dragonsreach_gildergreen"],
    "density": "bustling",
    "context_tags": ["exterior", "urban_city", "city_type"],
    "exit_label_from_parent": "Main Gate",
    "exit_label_to_parent": "Main Gate",
    "sub_locations": [
        {
            "id": 1001,
            "name": "Dragonsreach",
            "desc": "The imposing keep of the Jarl, an iconic symbol of Nord authority and power, once used to imprison the dragon Numinex in ages past.",
            "travel_desc": "The imposing keep of Whiterun's Jarl.",
            "tags": ["structure_type_fortified_keep", "settlement_features_jarls_longhouse", "cultural_historical_significance_historic_site", "government_local", "unique_landmark_iconic", "dragon_lore_ancient_site", "nordic_architecture_ancient"],
            "density": "average",
            "context_tags": ["interior", "urban_city", "keep_type", "government_building"],
            "exit_label_from_parent": "Palace Entrance",
            "exit_label_to_parent": "Exit Palace",
            "secrets": ["Hidden passage to escape the keep", "Ancient dragon lore books in the Jarl's private study"]
        },
        {
            "id": 1002,
            "name": "Jorrvaskr",
            "desc": "The ancient mead hall and headquarters of the Companions, where warriors forge bonds in battle and honor tradition.",
            "travel_desc": "Ancient mead hall, headquarters of the Companions.",
            "tags": ["structure_type_guild_hall_building", "settlement_features_companions_guild_hall", "cultural_historical_significance_historic_site", "warrior_culture_strong", "cultural_historical_significance_nordic_settlement_ancient", "faction_companions_hq"],
            "density": "average",
            "context_tags": ["interior", "urban_city", "meadhall_type", "faction_building_companions"],
            "exit_label_from_parent": "Hall Entrance",
            "exit_label_to_parent": "Exit Hall"
        },
        {
            "id": 1003,
            "name": "The Bannered Mare",
            "desc": "A bustling and well-loved tavern in the heart of Whiterun, run by the capable Hulda. Its large hearth, sturdy tables, and endless supply of Honningbrew Mead make it a popular gathering spot for warriors, travelers, and locals alike. Rumors and songs often fill the air, and one might even find a Companion or two sharing tales of their exploits. Saadia, a Redguard woman, works here, and Uthgerd the Unbroken is often seen brooding over a drink.",
            "travel_desc": "A lively tavern in the heart of Whiterun, run by Hulda.",
            "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available", "quest_giver_potential_hulda_saadia_uthgerd"],
            "density": "bustling",
            "context_tags": ["interior", "urban_city", "tavern_type", "safe_zone"],
            "demographics": {"Nord": 70, "Imperial": 10, "Breton": 5, "Redguard": 5, "Dunmer": 5, "Khajiit": 3, "Argonian": 2},
            "fixed_npcs": [
                {"name": "Hulda", "race": "Nord", "role": "innkeeper", "level": 8},
                {"name": "Saadia", "race": "Redguard", "role": "tavern_staff_server", "level": 3},
                {"name": "Uthgerd the Unbroken", "race": "Nord", "role": "warrior_patron", "level": 6}
            ],
            "exit_label_from_parent": "Tavern Door",
            "exit_label_to_parent": "Exit Tavern"
        },
        {
            "id": 1004,
            "name": "Warmaiden's",
            "desc": "The premier smithy in Whiterun, located just inside the main gate. Adrianne Avenicci can often be found working the forge outside, crafting and repairing arms and armor with skill. Her husband, Ulfberth War-Bear, manages the shop's interior, offering a fine selection of weaponry and armor. They are known for their quality goods and fair prices.",
            "travel_desc": "Whiterun's premier smithy, run by Adrianne and Ulfberth.",
            "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor", "item_type_armor_vendor", "crafting_tools", "quest_giver_potential_adrianne"],
            "density": "average",
            "context_tags": ["interior_shop_exterior_forge", "urban_city", "smithy_type"],
            "fixed_npcs": [
                {"name": "Adrianne Avenicci", "race": "Imperial", "role": "blacksmith", "level": 7},
                {"name": "Ulfberth War-Bear", "race": "Nord", "role": "merchant_blacksmith_shopkeeper", "level": 6}
            ],
            "exit_label_from_parent": "Smithy Entrance",
            "exit_label_to_parent": "Exit Smithy"
        },
        {
            "id": 1005,
            "name": "Arcadia's Cauldron",
            "desc": "A well-stocked apothecary shop run by the seemingly sweet but shrewd alchemist, Arcadia. She offers a wide variety of potions, poisons, and alchemical ingredients. Arcadia is always eager for new customers, sometimes remarking on their perceived ailments with a knowing smile, and might have tasks for those willing to gather rare components.",
            "travel_desc": "Apothecary run by Arcadia, selling potions and ingredients.",
            "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "economic_activity_alchemy_ingredient_source_rich", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_giver_potential_arcadia"],
            "density": "average",
            "context_tags": ["interior", "urban_city", "shop_type_alchemy"],
            "fixed_npcs": [
                {"name": "Arcadia", "race": "Imperial", "role": "alchemist_merchant", "level": 5}
            ],
            "exit_label_from_parent": "Shop Door",
            "exit_label_to_parent": "Exit Shop"
        },
        {
            "id": 1006,
            "name": "Temple of Kynareth",
            "desc": "A serene temple devoted to the wind and healing, centered around the ancient Gildergreen tree and frequented by worshippers.",
            "travel_desc": "Serene temple devoted to the wind and healing.",
            "tags": ["structure_type_temple_building", "settlement_features_temple_specific_god", "religious_site_aedric", "magical_properties_holy_ground_aedric", "healing_services", "kynareth_shrine", "unique_landmark_iconic_gildergreen", "quest_location_gildergreen_restoration"],
            "density": "average",
            "context_tags": ["interior", "urban_city", "temple_type", "religious_site"],
            "exit_label_from_parent": "Temple Doors",
            "exit_label_to_parent": "Exit Temple"
        },
        {
            "id": 1007,
            "name": "Plains District Market",
            "desc": "Bustling stalls offering regional produce, crafts, and curiosities, the commercial heart of Whiterun.",
            "travel_desc": "Bustling market stalls, Whiterun's commercial heart.",
            "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "item_type_food_vendor", "item_type_general_goods_vendor_stalls"],
            "density": "bustling",
            "context_tags": ["exterior", "urban_city", "market_type"],
            "exit_label_from_parent": "Enter Market",
            "exit_label_to_parent": "Leave Market Area"
        },
        {
            "id": 1008,
            "name": "The Drunken Huntsman",
            "desc": "A cozy tavern catering primarily to hunters and those of Bosmer heritage, owned and operated by the Bosmer Elrindir. Jenassa, a Dunmer mercenary skilled with a bow, can often be found here awaiting hire. The atmosphere is somewhat more subdued than the Bannered Mare, offering a quieter place for a drink and tales of the hunt.",
            "travel_desc": "Tavern popular with hunters, run by Elrindir.",
            "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "hunter_gathering_spot", "bosmer_influence_minor", "food_drink_vendor", "lodging_available", "rumor_source", "mercenary_hire_jenassa"],
            "density": "average",
            "context_tags": ["interior", "urban_city", "tavern_type", "safe_zone"],
            "demographics": {"Nord": 65, "Bosmer": 10, "Imperial": 10, "Breton": 5, "Redguard": 5, "Khajiit": 3, "Orc": 2},
            "fixed_npcs": [
                {"name": "Elrindir", "race": "Bosmer", "role": "innkeeper", "level": 6},
                {"name": "Jenassa", "race": "Dunmer", "role": "mercenary_archer", "level": 5}
            ],
            "exit_label_from_parent": "Tavern Door",
            "exit_label_to_parent": "Exit Tavern"
        },
        {
            "id": 1009,
            "name": "Belethor's General Goods",
            "desc": "A cluttered but surprisingly well-stocked general store run by the Breton merchant Belethor. He's known for his somewhat unsettling eagerness to buy and sell almost anything, famously quipping, 'Everything's for sale, my friend. Everything. If I had a sister, I'd sell her in a second.' His assistant, Sigurd, can sometimes be found chopping wood outside.",
            "travel_desc": "General store run by the eccentric Belethor.",
            "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety_extensive", "eccentric_merchant_owner_belethor", "item_type_various_vendor", "quest_giver_potential_belethor"],
            "density": "average",
            "context_tags": ["interior", "urban_city", "shop_type"],
            "fixed_npcs": [
                {"name": "Belethor", "race": "Breton", "role": "merchant_general_goods", "level": 4},
                {"name": "Sigurd", "race": "Nord", "role": "shop_assistant_woodcutter", "level": 2}
            ],
            "exit_label_from_parent": "Shop Door",
            "exit_label_to_parent": "Exit Shop"
        },
        {
            "id": 1010,
            "name": "Hall of the Dead",
            "desc": "A solemn place beneath the Temple of Kynareth where the Nords of Whiterun honor their ancestors and inter their dead.",
            "travel_desc": "Solemn place honoring Whiterun's ancestors.",
            "tags": ["structure_type_catacombs_structure", "religious_site_aedric", "nordic_burial_site_major", "arkay_presence_strong", "undead_presence_rumored_low", "quest_location_investigation_potential"],
            "density": "empty",
            "context_tags": ["interior", "urban_city", "crypt_type", "religious_site"],
            "exit_label_from_parent": "Crypt Entrance",
            "exit_label_to_parent": "Exit Crypt"
        },
        {
            "id": 1011,
            "name": "Carlotta Valentia's House",
            "desc": "The home of Carlotta Valentia, a food vendor in the market, and her daughter Mila.",
            "travel_desc": "Home of Carlotta Valentia and her daughter.",
            "tags": ["structure_type_residence", "commoner_dwelling", "family_dwelling_single_mother"],
            "density": "sparse",
            "context_tags": ["interior", "urban_city", "residence_type"],
            "exit_label_from_parent": "House Door",
            "exit_label_to_parent": "Exit House"
        },
        {
            "id": 1012,
            "name": "House Gray-Mane",
            "desc": "A prominent and respected Nord family in Whiterun, known for their traditional values and quiet concerns about Imperial policies.",
            "travel_desc": "Home of the prominent Gray-Mane family.",
            "tags": ["structure_type_residence_noble", "noble_estate_district", "nordic_culture_strong_traditional", "political_tension_high_family_feud", "stormcloak_sympathizers_potential", "political_family_gray_mane"],
            "density": "sparse",
            "context_tags": ["interior", "urban_city", "residence_type_noble"],
            "exit_label_from_parent": "House Door",
            "exit_label_to_parent": "Exit House"
        },
        {
            "id": 1013,
            "name": "House Battle-Born",
            "desc": "A wealthy and influential Nord family in Whiterun, strong supporters of the Empire and Imperial traditions.",
            "travel_desc": "Home of the wealthy Battle-Born family.",
            "tags": ["structure_type_residence_noble", "noble_estate_district", "imperial_influence_strong", "political_tension_high_family_feud", "political_family_battle_born"],
            "density": "sparse",
            "context_tags": ["interior", "urban_city", "residence_type_noble"],
            "exit_label_from_parent": "House Door",
            "exit_label_to_parent": "Exit House"
        },
        {
            "id": 1014,
            "name": "Breezehome",
            "desc": "A modest but cozy home available for purchase in Whiterun, conveniently located near the city gates.",
            "travel_desc": "Modest, cozy home available for purchase.",
            "tags": ["structure_type_residence", "player_home_available", "urban_dwelling_modest"],
            "density": "empty",
            "context_tags": ["interior", "urban_city", "residence_type_player_home"],
            "exit_label_from_parent": "House Door",
            "exit_label_to_parent": "Exit House"
        }
    ]
}