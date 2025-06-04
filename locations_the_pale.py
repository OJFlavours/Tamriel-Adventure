from locations_dawnstar_city import DAWNSTAR_CITY_LOCATIONS

THE_PALE_LOCATIONS = [
    # THE PALE
    {
        "id": 2,
        "name": "The Pale",
        "desc": "A frozen hold of bleak beauty, stretching from snow-tipped plains to the Sea of Ghosts. Harsh and unforgiving, known for its mining town of Dawnstar and dangerous wildlife. Strong Stormcloak sentiment prevails here.",
        "travel_desc": "Frozen hold of bleak beauty, known for Dawnstar and dangerous wildlife.",
        "tags": ["hold", "climate_arctic", "terrain_ice_field", "terrain_tundra_plains", "environment_coastal", "economic_activity_mining_quicksilver", "economic_activity_mining_iron", "nordic_culture_strong", "stormcloak_presence_strong_leaning", "state_or_condition_current_isolated_and_forgotten", "dangerous_wildlife_ice_wraiths_trolls", "travel_hub_sea_northern_ports_potential"],
       "context_tags": ["exterior", "hold_region", "arctic_region"],
       "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {
            "links": [
                {"name": "Whiterun Hold", "connection_type": "Road"},
                {"name": "Winterhold", "connection_type": "Road"},
                {"name": "Eastmarch", "connection_type": "Road"},
                {"name": "Hjaalmarch", "connection_type": "Road"},
                {"name": "Icespire Trail", "connection_type": "Path"},
                {"name": "Frostmere Road", "connection_type": "Path"}
            ]
        },
        "sub_locations": [
            {
                "id": 20,
                "name": "Dawnstar",
                "desc": "A resilient port town on the northern coast, thriving on fishing and mining. It is currently plagued by mysterious nightmares affecting its populace.",
                "travel_desc": "Resilient port town plagued by mysterious nightmares.",
                "tags": ["populated_town", "settlement_features_docks_harbor", "city_affiliation_dawnstar_town", "state_or_condition_current_isolated_and_forgotten", "economic_activity_mining_quicksilver", "economic_activity_fishing_industry_local", "urban_issues_or_atmosphere_haunted_rumors_strong_nightmares", "daedric_influence_subtle_rumor_vaermina", "settlement_features_jarls_longhouse", "climate_arctic", "environment_coastal", "quest_location_daedric_vaermina_nightmares"],
               "context_tags": ["exterior", "urban_town", "coastal_town"],
               "exit_label_from_parent": "Town Gates",
                "exit_label_to_parent": "Town Gates",
                "sub_locations": DAWNSTAR_CITY_LOCATIONS
            },
            {
                "id": 21,
                "name": "Nightcaller Temple",
                "desc": "An eerie, abandoned temple on a clifftop overlooking Dawnstar. It is sealed, but dark whispers and nightmares emanate from it, hinting at the Daedric Prince Vaermina's influence.",
                "travel_desc": "Eerie, abandoned temple, source of dark whispers.",
                "tags": ["structure_type_temple_building_ruined", "structure_condition_ruined_extensively_sealed", "magical_properties_daedric_influence_overt_vaermina", "dungeon_major", "quest_location_daedric_vaermina_skull_of_corruption", "urban_issues_or_atmosphere_haunted_rumors_strong_nightmares_source", "specific_landmark_type_daedric_shrine_prominent", "terrain_cliffside_overlook"],
                "exit_label_from_parent": "Temple Entrance",
                "context_tags": ["exterior", "daedric_ruin", "vaermina"],
                "exit_label_to_parent": "Exit Temple"
            },
            {
                "id": 22,
                "name": "Iron-Breaker Mine",
                "desc": "An iron mine located just outside Dawnstar, contributing to the town's resources.",
                "travel_desc": "Iron mine just outside Dawnstar.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "resource_node_iron", "dawnstar_outskirts", "economic_support_local"],
                "exit_label_from_parent": "Mine Entrance",
                "context_tags": ["exterior", "mine_site", "iron"],
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 23,
                "name": "Wreck of the Brinehammer",
                "desc": "The ghostly remains of a long-forgotten shipwreck scattered along the storm-battered coast south of Dawnstar. Rumored to hold lost treasures and spectral guardians.",
                "travel_desc": "Ghostly remains of a shipwreck, rumored lost treasures.",
                "tags": ["structure_type_shipwreck_site", "structure_condition_ruined_extensively_scattered", "dungeon_minor", "environment_coastal_storm_battered", "undead_presence_rumored_strong_ghosts_skeletons", "treasure_cache_rumored_lost_cargo", "exploration_point_historic_wreck"],
                "exit_label_from_parent": "Path to Wreck",
                "context_tags": ["exterior", "coastal_ruin", "shipwreck"],
                "exit_label_to_parent": "Leave Wreck Area"
            },
            {
                "id": 24,
                "name": "Frostflow Lighthouse",
                "desc": "A solitary lighthouse west of Dawnstar. Its light has recently gone out, and chilling screams were heard from within. A dark mystery involving Falmer awaits discovery.",
                "travel_desc": "Solitary lighthouse, light gone out, chilling screams heard.",
                "tags": ["structure_type_lighthouse_structure", "structure_condition_abandoned_light_extinguished", "dungeon_major", "falmer_presence_strong", "quest_location_investigation_family_tragedy", "tragedy_site_family_massacre", "chaurus_nest_major_potential", "urban_issues_or_atmosphere_haunted_rumors_strong_screams"],
                "exit_label_from_parent": "Lighthouse Door",
                "context_tags": ["exterior", "coastal_structure", "ruin_type"],
                "exit_label_to_parent": "Exit Lighthouse"
            },
            {
                "id": 25,
                "name": "Loreius Farm",
                "desc": "A small farmstead south of Dawnstar, owned by Vantus Loreius, often struggling against the harsh climate.",
                "travel_desc": "Small farmstead struggling against harsh climate.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_struggling", "state_or_condition_current_isolated_and_forgotten", "climate_arctic_edge", "settlement_minor", "quest_giver_potential_local_issues_cicero_related_potential"],
                "exit_label_from_parent": "Path to Farm",
                "context_tags": ["exterior", "rural_area", "farmstead"],
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 26,
                "name": "Nightgate Inn",
                "desc": "A remote and somewhat lonely inn nestled in a snowy pass between The Pale and Eastmarch. Run by the old Orc, Hadring, it offers a rare point of shelter for weary travelers braving the harsh northern roads. The atmosphere is quiet, with only a few hardy patrons usually present, and Hadring himself is a man of few words but might have tasks for those willing to venture into the surrounding wilderness.",
                "travel_desc": "Isolated inn run by Hadring, a refuge in a snowy pass.",
                "tags": ["structure_type_inn_building", "settlement_features_tavern", "state_or_condition_current_isolated_and_forgotten", "travel_route_marker_mountain_pass", "lodging_available", "food_drink_vendor", "rumor_source_travelers", "quest_giver_potential_local_issues_orc_related_potential", "location_specific_nightgate_inn"],
                "context_tags": ["interior", "rural_area", "tavern_type", "safe_zone"],
                "demographics": {"Nord": 70, "Imperial": 10, "Orc": 10, "Khajiit": 5, "Dunmer": 5},
                "fixed_npcs": [
                    {"name": "Hadring", "race": "Orc", "role": "innkeeper", "level": 9}
                ],
                "exit_label_from_parent": "Inn Door",
                "exit_label_to_parent": "Exit Inn"
            },
            {
                "id": 27,
                "name": "Red Road Pass",
                "desc": "A bandit-infested pass through the mountains in the southern part of The Pale, dangerous for unwary travelers.",
                "travel_desc": "Bandit-infested mountain pass, dangerous for travelers.",
                "tags": ["terrain_mountain_pass", "bandit_main_stronghold", "dungeon_major", "travel_route_alternative_dangerous", "state_or_condition_current_bandit_controlled_area", "quest_location_bounty_leader_potential"],
                "exit_label_from_parent": "Enter Pass",
                "context_tags": ["exterior", "mountain_pass", "bandit_area"],
                "exit_label_to_parent": "Exit Pass"
            },
            {
                "id": 28,
                "name": "Shearpoint",
                "desc": "A mountain peak in The Pale, home to an ancient dragon lair, a Word Wall, and the tomb of the Dragon Priest Krosis.",
                "travel_desc": "Mountain peak with dragon lair, Word Wall, and Krosis's tomb.",
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "cultural_historical_significance_dragon_cult_lair_priest_krosis", "terrain_mountain_peak", "dungeon_major", "undead_presence_strong_draugr_priest", "artifact_location_powerful_mask_krosis", "dragon_presence_potential_guardian"],
                "exit_label_from_parent": "Path to Peak",
                "context_tags": ["exterior", "mountain_peak", "dragon_lair"],
                "exit_label_to_parent": "Leave Peak Area"
            },
            {
                "id": 29,
                "name": "Shrouded Grove",
                "desc": "A small, hidden grove in The Pale, sometimes a site for unusual encounters, minor Daedric worship, or hidden alchemical ingredients.",
                "travel_desc": "Small, hidden grove, site of unusual encounters.",
                "tags": ["environment_wilderness_grove", "terrain_forest_hidden", "magical_properties_enchanted_neutral_subtle", "ritual_site_minor_potential_daedric_nature", "alchemy_ingredient_source_rich_rare_flora", "secluded_nature_spot", "mystery_local_unusual_encounters"],
                "exit_label_from_parent": "Path to Grove",
                "context_tags": ["exterior", "wilderness_area", "grove"],
                "exit_label_to_parent": "Leave Grove"
            },
            {
                "id": 20001,
                "name": "Silverdrift Lair",
                "desc": "A Nordic ruin west of Nightgate Inn, overrun by draugr and ancient guardians.",
                "travel_desc": "Nordic ruin overrun by draugr.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "cultural_historical_significance_nordic_ancient_site", "treasure_cache_rumored_ancient_nordic", "puzzle_ancient_nordic_potential"],
                "exit_label_from_parent": "Lair Entrance",
                "context_tags": ["exterior", "nordic_ruin", "dungeon"],
                "exit_label_to_parent": "Exit Lair"
            },
            {
                "id": 20002,
                "name": "Weynon Stones",
                "desc": "A small ruin southeast of Dawnstar, a circle of ancient stones that hum with faint magical energy, sometimes attracting bandits or mages.",
                "travel_desc": "Small ruin, circle of ancient stones humming with energy.",
                "tags": ["structure_type_standing_stone_circle_ruined", "cultural_historical_significance_ancient_magical_site_minor", "magical_properties_arcane_nexus_minor_faint", "bandit_minor_camp_potential", "mage_lair_hostile_potential_minor", "terrain_tundra_plains", "exploration_point_minor_lore"],
                "context_tags": ["exterior", "ruin", "standing_stones"],
                "exit_label_from_parent": "Path to Stones",
                "exit_label_to_parent": "Leave Stones Area"
            },
            {
                "id": 20003,
                "name": "Fort Dunstad",
                "desc": "A large fort in The Pale, strategically important. Currently garrisoned by Imperial soldiers, but its loyalty could shift with the rising political tensions.",
                "travel_desc": "Large, strategically important fort garrisoned by Imperials.",
                "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion", "imperial_influence_strong", "dungeon_major", "state_or_condition_current_contested_by_factions_potential_stormcloak", "civil_war_quest_historic_site_potential", "strategic_location_pale"],
                "context_tags": ["exterior", "imperial_fort", "fort"],
                "exit_label_from_parent": "Fort Gates",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 20004,
                "name": "Windward Ruins",
                "desc": "Crumbling Nordic ruins on a windswept hill overlooking the Sea of Ghosts, rumored to be haunted by sailors lost to the ice.",
                "travel_desc": "Crumbling Nordic ruins, rumored haunted by lost sailors.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_minor_potential", "environment_coastal_windswept_hill", "structure_condition_ruined_extensively", "magical_properties_haunted_aura_sailors_lost", "undead_presence_skeletons_ghosts_potential", "dungeon_minor", "exploration_point_historic_ruin"],
                "exit_label_from_parent": "Path to Ruins",
                "context_tags": ["exterior", "nordic_ruin", "coastal_ruin"],
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 20005,
                "name": "Pale Pass",
                "desc": "A treacherous mountain pass leading towards Cyrodiil from the southern Pale, known for blizzards and ice trolls. Currently lightly patrolled by Imperials.",
                "travel_desc": "Treacherous mountain pass to Cyrodiil, known for blizzards.",
                "tags": ["terrain_mountain_pass_treacherous", "cultural_historical_significance_historic_site_cyrodiil_border", "state_or_condition_current_contested_by_factions_potential_stormcloak", "imperial_influence_moderate_patrols", "monster_den_ice_troll_major", "climate_arctic_blizzards", "travel_route_major_dangerous_cyrodiil"],
                "context_tags": ["exterior", "mountain_pass", "border_pass"],
                "exit_label_from_parent": "Enter Pass",
                "exit_label_to_parent": "Exit Pass"
            },
            {
                "id": 20006,
                "name": "Great Henge of the Ice-Speakers",
                "desc": "An ancient and massive stone circle on the northern tundra, believed to have been used by early Atmoran settlers for sky-worship. Rarely visited.",
                "travel_desc": "Ancient, massive stone circle used for sky-worship.",
                "tags": ["structure_type_standing_stone_circle_massive", "cultural_historical_significance_nordic_ancient_site_atmoran_sky_worship", "magical_properties_arcane_nexus_minor_ancient", "state_or_condition_current_isolated_and_forgotten_rarely_visited", "terrain_tundra_plains_northern", "climate_arctic", "exploration_point_major_lore"],
                "exit_label_from_parent": "Path to Henge",
                "context_tags": ["exterior", "ancient_site", "standing_stones"],
                "exit_label_to_parent": "Leave Henge Area"
            },
            {
                "id": 20007,
                "name": "Snowpoint Overlook Cave",
                "desc": "A small ice cave high in the mountains of The Pale, offering a chilling view. It might be used by smugglers or serve as a den for ice wraiths.",
                "travel_desc": "Small ice cave offering a chilling view.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial", "economic_activity_smuggling_route_active_potential", "monster_den_ice_wraith", "terrain_mountain_peak_high", "dungeon_minor", "scenic_vista_panoramic_chilling", "exploration_point_hidden_cache_potential"],
                "exit_label_from_parent": "Cave Entrance",
                "context_tags": ["exterior", "ice_cave", "overlook"],
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 20008,
                "name": "Forgotten Stones of the North",
                "desc": "A small, weathered circle of ancient stones on the tundra of The Pale. Their original purpose is lost to time, but they emanate a faint, cold energy.",
                "travel_desc": "Small, weathered circle of ancient stones.",
                "tags": ["structure_type_standing_stone_circle_weathered", "cultural_historical_significance_nordic_ancient_site_lost_purpose", "structure_condition_weathered_ancient", "terrain_tundra_plains", "magical_properties_enchanted_neutral_faint_cold_energy", "mystery_local_lost_history", "exploration_point_minor_lore"],
                "exit_label_from_parent": "Path to Stones",
                "context_tags": ["exterior", "ancient_site", "standing_stones"],
                "exit_label_to_parent": "Leave Stones Area"
            },
            {
                "id": 20009,
                "name": "Icerunner's Rest",
                "desc": "A tiny, wind-battered fishing hamlet clinging to the icy northern coast of The Pale. Its few inhabitants are hardy folk, accustomed to the harsh sea.",
                "travel_desc": "Tiny, wind-battered fishing hamlet.",
                "tags": ["populated_village_hamlet", "settlement_minor_fishing", "economic_activity_fishing_industry_local_subsistence", "environment_coastal_icy_northern", "climate_glacial_harsh", "state_or_condition_current_isolated_and_forgotten_hardy_folk"],
                "exit_label_from_parent": "Path to Hamlet",
                "context_tags": ["exterior", "coastal_village", "fishing_village"],
                "exit_label_to_parent": "Leave Hamlet"
            },
            {
                "id": 20010,
                "name": "Snowdrift Cabin",
                "desc": "A solitary trapper's cabin, half-buried in snowdrifts for much of the year, located deep within the snowy plains of The Pale.",
                "travel_desc": "Solitary trapper's cabin, half-buried in snow.",
                "tags": ["structure_type_shack_or_hut_trapper", "structure_condition_weathered_snow_buried", "economic_activity_hunting_furs_meat_trapping", "climate_arctic_deep_snow", "terrain_tundra_plains_isolated", "hermit_lair_potential_trapper"],
                "context_tags": ["exterior", "tundra", "cabin"],
                "exit_label_from_parent": "Path to Cabin",
                "exit_label_to_parent": "Leave Cabin Area"
            },
            {
                "id": 20011,
                "name": "Frostmoon Crag Cave",
                "desc": "An icy cave system high on a crag in The Pale, often glittering with frost and home to ice wraiths or frost trolls.",
                "travel_desc": "Icy cave system, home to ice wraiths or frost trolls.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial_frosty", "dungeon_minor", "monster_den_frost_troll", "monster_den_ice_wraith", "terrain_mountain_peak_crag", "alchemy_ingredient_source_rich_frost_salts_potential"],
                "context_tags": ["exterior", "ice_cave", "mountain_area"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 20012,
                "name": "Ruins of the Lost Patrol",
                "desc": "A scatter of weathered stones and a broken standard on the bleak tundra, marking the last stand of a forgotten Imperial or Stormcloak patrol from a past conflict.",
                "travel_desc": "Weathered stones marking last stand of a forgotten patrol.",
                "tags": ["structure_type_ruined_settlement_battle_marker", "cultural_historical_significance_battlefield_historic_forgotten_patrol", "magical_properties_haunted_aura_potential_lost_soldiers", "terrain_tundra_plains_bleak", "state_or_condition_current_isolated_and_forgotten", "exploration_point_historic_remnants"],
                "exit_label_from_parent": "Path to Ruins",
                "context_tags": ["exterior", "battlefield", "ruin"],
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 20013,
                "name": "Yorgrim's Overlook",
                "desc": "The crumbling ruins of an ancient Nordic watchtower, named after a forgotten hero. It offers a commanding view of the surrounding tundra but is now home to bandits or wildlife.",
                "travel_desc": "Crumbling ruins of an ancient Nordic watchtower.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_minor_potential", "dungeon_minor", "bandit_minor_camp_potential", "monster_den_wildlife_potential", "scenic_vista_panoramic_tundra_view", "cultural_historical_significance_nordic_ancient_site_hero_yorgrim"],
                "context_tags": ["exterior", "nordic_ruin", "overlook"],
                "exit_label_from_parent": "Path to Overlook",
                "exit_label_to_parent": "Leave Overlook"
            },
            {
                "id": 20014,
                "name": "Stillborn Cave (The Pale)",
                "desc": "A small, cold cave system in The Pale, named for a local tragedy or perhaps the eerie silence within. Often inhabited by frost spiders or other cold-dwelling creatures.",
                "travel_desc": "Small, cold cave system, named for local tragedy.",
                "tags": ["structure_type_natural_cave_cold", "climate_arctic", "dungeon_minor", "monster_den_frost_spider", "urban_issues_or_atmosphere_haunted_rumors_strong_eerie_silence", "tragedy_site_minor_local_legend", "alchemy_ingredient_source_rich_frostbite_venom_potential"],
                "context_tags": ["exterior", "ice_cave", "dungeon"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 20015,
                "name": "The Lord Stone",
                "desc": "Found high in the mountains on the border of The Pale, east of Morthal, this Standing Stone grants increased physical resilience and resistance to magical attacks.",
                "travel_desc": "Standing Stone granting increased physical and magic resistance.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive_defensive", "terrain_mountain_peak_border_pale_hjaalmarch", "cultural_historical_significance_ancient_magical_site", "climate_arctic_alpine", "buff_physical_resistance_increased", "buff_magic_resistance_increased"],
                "context_tags": ["exterior", "standing_stone", "magical_site"],
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 20016,
                "name": "Korvanjund",
                "desc": "A large Nordic ruin in The Pale, south of Dawnstar. It is an ancient burial site of Nord heroes and kings, rumored to hold significant historical artifacts, possibly including a crown of legend. Heavily guarded by draugr.",
                "travel_desc": "Large Nordic ruin, ancient burial site of heroes and kings.",
                "tags": ["nordic_burial_site_major_royal_tomb", "dungeon_major", "undead_presence_strong", "draugr_heavy_heroes_kings", "cultural_historical_significance_nordic_ancient_site_heroes_kings", "quest_location_civil_war_jagged_crown", "specific_landmark_type_word_wall_location_potential", "artifact_location_rumored_jagged_crown", "puzzle_ancient_nordic_potential"],
                "context_tags": ["exterior", "nordic_ruin", "dungeon"],
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 20017,
                "name": "Irkngthand",
                "desc": "A massive and ancient Dwemer ruin in The Pale, west of Nightgate Inn. It is a sprawling complex with many dangers, including Falmer and Dwemer constructs. Rumored to hold significant Dwemer artifacts.",
                "travel_desc": "Massive Dwemer ruin with Falmer and constructs.",
                "tags": ["dwemer_ruin_major_city_complex", "dungeon_large_complex", "falmer_presence_strong", "mechanical_constructs_dwemer_heavy", "quest_location_thieves_guild_eyes_of_falmer", "cultural_historical_significance_dwemer_ruin_site", "specific_landmark_type_blackreach_elevator_access_potential", "chaurus_nest_major_potential", "ancient_technology_dwemer", "treasure_cache_dwemer_artifacts_rumored"],
                "context_tags": ["exterior", "dwemer_ruin", "dungeon"],
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 20018,
                "name": "Duskglow Crevice",
                "desc": "A dark, winding cave system in The Pale, south of Dawnstar, infested with Falmer and their chaurus companions. It is a dangerous place, shunned by locals.",
                "travel_desc": "Dark, winding cave system infested with Falmer.",
                "tags": ["structure_type_natural_cave_crevice", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_major", "environment_underground_dark_winding", "state_or_condition_current_lawless_area_dangerous", "alchemy_ingredient_source_rich_falmer_ears_chaurus_eggs"],
                "context_tags": ["exterior", "falmer_cave", "dungeon"],
                "exit_label_from_parent": "Crevice Entrance",
                "exit_label_to_parent": "Exit Crevice"
            }
        ]
    }
]