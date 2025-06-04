RIFTEN_CITY_LOCATIONS = [
    {
        "id": 9001,
        "name": "The Bee and Barb",
        "desc": "A popular tavern in Riften, owned by Keerava and Talen-Jei. A common meeting place and source of rumors, often frequented by Thieves Guild associates.",
        "travel_desc": "Popular tavern, common meeting place and rumor source.",
        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular_riften", "rumor_source_thieves_guild", "food_drink_vendor", "lodging_available", "quest_giver_potential_local_issues"],
        "demographics": {"Nord": 40, "Dunmer": 20, "Argonian": 15, "Khajiit": 10, "Imperial": 5, "Breton": 5, "Redguard": 5},
        "exit_label_from_parent": "Tavern Door",
        "exit_label_to_parent": "Exit Tavern",
        "fixed_npcs": [
            {"name": "Talen-Jei", "race": "Argonian", "gender": "Male", "role": "publican", "level": 6},
            {"name": "Keerava", "race": "Argonian", "gender": "Female", "role": "publican", "level": 6}
        ]
    },
    {
        "id": 9002,
        "name": "Black-Briar Meadery (Riften Building)",
        "desc": "The main office and shopfront for the powerful Black-Briar Meadery within Riften, a symbol of Maven Black-Briar's economic and political control over the city.",
        "travel_desc": "Main office for the powerful Black-Briar Meadery.",
        "tags": ["structure_type_shop_building_meadery", "economic_activity_brewing_mead_ale_major_black_briar", "political_influence_black_briar_family_business", "economic_powerhouse_local", "shop_specialty_goods_mead"],
        "exit_label_from_parent": "Meadery Door",
        "exit_label_to_parent": "Exit Meadery"
    },
    {
        "id": 9003,
        "name": "The Pawned Prawn",
        "desc": "A general goods store in Riften, run by Bersi Honey-Hand. A place to buy and sell various items, some of questionable origin.",
        "travel_desc": "General goods store run by Bersi Honey-Hand.",
        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "thieves_guild_fence_connection_potential", "economic_activity_trade_hub_local"],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 9004,
        "name": "Mistveil Keep",
        "desc": "The Jarl's residence in Riften, currently home to Jarl Laila Law-Giver, though her authority is often undermined by Maven Black-Briar.",
        "travel_desc": "Jarl's residence, home to Jarl Laila Law-Giver.",
        "tags": ["structure_type_palace_or_manor_keep", "settlement_features_jarls_longhouse", "government_local_laila_law_giver", "political_tension_high_black_briar_shadow_rule", "political_influence_black_briar_family_strong"],
        "exit_label_from_parent": "Keep Entrance",
        "exit_label_to_parent": "Exit Keep"
    },
    {
        "id": 9005,
        "name": "The Ratway",
        "desc": "A dangerous, labyrinthine network of tunnels beneath Riften, serving as the entrance to the Ragged Flagon and the hidden headquarters of the Thieves Guild.",
        "travel_desc": "Dangerous tunnels beneath Riften, entrance to Thieves Guild HQ.",
        "tags": ["dungeon_major_city_undercity", "thieves_guild_access_route", "criminal_hideout_network", "state_or_condition_current_lawless_area_city_section", "environment_sewers_forgotten_tunnels", "urban_issues_or_atmosphere_dangerous_undercity"],
        "exit_label_from_parent": "Ratway Entrance",
        "exit_label_to_parent": "Exit to Riften",
        "sub_locations": [
            {
                "id": 90051,
                "name": "The Ragged Flagon",
                "desc": "A hidden tavern within the Ratway, serving as the main gathering area, bar, and neutral ground for the Thieves Guild and its associates.",
                "travel_desc": "Hidden tavern, main gathering area for Thieves Guild.",
                "tags": ["structure_type_inn_building_secret", "settlement_features_tavern_thieves_guild", "thieves_guild_hq_meeting_place", "thieves_guild_fence_location", "information_broker_guild_contacts", "social_hub_criminal_underworld"],
                "demographics": {"Breton": 20, "Nord": 20, "Dunmer": 15, "Khajiit": 15, "Argonian": 10, "Imperial": 10, "Redguard": 5, "Bosmer": 5},
                "exit_label_from_parent": "Enter Flagon",
                "exit_label_to_parent": "Exit to Ratway"
            },
            {
                "id": 90052,
                "name": "The Cistern",
                "desc": "The secure, inner sanctum and living quarters of the Thieves Guild, deep within the Ratway, accessible only to trusted members.",
                "travel_desc": "Secure inner sanctum of the Thieves Guild.",
                "tags": ["thieves_guild_hq_inner_sanctum", "settlement_features_training_area_thief_skills", "structure_type_sleeping_quarters_guild", "treasure_cache_guild_vault_potential", "secret_location_guild_only", "faction_thieves_guild_main_base"],
                "exit_label_from_parent": "Enter Cistern",
                "exit_label_to_parent": "Exit to Ragged Flagon"
            }
        ]
    },
    {
        "id": 9006,
        "name": "Temple of Mara (Riften)",
        "desc": "A prominent temple dedicated to Mara, the Divine of Love and Compassion. It is a place for marriages, seeking guidance on love, and helping the needy.",
        "travel_desc": "Prominent temple dedicated to Mara, Divine of Love.",
        "tags": ["structure_type_temple_building_major", "religious_site_aedric", "mara_shrine_prominent", "event_wedding_location", "quest_location_agents_of_mara", "settlement_features_temple_divines", "social_hub_religious_community"],
        "exit_label_from_parent": "Temple Doors",
        "exit_label_to_parent": "Exit Temple"
    },
    {
        "id": 9007,
        "name": "The Scorched Hammer",
        "desc": "Balimund's smithy in Riften, known for its quality craftsmanship and Balimund's expertise with fire salts in forging.",
        "travel_desc": "Balimund's smithy, known for quality craftsmanship.",
        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production_skilled", "item_type_weapon_vendor", "item_type_armor_vendor", "crafting_specialty_fire_salts"],
        "exit_label_from_parent": "Smithy Entrance",
        "exit_label_to_parent": "Exit Smithy"
    },
     {
        "id": 9008,
        "name": "Elgrim's Elixirs",
        "desc": "An apothecary shop run by Elgrim and his wife Hafjorg, located on Riften's lower platforms. Elgrim is a master alchemist, albeit somewhat reclusive.",
        "travel_desc": "Apothecary shop run by master alchemist Elgrim.",
        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable_master", "item_type_potion_vendor", "item_type_ingredient_vendor", "hermit_lair_potential_alchemist", "skill_trainer_alchemy_master_potential"],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 9009,
        "name": "Riften Marketplace",
        "desc": "The central market area of Riften, with various stalls selling food, jewelry, and other goods. A prime location for pickpockets and observant guild members.",
        "travel_desc": "Central market area with various stalls.",
        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "thieves_guild_pickpocket_hotspot", "thieves_guild_observation_post_potential"],
        "exit_label_from_parent": "Enter Marketplace",
        "exit_label_to_parent": "Leave Marketplace"
    },
    {
        "id": 9010,
        "name": "Honorhall Orphanage",
        "desc": "Riften's orphanage, currently run by the cruel Grelod the Kind. The children suffer under her neglect and abuse.",
        "travel_desc": "Riften's orphanage, run by the cruel Grelod.",
        "tags": ["structure_type_orphanage", "quest_location_dark_brotherhood_initiation_aventus", "social_issue_child_abuse_grelod", "urban_issues_or_atmosphere_oppressive_atmosphere_children", "faction_dark_brotherhood_target"],
        "exit_label_from_parent": "Orphanage Door",
        "exit_label_to_parent": "Exit Orphanage"
    },
    {
        "id": 9011,
        "name": "Black-Briar Manor",
        "desc": "The grand residence of the powerful and influential Black-Briar family, heavily guarded and a testament to their wealth and control over Riften.",
        "travel_desc": "Grand residence of the powerful Black-Briar family.",
        "tags": ["structure_type_residence_noble_manor", "noble_estate_district", "political_influence_black_briar_family_home", "structure_condition_fortified_private", "maven_black_briar_residence", "political_tension_high_power_center"],
        "exit_label_from_parent": "Manor Gates",
        "exit_label_to_parent": "Exit Manor"
    },
    {
        "id": 9012,
        "name": "Beggar's Row",
        "desc": "A dilapidated section of Riften's lower walkways where the city's poorest and most desperate souls eke out a meager existence.",
        "travel_desc": "Dilapidated section where the city's poorest reside.",
        "tags": ["settlement_features_district_slums", "social_issue_poverty_extreme", "beggars_community_hub", "urban_issues_or_atmosphere_desperation_squalor", "structure_condition_dilapidated"],
        "exit_label_from_parent": "Enter Beggar's Row",
        "exit_label_to_parent": "Leave Beggar's Row"
    },
    {
        "id": 9013,
        "name": "Riften Warehouse",
        "desc": "A large warehouse on the Riften docks, often used for storing goods, both legitimate and illicit. Rumored to be a key point in the city's smuggling operations and sometimes used by the Thieves Guild.",
        "travel_desc": "Large warehouse on Riften docks, used for storing goods.",
        "tags": ["structure_type_warehouse_docks", "economic_activity_storage_commercial", "economic_activity_smuggling_hotspot_potential", "thieves_guild_interest_operations", "political_influence_black_briar_family_connection_rumor", "settlement_features_docks_harbor"],
        "exit_label_from_parent": "Warehouse Doors",
        "exit_label_to_parent": "Exit Warehouse"
    }
]