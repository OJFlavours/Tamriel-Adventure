from locations_windhelm_city import WINDHELM_CITY_LOCATIONS

EASTMARCH_LOCATIONS = [
    # EASTMARCH
    {
        "id": 7,
        "name": "Eastmarch",
        "desc": "A harsh, volcanic hold in eastern Skyrim, dominated by the ancient city of Windhelm, seat of Jarl Ulfric Stormcloak and a center of growing rebellion. Known for its hot springs, giants, and fierce Nordic traditions.",
        "travel_desc": "Harsh, volcanic hold, home to Windhelm and Stormcloak rebellion.",
        "tags": ["hold", "terrain_volcanic_tundra", "nordic_culture_strong_ancient", "stormcloak_presence_strong_capital", "terrain_hot_springs", "specific_landmark_type_giant_camp_region", "political_tension_high_civil_war_epicenter", "morrowind_border_region", "climate_subarctic_volcanic", "environment_geothermal_area", "dunmer_refugee_presence_significant", "argonian_worker_presence_significant"],
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
                "exit_label_from_parent": "Path to Village",
                "exit_label_to_parent": "Leave Village",
                 "sub_locations": [
                    {
                        "id": 7101,
                        "name": "Braidwood Inn",
                        "desc": "The local inn in the small mining village of Kynesgrove, run by Iddra. It provides essential food, lodging, and a place for the local miners and infrequent travelers to gather. Roggi Knot-Beard, a miner, is a frequent patron.",
                        "travel_desc": "Kynesgrove's local inn, run by Iddra.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source", "business_owner_iddra", "location_specific_braidwood_inn"],
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
                "exit_label_from_parent": "Fort Gates",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 73,
                "name": "Eldergleam Sanctuary",
                "desc": "A sacred, tranquil grove hidden in Eastmarch, home to the ancient and revered Eldergleam tree. A place of pilgrimage and natural wonder, protected by nature spirits.",
                "travel_desc": "Sacred, tranquil grove, home to the Eldergleam tree.",
                "tags": ["cultural_historical_significance_sacred_grove_kynareth_eldergleam", "unique_natural_formation_magical_tree_eldergleam", "magical_properties_aedric_blessing_active", "quest_location_kynareth_gildergreen_restoration_whiterun", "monster_den_spriggan_potential_guardians", "secluded_nature_spot_pilgrimage", "alchemy_ingredient_source_rich_unique_bark_sap", "terrain_forest_eastmarch_hidden_sanctuary"],
                "exit_label_from_parent": "Path to Sanctuary",
                "exit_label_to_parent": "Leave Sanctuary"
            },
            {
                "id": 74,
                "name": "Narzulbur",
                "desc": "An Orc stronghold in Eastmarch, situated near a rich ebony mine. They adhere strictly to the Code of Malacath and are wary of outsiders.",
                "travel_desc": "Orc stronghold near a rich ebony mine.",
                "tags": ["orc_stronghold", "populated_settlement_orcish", "economic_activity_mining_ebony", "malacath_worship", "structure_type_fortified_settlement", "cultural_historical_significance_orc_tradition", "terrain_volcanic_tundra_mountains_eastmarch", "warrior_culture_orcish", "isolated_location", "faction_orc_tribe_narzulbur", "quest_giver_potential_orc_chief_issues"],
                "exit_label_from_parent": "Stronghold Gate",
                "exit_label_to_parent": "Leave Stronghold",
                "sub_locations": [
                    {
                        "id": 7401,
                        "name": "Mauhulakh's Longhouse",
                        "desc": "The longhouse of Chief Mauhulakh, stern leader of Narzulbur.",
                        "travel_desc": "Longhouse of Chief Mauhulakh.",
                        "tags": ["structure_type_longhouse_orcish", "government_tribal", "chieftains_hall", "residence_chief"],
                        "exit_label_from_parent": "Longhouse Door",
                        "exit_label_to_parent": "Exit Longhouse"
                    },
                    {
                        "id": 7402,
                        "name": "Gloombound Mine (Ebony)",
                        "desc": "Narzulbur's productive ebony mine, a source of great wealth and Orcish pride, but also dangers from deep within.",
                        "travel_desc": "Narzulbur's productive ebony mine.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_ebony", "resource_node_ebony", "dungeon_minor_extension_potential", "orc_controlled_mine"],
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
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 76,
                "name": "Bonestrewn Crest",
                "desc": "A mountain peak in the southern volcanic region of Eastmarch, an ancient dragon lair and site of a Word Wall, though no dragon has roosted here for centuries.",
                "travel_desc": "Mountain peak, ancient dragon lair and Word Wall site.",
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "terrain_mountain_peak_volcanic_southern_eastmarch", "dungeon_minor_lair_potential", "cultural_historical_significance_dragon_lore_site_ancient", "climate_subarctic_volcanic", "exploration_point_remote_lore_word_wall"],
                "exit_label_from_parent": "Path to Crest",
                "exit_label_to_parent": "Leave Crest Area"
            },
            {
                "id": 77,
                "name": "Cronvangr Cave",
                "desc": "A large cave system in the hot springs region of Eastmarch, heavily infested with giant frostbite spiders. Rumors also speak of a hidden vampire presence within.",
                "travel_desc": "Large cave system infested with giant frostbite spiders.",
                "tags": ["structure_type_natural_cave_large", "monster_den_spider_major_frostbite", "specific_landmark_type_vampire_coven_minor_potential_hidden_section", "dungeon_major", "terrain_hot_springs_nearby_eastmarch", "alchemy_ingredient_source_rich_venom_spider_eggs", "quest_location_bounty_potential_spiders_vampires"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 78,
                "name": "Darkwater Crossing",
                "desc": "A small mining settlement on the Darkwater River, primarily focused on corundum ore. A mix of Nords and Argonians work and live here.",
                "travel_desc": "Small mining settlement focused on corundum ore.",
                "tags": ["populated_village_mining", "settlement_minor", "economic_activity_mining_corundum", "argonian_culture_local_workers", "terrain_river_delta_darkwater", "climate_volcanic_tundra_edge", "quest_giver_potential_local_issues_mine_related_argonian_concerns"],
                "exit_label_from_parent": "Path to Settlement",
                "exit_label_to_parent": "Leave Settlement",
                "sub_locations": [
                    {
                        "id": 7801,
                        "name": "Goldenrock Mine",
                        "desc": "The corundum mine that supports Darkwater Crossing, known for its rich veins.",
                        "travel_desc": "Corundum mine supporting Darkwater Crossing.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_corundum", "resource_node_corundum"],
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    }
                ]
            },
            {
                "id": 79,
                "name": "Gallows Rock",
                "desc": "A ruined fort southwest of Windhelm, now serving as a major stronghold for the Silver Hand, hunters of werewolves. A dangerous place for any lycanthrope.",
                "travel_desc": "Ruined fort, a major Silver Hand stronghold.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_silver_hand_hq_major", "dungeon_major", "quest_location_companions_guild_hall_silver_hand_conflict", "faction_hostile_silver_hand_stronghold", "state_or_condition_current_enemy_controlled_area_silver_hand", "werewolf_lore_silver_hand_hunters"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 70001,
                "name": "Gloomreach",
                "desc": "A dark and winding cave system in the southern mountains of Eastmarch, often inhabited by Falmer, Chaurus, or other dangerous subterranean creatures.",
                "travel_desc": "Dark, winding cave system inhabited by Falmer and Chaurus.",
                "tags": ["structure_type_natural_cave_winding", "falmer_presence_strong_potential", "chaurus_nest_potential", "dungeon_major", "terrain_mountainous_southern_eastmarch", "environment_underground_dark_gloomreach", "state_or_condition_current_lawless_area_falmer_territory_potential", "exploration_challenge_dangerous_subterranean"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 70002,
                "name": "Lost Knife Hideout",
                "desc": "A large cave system serving as a major bandit hideout, located near the border with The Rift. Known for its ruthless gang, the 'Lost Knife' bandits.",
                "travel_desc": "Large cave system, a major bandit hideout.",
                "tags": ["structure_type_natural_cave_large_hideout", "bandit_main_stronghold_lost_knife_gang", "dungeon_major", "state_or_condition_current_bandit_controlled_area", "quest_location_bounty_leader_lost_knife", "economic_activity_looting_storage_bandit_operations", "terrain_eastmarch_rift_border"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 70003,
                "name": "Mixwater Mill",
                "desc": "A lumber mill on the White River in Eastmarch, run by Gilfre. A quiet spot, but travelers sometimes report strange noises from the nearby woods at night.",
                "travel_desc": "Lumber mill on the White River, run by Gilfre.",
                "tags": ["structure_type_lumber_mill_site", "settlement_minor", "economic_activity_logging_timber", "terrain_river_delta_white_river", "climate_volcanic_tundra_edge", "mystery_local_rumor_strange_noises_woods", "peaceful_area_potential", "quest_giver_potential_gilfre_marriage_local_issues"],
                "exit_label_from_parent": "Path to Mill",
                "exit_label_to_parent": "Leave Mill"
            },
            {
                "id": 70004,
                "name": "Morvunskar",
                "desc": "A ruined fort south of Windhelm, now occupied by hostile mages. During particular revelries, a portal to Sanguine's realm of Oblivion might be found here.",
                "travel_desc": "Ruined fort occupied by hostile mages, portal to Sanguine's realm.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_mage_lair_hostile_conjurers", "quest_location_daedric_sanguine_a_night_to_remember", "dungeon_major", "magical_properties_daedric_influence_overt_temporary_sanguine_portal", "undead_presence_potential_conjured", "portal_to_oblivion_sanguine_temporary_misty_grove", "terrain_south_windhelm_roadside"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 70005,
                "name": "Refugees' Rest",
                "desc": "A small, ruined Nordic structure east of Windhelm, marking a somber historical event related to the Night of Tears or similar ancient tragedy. Often haunted by sorrowful spirits.",
                "travel_desc": "Small, ruined Nordic structure marking a somber event.",
                "tags": ["structure_type_ruined_shrine_nordic_somber", "cultural_historical_significance_nordic_ancient_site_tragedy_night_of_tears_refugees", "magical_properties_haunted_aura_sorrowful_spirits", "undead_presence_ghosts_potential", "terrain_volcanic_tundra_east_windhelm", "night_of_tears_related_rumor", "exploration_point_historic_memorial"],
                "exit_label_from_parent": "Path to Ruin",
                "exit_label_to_parent": "Leave Ruin"
            },
            {
                "id": 70006,
                "name": "Riverside Shack",
                "desc": "A small, isolated shack on the banks of the White River, sometimes home to a reclusive fisherman, a desperate poacher, or even a territorial creature.",
                "travel_desc": "Small, isolated shack on the banks of the White River.",
                "tags": ["structure_type_shack_or_hut_isolated", "terrain_river_delta_white_river", "hermit_lair_potential_fisherman_poacher", "economic_activity_fishing_subsistence_potential", "monster_den_mudcrab_potential", "isolated_location", "exploration_point_minor_dwelling"],
                "exit_label_from_parent": "Path to Shack",
                "exit_label_to_parent": "Leave Shack Area"
            },
            {
                "id": 70007,
                "name": "Stony Creek Cave",
                "desc": "A cave in the southern part of Eastmarch's volcanic tundra, inhabited by bandits who have discovered a valuable alchemical ingredient deep within - Finn's Lute for the Bards College.",
                "travel_desc": "Cave inhabited by bandits, contains Finn's Lute.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "alchemy_ingredient_source_rich_unique_flora_deep_within", "quest_location_bards_college_finns_lute", "terrain_volcanic_tundra_southern_eastmarch", "treasure_cache_rumored_bandit_loot", "state_or_condition_current_bandit_controlled_area"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 70008,
                "name": "Traitor's Post",
                "desc": "A small, abandoned shack east of Windhelm, rumored to have been used by outlaws or spies. It's often a meeting point for clandestine activities.",
                "travel_desc": "Small, abandoned shack, rumored outlaw meeting point.",
                "tags": ["structure_type_shack_or_hut_abandoned_ominous", "bandit_minor_camp_potential_clandestine_meeting_spot", "spy_network_rumor_outlaws", "treasure_cache_rumored_hidden", "terrain_volcanic_tundra_roadside_east_windhelm", "quest_location_minor_intrigue_potential", "exploration_point_mystery_shack"],
                "exit_label_from_parent": "Path to Post",
                "exit_label_to_parent": "Leave Post Area"
            },
            {
                "id": 70009,
                "name": "Uttering Hills Cave",
                "desc": "A cave system southwest of Windhelm, serving as a hideout for a group of bandits.",
                "travel_desc": "Cave system, hideout for Summerset Shadows bandits.",
                "tags": ["structure_type_natural_cave_system", "bandit_main_stronghold_altmer_summerset_shadows", "dungeon_major", "faction_hostile_summerset_shadows", "quest_location_thieves_guild_potential_summerset_shadows_quest", "altmer_presence_hostile_bandits", "state_or_condition_current_bandit_controlled_area_altmer", "terrain_southwest_windhelm_hills"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 70010,
                "name": "Witchmist Grove",
                "desc": "A mystical grove in the southern hot springs region of Eastmarch, home to unique flora, spriggans, and possibly a reclusive hagraven or witch.",
                "travel_desc": "Mystical grove with unique flora and spriggans.",
                "tags": ["unique_natural_formation_magical_grove_mystical", "monster_den_spriggan_strong_guardians", "specific_landmark_type_hagraven_coven_lair_potential_reclusive_witch", "terrain_hot_springs_southern_eastmarch", "alchemy_ingredient_source_rich_unique_flora_witchmist", "ritual_site_nature_magic_potential_primal", "magical_properties_enchanted_neutral_wild_magic", "witch_coven_potential_rumor"],
                "exit_label_from_parent": "Path to Grove",
                "exit_label_to_parent": "Leave Grove"
            },
            {
                "id": 70013,
                "name": "Cragwallow Slope",
                "desc": "A dangerous, rocky slope in the volcanic tundra, known for its frequent rockfalls and as a nesting ground for cliff racers or other aerial predators if they were native.",
                "travel_desc": "Dangerous, rocky slope known for frequent rockfalls.",
                "tags": ["terrain_volcanic_tundra_slope_dangerous", "dangerous_terrain_rockslides_frequent", "monster_den_cliff_racer_skyrim_equivalent_potential_aerial_predators", "environment_wilderness_hazard_zone", "exploration_challenge_environmental_perilous", "climate_subarctic_volcanic", "dungeon_minor_outdoor_hazard_area"],
                "exit_label_from_parent": "Path to Slope",
                "exit_label_to_parent": "Leave Slope Area"
            },
            {
                "id": 70014,
                "name": "Steamcrag Camp",
                "desc": "A large camp of giants and mammoths situated in the hot springs region of Eastmarch, generally peaceful unless provoked.",
                "travel_desc": "Large camp of giants and mammoths in hot springs region.",
                "tags": ["specific_landmark_type_giant_camp_established_major", "mammoth_herd_grazing_large", "terrain_hot_springs_eastmarch", "neutral_encounter_giant_mammoth_peaceful_unless_provoked", "terrain_volcanic_tundra", "cultural_historical_significance_giant_territory_traditional_camp"],
                "exit_label_from_parent": "Path to Camp",
                "exit_label_to_parent": "Leave Camp Area"
            },
            {
                "id": 70015,
                "name": "Abandoned Lodge of the Nine Holds",
                "desc": "A once-grand hunting lodge in the eastern forests, now fallen into disrepair and rumored to be haunted by its former occupants or used by bandits.",
                "travel_desc": "Once-grand hunting lodge, now ruined and rumored haunted.",
                "tags": ["structure_type_lodge_abandoned_grand_historic", "structure_condition_ruined_extensively_dilapidated", "magical_properties_haunted_aura_potential_former_occupants", "bandit_minor_camp_potential_hideout", "terrain_forest_eastmarch_isolated", "dungeon_minor", "cultural_historical_significance_historic_site_minor_nine_holds_lodge"],
                "exit_label_from_parent": "Path to Lodge",
                "exit_label_to_parent": "Leave Lodge Area"
            },
            {
                "id": 70016,
                "name": "Witchmist Grove Cave",
                "desc": "A damp, mossy cave system connected to or near Witchmist Grove, likely sharing its magical and dangerous nature, possibly extending the spriggan or hagraven territory.",
                "travel_desc": "Damp, mossy cave system near Witchmist Grove.",
                "tags": ["structure_type_natural_cave_damp_mossy", "monster_den_spriggan_potential_witchmist_connection", "specific_landmark_type_hagraven_coven_lair_potential_extension_witchmist", "dungeon_minor", "terrain_hot_springs_nearby_witchmist_grove", "magical_properties_enchanted_neutral_nature_magic", "alchemy_ingredient_source_rich_potential_cave_flora"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 70017,
                "name": "Dunmer Refugee Camp (Eastmarch)",
                "desc": "A small, struggling camp of Dunmer refugees who have fled Morrowind, located in a less hospitable part of Eastmarch, seeking safety but finding hardship.",
                "travel_desc": "Small, struggling camp of Dunmer refugees.",
                "tags": ["populated_village_makeshift_refugee_camp", "settlement_minor_refugee_dunmer", "dunmer_culture_local_displaced", "social_issue_poverty_displacement_hardship", "terrain_volcanic_tundra_edge_eastmarch", "state_or_condition_current_struggling_seeking_safety", "morrowind_border_region_refugees"],
                "exit_label_from_parent": "Path to Camp",
                "exit_label_to_parent": "Leave Camp Area"
            },
            {
                "id": 70018,
                "name": "Ashfall Farm",
                "desc": "A small, struggling farm in the volcanic tundra of Eastmarch, where hardy Nords attempt to grow crops despite the harsh ashfall and geothermal activity.",
                "travel_desc": "Small, struggling farm in volcanic tundra.",
                "tags": ["structure_type_farmstead_struggling", "economic_activity_farming_crops_struggling_hardy_crops", "terrain_volcanic_tundra_ashfall_zone", "climate_harsh_volcanic_geothermal", "settlement_minor", "state_or_condition_current_struggling_resilient_farmers"],
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 70019,
                "name": "Boiling Springs Camp",
                "desc": "A tiny settlement of hunters and trappers who have made their camp near Eastmarch's famous hot springs, utilizing the warm waters and local game.",
                "travel_desc": "Tiny settlement of hunters near hot springs.",
                "tags": ["populated_village_makeshift_camp", "settlement_minor_hunter_trapper", "economic_activity_hunting_furs_meat", "terrain_hot_springs_eastmarch", "resource_node_game_geothermal_warmth", "climate_subarctic_volcanic", "unique_lifestyle_hot_springs_campers"],
                "exit_label_from_parent": "Path to Camp",
                "exit_label_to_parent": "Leave Camp Area"
            },
            {
                "id": 70020,
                "name": "Sulfur-Spring Grotto",
                "desc": "A small cave system near Eastmarch's volcanic hot springs, filled with sulfurous fumes and often home to creatures adapted to the heat, or desperate outcasts.",
                "travel_desc": "Small cave system near hot springs, filled with sulfurous fumes.",
                "tags": ["structure_type_natural_cave_grotto", "terrain_hot_springs_volcanic_sulfurous", "monster_den_fire_atronach_potential_heat_adapted_creatures", "alchemy_ingredient_source_rich_sulfur_minerals", "dangerous_environment_fumes_heat", "dungeon_minor", "climate_subarctic_volcanic", "exploration_point_geothermal_cave"],
                "exit_label_from_parent": "Grotto Entrance",
                "exit_label_to_parent": "Exit Grotto"
            },
            {
                "id": 70021,
                "name": "Ruins of Old Amol",
                "desc": "The scattered, ancient foundations and a few crumbling walls of a settlement that predated Fort Amol, now mostly reclaimed by the volcanic tundra.",
                "travel_desc": "Scattered ancient foundations of a pre-Fort Amol settlement.",
                "tags": ["structure_type_ruined_settlement_nordic_ancient", "cultural_historical_significance_nordic_ancient_site_minor_pre_amol", "structure_condition_ruined_extensively_reclaimed_by_tundra", "terrain_volcanic_tundra", "exploration_point_historic_foundations", "archaeology_site_potential_early_nordic"],
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 70022,
                "name": "Shrine of Mara (Eastmarch Hot Springs)",
                "desc": "A small, secluded shrine to Mara, Goddess of Love, nestled among the steaming vents and warm pools of Eastmarch's hot springs. A place of unexpected serenity.",
                "travel_desc": "Secluded shrine to Mara among hot springs.",
                "tags": ["structure_type_shrine_outdoor_structure_secluded", "religious_site_aedric", "mara_shrine", "terrain_hot_springs_eastmarch", "secluded_nature_spot_serene", "magical_properties_holy_ground_aedric_potential", "peaceful_area_unexpected_serenity", "exploration_point_religious_hidden"],
                "exit_label_from_parent": "Path to Shrine",
                "exit_label_to_parent": "Leave Shrine Area"
            },
            {
                "id": 70023,
                "name": "Shrine of Malacath (Narzulbur Outskirts)",
                "desc": "A crude, outdoor shrine dedicated to Malacath, located a short distance from the Orc stronghold of Narzulbur. Used by Orcs for private offerings or rituals.",
                "travel_desc": "Crude outdoor shrine to Malacath near Narzulbur.",
                "tags": ["structure_type_shrine_outdoor_structure_crude_orcish", "religious_site_daedric_orcish_malacath", "malacath_shrine", "orc_culture_strong", "ritual_site_tribal_potential_offerings", "narzulbur_outskirts", "cultural_historical_significance_orc_tradition_worship"],
                "exit_label_from_parent": "Path to Shrine",
                "exit_label_to_parent": "Leave Shrine Area"
            },
            {
                "id": 70024,
                "name": "Riverside Shack (Eastmarch Volcanic Plains)",
                "desc": "An isolated, ramshackle hut on the banks of a river cutting through Eastmarch's volcanic plains. Could be home to a reclusive fisherman or a desperate outcast.",
                "travel_desc": "Isolated, ramshackle hut on river banks.",
                "tags": ["structure_type_shack_or_hut_ramshackle", "terrain_volcanic_tundra_river_bank", "hermit_lair_potential_fisherman_outcast", "economic_activity_fishing_subsistence_potential", "isolated_location", "climate_subarctic_volcanic", "exploration_point_minor_dwelling_isolated"],
                "exit_label_from_parent": "Path to Shack",
                "exit_label_to_parent": "Leave Shack Area"
            },
            {
                "id": 70025,
                "name": "Volcanic Vent Cave",
                "desc": "A small cave system formed near an active volcanic vent, filled with heated air and strange mineral deposits. May be home to fire atronachs or other heat-adapted creatures.",
                "travel_desc": "Small cave system near an active volcanic vent.",
                "tags": ["structure_type_natural_cave_volcanic_vent", "terrain_volcanic_tundra_vent_active", "monster_den_fire_atronach_potential_heat_adapted", "alchemy_ingredient_source_rich_minerals_volcanic", "dangerous_environment_heat_fumes", "dungeon_minor", "climate_subarctic_volcanic", "unique_natural_formation_geothermal_cave"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 70026,
                "name": "The Atronach Stone",
                "desc": "A Standing Stone located in the volcanic tundra of Eastmarch, south of Windhelm. It grants a larger pool of magicka but hinders natural regeneration, forcing reliance on absorption or potions.",
                "travel_desc": "Standing Stone granting larger magicka pool but hindering regeneration.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_powerful_double_edged", "terrain_volcanic_tundra_south_windhelm", "cultural_historical_significance_ancient_magical_site", "buff_magicka_increased_large", "debuff_magicka_regen_slowed_significantly", "power_magic_absorption_passive"],
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 70027,
                "name": "Kagrenzel",
                "desc": "A remote Dwemer ruin in the mountains of Eastmarch, known for its peculiar entrance trap that drops explorers into a deep chasm leading to a Falmer-infested cave system.",
                "travel_desc": "Remote Dwemer ruin with a peculiar entrance trap.",
                "tags": ["dwemer_ruin_minor_outpost_remote", "dungeon_major_trap_complex_deadly_entrance", "falmer_presence_strong_connected_cave_system", "ancient_technology_dwemer_trap_peculiar", "terrain_mountainous_eastmarch_velothi_border", "chaurus_nest_potential_deep_within", "cultural_historical_significance_dwemer_ruin_site", "exploration_challenge_deadly_trap_puzzle"],
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 70028,
                "name": "Mistwatch",
                "desc": "A ruined fort in southern Eastmarch, overlooking the road to The Rift. It is currently occupied by a band of bandits led by a charismatic chief, and is connected to a local family's tragedy.",
                "travel_desc": "Ruined fort occupied by bandits, connected to a local tragedy.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold_charismatic_leader", "dungeon_major", "quest_location_local_legend_rescue_family_tragedy", "terrain_rift_border_overlook_eastmarch", "state_or_condition_current_bandit_controlled_area", "strategic_lookout_decayed_fort"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 70029,
                "name": "Mara's Eye Pond",
                "desc": "A small, tranquil pond in Eastmarch, west of Morvunskar. Beneath its surface lies the entrance to Mara's Eye Den, a cave often used by vampires or other creatures.",
                "travel_desc": "Small, tranquil pond with a hidden cave entrance beneath.",
                "tags": ["unique_natural_formation_pond_tranquil_surface", "dungeon_access_hidden_underwater_mara_eye_den", "specific_landmark_type_vampire_coven_minor_potential_den", "terrain_volcanic_tundra_edge_west_morvunskar", "mystery_local_hidden_lair", "secluded_nature_spot_deceptive_danger_below"],
                "exit_label_from_parent": "Path to Pond",
                "exit_label_to_parent": "Leave Pond Area",
                "sub_locations": [
                    {
                        "id": 700291,
                        "name": "Mara's Eye Den",
                        "desc": "A damp cave system accessible from Mara's Eye Pond, often serving as a den for vampires or other creatures seeking a hidden lair.",
                        "travel_desc": "Damp cave system, often a den for vampires.",
                        "tags": ["structure_type_natural_cave", "specific_landmark_type_vampire_coven_minor", "dungeon_minor", "monster_den_vampire", "magical_properties_tainted_by_dark_magic_potential", "secret_location_underwater_access"],
                        "exit_label_from_parent": "Den Entrance",
                        "exit_label_to_parent": "Exit Den"
                    }
                ]
            },
            {
                "id": 70030,
                "name": "Abandoned Prison",
                "desc": "A crumbling, forgotten prison in the wilds of Eastmarch, its cells now empty or home to desperate squatters, bandits, or restless spirits of former inmates.",
                "travel_desc": "Crumbling, forgotten prison in the wilds.",
                "tags": ["structure_type_ruined_prison_forgotten", "structure_condition_abandoned_ruined_crumbling", "dungeon_minor", "bandit_minor_camp_potential_squatters", "magical_properties_haunted_aura_potential_former_inmates", "cultural_historical_significance_historic_site_abandoned_prison", "urban_issues_or_atmosphere_eerie_atmosphere_despair", "exploration_point_historic_ruin_dark_past"],
                "exit_label_from_parent": "Path to Prison",
                "exit_label_to_parent": "Leave Prison Area"
            }
        ]
    }
]