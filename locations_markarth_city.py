MARKARTH_CITY_LOCATIONS = [
    {
        "id": 6001,
        "name": "Silver-Blood Inn",
        "desc": "Markarth's primary inn, owned by the powerful and often ruthless Silver-Blood family. Managed by Kleppr, it's a central hub for city life, though shadowed by the family's influence. Rumors of political maneuvering, Forsworn conspiracies, and shady deals are common here. Frabbi, Kleppr's wife, also works at the inn.",
        "travel_desc": "Markarth's inn, owned by the Silver-Bloods, managed by Kleppr.",
        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "political_intrigue_high", "silver_blood_family_owned", "rumor_source", "food_drink_vendor", "lodging_available", "economic_activity_trade_local_shady", "business_owner_silver_blood_family_kleppr_manager", "location_specific_silver_blood_inn"],
        "context_tags": ["interior", "urban_city", "tavern_type", "safe_zone_ish"],
        "demographics": {"Breton": 40, "Nord": 30, "Imperial": 10, "Orc": 10, "Redguard": 5, "Khajiit": 5},
        "fixed_npcs": [
            {"name": "Kleppr", "race": "Nord", "role": "innkeeper", "level": 6},
            {"name": "Frabbi", "race": "Nord", "role": "server", "level": 4}
        ],
        "exit_label_from_parent": "Inn Door",
        "exit_label_to_parent": "Exit Inn"
    },
    {
        "id": 6002,
        "name": "Understone Keep",
        "desc": "An ancient Dwemer fortification carved into the rock, serving as the Jarl's palace. It also houses a Dwemer museum managed by Calcelmo and provides access to the ruins of Nchuand-Zel.",
        "travel_desc": "Ancient Dwemer fortification, Jarl's palace and museum.",
        "tags": ["structure_type_fortified_keep", "structure_type_dwemer_ruin_repurposed", "government_local", "settlement_features_jarls_longhouse", "cultural_historical_significance_dwemer_ruin_site", "settlement_features_museum_dwemer", "dungeon_access_nchuand_zel", "scholar_calcelmo_residence", "dwemer_architecture_dominant"] ,
        "exit_label_from_parent": "Keep Entrance",
        "exit_label_to_parent": "Exit Keep",
        "sub_locations": [
            {
                "id": 60028,
                "name": "Nchuand-Zel",
                "desc": "The vast and ancient Dwemer city ruins located directly beneath Understone Keep in Markarth. It is a dangerous labyrinth of crumbling halls, active Dwemer machinery, Falmer, and potentially a slumbering Centurion.",
                "travel_desc": "Vast Dwemer city ruins beneath Understone Keep.",
                "tags": ["dwemer_ruin_major_city", "dungeon_large_complex", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "ancient_technology_dwemer", "cultural_historical_significance_dwemer_ruin_site", "understone_keep_access_only", "labyrinthine_layout", "chaurus_nest_potential", "treasure_cache_dwemer_artifacts_rumored"],
                "exit_label_from_parent": "Enter Ruins",
                "exit_label_to_parent": "Exit to Keep"
            }
        ]
    },
    {
        "id": 6003,
        "name": "Cidhna Mine",
        "desc": "Markarth's infamous silver mine, which also serves as a brutal prison primarily for accused Forsworn. Conditions are harsh, and escape is said to be impossible.",
        "travel_desc": "Infamous silver mine and brutal Forsworn prison.",
        "tags": ["structure_type_mine_active", "economic_activity_mining_silver", "settlement_features_prison_mine", "forsworn_incarceration", "quest_location_forsworn_uprising", "social_issue_forced_labor", "political_tension_high", "state_or_condition_current_brutal_conditions"],
        "exit_label_from_parent": "Mine Entrance",
        "exit_label_to_parent": "Exit Mine"
    },
    {
        "id": 6004,
        "name": "Arnleif and Sons Trading Company",
        "desc": "A long-standing general goods store in Markarth, currently run by the Breton Lisbet after her husband's death. The store faces challenges from Forsworn raids disrupting trade routes and the Silver-Blood family's economic dominance. Lisbet is trying to keep the business afloat and may have tasks for reliable individuals.",
        "travel_desc": "General goods store in Markarth, run by Lisbet.",
        "tags": ["structure_type_shop_building", "shop_general_goods", "economic_activity_trade_hub_local", "quest_giver_potential_lisbet_statue", "business_struggling", "business_owner_lisbet"],
        "context_tags": ["interior", "urban_city", "shop_type"],
        "fixed_npcs": [
            {"name": "Lisbet", "race": "Breton", "role": "merchant_general_goods", "level": 5}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 6005,
        "name": "The Hag's Cure",
        "desc": "Markarth's apothecary, run by the elderly Reachwoman Bothela. She is a skilled alchemist with deep knowledge of local herbs and Reach traditions, offering potions, ingredients, and perhaps some unique remedies. Her apprentice, Muiri, assists her.",
        "travel_desc": "Apothecary in Markarth, run by Bothela.",
        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "reach_culture_knowledge_source", "wise_elder_owner", "business_owner_bothela", "quest_giver_potential_bothela_muiri"],
        "context_tags": ["interior", "urban_city", "shop_type_alchemy"],
        "fixed_npcs": [
            {"name": "Bothela", "race": "Breton", "role": "alchemist_merchant_elder", "level": 8},
            {"name": "Muiri", "race": "Breton", "role": "alchemist_apprentice", "level": 3}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 6006,
        "name": "Markarth Market Square",
        "desc": "An open-air market in the heart of the city where various vendors sell their goods, often under the watchful eye of city guards. Tensions between Nords and Reach natives can sometimes spill over here.",
        "travel_desc": "Open-air market, heart of the city.",
        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "guard_patrols_heavy", "cultural_tension_point", "urban_issues_or_atmosphere_tense_atmosphere"],
        "exit_label_from_parent": "Enter Market",
        "exit_label_to_parent": "Leave Market"
    },
    {
        "id": 6007,
        "name": "Temple of Dibella",
        "desc": "A grand temple dedicated to Dibella, the goddess of beauty and love, home to several priestesses and the site of the Sybil of Dibella.",
        "travel_desc": "Grand temple dedicated to Dibella, goddess of beauty.",
        "tags": ["structure_type_temple_building", "religious_site_aedric", "dibella_shrine", "quest_location_dibella", "sacred_site_female_only_inner_sanctum", "unique_landmark_iconic", "art_beauty_focus"],
        "exit_label_from_parent": "Temple Doors",
        "exit_label_to_parent": "Exit Temple"
    },
    {
        "id": 6008,
        "name": "Ghorza's Smithy",
        "desc": "The forge and workshop of Ghorza gra-Bagol, a skilled Orc blacksmith located near the Markarth smelter. She is a stern but fair smith, dedicated to her craft and Orcish traditions. Ghorza offers smithing services, sells weapons and armor, and may provide training or tasks for those who prove their worth or knowledge of smithing.",
        "travel_desc": "Smithy of Ghorza gra-Bagol, Orc blacksmith in Markarth.",
        "tags": ["settlement_features_blacksmith_forge_active", "structure_type_shop_building", "economic_activity_smithing_production", "orc_craftsman", "skill_trainer_smithing_potential", "item_type_weapon_vendor", "item_type_armor_vendor", "business_owner_ghorza"],
        "context_tags": ["interior_shop_exterior_forge", "urban_city", "smithy_type"],
        "fixed_npcs": [
            {"name": "Ghorza gra-Bagol", "race": "Orc", "role": "blacksmith_trainer", "level": 7}
        ],
        "exit_label_from_parent": "Smithy Entrance",
        "exit_label_to_parent": "Exit Smithy"
    },
    {
        "id": 6009,
        "name": "Markarth Smelter",
        "desc": "The industrial smelter used to process ore from Cidhna Mine and other regional mining operations.",
        "travel_desc": "Industrial smelter for ore processing.",
        "tags": ["industrial_facility", "settlement_features_smelter_active", "economic_activity_mining_silver_processing", "resource_node_processing"],
        "exit_label_from_parent": "Enter Smelter Area",
        "exit_label_to_parent": "Leave Smelter Area"
    }
]