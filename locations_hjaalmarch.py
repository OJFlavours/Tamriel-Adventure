from locations_morthal_city import MORTHAL_CITY_LOCATION_DATA

HJAALMARCH_LOCATIONS = [
    # HJAALMARCH (Morthal Hold)
    {
        "id": 4,
        "name": "Hjaalmarch",
        "desc": "A bleak, marshy hold shrouded in perpetual mist and steeped in superstition. Its capital, Morthal, is known for its reclusive nature and recent troubles with strange occurrences and whispers of vampirism.",
        "travel_desc": "Bleak, marshy hold shrouded in mist and superstition.",
        "tags": ["hold", "terrain_marsh_swamp_dominant", "state_or_condition_current_isolated_and_forgotten_bleak", "nordic_culture_local_reclusive", "urban_issues_or_atmosphere_fear_and_superstition_pervasive", "magical_properties_daedric_influence_subtle_rumor_vampirism", "climate_swampy_misty", "environment_wilderness_marshland", "political_tension_high_potential_jarl_seer", "economic_activity_logging_timber_minor", "economic_activity_mining_iron_minor"],
        "density": "sparse",
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {
            "links": [
                {"name": "The Pale", "connection_type": "Road"},
                {"name": "The Reach", "connection_type": "Road"},
                {"name": "Haafingar", "connection_type": "Road"},
                {"name": "Stonehills Trail", "connection_type": "Path"},
                {"name": "Drajkmyr Marsh Path", "connection_type": "Path"}
            ]
        },
        "sub_locations": [
            {
                "id": 40,
                "name": "Morthal",
                "desc": "A somber town built on the edge of the Drajkmyr Marsh, wrapped in fog and mystery. Its Jarl, Idgrod Ravencrone, is a seer, and the town is currently dealing with unease from a recent fire and talk of vampires.",
                "travel_desc": "Somber town on marsh edge, wrapped in fog and mystery.",
                "tags": ["populated_town", "terrain_marsh_edge_drajkmyr", "city_affiliation_morthal_town", "urban_issues_or_atmosphere_fear_and_superstition_vampires_fire", "magical_properties_daedric_influence_subtle_rumor_vampirism", "settlement_features_jarls_longhouse_idgrod_seer", "state_or_condition_current_isolated_and_forgotten_somber", "quest_location_vampire_investigation_laid_to_rest", "climate_swampy_foggy", "nordic_architecture_local_wood"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Town",
                "exit_label_to_parent": "Leave Town",
                "sub_locations": MORTHAL_CITY_LOCATION_DATA
            },
            {
                "id": 41,
                "name": "Movarth's Lair",
                "desc": "A dank cave north of Morthal, rumored to be the den of the master vampire Movarth Piquine and his thralls. Its discovery is key to resolving Morthal's troubles.",
                "travel_desc": "Dank cave, rumored den of master vampire Movarth.",
                "tags": ["structure_type_natural_cave_dank", "specific_landmark_type_vampire_ancient_lair_movarth", "dungeon_major", "quest_location_vampire_investigation_laid_to_rest_lair", "undead_presence_strong_vampires_thralls", "magical_properties_tainted_by_dark_magic", "boss_fight_vampire_lord_potential_movarth", "state_or_condition_current_lawless_area_vampire"],
                "density": "average",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 42,
                "name": "Ustengrav",
                "desc": "A sprawling ancient Nordic tomb deep within Hjaalmarch's marshes, said to hold the Horn of Jurgen Windcaller, a significant relic sought by the Greybeards.",
                "travel_desc": "Sprawling Nordic tomb, said to hold Horn of Jurgen Windcaller.",
                "tags": ["nordic_burial_site_major_sprawling", "dungeon_large_complex", "undead_presence_strong", "draugr_heavy", "quest_location_main_story_early_horn_of_jurgen_windcaller", "specific_landmark_type_word_wall_location", "artifact_location_unique_item_horn_of_jurgen_windcaller", "puzzle_ancient_nordic_traps", "terrain_marsh_edge_hjaalmarch", "cultural_historical_significance_nordic_ancient_site_relic"],
                "density": "average",
                "exit_label_from_parent": "Tomb Entrance",
                "exit_label_to_parent": "Exit Tomb"
            },
            {
                "id": 43,
                "name": "Stonehills",
                "desc": "A modest mining outpost in Hjaalmarch, focused on excavating iron ore, managed by Pactur.",
                "travel_desc": "Modest mining outpost focused on iron ore.",
                "tags": ["populated_village_outpost_mining", "settlement_minor", "economic_activity_mining_iron", "resource_node_iron", "terrain_hilly_marsh_edge", "climate_swampy_edge", "quest_giver_potential_mine_issues"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Outpost",
                "exit_label_to_parent": "Leave Outpost",
                "sub_locations": [
                    {
                        "id": 4301,
                        "name": "Rockwallow Mine",
                        "desc": "The iron mine that sustains the small settlement of Stonehills.",
                        "travel_desc": "Iron mine sustaining Stonehills.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "resource_node_iron", "economic_backbone_stonehills"],
                        "density": "average",
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    },
                    {
                        "id": 4302,
                        "name": "Sorli's House",
                        "desc": "The residence of Sorli the Builder, an important figure in Stonehills who hopes to see the mine prosper.",
                        "travel_desc": "Residence of Sorli the Builder.",
                        "tags": ["structure_type_residence", "commoner_dwelling_mine_owner_family", "community_leader_potential_pactur_sorli"],
                        "density": "sparse",
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    }
                ]
            },
            {
                "id": 44,
                "name": "Apprentice Stone",
                "desc": "A Standing Stone located in the marshes northwest of Morthal, granting faster Magicka regeneration but also increased susceptibility to magic.",
                "travel_desc": "Standing Stone granting faster Magicka regen but increased susceptibility.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_double_edged", "terrain_marsh_island", "cultural_historical_significance_ancient_magical_site", "buff_magicka_regen_increased", "debuff_magic_weakness_increased", "power_magicka_focused_risky"],
                "density": "empty",
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 45,
                "name": "Brood Cavern",
                "desc": "A small cave in Hjaalmarch, often infested with spiders, chaurus, or other venomous creatures.",
                "travel_desc": "Small cave often infested with venomous creatures.",
                "tags": ["structure_type_natural_cave", "monster_den_spider_major_potential", "monster_den_chaurus_potential", "dungeon_minor", "terrain_marsh", "alchemy_ingredient_source_rich_potential_venom_eggs", "exploration_point_dangerous_creatures"],
                "density": "average",
                "exit_label_from_parent": "Cavern Entrance",
                "exit_label_to_parent": "Exit Cavern"
            },
            {
                "id": 46,
                "name": "Chillwind Depths",
                "desc": "A large cave system south of Dragon Bridge (near Hjaalmarch border), inhabited by Falmer, Chaurus, and other subterranean horrors.",
                "travel_desc": "Large cave system inhabited by Falmer and Chaurus.",
                "tags": ["structure_type_natural_cave_large", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_major", "environment_underground_deep", "terrain_mountain_cave_remote_hjaalmarch_haafingar_border", "state_or_condition_current_lawless_area_falmer_territory", "exploration_challenge_extreme_danger"],
                "density": "bustling",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 47,
                "name": "Dead Men's Respite",
                "desc": "A Nordic ruin southwest of Morthal, connected to the Bards College and the legend of King Olaf One-Eye. It is guarded by draugr and holds ancient secrets.",
                "travel_desc": "Nordic ruin connected to Bards College and King Olaf.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "faction_bards_college_related_quest_king_olaf", "specific_landmark_type_word_wall_location", "cultural_historical_significance_legendary_hero_location_king_olaf", "puzzle_ancient_nordic_ghostly_bard", "artifact_location_king_olafs_verse_potential"],
                "density": "average",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 48,
                "name": "Folgunthur",
                "desc": "An ancient Nordic ruin south of Solitude, near the Hjaalmarch border, where a fragment of the legendary Gauldur Amulet is sought, guarded by Mikrul Gauldurson.",
                "travel_desc": "Ancient Nordic ruin, site of a Gauldur Amulet fragment.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy_gauldurson", "quest_location_artifact_gauldur_amulet_fragment", "cultural_historical_significance_ancient_magical_site_gauldur_legend", "puzzle_dragon_claw_ivory", "artifact_location_powerful_gauldur_fragment", "boss_fight_draugr_lord_mikrul_gauldurson"],
                "density": "average",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 49,
                "name": "Kjenstag Ruins",
                "desc": "Ruined Nordic structures in the marshes, sometimes haunted by restless spirits or occupied by desperate bandits seeking shelter.",
                "travel_desc": "Ruined Nordic structures in the marshes.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_minor_potential", "terrain_marsh_isolated", "magical_properties_haunted_aura_potential_restless_spirits", "bandit_minor_camp_potential_shelter", "structure_condition_ruined_extensively", "exploration_point_minor_ruin"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 40001,
                "name": "Meeko's Shack",
                "desc": "A small, abandoned shack south of Solitude Sawmill, near the Hjaalmarch border. A loyal dog named Meeko waits here for his deceased master.",
                "travel_desc": "Small, abandoned shack where Meeko waits.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_abandoned", "animal_companion_unique_meeko_dog", "tragedy_site_minor_deceased_master", "terrain_forested_area_edge_haafingar_hjaalmarch_border", "quest_giver_potential_adopt_dog"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Shack",
                "exit_label_to_parent": "Leave Shack Area"
            },
            {
                "id": 40002,
                "name": "Robber's Gorge",
                "desc": "A bandit-controlled ravine and bridge southwest of Rorikstead, on the edge of Hjaalmarch, a notorious spot for ambushes.",
                "travel_desc": "Bandit-controlled ravine and bridge, ambush spot.",
                "tags": ["bandit_main_stronghold_ravine", "terrain_canyon_river_gorge", "structure_type_bridge_structure_wooden", "dungeon_major", "state_or_condition_current_bandit_controlled_area", "toll_road_illegal_ambush_spot", "quest_location_bounty_leader_potential"],
                "density": "average",
                "exit_label_from_parent": "Path to Gorge",
                "exit_label_to_parent": "Leave Gorge Area"
            },
            {
                "id": 40003,
                "name": "Wreck of the Icerunner",
                "desc": "A shipwreck on the northern coast of Hjaalmarch, west of Solitude. It is now a den for bandits or pirates who prey on coastal traffic.",
                "travel_desc": "Shipwreck on the northern coast, den for bandits/pirates.",
                "tags": ["structure_type_shipwreck_site_coastal", "specific_landmark_type_pirate_cove_hidden_potential", "environment_coastal_northern_hjaalmarch", "dungeon_minor", "treasure_cache_rumored_lost_cargo", "bandit_minor_camp_potential_pirates", "exploration_point_historic_wreck"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Wreck",
                "exit_label_to_parent": "Leave Wreck Area"
            },
            {
                "id": 40004,
                "name": "The Stumbling Sabrecat",
                "desc": "A rickety, half-sunken shack in the deepest part of the Drajkmyr Marsh, rumored to be the home of a reclusive (and possibly mad) alchemist or a coven of witches.",
                "travel_desc": "Rickety, half-sunken shack in Drajkmyr Marsh.",
                "tags": ["structure_type_shack_or_hut_rickety_sunken", "structure_condition_ruined_extensively_half_sunken", "terrain_marsh_deep_drajkmyr", "hermit_lair_potential_mad_alchemist_witch", "magical_properties_tainted_by_dark_magic_potential", "alchemy_ingredient_source_rich_potential_rare_swamp_flora", "witch_coven_potential_rumor", "mystery_local_reclusive_occupant"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Shack",
                "exit_label_to_parent": "Leave Shack Area"
            },
            {
                "id": 40005,
                "name": "Folkvar's Folly",
                "desc": "A small, abandoned watchtower slowly sinking into the marsh. Local legend says it was built by a foolish Thane who ignored warnings about the unstable ground.",
                "travel_desc": "Small, abandoned watchtower sinking into the marsh.",
                "tags": ["structure_type_ruined_tower_sinking", "structure_condition_collapsed_sinking_marsh", "terrain_marsh", "cultural_historical_significance_local_legend_foolish_thane", "bandit_minor_camp_potential", "state_or_condition_current_isolated_and_forgotten", "exploration_point_minor_ruin_legend"],
                "density": "empty",
                "exit_label_from_parent": "Path to Ruin",
                "exit_label_to_parent": "Leave Ruin"
            },
            {
                "id": 40006,
                "name": "Drajkmyr Crossing",
                "desc": "A tiny, precarious stilt-village built over the murky waters on the edge of the Drajkmyr marsh, known for its unique eel fishing techniques.",
                "travel_desc": "Tiny, precarious stilt-village known for eel fishing.",
                "tags": ["populated_village_stilt", "settlement_minor_precarious", "economic_activity_fishing_industry_local_eel_specialty", "terrain_marsh_drajkmyr_edge", "structure_type_settlement_minor_stilt_village", "unique_culture_local_eel_fishing", "state_or_condition_current_isolated_and_forgotten", "climate_swampy_misty"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Crossing",
                "exit_label_to_parent": "Leave Crossing"
            },
            {
                "id": 40007,
                "name": "Peatbogger's Hut",
                "desc": "The isolated hut of a solitary peat farmer, who harvests the rich soil of Hjaalmarch for fuel and fertilizer.",
                "travel_desc": "Isolated hut of a solitary peat farmer.",
                "tags": ["structure_type_shack_or_hut_peat_farmer", "economic_activity_farming_crops_peat_harvesting", "terrain_marsh_isolated", "hermit_lair_potential_solitary_farmer", "state_or_condition_current_isolated_and_forgotten", "resource_node_peat_fuel_fertilizer"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Hut",
                "exit_label_to_parent": "Leave Hut Area"
            },
            {
                "id": 40008,
                "name": "Murkwater Hollow",
                "desc": "A muddy, flooded cave system deep within Hjaalmarch's swamps, likely home to chaurus, mudcrabs, or even a reclusive giant snake if such existed.",
                "travel_desc": "Muddy, flooded cave system in Hjaalmarch's swamps.",
                "tags": ["structure_type_natural_cave_flooded", "terrain_marsh_swamp_deep", "dungeon_minor", "monster_den_chaurus", "monster_den_mudcrab", "structure_condition_flooded_muddy", "alchemy_ingredient_source_rich_potential_chaurus_eggs_mudcrab_chitin"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 40009,
                "name": "Sinking Stones of the Marsh",
                "desc": "A small, barely visible ruin of ancient stones half-sunk in the swamp, perhaps part of an old Nordic watchtower or shrine, now reclaimed by the marsh.",
                "travel_desc": "Small ruin of ancient stones half-sunk in the swamp.",
                "tags": ["structure_type_ruined_shrine_nordic_watchtower_potential", "nordic_burial_site_minor_potential", "terrain_marsh_sinking_stones", "structure_condition_collapsed_half_sunk", "treasure_cache_rumored_meager", "cultural_historical_significance_nordic_ancient_site_reclaimed_by_marsh", "exploration_point_minor_ruin"],
                "density": "empty",
                "exit_label_from_parent": "Path to Stones",
                "exit_label_to_parent": "Leave Stones Area"
            },
            {
                "id": 40010,
                "name": "Misty Grove Farm",
                "desc": "A small, struggling farm on the edge of the Drajkmyr Marsh, where the farmer battles constant dampness and swamp pests to grow hardy root vegetables.",
                "travel_desc": "Small, struggling farm on the edge of Drajkmyr Marsh.",
                "tags": ["structure_type_farmstead_struggling", "economic_activity_farming_crops_root_vegetables", "terrain_marsh_edge_drajkmyr", "state_or_condition_current_isolated_and_forgotten_struggling", "structure_condition_weathered_damp", "climate_swampy_pests"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 40011,
                "name": "Fort Snowhawk (Ruined)",
                "desc": "The dilapidated ruins of an old Imperial fort, now largely swallowed by the marsh. Rumored to be haunted by its former garrison or used as a hideout by bog bandits.",
                "travel_desc": "Dilapidated ruins of an old Imperial fort.",
                "tags": ["structure_type_ruined_fort_imperial_historic", "terrain_marsh_swallowed", "dungeon_minor", "magical_properties_haunted_aura_potential_former_garrison", "bandit_minor_camp_potential_bog_bandits", "cultural_historical_significance_historic_site_imperial_fort", "structure_condition_ruined_extensively_dilapidated"],
                "density": "sparse",
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 40012,
                "name": "Shrine of Herma-Mora (Hidden Marsh Shrine)",
                "desc": "A small, hidden shrine of crudely piled stones and waterlogged tomes dedicated to Hermaeus Mora, tucked away in a particularly dense and foggy part of Hjaalmarch. Only those seeking forbidden knowledge would find it.",
                "travel_desc": "Small, hidden shrine to Hermaeus Mora.",
                "tags": ["structure_type_shrine_outdoor_structure_crude", "magical_properties_daedric_influence_overt_hermaeus_mora", "terrain_marsh_dense_foggy", "secret_location_hidden_shrine", "forbidden_knowledge_dangerous_waterlogged_tomes", "cult_activity_potential_minor_hermaeus_mora", "hermaeus_mora_shrine", "exploration_point_lore_daedric"],
                "density": "empty",
                "exit_label_from_parent": "Path to Shrine",
                "exit_label_to_parent": "Leave Shrine Area"
            },
            {
                "id": 40013,
                "name": "Bogbound Barrow",
                "desc": "A small, partially flooded Nordic barrow slowly being reclaimed by the swamp. It's likely home to draugr who guard meager treasures.",
                "travel_desc": "Small, partially flooded Nordic barrow.",
                "tags": ["nordic_burial_site_minor_barrow", "structure_condition_flooded_partially", "dungeon_minor", "undead_presence_strong", "draugr_heavy_meager_treasure_guardians", "terrain_marsh_reclaimed", "exploration_point_minor_tomb"],
                "density": "sparse",
                "exit_label_from_parent": "Barrow Entrance",
                "exit_label_to_parent": "Exit Barrow"
            },
            {
                "id": 40014,
                "name": "Lost Echo Cave",
                "desc": "A large cave system in Hjaalmarch, west of Morthal, known for its unusual acoustics. It is now a den for Falmer and their chaurus, and contains an ancient Word Wall.",
                "travel_desc": "Large cave system known for unusual acoustics, den for Falmer.",
                "tags": ["structure_type_natural_cave_large", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_major", "specific_landmark_type_word_wall_location", "unique_natural_formation_unusual_acoustics", "state_or_condition_current_lawless_area_falmer_territory", "terrain_hjaalmarch_west_morthal"],
                "density": "average",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 40015,
                "name": "Ragnvald",
                "desc": "An ancient Nordic ruin in the mountains of Hjaalmarch, north of Markarth. It is a burial site guarded by powerful draugr and the Dragon Priest Otar the Mad.",
                "travel_desc": "Ancient Nordic ruin, burial site of Dragon Priest Otar.",
                "tags": ["nordic_burial_site_major_dragon_priest_tomb", "dungeon_large_complex", "cultural_historical_significance_dragon_cult_lair_priest_otar_the_mad", "undead_presence_strong_powerful", "draugr_heavy", "specific_landmark_type_word_wall_location", "magical_properties_arcane_nexus_powerful", "dragon_priest_otar", "artifact_location_powerful_mask_otar", "terrain_mountainous_hjaalmarch_north_markarth"],
                "density": "average",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 40016,
                "name": "Orotheim",
                "desc": "A small cave system in the western part of Hjaalmarch, often used as a hideout by a desperate group of bandits preying on the sparse traffic through the marshes.",
                "travel_desc": "Small cave system, often a bandit hideout.",
                "tags": ["structure_type_natural_cave_small", "bandit_minor_camp_desperate", "dungeon_minor", "terrain_marsh_edge_western_hjaalmarch", "state_or_condition_current_bandit_controlled_area", "quest_location_bounty_potential_minor"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 40017,
                "name": "Mzinchaleft",
                "desc": "A large Dwemer ruin in Hjaalmarch, south of Dawnstar (near The Pale border). It is a dangerous complex filled with Dwemer constructs, Falmer, and a Great Lift providing access to Blackreach.",
                "travel_desc": "Large Dwemer ruin with access to Blackreach.",
                "tags": ["dwemer_ruin_major_city_complex", "dungeon_large_complex_dangerous", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "specific_landmark_type_blackreach_elevator_access", "cultural_historical_significance_dwemer_ruin_site_major", "ancient_technology_dwemer", "chaurus_nest_major_potential", "terrain_hjaalmarch_pale_border_south_dawnstar", "quest_location_daedric_hermaeus_mora_ogradh_potential"],
                "density": "bustling",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            }
        ]
    }
]