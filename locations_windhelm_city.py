WINDHELM_CITY_LOCATIONS = [
    {
        "id": 7001,
        "name": "Candlehearth Hall",
        "desc": "A large, historic, and popular tavern in Windhelm, easily recognizable by its large central hearth that is said to have burned for centuries. Run by Elda Early-Dawn, it's a common gathering place for Nords, Stormcloak soldiers, and travelers. Susanna the Wicked, a serving wench, is a notable employee. It's a prime spot for local news, rumors, and strong drink.",
        "travel_desc": "Windhelm's historic tavern, run by Elda Early-Dawn.",
        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "cultural_historical_significance_historic_site", "rumor_source", "food_drink_vendor", "lodging_available", "stormcloak_presence_patrons"],
        "context_tags": ["interior", "urban_city", "tavern_type_historic", "safe_zone"],
        "demographics": {"Nord": 60, "Dunmer": 20, "Argonian": 10, "Imperial": 5, "Breton": 3, "Khajiit": 2},
        "fixed_npcs": [
            {"name": "Elda Early-Dawn", "race": "Nord", "role": "innkeeper", "level": 7},
            {"name": "Susanna the Wicked", "race": "Nord", "role": "tavern_staff_server", "level": 4}
        ],
        "exit_label_from_parent": "Tavern Door",
        "exit_label_to_parent": "Exit Tavern"
    },
    {
        "id": 7002,
        "name": "Oengul's Smithy",
        "desc": "The primary blacksmith in Windhelm, run by the staunch Stormcloak supporter Oengul War-Anvil, with assistance from his apprentice Hermir Strong-Heart. They provide quality Nord-style arms and armor, essential for the ongoing war effort and for adventurers braving Eastmarch's dangers.",
        "travel_desc": "Windhelm's blacksmith, run by Oengul War-Anvil.",
        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor", "item_type_armor_vendor", "stormcloak_presence_owner_sympathizer", "business_owner_oengul"],
        "context_tags": ["interior_shop_exterior_forge", "urban_city", "smithy_type"],
        "fixed_npcs": [
            {"name": "Oengul War-Anvil", "race": "Nord", "role": "blacksmith_stormcloak_supporter", "level": 8},
            {"name": "Hermir Strong-Heart", "race": "Nord", "role": "blacksmith_apprentice", "level": 4}
        ],
        "exit_label_from_parent": "Smithy Entrance",
        "exit_label_to_parent": "Exit Smithy"
    },
    {
        "id": 7003,
        "name": "Palace of the Kings",
        "desc": "The formidable ancient seat of Ysgramor's dynasty, now serving as Jarl Ulfric Stormcloak's residence and military headquarters for his growing faction.",
        "travel_desc": "Ancient seat of Ysgramor's dynasty, Ulfric's HQ.",
        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local_stormcloak", "military_presence_stormcloak_hq", "cultural_historical_significance_ysgramor_related_site", "stormcloak_presence_strong", "unique_landmark_iconic", "political_tension_high_civil_war_focus"],
        "exit_label_from_parent": "Palace Doors",
        "exit_label_to_parent": "Exit Palace"
    },
    {
        "id": 7004,
        "name": "The White Phial",
        "desc": "An esteemed but somewhat cluttered apothecary shop run by the elderly and ailing Altmer alchemist, Nurelion. He is singularly obsessed with finding the legendary White Phial. His young apprentice, Quintus Navale, manages the day-to-day sales and worries about his master's health.",
        "travel_desc": "Apothecary run by Nurelion, seeker of the White Phial.",
        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_location_unique_artifact_white_phial", "unique_item_lore_artifact", "business_owner_nurelion"],
        "context_tags": ["interior", "urban_city", "shop_type_alchemy"],
        "fixed_npcs": [
            {"name": "Nurelion", "race": "Altmer", "role": "alchemist_master_ailing", "level": 10},
            {"name": "Quintus Navale", "race": "Imperial", "role": "alchemist_apprentice_shopkeeper", "level": 5}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 7005,
        "name": "Sadri's Used Wares",
        "desc": "Revyn Sadri's general goods store located in Windhelm's Gray Quarter. He is a Dunmer merchant who strives to be honest and fair, offering a variety of second-hand items, tools, and curiosities to the local community, despite the hardships faced by his people.",
        "travel_desc": "Revyn Sadri's general store in the Gray Quarter.",
        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "dunmer_culture_local", "settlement_features_district_ethnic_dunmer_gray_quarter", "business_owner_revyn_sadri", "quest_giver_potential_stolen_ring"],
        "context_tags": ["interior", "urban_city_district_gray_quarter", "shop_type"],
        "fixed_npcs": [
            {"name": "Revyn Sadri", "race": "Dunmer", "role": "merchant_general_goods", "level": 4}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 7006,
        "name": "Windhelm Market Square",
        "desc": "A bustling open-air market near the city gates of Windhelm, featuring various stalls. Aval Atheron sells general goods, while Niranye, an Altmer pawnbroker, deals in more discreet transactions. The atmosphere can be tense due to the city's political climate and racial undertones.",
        "travel_desc": "Windhelm's bustling open-air market.",
        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "urban_issues_or_atmosphere_tense_atmosphere", "item_type_food_vendor", "item_type_general_goods_vendor_stalls"],
        "context_tags": ["exterior", "urban_city", "market_type"],
        "fixed_npcs": [
            {"name": "Aval Atheron", "race": "Dunmer", "role": "merchant_stall_general", "level": 3},
            {"name": "Niranye", "race": "Altmer", "role": "merchant_stall_pawnbroker_fence", "level": 6}
        ],
        "exit_label_from_parent": "Enter Market",
        "exit_label_to_parent": "Leave Market"
    },
    {
        "id": 7007,
        "name": "Temple of Talos (Windhelm)",
        "desc": "A place of clandestine Talos worship, highly significant given the Stormcloak cause and the Thalmor's ban. Attended by those loyal to traditional Nord beliefs.",
        "travel_desc": "Place of clandestine Talos worship.",
        "tags": ["structure_type_temple_building", "religious_site_aedric_secret", "talos_shrine", "nordic_culture_strong", "political_tension_high_religious", "stormcloak_presence_strong", "thalmor_presence_hostile_potential"],
        "exit_label_from_parent": "Temple Doors",
        "exit_label_to_parent": "Exit Temple"
    },
    {
        "id": 7008,
        "name": "Gray Quarter (Dunmer District)",
        "desc": "The segregated district where most of Windhelm's Dunmer refugee population resides, often facing prejudice and harsh living conditions.",
        "travel_desc": "Segregated district for Windhelm's Dunmer refugees.",
        "tags": ["settlement_features_district_ethnic_dunmer_gray_quarter", "dunmer_culture_strong", "urban_issues_or_atmosphere_oppressive_atmosphere", "social_issue_racism_segregation", "social_issue_poverty"],
        "exit_label_from_parent": "Enter Gray Quarter",
        "exit_label_to_parent": "Leave Gray Quarter"
    },
    {
        "id": 7009,
        "name": "Argonian Assemblage (Docks)",
        "desc": "The dockside area where Windhelm's Argonian dockworkers are forced to live in cramped and poor conditions, working for low wages.",
        "travel_desc": "Dockside area where Argonian dockworkers live.",
        "tags": ["settlement_features_district_ethnic_argonian_assemblage", "argonian_culture_local", "urban_issues_or_atmosphere_oppressive_atmosphere", "social_issue_racism_segregation", "economic_activity_manual_labor", "settlement_features_docks_harbor"],
        "exit_label_from_parent": "Enter Assemblage",
        "exit_label_to_parent": "Leave Assemblage"
    },
    {
        "id": 7010,
        "name": "Aretino Residence",
        "desc": "The home of Aventus Aretino, a young boy attempting to perform the Black Sacrament to contact the Dark Brotherhood after the death of his mother.",
        "travel_desc": "Home of Aventus Aretino, performing the Black Sacrament.",
        "tags": ["structure_type_residence", "quest_location_dark_brotherhood_initiation", "social_issue_child_neglect_potential", "urban_dwelling_modest", "magical_properties_ritualistic_dark_sacrament"],
        "exit_label_from_parent": "House Door",
        "exit_label_to_parent": "Exit House"
    },
    {
        "id": 7011,
        "name": "Hall of the Dead (Windhelm)",
        "desc": "Windhelm's catacombs for honoring the dead, maintained by Helgird, a priestess of Arkay, who also deals with the city's recent murder victims.",
        "travel_desc": "Windhelm's catacombs for honoring the dead.",
        "tags": ["structure_type_catacombs_structure", "religious_site_aedric", "arkay_presence", "nordic_burial_site_major", "quest_location_investigation_serial_killer", "undead_presence_rumored_low"],
        "exit_label_from_parent": "Hall Entrance",
        "exit_label_to_parent": "Exit Hall"
    },
    {
        "id": 7012,
        "name": "Windhelm Port",
        "desc": "The icy docks of Windhelm, a vital hub for trade with northern Tamriel and Solstheim, despite the harsh conditions. Home to the East Empire Company office.",
        "travel_desc": "Icy docks of Windhelm, a vital trade hub.",
        "tags": ["settlement_features_docks_harbor", "economic_activity_trade_hub_major_maritime", "travel_hub_sea_solstheim", "climate_arctic_coastal", "east_empire_company_presence", "argonian_culture_local_nearby"],
        "exit_label_from_parent": "Enter Port",
        "exit_label_to_parent": "Leave Port"
    },
    {
        "id": 7013,
        "name": "New Gnisis Cornerclub",
        "desc": "A Dunmer-run tavern located in Windhelm's Gray Quarter, managed by Ambarys Rendar. It serves as a gathering place for the local Dunmer population, offering familiar food, drink, and a sense of community amidst the often harsh treatment they receive in the city.",
        "travel_desc": "Dunmer tavern in Windhelm's Gray Quarter, run by Ambarys Rendar.",
        "tags": ["structure_type_inn_building", "settlement_features_tavern_ethnic_dunmer", "social_hub_dunmer_community", "dunmer_culture_strong", "settlement_features_district_ethnic_dunmer_gray_quarter", "food_drink_vendor_dunmer_specialties", "lodging_available_basic", "rumor_source_dunmer_perspective"],
        "context_tags": ["interior", "urban_city_district_gray_quarter", "tavern_type_ethnic", "safe_zone_community"],
        "demographics": {"Dunmer": 80, "Nord": 10, "Argonian": 5, "Other": 5},
        "fixed_npcs": [
            {"name": "Ambarys Rendar", "race": "Dunmer", "role": "innkeeper_dunmer_community", "level": 6}
        ],
        "exit_label_from_parent": "Cornerclub Door",
        "exit_label_to_parent": "Exit Cornerclub"
    }
]