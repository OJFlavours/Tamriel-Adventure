from locations_solitude_city import SOLITUDE_CITY_LOCATIONS

HAAFINGAR_LOCATIONS = [
    # HAAFINGAR
    {
        "id": 8,
        "name": "Haafingar",
        "desc": "A strategic coastal hold in northwestern Skyrim, dominated by the majestic capital city of Solitude. It is the primary Imperial stronghold in Skyrim and a vital hub for maritime trade.",
        "travel_desc": "Strategic coastal hold, home to Solitude and Imperial stronghold.",
        "tags": ["hold", "environment_coastal_major_northwestern_skyrim", "imperial_influence_strong_primary_stronghold_skyrim", "economic_activity_trade_hub_major_maritime_tamriel_wide", "nordic_culture_imperialized_cosmopolitan", "city_affiliation_solitude_capital_skyrim", "settlement_features_bards_college_renowned", "thalmor_presence_strong_embassy_influence", "climate_temperate_coastal", "political_tension_high_imperial_stormcloak_capital_focus", "travel_hub_major_sea_land"],
        "density": "sparse",
        "demographics": {"Nord": 65, "Imperial": 25, "Breton": 5, "Others": 5},
        "travel": {
            "links": [
                {"name": "The Reach", "connection_type": "Road"},
                {"name": "Whiterun Hold", "connection_type": "Road"},
                {"name": "Hjaalmarch", "connection_type": "Road"},
                {"name": "Dragon Bridge Road", "connection_type": "Path"},
                {"name": "Coastal Sea Route (to other ports)", "connection_type": "Sea Route"},
                {"name": "Northwatch Keep Trail", "connection_type": "Path"}
            ]
        },
        "sub_locations": [
            {
                "id": 80,
                "name": "Solitude",
                "desc": "The grand capital of Skyrim under Imperial control, perched atop a natural stone arch overlooking the Karth River delta. It is home to High King Torygg in the Blue Palace, the Imperial Legion headquarters at Castle Dour, and the renowned Bards College.",
                "travel_desc": "Grand capital of Skyrim, perched atop a stone arch.",
                "tags": ["populated_city_capital_skyrim_grand", "imperial_influence_dominant_seat_of_power", "city_affiliation_haafingar_capital", "economic_activity_trade_hub_major_maritime", "settlement_features_bards_college", "settlement_features_docks_harbor_major", "architecture_grand_imperial_stone_arch", "political_tension_high_imperial_stormcloak_seat_of_power", "unique_landmark_iconic_arch_blue_palace_castle_dour", "structure_type_fortified_city_wall_impressive", "thalmor_presence_strong_embassy_office", "urban_issues_or_atmosphere_bustling_trade_atmosphere_political_intrigue"],
                "density": "bustling",
                "exit_label_from_parent": "City Gates",
                "exit_label_to_parent": "City Gates",
                "sub_locations": SOLITUDE_CITY_LOCATIONS
            },
            {
                "id": 81,
                "name": "Dragon Bridge",
                "desc": "A quaint village in northwestern Haafingar, built around an ancient and iconic stone bridge spanning the Karth River. It serves as a strategic crossing point and hosts an Imperial outpost.",
                "travel_desc": "Quaint village built around an ancient stone bridge.",
                "tags": ["populated_village", "settlement_minor_strategic", "structure_type_bridge_ancient_landmark", "strategic_location_river_crossing", "economic_activity_logging_timber_nearby", "military_presence_imperial_penitus_oculatus", "travel_hub_minor"],
                "density": "average",
                "exit_label_from_parent": "Road to Village",
                "exit_label_to_parent": "Leave Village",
                 "sub_locations": [
                    {
                        "id": 8101,
                        "name": "Four Shields Tavern",
                        "desc": "The inn at Dragon Bridge, a common stop for Imperial soldiers, Penitus Oculatus agents, and travelers on the road to Solitude or the Reach.",
                        "travel_desc": "Inn at Dragon Bridge, common stop for soldiers.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source_military_travelers"],
                        "density": "average",
                        "demographics": {"Nord": 60, "Imperial": 30, "Breton": 5, "Redguard": 5},
                        "exit_label_from_parent": "Tavern Door",
                        "exit_label_to_parent": "Exit Tavern"
                    },
                    {
                        "id": 8102,
                        "name": "Dragon Bridge Lumber Camp",
                        "desc": "The lumber mill that supports the village of Dragon Bridge, run by Horgeir.",
                        "travel_desc": "Lumber mill supporting Dragon Bridge.",
                        "tags": ["structure_type_lumber_mill_site", "economic_activity_logging_timber", "resource_node_wood"],
                        "density": "sparse",
                        "exit_label_from_parent": "Path to Mill",
                        "exit_label_to_parent": "Leave Mill"
                    },
                    {
                        "id": 8103,
                        "name": "Penitus Oculatus Outpost (Dragon Bridge)",
                        "desc": "A fortified Imperial outpost near Dragon Bridge, often used by the Penitus Oculatus for operations in Haafingar and the western holds.",
                        "travel_desc": "Fortified Imperial outpost near Dragon Bridge.",
                        "tags": ["structure_type_fortified_outpost", "military_presence_imperial_penitus_oculatus", "imperial_influence_strong_military_intelligence", "strategic_location_monitoring"],
                        "density": "sparse",
                        "exit_label_from_parent": "Outpost Gate",
                        "exit_label_to_parent": "Exit Outpost"
                    }
                ]
            },
            {
                "id": 82,
                "name": "Wolfskull Cave",
                "desc": "A dark, foreboding cave system high in the mountains of Haafingar. Necromancers are rumored to gather here, attempting rituals to resurrect the ancient Wolf Queen Potema.",
                "travel_desc": "Dark cave where necromancers attempt to resurrect Potema.",
                "tags": ["structure_type_natural_cave_large", "dungeon_major", "magical_properties_haunted_aura_strong", "specific_landmark_type_necromancer_ritual_site", "quest_location_potema_wolf_queen", "undead_presence_strong", "magical_properties_tainted_by_dark_magic", "terrain_mountainous_remote"],
                "density": "average",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 83,
                "name": "Fort Hraggstad",
                "desc": "An Imperial fort northwest of Solitude, guarding the coastline. It is currently garrisoned by Imperial soldiers, though its readiness might be tested by local banditry or rising Stormcloak sentiment elsewhere.",
                "travel_desc": "Imperial fort guarding the coastline.",
                "tags": ["structure_type_fortified_keep_coastal", "military_presence_imperial_legion", "dungeon_major_potential_if_contested", "environment_coastal_defense", "strategic_location_maritime_defense", "civil_war_quest_historic_site_potential"],
                "density": "average",
                "exit_label_from_parent": "Fort Gates",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 84,
                "name": "Brinewater Grotto",
                "desc": "A coastal cave system south of Solitude Docks, a known haunt for smugglers and bandits who use its hidden coves to move illicit goods.",
                "travel_desc": "Coastal cave system, known haunt for smugglers.",
                "tags": ["structure_type_natural_cave_coastal", "economic_activity_smuggling_route_active", "bandit_minor_camp_coastal", "dungeon_minor", "treasure_cache_rumored", "secret_location_cove"],
                "density": "sparse",
                "exit_label_from_parent": "Grotto Entrance",
                "exit_label_to_parent": "Exit Grotto"
            },
            {
                "id": 85,
                "name": "Broken Oar Grotto",
                "desc": "A large, hidden coastal cave system north of Solitude, serving as a major pirate and bandit stronghold known as Blackblood Marauders' hideout.",
                "travel_desc": "Large coastal cave, major pirate stronghold.",
                "tags": ["structure_type_natural_cave_large_coastal", "specific_landmark_type_pirate_cove_major_blackblood", "bandit_main_stronghold_pirate", "dungeon_major_complex", "quest_location_bounty_leader_pirate", "treasure_cache_major_rumored", "shipwreck_site_potential_interior"],
                "density": "bustling",
                "exit_label_from_parent": "Grotto Entrance",
                "exit_label_to_parent": "Exit Grotto"
            },
            {
                "id": 86,
                "name": "Ironback Hideout",
                "desc": "A small, well-hidden cave or ruin serving as a minor bandit hideout in the wilderness of Haafingar, used for ambushing travelers on less-patrolled roads.",
                "travel_desc": "Small, hidden cave, minor bandit hideout.",
                "tags": ["structure_type_natural_cave_minor_hidden", "bandit_minor_camp_ambush", "dungeon_minor", "wilderness_danger_spot", "terrain_hilly_forested_potential"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 87,
                "name": "Pinemoon Cave",
                "desc": "A cave system in the mountains of Haafingar, often inhabited by vampires or other dangerous creatures drawn to its isolation and darkness.",
                "travel_desc": "Cave system often inhabited by vampires.",
                "tags": ["structure_type_natural_cave", "specific_landmark_type_vampire_coven_minor_potential", "monster_den_dangerous_creatures", "dungeon_minor_dark", "terrain_mountainous_remote", "magical_properties_tainted_by_dark_magic_potential"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 88,
                "name": "Potema's Catacombs",
                "desc": "The extensive catacombs beneath Solitude's Temple of the Divines, where the Wolf Queen Potema's spirit is confronted by those seeking to prevent her return to power.",
                "travel_desc": "Extensive catacombs beneath Solitude's Temple.",
                "tags": ["structure_type_catacombs_structure_ancient", "undead_presence_strong_powerful", "dungeon_major_quest_specific", "quest_location_potema_wolf_queen_final", "boss_fight_potema_spirit_powerful", "magical_properties_haunted_aura_strong", "solitude_undercity_access"],
                "density": "average",
                "exit_label_from_parent": "Catacomb Entrance",
                "exit_label_to_parent": "Exit Catacombs"
            },
            {
                "id": 89,
                "name": "Ravenscar Hollow",
                "desc": "A small cave on the northern coast of Haafingar, typically home to a coven of hagravens who perform dark rituals overlooking the stormy sea.",
                "travel_desc": "Small coastal cave, home to a hagraven coven.",
                "tags": ["structure_type_natural_cave_coastal", "specific_landmark_type_hagraven_coven_lair", "ritual_site_dark_magic_coastal", "dungeon_minor", "magical_properties_tainted_by_dark_magic", "monster_den_hagraven"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 80001,
                "name": "Shadowgreen Cavern",
                "desc": "A lush, hidden cave system with unique bioluminescent flora and fauna, located southwest of Solitude. A place of surprising beauty and dangerous predators.",
                "travel_desc": "Lush, hidden cave with bioluminescent flora.",
                "tags": ["structure_type_natural_cave_hidden_lush", "unique_natural_formation_bioluminescent_flora", "alchemy_ingredient_source_rich_unique_glowing", "monster_den_spriggan_potential", "monster_den_predator_cave", "dungeon_minor_beautiful_dangerous", "secluded_nature_spot_underground"],
                "density": "sparse",
                "exit_label_from_parent": "Cavern Entrance",
                "exit_label_to_parent": "Exit Cavern"
            },
            {
                "id": 80002,
                "name": "Steepfall Burrow",
                "desc": "A small cave system or den, likely inhabited by frost trolls or ice wraiths, in the snowy mountains of Haafingar, guarding a narrow pass.",
                "travel_desc": "Small cave den, likely inhabited by frost trolls.",
                "tags": ["structure_type_natural_cave_ice", "monster_den_frost_troll_ice_wraith", "terrain_mountain_peak_pass", "dungeon_minor", "climate_glacial", "travel_route_alternative_dangerous_potential"],
                "density": "sparse",
                "exit_label_from_parent": "Burrow Entrance",
                "exit_label_to_parent": "Exit Burrow"
            },
            {
                "id": 80003,
                "name": "Stillborn Cave",
                "desc": "A small, eerie cave in Haafingar, rumored to be cursed or haunted by a sorrowful spirit. Few dare to enter.",
                "travel_desc": "Small, eerie cave rumored to be cursed or haunted.",
                "tags": ["structure_type_natural_cave_minor", "magical_properties_cursed_aura_rumor", "magical_properties_haunted_aura_potential_sorrowful", "local_legend_tragedy", "urban_issues_or_atmosphere_eerie_atmosphere"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 80004,
                "name": "The Steed Stone",
                "desc": "A Standing Stone located northwest of Solitude on a high ridge, granting increased carry weight and removing movement penalties from armor.",
                "travel_desc": "Standing Stone granting increased carry weight.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive_utility", "buff_carry_weight_increased", "buff_armor_no_penalty", "terrain_mountain_ridge_scenic", "cultural_historical_significance_ancient_magical_site"],
                "density": "empty",
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 80005,
                "name": "Katla's Farm",
                "desc": "A farm located just outside Solitude's main gates, providing produce and horses for the city and the Legion. Run by Katla.",
                "travel_desc": "Farm outside Solitude, provides produce and horses.",
                "tags": ["structure_type_farmstead", "settlement_features_stables_active", "economic_activity_farming_crops_livestock", "item_type_horse_vendor", "solitude_outskirts", "resource_node_food_supply"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 80014,
                "name": "Northwatch Keep",
                "desc": "A remote coastal fortress controlled by the Thalmor, used as a prison for those they deem enemies of the Aldmeri Dominion. It is heavily guarded and a symbol of Thalmor oppression.",
                "travel_desc": "Remote coastal fortress controlled by the Thalmor.",
                "tags": ["structure_type_fortified_keep_coastal_remote", "thalmor_presence_strong_fortress_prison", "settlement_features_prison_political_thalmor", "political_tension_high_foreign_occupation_stronghold_oppression", "dangerous_infiltration_target_heavily_guarded", "quest_location_rescue_thalmor_prisoners_main_quest_related_potential", "state_or_condition_current_enemy_controlled_area_thalmor", "altmer_presence_hostile_dominant", "environment_coastal_northern_haafingar"],
                "density": "average",
                "exit_label_from_parent": "Path to Keep",
                "exit_label_to_parent": "Leave Keep Area"
            },
            {
                "id": 80015,
                "name": "Volskygge",
                "desc": "An ancient Nordic ruin high in the mountains of Haafingar, leading to a Dragon Priest's tomb at its peak. Guarded by draugr and powerful magic.",
                "travel_desc": "Ancient Nordic ruin leading to a Dragon Priest's tomb.",
                "tags": ["nordic_burial_site_major_mountain_top", "cultural_historical_significance_dragon_cult_lair_priest_volsung", "undead_presence_strong_powerful_draugr_priest", "dungeon_major_complex_mountain_peak_ruin", "specific_landmark_type_word_wall_location", "artifact_location_powerful_mask_volsung", "draugr_heavy", "terrain_mountain_peak_haafingar", "puzzle_ancient_nordic_runes_potential"],
                "density": "average",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 80016,
                "name": "Clearpine Pond",
                "desc": "A tranquil pond nestled in the forests of Haafingar, known for its clear waters and abundant fish. A popular spot for local hunters and hermits.",
                "travel_desc": "Tranquil pond known for clear waters and abundant fish.",
                "tags": ["unique_natural_formation_pond_tranquil", "terrain_forest_haafingar", "economic_activity_fishing_industry_local_potential_abundant_fish", "hunter_gathering_spot_potential_hermit_camp", "peaceful_area_secluded", "secluded_nature_spot", "alchemy_ingredient_source_rich_potential_pond_flora"],
                "density": "empty",
                "exit_label_from_parent": "Path to Pond",
                "exit_label_to_parent": "Leave Pond Area"
            },
            {
                "id": 80017,
                "name": "Coastal Watch Fishery",
                "desc": "A small fishing village nestled in a cove near a crumbling, ancient watchtower on Haafingar's coast. The villagers are wary of both pirates and the crumbling tower's secrets.",
                "travel_desc": "Small fishing village near a crumbling watchtower.",
                "tags": ["populated_village_fishing", "settlement_minor_fishing_coastal_cove", "economic_activity_fishing_industry_local", "structure_type_ruined_tower_nearby_watchtower", "pirate_threat_local_rumor_coastal_raids", "cultural_historical_significance_local_legend_mystery_tower", "environment_coastal_cove_haafingar", "climate_temperate_coastal"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Fishery",
                "exit_label_to_parent": "Leave Fishery"
            },
            {
                "id": 80018,
                "name": "Shepherd's Rest Farm",
                "desc": "A secluded farm high in the hills of Haafingar, known for its hardy mountain sheep and the potent, if rough, cheese made from their milk.",
                "travel_desc": "Secluded farm known for hardy mountain sheep.",
                "tags": ["structure_type_farmstead_remote_highland", "economic_activity_farming_livestock_sheep_hardy", "unique_produce_cheese_mountain_potent", "isolated_location_haafingar_hills", "terrain_hilly_pastoral", "settlement_minor", "family_owned_farm_reclusive"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 80019,
                "name": "Smuggler's Cove (Minor)",
                "desc": "A small, well-hidden sea cave on Haafingar's coast, used by petty smugglers to land illicit goods or hide from patrols. Likely contains a small cache.",
                "travel_desc": "Small, hidden sea cave used by smugglers.",
                "tags": ["structure_type_natural_cave_coastal_hidden_sea_cave", "dungeon_minor", "economic_activity_smuggling_cache_small_petty_smugglers", "secret_location_cove_hidden_entrance", "treasure_cache_rumored_minor_illicit_goods", "exploration_point_smugglers_den"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cove"
            },
            {
                "id": 80020,
                "name": "Ruined Coastal Shrine",
                "desc": "The crumbling remains of a small, ancient shrine dedicated to an unknown sea deity or ancestor, battered by the coastal winds and waves of Haafingar.",
                "travel_desc": "Crumbling remains of an ancient coastal shrine.",
                "tags": ["structure_type_ruined_shrine_coastal_ancient", "cultural_historical_significance_ancient_religious_site_unknown_sea_deity_ancestor", "structure_condition_weathered_ruined_battered", "environment_coastal_exposed_windswept", "mystery_local_forgotten_god_sea_worship", "exploration_point_historic_religious_site"],
                "density": "empty",
                "exit_label_from_parent": "Path to Shrine",
                "exit_label_to_parent": "Leave Shrine Area"
            },
            {
                "id": 80021,
                "name": "Widow's Watch Ruins",
                "desc": "The crumbling remains of a small watchtower on a lonely cliff overlooking the Sea of Ghosts. Local tales say it was built by a noblewoman awaiting her lost husband's return from sea, and her sorrowful spirit still lingers.",
                "travel_desc": "Crumbling watchtower ruins overlooking the Sea of Ghosts.",
                "tags": ["structure_type_ruined_tower_coastal_watchtower", "dungeon_minor", "magical_properties_haunted_aura_potential_sorrowful_widow_spirit", "scenic_vista_panoramic_coastal_ruined_sea_of_ghosts", "cultural_historical_significance_local_legend_tragic_lost_husband", "structure_condition_ruined_extensively_crumbling", "exploration_point_haunted_ruin"],
                "density": "empty",
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 80022,
                "name": "Shrine of Dibella (Wilderness - Haafingar)",
                "desc": "A secluded, beautifully maintained outdoor shrine to Dibella, hidden in a picturesque grove or clifftop in Haafingar's wilderness. A place of quiet inspiration and artistic offerings.",
                "travel_desc": "Secluded outdoor shrine to Dibella.",
                "tags": ["structure_type_shrine_outdoor_structure_beautiful", "religious_site_aedric", "dibella_shrine", "secluded_nature_spot_picturesque_grove_cliffside", "magical_properties_holy_ground_aedric_potential", "art_beauty_focus_inspiration_offerings", "terrain_grove_cliffside_potential_haafingar_wilderness", "exploration_point_religious_hidden_serene"],
                "density": "empty",
                "exit_label_from_parent": "Path to Shrine",
                "exit_label_to_parent": "Leave Shrine Area"
            },
            {
                "id": 80024,
                "name": "The Katariah (Imperial Flagship)",
                "desc": "A massive Imperial warship, often docked at Solitude or patrolling the Sea of Ghosts. It represents the might of the Imperial Navy in Skyrim's waters. (May not be Emperor Titus Mede II's personal vessel in 4E 200, but a significant flagship).",
                "travel_desc": "Massive Imperial warship, often docked at Solitude.",
                "tags": ["structure_type_ship_imperial_warship_major_flagship", "military_presence_imperial_navy_skyrim_fleet", "solitude_docks_visitor_potential_patrol_route", "environment_sea_of_ghosts_patrol_coastal_waters", "unique_landmark_mobile_potential_imperial_might", "imperial_influence_strong_naval_power_projection", "event_encounter_potential_naval_battle_boarding"],
                "density": "bustling",
                "exit_label_from_parent": "Board Ship",
                "exit_label_to_parent": "Disembark Ship"
            },
            {
                "id": 80025,
                "name": "Orphan's Tear",
                "desc": "A shipwreck on the northern coast of Haafingar, west of the Solitude Lighthouse. It is rumored to hold lost treasures and is sometimes used as a hideout by coastal scavengers or bandits.",
                "travel_desc": "Shipwreck rumored to hold lost treasures.",
                "tags": ["structure_type_shipwreck_site_coastal_northern_haafingar", "treasure_cache_rumored_lost_valuable_cargo", "bandit_minor_camp_scavenger_potential_coastal_bandits", "dungeon_minor", "environment_coastal_exploration_wreckage", "quest_location_minor_potential_retrieve_item_clear_scavengers"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Wreck",
                "exit_label_to_parent": "Leave Wreck Area"
            },
            {
                "id": 80026,
                "name": "Solitude Lighthouse (Structure)",
                "desc": "The tall lighthouse guiding ships into Solitude's harbor. While functional, its keeper might have local concerns or knowledge.",
                "travel_desc": "Tall lighthouse guiding ships into Solitude's harbor.",
                "tags": ["structure_type_lighthouse_structure_functional_solitude", "environment_coastal_landmark_navigational_solitude_harbor", "solitude_harbor_aid_shipping_safety", "quest_giver_potential_lighthouse_keeper_concerns_knowledge", "unique_landmark_iconic_local_solitude_skyline", "exploration_point_functional_lighthouse"],
                "density": "sparse",
                "exit_label_from_parent": "Lighthouse Door",
                "exit_label_to_parent": "Exit Lighthouse"
            },
            {
                "id": 80027,
                "name": "The Dainty Sload",
                "desc": "A notorious pirate or smuggler ship that sometimes anchors in hidden coves along Haafingar's coast, or might even brazenly try to trade illicit goods at the Solitude Docks under a false flag.",
                "travel_desc": "Notorious pirate or smuggler ship.",
                "tags": ["structure_type_ship_pirate_smuggler_notorious_dainty_sload", "faction_hostile_pirate_sload_crew", "environment_coastal_encounter_hostile_potential_hidden_coves_docks", "economic_activity_smuggling_illicit_trade_skooma_contraband", "black_market_connection_rumor_riften_solitude", "unique_encounter_named_ship_pirate_captain", "quest_location_bounty_target_potential_ship_captain"]
            }
        ]
    },
    {
        "id": 8012,
        "name": "Solitude Caravan Camp",
        "desc": "A temporary camp set up by traveling merchants outside Solitude. It's a place of trade and rest for those journeying through Haafingar.",
        "travel_desc": "Caravan camp outside Solitude.",
        "tags": ["structure_type_encampment", "settlement_features_caravan_camp", "economic_activity_trade_caravans", "travel_hub_roadside"],
        "density": "sparse",
        "context_tags": ["exterior", "encampment_type", "trade_zone"],
        "demographics": {"Nord": 40, "Imperial": 30, "Khajiit": 20, "Breton": 10},
        "exit_label_from_parent": "Camp Entrance",
        "exit_label_to_parent": "Exit Camp"
    },
    {
        "id": 80011,
        "name": "Pelagius Wing",
        "desc": "A sealed-off wing of the Blue Palace, rumored to be haunted by the mad Emperor Pelagius Septim III.",
        "travel_desc": "Sealed-off wing of the Blue Palace, rumored to be haunted.",
        "tags": ["structure_type_castle_wing_sealed", "haunted_location_ghosts_spirits", "unique_landmark_historical_site", "blue_palace_extension", "imperial_history_related"],
        "density": "sparse",
        "context_tags": ["interior", "castle_wing"],
        "exit_label_from_parent": "Wing Entrance",
        "exit_label_to_parent": "Exit Wing"
    },
]