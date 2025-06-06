from locations_whiterun_city import WHITERUN_CITY_LOCATION_DATA

WHITERUN_LOCATIONS = [
    # WHITERUN HOLD
    {
        "id": 1,
        "name": "Whiterun Hold",
        "desc": "The fertile heartland of Skyrim, marked by golden plains and the bustling city of Whiterun. A center of commerce, Imperial influence, and ancient Nordic tradition.",
        "travel_desc": "The fertile heartland of Skyrim, a center of commerce and tradition.",
        "tags": ["hold", "terrain_plains", "central_location", "economic_activity_trade_hub_regional", "nordic_culture_strong", "imperial_influence_moderate", "climate_temperate", "economic_activity_farming_crops", "economic_activity_farming_livestock", "state_or_condition_current_politically_stable", "travel_hub_major"],
        "context_tags": ["exterior", "hold_capital_type", "wilderness", "plains_type"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "links": [
                {"name": "The Rift", "connection_type": "Road"},
                {"name": "Eastmarch", "connection_type": "Road"},
                {"name": "The Reach", "connection_type": "Road"},
                {"name": "Haafingar", "connection_type": "Road"},
                {"name": "Falkreath Hold", "connection_type": "Road"},
                {"name": "The Pale", "connection_type": "Road"},
                {"name": "Riverwood", "connection_type": "Path"},
                {"name": "Rorikstead", "connection_type": "Path"},
                {"name": "Helgen", "connection_type": "Path"}
            ]
        },
        "travel_time": 2, # Whiterun Hold takes longer to traverse
        "sub_locations": [
            WHITERUN_CITY_LOCATION_DATA,
            {
                "id": 11,
                "name": "Riverwood",
                "desc": "A quaint logging village along the White River, known for its simplicity and rustic charm, often the first stop for travelers from the south.",
                "travel_desc": "Quaint logging village along the White River.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_logging_timber", "terrain_river_delta", "climate_temperate", "terrain_forest", "travel_hub_minor", "quest_location_main_story_early_dragon_attack_aftermath_potential"],
                "context_tags": ["exterior", "rural_village", "village_type"],
                "exit_label_from_parent": "Path",
                "exit_label_to_parent": "Path",
                "sub_locations": [
                    {
                        "id": 1101,
                        "name": "Sleeping Giant Inn",
                        "desc": "A cozy and welcoming inn at the heart of Riverwood, run by the Nord couple Orgnar and Delphine (though Delphine maintains a low profile). It's a common stop for travelers heading to or from Whiterun and often has patrons sharing news from the road or local gossip. Delphine might have a particular interest in news about dragons.",
                        "travel_desc": "Cozy inn in Riverwood, run by Orgnar and Delphine.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available", "quest_location_main_story_early_delphine"],
                        "context_tags": ["interior", "village_type", "tavern_type", "safe_zone"],
                        "demographics": {"Nord": 75, "Imperial": 10, "Breton": 5, "Bosmer": 5, "Redguard": 5},
                        "fixed_npcs": [
                            {"name": "Orgnar", "race": "Nord", "role": "innkeeper", "level": 5},
                            {"name": "Delphine", "race": "Breton", "role": "innkeeper_secretive", "level": 15}
                        ],
                        "exit_label_from_parent": "Inn Door",
                        "exit_label_to_parent": "Exit Inn"
                    },
                    {
                        "id": 1102,
                        "name": "Riverwood Trader",
                        "desc": "The main general goods store in Riverwood, run by the Imperial Lucan Valerius and his sister Camilla Valerius. They offer a variety of essential supplies, tools, and some local crafts. Lucan is currently distressed about a recent theft of a valuable golden claw heirloom.",
                        "travel_desc": "General goods store run by Lucan and Camilla Valerius.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "quest_location_golden_claw"],
                        "context_tags": ["interior", "village_type", "shop_type"],
                        "fixed_npcs": [
                            {"name": "Lucan Valerius", "race": "Imperial", "role": "merchant_general_goods", "level": 4},
                            {"name": "Camilla Valerius", "race": "Imperial", "role": "shop_assistant", "level": 3}
                        ],
                        "exit_label_from_parent": "Shop Door",
                        "exit_label_to_parent": "Exit Shop"
                    },
                    {
                        "id": 1103,
                        "name": "Alvor's Smithy",
                        "desc": "The local blacksmith in Riverwood, run by the Nord Alvor. He is a skilled smith who provides tools, weapons, and armor for the village and passing travelers. Alvor is married to Sigrid and has a daughter, Dorthe. He is generally supportive of the Empire and concerned about the dragon attacks.",
                        "travel_desc": "Riverwood's blacksmith, run by Alvor.",
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "crafting_tools", "imperial_sympathizers_potential", "item_type_weapon_vendor_basic", "item_type_armor_vendor_basic", "quest_giver_potential_tutorial_smithing"],
                        "context_tags": ["interior_shop_exterior_forge", "village_type", "smithy_type"],
                        "fixed_npcs": [
                            {"name": "Alvor", "race": "Nord", "role": "blacksmith", "level": 6},
                            {"name": "Sigrid", "race": "Nord", "role": "blacksmith_spouse", "level": 3}
                        ],
                        "exit_label_from_parent": "Smithy Entrance",
                        "exit_label_to_parent": "Exit Smithy"
                    },
                    {
                        "id": 1104,
                        "name": "Faendal's House",
                        "desc": "The home of Faendal, a Bosmer archer and lumberjack in Riverwood.",
                        "travel_desc": "Home of Faendal, Bosmer archer and lumberjack.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "bosmer_influence_minor", "quest_giver_potential_faendal_camilla_love_triangle"],
                        "context_tags": ["interior", "rural_village", "residence_type"],
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    },
                    {
                        "id": 1105,
                        "name": "Sven and Hilde's House",
                        "desc": "The home of Sven, a local bard, and his mother Hilde.",
                        "travel_desc": "Home of Sven, local bard, and his mother.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "bard_dwelling", "quest_giver_potential_sven_camilla_love_triangle"],
                        "context_tags": ["interior", "rural_village", "residence_type"],
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    }
                ]
            },
            {
                "id": 12,
                "name": "Rorikstead",
                "travel_time": 3, # Rorikstead is further
                "desc": "A fertile farming village that supplies Whiterun with produce. Despite its prosperity, some whisper of strange pacts or hidden influences behind its unusual success.",
                "travel_desc": "Fertile farming village, supplies Whiterun with produce.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_farming_crops", "terrain_plains", "climate_temperate", "magical_properties_enchanted_neutral_prosperity_rumor", "daedric_influence_subtle_rumor", "mystery_local_unusual_success"],
                "context_tags": ["exterior", "rural_village", "village_type"],
                "exit_label_from_parent": "Path",
                "exit_label_to_parent": "Path",
                "sub_locations": [
                    {
                        "id": 1201,
                        "name": "Frostfruit Inn",
                        "desc": "The heart of Rorikstead, this cozy inn is run by Mralki and his wife Erikur. It's known for its warm hearth, local cider, and the surprisingly good spirits of its patrons, despite the village's somewhat mysterious prosperity. It's a good place to hear local rumors or find a room for the night.",
                        "travel_desc": "Cozy inn in Rorikstead, run by Mralki.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "food_drink_vendor", "lodging_available", "rumor_source_local_mystery"],
                        "context_tags": ["interior", "village_type", "tavern_type", "safe_zone"],
                        "demographics": {"Nord": 80, "Breton": 10, "Imperial": 5, "Redguard": 5},
                        "fixed_npcs": [
                            {"name": "Mralki", "race": "Nord", "role": "innkeeper", "level": 6},
                            {"name": "Erikur", "race": "Nord", "role": "innkeeper_spouse", "level": 5}
                        ],
                        "exit_label_from_parent": "Inn Door",
                        "exit_label_to_parent": "Exit Inn"
                    },
                    {
                        "id": 1202,
                        "name": "Rorikstead General Supplies",
                        "desc": "A small, unassuming general store in Rorikstead, run by Ennis. He offers essential supplies, some farm produce, and occasionally has tools or other practical items for sale. Given Rorikstead's focus on farming, his stock reflects the needs of the local community.",
                        "travel_desc": "Small general store in Rorikstead, run by Ennis.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety_limited", "local_supplier_farm_goods"],
                        "context_tags": ["interior", "village_type", "shop_type"],
                        "fixed_npcs": [
                            {"name": "Ennis", "race": "Redguard", "role": "merchant_general_goods", "level": 3}
                        ],
                        "exit_label_from_parent": "Shop Door",
                        "exit_label_to_parent": "Exit Shop"
                    },
                    {
                        "id": 1203,
                        "name": "Lemkil's Farmhouse",
                        "desc": "The farmstead of Lemkil, a local farmer in Rorikstead with two daughters.",
                        "travel_desc": "Farmstead of Lemkil and his two daughters.",
                        "tags": ["structure_type_farmstead", "structure_type_residence", "economic_activity_farming_crops", "social_issue_child_abuse_potential"],
                        "context_tags": ["exterior", "rural_village", "residence_type", "farmstead_type"],
                        "exit_label_from_parent": "Farmhouse Door",
                        "exit_label_to_parent": "Exit Farmhouse"
                    },
                    {
                        "id": 1204,
                        "name": "Jouane Manette's House",
                        "desc": "The home of Jouane Manette, a Breton farmer in Rorikstead.",
                        "travel_desc": "Home of Jouane Manette, a Breton farmer.",
                        "tags": ["structure_type_farmstead", "structure_type_residence", "economic_activity_farming_crops", "breton_settler"],
                        "context_tags": ["exterior", "rural_village", "residence_type", "farmstead_type"],
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    }
                ]
            },
            {
                "id": 13,
                "name": "Honningbrew Meadery",
                "desc": "A well-known meadery south-east of Whiterun, famed for its exceptionally smooth Honningbrew Mead. Currently run by Sabjorn, the meadery has a long history but has recently faced troubles, including competition and accusations of sabotage. It's a key location for those interested in the local brewing scene or perhaps the Thieves Guild.",
                "travel_desc": "Famed meadery run by Sabjorn, known for smooth mead.",
                "tags": ["structure_type_meadery_building", "economic_activity_brewing_mead_ale", "shop_specialty_goods_mead", "quest_location_thieves_guild", "sabotage_target_potential", "economic_competition_black_briar", "business_owner_sabjorn"],
                "context_tags": ["interior_exterior_complex", "rural_industrial", "meadery_type"],
                "fixed_npcs": [
                    {"name": "Sabjorn", "race": "Nord", "role": "meadery_owner_merchant", "level": 5},
                    {"name": "Mallus Maccius", "race": "Imperial", "role": "meadery_worker_foreman_potential", "level": 4}
                ],
                "exit_label_from_parent": "Path",
                "exit_label_to_parent": "Path"
            },
            {
                "id": 14,
                "name": "Western Watchtower",
                "travel_time": 4, # Western Watchtower is further and more dangerous
                "desc": "An old, ruined guard tower on the outskirts of Whiterun, fallen into disrepair over the years. It stands as a lonely sentinel over the plains, a relic of past conflicts.",
                "travel_desc": "Old, ruined guard tower on Whiterun's outskirts.",
                "tags": ["structure_type_ruined_tower", "cultural_historical_significance_historic_site", "dragon_lore_ancient_site_attack_recent", "state_or_condition_current_recently_attacked_recovering", "battlefield_minor_historic_dragon_attack", "quest_location_main_story_early_dragon_investigation"],
                "context_tags": ["exterior", "rural_wilderness", "ruin_type"],
                "exit_label_from_parent": "Path to Ruin",
                "exit_label_to_parent": "Path from Ruin"
            },
            {
                "id": 15,
                "name": "Bleak Falls Barrow",
                "desc": "An ancient Nordic tomb high among the mountains overlooking Riverwood, crawling with draugr and secrets of old, including a Word Wall.",
                "travel_desc": "Ancient Nordic tomb overlooking Riverwood.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "specific_landmark_type_word_wall_location", "quest_location_main_story_early_dragonstone", "puzzle_dragon_claw_golden", "cultural_historical_significance_nordic_ancient_site", "terrain_mountainous_overlook"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type", "barrow_type"],
                "exit_label_from_parent": "Barrow Entrance",
                "exit_label_to_parent": "Exit Barrow"
            },
            {
                "id": 16,
                "name": "Silent Moons Camp",
                "desc": "A clandestine bandit camp hidden in the wilderness north-west of Whiterun, known for its lunar-enchanted weapons.",
                "travel_desc": "Clandestine bandit camp with lunar-enchanted weapons.",
                "tags": ["bandit_minor_camp", "structure_type_ruined_settlement_forge", "dungeon_minor", "magical_properties_enchanted_neutral_lunar", "specific_landmark_type_lunar_forge", "weapon_enchanting_site_lunar", "state_or_condition_current_bandit_controlled_area"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type", "camp_type"],
                "exit_label_from_parent": "Camp Entrance",
                "exit_label_to_parent": "Leave Camp"
            },
            {
                "id": 17,
                "name": "Lund's Hut",
                "desc": "A small, isolated hut north of Rorikstead, once home to the unfortunate Lund.",
                "travel_desc": "Small, isolated hut north of Rorikstead.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_abandoned", "environment_wilderness", "tragedy_site_minor_death", "magical_properties_haunted_aura_potential", "isolated_location"],
                "context_tags": ["exterior", "rural_wilderness", "ruin_type", "abandoned_type"],
                "exit_label_from_parent": "Path to Hut",
                "exit_label_to_parent": "Leave Hut Area"
            },
            {
                "id": 18,
                "name": "Gjukar's Monument",
                "desc": "A stone monument south of Rorikstead, marking the site of an ancient battle and the resting place of the warrior Gjukar.",
                "travel_desc": "Stone monument marking an ancient battle site.",
                "tags": ["structure_type_monument_historic_site", "cultural_historical_significance_battlefield_historic_ancient", "magical_properties_haunted_aura_potential", "nordic_burial_site_major_nearby_rumor", "quest_location_minor_investigation_potential"],
                "context_tags": ["exterior", "rural_wilderness", "monument_type"],
                "exit_label_from_parent": "Path to Monument",
                "exit_label_to_parent": "Leave Monument Area"
            },
            {
                "id": 19,
                "name": "Secunda's Kiss",
                "desc": "A giant's camp located west of Whiterun, named for the nearby moon Secunda.",
                "travel_desc": "Giant's camp located west of Whiterun.",
                "tags": ["specific_landmark_type_giant_camp_established", "environment_wilderness", "terrain_plains", "mammoth_herd_grazing", "neutral_encounter_giant_mammoth"],
                "context_tags": ["exterior", "rural_wilderness", "giant_camp_type"],
                "exit_label_from_parent": "Path to Camp",
                "exit_label_to_parent": "Leave Camp Area"
            },
            {
                "id": 10001,
                "name": "Sleeping Tree Camp",
                "desc": "A giant's camp west of Whiterun, notable for a strange, glowing tree and the potent sap it produces.",
                "travel_desc": "Giant's camp with a strange, glowing tree.",
                "tags": ["specific_landmark_type_giant_camp_established", "unique_natural_formation_glowing_tree", "alchemy_ingredient_source_rich_sleeping_tree_sap", "magical_properties_enchanted_neutral_tree", "mystery_local_origin_of_tree", "quest_giver_potential_ysolda_sap"],
                "context_tags": ["exterior", "rural_wilderness", "giant_camp_type"],
                "exit_label_from_parent": "Path to Camp",
                "exit_label_to_parent": "Leave Camp Area"
            },
            {
                "id": 10002,
                "name": "Swindler's Den",
                "desc": "A cave system west of Whiterun, serving as a hideout for bandits and perhaps some Alik'r warriors if circumstances align.",
                "travel_desc": "Cave system hideout for bandits.",
                "tags": ["structure_type_natural_cave", "bandit_main_stronghold", "dungeon_major", "quest_location_main_story_early_redguard_woman", "faction_alikr_warriors_presence_potential", "state_or_condition_current_bandit_controlled_area"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type", "cave_type"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 10003,
                "name": "White River Watch",
                "desc": "A small cave east of Honningbrew Meadery, inhabited by bandits led by Hajvarr Iron-Hand.",
                "travel_desc": "Small cave inhabited by bandits.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "terrain_river_delta_overlook", "state_or_condition_current_bandit_controlled_area"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type", "cave_type"],
                "fixed_npcs": [
                    {"name": "Hajvarr Iron-Hand", "race": "Nord", "role": "bandit_leader", "level": 10}
                ],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 10004,
                "name": "Halted Stream Camp",
                "desc": "A bandit-occupied iron mine north of Whiterun, containing a spell tome for Transmute Ore.",
                "travel_desc": "Bandit-occupied iron mine with Transmute Ore spell.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "state_or_condition_current_bandit_controlled_area"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type", "mine_type"]
            },
            {
                "id": 10005,
                "name": "Chillfurrow Farm",
                "desc": "A prosperous farm run by Wilmuth and his family, just outside Whiterun's walls, known for its diverse crops.",
                "travel_desc": "Prosperous farm just outside Whiterun's walls.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "economic_activity_farming_livestock", "settlement_minor", "terrain_plains_whiterun_outskirts"],
                "context_tags": ["exterior", "rural_plains", "farmstead_type"]
            },
            {
                "id": 10006,
                "name": "Pelagia Farm",
                "desc": "The farmstead of Severio Pelagia, located near Whiterun, contributing to the city's food supply.",
                "travel_desc": "Farmstead contributing to Whiterun's food supply.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "settlement_minor", "terrain_plains_whiterun_outskirts"],
                "context_tags": ["exterior", "rural_plains", "farmstead_type"]
            },
            {
                "id": 10007,
                "name": "Valtheim Towers",
                "desc": "A pair of fortified towers spanning the White River east of Whiterun, often occupied by bandits demanding tolls.",
                "travel_desc": "Fortified towers spanning White River, often bandit-occupied.",
                "tags": ["structure_type_ruined_tower_pair", "bandit_minor_camp"],
                "context_tags": ["exterior", "rural_wilderness", "ruin_type"]
            },
            {
                "id": 10008,
                "name": "Greenspring Hollow",
                "desc": "A small, secluded cave known for its natural spring and unique mosses, sometimes used as a hunter's shelter or a troll's den.",
                "travel_desc": "Secluded cave with a natural spring and unique mosses.",
                "tags": ["structure_type_natural_cave"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type"]
            },
            {
                "id": 10009,
                "name": "Redoran's Retreat",
                "desc": "A small, damp cave west of Whiterun, often used as a hideout by a lone bandit or a small group of outcasts.",
                "travel_desc": "Small, damp cave often used as a bandit hideout.",
                "tags": ["structure_type_natural_cave"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type"]
            },
            {
                "id": 10010,
                "name": "Guldun Rock Overlook",
                "desc": "A rocky outcrop near the Whiterun plains, offering a strategic view. Sometimes used by hunters as a lookout or temporarily inhabited by wildlife.",
                "travel_desc": "Rocky outcrop offering a strategic view.",
                "tags": ["terrain_hilly_rocky_outcrop"],
                "context_tags": ["exterior", "rural_wilderness"]
            },
            {
                "id": 10011,
                "name": "Dustman's Cairn",
                "desc": "An ancient Nordic barrow west of Whiterun, a significant site for the Companions and haunted by draugr.",
                "travel_desc": "Ancient Nordic barrow, significant for the Companions.",
                "tags": ["nordic_burial_site_major"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type"]
            },
            {
                "id": 10012,
                "name": "Fellglow Keep",
                "desc": "A ruined fort east of Whiterun, now overrun by necromancers and their experiments. It holds forbidden knowledge and dangerous foes.",
                "travel_desc": "Ruined fort overrun by necromancers.",
                "tags": ["structure_type_ruined_fort"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type", "ruin_type"]
            },
            {
                "id": 10013,
                "name": "Battle-Born Farm",
                "desc": "A prosperous farm outside Whiterun, owned and operated by the Battle-Born family, known for its crops and livestock.",
                "travel_desc": "Prosperous farm of the Battle-Born family.",
                "tags": ["structure_type_farmstead"],
                "context_tags": ["exterior", "rural_plains", "farmstead_type"]
            },
            {
                "id": 10014,
                "name": "Gray-Mane Farm",
                "desc": "A traditional Nord farmstead near Whiterun, belonging to the Gray-Mane family, reflecting their more rustic and independent values.",
                "travel_desc": "Traditional Nord farmstead of the Gray-Mane family.",
                "tags": ["structure_type_farmstead"],
                "context_tags": ["exterior", "rural_plains", "farmstead_type"]
            },
            {
                "id": 10015,
                "name": "Whiterun Pass Cave",
                "desc": "A small cave system that cuts through the hills near Whiterun, sometimes used by travelers as a shortcut or by creatures as a den.",
                "travel_desc": "Small cave system, a shortcut through hills.",
                "tags": ["structure_type_natural_cave"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type"]
            },
            {
                "id": 10016,
                "name": "Granite Hill Redoubt",
                "desc": "A fortified bandit encampment built into the rocky hills west of Whiterun, a source of trouble for local farms and travelers.",
                "travel_desc": "Fortified bandit encampment in rocky hills.",
                "tags": ["bandit_main_stronghold"],
                "context_tags": ["exterior", "rural_wilderness", "dungeon_type", "camp_type", "ruin_type"]
            },
            {
                "id": 10017,
                "name": "Lone Hunter's Shack",
                "desc": "A small, isolated shack used by hunters.",
                "tags": [],
                "context_tags": []
            }
        ]
    }
]
