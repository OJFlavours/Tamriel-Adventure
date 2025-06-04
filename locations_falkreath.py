from locations_falkreath_city import FALKREATH_CITY_LOCATIONS
FALKREATH_LOCATIONS = [
    # FALKREATH HOLD
    {
        "id": 5,
        "name": "Falkreath Hold",
        "desc": "A heavily forested hold in southern Skyrim, known for its ancient woods, towering mountains, and the somber town of Falkreath with its large graveyard. It borders Cyrodiil and is an important Imperial territory.",
        "travel_desc": "Heavily forested southern hold, known for ancient woods and mountains.",
        "tags": ["hold", "terrain_forest_dense_ancient", "climate_temperate_continental", "cultural_historical_significance_graveyard_town_falkreath", "terrain_mountainous_southern_skyrim", "cyrodiil_border_region", "nordic_culture_local_somber", "imperial_influence_strong", "economic_activity_logging_timber_major", "state_or_condition_current_politically_stable", "dark_brotherhood_presence_rumored_sanctuary"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "links": [
                {"name": "Whiterun Hold", "connection_type": "Road"},
                {"name": "The Reach", "connection_type": "Road"},
                {"name": "Cyrodiil (Fort Neugrad Pass)", "connection_type": "Road"},
                {"name": "Helgen Pass (functional)", "connection_type": "Path"},
                {"name": "Pine Forest Trail", "connection_type": "Path"},
                {"name": "Jerall Mountains Path", "connection_type": "Path"}
            ]
        },
        "sub_locations": [
            {
                "id": 50,
                "name": "Falkreath (Town)",
                "desc": "A quiet, somewhat gloomy town nestled in the southern forests, known for its extensive graveyard and timber industry. It is the seat of Jarl Siddgeir, an Imperial appointee.",
                "travel_desc": "Quiet, gloomy town known for its graveyard and timber industry.",
                "tags": ["populated_town", "terrain_forest_southern", "city_affiliation_falkreath_town", "cultural_historical_significance_graveyard_town_largest_in_skyrim", "settlement_features_jarls_longhouse_siddgeir", "daedric_influence_subtle_rumor_clues", "economic_activity_logging_timber", "urban_issues_or_atmosphere_oppressive_atmosphere_gloomy", "imperial_influence_strong", "nordic_architecture_local_wood"],
                "exit_label_from_parent": "Town Gate",
                "exit_label_to_parent": "Town Gate",
                "sub_locations": FALKREATH_CITY_LOCATIONS,
            },
            {
                "id": 51,
                "name": "Pinewatch",
                "desc": "A secluded farmhouse north of Falkreath. While appearing innocent, it serves as a well-concealed front for a secret bandit hideout and smuggling operation.",
                "travel_desc": "Secluded farmhouse, a front for a bandit hideout.",
                "tags": ["structure_type_farmstead_front_operation", "bandit_main_stronghold_hidden_cave", "dungeon_major_complex", "quest_location_thieves_guild_riggs_note", "economic_activity_smuggling_route_active", "secret_location_hidden_basement_entrance", "terrain_forest_secluded", "state_or_condition_current_bandit_controlled_area"],
                "exit_label_from_parent": "Path to Farmhouse",
                "exit_label_to_parent": "Leave Farmhouse Area"
            },
            {
                "id": 52,
                "name": "Halldir's Cairn",
                "desc": "A solemn Nordic barrow southwest of Falkreath, haunted by the powerful draugr sorcerer Halldir and his elemental thralls.",
                "travel_desc": "Solemn Nordic barrow haunted by draugr sorcerer Halldir.",
                "tags": ["nordic_burial_site_major_cairn", "dungeon_major", "undead_presence_strong_draugr_sorcerer_halldir", "magical_properties_arcane_nexus_elemental_magic", "monster_den_elemental_thralls_fire_frost_shock", "draugr_heavy", "boss_fight_mage_powerful_halldir", "terrain_forest_southwest_falkreath"],
                "exit_label_from_parent": "Cairn Entrance",
                "exit_label_to_parent": "Exit Cairn"
            },
            {
                "id": 53,
                "name": "Helgen",
                "desc": "A modest but strategically important Imperial fortified town at the southern border of Whiterun Hold, known for its lumber trade and guarding the pass to Cyrodiil. It is currently a functional settlement.",
                "travel_desc": "Modest Imperial fortified town, guards pass to Cyrodiil.",
                "tags": ["populated_village_fortified", "imperial_influence_strong_outpost", "economic_activity_logging_timber", "cyrodiil_border_region_pass_guard", "quest_location_main_story_opening_sequence_potential_alt_start", "state_or_condition_current_functional_settlement_pre_dragon_attack", "terrain_whiterun_falkreath_border"],
                "exit_label_from_parent": "Town Gate",
                "exit_label_to_parent": "Town Gate",
                 "sub_locations": [
                    {
                        "id": 5301,
                        "name": "Helgen Keep",
                        "desc": "The main keep of Helgen, garrisoned by Imperial soldiers. It serves as the town's primary defense and administrative center.",
                        "travel_desc": "Main keep of Helgen, garrisoned by Imperials.",
                        "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion_garrison", "imperial_influence_strong", "government_local_imperial_command", "structure_condition_pristine_functional"],
                        "exit_label_from_parent": "Keep Entrance",
                        "exit_label_to_parent": "Exit Keep"
                    },
                    {
                        "id": 5302,
                        "name": "Helgen Homestead",
                        "desc": "One of the sturdy wooden homes within the town of Helgen.",
                        "travel_desc": "A sturdy wooden home in Helgen.",
                        "tags": ["structure_type_residence", "commoner_dwelling_wooden_sturdy", "settlement_minor_housing"],
                        "exit_label_from_parent": "House Door",
                        "exit_label_to_parent": "Exit House"
                    },
                    {
                        "id": 5303,
                        "name": "The Dragon's Rest Inn (Helgen)",
                        "desc": "A small, welcoming inn in Helgen, catering to local loggers and Imperial soldiers passing through.",
                        "travel_desc": "Small, welcoming inn in Helgen.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local_loggers_soldiers", "food_drink_vendor", "lodging_available", "rumor_source_local_border_news"],
                        "demographics": {"Imperial": 50, "Nord": 40, "Breton": 5, "Redguard": 5},
                        "exit_label_from_parent": "Inn Door",
                        "exit_label_to_parent": "Exit Inn"
                    }
                ]
            },
            {
                "id": 54,
                "name": "Ancestor Glade",
                "desc": "A hidden, serene glade sacred to the Moth Priests, located in the southern mountains of Falkreath Hold. It's a place of profound natural beauty and ancient ritual, though its significance is known to few.",
                "travel_desc": "Hidden, serene glade sacred to Moth Priests.",
                "tags": ["cultural_historical_significance_sacred_grove_moth_priests_kynareth", "unique_natural_formation_ancestor_moths_canticle_trees", "magical_properties_aedric_blessing_active_ancient_ritual_site", "secluded_nature_spot_profound_beauty", "quest_location_dawnguard_potential_alt_moth_priest_ritual", "alchemy_ingredient_source_rich_unique_ancestor_moth_wings_bark", "terrain_southern_falkreath_mountains_hidden"],
                "exit_label_from_parent": "Path to Glade",
                "exit_label_to_parent": "Leave Glade"
            },
            {
                "id": 55,
                "name": "Bloodlet Throne",
                "desc": "A ruined fort atop a mountain in Falkreath, now a lair for a powerful coven of vampires who prey on unwary travelers.",
                "travel_desc": "Ruined fort, lair for a powerful vampire coven.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_vampire_ancient_lair_coven", "dungeon_major", "terrain_mountain_peak_falkreath", "state_or_condition_current_lawless_area_vampire_controlled", "undead_presence_strong_vampires_thralls", "magical_properties_tainted_by_dark_magic", "boss_fight_vampire_lord_potential"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 56,
                "name": "Brittleshin Pass",
                "desc": "A small cave system serving as a pass through the mountains south of Falkreath, often inhabited by necromancers, undead, or desperate bandits.",
                "travel_desc": "Small cave system, a pass through the mountains.",
                "tags": ["structure_type_natural_cave_pass", "terrain_mountain_pass_south_falkreath", "specific_landmark_type_necromancer_lair_potential", "undead_presence_skeletons_potential", "bandit_minor_camp_potential", "dungeon_minor", "travel_route_alternative_dangerous", "exploration_point_shortcut_cave"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 57,
                "name": "Embershard Mine",
                "desc": "An iron mine located between Riverwood and Helgen, currently occupied by a band of opportunistic bandits.",
                "travel_desc": "Iron mine occupied by bandits.",
                "tags": ["structure_type_mine_active_iron", "economic_activity_mining_iron", "bandit_minor_camp_opportunistic", "dungeon_minor", "state_or_condition_current_bandit_controlled_area", "resource_node_iron", "quest_location_clear_mine_early_game_potential", "riverwood_helgen_road_nearby"],
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 58,
                "name": "Evergreen Grove",
                "desc": "A small, secluded grove west of Falkreath, known for its spriggans and natural tranquility. Alchemists sometimes seek rare herbs here.",
                "travel_desc": "Secluded grove known for spriggans and tranquility.",
                "tags": ["environment_wilderness_grove_secluded", "terrain_forest_west_falkreath", "specific_landmark_type_spriggan_sanctuary", "alchemy_ingredient_source_rich_rare_herbs", "secluded_nature_spot_tranquil", "magical_properties_enchanted_neutral_nature_spirits", "monster_den_spriggan_strong"],
                "exit_label_from_parent": "Path to Grove",
                "exit_label_to_parent": "Leave Grove"
            },
            {
                "id": 59,
                "name": "Knifepoint Ridge",
                "desc": "A bandit-occupied mine and camp in the northwestern part of Falkreath Hold, from which raids are launched. Rumored to be connected to a Daedric artifact.",
                "travel_desc": "Bandit-occupied mine and camp, rumored Daedric connection.",
                "tags": ["structure_type_mine_active_camp_integrated", "economic_activity_mining_corundum_potential", "bandit_main_stronghold_raiding_base", "dungeon_major", "quest_location_daedric_boethiah_champion", "state_or_condition_current_bandit_controlled_area", "terrain_northwestern_falkreath_hold", "artifact_location_daedric_related_potential"],
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Leave Ridge Area"
            },
            {
                "id": 50001,
                "name": "Moss Mother Cavern",
                "desc": "A cave system east of Falkreath, home to various creatures like spriggans and bears, and connected to local legends of nature spirits.",
                "travel_desc": "Cave system home to spriggans and bears.",
                "tags": ["structure_type_natural_cave", "monster_den_spriggan", "monster_den_bear", "quest_location_local_legend_valdr_hunt", "dungeon_minor", "unique_natural_formation_mossy_cave", "alchemy_ingredient_source_rich_moss_animal_parts"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 50002,
                "name": "Peak's Shade Tower",
                "desc": "A ruined tower south of Falkreath, often a lair for hagravens or other malevolent creatures who perform dark rituals under the forest canopy.",
                "travel_desc": "Ruined tower, often a hagraven lair.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main_potential", "magical_properties_tainted_by_dark_magic", "dungeon_minor", "terrain_forest_south_falkreath", "ritual_site_dark_magic_hagraven", "monster_den_hagraven"],
                "exit_label_from_parent": "Path to Tower",
                "exit_label_to_parent": "Leave Tower Area"
            },
            {
                "id": 50003,
                "name": "Roadside Ruins",
                "desc": "Crumbling Nordic ruins along the road in Falkreath Hold, sometimes attracting spriggans guarding their territory or bandits lying in ambush.",
                "travel_desc": "Crumbling Nordic ruins along the road.",
                "tags": ["structure_type_ruined_shrine_nordic", "nordic_burial_site_minor_potential", "roadside_encounter_point", "monster_den_spriggan_potential", "bandit_minor_camp_potential_ambush", "structure_condition_ruined_extensively", "exploration_point_minor_ruin"],
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 50004,
                "name": "Sunderstone Gorge",
                "desc": "A large cave system in the southern mountains of Falkreath, housing an ancient Word Wall and various magical inhabitants, including fire-wielding mages or atronachs.",
                "travel_desc": "Large cave system with a Word Wall and magical inhabitants.",
                "tags": ["structure_type_natural_cave_gorge", "dungeon_major", "specific_landmark_type_word_wall_location", "magical_properties_elemental_fire_dominant", "monster_den_fire_atronach", "mage_lair_hostile_fire_mages", "terrain_southern_falkreath_mountains", "exploration_challenge_elemental_hazard"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Gorge"
            },
            {
                "id": 50005,
                "name": "Cracked Tusk Keep",
                "desc": "A ruined fort in Falkreath Hold, now occupied by a fierce band of Orc bandits. Rumor has it they guard a fragment of a powerful Daedric artifact.",
                "travel_desc": "Ruined fort occupied by Orc bandits, guards Daedric artifact fragment.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold_orc", "orc_presence_hostile_bandits", "dungeon_major", "quest_location_daedric_mehrunes_razor_pieces", "artifact_location_daedric_razor_pieces", "state_or_condition_current_bandit_controlled_area_orc"],
                "exit_label_from_parent": "Keep Entrance",
                "exit_label_to_parent": "Exit Keep"
            },
            {
                "id": 50006,
                "name": "Angi's Camp",
                "desc": "A secluded cabin in the southern mountains of Falkreath, home to Angi, a skilled archer offering training to those who find her.",
                "travel_desc": "Secluded cabin, home to Angi, a skilled archer.",
                "tags": ["structure_type_shack_or_hut_cabin", "hermit_lair_archer_angi", "skill_trainer_archery_expert", "terrain_mountainous_southern_falkreath", "state_or_condition_current_isolated_and_forgotten", "hunter_gathering_spot_secluded", "quest_giver_potential_archery_training"],
                "exit_label_from_parent": "Path to Camp",
                "exit_label_to_parent": "Leave Camp"
            },
            {
                "id": 50007,
                "name": "Fort Neugrad",
                "desc": "A large Imperial fort near the Cyrodiilic border, guarding a key mountain pass. Currently well-garrisoned and a symbol of Imperial authority in the region.",
                "travel_desc": "Large Imperial fort guarding pass to Cyrodiil.",
                "tags": ["structure_type_fortified_keep_imperial", "military_presence_imperial_legion_garrison", "imperial_influence_strong_border_fort", "cyrodiil_border_region_pass_guard", "dungeon_major", "state_or_condition_current_contested_by_factions_potential_stormcloak", "civil_war_quest_historic_site_potential", "strategic_location_border_pass"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 50008,
                "name": "Lake Ilinalta",
                "desc": "A large, deep lake in western Falkreath Hold, shrouded in mist and legend. Its depths are said to hold ancient secrets and perhaps even a sunken ruin.",
                "travel_desc": "Large, deep lake shrouded in mist and legend.",
                "tags": ["terrain_lake_large_deep_misty", "climate_temperate", "cultural_historical_significance_local_legend_sunken_ruin", "structure_type_ruined_fort_submerged_potential_ilinaltas_deep", "economic_activity_fishing_industry_local", "unique_natural_formation_lake", "quest_location_daedric_azura_star_related_interior_ruin"],
                "exit_label_from_parent": "Path to Lakeshore",
                "exit_label_to_parent": "Leave Lakeshore",
                "sub_locations": [
                    {
                        "id": 500081,
                        "name": "Ilinalta's Deep",
                        "desc": "The treacherous, flooded ruins of an ancient fort or temple within Lake Ilinalta, rumored to be haunted and guarded by necromancers or dark creatures.",
                        "travel_desc": "Flooded ruins within Lake Ilinalta, guarded by necromancers.",
                        "tags": ["structure_type_ruined_fort_submerged_temple_potential", "specific_landmark_type_necromancer_lair", "undead_presence_strong_skeletons_necromancers", "dungeon_major", "quest_location_daedric_azura_star_broken", "magical_properties_tainted_by_dark_magic", "structure_condition_flooded_treacherous", "boss_fight_necromancer_powerful_potential"],
                        "exit_label_from_parent": "Ruin Entrance",
                        "exit_label_to_parent": "Exit Ruin"
                    }
                ]
            },
            {
                "id": 50009,
                "name": "The Lady Stone",
                "desc": "A Standing Stone located on an island in Lake Ilinalta, granting enhanced health and stamina regeneration.",
                "travel_desc": "Standing Stone on an island, enhances regeneration.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive_regenerative", "terrain_island_lake_ilinalta", "cultural_historical_significance_ancient_magical_site", "buff_health_regen_increased", "buff_stamina_regen_increased", "power_regenerative_passive"],
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 50010,
                "name": "Hunter's Rest Clearing",
                "desc": "A small, secluded clearing deep in the forests of Falkreath, often used by hunters as a temporary camp. Signs of recent use are common.",
                "travel_desc": "Secluded clearing, often used by hunters.",
                "tags": ["hunter_gathering_spot_camp", "environment_wilderness", "terrain_forest_deep_falkreath", "secluded_nature_spot", "bandit_minor_camp_potential_temporary", "exploration_point_minor"],
                "exit_label_from_parent": "Path to Clearing",
                "exit_label_to_parent": "Leave Clearing"
            },
            {
                "id": 50011,
                "name": "Wolfstooth Den",
                "desc": "A shallow cave system within Falkreath's dense woods, currently serving as a den for a pack of territorial wolves.",
                "travel_desc": "Shallow cave system, den for territorial wolves.",
                "tags": ["structure_type_natural_cave_shallow", "monster_den_wolf_pack_major", "terrain_forest_dense_falkreath", "dungeon_minor", "animal_den_wolf_territorial", "alchemy_ingredient_source_rich_wolf_pelts"],
                "exit_label_from_parent": "Den Entrance",
                "exit_label_to_parent": "Exit Den"
            },
            {
                "id": 50012,
                "name": "Half-Moon Mill",
                "desc": "A lumber mill owned by Hert and Hern, a reclusive couple. Rumors persist about their nocturnal activities and connections to darker elements.",
                "travel_desc": "Lumber mill owned by a reclusive couple, rumors persist.",
                "tags": ["structure_type_lumber_mill_site", "settlement_minor", "economic_activity_logging_timber", "specific_landmark_type_vampire_coven_minor_potential_owners_hert_hern", "isolated_location_lake_ilinalta_shore", "mystery_local_nocturnal_activities", "quest_location_dark_brotherhood_target_potential"],
                "exit_label_from_parent": "Path to Mill",
                "exit_label_to_parent": "Leave Mill"
            },
            {
                "id": 50013,
                "name": "Granitehall Farm",
                "desc": "A small, hardy farm nestled near the mountains of Falkreath, known for its resilient goats and strong mead.",
                "travel_desc": "Small, hardy farm known for resilient goats and strong mead.",
                "tags": ["structure_type_farmstead_hardy", "economic_activity_farming_livestock_goats", "economic_activity_brewing_mead_ale_strong", "terrain_mountainous_falkreath", "isolated_location", "settlement_minor", "unique_produce_goat_cheese_mead"],
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 50014,
                "name": "Shadowed Path Cave",
                "desc": "A dark, winding cave often used by smugglers as a discreet route through Falkreath's forests, or as a den for bears and other forest predators.",
                "travel_desc": "Dark, winding cave used by smugglers or predators.",
                "tags": ["structure_type_natural_cave_winding", "terrain_forest_falkreath", "dungeon_minor", "economic_activity_smuggling_route_active_potential", "monster_den_bear_potential", "monster_den_wolf_potential", "exploration_point_hidden_path"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 50015,
                "name": "Crumbling Border Watch",
                "desc": "The ruins of a small Imperial watchtower near the Cyrodiil border in Falkreath Hold, now overgrown and sometimes used by bandits as a lookout.",
                "travel_desc": "Ruined Imperial watchtower near Cyrodiil border.",
                "tags": ["structure_type_ruined_tower_imperial_watchtower", "military_presence_historic_imperial", "terrain_mountainous_cyrodiil_border", "structure_condition_ruined_extensively_overgrown", "bandit_minor_camp_potential_lookout", "cyrodiil_border_region", "exploration_point_historic_ruin"],
                "exit_label_from_parent": "Path to Ruin",
                "exit_label_to_parent": "Leave Ruin"
            },
            {
                "id": 50018,
                "name": "South Skybound Watch",
                "desc": "A ruined Nordic watchtower and barrow complex, similar to its northern counterpart, located in the southern mountains of Falkreath Hold. It contains an ancient Word Wall and is guarded by draugr.",
                "travel_desc": "Ruined Nordic watchtower and barrow with a Word Wall.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_major_complex", "specific_landmark_type_word_wall_location", "dungeon_major", "undead_presence_strong", "draugr_heavy", "terrain_mountainous_southern_falkreath", "cultural_historical_significance_nordic_ancient_site"],
                "exit_label_from_parent": "Path to Watchtower",
                "exit_label_to_parent": "Leave Watchtower"
            },
            {
                "id": 50019, 
                "name": "Shor's Watchtower",
                "desc": "A ruined watchtower near the border of Falkreath and The Rift, overlooking the road to Shor's Stone. Often occupied by bandits.",
                "travel_desc": "Ruined watchtower overlooking road to Shor's Stone.",
                "tags": ["structure_type_ruined_tower_watchtower", "bandit_minor_camp_potential", "roadside_ruin_falkreath_rift_border", "strategic_lookout_decayed_shors_stone_road", "dungeon_minor"],
                "exit_label_from_parent": "Path to Tower",
                "exit_label_to_parent": "Leave Tower Area"
            },
            {
                "id": 50020,
                "name": "Bleakwind Basin",
                "desc": "A large, open basin in Falkreath Hold, west of Whiterun, known as a traditional gathering place for giants and their mammoth herds.",
                "travel_desc": "Large basin, traditional gathering place for giants.",
                "tags": ["specific_landmark_type_giant_camp_established_major", "mammoth_herd_grazing", "terrain_plains_open_basin_falkreath_whiterun_border", "neutral_encounter_giant_mammoth_large_group", "cultural_historical_significance_giant_gathering_place"],
                "exit_label_from_parent": "Path to Basin",
                "exit_label_to_parent": "Leave Basin"
            },
            {
                "id": 50021, 
                "name": "Shor's Watchtower", # Note: Duplicate name, assuming distinct location due to ID
                "desc": "A ruined watchtower near the border of Falkreath and The Rift, overlooking the road to Shor's Stone. Often occupied by bandits.",
                "travel_desc": "Ruined watchtower, often bandit-occupied.",
                "tags": ["structure_type_ruined_tower_watchtower", "bandit_minor_camp_potential", "roadside_ruin_falkreath_rift_border", "strategic_lookout_decayed_shors_stone_road", "dungeon_minor"],
                "exit_label_from_parent": "Path to Tower",
                "exit_label_to_parent": "Leave Tower Area"
            },
            {
                "id": 50022,
                "name": "Bannermist Tower",
                "desc": "A ruined watchtower south of Lake Ilinalta in Falkreath Hold, now occupied by bandits who use it to prey on travelers.",
                "travel_desc": "Ruined watchtower occupied by bandits.",
                "tags": ["structure_type_ruined_tower_watchtower", "bandit_minor_camp", "dungeon_minor", "roadside_danger_spot_lake_ilinalta_south", "state_or_condition_current_bandit_controlled_area"],
                "exit_label_from_parent": "Path to Tower",
                "exit_label_to_parent": "Leave Tower Area"
            },
            {
                "id": 50023,
                "name": "Anise's Cabin",
                "desc": "A small, seemingly innocent cabin located near Riverwood, on the edge of Falkreath Hold. Anise is an elderly woman with a hidden cellar revealing her dabbling in witchcraft.",
                "travel_desc": "Small cabin with a hidden cellar revealing witchcraft.",
                "tags": ["structure_type_shack_or_hut_cabin", "witch_coven_potential_hidden_cellar", "secret_location_witchcraft_lair", "alchemy_ingredient_source_rich_cabin_cellar", "neutral_encounter_secret_hostile_potential_anise", "quest_giver_potential_minor_task_or_threat", "terrain_forested_area_edge_riverwood_falkreath"],
                "exit_label_from_parent": "Path to Cabin",
                "exit_label_to_parent": "Leave Cabin Area"
            }
        ]
    }
]