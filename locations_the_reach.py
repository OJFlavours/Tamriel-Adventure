from locations_markarth_city import MARKARTH_CITY_LOCATIONS

THE_REACH_LOCATIONS = [
    # THE REACH
    {
        "id": 6,
        "name": "The Reach",
        "desc": "A wild, rugged, and mountainous region in western Skyrim, dominated by steep cliffs, deep valleys, and ancient Dwemer ruins. It is the heartland of the native Forsworn, who wage a bitter insurgency against Nord rule.",
        "travel_desc": "Wild, rugged, mountainous region, heartland of the Forsworn.",
        "tags": ["hold", "terrain_mountainous_extreme", "dwemer_ruin_heavy", "state_or_condition_current_forsworn_controlled_area_extensive", "economic_activity_mining_silver", "cultural_historical_significance_breton_reachmen_culture_strong", "state_or_condition_current_active_warzone_nearby_forsworn_insurgency", "climate_temperate_alpine", "environment_wilderness_rugged", "political_tension_high_forsworn_nord_conflict"],
        "demographics": {"Breton (Reachmen/Forsworn)": 60, "Nord": 30, "Orc": 5, "Others": 5},
        "travel": {
            "links": [
                {"name": "Whiterun Hold", "connection_type": "Road"},
                {"name": "Haafingar", "connection_type": "Road"},
                {"name": "Falkreath Hold", "connection_type": "Road"},
                {"name": "Hjaalmarch", "connection_type": "Road"},
                {"name": "Karth River Valley", "connection_type": "Path"},
                {"name": "Sundered Hills Pass", "connection_type": "Path"},
                {"name": "Hag Rock Trail", "connection_type": "Path"},
                {"name": "Deep Folk Crossing Path", "connection_type": "Path"}
            ]
        },
        "sub_locations": [
            {
                "id": 60,
                "name": "Markarth",
                "desc": "A city built into the stone cliffs by the Dwemer, now the capital of the Reach under Nord Jarl Igmund. It is known for its silver mines, brutalist architecture, and the simmering Forsworn conspiracy within its walls.",
                "travel_desc": "City built into stone cliffs, capital of the Reach.",
                "tags": ["populated_city", "structure_type_dwemer_city_repurposed", "terrain_mountain_city", "city_affiliation_the_reach_capital", "urban_issues_or_atmosphere_rampant_corruption_forsworn_conspiracy", "economic_activity_mining_silver", "settlement_features_jarls_longhouse", "imperial_influence_strong", "political_tension_high_forsworn_nord_conflict", "cultural_historical_significance_dwemer_ruin_major_city_integrated", "unique_landmark_iconic_stone_city", "dwemer_architecture_dominant", "urban_issues_or_atmosphere_oppressive_atmosphere", "state_or_condition_current_heavily_guarded"],
                "exit_label_from_parent": "City Gates",
                "exit_label_to_parent": "City Gates",
                "sub_locations": MARKARTH_CITY_LOCATIONS
            },
            {
                "id": 61,
                "name": "Karthwasten",
                "desc": "A rugged mining village in the Reach, centered around Sanuarach Mine and Fenn's Gulch Mine. It is frequently caught in the crossfire between Markarth's Silver-Blood family interests and Forsworn raids.",
                "travel_desc": "Rugged mining village, often caught in Forsworn raids.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_mining_silver", "political_tension_high_forsworn_conflict_zone", "economic_activity_mining_silver_contested", "political_influence_silver_blood_family", "state_or_condition_current_frequent_raids_local_forsworn", "terrain_mountain_valley", "climate_temperate_alpine"],
                "exit_label_from_parent": "Path to Village",
                "exit_label_to_parent": "Leave Village",
                 "sub_locations": [
                    {
                        "id": 6101,
                        "name": "Karthwasten Hall",
                        "desc": "The main hall in the small mining village of Karthwasten. It serves as a gathering place for the local miners and residents, often functioning as a makeshift inn due to the village's rugged nature. Discussions here frequently revolve around the ownership of the local silver mines (Sanuarach and Fenn's Gulch) and the constant threat of Forsworn raids. Ainethach, a Breton, is the owner of Sanuarach Mine and a prominent figure.",
                        "travel_desc": "Karthwasten's main hall and makeshift inn.",
                        "tags": ["structure_type_community_building", "social_hub_local", "meeting_hall_village", "inn_makeshift", "rumor_source", "quest_giver_potential_ainethach_mine_dispute"],
                        "context_tags": ["interior", "village_type", "tavern_type_makeshift", "safe_zone_ish"],
                        "demographics": {"Breton": 50, "Nord": 35, "Orc": 10, "Imperial": 5},
                        "fixed_npcs": [
                             {"name": "Ainethach", "race": "Breton", "role": "mine_owner_community_leader", "level": 7}
                        ],
                        "exit_label_from_parent": "Hall Door",
                        "exit_label_to_parent": "Exit Hall"
                    },
                    {
                        "id": 6102,
                        "name": "Sanuarach Mine",
                        "desc": "A silver mine in Karthwasten, owned by Ainethach. It's a key source of income for the village but is often at the center of disputes with the Silver-Blood family of Markarth and subject to Forsworn attacks. The miners here work under difficult conditions.",
                        "travel_desc": "Silver mine in Karthwasten, owned by Ainethach.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_silver", "resource_node_silver", "conflict_point_ownership_dispute_silver_blood", "forsworn_target_potential", "business_owner_ainethach"],
                        "context_tags": ["interior_cave", "industrial_site", "mine_type"],
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    },
                    {
                         "id": 6103,
                         "name": "Fenn's Gulch Mine",
                         "desc": "Another silver mine near Karthwasten, currently under the control of the Silver-Blood family through their mercenaries. Its operation is a point of contention for the local miners and Ainethach.",
                         "travel_desc": "Silver mine near Karthwasten, Silver-Blood controlled.",
                         "tags": ["structure_type_mine_active", "economic_activity_mining_silver", "resource_node_silver", "dangerous_area_forsworn_raids", "conflict_point_silver_blood_control", "mercenary_presence_silver_blood"],
                         "context_tags": ["interior_cave", "industrial_site", "mine_type"],
                         "exit_label_from_parent": "Mine Entrance",
                         "exit_label_to_parent": "Exit Mine"
                    }
                ]
            },
            {
                "id": 62,
                "name": "Druadach Redoubt",
                "desc": "A major Forsworn encampment and cave system hidden in the mountains southwest of Karthwasten, a formidable stronghold of the Reach's native rebellion.",
                "travel_desc": "Major Forsworn encampment and cave system.",
                "tags": ["faction_forsworn_stronghold_major", "structure_type_cave_system_fortified", "dungeon_major", "political_faction_rebel_base", "quest_location_faction_alliance_potential_forsworn", "forsworn_presence_strong", "hagraven_presence_potential", "terrain_mountainous_hidden", "state_or_condition_current_forsworn_controlled_area_major_base"],
                "exit_label_from_parent": "Redoubt Entrance",
                "exit_label_to_parent": "Leave Redoubt"
            },
            {
                "id": 63,
                "name": "Deep Folk Crossing",
                "desc": "An ancient Dwemer bridge spanning a tumultuous river high in the mountains. A breathtaking and perilous relic, rumored to lead to undiscovered ruins.",
                "travel_desc": "Ancient Dwemer bridge spanning a tumultuous river.",
                "tags": ["structure_type_bridge_dwemer_ancient", "ruin_landmark_remote", "scenic_vista_panoramic_dangerous", "exploration_challenge_perilous_crossing", "undiscovered_ruins_rumor_dwemer", "terrain_mountain_pass", "terrain_river_gorge", "cultural_historical_significance_dwemer_engineering_feat", "state_or_condition_current_isolated_and_forgotten"],
                "exit_label_from_parent": "Path to Crossing",
                "exit_label_to_parent": "Leave Crossing Area"
            },
            {
                "id": 64,
                "name": "Dushnikh Yal",
                "desc": "An Orc stronghold in the southwestern Reach, adhering to the ancient Code of Malacath. Known for its skilled warriors, miners, and adherence to tradition.",
                "travel_desc": "Orc stronghold adhering to the Code of Malacath.",
                "tags": ["orc_stronghold", "populated_settlement_orcish", "tribal_community_orcish", "terrain_mountain_settlement_fortified", "economic_activity_mining_orichalcum", "warrior_culture_orcish", "malacath_worship", "structure_type_fortified_settlement", "cultural_historical_significance_orc_tradition", "faction_orc_tribe_dushnikh_yal", "climate_temperate_alpine"],
                "exit_label_from_parent": "Stronghold Gate",
                "exit_label_to_parent": "Leave Stronghold",
                 "sub_locations": [
                    {
                        "id": 6401,
                        "name": "Burguk's Longhouse",
                        "desc": "The longhouse of Chief Burguk, the stern but fair leader of Dushnikh Yal.",
                        "travel_desc": "Longhouse of Chief Burguk.",
                        "tags": ["structure_type_longhouse_orcish", "government_tribal", "chieftains_hall", "residence_chief"],
                        "exit_label_from_parent": "Longhouse Door",
                        "exit_label_to_parent": "Exit Longhouse"
                    },
                    {
                        "id": 6402,
                        "name": "Dushnikh Mine (Orichalcum)",
                        "desc": "The stronghold's orichalcum mine, providing valuable ore for Orcish smithing and trade.",
                        "travel_desc": "Stronghold's orichalcum mine.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_orichalcum", "resource_node_orichalcum", "orc_controlled_mine"],
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    },
                    {
                        "id": 6403,
                        "name": "Gharol's Smithy (Dushnikh Yal)",
                        "desc": "The forge of Gharol, the skilled blacksmith of Dushnikh Yal, crafting traditional Orcish arms and armor.",
                        "travel_desc": "Forge of Gharol, skilled Orc blacksmith.",
                        "tags": ["settlement_features_blacksmith_forge_active", "structure_type_shop_building", "economic_activity_smithing_production", "crafting_orcish_traditional", "female_orc_smith", "item_type_weapon_vendor", "item_type_armor_vendor"],
                        "exit_label_from_parent": "Smithy Entrance",
                        "exit_label_to_parent": "Exit Smithy"
                    }
                ]
            },
            {
                "id": 65,
                "name": "Blind Cliff Cave",
                "desc": "A cave system north of Markarth, a den for Forsworn ritualists and their hagraven allies.",
                "travel_desc": "Cave system, den for Forsworn ritualists.",
                "tags": ["structure_type_natural_cave", "forsworn_ritual_site", "specific_landmark_type_hagraven_coven_lair_main", "dungeon_minor", "magical_properties_tainted_by_dark_magic", "forsworn_presence_strong", "hagraven_presence_strong", "state_or_condition_current_forsworn_controlled_area"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 66,
                "name": "Bruca's Leap Redoubt",
                "desc": "A Forsworn encampment built around a waterfall and river, east of Karthwasten, utilizing the natural defenses of the terrain.",
                "travel_desc": "Forsworn encampment built around a waterfall.",
                "tags": ["structure_type_fortified_camp_forsworn", "forsworn_presence_strong", "unique_natural_formation_waterfall_location_strategic", "dungeon_minor", "terrain_river_delta_outpost", "natural_defenses_utilized", "state_or_condition_current_forsworn_controlled_area"],
                "exit_label_from_parent": "Redoubt Entrance",
                "exit_label_to_parent": "Leave Redoubt"
            },
            {
                "id": 67,
                "name": "Dead Crone Rock",
                "desc": "A ruined tower and Forsworn stronghold west of Markarth, a place of dark magic and a site for a Daedric quest related to Mehrunes' Razor.",
                "travel_desc": "Ruined tower and Forsworn stronghold, site for Daedric quest.",
                "tags": ["structure_type_ruined_tower", "forsworn_stronghold_major", "specific_landmark_type_hagraven_coven_lair_main", "quest_location_daedric_mehrunes_razor_pieces", "dungeon_major", "forsworn_presence_strong", "hagraven_presence_strong", "magical_properties_tainted_by_dark_magic", "artifact_location_daedric_razor_pieces", "state_or_condition_current_forsworn_controlled_area"],
                "exit_label_from_parent": "Path to Rock",
                "exit_label_to_parent": "Leave Rock Area"
            },
            {
                "id": 68,
                "name": "Deepwood Redoubt",
                "desc": "A large Forsworn encampment and Nordic ruin complex northwest of Markarth, serving as a major base and leading to the hagraven lair of Hag's End.",
                "travel_desc": "Large Forsworn encampment leading to Hag's End.",
                "tags": ["structure_type_fortified_camp_ruin_integrated", "forsworn_stronghold_major", "nordic_ruin_integrated", "dungeon_major_complex", "quest_location_exploration_hags_end", "hags_end_access", "forsworn_presence_strong", "hagraven_presence_potential", "state_or_condition_current_forsworn_controlled_area_major_base"],
                "exit_label_from_parent": "Redoubt Entrance",
                "exit_label_to_parent": "Leave Redoubt"
            },
            {
                "id": 69,
                "name": "Dragontooth Crater",
                "desc": "An ancient, dormant volcanic crater high in the northern mountains of the Reach. While no dragons have been seen for eras, old tales speak of it as a nesting site.",
                "travel_desc": "Ancient, dormant volcanic crater, rumored dragon nesting site.",
                "tags": ["unique_natural_formation_volcanic_crater_dormant", "terrain_mountain_peak_remote_northern_reach", "dungeon_potential_lair_ancient_dragon", "dragon_lore_ancient_site_nesting_rumor", "cultural_historical_significance_legendary_site", "climate_alpine_extreme_weather", "exploration_challenge_remote_dangerous"],
                "exit_label_from_parent": "Path to Crater",
                "exit_label_to_parent": "Leave Crater Area"
            },
            {
                "id": 60001,
                "name": "Hag Rock Redoubt",
                "desc": "A Forsworn-occupied ruin south of Markarth, a constant threat to travelers and caravans in the area.",
                "travel_desc": "Forsworn-occupied ruin, threat to travelers.",
                "tags": ["structure_type_ruined_fort", "forsworn_presence_strong", "dungeon_minor", "quest_location_bounty_target_potential", "state_or_condition_current_forsworn_controlled_area", "roadside_danger_spot_south_markarth"],
                "exit_label_from_parent": "Redoubt Entrance",
                "exit_label_to_parent": "Leave Redoubt"
            },
            {
                "id": 60002,
                "name": "Hag's End",
                "desc": "A ruined tower accessible through Deepwood Redoubt, home to powerful hagravens and an ancient Word Wall.",
                "travel_desc": "Ruined tower, home to hagravens and a Word Wall.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main_powerful", "dungeon_major", "specific_landmark_type_word_wall_location", "quest_location_exploration_deepwood_redoubt_access", "magical_properties_tainted_by_dark_magic", "hagraven_presence_strong", "state_or_condition_current_forsworn_controlled_area_deepwood"],
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit to Deepwood Redoubt"
            },
            {
                "id": 60003,
                "name": "Karthspire",
                "desc": "A towering, craggy mountain in the Reach, infamous for its large Forsworn presence at its base, guarding the hidden ascent to ancient ruins.",
                "travel_desc": "Towering mountain with large Forsworn presence at base.",
                "tags": ["terrain_mountain_peak_landmark_craggy", "state_or_condition_current_forsworn_controlled_area_heavy_base", "cultural_historical_significance_ancient_ruins_summit_rumor_sky_haven", "dangerous_ascent_perilous_forsworn_guardians", "quest_location_main_story_potential_sky_haven_temple", "cultural_historical_significance_blades_related_rumor"],
                "exit_label_from_parent": "Path to Karthspire",
                "exit_label_to_parent": "Leave Karthspire Area"
            },
            {
                "id": 60004,
                "name": "Kolskeggr Mine",
                "desc": "A rich gold mine east of Markarth, currently abandoned or lightly worked due to frequent and brutal Forsworn attacks that have driven off miners.",
                "travel_desc": "Rich gold mine, abandoned due to Forsworn attacks.",
                "tags": ["structure_type_mine_abandoned_gold", "economic_activity_mining_gold_historic_rich", "state_or_condition_current_forsworn_controlled_area_attacks_severe", "quest_location_reclaim_mine_kolskeggr", "state_or_condition_current_abandoned_due_to_danger", "resource_node_gold_valuable", "forsworn_presence_strong_nearby_attacks"],
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 60005,
                "name": "Left Hand Mine",
                "desc": "An iron mine located just outside Markarth, owned by Skaggi Scar-Face, providing steady work for the town.",
                "travel_desc": "Iron mine outside Markarth, owned by Skaggi Scar-Face.",
                "tags": ["structure_type_mine_active_iron", "economic_activity_mining_iron", "resource_node_iron", "settlement_minor_support_markarth", "local_employer_markarth_outskirts", "quest_giver_potential_mine_owner_skaggi"],
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 60006,
                "name": "Lost Valley Redoubt",
                "desc": "A major Forsworn encampment built around scenic waterfalls and ancient Nordic structures, home to powerful Forsworn Briarhearts and an ancient Word Wall.",
                "travel_desc": "Major Forsworn encampment with waterfalls and a Word Wall.",
                "tags": ["structure_type_fortified_camp_ruin_integrated", "forsworn_stronghold_major_scenic", "unique_natural_formation_waterfall_location_defensive", "nordic_ruin_integrated", "dungeon_major", "specific_landmark_type_word_wall_location", "briarheart_presence_strong", "forsworn_presence_strong", "state_or_condition_current_forsworn_controlled_area_major_base"],
                "exit_label_from_parent": "Redoubt Entrance",
                "exit_label_to_parent": "Leave Redoubt"
            },
            {
                "id": 60007,
                "name": "Reachcliff Cave",
                "desc": "A cave south of Markarth. While sometimes occupied by undead, it's also known as a site for a dark Daedric ritual involving Namira.",
                "travel_desc": "Cave, site of a dark Daedric ritual involving Namira.",
                "tags": ["structure_type_natural_cave", "undead_presence_potential_draugr", "quest_location_daedric_namira_cannibalism", "dungeon_minor", "ritual_site_dark_daedric_namira", "magical_properties_daedric_influence_overt_namira", "faction_cannibal_cult_potential_eola", "state_or_condition_current_desecrated_potential"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 60008,
                "name": "Reachwind Eyrie",
                "desc": "A ruined Dwemer tower on a clifftop overlooking the Karth River. It's often used as a lookout or minor outpost by Forsworn or bandits.",
                "travel_desc": "Ruined Dwemer tower overlooking Karth River.",
                "tags": ["structure_type_ruined_tower_dwemer", "forsworn_outpost_potential", "bandit_lookout_potential", "scenic_vista_strategic_river_view_karth", "terrain_cliffside_eyrie", "cultural_historical_significance_dwemer_ruin_minor", "dungeon_minor_tower_ruin"],
                "exit_label_from_parent": "Path to Eyrie",
                "exit_label_to_parent": "Leave Eyrie"
            },
            {
                "id": 60009,
                "name": "Red Eagle Redoubt",
                "desc": "A large Forsworn camp and Nordic ruin complex, central to the legend of the ancient Reach hero, Red Eagle. Many Forsworn revere this site.",
                "travel_desc": "Large Forsworn camp, central to legend of Red Eagle.",
                "tags": ["structure_type_fortified_camp_ruin_integrated", "forsworn_camp_historic_revered", "nordic_ruin_integrated", "dungeon_major", "cultural_historical_significance_legendary_hero_location_red_eagle", "quest_location_lore_artifact_red_eagles_bane", "forsworn_presence_strong", "cultural_historical_significance_forsworn_hero_site", "artifact_location_unique_item_potential_red_eagles_fury", "state_or_condition_current_forsworn_controlled_area_major_base"],
                "exit_label_from_parent": "Redoubt Entrance",
                "exit_label_to_parent": "Leave Redoubt"
            },
            {
                "id": 60010,
                "name": "Sky Haven Temple",
                "desc": "An ancient, forgotten temple complex high in the Karthspire mountain, rumored to have once been a sanctuary for a lost order of dragon hunters. Its exact location is a mystery, likely hidden behind perilous Forsworn territory and natural barriers.",
                "travel_desc": "Ancient, forgotten temple, rumored dragon hunter sanctuary.",
                "tags": ["structure_type_temple_ruined_ancient", "cultural_historical_significance_historic_temple_lost_blades", "secret_location_rumored_hidden_karthspire", "dragon_lore_ancient_site_blades_related", "terrain_mountain_peak_hidden_karthspire", "cultural_historical_significance_ancient_ruin_blades", "faction_blades_history_rumored_hq", "cultural_historical_significance_blades_hq_ancient", "quest_location_main_story_potential_elder_scroll_related"],
                "exit_label_from_parent": "Path to Temple",
                "exit_label_to_parent": "Leave Temple Area",
                "sub_locations": [
                    {
                        "id": 600101,
                        "name": "Alduin's Wall",
                        "desc": "A massive, ancient carved wall rumored to exist deep within the Karthspire ruins. Its intricate carvings are believed by some to depict ancient dragon myths or forgotten histories. Its true meaning is lost to time.",
                        "travel_desc": "Massive, ancient carved wall depicting dragon myths.",
                        "tags": ["historic_artifact_legendary_prophetic", "ancient_carving_prophetic_rumor_dragon_war", "dragon_myth_depiction_alduin_defeat", "cultural_historical_significance_prophetic_wall_blades", "faction_blades_lore_central", "dwemer_influence_potential_construction_rumor", "unique_landmark_iconic_wall"],
                        "exit_label_from_parent": "Approach Wall",
                        "exit_label_to_parent": "Leave Wall Area"
                    }
                ]
            },
            {
                "id": 60011,
                "name": "Soljund's Sinkhole",
                "desc": "A moonstone mine east of Markarth that has recently broken into a draugr-infested Nordic ruin, causing terror among the miners.",
                "travel_desc": "Moonstone mine broken into a draugr-infested ruin.",
                "tags": ["structure_type_mine_active_moonstone", "economic_activity_mining_moonstone", "nordic_ruin_breach_recent_sinkhole", "undead_presence_strong_draugr_infestation", "dungeon_minor_mine_ruin_combo", "resource_node_moonstone_dangerous", "quest_location_clear_mine_soljunds_sinkhole", "state_or_condition_current_recently_attacked_recovering_potential"],
                "exit_label_from_parent": "Mine Entrance",
                "exit_label_to_parent": "Exit Mine"
            },
            {
                "id": 60012,
                "name": "Old Hroldan Inn",
                "desc": "A truly ancient inn situated in the wilds of the Reach, south of Soljund's Sinkhole. Run by Eydis, the inn is steeped in history, with local legends claiming that Tiber Septim himself once stayed in the large suite. Guests sometimes report strange occurrences, and a ghostly presence is often felt, particularly in Tiber Septim's old room.",
                "travel_desc": "Ancient inn in the Reach, run by Eydis; Tiber Septim legend.",
                "tags": ["structure_type_inn_building_ancient", "tavern_remote_historic", "cultural_historical_significance_historic_site_tiber_septim_stayed", "magical_properties_haunted_aura_potential_ghost_quest", "isolated_lodging", "rumor_source_local_legends_ghosts", "food_drink_vendor", "quest_location_ghost_of_old_hroldan", "business_owner_eydis"],
                "context_tags": ["interior", "wilderness_isolated", "tavern_type_historic", "safe_zone_ish"],
                "demographics": {"Nord": 60, "Breton": 20, "Imperial": 10, "Redguard": 5, "Orc": 5},
                "fixed_npcs": [
                    {"name": "Eydis", "race": "Nord", "role": "innkeeper_historic_site", "level": 7}
                ],
                "exit_label_from_parent": "Inn Door",
                "exit_label_to_parent": "Exit Inn"
            },
            {
                "id": 60013,
                "name": "Mor Khazgur",
                "desc": "An Orc stronghold in the northwestern Reach, known for its skilled hunters and fierce warriors, led by Chief Larak.",
                "travel_desc": "Orc stronghold known for skilled hunters and warriors.",
                "tags": ["orc_stronghold", "populated_settlement_orcish", "tribal_community_orcish", "terrain_mountain_settlement_fortified_northwestern_reach", "economic_activity_hunting_furs_meat_skilled", "warrior_culture_orcish", "malacath_worship", "structure_type_fortified_settlement", "economic_activity_mining_orichalcum_potential", "cultural_historical_significance_orc_tradition", "faction_orc_tribe_mor_khazgur", "climate_temperate_alpine"],
                "exit_label_from_parent": "Stronghold Gate",
                "exit_label_to_parent": "Leave Stronghold",
                "sub_locations": [
                    {
                        "id": 600131,
                        "name": "Larak's Longhouse",
                        "desc": "The longhouse of Chief Larak, leader of Mor Khazgur.",
                        "travel_desc": "Longhouse of Chief Larak.",
                        "tags": ["structure_type_longhouse_orcish", "government_tribal", "chieftains_hall", "residence_chief"],
                        "exit_label_from_parent": "Longhouse Door",
                        "exit_label_to_parent": "Exit Longhouse"
                    },
                    {
                        "id": 600132,
                        "name": "Mor Khazgur Mine (Orichalcum)",
                        "desc": "The stronghold's orichalcum mine, crucial for their smithing and economy.",
                        "travel_desc": "Stronghold's orichalcum mine.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_orichalcum", "resource_node_orichalcum", "orc_controlled_mine"],
                        "exit_label_from_parent": "Mine Entrance",
                        "exit_label_to_parent": "Exit Mine"
                    }
                ]
            },
            {
                "id": 60014,
                "name": "Purewater Run",
                "desc": "A small, hidden cave system behind a waterfall, known for its remarkably clear stream and rare fish. Sometimes used by outlaws as a discreet meeting place.",
                "travel_desc": "Hidden cave behind waterfall, known for clear stream.",
                "tags": ["structure_type_natural_cave_hidden_waterfall", "unique_natural_formation_clear_spring_rare_fish", "economic_activity_fishing_rare_fish_source", "bandit_minor_camp_potential_outlaw_meeting_spot", "dungeon_minor", "terrain_mountainous_reach", "environment_wilderness", "alchemy_ingredient_source_rich_potential_rare_flora_fauna", "secluded_nature_spot_picturesque"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 60015,
                "name": "Reachwind Crag",
                "desc": "A series of treacherous, wind-swept cliffs and narrow paths, home to territorial hagravens and offering perilous views over the Karth River valley.",
                "travel_desc": "Treacherous cliffs, home to territorial hagravens.",
                "tags": ["terrain_cliff_network_treacherous", "specific_landmark_type_hagraven_coven_lair_main_territory", "dangerous_terrain_high_winds_narrow_paths", "scenic_vista_perilous_river_view_karth", "monster_den_hagraven_strong", "forsworn_presence_potential_allies", "terrain_mountainous_reach", "environment_wilderness", "dungeon_minor_outdoor_cliffside", "state_or_condition_current_lawless_area_hagraven"],
                "exit_label_from_parent": "Path to Crag",
                "exit_label_to_parent": "Leave Crag Area"
            },
            {
                "id": 60016,
                "name": "Reachwater Rock",
                "desc": "A cave system behind a waterfall in the Reach, containing ancient Nordic ruins and playing a part in the legend of the Gauldur Amulet.",
                "travel_desc": "Cave behind waterfall, contains Nordic ruins (Gauldur Amulet).",
                "tags": ["structure_type_natural_cave_waterfall_hidden", "nordic_ruin_interior_gauldur_legend", "dungeon_major", "quest_location_artifact_gauldur_amulet_fragment_final_assembly", "cultural_historical_significance_ancient_magical_site_gauldur", "terrain_mountainous_reach", "environment_wilderness", "artifact_location_powerful_gauldur_amulet_complete", "undead_presence_strong_potential_gauldurson_spirits", "puzzle_ancient_nordic_potential_gauldur_lore"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 60017,
                "name": "Four Skull Lookout",
                "desc": "A ruined Nordic tower and small barrow complex in the Reach, often occupied by bandits or Forsworn, guarding an ancient Word Wall.",
                "travel_desc": "Ruined Nordic tower and barrow, guards a Word Wall.",
                "tags": ["structure_type_ruined_tower_nordic_lookout", "nordic_burial_site_minor_complex", "bandit_outpost_potential", "forsworn_camp_potential", "specific_landmark_type_word_wall_location", "dungeon_minor", "terrain_mountainous_reach", "environment_wilderness", "undead_presence_potential_draugr_guardians", "exploration_point_lore_word_wall"],
                "exit_label_from_parent": "Path to Lookout",
                "exit_label_to_parent": "Leave Lookout"
            },
            {
                "id": 60018,
                "name": "Karthside Hovel",
                "desc": "A tiny, impoverished hamlet of Reach natives clinging to the cliffs near the Karth River, often harassed by both Forsworn and Markarth guards.",
                "travel_desc": "Tiny, impoverished hamlet of Reach natives.",
                "tags": ["populated_village_reach_native_poor_hovel", "settlement_minor_cliffside_precarious", "cliffside_dwelling_precarious", "forsworn_sympathizers_potential_oppressed", "state_or_condition_current_conflict_zone_civilian_harassment_guards_forsworn", "terrain_mountainous_karth_river", "environment_wilderness", "social_issue_poverty_extreme", "economic_activity_fishing_subsistence_potential"],
                "exit_label_from_parent": "Path to Hovel",
                "exit_label_to_parent": "Leave Hovel"
            },
            {
                "id": 60019,
                "name": "Eagles' Nest Farm",
                "desc": "A very remote and high-altitude farm in The Reach, accessible only by treacherous paths, known for its hardy livestock and reclusive owners.",
                "travel_desc": "Remote, high-altitude farm with hardy livestock.",
                "tags": ["structure_type_farmstead_remote_high_altitude", "economic_activity_farming_livestock_hardy_mountain_breeds", "isolated_community_self_sufficient", "dangerous_access_route_treacherous_paths", "terrain_mountain_peak_reach", "environment_wilderness", "hermit_lair_potential_reclusive_family", "unique_produce_mountain_herbs_cheese_potential"],
                "exit_label_from_parent": "Path to Farm",
                "exit_label_to_parent": "Leave Farm Area"
            },
            {
                "id": 60020,
                "name": "Cliffside Crevice",
                "desc": "A narrow cave system hidden within the steep cliffs of The Reach, a perfect natural hideout for Forsworn scouts or a den for cliff-dwelling creatures.",
                "travel_desc": "Narrow cave system hidden in steep cliffs.",
                "tags": ["structure_type_natural_cave_cliffside_narrow", "dungeon_minor", "forsworn_hideout_potential_scout_ambush", "monster_den_cliff_creatures_falmer_potential_high_altitude", "natural_fortification_hidden_crevice", "terrain_mountainous_steep_cliffs", "environment_wilderness", "forsworn_presence_potential"],
                "exit_label_from_parent": "Crevice Entrance",
                "exit_label_to_parent": "Exit Crevice"
            },
            {
                "id": 60021,
                "name": "Ruined Dwemer Outpost (Minor)",
                "desc": "The scattered, collapsed remains of a small Dwemer outpost or monitoring station, likely picked clean of valuables long ago but still hinting at their ancient presence.",
                "travel_desc": "Scattered remains of a small Dwemer outpost.",
                "tags": ["structure_type_ruined_settlement_dwemer_outpost", "dwemer_ruin_minor_outpost_monitoring_station", "cultural_historical_significance_dwemer_ruin_minor", "ancient_technology_remnants_scattered", "exploration_point_minor_lore_dwemer", "terrain_mountainous_reach", "environment_wilderness", "structure_condition_collapsed_extensively_picked_clean"],
                "exit_label_from_parent": "Path to Ruins",
                "exit_label_to_parent": "Leave Ruins"
            },
            {
                "id": 60022,
                "name": "Fort Sungard (Contested Ruin)",
                "desc": "A large, strategically important fort in the Reach, now mostly in ruins. It's a frequent point of conflict, with Forsworn, bandits, or even small Imperial/Stormcloak scouting parties vying for control of its crumbling walls.",
                "travel_desc": "Large, ruined fort, frequent point of conflict.",
                "tags": ["structure_type_ruined_fort_major_strategic", "dungeon_major", "state_or_condition_current_forsworn_conflict_zone_contested", "bandit_stronghold_potential", "state_or_condition_current_contested_territory_military_various_factions", "cultural_historical_significance_historic_fort_reach", "terrain_mountainous_reach", "environment_wilderness", "forsworn_presence_potential", "imperial_influence_potential_historic", "stormcloak_influence_potential_historic", "civil_war_quest_historic_site_potential"],
                "exit_label_from_parent": "Fort Entrance",
                "exit_label_to_parent": "Exit Fort"
            },
            {
                "id": 60023,
                "name": "Old Gods' Clearing (Reach Wilderness)",
                "desc": "A secluded clearing deep in the Reach wilderness, marked by weathered, primitive stone carvings and arrangements hinting at ancient Reach native worship, pre-dating even the Nords.",
                "travel_desc": "Secluded clearing with primitive stone carvings.",
                "tags": ["structure_type_shrine_outdoor_structure_primitive_weathered", "cultural_historical_significance_reachmen_ancient_site_pre_nordic", "forsworn_sacred_site_potential_old_gods", "environment_wilderness_landmark_hidden_clearing", "ritual_site_old_gods_forsworn", "terrain_mountainous_deep_reach", "magical_properties_enchanted_neutral_potential_ancient_power", "forsworn_presence_spiritual_gathering_place"],
                "exit_label_from_parent": "Path to Clearing",
                "exit_label_to_parent": "Leave Clearing"
            },
            {
                "id": 60024,
                "name": "Briarheart Warren",
                "desc": "A small, thorny cave system hidden in the rugged hills of the Reach, rumored to be a place where Forsworn Briarhearts are created or where they retreat to recover.",
                "travel_desc": "Thorny cave system, rumored Briarheart creation site.",
                "tags": ["structure_type_natural_cave_thorny_hidden", "dungeon_minor", "forsworn_ritual_site_briarheart_rumor_creation", "forsworn_hideout_secret_briarheart_retreat", "dangerous_flora_thorns_briars", "terrain_mountainous_rugged_hills_reach", "environment_wilderness", "magical_properties_ritualistic_dark_nature_magic", "forsworn_presence_strong_potential_guardians", "briarheart_presence_potential_recovering_created"],
                "exit_label_from_parent": "Cave Entrance",
                "exit_label_to_parent": "Exit Cave"
            },
            {
                "id": 60025,
                "name": "The Lover Stone",
                "desc": "An ancient Standing Stone found in the rugged hills east of Markarth, said to grant those who touch it a quicker aptitude in all endeavors.",
                "travel_desc": "Standing Stone granting quicker aptitude in all endeavors.",
                "tags": ["specific_landmark_type_standing_stone_magical", "buff_skill_learning_all_increased_lovers_comfort_effect", "terrain_mountainous_rugged_hills_east_markarth", "cultural_historical_significance_ancient_magical_site", "environment_wilderness_reach", "magical_properties_enchanted_positive_utility", "power_skill_boost_passive"],
                "exit_label_from_parent": "Path to Stone",
                "exit_label_to_parent": "Leave Stone Area"
            },
            {
                "id": 60026,
                "name": "Valthume",
                "desc": "An ancient and sprawling Nordic ruin deep in the mountains of The Reach, southeast of Markarth. It is the burial place of the Dragon Priest Hevnoraak and a site of significant old power.",
                "travel_desc": "Sprawling Nordic ruin, burial place of Dragon Priest Hevnoraak.",
                "tags": ["nordic_burial_site_major_dragon_priest_tomb", "dungeon_large_complex_sprawling", "cultural_historical_significance_dragon_cult_lair_priest_hevnoraak", "undead_presence_strong_powerful_draugr_priest", "cultural_historical_significance_ancient_magical_site_old_power", "specific_landmark_type_word_wall_location", "quest_location_dragon_priest_hevnoraak", "artifact_location_powerful_mask_hevnoraak", "draugr_heavy", "terrain_mountainous_reach_southeast_markarth"],
                "exit_label_from_parent": "Ruin Entrance",
                "exit_label_to_parent": "Exit Ruin"
            },
            {
                "id": 60029,
                "name": "Rebel's Cairn",
                "desc": "An ancient cairn in the Reach, west of Karthwasten, said to be the burial site of a legendary Forsworn hero. It is a sacred place for some Reachmen and may hold ancient secrets or guardians.",
                "travel_desc": "Ancient cairn, burial site of a legendary Forsworn hero.",
                "tags": ["structure_type_ruined_shrine_cairn_ancient", "cultural_historical_significance_forsworn_hero_site_legendary", "forsworn_sacred_site_revered", "dungeon_minor_historic_burial", "undead_guardian_potential_hero_spirit", "reach_lore_heroic_figure_red_eagle_related_potential", "terrain_mountainous_west_karthwasten", "environment_wilderness", "forsworn_presence_spiritual_pilgrimage_potential", "quest_location_local_legend_potential_artifact"],
                "exit_label_from_parent": "Cairn Entrance",
                "exit_label_to_parent": "Exit Cairn"
            },
            {
                "id": 60030,
                "name": "Blind Cliff Bastion",
                "desc": "A ruined Nordic tower complex built into the cliffs of the Reach, now a formidable Forsworn stronghold. Distinct from Blind Cliff Cave.",
                "travel_desc": "Ruined Nordic tower complex, formidable Forsworn stronghold.",
                "tags": ["structure_type_ruined_fort_nordic_cliffside_bastion", "forsworn_stronghold_major_cliffside", "dungeon_major_vertical_complex", "dangerous_approach_forsworn_defenses", "reach_fortification_native_repurposed", "terrain_mountainous_cliffs_reach", "environment_wilderness", "forsworn_presence_strong", "hagraven_presence_potential", "state_or_condition_current_forsworn_controlled_area_major_base"],
                "exit_label_from_parent": "Bastion Entrance",
                "exit_label_to_parent": "Leave Bastion"
            }
        ]
    }
]