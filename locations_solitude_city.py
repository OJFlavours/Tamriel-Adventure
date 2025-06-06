SOLITUDE_CITY_LOCATIONS = [
    {
        "id": 8001,
        "name": "Blue Palace",
        "desc": "The opulent palace residence of High King Torygg and his court. A center of Imperial administration and Skyrim's nobility.",
        "travel_desc": "Opulent palace residence of High King Torygg.",
        "tags": ["structure_type_palace_or_manor", "government_local_skyrim_capital", "high_king_torygg_residence", "imperial_influence_strong_court", "noble_estate_district", "unique_landmark_iconic"],
        "density": "average",
        "exit_label_from_parent": "Palace Entrance",
        "exit_label_to_parent": "Exit Palace"
    },
    {
        "id": 8002,
        "name": "Castle Dour",
        "desc": "A robust Imperial fortification within Solitude, serving as the primary headquarters of the Imperial Legion in Skyrim under the command of a high-ranking Legate (General Tullius not yet arrived or in overall command).",
        "travel_desc": "Imperial Legion HQ in Solitude.",
        "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion_hq", "imperial_influence_dominant_military", "settlement_features_armory_barracks", "government_military_command"],
        "density": "bustling",
        "exit_label_from_parent": "Castle Gates",
        "exit_label_to_parent": "Exit Castle"
    },
    {
        "id": 8003,
        "name": "The Winking Skeever",
        "desc": "Solitude's most popular tavern, run by Corpulus Vinius. It's a bustling place, frequented by Imperial soldiers, nobles, merchants, Bards College students, and travelers from across Tamriel. The Argonian Gulum-Ei is a regular, often involved in shady dealings. It's an excellent spot for rumors, drinks, and finding work or companionship.",
        "travel_desc": "Solitude's popular tavern, run by Corpulus Vinius.",
        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available", "quest_giver_potential_gulum_ei", "business_owner_corpulus_vinius", "location_specific_winking_skeever"],
        "density": "bustling",
        "context_tags": ["interior", "urban_city_capital", "tavern_type_bustling", "safe_zone"],
        "demographics": {"Imperial": 30, "Nord": 40, "Breton": 10, "Redguard": 5, "Altmer": 5, "Khajiit": 5, "Argonian": 3, "Bosmer": 2},
        "fixed_npcs": [
            {"name": "Corpulus Vinius", "race": "Imperial", "role": "innkeeper", "level": 7},
            {"name": "Gulum-Ei", "race": "Argonian", "role": "shady_patron", "level": 5}
        ],
        "exit_label_from_parent": "Tavern Door",
        "exit_label_to_parent": "Exit Tavern"
    },
    {
        "id": 8004,
        "name": "Bits and Pieces",
        "desc": "A general goods store in Solitude, owned and operated by the Imperial merchant Sayma. The shop offers a wide variety of items, from common household supplies and tools to imported novelties and curiosities reflecting Solitude's status as a major port city.",
        "travel_desc": "General goods store in Solitude, run by Sayma.",
        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "economic_activity_trade_hub_local", "business_owner_sayma"],
        "density": "average",
        "context_tags": ["interior", "urban_city_capital", "shop_type"],
        "fixed_npcs": [
            {"name": "Sayma", "race": "Imperial", "role": "merchant_general_goods", "level": 6}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 8005,
        "name": "Angeline's Aromatics",
        "desc": "An apothecary shop run by Angeline Morrard, selling potions, ingredients, and alchemical supplies. Angeline is often concerned about her daughter serving in the Legion.",
        "travel_desc": "Apothecary shop selling potions and ingredients.",
        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_giver_potential_family_issue"],
        "density": "sparse",
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 8006,
        "name": "Radiant Raiment",
        "desc": "An upscale clothing store in Solitude, owned by the Altmer sisters Taarie and Endarie. They offer fine, fashionable attire and tailoring services, catering to the city's nobility and wealthy merchants. Both sisters are known for their somewhat haughty and critical attitudes, especially Taarie.",
        "travel_desc": "Upscale clothing store in Solitude, run by Taarie and Endarie.",
        "tags": ["structure_type_shop_building", "shop_specialty_goods_clothing", "economic_activity_tailoring_high_fashion", "altmer_presence_business", "social_hub_elite_potential", "business_owner_taarie_endarie"],
        "density": "average",
        "context_tags": ["interior", "urban_city_capital", "shop_type_clothing_high_end"],
        "fixed_npcs": [
            {"name": "Taarie", "race": "Altmer", "role": "merchant_clothing_tailor_haughty", "level": 5},
            {"name": "Endarie", "race": "Altmer", "role": "merchant_clothing_tailor", "level": 5}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 8007,
        "name": "Fletcher",
        "desc": "Fihada's fletching shop in Solitude, specializing in bows, arrows of all types, and other archery supplies. He is a Redguard craftsman who caters to the Imperial Legion, local hunters, and any archers passing through the capital.",
        "travel_desc": "Fihada's fletching shop in Solitude.",
        "tags": ["structure_type_shop_building", "shop_specialty_goods_archery", "item_type_weapon_bow_arrow_vendor", "economic_activity_crafting_fletching", "business_owner_fihada"],
        "density": "sparse",
        "context_tags": ["interior", "urban_city_capital", "shop_type_archery"],
        "fixed_npcs": [
            {"name": "Fihada", "race": "Redguard", "role": "merchant_fletcher", "level": 6}
        ],
        "exit_label_from_parent": "Shop Door",
        "exit_label_to_parent": "Exit Shop"
    },
    {
        "id": 8008,
        "name": "Solitude Blacksmith (Beirand)",
        "desc": "Beirand's smithy, located near Castle Dour, providing weapons, armor, and smithing services to the Legion and citizens.",
        "travel_desc": "Beirand's smithy, near Castle Dour.",
        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor", "item_type_armor_vendor", "imperial_legion_supplier_potential"],
        "density": "average",
        "exit_label_from_parent": "Smithy Entrance",
        "exit_label_to_parent": "Exit Smithy"
    },
    {
        "id": 8009,
        "name": "Bards College",
        "desc": "A renowned institution dedicated to preserving Skyrim's history and fostering the talents of bards, musicians, and performers. They hold an annual festival, the Burning of King Olaf.",
        "travel_desc": "Renowned institution for bards and musicians.",
        "tags": ["structure_type_guild_hall_building_college", "settlement_features_bards_college", "cultural_historical_significance_historic_institution", "quest_location_bards_college_main", "event_festival_king_olaf", "education_arts_music_lore", "unique_landmark_iconic"],
        "density": "average",
        "exit_label_from_parent": "College Entrance",
        "exit_label_to_parent": "Exit College"
    },
    {
        "id": 8010,
        "name": "Temple of the Divines (Solitude)",
        "desc": "A grand temple in Solitude dedicated to the worship of all Eight Divines (Talos worship is suppressed but may occur secretly). A center of religious life and Imperial faith.",
        "travel_desc": "Grand temple dedicated to the Eight Divines.",
        "tags": ["structure_type_temple_building_major", "religious_site_aedric_eight_divines", "imperial_influence_strong_religious", "talos_worship_banned_publicly", "event_wedding_location", "settlement_features_temple_divines"],
        "density": "average",
        "exit_label_from_parent": "Temple Doors",
        "exit_label_to_parent": "Exit Temple"
    },
    {
        "id": 8011,
        "name": "Solitude Docks",
        "desc": "The bustling port area of Solitude, handling sea trade from across Tamriel. Home to the East Empire Company Warehouse and various shipping businesses.",
        "travel_desc": "Bustling port area handling sea trade.",
        "tags": ["settlement_features_docks_harbor_major", "economic_activity_trade_hub_major_maritime", "east_empire_company_presence_hq", "travel_hub_sea_interprovincial", "structure_type_warehouse_district", "economic_activity_shipping_industry"],
        "density": "bustling",
        "exit_label_from_parent": "Path to Docks",
        "exit_label_to_parent": "Leave Docks"
    },
    {
        "id": 8012,
        "name": "Erikur's House",
        "desc": "The lavish residence of Thane Erikur, an influential and often corrupt noble in Solitude with significant business interests.",
        "travel_desc": "Lavish residence of Thane Erikur.",
        "tags": ["structure_type_residence_noble", "noble_estate_district", "political_tension_high_corruption", "economic_activity_trade_shady_deals", "thane_erikur_residence"],
        "density": "sparse",
        "exit_label_from_parent": "House Door",
        "exit_label_to_parent": "Exit House"
    },
    {
        "id": 8013,
        "name": "Thalmor Embassy (Access Point/Office in Solitude)",
        "desc": "While the main embassy is more remote, the Thalmor maintain a significant presence and office within Solitude to oversee Imperial compliance with the White-Gold Concordat, a source of much local resentment.",
        "travel_desc": "Thalmor office overseeing White-Gold Concordat compliance.",
        "tags": ["structure_type_embassy_office", "thalmor_presence_strong_office", "political_tension_high_foreign_occupation_aspect", "white_gold_concordat_enforcement_local", "urban_issues_or_atmosphere_fear_and_superstition_thalmor", "diplomatic_intrigue_high"],
        "density": "average",
        "exit_label_from_parent": "Embassy Office Door",
        "exit_label_to_parent": "Exit Office"
    }
]