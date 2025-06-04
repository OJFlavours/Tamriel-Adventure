WINTERHOLD_CITY_LOCATIONS = [
    {
        "id": 30,
        "name": "Winterhold (Town Remnants)",
        "desc": "A shadow of its former self, this small, windswept town clings to the cliffs, overshadowed by the imposing College. Most of the original grand city now lies beneath the waves due to the Great Collapse.",
        "travel_desc": "Small, windswept town, a shadow of its former self.",
        "tags": ["populated_town_remnants", "structure_condition_ruined_extensively_city_lost_to_sea", "city_affiliation_winterhold_town_ruined", "magical_properties_arcane_nexus_college_nearby", "cultural_historical_significance_great_collapse_affected_site_epicenter", "state_or_condition_current_isolated_and_forgotten_shadow_of_former_self", "settlement_features_jarls_longhouse", "urban_issues_or_atmosphere_fear_and_superstition_college_mistrust", "climate_glacial_coastal_windswept", "faction_college_of_winterhold_overshadowing_presence"],
        "exit_label_from_parent": "Path to Town",
        "exit_label_to_parent": "Leave Town",
        "sub_locations": [
            {
                "id": 3001,
                "name": "The Frozen Hearth",
                "desc": "The only inn still operating in the sparse remnants of Winterhold town. Run by Dagur, it provides a somewhat grim shelter from the biting winds for the few locals, College members, and hardy travelers. Nelacar, a former College mage, can often be found here, and may have information or tasks related to Daedric artifacts.",
                "travel_desc": "Winterhold's sole inn, run by Dagur; Nelacar is a notable patron.",
                "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular_local_college", "rumor_source_college_local_issues", "food_drink_vendor", "lodging_available", "structure_condition_weathered_sole_survivor_inn", "quest_giver_potential_nelacar_azuras_star", "location_specific_frozen_hearth"],
                "context_tags": ["interior", "urban_town_remnants", "tavern_type", "safe_zone"],
                "demographics": {"Nord": 60, "Altmer": 15, "Dunmer": 10, "Breton": 10, "Imperial": 5},
                "fixed_npcs": [
                    {"name": "Dagur", "race": "Nord", "role": "innkeeper", "level": 7},
                    {"name": "Nelacar", "race": "Altmer", "role": "scholar_mage_reclusive", "level": 10}
                ],
                "exit_label_from_parent": "Inn Door",
                "exit_label_to_parent": "Exit Inn"
            },
            {
                "id": 3002,
                "name": "College of Winterhold",
                "desc": "A venerable institution of magic, perched precariously on a separated clifftop, a beacon for mages across Tamriel. Led by Arch-Mage Savos Aren.",
                "travel_desc": "Venerable institution of magic on a clifftop.",
                "tags": ["structure_type_guild_hall_building_college", "settlement_features_college_of_winterhold_main", "magical_properties_arcane_nexus_major", "cultural_historical_significance_ancient_magical_site_venerable", "political_tension_high_town_relations", "unique_landmark_iconic_cliff_perch", "quest_location_college_of_winterhold_main_questline", "faction_college_of_winterhold_hq", "education_magic_arcane_arts"],
                "exit_label_from_parent": "College Bridge",
                "exit_label_to_parent": "Leave College",
                "sub_locations": [
                    {
                        "id": 30021,
                        "name": "The Midden",
                        "desc": "The dark, forgotten underbelly of the College of Winterhold, a network of icy tunnels and chambers. Used for refuse, dangerous experiments, and rumored to hide darker secrets, including the Atronach Forge.",
                        "travel_desc": "Dark, forgotten underbelly of the College.",
                        "tags": ["environment_underground_icy_tunnels", "dungeon_major_college_undercroft", "magical_properties_tainted_by_dark_magic_experiments", "specific_landmark_type_atronach_forge_location", "undead_presence_rumored_strong_failed_experiments", "secret_location_college_secrets", "faction_college_of_winterhold_related_dark_secrets", "monster_den_ice_wraith_skeletons_potential"],
                        "exit_label_from_parent": "Enter The Midden",
                        "exit_label_to_parent": "Exit to College Courtyard"
                    }
                ]
            },
            {
                "id": 3003,
                "name": "Jarl's Longhouse (Winterhold)",
                "desc": "The modest seat of Winterhold's Jarl Korir, a man bitter about the College's perceived indifference to the town's plight.",
                "travel_desc": "Modest seat of Winterhold's Jarl Korir.",
                "tags": ["structure_type_palace_or_manor_modest", "settlement_features_jarls_longhouse", "government_local_jarl_korir", "structure_condition_weathered_struggling", "political_tension_high_college_mistrust_bitterness"],
                "exit_label_from_parent": "Longhouse Door",
                "exit_label_to_parent": "Exit Longhouse"
            },
            {
                "id": 3004,
                "name": "Birna's Oddments",
                "desc": "A small, struggling general goods store in Winterhold, run by the Nord woman Birna. Her stock is meager, consisting of various oddments and scavenged items. She may possess items of surprising value or historical interest, like a certain dragon claw, if one knows to ask or can afford her prices.",
                "travel_desc": "Small general goods store in Winterhold, run by Birna.",
                "tags": ["structure_type_shop_building", "shop_general_goods_oddments", "trade_variety_limited_scavenged", "economic_activity_trade_hub_minor_struggling", "structure_condition_weathered", "quest_giver_potential_coral_dragon_claw", "business_owner_birna"],
                "context_tags": ["interior", "urban_town_remnants", "shop_type"],
                "fixed_npcs": [
                    {"name": "Birna", "race": "Nord", "role": "merchant_general_goods", "level": 3}
                ],
                "exit_label_from_parent": "Shop Door",
                "exit_label_to_parent": "Exit Shop"
            }
        ]
    }
]