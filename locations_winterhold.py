from locations_winterhold_city import WINTERHOLD_CITY_LOCATIONS

WINTERHOLD_LOCATIONS = [
    # WINTERHOLD HOLD
    {
        "id": 3,
        "name": "Winterhold Hold",
        "desc": "A shattered hold on the northern coast, defined by icy gales, ancient ruins, and the dominant presence of the College of Winterhold. Much of the original city was lost to the Great Collapse centuries ago.",
        "travel_desc": "Shattered northern hold, home to the College of Winterhold.",
        "tags": ["hold", "climate_glacial_extreme_weather", "terrain_ice_field_coastal", "environment_coastal_northern", "magical_properties_arcane_nexus_college", "cultural_historical_significance_great_collapse_affected_site_major", "nordic_culture_ancient_remnants", "faction_college_of_winterhold_dominant_presence", "state_or_condition_current_economically_depressed_shattered", "structure_condition_ruined_extensively_city_lost", "travel_hub_sea_northern_ports_historic_potential"],
        "density": "sparse",
        "demographics": {"Nord": 75, "Altmer": 10, "Dunmer": 10, "Others": 5},
        "travel": {
            "links": [
                {"name": "The Pale", "connection_type": "Road"},
                {"name": "Eastmarch", "connection_type": "Road"},
                {"name": "Saarthal Trail", "connection_type": "Path"},
                {"name": "Glacial Path", "connection_type": "Path"},
                {"name": "Sea of Ghosts Ice Floes (dangerous)", "connection_type": "Sea Route"}
            ]
        },
        "sub_locations": [
            *WINTERHOLD_CITY_LOCATIONS,  # Unpack the city locations here
            {
                "id": 31,
                "name": "Saarthal",
                "desc": "The excavated ruins of one of Skyrim's first human settlements, a site of great magical power and ancient Nordic mysteries, closely tied to the College of Winterhold's studies.",
                "travel_desc": "Excavated ruins of an early human settlement.",
                "tags": ["nordic_burial_site_major_excavated", "dungeon_major", "undead_presence_strong", "draugr_heavy", "magical_properties_arcane_nexus_powerful", "faction_college_of_winterhold_related_quest_excavation", "cultural_historical_significance_nordic_ancient_site_first_settlement", "artifact_location_powerful_eye_of_magnus_related", "puzzle_ancient_magic_nordic", "quest_location_college_of_winterhold_early"],
                "density": "average",
                "exit_label_from_parent": "Excavation Entrance",
                "exit_label_to_parent": "Exit Excavation"
            },
            {
                "id": 32,
                "name": "Hob's Fall Cave",
                "desc": "A shadowy coastal cave north of Winterhold, a den for necromancers and their unholy experiments, or perhaps desperate smugglers.",
                "travel_desc": "Shadowy coastal cave, den for necromancers or smugglers.",
                "tags": ["structure_type_natural_cave_coastal", "specific_landmark_type_necromancer_lair_potential", "economic_activity_smuggling_route_active_potential", "dungeon_minor", "environment_coastal_northern", "magical_properties_tainted_by_dark_magic_potential", "undead_presence_skeletons_potential", "mage_lair_hostile_potential_necromancer", "quest_giver_potential_purity_of_essence_potion"],
                "density": "average",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 33,
                "name": "Yngol Barrow",
                "desc": "A mournful Nordic tomb east of Windhelm (close to Winterhold's border), where ancient magics linger and the ghost of Yngol's shade may be found by those seeking its secrets.",
                "travel_desc": "Mournful Nordic tomb where ancient magics linger.",
                "tags": ["nordic_burial_site_major_mournful", "dungeon_major", "undead_presence_strong_ghosts_draugr", "magical_properties_haunted_aura_strong", "cultural_historical_significance_legendary_hero_location_ysgramor_son_yngol", "artifact_location_unique_item_helm_of_yngol", "puzzle_ancient_nordic_coral_claw_potential", "quest_location_investigation_legend"],
                "density": "average",
                "exit_label_from_parent": "Barrow Entrance",
                "exit_label_to_parent": "Exit Barrow"
            },
            {
                "id": 34,
                "name": "Alftand",
                "desc": "A vast and treacherous Dwemer ruin deep within the mountains of Winterhold, one of the primary known entrances to the subterranean realm of Blackreach. It is a dangerous place, still patrolled by ancient constructs and inhabited by Falmer.",
                "travel_desc": "Vast Dwemer ruin, entrance to Blackreach.",
                "tags": ["dwemer_ruin_major_city_complex", "dungeon_large_complex_treacherous", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "specific_landmark_type_blackreach_elevator_access", "quest_location_main_story_elder_scroll_potential", "cultural_historical_significance_dwemer_ruin_site_major", "chaurus_nest_major_potential", "structure_condition_ruined_extensively_icy", "ancient_technology_dwemer", "terrain_mountainous_winterhold_deep"],
                "density": "bustling",
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin",
                "sub_locations": [
                    {
                        "id": 3401,
                        "name": "Alftand Glacial Ruins",
                        "desc": "The icy, upper exterior sections of Alftand, often patrolled by Falmer and ice wraiths.",
                        "travel_desc": "Icy, upper exterior sections of Alftand.",
                        "tags": ["dwemer_ruin_minor_outpost_exterior", "climate_glacial_icy", "monster_den_ice_wraith", "falmer_presence_scouts_patrols", "structure_condition_ruined_extensively_glacial", "dungeon_minor_exterior_section"],
                        "density": "sparse",
                        "exit_label_from_parent": "Enter Glacial Ruins",
                        "exit_label_to_parent": "Exit to Alftand Overlook"
                    },
                    {
                        "id": 3402,
                        "name": "Alftand Animonculory",
                        "desc": "The main Dwemer manufactory within Alftand, filled with constructs, traps, and remnants of Dwemer machinery.",
                        "travel_desc": "Main Dwemer manufactory within Alftand.",
                        "tags": ["dwemer_ruin_major_city_section_animonculory", "mechanical_constructs_dwemer_heavy_manufactory", "trap_heavy_environment_dwemer", "ancient_technology_dwemer_machinery", "falmer_presence_strong_infestation", "dungeon_major_interior_section"],
                        "density": "bustling",
                        "exit_label_from_parent": "Enter Animonculory",
                        "exit_label_to_parent": "Exit to Glacial Ruins"
                    },
                    {
                        "id": 3403,
                        "name": "Alftand Cathedral",
                        "desc": "The grand central chamber of Alftand, leading deeper into the earth towards Blackreach. A place of significant Dwemer engineering.",
                        "travel_desc": "Grand central chamber of Alftand, leads to Blackreach.",
                        "tags": ["dwemer_ruin_major_city_section_cathedral", "structure_type_temple_building_dwemer_grand_chamber", "specific_landmark_type_blackreach_elevator_access_main", "mechanical_constructs_dwemer_boss_potential_centurion", "falmer_presence_strong_guardians", "dungeon_major_central_hub", "ancient_technology_dwemer_engineering_feat"],
                        "density": "average",
                        "exit_label_from_parent": "Enter Cathedral",
                        "exit_label_to_parent": "Exit to Animonculory"
                    }
                ]
            },
            {
                "id": 35,
                "name": "Frostmere Crypt",
                "desc": "A Nordic barrow on the border between The Pale and Winterhold, rumored to be home to bandits and a legendary spectral weapon known as 'The Pale Blade'.",
                "travel_desc": "Nordic barrow rumored home to 'The Pale Blade'.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong_draugr_ghosts", "bandit_minor_camp_potential_surface_or_interior", "quest_location_local_legend_pale_blade", "artifact_location_unique_item_pale_blade", "magical_properties_haunted_aura_strong", "terrain_pale_winterhold_border"],
                "density": "average",
                "exit_label_from_parent": "Crypt Entrance",
                "exit_label_to_parent": "Exit Crypt"
            },
            {
                "id": 36,
                "name": "Pilgrim's Trench",
                "desc": "A shipwreck graveyard in the icy waters north of Winterhold, a treacherous area for sailors, rumored to hold lost cargo and attract scavengers.",
                "travel_desc": "Shipwreck graveyard in icy waters.",
                "tags": ["structure_type_shipwreck_site_graveyard", "environment_coastal_icy_waters", "climate_glacial", "treasure_cache_rumored_lost_cargo", "dangerous_underwater_exploration_freezing", "monster_den_slaughterfish_potential", "exploration_point_multiple_wrecks"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Trench",
                "exit_label_to_parent": "Leave Trench Area"
            },
            {
                "id": 37,
                "name": "Sightless Pit",
                "desc": "A deep, dark chasm leading into a Falmer-infested cave system, located in the southwestern mountains of Winterhold. A place of utter darkness and terror.",
                "travel_desc": "Deep, dark chasm leading to Falmer-infested cave.",
                "tags": ["structure_type_natural_cave_chasm", "falmer_presence_strong_major_den", "dungeon_major_deep_dark", "terrain_canyon_deep_chasm", "environment_underground_utter_darkness", "chaurus_nest_major", "state_or_condition_current_lawless_area_falmer_territory", "exploration_challenge_extreme_danger"],
                "density": "bustling",
                "exit_label_from_parent": "Chasm Entrance",
                "exit_label_to_parent": "Exit Chasm"
            },
            {
                "id": 38,
                "name": "Skytemple Ruins",
                "desc": "Ruined Nordic towers atop a desolate mountain, offering a commanding view of Winterhold's icy expanse but little shelter from the biting winds.",
                "travel_desc": "Ruined Nordic towers atop a desolate mountain.",
                "tags": ["structure_type_ruined_tower_nordic_pair", "nordic_burial_site_minor_potential", "terrain_mountain_peak_desolate", "structure_condition_ruined_extensively_windswept", "climate_glacial_biting_winds", "scenic_vista_panoramic_icy_expanse", "exploration_point_minor_ruin"],
                "density": "empty",
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 39,
                "name": "Snowpoint Beacon",
                "desc": "A ruined watchtower on the northern coast of Winterhold, now a desolate landmark against the frozen sea.",
                "travel_desc": "Ruined watchtower, desolate coastal landmark.",
                "tags": ["structure_type_ruined_tower_watchtower", "environment_coastal_northern", "structure_condition_abandoned_desolate", "state_or_condition_current_isolated_and_forgotten", "climate_glacial", "exploration_point_minor_landmark"],
                "density": "empty",
                "exit_label_from_parent": "Path to Beacon",
                "exit_label_to_parent": "Leave Beacon Area"
            },
            {
                "id": 30001,
                "name": "Ysgramor's Tomb",
                "desc": "The final resting place of the legendary Ysgramor, founder of the Companions and leader of the Five Hundred Companions. A revered and dangerous Nordic tomb, closely guarded by the spirits of ancient heroes.",
                "travel_desc": "Final resting place of the legendary Ysgramor.",
                "tags": ["nordic_burial_site_major_revered", "cultural_historical_significance_legendary_hero_location_ysgramor", "faction_companions_related_quest_final", "undead_presence_strong_ancient_hero_spirits", "draugr_heavy", "dungeon_major", "quest_location_companions_guild_hall_final_trial", "artifact_location_powerful_wuuthrad_potential_return", "puzzle_ancient_nordic_companions_lore"],
                "density": "average",
                "exit_label_from_parent": "Tomb Entrance",
                "exit_label_to_parent": "Exit Tomb"
            },
            {
                "id": 30002,
                "name": "The Serpent Stone",
                "desc": "A Standing Stone located on an island in the Sea of Ghosts, north of the College of Winterhold, granting a unique paralytic magical power once per day.",
                "travel_desc": "Standing Stone granting paralytic magical power.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_offensive", "terrain_island_sea_of_ghosts", "environment_coastal_northern", "climate_glacial", "power_paralysis_ranged_daily", "cultural_historical_significance_ancient_magical_site"],
                "density": "empty",
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 30003,
                "name": "Driftshade Refuge",
                "desc": "An abandoned fort in Winterhold, which rumors say was once used by a renegade group of mages or, more recently, became a den for ice wraiths or desperate bandits.",
                "travel_desc": "Abandoned fort, rumored renegade mage or bandit den.",
                "tags": ["structure_type_ruined_fort", "structure_condition_abandoned_ruined", "monster_den_ice_wraith_potential", "bandit_minor_camp_potential", "dungeon_minor", "specific_landmark_type_silver_hand_hq_potential_alt", "mage_lair_hostile_potential_renegade", "exploration_point_historic_ruin"],
                "density": "sparse",
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 30004,
                "name": "Bleakcoast Cave",
                "desc": "A desolate ice cave on the northern coast, home to frost trolls and other hardy creatures adapted to the extreme cold.",
                "travel_desc": "Desolate ice cave, home to frost trolls.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial_desolate", "monster_den_frost_troll_major", "environment_coastal_northern", "dungeon_minor", "terrain_ice_field_coastal", "alchemy_ingredient_source_rich_troll_fat_potential"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 30005,
                "name": "The Wreck of the Winter Warbler",
                "desc": "A shipwreck frozen in the ice along Winterhold's northern coast, its treasures and the fate of its crew preserved in the cold.",
                "travel_desc": "Shipwreck frozen in ice, treasures preserved.",
                "tags": ["structure_type_shipwreck_site_frozen_in_ice", "structure_condition_ruined_extensively_preserved_in_ice", "environment_coastal_northern", "climate_glacial", "treasure_cache_rumored_lost_cargo", "undead_presence_skeletons_potential_frozen_crew", "dungeon_minor", "exploration_point_historic_wreck"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Wreck",
                "exit_label_to_parent": "Leave Wreck Area"
            },
            {
                "id": 30006,
                "name": "Japhet's Folly",
                "desc": "A small, isolated tower on an island far off the coast of Winterhold, rumored to be the retreat of a mad wizard or a hidden pirate cache. Currently, it is mostly a ruin battered by storms.",
                "travel_desc": "Isolated tower ruin, rumored mad wizard retreat.",
                "tags": ["structure_type_ruined_tower_isolated", "terrain_island_remote_sea_of_ghosts", "state_or_condition_current_isolated_and_forgotten_storm_battered", "magical_properties_enchanted_neutral_potential_mad_wizard", "specific_landmark_type_pirate_cove_hidden_potential", "environment_coastal", "climate_glacial", "quest_location_college_of_winterhold_potential_investigation", "dungeon_minor"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Tower",
                "exit_label_to_parent": "Leave Tower Area"
            },
            {
                "id": 30007,
                "name": "Frostedge Fishery",
                "desc": "A struggling fishing outpost on the treacherous icy coast of Winterhold, where a few hardy souls attempt to make a living from the frozen sea.",
                "travel_desc": "Struggling fishing outpost on treacherous icy coast.",
                "tags": ["populated_village_outpost", "settlement_minor_fishing", "economic_activity_fishing_industry_local_struggling", "environment_coastal_treacherous_icy", "climate_glacial_harsh", "state_or_condition_current_economically_depressed_isolated"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Fishery",
                "exit_label_to_parent": "Leave Fishery"
            },
            {
                "id": 30008,
                "name": "Hermit's Peak Cave",
                "desc": "A small, somewhat habitable ice cave high in the mountains of Winterhold, rumored to be the dwelling of a reclusive mage or a forgotten scholar.",
                "travel_desc": "Small, habitable ice cave, rumored hermit dwelling.",
                "tags": ["structure_type_natural_cave_ice_habitable", "climate_glacial_high_altitude", "terrain_mountain_peak", "hermit_lair_potential_mage_scholar", "magical_properties_arcane_focus_minor_potential", "dungeon_minor", "exploration_point_hidden_retreat"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 30009,
                "name": "Glacial Crevice",
                "desc": "A narrow, icy fissure in the mountains of Winterhold, leading to a small, frigid cave system. Often home to ice wraiths or other cold-dwelling creatures.",
                "travel_desc": "Narrow, icy fissure leading to a frigid cave system.",
                "tags": ["structure_type_natural_cave_ice_fissure", "climate_glacial_frigid", "dungeon_minor", "monster_den_ice_wraith", "terrain_mountain_pass_narrow", "unique_natural_formation_glacial_crevice", "exploration_point_dangerous_passage"],
                "density": "sparse",
                "exit_label_from_parent": "Crevice Entrance",
                "exit_label_to_parent": "Exit Crevice"
            },
            {
                "id": 30010,
                "name": "Forgotten Scholar's Hovel",
                "desc": "The collapsed remains of a small, ancient stone hovel, half-buried in snow. A few weathered books or scrolls might hint at its former occupant.",
                "travel_desc": "Collapsed remains of a small, ancient stone hovel.",
                "tags": ["structure_type_ruined_shack_hovel", "cultural_historical_significance_historic_site_minor_scholar", "structure_condition_collapsed_snow_buried", "lore_clue_potential_weathered_books_scrolls", "climate_glacial", "terrain_ice_field_isolated", "exploration_point_historic_remnants"],
                "density": "empty",
                "exit_label_from_parent": "Path to Hovel",
                "exit_label_to_parent": "Leave Hovel Area"
            },
            {
                "id": 30011,
                "name": "Snow-Shod Stables & Farm (Winterhold Outskirts)",
                "desc": "A surprisingly resilient farm and stables on the very edge of Winterhold's domain, perhaps benefiting from minor College enchantments to ward off the worst of the cold. They breed hardy northern ponies.",
                "travel_desc": "Resilient farm and stables on Winterhold's edge.",
                "tags": ["structure_type_farmstead", "structure_type_stable_building", "economic_activity_farming_livestock_hardy_ponies", "settlement_minor_resilient", "climate_arctic_edge_winterhold", "magical_properties_enchanted_neutral_potential_college_wards", "resource_node_horses_northern_breed"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 30012,
                "name": "Whistling Mine",
                "desc": "A tiny, struggling mining outpost in the northern cliffs of Winterhold, where miners brave the biting winds to extract a rare, ice-infused ore said to hum faintly.",
                "travel_desc": "Tiny, struggling mining outpost for rare, ice-infused ore.",
                "tags": ["populated_village_outpost_mining", "settlement_minor_struggling", "economic_activity_mining_gems_rare_ice_ore", "structure_type_mine_active_small", "climate_glacial_cliffs", "state_or_condition_current_isolated_and_forgotten_struggling", "magical_properties_enchanted_neutral_potential_humming_ore", "resource_node_rare_ore"],
                "density": "sparse",
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 30013,
                "name": "Shrine of Jhunal (Lost)",
                "desc": "The snow-swept, crumbling ruins of an ancient shrine dedicated to Jhunal, the Nordic god of knowledge and runes, predating the College's dominance. A few weathered carvings remain.",
                "travel_desc": "Crumbling ruins of an ancient shrine to Jhunal.",
                "tags": ["structure_type_ruined_shrine_nordic", "religious_site_aedric_jhunal_runes_knowledge", "cultural_historical_significance_nordic_ancient_site_pre_college", "magical_properties_arcane_focus_minor_potential_runic", "lore_clue_potential_weathered_carvings", "climate_glacial", "terrain_ice_field_snow_swept", "exploration_point_historic_religious_site"],
                "density": "empty",
                "exit_label_from_parent": "Path to Shrine",
                "exit_label_to_parent": "Leave Shrine Area"
            },
            {
                "id": 30014,
                "name": "Frozen Mammoth Cave",
                "desc": "A glacial cave where an ancient mammoth was flash-frozen millennia ago. The cave is now home to ice wraiths and other frost creatures, drawn to its intense cold.",
                "travel_desc": "Glacial cave with a flash-frozen ancient mammoth.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial_intense_cold", "dungeon_minor", "monster_den_ice_wraith_frost_creatures", "unique_natural_formation_flash_frozen_mammoth", "cultural_historical_significance_historic_site_prehistoric_remains", "alchemy_ingredient_source_rich_mammoth_tusk_potential"],
                "density": "sparse",
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 30015,
                "name": "The Tower Stone",
                "desc": "Located on a windswept clifftop along Winterhold's icy coast, this Standing Stone grants the power to once a day open any expert-level or lower lock.",
                "travel_desc": "Standing Stone granting power to open expert locks.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_utility", "environment_coastal_icy_clifftop", "terrain_cliffside_windswept", "cultural_historical_significance_ancient_magical_site", "power_unlock_expert_locks_daily", "utility_buff_lockpicking"],
                "density": "empty",
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 30016,
                "name": "Mount Anthor",
                "desc": "A high mountain peak on the border of Winterhold and The Pale, known in ancient legends as a dragon lair. While no dragons have been seen for centuries, it holds an ancient Word Wall.",
                "travel_desc": "High mountain peak, legendary dragon lair with Word Wall.",
                "tags": ["terrain_mountain_peak_high", "specific_landmark_type_dragon_lair_ancient_inactive_legendary", "specific_landmark_type_word_wall_location", "dungeon_minor_lair_potential", "cultural_historical_significance_dragon_lore_site_ancient", "climate_glacial_alpine", "state_or_condition_current_isolated_and_forgotten", "exploration_point_remote_lore"],
                "density": "sparse",
                "exit_label_from_parent": "Path to Peak",
                "exit_label_to_parent": "Leave Peak Area"
            },
            {
                "id": 30018,
                "name": "Yngvild",
                "desc": "An icy Nordic ruin on an island northeast of Dawnstar (near Winterhold border). It is haunted by the ghosts of women enthralled by the necromancer Arondil.",
                "travel_desc": "Icy Nordic ruin haunted by enthralled ghosts.",
                "tags": ["nordic_burial_site_major_icy", "structure_condition_ruined_extensively", "dungeon_major", "specific_landmark_type_necromancer_lair_arondil", "magical_properties_haunted_aura_strong_enthralled_ghosts", "undead_presence_strong_ghosts_draugr", "quest_location_investigation_necromancer_arondil", "terrain_island_northeast_dawnstar", "environment_coastal", "climate_glacial", "artifact_location_unique_item_potential_arondils_journals"],
                "density": "average",
                "exit_label_from_parent": "Path to Ruin",
                "exit_label_to_parent": "Leave Ruin"
            }
        ]
    }
]