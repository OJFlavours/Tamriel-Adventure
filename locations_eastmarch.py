from locations_windhelm_city import WINDHELM_CITY_LOCATIONS

EASTMARCH_LOCATIONS = [
    # EASTMARCH
    {
        "id": 7,
        "name": "Eastmarch",
        "desc": "A harsh, volcanic hold in eastern Skyrim, dominated by the ancient city of Windhelm, seat of Jarl Ulfric Stormcloak and a center of growing rebellion. Known for its hot springs, giants, and fierce Nordic traditions.",
        "travel_desc": "Harsh, volcanic hold, home to Windhelm and Stormcloak rebellion.",
        "tags": ["hold", "terrain_volcanic_tundra", "nordic_culture_strong_ancient", "stormcloak_presence_strong_capital", "terrain_hot_springs", "specific_landmark_type_giant_camp_region", "political_tension_high_civil_war_epicenter", "morrowind_border_region", "climate_subarctic_volcanic", "environment_geothermal_area", "dunmer_refugee_presence_significant", "argonian_worker_presence_significant"],
        "density": "sparse",
        "context_tags": ["exterior", "hold_region", "volcanic_region"],
        "demographics": {"Nord": 90, "Dunmer": 5, "Argonian": 3, "Others": 2},
        "travel": {
            "links": [
                {"name": "Whiterun Hold", "connection_type": "Road"},
                {"name": "The Rift", "connection_type": "Road"},
                {"name": "The Pale", "connection_type": "Road"},
                {"name": "Winterhold", "connection_type": "Road"},
                {"name": "Volcanic Tundra Trail", "connection_type": "Path"},
                {"name": "Dunmeth Pass to Morrowind (treacherous)", "connection_type": "Path"}
            ]
        },
        "sub_locations": [
            {
                "id": 70,
                "name": "Windhelm",
                "desc": "One of Skyrim's oldest cities, the traditional capital of the First Empire, and current seat of Jarl Ulfric Stormcloak. It is a city of stone, snow, and strong anti-Imperial sentiment, a focal point of brewing rebellion.",
                "travel_desc": "Ancient city of stone and snow, seat of Jarl Ulfric Stormcloak.",
                "tags": ["populated_city", "cultural_historical_significance_historic_capital_nordic_first_empire", "nordic_architecture_ancient_stone", "city_affiliation_eastmarch_capital", "stormcloak_presence_strong_hq_ulfric", "settlement_features_district_ethnic_dunmer_gray_quarter", "settlement_features_district_ethnic_argonian_assemblage_docks", "political_tension_high_civil_war_focus_rebellion_capital", "settlement_features_jarls_longhouse_ulfric_palace_of_kings", "climate_arctic_coastal", "structure_type_fortified_city_wall_ancient", "urban_issues_or_atmosphere_tense_atmosphere_racial_political", "unique_landmark_iconic_palace_of_kings_gray_quarter", "urban_issues_or_atmosphere_racial_tension_overt"],
                "density": "bustling",
                "exit_label_from_parent": "City Gates",
                "exit_label_to_parent": "City Gates",
                "sub_locations": WINDHELM_CITY_LOCATIONS
            },
            {
                "id": 71,
                "name": "Kynesgrove",
                "desc": "A small, industrious mining village on the slopes of the volcanic tundra, known for its malachite mine. It is also situated near an ancient dragon burial site, a fact known to few.",
                "travel_desc": "Small mining village known for its malachite mine.",
                "tags": ["populated_village", "settlement_minor_mining", "economic_activity_mining_malachite", "terrain_volcanic_tundra_slope", "dragon_lore_ancient_site_burial_nearby", "climate_subarctic_volcanic", "quest_location_main_story_early_dragon_sighting_kynesgrove"],
                "density": "average",
                "exit_label_from_parent": "Path to Village",
                "exit_label_to_parent": "Leave Village",
                 "sub_locations": [
                    {
                        "id": 7101,
                        "name": "Braidwood Inn",
                        "desc": "The local inn in the small mining village of Kynesgrove, run by Iddra. It provides essential food, lodging, and a place for the local miners and infrequent travelers to gather. Roggi Knot-Beard, a miner, is a frequent patron.",
                        "travel_desc": "Kynesgrove's local inn, run by Iddra.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source", "business_owner_iddra", "location_specific_braidwood_inn"],
                        "density": "average",
                        "context_tags": ["interior", "village_type_mining", "tavern_type", "safe_zone"],
                        "demographics": {"Nord": 80, "Imperial": 5, "Dunmer": 5, "Argonian": 5, "Orc": 5},
                        "fixed_npcs": [
                            {"name": "Iddra", "race": "Nord", "role": "innkeeper", "level": 5},
                            {"name": "Roggi Knot-Beard", "race": "Nord", "role": "miner_patron", "level": 3}
                        ],
                        "exit_label_from_parent": "Inn Door",
                        "exit_label_to_parent": "Exit Inn"
                    },
                    {
                        "id": 7102,
                        "name": "Steamscorch Mine",
                        "desc": "The malachite mine that is the lifeblood of Kynesgrove, a source of valuable ore.",
                        "travel_desc": "Malachite mine, lifeblood of Kynesgrove.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_malachite", "resource_node_malachite", "dragon_lore_ancient_site_burial_nearby_mine_entrance_potential_impact", "quest_location_main_story_early_dragon_sahloknir_attack"],
                        "density": "average",
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    }
                ]
            },
            {
                "id": 72,
                "name": "Fort Amol",
                "desc": "A strategic fort in Eastmarch, currently held by Stormcloak-aligned soldiers, guarding the pass to Whiterun. It has seen skirmishes in the past.",
                "travel_desc": "Strategic fort held by Stormcloak soldiers.",
                "tags": ["structure_type_fortified_keep", "military_presence_stormcloak_garrison", "stormcloak_presence_strong", "dungeon_major_potential_if_contested", "civil_war_quest_historic_site_potential", "terrain_mountain_pass_defense_eastmarch_whiterun", "strategic_location_civil_war"],
                "density": "average",
                "exit_label_from_parent": "Fort Gates",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 73,
                "name": "Eldergleam Sanctuary",
                "desc": "A sacred, tranquil grove hidden in Eastmarch, home to the ancient and revered Eldergleam tree. A place of pilgrimage and natural wonder, protected by nature spirits.",
                "travel_desc": "Sacred, tranquil grove, home to the Eldergleam tree.",
                "tags": ["cultural_historical_significance_sacred_grove_kynareth_eldergleam", "unique_natural_formation_magical_tree_eldergleam", "magical_properties_aedric_blessing_active", "quest_location_kynareth_gildergreen_restoration_whiterun", "monster_den_spriggan_potential_guardians", "secluded_nature_spot_pilgrimage", "alchemy_ingredient_source_rich_unique_bark_sap", "terrain_forest_eastmarch_hidden_sanctuary"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Sanctuary",
                "exit_label_to_parent": "Leave Sanctuary"
            },
            {
                "id": 74,
                "name": "Narzulbur",
                "desc": "An Orc stronghold in Eastmarch, situated near a rich ebony mine. They adhere strictly to the Code of Malacath and are wary of outsiders.",
                "travel_desc": "Orc stronghold near a rich ebony mine.",
                "tags": ["orc_stronghold", "populated_settlement_orcish", "economic_activity_mining_ebony", "malacath_worship", "structure_type_fortified_settlement", "cultural_historical_significance_orc_tradition", "terrain_volcanic_tundra_mountains_eastmarch", "warrior_culture_orcish", "isolated_location", "faction_orc_tribe_narzulbur", "quest_giver_potential_orc_chief_issues"],
                "density": "average",
                "exit_label_from_parent": "Stronghold Gate",
                "exit_label_to_parent": "Leave Stronghold",
                "sub_locations": [
                    {
                        "id": 7401,
                        "name": "Mauhulakh's Longhouse",
                        "desc": "The longhouse of Chief Mauhulakh, stern leader of Narzulbur.",
                        "travel_desc": "Longhouse of Chief Mauhulakh.",
                        "tags": ["structure_type_longhouse_orcish", "government_tribal", "chieftains_hall", "residence_chief"],
                        "density": "sparse",
                        "exit_label_from_parent": "Longhouse Door",
                        "exit_label_to_parent": "Exit Longhouse"
                    },
                    {
                        "id": 7402,
                        "name": "Gloombound Mine (Ebony)",
                        "desc": "Narzulbur's productive ebony mine, a source of great wealth and Orcish pride, but also dangers from deep within.",
                        "travel_desc": "Narzulbur's productive ebony mine.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_ebony", "resource_node_ebony", "dungeon_minor_extension_potential", "orc_controlled_mine"],
                        "density": "average",
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    }
                ]
            },
            {
                "id": 75,
                "name": "Ansilvund",
                "desc": "A Nordic ruin in Eastmarch, haunted by powerful draugr and connected to a tragic love story and necromantic rituals performed by Lu'ah Al-Skaven.",
                "travel_desc": "Nordic ruin haunted by draugr, site of necromantic rituals.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong_powerful_draugr_ghosts", "specific_landmark_type_necromancer_lair_luah_al_skaven", "specific_landmark_type_word_wall_location", "magical_properties_tainted_by_dark_magic", "quest_location_local_legend_tragic_love_ansilvund_ghosts", "draugr_heavy", "puzzle_ancient_nordic_lore"],
                "density": "average",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 76,
                "name": "Bonestrewn Crest",
                "desc": "A mountain peak in the southern volcanic region of Eastmarch, an ancient dragon lair and site of a Word Wall, though no dragon has roosted here for centuries.",
                "travel_desc": "Mountain peak, ancient dragon lair and Word Wall site.",
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "terrain_mountain_peak_volcanic_southern_eastmarch", "dungeon_minor_lair_potential", "cultural_historical_significance_dragon_lore_site_ancient", "climate_subarctic_volcanic", "exploration_point_remote_lore_word_wall"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Crest",
                "exit_label_to_parent": "Leave Crest Area"
            }
        ]
    },
    {
        "id": 7000,
        "name": "Windhelm Streets",
        "desc": "The main thoroughfares of Windhelm, filled with merchants, guards, and citizens. The streets reflect the city's ancient history and current political tensions.",
        "travel_desc": "The main streets of Windhelm.",
        "tags": ["urban_area", "city_district", "settlement_features_market_district", "settlement_features_residential_district", "settlement_features_guard_presence", "political_tension_high_civil_war_focus_rebellion_capital"],
        "density": "bustling",
        "context_tags": ["exterior", "urban_town", "city_street"],
        "demographics": {"Nord": 85, "Dunmer": 10, "Argonian": 3, "Imperial": 2},
        "exit_label_from_parent": "Street Entrance",
        "exit_label_to_parent": "Exit Street"
    },
    {
        "id": 7006,
        "name": "Windhelm Market Square",
        "desc": "A bustling open-air market near the city gates of Windhelm, featuring various stalls. Aval Atheron sells general goods, while Niranye, an Altmer pawnbroker, deals in more discreet transactions. The atmosphere can be tense due to the city's political climate and racial undertones.",
        "travel_desc": "Windhelm's bustling open-air market.",
        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "urban_issues_or_atmosphere_tense_atmosphere", "item_type_food_vendor", "item_type_general_goods_vendor_stalls"],
        "density": "bustling",
        "context_tags": ["exterior", "urban_city", "market_type"],
        "demographics": {"Nord": 85, "Dunmer": 10, "Argonian": 3, "Imperial": 2},
        "exit_label_from_parent": "Enter Market",
        "exit_label_to_parent": "Leave Market"
    },
    {
        "id": 7007,
        "name": "Temple of Talos (Windhelm)",
        "desc": "A place of clandestine Talos worship, highly significant given the Stormcloak cause and the Thalmor's ban. Attended by those loyal to traditional Nord beliefs.",
        "travel_desc": "Place of clandestine Talos worship.",
        "tags": ["structure_type_temple_building", "religious_site_aedric_secret", "talos_shrine", "nordic_culture_strong", "political_tension_high_religious", "stormcloak_presence_strong", "thalmor_presence_hostile_potential"],
        "density": "sparse",
        "exit_label_from_parent": "Temple Doors",
        "exit_label_to_parent": "Exit Temple"
    },
    {
        "id": 7008,
        "name": "Gray Quarter (Dunmer District)",
        "desc": "The segregated district where most of Windhelm's Dunmer refugee population resides, often facing prejudice and harsh living conditions.",
        "travel_desc": "Segregated district for Windhelm's Dunmer refugees.",
        "tags": ["settlement_features_district_ethnic_dunmer_gray_quarter", "dunmer_culture_strong", "urban_issues_or_atmosphere_oppressive_atmosphere", "social_issue_racism_segregation", "social_issue_poverty"],
        "density": "bustling",
        "exit_label_from_parent": "Enter Gray Quarter",
        "exit_label_to_parent": "Leave Gray Quarter"
    },
    {
        "id": 7009,
        "name": "Argonian Assemblage (Docks)",
        "desc": "The dockside area where Windhelm's Argonian dockworkers are forced to live in cramped and poor conditions, working for low wages.",
        "travel_desc": "Dockside area where Argonian dockworkers live.",
        "tags": ["settlement_features_district_ethnic_argonian_assemblage", "argonian_culture_local", "urban_issues_or_atmosphere_oppressive_atmosphere", "social_issue_racism_segregation", "economic_activity_manual_labor", "settlement_features_docks_harbor"],
        "density": "bustling",
        "exit_label_from_parent": "Enter Assemblage",
        "exit_label_to_parent": "Leave Assemblage"
    },
    {
        "id": 7011,
        "name": "Hall of the Dead (Windhelm)",
        "desc": "Windhelm's catacombs for honoring the dead, maintained by Helgird, a priestess of Arkay, who also deals with the city's recent murder victims.",
        "travel_desc": "Windhelm's catacombs for honoring the dead.",
        "tags": ["structure_type_catacombs_structure", "religious_site_aedric", "arkay_presence", "nordic_burial_site_major", "quest_location_investigation_serial_killer", "undead_presence_rumored_low"],
        "density": "empty",
        "exit_label_from_parent": "Hall Entrance",
        "exit_label_to_parent": "Exit Hall"
    },
    {
        "id": 7012,
        "name": "Windhelm Port",
        "desc": "The icy docks of Windhelm, a vital hub for trade with northern Tamriel and Solstheim, despite the harsh conditions. Home to the East Empire Company office.",
        "travel_desc": "Icy docks of Windhelm, a vital trade hub.",
        "tags": ["settlement_features_docks_harbor", "economic_activity_trade_hub_major_maritime", "travel_hub_sea_solstheim", "climate_arctic_coastal", "east_empire_company_presence", "argonian_culture_local_nearby"],
        "density": "bustling",
        "exit_label_from_parent": "Enter Port",
        "exit_label_to_parent": "Leave Port"
    },
    {
        "id": 70001,
        "name": "Gallows Rock",
        "desc": "A fortress in Eastmarch.",
        "travel_desc": "A fortress in Eastmarch.",
        "tags": ["structure_type_fortress"],
        "density": "average",
        "exit_label_from_parent": "Enter Fortress",
        "exit_label_to_parent": "Leave Fortress"
    },
    {
        "id": 7006,
        "name": "House of Clan Shatter-Shield",
        "desc": "The home of Clan Shatter-Shield, a prominent Nord family in Windhelm.",
        "travel_desc": "Home of Clan Shatter-Shield.",
        "tags": ["structure_type_residence", "nordic_culture_strong"],
        "density": "sparse",
        "exit_label_from_parent": "Enter House",
        "exit_label_to_parent": "Leave House"
    },
    {
        "id": 7007,
        "name": "Viola Giordano's House",
        "desc": "The home of Viola Giordano, a Nord woman living in Windhelm.",
        "travel_desc": "Home of Viola Giordano.",
        "tags": ["structure_type_residence", "nordic_culture_strong"],
        "density": "sparse",
        "exit_label_from_parent": "Enter House",
        "exit_label_to_parent": "Leave House"
    }
]
