FALKREATH_CITY_LOCATIONS = [
    {
        "id": 5001,
        "name": "Dead Man's Drink",
        "desc": "Falkreath's only inn, run by the Imperial Valga Vinicia. It's a somewhat somber place, reflecting the town's atmosphere, but offers warm meals, strong drinks, and beds for the night. Locals and the occasional traveler gather here, often discussing the hold's dangers or the Jarl's latest decrees. Narri and Tekla work here.",
        "travel_desc": "Falkreath's inn, run by Valga Vinicia.",
        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "rumor_source_local_legends_daedric_rumors", "food_drink_vendor", "lodging_available", "business_owner_valga_vinicia", "location_specific_dead_mans_drink"],
        "density": "average",
        "context_tags": ["interior", "urban_town", "tavern_type", "safe_zone"],
        "demographics": {"Nord": 70, "Imperial": 15, "Breton": 5, "Redguard": 5, "Bosmer": 5},
        "fixed_npcs": [
            {"name": "Valga Vinicia", "race": "Imperial", "role": "innkeeper", "level": 6},
            {"name": "Narri", "race": "Nord", "role": "tavern_staff_server", "level": 3},
            {"name": "Tekla", "race": "Nord", "role": "tavern_staff_server", "level": 3}
        ],
        "exit_label_from_parent": "Tavern Door",
        "exit_label_to_parent": "Exit Tavern"
    },
    {
        "id": 5002,
        "name": "Jarl's Longhouse (Falkreath)",
        "desc": "The seat of authority in Falkreath Hold, residence of Jarl Siddgeir.",
        "travel_desc": "Seat of authority, residence of Jarl Siddgeir.",
        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local_jarl_siddgeir", "imperial_influence_strong_appointed_jarl", "quest_giver_potential_jarl_tasks"],
        "density": "average",
        "exit_label_from_parent": "Longhouse Entrance",
        "exit_label_to_parent": "Exit Longhouse"
    },
    {
        "id": 5003,
        "name": "Falkreath Graveyard",
        "desc": "An expansive and ancient cemetery, the largest in Skyrim, where many Nords, both heroes and common folk, are laid to rest. Restless spirits are sometimes rumored here.",
        "travel_desc": "Expansive, ancient cemetery, largest in Skyrim.",
        "tags": ["cultural_historical_significance_historic_burial_site_major_largest_skyrim", "religious_site_aedric_arkay", "arkay_presence_strong_priest_runil", "undead_presence_rumored_low_restless_spirits", "unique_landmark_iconic_town_feature", "urban_issues_or_atmosphere_haunted_rumors_strong_graveyard", "quest_location_ancestor_worhsip_runil_journal"],
        "density": "empty",
        "exit_label_from_parent": "Graveyard Gate",
        "exit_label_to_parent": "Exit Graveyard"
    },
    {
        "id": 5004,
        "name": "Gray Pine Goods",
        "desc": "Falkreath's primary general store, run by the Nord Solaf. He stocks a variety of goods, from essential supplies and hunting gear to lumber sourced from the local mill. Solaf is known to be a Stormcloak sympathizer and might offer different prices or information based on one's allegiances.",
        "travel_desc": "Falkreath's general store, run by Solaf.",
        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety_local_goods", "item_type_hunting_gear_vendor", "item_type_lumber_vendor", "stormcloak_sympathizers_potential_owner_solaf", "business_owner_solaf"],
        "density": "sparse",
        "context_tags": ["interior", "urban_town", "shop_type"],
        "fixed_npcs": [
            {"name": "Solaf", "race": "Nord", "role": "merchant_general_goods", "level": 5}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 5005,
        "name": "Lod's House and Smithy",
        "desc": "The workshop and home of Lod, Falkreath's resident blacksmith. He is a skilled Nord smith, providing weapons, armor, and smithing services to the town. Lod is often busy at his forge and is known to be looking for a particular stray dog he's seen around town, believing it might bring him luck or inspiration.",
        "travel_desc": "Falkreath's blacksmith, run by Lod.",
        "tags": ["structure_type_shop_building", "structure_type_residence", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "quest_giver_daedric_clues_barbas_dog", "item_type_weapon_vendor", "item_type_armor_vendor", "business_owner_lod"],
        "density": "sparse",
        "context_tags": ["interior_shop_exterior_forge", "urban_town", "smithy_type"],
        "fixed_npcs": [
            {"name": "Lod", "race": "Nord", "role": "blacksmith", "level": 6}
        ],
        "exit_label_from_parent": "Smithy Entrance",
        "exit_label_to_parent": "Exit Smithy"
    },
    {
        "id": 5006,
        "name": "Hall of the Dead (Falkreath)",
        "desc": "Falkreath's hall for honoring the dead, managed by Runil, a priest of Arkay, who also tends the graveyard.",
        "travel_desc": "Falkreath's hall for honoring the dead.",
        "tags": ["structure_type_temple_building_hall_of_the_dead", "religious_site_aedric_arkay", "arkay_shrine_priest_runil", "settlement_features_catacombs_burial_access_potential", "quest_giver_potential_runil_ancestor_worhsip"],
        "density": "empty",
        "exit_label_from_parent": "Hall Entrance",
        "exit_label_to_parent": "Exit Hall"
    },
    {
        "id": 5007,
        "name": "Dark Brotherhood Sanctuary (Falkreath Entrance)",
        "desc": "A hidden sanctuary of the Dark Brotherhood, concealed within the pine forests near Falkreath. Its door is marked by a sinister black hand.",
        "travel_desc": "Hidden sanctuary of the Dark Brotherhood.",
        "tags": ["specific_landmark_type_assassin_guild_hq_active_dark_brotherhood", "secret_location_hidden_entrance_black_door", "dungeon_major_entrance_sanctuary", "terrain_forest_pine", "magical_properties_tainted_by_dark_magic_potential", "faction_dark_brotherhood_main_base"],
        "density": "empty",
        "exit_label_from_parent": "Path to Sanctuary",
        "exit_label_to_parent": "Leave Sanctuary Area"
    }
]