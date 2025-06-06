from locations_riften_city import RIFTEN_CITY_LOCATIONS

THE_RIFT_LOCATIONS = [
    # THE RIFT
    {
        "id": 9,
        "name": "The Rift",
        "desc": "A temperate, autumnal hold in southeastern Skyrim, known for its golden forests, numerous lakes, and the city of Riften, a haven for the Thieves Guild and rife with corruption. It borders Morrowind and Cyrodiil.",
        "travel_desc": "Temperate, autumnal hold with golden forests and numerous lakes.",
        "tags": ["hold", "terrain_forest_autumnal_large_golden_woods", "terrain_lake_region_abundant_honrich_geir", "faction_thieves_guild_presence_strong_hq_riften", "nordic_culture_local_rift_traditions", "morrowind_border_region_velothi_mountains", "cyrodiil_border_region_jerall_mountains", "urban_issues_or_atmosphere_corrupt_underbelly_pervasive", "political_influence_black_briar_family_dominance_maven", "climate_temperate_continental", "beautiful_scenery_autumnal_lakes", "economic_activity_brewing_mead_ale_black_briar_honningbrew_rivalry_potential", "economic_activity_fishing_industry_local_lakes"],
        "density": "sparse",
        "demographics": {"Nord": 75, "Dunmer": 10, "Argonian": 10, "Khajiit": 3, "Others": 2},
        "travel": {
            "links": [
                {"name": "Whiterun Hold", "connection_type": "Road"},
                {"name": "Eastmarch", "connection_type": "Road"},
                {"name": "Falkreath Hold", "connection_type": "Road"},
                {"name": "Cyrodiil (Lost Prospect Pass)", "connection_type": "Road"},
                {"name": "Morrowind (Velothi Mountains route)", "connection_type": "Road"},
                {"name": "Goldenglow Path", "connection_type": "Path"},
                {"name": "Jerall Mountain Trail", "connection_type": "Path"},
                {"name": "Velothi Mountains Pass", "connection_type": "Path"},
                {"name": "Lake Honrich Shoreline", "connection_type": "Path"}
            ]
        },
        "sub_locations": [
            {
                "id": 90,
                "name": "Riften",
                "desc": "A city built upon a lake, with canals running through its wooden structures. It is infamous for corruption, the powerful Black-Briar family's influence, and being the headquarters of the Thieves Guild under Mercer Frey.",
                "travel_desc": "City built upon a lake, infamous for corruption and Thieves Guild HQ.",
                "tags": ["populated_city", "terrain_lake_city_canals_wooden_structures", "city_affiliation_the_rift_capital", "faction_thieves_guild_presence_strong_hq_ratway", "political_influence_black_briar_family_total_maven_control", "urban_issues_or_atmosphere_corrupt_city_major_infamous", "settlement_features_jarls_longhouse_laila_law_giver_figurehead", "mercenary_presence_strong_black_briar_thugs", "structure_type_wooden_architecture_canals_unique", "unique_landmark_iconic_canal_city_mistveil_keep", "urban_issues_or_atmosphere_high_crime_rate_thievery"],
                "density": "bustling",
                "exit_label_from_parent": "City Gates",
                "exit_label_to_parent": "City Gates",
                "sub_locations": RIFTEN_CITY_LOCATIONS
            },
            {
                "id": 91,
                "name": "Shor's Stone",
                "desc": "A small mining village in the northern Rift, primarily focused on an ebony mine that has recently been troubled by giant frostbite spiders from a nearby cave.",
                "travel_desc": "Small mining village focused on a troubled ebony mine.",
                "tags": ["populated_village", "settlement_minor_mining", "economic_activity_mining_ebony", "resource_node_ebony_rare", "monster_infestation_spider_recent", "quest_location_clear_mine", "terrain_northern_rift_mountains"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Village",
                "exit_label_to_parent": "Leave Village",
                "sub_locations": [
                    {
                        "id": 9101,
                        "name": "Redbelly Mine",
                        "desc": "The ebony mine that is the main source of livelihood for Shor's Stone, currently unsafe due to spider infestation.",
                        "travel_desc": "Ebony mine, currently unsafe due to spiders.",
                        "tags": ["structure_type_mine_active_infested", "economic_activity_mining_ebony", "resource_node_ebony_dangerous", "monster_infestation_spider_major", "quest_location_clear_mine_shors_stone", "dungeon_minor_mine_infested"],
                        "density": "average",
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    },
                    {
                        "id": 9102,
                        "name": "Sylgja's House",
                        "desc": "The home of Sylgja, a miner in Shor's Stone, whose father works in Darkwater Crossing.",
                        "travel_desc": "Home of Sylgja, a miner in Shor's Stone.",
                        "tags": ["structure_type_residence", "commoner_dwelling_miner", "quest_giver_potential_family_related"],
                        "density": "sparse",
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    },
                    {
                        "id": 9103,
                        "name": "Filnjar's House and Smithy",
                        "desc": "The home and modest smithy of Filnjar, the blacksmith of Shor's Stone.",
                        "travel_desc": "Home and smithy of Filnjar, blacksmith of Shor's Stone.",
                        "tags": ["structure_type_residence", "structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor_potential", "item_type_armor_vendor_potential"],
                        "density": "sparse",
                        "exit_label_from_parent": "Smithy Entrance",
                        "exit_label_to_parent": "Exit Smithy"
                    }
                ]
            },
            {
                "id": 92,
                "name": "Ivarstead",
                "desc": "A small village at the foot of the Throat of the World, on the shores of Lake Geir. It is the traditional starting point for the pilgrimage up the Seven Thousand Steps to High Hrothgar.",
                "travel_desc": "Small village, starting point for High Hrothgar pilgrimage.",
                "tags": ["populated_village", "settlement_minor_pilgrimage_base", "travel_hub_pilgrimage_high_hrothgar", "terrain_lake_geir_shoreline", "terrain_mountain_foot_throat_of_world", "cultural_historical_significance_greybeards_path_start", "climate_temperate_mountain_valley"],
                "density": "average",
                "exit_label_from_parent": "Path to Village",
                "exit_label_to_parent": "Leave Village",
                "sub_locations": [
                    {
                        "id": 9201,
                        "name": "Vilemyr Inn",
                        "desc": "The only inn in the quiet village of Ivarstead, nestled at the foot of the 7,000 Steps. Run by the aging but kind Wilhelm, it's a common resting place for pilgrims heading to High Hrothgar. Wilhelm is often worried about the nearby Shroud Hearth Barrow and the strange noises emanating from it. The inn has a warm fire and a few regulars, but it's not as boisterous as taverns in larger cities.",
                        "travel_desc": "Ivarstead's inn, run by Wilhelm, a stop for High Hrothgar pilgrims.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source", "quest_giver_potential_barrow_investigation_wilhelm", "location_specific_vilemyr_inn"],
                        "density": "average",
                        "context_tags": ["interior", "village_type", "tavern_type", "safe_zone"],
                        "demographics": {"Nord": 85, "Imperial": 5, "Breton": 5, "Dunmer": 5},
                        "fixed_npcs": [
                            {"name": "Wilhelm", "race": "Nord", "role": "innkeeper", "level": 7}
                        ],
                        "exit_label_from_parent": "Inn Door",
                        "exit_label_to_parent": "Exit Inn"
                    },
                    {
                        "id": 9202,
                        "name": "Shroud Hearth Barrow (Ivarstead Entrance)",
                        "desc": "An ancient Nordic barrow located within Ivarstead itself. Locals believe it to be haunted and avoid it, though Wilhelm seeks someone to investigate.",
                        "travel_desc": "Ancient Nordic barrow within Ivarstead, believed haunted.",
                        "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong_draugr", "magical_properties_haunted_aura", "quest_location_local_investigation_ivarstead", "puzzle_dragon_claw_sapphire", "cultural_historical_significance_nordic_ancient_site", "urban_issues_or_atmosphere_haunted_rumors_strong"],
                        "density": "average",
                        "exit_label_from_parent": "Barrow Entrance",
                        "exit_label_to_parent": "Exit Barrow"
                    },
                    {
                        "id": 9203,
                        "name": "Klimmek's House",
                        "desc": "The home of Klimmek, a resident of Ivarstead who makes regular supply deliveries to High Hrothgar for the Greybeards.",
                        "travel_desc": "Home of Klimmek, makes deliveries to High Hrothgar.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "quest_giver_potential_high_hrothgar_delivery", "greybeards_related_supplier"],
                        "density": "sparse",
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    },
                    {
                        "id": 9204,
                        "name": "Narfi's Wrecked House",
                        "desc": "The ruined and isolated house of Narfi, a distraught beggar living across the river from Ivarstead, searching for his missing sister.",
                        "travel_desc": "Ruined house of Narfi, a distraught beggar.",
                        "tags": ["structure_type_ruined_shack", "structure_condition_collapsed", "hermit_lair_beggar", "quest_location_dark_brotherhood_target_potential", "social_issue_poverty_grief", "isolated_location_river_other_side"],
                        "density": "sparse",
                        "exit_label_from_parent": "Path to Ruin",
                        "exit_label_to_parent": "Exit Ruin"
                    }
                ]
            },
            {
                "id": 93,
                "name": "Lost Prospect Mine",
                "desc": "An abandoned gold mine in the Rift, often occupied by bandits. It is rumored to be played out, but some say a few veins might remain for the determined.",
                "travel_desc": "Abandoned gold mine, often occupied by bandits.",
                "tags": ["structure_type_mine_abandoned", "economic_activity_mining_gold_historic", "resource_node_gold_rumored_depleted", "bandit_minor_camp_potential", "dungeon_minor", "exploration_challenge_potential_reward", "terrain_eastern_rift_mountains"],
                "density": "sparse",
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 94,
                "name": "Broken Helm Hollow",
                "desc": "A secluded cave system east of Riften, serving as a well-established bandit hideout with multiple chambers.",
                "travel_desc": "Secluded cave system, well-established bandit hideout.",
                "tags": ["structure_type_natural_cave", "bandit_main_stronghold", "dungeon_major_multi_level", "state_or_condition_current_bandit_controlled_area", "terrain_eastern_rift_forest", "quest_location_bounty_potential"],
                "density": "average",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 95,
                "name": "Avanchnzel",
                "desc": "A large and dangerous Dwemer ruin in the southern mountains of the Rift. It contains ancient technology, Falmer, and is the focus of a quest to retrieve a unique Dwemer lexicon for From-Deepest-Fathoms.",
                "travel_desc": "Large, dangerous Dwemer ruin with ancient technology.",
                "tags": ["dwemer_ruin_major_city", "dungeon_large_complex", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "quest_location_unique_artifact_dwemer_lexicon", "ancient_technology_dwemer", "cultural_historical_significance_dwemer_ruin_site", "terrain_southern_rift_mountains", "chaurus_nest_potential"],
                "density": "bustling",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 96,
                "name": "Boulderfall Cave",
                "desc": "A cave in the eastern Rift, often inhabited by necromancers or other dark mages who use its seclusion for their sinister experiments.",
                "travel_desc": "Cave often inhabited by necromancers.",
                "tags": ["structure_type_natural_cave", "specific_landmark_type_necromancer_lair", "magical_properties_tainted_by_dark_magic", "dungeon_minor", "undead_presence_skeletons_experiments", "ritual_site_dark_magic", "terrain_eastern_rift_wilderness"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 97,
                "name": "Clearspring Tarn",
                "desc": "A small, picturesque tarn and cave system west of Shor's Stone, often home to trolls guarding a treasure hunter's remains and note.",
                "travel_desc": "Picturesque tarn and cave system, often home to trolls.",
                "tags": ["structure_type_natural_cave_tarn", "monster_den_troll_guardian", "unique_natural_formation_tarn", "treasure_cache_minor_hunter_remains", "dungeon_minor", "secluded_nature_spot", "alchemy_ingredient_source_rich_potential"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 98,
                "name": "Crystaldrift Cave",
                "desc": "A small ice cave south of Riften, notable for its unique crystal formations. It is sometimes a den for frost creatures or a reclusive hermit.",
                "travel_desc": "Small ice cave notable for unique crystal formations.",
                "tags": ["structure_type_natural_cave_ice", "unique_natural_formation_crystal_cave", "monster_den_frost_creatures_potential", "hermit_lair_potential", "dungeon_minor", "climate_cold_cave", "alchemy_ingredient_source_rich_crystals_potential"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 99,
                "name": "Darklight Tower",
                "desc": "A ruined tower southwest of Riften, now a den for hagravens and the site of a Daedric quest where Illia attempts to stop her mother from becoming a hagraven.",
                "travel_desc": "Ruined tower, den for hagravens and site of Daedric quest.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main", "magical_properties_tainted_by_dark_magic", "dungeon_major_vertical", "quest_location_daedric_related_illia", "monster_den_hagraven_powerful", "witch_coven_powerful", "terrain_southern_rift_mountains"],
                "density": "average",
                "exit_label_from_parent": "Tower Entrance",
                "exit_label_to_parent": "Exit Tower"
            },
            {
                "id": 90001,
                "name": "Treva's Watch",
                "desc": "A ruined fort west of Ivarstead, taken over by bandits. Stalleo, a Nord whose family was driven out, seeks help to reclaim it.",
                "travel_desc": "Ruined fort taken over by bandits.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold", "dungeon_major", "quest_location_reclaim_fort_family", "state_or_condition_current_bandit_controlled_area", "terrain_western_rift_river"],
                "density": "average",
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 90002,
                "name": "Nilheim",
                "desc": "A ruined watchtower east of Ivarstead, occupied by bandits who employ a clever ambush by pretending to be legitimate guards.",
                "travel_desc": "Ruined watchtower occupied by bandits using an ambush tactic.",
                "tags": ["structure_type_ruined_tower", "bandit_minor_camp_deceptive_ambush", "dungeon_minor", "roadside_danger_spot", "quest_location_minor_investigation_potential", "terrain_eastern_rift_roadside"]
            }
        ]
    }
]