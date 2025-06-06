DAWNSTAR_CITY_LOCATIONS = [
    {
        "id": 2001,
        "name": "Windpeak Inn",
        "desc": "The main inn of Dawnstar, run by Thoring. It's a somewhat gloomy place, reflecting the town's current troubles with nightmares. Locals and the occasional traveler gather here, often discussing the strange occurrences and seeking respite from the harsh northern climate.",
        "travel_desc": "Dawnstar's inn, run by Thoring, troubled by nightmares.",
        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source_nightmares_local_issues", "food_drink_vendor", "lodging_available", "urban_issues_or_atmosphere_fear_and_superstition_nightmares", "location_specific_windpeak_inn"],
        "density": "average",
        "context_tags": ["interior", "urban_town", "tavern_type", "safe_zone"],
        "demographics": {"Nord": 80, "Imperial": 5, "Dunmer": 5, "Khajiit": 5, "Argonian": 5},
        "fixed_npcs": [
            {"name": "Thoring", "race": "Nord", "role": "innkeeper", "level": 6},
            {"name": "Karita", "race": "Nord", "role": "bard_local", "level": 4}
        ],
        "exit_label_from_parent": "Inn Door",
        "exit_label_to_parent": "Exit Inn"
    },
    {
        "id": 2002,
        "name": "Quicksilver Mine",
        "desc": "A vital quicksilver mine for Dawnstar's economy, owned by Leigelf. Miners toil here daily, though recent talk of strange occurrences and the town's pervasive nightmares have made some uneasy. The mine is a key source of income for the town.",
        "travel_desc": "Dawnstar's Quicksilver Mine, owned by Leigelf.",
        "tags": ["structure_type_mine_active", "economic_activity_mining_quicksilver", "resource_node_quicksilver", "urban_issues_or_atmosphere_haunted_rumors_strong_mine_related_potential", "economic_backbone_dawnstar", "business_owner_leigelf"],
        "density": "average",
        "context_tags": ["interior", "industrial_site", "mine_type"],
        "fixed_npcs": [
           {"name": "Leigelf", "race": "Nord", "role": "mine_owner", "level": 7}
        ],
        "exit_label_from_parent": "Mine Entrance",
        "exit_label_to_parent": "Exit Mine"
    },
    {
        "id": 2003,
        "name": "The Mortar and Pestle",
        "desc": "Frida's alchemy shop in Dawnstar, a small but well-stocked establishment. Frida, an elderly alchemist, concocts various potions and sells ingredients. She is knowledgeable about local herbs and may have tasks for those willing to brave the wilds of The Pale for rare components.",
        "travel_desc": "Frida's alchemy shop in Dawnstar.",
        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_giver_potential_ingredient_gathering", "business_owner_frida"],
        "density": "sparse",
        "context_tags": ["interior", "urban_town", "shop_type"],
        "fixed_npcs": [
            {"name": "Frida", "race": "Nord", "role": "alchemist_merchant", "level": 5}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 2004,
        "name": "The White Hall",
        "desc": "The Jarl's longhouse in Dawnstar, currently the seat of Jarl Skald the Elder, a fervent Stormcloak supporter. The hall reflects the harshness of The Pale, and discussions within often revolve around the civil war and the town's ongoing nightmare problem.",
        "travel_desc": "The Jarl's longhouse in Dawnstar, seat of Jarl Skald.",
        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local_stormcloak_jarl_skald", "stormcloak_presence_strong", "political_family_stormcloak_jarl"],
        "density": "average",
        "context_tags": ["interior", "urban_town", "government_building"],
        "fixed_npcs": [
            {"name": "Skald the Elder", "race": "Nord", "role": "jarl_stormcloak", "level": 10},
            {"name": "Brina Merilis", "race": "Imperial", "role": "jarl_advisor", "level": 8}
        ],
        "exit_label_from_parent": "Hall Entrance",
        "exit_label_to_parent": "Exit Hall"
    },
    {
        "id": 2005,
        "name": "Rustleif's House and Smithy",
        "desc": "The home and workshop of Rustleif, Dawnstar's resident blacksmith. He is a skilled Nord smith who provides essential tools and repairs for the townsfolk and miners. Rustleif is married to Seren and dreams of crafting a fine dagger for her from materials from his homeland.",
        "travel_desc": "Rustleif's blacksmith shop in Dawnstar.",
        "tags": ["structure_type_shop_building", "structure_type_residence", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "crafting_tools", "item_type_weapon_vendor", "item_type_armor_vendor", "quest_giver_potential_personal_item", "business_owner_rustleif"],
        "density": "sparse",
        "context_tags": ["interior_shop_exterior_forge", "urban_town", "smithy_type"],
        "fixed_npcs": [
            {"name": "Rustleif", "race": "Nord", "role": "blacksmith", "level": 6},
            {"name": "Seren", "race": "Redguard", "role": "blacksmith_spouse", "level": 3}
        ],
        "exit_label_from_parent": "Smithy Entrance",
        "exit_label_to_parent": "Exit Smithy"
    },
    {
        "id": 2006,
        "name": "Dawnstar Sanctuary",
        "desc": "A forgotten and ruined sanctuary of the Dark Brotherhood, hidden near Dawnstar. Its secrets lie buried in snow and shadow.",
        "travel_desc": "Forgotten and ruined Dark Brotherhood sanctuary.",
        "tags": ["structure_type_ruined_shrine_sanctuary", "specific_landmark_type_assassin_guild_hq_abandoned_dark_brotherhood", "dungeon_minor", "secret_location_hidden_entrance", "magical_properties_tainted_by_dark_magic", "structure_condition_collapsed_ruined", "faction_dark_brotherhood_historic_site"],
        "density": "empty",
        "context_tags": ["exterior", "urban_town", "ruin_type", "dark_brotherhood"],
        "exit_label_from_parent": "Sanctuary Entrance",
        "exit_label_to_parent": "Exit Sanctuary"
    }
]