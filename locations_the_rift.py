from locations_riften_city import RIFTEN_CITY_LOCATIONS

THE_RIFT_LOCATIONS = [
    # THE RIFT
    {
        "id": 9,
        "name": "The Rift",
        "desc": "A temperate, autumnal hold in southeastern Skyrim, known for its golden forests, numerous lakes, and the city of Riften, a haven for the Thieves Guild and rife with corruption. It borders Morrowind and Cyrodiil.",
        "travel_desc": "Temperate, autumnal hold with golden forests and numerous lakes.",
        "tags": ["hold", "terrain_forest_autumnal_large_golden_woods", "terrain_lake_region_abundant_honrich_geir", "faction_thieves_guild_presence_strong_hq_riften", "nordic_culture_local_rift_traditions", "morrowind_border_region_velothi_mountains", "cyrodiil_border_region_jerall_mountains", "urban_issues_or_atmosphere_corrupt_underbelly_pervasive", "political_influence_black_briar_family_dominance_maven", "climate_temperate_continental", "beautiful_scenery_autumnal_lakes", "economic_activity_brewing_mead_ale_black_briar_honningbrew_rivalry_potential", "economic_activity_fishing_industry_local_lakes"],
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
                "exit_label_from_parent": "Path to Village",
                "exit_label_to_parent": "Leave Village",
                "sub_locations": [
                    {
                        "id": 9101,
                        "name": "Redbelly Mine",
                        "desc": "The ebony mine that is the main source of livelihood for Shor's Stone, currently unsafe due to spider infestation.",
                        "travel_desc": "Ebony mine, currently unsafe due to spiders.",
                        "tags": ["structure_type_mine_active_infested", "economic_activity_mining_ebony", "resource_node_ebony_dangerous", "monster_infestation_spider_major", "quest_location_clear_mine_shors_stone", "dungeon_minor_mine_infested"],
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    },
                    {
                        "id": 9102,
                        "name": "Sylgja's House",
                        "desc": "The home of Sylgja, a miner in Shor's Stone, whose father works in Darkwater Crossing.",
                        "travel_desc": "Home of Sylgja, a miner in Shor's Stone.",
                        "tags": ["structure_type_residence", "commoner_dwelling_miner", "quest_giver_potential_family_related"],
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    },
                    {
                        "id": 9103,
                        "name": "Filnjar's House and Smithy",
                        "desc": "The home and modest smithy of Filnjar, the blacksmith of Shor's Stone.",
                        "travel_desc": "Home and smithy of Filnjar, blacksmith of Shor's Stone.",
                        "tags": ["structure_type_residence", "structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor_potential", "item_type_armor_vendor_potential"],
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
                "exit_label_from_parent": "Path to Village",
                "exit_label_to_parent": "Leave Village",
                "sub_locations": [
                    {
                        "id": 9201,
                        "name": "Vilemyr Inn",
                        "desc": "The only inn in the quiet village of Ivarstead, nestled at the foot of the 7,000 Steps. Run by the aging but kind Wilhelm, it's a common resting place for pilgrims heading to High Hrothgar. Wilhelm is often worried about the nearby Shroud Hearth Barrow and the strange noises emanating from it. The inn has a warm fire and a few regulars, but it's not as boisterous as taverns in larger cities.",
                        "travel_desc": "Ivarstead's inn, run by Wilhelm, a stop for High Hrothgar pilgrims.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source", "quest_giver_potential_barrow_investigation_wilhelm", "location_specific_vilemyr_inn"],
                        "context_tags": ["interior", "village_type", "tavern_type", "safe_zone"], # Added context_tags
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
                        "exit_label_from_parent": "Barrow Entrance",
                        "exit_label_to_parent": "Exit Barrow"
                    },
                    {
                        "id": 9203,
                        "name": "Klimmek's House",
                        "desc": "The home of Klimmek, a resident of Ivarstead who makes regular supply deliveries to High Hrothgar for the Greybeards.",
                        "travel_desc": "Home of Klimmek, makes deliveries to High Hrothgar.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "quest_giver_potential_high_hrothgar_delivery", "greybeards_related_supplier"],
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    },
                    {
                        "id": 9204,
                        "name": "Narfi's Wrecked House",
                        "desc": "The ruined and isolated house of Narfi, a distraught beggar living across the river from Ivarstead, searching for his missing sister.",
                        "travel_desc": "Ruined house of Narfi, a distraught beggar.",
                        "tags": ["structure_type_ruined_shack", "structure_condition_collapsed", "hermit_lair_beggar", "quest_location_dark_brotherhood_target_potential", "social_issue_poverty_grief", "isolated_location_river_other_side"],
                        "exit_label_from_parent": "Path to Ruin",
                        "exit_label_to_parent": "Leave Ruin"
                    }
                ]
            },
            {
                "id": 93,
                "name": "Lost Prospect Mine",
                "desc": "An abandoned gold mine in the Rift, often occupied by bandits. It is rumored to be played out, but some say a few veins might remain for the determined.",
                "travel_desc": "Abandoned gold mine, often occupied by bandits.",
                "tags": ["structure_type_mine_abandoned", "economic_activity_mining_gold_historic", "resource_node_gold_rumored_depleted", "bandit_minor_camp_potential", "dungeon_minor", "exploration_challenge_potential_reward", "terrain_eastern_rift_mountains"],
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 94,
                "name": "Broken Helm Hollow",
                "desc": "A secluded cave system east of Riften, serving as a well-established bandit hideout with multiple chambers.",
                "travel_desc": "Secluded cave system, well-established bandit hideout.",
                "tags": ["structure_type_natural_cave", "bandit_main_stronghold", "dungeon_major_multi_level", "state_or_condition_current_bandit_controlled_area", "terrain_eastern_rift_forest", "quest_location_bounty_potential"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 95,
                "name": "Avanchnzel",
                "desc": "A large and dangerous Dwemer ruin in the southern mountains of the Rift. It contains ancient technology, Falmer, and is the focus of a quest to retrieve a unique Dwemer lexicon for From-Deepest-Fathoms.",
                "travel_desc": "Large, dangerous Dwemer ruin with ancient technology.",
                "tags": ["dwemer_ruin_major_city", "dungeon_large_complex", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "quest_location_unique_artifact_dwemer_lexicon", "ancient_technology_dwemer", "cultural_historical_significance_dwemer_ruin_site", "terrain_southern_rift_mountains", "chaurus_nest_potential"],
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 96,
                "name": "Boulderfall Cave",
                "desc": "A cave in the eastern Rift, often inhabited by necromancers or other dark mages who use its seclusion for their sinister experiments.",
                "travel_desc": "Cave often inhabited by necromancers.",
                "tags": ["structure_type_natural_cave", "specific_landmark_type_necromancer_lair", "magical_properties_tainted_by_dark_magic", "dungeon_minor", "undead_presence_skeletons_experiments", "ritual_site_dark_magic", "terrain_eastern_rift_wilderness"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 97,
                "name": "Clearspring Tarn",
                "desc": "A small, picturesque tarn and cave system west of Shor's Stone, often home to trolls guarding a treasure hunter's remains and note.",
                "travel_desc": "Picturesque tarn and cave system, often home to trolls.",
                "tags": ["structure_type_natural_cave_tarn", "monster_den_troll_guardian", "unique_natural_formation_tarn", "treasure_cache_minor_hunter_remains", "dungeon_minor", "secluded_nature_spot", "alchemy_ingredient_source_rich_potential"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 98,
                "name": "Crystaldrift Cave",
                "desc": "A small ice cave south of Riften, notable for its unique crystal formations. It is sometimes a den for frost creatures or a reclusive hermit.",
                "travel_desc": "Small ice cave notable for unique crystal formations.",
                "tags": ["structure_type_natural_cave_ice", "unique_natural_formation_crystal_cave", "monster_den_frost_creatures_potential", "hermit_lair_potential", "dungeon_minor", "climate_cold_cave", "alchemy_ingredient_source_rich_crystals_potential"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 99,
                "name": "Darklight Tower",
                "desc": "A ruined tower southwest of Riften, now a den for hagravens and the site of a Daedric quest where Illia attempts to stop her mother from becoming a hagraven.",
                "travel_desc": "Ruined tower, den for hagravens and site of Daedric quest.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main", "magical_properties_tainted_by_dark_magic", "dungeon_major_vertical", "quest_location_daedric_related_illia", "monster_den_hagraven_powerful", "witch_coven_powerful", "terrain_southern_rift_mountains"],
                "exit_label_from_parent": "Tower Entrance",
                "exit_label_to_parent": "Exit Tower"
            },
            {
                "id": 90001,
                "name": "Faldar's Tooth",
                "desc": "A ruined fort west of Riften, initially overrun by wolves, but later becomes a hideout for bandits or the Silver Hand, depending on unfolding events.",
                "travel_desc": "Ruined fort, initially overrun by wolves.",
                "tags": ["structure_type_ruined_fort", "dungeon_major_contested", "monster_den_wolf_initial_large", "bandit_main_stronghold_potential", "specific_landmark_type_silver_hand_hq_potential", "strategic_location_west_riften", "state_or_condition_current_dynamic_occupancy"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 90002,
                "name": "Fort Greenwall",
                "desc": "A large fort in the eastern Rift, strategically important. Currently garrisoned by Imperial soldiers, but its control is tenuous given the Rift's leanings.",
                "travel_desc": "Large, strategically important fort garrisoned by Imperials.",
                "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion", "dungeon_major_potential_if_contested", "strategic_location_eastern_rift_border", "civil_war_quest_historic_site_potential", "state_or_condition_current_contested_by_factions_potential_stormcloak"],
                "exit_label_from_parent": "Fort Gates",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 90003,
                "name": "Froki's Shack",
                "desc": "The isolated shack of Froki Whetted-Blade, an old hunter and devout follower of Kyne, located in the southern mountains of the Rift. He offers tasks related to Kyne's sacred trials.",
                "travel_desc": "Isolated shack of Froki, old hunter and follower of Kyne.",
                "tags": ["structure_type_shack_or_hut", "hermit_lair_hunter_devout", "quest_location_kyne_sacred_trials", "religious_site_aedric_kyne_shrine_nearby", "animal_lore_expert", "isolated_location_mountain", "skill_trainer_archery_potential"],
                "exit_label_from_parent": "Path to Shack",
                "exit_label_to_parent": "Leave Shack Area"
            },
            {
                "id": 90004,
                "name": "Goldenglow Estate",
                "desc": "A large honey farm and apiary on an island in Lake Honrich, owned by Aringoth. It's a major supplier of honey for the Black-Briar Meadery and becomes a key target in a Thieves Guild questline.",
                "travel_desc": "Large honey farm and apiary on an island.",
                "tags": ["structure_type_farmstead_apiary_large", "terrain_island_lake_honrich", "quest_location_thieves_guild_major_sabotage", "economic_activity_brewing_mead_ale_supplier_black_briar", "structure_condition_wealthy_estate_guarded", "faction_thieves_guild_target", "unique_produce_honey_goldenglow"],
                "exit_label_from_parent": "Path to Estate",
                "exit_label_to_parent": "Leave Estate"
            },
            {
                "id": 90005,
                "name": "Heartwood Mill",
                "desc": "A lumber mill on the shores of Lake Honrich, run by Grosta. A peaceful location providing wood for Riften.",
                "travel_desc": "Lumber mill on Lake Honrich, run by Grosta.",
                "tags": ["structure_type_lumber_mill_site", "settlement_minor", "economic_activity_logging_timber", "terrain_lake_honrich_shoreline", "peaceful_area", "resource_node_wood"],
                "exit_label_from_parent": "Path to Mill",
                "exit_label_to_parent": "Leave Mill"
            },
            {
                "id": 90006,
                "name": "Honeystrand Cave",
                "desc": "A small cave south of Ivarstead, often a den for bears or other local wildlife.",
                "travel_desc": "Small cave, often a den for bears.",
                "tags": ["structure_type_natural_cave", "monster_den_bear_common", "dungeon_minor", "terrain_southern_rift_forest", "alchemy_ingredient_source_rich_potential_animal_parts"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 90007,
                "name": "Last Vigil",
                "desc": "A ruined watchtower and ancient dragon burial site high in the mountains of the Rift. While no dragons stir now, it's a place of potent old magic and may attract those interested in such power (like ancient vampire cults or dragon scholars).",
                "travel_desc": "Ruined watchtower and ancient dragon burial site.",
                "tags": ["structure_type_ruined_tower", "dragon_lore_ancient_site_burial", "magical_properties_arcane_nexus_ancient", "terrain_mountain_peak_remote", "specific_landmark_type_vampire_coven_minor_potential_interest", "scholar_retreat_rumor_dragon_lore", "dungeon_minor", "cultural_historical_significance_dragon_cult_site_potential"],
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 90008,
                "name": "Merryfair Farm",
                "desc": "A farmstead located near Riften, owned by Dravin Llanith, who is often worried about his stolen bow.",
                "travel_desc": "Farmstead near Riften, owned by Dravin Llanith.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "quest_giver_potential_stolen_item", "riften_outskirts", "settlement_minor"],
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 90009,
                "name": "Nightingale Hall",
                "desc": "The secret sanctuary and headquarters of the Nightingales, protectors of Nocturnal's shrine, hidden within a cave system in the Rift. Its existence is known only to the highest echelons of the Thieves Guild.",
                "travel_desc": "Secret sanctuary and HQ of the Nightingales.",
                "tags": ["structure_type_secret_sanctuary_cave", "faction_nightingales_hq", "religious_site_daedric_nocturnal_shrine", "thieves_guild_elite_order_related", "dungeon_major_quest_specific", "magical_properties_daedric_influence_overt_nocturnal", "secret_location_guild_elite_only", "artifact_location_nightingale_armor_weapons"],
                "exit_label_from_parent": "Secret Entrance",
                "exit_label_to_parent": "Exit Hall"
            },
            {
                "id": 90010,
                "name": "Nilheim",
                "desc": "A ruined watchtower east of Ivarstead, occupied by bandits who employ a clever ambush by pretending to be legitimate guards.",
                "travel_desc": "Ruined watchtower occupied by bandits using an ambush tactic.",
                "tags": ["structure_type_ruined_tower", "bandit_minor_camp_deceptive_ambush", "dungeon_minor", "roadside_danger_spot", "quest_location_minor_investigation_potential", "terrain_eastern_rift_roadside"],
                "exit_label_from_parent": "Path to Tower",
                "exit_label_to_parent": "Leave Tower Area"
            },
            {
                "id": 90011,
                "name": "Northwind Summit",
                "desc": "A mountain peak in the northern Rift, near Shor's Stone, known as an ancient dragon lair and the site of a Word Wall.",
                "travel_desc": "Mountain peak, ancient dragon lair and Word Wall site.",
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "terrain_mountain_peak_high", "dungeon_minor_lair_potential", "cultural_historical_significance_dragon_lore_site_ancient", "undead_presence_draugr_potential"],
                "exit_label_from_parent": "Path to Summit",
                "exit_label_to_parent": "Leave Summit Area"
            },
            {
                "id": 90012,
                "name": "Pinepeak Cavern",
                "desc": "A cave system near Ivarstead, often inhabited by bears or other forest creatures.",
                "travel_desc": "Cave system near Ivarstead, often inhabited by bears.",
                "tags": ["structure_type_natural_cave", "monster_den_bear_common", "dungeon_minor", "terrain_forest_ivarstead_nearby", "alchemy_ingredient_source_rich_potential_animal_parts"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 90013,
                "name": "Redwater Den",
                "desc": "A rundown shack that serves as a front for a clandestine skooma operation, possibly with ties to a darker, more sinister group dealing in a particularly potent brew.",
                "travel_desc": "Rundown shack, front for a skooma operation.",
                "tags": ["structure_type_shack_or_hut_front", "economic_activity_skooma_production_distribution_hidden", "dungeon_major_underground_complex", "specific_landmark_type_vampire_coven_minor_potential_skooma_blood", "criminal_hideout_network_skooma", "magical_properties_tainted_by_dark_magic_potential", "quest_location_dawnguard_potential_alt"],
                "exit_label_from_parent": "Shack Door",
                "exit_label_to_parent": "Exit Shack"
            },
            {
                "id": 90014,
                "name": "Sarethi Farm",
                "desc": "A farmstead near Ivarstead, run by Avrusa Sarethi, an alchemist known for successfully cultivating Nirnroot.",
                "travel_desc": "Farmstead run by Avrusa Sarethi, known for Nirnroot.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_alchemy", "alchemy_ingredient_source_rich_nirnroot_cultivated", "quest_giver_potential_alchemy_research", "settlement_minor", "dunmer_culture_local_farmer_alchemist"],
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 90015,
                "name": "Snapleg Cave",
                "desc": "A cave system south of Ivarstead, often home to spriggans, witches, or hagravens drawn to its primal energies.",
                "travel_desc": "Cave system, home to spriggans, witches, or hagravens.",
                "tags": ["structure_type_natural_cave", "magical_properties_enchanted_primal", "monster_den_spriggan_strong", "specific_landmark_type_hagraven_coven_lair_potential", "witch_coven_potential", "dungeon_minor", "ritual_site_nature_magic_potential", "terrain_southern_rift_forest"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 90016,
                "name": "Snow-Shod Farm",
                "desc": "A farmstead near Riften, owned by the influential Snow-Shod family, who are staunch supporters of Ulfric Stormcloak.",
                "travel_desc": "Farmstead owned by the influential Snow-Shod family.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_livestock", "political_influence_stormcloak_family_snow_shod", "riften_outskirts", "settlement_minor", "nordic_culture_strong"],
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 90017,
                "name": "Stendarr's Beacon",
                "desc": "A ruined watchtower in the eastern Rift, now maintained by the Vigilants of Stendarr as an outpost in their crusade against Daedra, vampires, and other abominations.",
                "travel_desc": "Ruined watchtower, now a Vigilant of Stendarr outpost.",
                "tags": ["structure_type_ruined_tower_repurposed", "faction_vigilants_of_stendarr_outpost", "religious_military_order_anti_daedra", "dungeon_minor_fortified", "quest_location_vigilant_tasks_potential", "terrain_eastern_rift_mountains", "state_or_condition_current_vigilant_controlled_area"],
                "exit_label_from_parent": "Path to Beacon",
                "exit_label_to_parent": "Leave Beacon Area"
            },
            {
                "id": 90018,
                "name": "Treva's Watch",
                "desc": "A ruined fort west of Ivarstead, taken over by bandits. Stalleo, a Nord whose family was driven out, seeks help to reclaim it.",
                "travel_desc": "Ruined fort taken over by bandits.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold", "dungeon_major", "quest_location_reclaim_fort_family", "state_or_condition_current_bandit_controlled_area", "terrain_western_rift_river"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 90019,
                "name": "Tolvald's Cave",
                "desc": "A very large and dangerous cave system in the Velothi Mountains on the border with Morrowind, infested with Falmer, Chaurus, and possibly other deep-dwelling horrors.",
                "travel_desc": "Large, dangerous cave system infested with Falmer and Chaurus.",
                "tags": ["structure_type_natural_cave_large_complex", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_large_complex_dangerous", "morrowind_border_region_velothi_mountains", "exploration_challenge_deadly", "state_or_condition_current_lawless_area", "quest_location_investigation_rumor_potential"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 90020,
                "name": "Autumnwatch Tower",
                "desc": "A pair of ruined Nordic towers overlooking the golden forests of the Rift, often used as a lair by dragons in ages past, now possibly home to Forsworn or bandits.",
                "travel_desc": "Ruined Nordic towers overlooking golden forests.",
                "tags": ["structure_type_ruined_tower_nordic_pair", "scenic_vista_panoramic_autumnal_forest", "dragon_lore_ancient_site_lair_rumor", "forsworn_presence_potential_outpost", "bandit_minor_camp_potential", "dungeon_minor", "terrain_rift_forest_overlook"],
                "exit_label_from_parent": "Path to Towers",
                "exit_label_to_parent": "Leave Towers Area"
            },
            {
                "id": 90021,
                "name": "Black-Briar Lodge",
                "desc": "A secluded hunting lodge owned by the Black-Briar family, located northeast of Riften. Used for private gatherings and potentially illicit dealings.",
                "travel_desc": "Secluded hunting lodge owned by the Black-Briar family.",
                "tags": ["structure_type_lodge_private_elite", "political_influence_black_briar_family_retreat", "secret_location_illicit_dealings_potential", "structure_condition_well_guarded", "terrain_rift_forest_secluded", "quest_location_thieves_guild_intrigue_potential"],
                "exit_label_from_parent": "Path to Lodge",
                "exit_label_to_parent": "Leave Lodge Area"
            },
            {
                "id": 90022,
                "name": "Forelhost",
                "desc": "A massive, ancient Nordic monastery fortress on a mountaintop in The Rift, the last stronghold of the Dragon Cult. It is now sealed and haunted by its former Dragon Priest Rahgot and his draugr followers.",
                "travel_desc": "Massive Nordic fortress, last stronghold of Dragon Cult.",
                "tags": ["nordic_burial_site_major_fortress", "cultural_historical_significance_dragon_cult_lair_priest_rahgot", "undead_presence_strong_powerful_draugr", "dungeon_large_complex_mountain_top", "artifact_location_powerful_mask", "structure_condition_sealed_ruin_dangerous", "quest_location_dragon_priest_mask", "terrain_mountain_peak_rift"],
                "demographics": {"Draugr": 85, "Frost Trolls (exterior)": 10, "Dragon Priest": 1},
                "travel": { "links": [{"name": "The Rift plains", "connection_type": "Treacherous mountain path"}] },
                "exit_label_from_parent": "Path to Fortress",
                "exit_label_to_parent": "Leave Fortress Area"
            },
            {
                "id": 90023,
                "name": "Giant's Grove",
                "desc": "A small, hidden grove within the Rift's forests, where a reclusive giant tends to a painted cow. A place of unusual peace.",
                "travel_desc": "Hidden grove where a giant tends a painted cow.",
                "tags": ["unique_natural_formation_hidden_grove", "neutral_encounter_giant_painted_cow", "cultural_historical_significance_local_legend_folk_tale", "secluded_nature_spot", "peaceful_area", "terrain_rift_forest_hidden"],
                "exit_label_from_parent": "Path to Grove",
                "exit_label_to_parent": "Leave Grove"
            },
            {
                "id": 90024,
                "name": "Ruunvald Excavation",
                "desc": "An archaeological dig site in the eastern mountains of the Rift, where Vigilants of Stendarr were investigating ancient ruins before something went terribly wrong. Now a place of danger and dark influence.",
                "travel_desc": "Archaeological dig site, now a place of danger.",
                "tags": ["structure_type_excavation_site_ruined", "faction_vigilants_of_stendarr_tragedy_site", "magical_properties_tainted_by_dark_magic_influence", "dungeon_major_dangerous_investigation", "undead_presence_strong_potential_vigilants_or_other", "quest_location_dawnguard_potential_alt", "terrain_eastern_rift_mountains"],
                "exit_label_from_parent": "Path to Excavation",
                "exit_label_to_parent": "Leave Excavation Site"
            },
            {
                "id": 90025,
                "name": "Lakeside Landing",
                "desc": "A small community of fisherfolk and boatwrights on the shores of Lake Honrich in The Rift, known for their sturdy fishing boats and tales of the lake's depths.",
                "travel_desc": "Small community of fisherfolk and boatwrights.",
                "tags": ["populated_village", "settlement_minor_fishing_boatwright", "economic_activity_fishing_industry_local", "economic_activity_crafting_boatbuilding", "terrain_lake_honrich_shoreline", "rumor_source_local_legends_lake_monsters"],
                "exit_label_from_parent": "Path to Landing",
                "exit_label_to_parent": "Leave Landing"
            },
            {
                "id": 90026,
                "name": "Goldenleaf Farmstead",
                "desc": "A picturesque farm in The Rift, renowned for its vibrant autumn foliage and the sweet, crisp apples grown in its orchards.",
                "travel_desc": "Picturesque farm renowned for vibrant autumn foliage.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_orchard_apples", "unique_produce_goldenleaf_apples", "terrain_rift_forest_autumnal", "scenic_vista_picturesque", "settlement_minor", "peaceful_area"],
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 90027,
                "name": "Tanglewood Den",
                "desc": "A dense, overgrown cave system hidden deep within the autumnal forests of The Rift, often serving as a den for bears, spriggans, or a reclusive alchemist.",
                "travel_desc": "Dense, overgrown cave system, den for bears or spriggans.",
                "tags": ["structure_type_natural_cave_overgrown", "dungeon_minor", "monster_den_bear_potential", "monster_den_spriggan_potential", "hermit_lair_potential_alchemist", "terrain_rift_forest_deep", "alchemy_ingredient_source_rich_potential"],
                "exit_label_from_parent": "Den Entrance",
                "exit_label_to_parent": "Exit Den"
            },
            {
                "id": 90028,
                "name": "Ruins of Autumn's End",
                "desc": "The crumbling remains of an old hunting lodge or minor keep in The Rift, now reclaimed by the forest. It might hold forgotten treasures or be used by local bandits.",
                "travel_desc": "Crumbling remains of an old hunting lodge or keep.",
                "tags": ["structure_type_ruined_lodge_keep", "cultural_historical_significance_historic_site_minor", "treasure_cache_rumored_minor", "bandit_minor_camp_potential", "dungeon_minor", "terrain_rift_forest_reclaimed", "structure_condition_ruined_extensively"],
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 90029,
                "name": "Shrine of Zenithar (Rift Forest)",
                "desc": "An outdoor shrine dedicated to Zenithar, the Divine of Work and Commerce, located along an old trade path in the Rift's forests. Merchants and craftsmen sometimes leave offerings here for prosperity.",
                "travel_desc": "Outdoor shrine to Zenithar on an old trade path.",
                "tags": ["structure_type_shrine_outdoor_structure", "religious_site_aedric", "zenithar_shrine", "economic_activity_trade_route_shrine", "magical_properties_holy_ground_aedric_potential", "terrain_rift_forest_trade_path", "cultural_historical_significance_trade_god_worship"],
                "exit_label_from_parent": "Path to Shrine",
                "exit_label_to_parent": "Leave Shrine Area"
            },
            {
                "id": 90030,
                "name": "Angarvunde",
                "desc": "An ancient and extensive Nordic ruin in the mountains of the Rift, deeply buried and heavily guarded by draugr. It is known for a tragic tale of betrayal and a powerful artifact sought by some.",
                "travel_desc": "Ancient Nordic ruin, known for tragic tale and artifact.",
                "tags": ["nordic_burial_site_major", "dungeon_large_complex", "undead_presence_strong_powerful_draugr", "cultural_historical_significance_nordic_ancient_site_tragic_lore", "artifact_location_rumored_powerful", "specific_landmark_type_word_wall_location_potential", "quest_location_local_legend_investigation", "terrain_rift_mountains_buried"],
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 90031,
                "name": "The Shadow Stone",
                "desc": "A Standing Stone hidden in the forests south of Riften, near the traditional grounds of the Nightingales. It grants the power of invisibility for a short duration, once per day.",
                "travel_desc": "Standing Stone granting power of invisibility.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_stealth", "power_invisibility_temporary_daily", "terrain_rift_forest_hidden", "faction_nightingales_lore_associated_potential", "cultural_historical_significance_ancient_magical_site"],
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 90032,
                "name": "Ruins of Bthalft",
                "desc": "Crumbling Dwemer ruins in the southern Rift, notable for an outdoor Dwemer mechanism. Legends say it's an access point to deeper, hidden Dwemer workings and perhaps the legendary Aetherium Forge.",
                "travel_desc": "Crumbling Dwemer ruins with an outdoor mechanism.",
                "tags": ["dwemer_ruin_minor_outpost_outdoor", "ancient_technology_dwemer_mechanism_exterior", "quest_location_aetherium_forge_access_rumor", "falmer_presence_potential_nearby_ruins", "cultural_historical_significance_dwemer_ruin_site_aetherium", "terrain_southern_rift_ruins", "exploration_challenge_puzzle_potential"],
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 90033,
                "name": "Fallowstone Cave",
                "desc": "A large cave system in the northern Rift, near Shor's Stone. It is often a den for bears or trolls and is one of the sites for Kyne's Sacred Trials.",
                "travel_desc": "Large cave system, den for bears/trolls, site for Kyne's Trials.",
                "tags": ["structure_type_natural_cave_large", "monster_den_bear_troll_major", "quest_location_kyne_sacred_trials", "dungeon_major_natural", "terrain_northern_rift_wilderness", "hunting_ground_dangerous_sacred"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 90034,
                "name": "Lost Tongue Overlook",
                "desc": "A ruined Nordic watchtower and ancient dragon lair high in the mountains of The Rift, south of Riften. It contains a Word Wall and is often guarded by powerful draugr or other ancient entities.",
                "travel_desc": "Ruined Nordic watchtower and dragon lair with Word Wall.",
                "tags": ["structure_type_ruined_tower_nordic", "specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "dungeon_major", "undead_presence_strong_draugr_powerful", "terrain_mountain_peak_rift_overlook", "cultural_historical_significance_dragon_lore_site_ancient"],
                "exit_label_from_parent": "Path to Overlook",
                "exit_label_to_parent": "Leave Overlook"
            },
            {
                "id": 90035,
                "name": "Geirmund's Hall",
                "desc": "An ancient Nordic ruin on an island in Lake Geir, east of Ivarstead. It is the tomb of the archmage Geirmund and is guarded by draugr and a powerful necromancer.",
                "travel_desc": "Ancient Nordic ruin on an island, tomb of archmage Geirmund.",
                "tags": ["nordic_burial_site_major_island", "dungeon_major_tomb_archmage", "undead_presence_strong_draugr", "specific_landmark_type_necromancer_lair_guardian", "quest_location_artifact_gauldur_amulet_fragment", "cultural_historical_significance_legendary_hero_location_geirmund", "terrain_island_lake_geir", "artifact_location_powerful"],
                "exit_label_from_parent": "Hall Entrance",
                "exit_label_to_parent": "Exit Hall"
            }
        ]
    }
]