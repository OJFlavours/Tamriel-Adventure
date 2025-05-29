LOCATIONS = [
    # WHITERUN HOLD
    {
        "id": 1,
        "name": "Whiterun Hold",
        "desc": "The fertile heartland of Skyrim, marked by golden plains and the bustling city of Whiterun. A center of commerce, Imperial influence, and ancient Nordic tradition.",
        "tags": ["hold", "terrain_plains", "central_location", "economic_activity_trade_hub_regional", "nordic_culture_strong", "imperial_influence_moderate", "climate_temperate", "economic_activity_farming_crops", "economic_activity_farming_livestock", "state_or_condition_current_politically_stable", "travel_hub_major"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "roads": ["The Rift", "Eastmarch", "The Reach", "Haafingar", "Falkreath Hold", "The Pale"],
            "paths": ["Riverwood", "Rorikstead", "Helgen"]
        },
        "sub_locations": [
            {
                "id": 10,
                "name": "Whiterun",
                "desc": "A thriving trade city built around the great keep Dragonsreach, seat of Jarl Balgruuf the Greater. Its bustling market and legendary mead hall form the heart of the hold.",
                "tags": ["populated_city", "city_affiliation_whiterun_hold_capital", "economic_activity_trade_hub_major", "settlement_features_market_square", "settlement_features_jarls_longhouse", "settlement_features_companions_guild_hall", "settlement_features_temple_divines", "imperial_influence_strong", "cultural_historical_significance_nordic_settlement_ancient", "structure_type_fortified_city_wall", "cultural_historical_significance_ysgramor_related_site", "urban_issues_or_atmosphere_bustling_trade_atmosphere", "unique_landmark_iconic_dragonsreach_gildergreen"],
                "sub_locations": [
                    {
                        "id": 1001,
                        "name": "Dragonsreach",
                        "desc": "The imposing keep of the Jarl, an iconic symbol of Nord authority and power, once used to imprison the dragon Numinex in ages past.",
                        "tags": ["structure_type_fortified_keep", "settlement_features_jarls_longhouse", "cultural_historical_significance_historic_site", "government_local", "unique_landmark_iconic", "dragon_lore_ancient_site", "nordic_architecture_ancient"]
                    },
                    {
                        "id": 1002,
                        "name": "Jorrvaskr",
                        "desc": "The ancient mead hall and headquarters of the Companions, where warriors forge bonds in battle and honor tradition.",
                        "tags": ["structure_type_guild_hall_building", "settlement_features_companions_guild_hall", "cultural_historical_significance_historic_site", "warrior_culture_strong", "cultural_historical_significance_nordic_settlement_ancient", "faction_companions_hq"]
                    },
                    {
                        "id": 1003,
                        "name": "The Bannered Mare",
                        "desc": "A lively tavern where travelers and locals share stories over hearty ale, a central hub of Whiterun's social life.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available"]
                    },
                    {
                        "id": 1004,
                        "name": "Warmaiden's",
                        "desc": "A masterful smithy known for crafting sturdy weapons and armor, run by Adrianne Avenicci and Ulfberth War-Bear.",
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor", "item_type_armor_vendor", "crafting_tools"]
                    },
                    {
                        "id": 1005,
                        "name": "Arcadia's Cauldron",
                        "desc": "A cozy apothecary brimming with ingredients and potions, run by the alchemist Arcadia.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "economic_activity_alchemy_ingredient_source_rich", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_giver_potential_arcadia"]
                    },
                    {
                        "id": 1006,
                        "name": "Temple of Kynareth",
                        "desc": "A serene temple devoted to the wind and healing, centered around the ancient Gildergreen tree and frequented by worshippers.",
                        "tags": ["structure_type_temple_building", "settlement_features_temple_specific_god", "religious_site_aedric", "magical_properties_holy_ground_aedric", "healing_services", "kynareth_shrine", "unique_landmark_iconic_gildergreen", "quest_location_gildergreen_restoration"]
                    },
                    {
                        "id": 1007,
                        "name": "Plains District Market",
                        "desc": "Bustling stalls offering regional produce, crafts, and curiosities, the commercial heart of Whiterun.",
                        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "item_type_food_vendor", "item_type_general_goods_vendor_stalls"]
                    },
                    {
                        "id": 1008,
                        "name": "The Drunken Huntsman",
                        "desc": "A tavern popular with hunters and adventurers, known for its rustic charm and owned by Elrindir.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "hunter_gathering_spot", "bosmer_influence_minor", "food_drink_vendor", "lodging_available", "rumor_source"]
                    },
                    {
                        "id": 1009,
                        "name": "Belethor's General Goods",
                        "desc": "A shop stocking a wide variety of items, where Belethor claims everything is for sale... if the price is right.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety_extensive", "eccentric_merchant_owner_belethor", "item_type_various_vendor"]
                    },
                    {
                        "id": 1010,
                        "name": "Hall of the Dead",
                        "desc": "A solemn place beneath the Temple of Kynareth where the Nords of Whiterun honor their ancestors and inter their dead.",
                        "tags": ["structure_type_catacombs_structure", "religious_site_aedric", "nordic_burial_site_major", "arkay_presence_strong", "undead_presence_rumored_low", "quest_location_investigation_potential"]
                    },
                    {
                        "id": 1011,
                        "name": "Carlotta Valentia's House",
                        "desc": "The home of Carlotta Valentia, a food vendor in the market, and her daughter Mila.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "family_dwelling_single_mother"]
                    },
                    {
                        "id": 1012,
                        "name": "House Gray-Mane",
                        "desc": "A prominent and respected Nord family in Whiterun, known for their traditional values and quiet concerns about Imperial policies.",
                        "tags": ["structure_type_residence_noble", "noble_estate_district", "nordic_culture_strong_traditional", "political_tension_high_family_feud", "stormcloak_sympathizers_potential", "political_family_gray_mane"]
                    },
                    {
                        "id": 1013,
                        "name": "House Battle-Born",
                        "desc": "A wealthy and influential Nord family in Whiterun, strong supporters of the Empire and Imperial traditions.",
                        "tags": ["structure_type_residence_noble", "noble_estate_district", "imperial_influence_strong", "political_tension_high_family_feud", "political_family_battle_born"]
                    },
                    {
                        "id": 1014,
                        "name": "Breezehome",
                        "desc": "A modest but cozy home available for purchase in Whiterun, conveniently located near the city gates.",
                        "tags": ["structure_type_residence", "player_home_available", "urban_dwelling_modest"]
                    }
                ]
            },
            {
                "id": 11,
                "name": "Riverwood",
                "desc": "A quaint logging village along the White River, known for its simplicity and rustic charm, often the first stop for travelers from the south.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_logging_timber", "terrain_river_delta", "climate_temperate", "terrain_forest", "travel_hub_minor", "quest_location_main_story_early_dragon_attack_aftermath_potential"],
                "sub_locations": [
                    {
                        "id": 1101,
                        "name": "Sleeping Giant Inn",
                        "desc": "A warm inn that serves as a gathering point for weary travelers and locals, run by Orgnar.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available"]
                    },
                    {
                        "id": 1102,
                        "name": "Riverwood Trader",
                        "desc": "A modest shop offering a variety of everyday goods, run by Lucan Valerius and his sister Camilla.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "quest_location_golden_claw"]
                    },
                    {
                        "id": 1103,
                        "name": "Alvor's Smithy",
                        "desc": "The local blacksmith renowned for practical and durable tools, run by Alvor.",
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "crafting_tools", "imperial_sympathizers_potential", "item_type_weapon_vendor_basic", "item_type_armor_vendor_basic"]
                    },
                    {
                        "id": 1104,
                        "name": "Faendal's House",
                        "desc": "The home of Faendal, a Bosmer archer and lumberjack in Riverwood.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "bosmer_influence_minor", "quest_giver_potential_faendal_camilla_love_triangle"]
                    },
                    {
                        "id": 1105,
                        "name": "Sven and Hilde's House",
                        "desc": "The home of Sven, a local bard, and his mother Hilde.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "bard_dwelling", "quest_giver_potential_sven_camilla_love_triangle"]
                    }
                ]
            },
            {
                "id": 12,
                "name": "Rorikstead",
                "desc": "A fertile farming village that supplies Whiterun with produce. Despite its prosperity, some whisper of strange pacts or hidden influences behind its unusual success.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_farming_crops", "terrain_plains", "climate_temperate", "magical_properties_enchanted_neutral_prosperity_rumor", "daedric_influence_subtle_rumor", "mystery_local_unusual_success"],
                "sub_locations": [
                    {
                        "id": 1201,
                        "name": "Frostfruit Inn",
                        "desc": "A cozy inn known for its warm hearth and local cider, run by Mralki.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "food_drink_vendor", "lodging_available"]
                    },
                    {
                        "id": 1202,
                        "name": "Rorikstead General Supplies",
                        "desc": "A small stall or shop run by a local, offering essential supplies and some farm produce.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety_limited"]
                    },
                    {
                        "id": 1203,
                        "name": "Lemkil's Farmhouse",
                        "desc": "The farmstead of Lemkil, a local farmer in Rorikstead with two daughters.",
                        "tags": ["structure_type_farmstead", "structure_type_residence", "economic_activity_farming_crops", "social_issue_child_abuse_potential"]
                    },
                    {
                        "id": 1204,
                        "name": "Jouane Manette's House",
                        "desc": "The home of Jouane Manette, a Breton farmer in Rorikstead.",
                        "tags": ["structure_type_farmstead", "structure_type_residence", "economic_activity_farming_crops", "breton_settler"]
                    }
                ]
            },
            {
                "id": 13,
                "name": "Honningbrew Meadery",
                "desc": "Famed for its exceptionally smooth mead, a visit here is both a taste of history and local culture. It has recently faced competition and sabotage.",
                "tags": ["structure_type_meadery_building", "economic_activity_brewing_mead_ale", "shop_specialty_goods_mead", "quest_location_thieves_guild", "sabotage_target_potential", "economic_competition_black_briar"]
            },
            {
                "id": 14,
                "name": "Western Watchtower",
                "desc": "An old, ruined guard tower on the outskirts of Whiterun, fallen into disrepair over the years. It stands as a lonely sentinel over the plains, a relic of past conflicts.",
                "tags": ["structure_type_ruined_tower", "cultural_historical_significance_historic_site", "dragon_lore_ancient_site_attack_recent", "state_or_condition_current_recently_attacked_recovering", "battlefield_minor_historic_dragon_attack", "quest_location_main_story_early_dragon_investigation"]
            },
            {
                "id": 15,
                "name": "Bleak Falls Barrow",
                "desc": "An ancient Nordic tomb high among the mountains overlooking Riverwood, crawling with draugr and secrets of old, including a Word Wall.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "specific_landmark_type_word_wall_location", "quest_location_main_story_early_dragonstone", "puzzle_dragon_claw_golden", "cultural_historical_significance_nordic_ancient_site", "terrain_mountainous_overlook"]
            },
            {
                "id": 16,
                "name": "Silent Moons Camp",
                "desc": "A clandestine bandit camp hidden in the wilderness north-west of Whiterun, known for its lunar-enchanted weapons.",
                "tags": ["bandit_minor_camp", "structure_type_ruined_settlement_forge", "dungeon_minor", "magical_properties_enchanted_neutral_lunar", "specific_landmark_type_lunar_forge", "weapon_enchanting_site_lunar", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 17,
                "name": "Lund's Hut",
                "desc": "A small, isolated hut north of Rorikstead, once home to the unfortunate Lund.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_abandoned", "environment_wilderness", "tragedy_site_minor_death", "magical_properties_haunted_aura_potential", "isolated_location"]
            },
            {
                "id": 18,
                "name": "Gjukar's Monument",
                "desc": "A stone monument south of Rorikstead, marking the site of an ancient battle and the resting place of the warrior Gjukar.",
                "tags": ["structure_type_monument_historic_site", "cultural_historical_significance_battlefield_historic_ancient", "magical_properties_haunted_aura_potential", "nordic_burial_site_major_nearby_rumor", "quest_location_minor_investigation_potential"]
            },
            {
                "id": 19,
                "name": "Secunda's Kiss",
                "desc": "A giant's camp located west of Whiterun, named for the nearby moon Secunda.",
                "tags": ["specific_landmark_type_giant_camp_established", "environment_wilderness", "terrain_plains", "mammoth_herd_grazing", "neutral_encounter_giant_mammoth"]
            },
            {
                "id": 10001,
                "name": "Sleeping Tree Camp",
                "desc": "A giant's camp west of Whiterun, notable for a strange, glowing tree and the potent sap it produces.",
                "tags": ["specific_landmark_type_giant_camp_established", "unique_natural_formation_glowing_tree", "alchemy_ingredient_source_rich_sleeping_tree_sap", "magical_properties_enchanted_neutral_tree", "mystery_local_origin_of_tree", "quest_giver_potential_ysolda_sap"]
            },
            {
                "id": 10002,
                "name": "Swindler's Den",
                "desc": "A cave system west of Whiterun, serving as a hideout for bandits and perhaps some Alik'r warriors if circumstances align.",
                "tags": ["structure_type_natural_cave", "bandit_main_stronghold", "dungeon_major_multi_level", "quest_location_main_story_early_redguard_woman", "faction_alikr_warriors_presence_potential", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 10003,
                "name": "White River Watch",
                "desc": "A small cave east of Honningbrew Meadery, inhabited by bandits led by Hajvarr Iron-Hand.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "terrain_river_delta_overlook", "state_or_condition_current_bandit_controlled_area", "quest_giver_potential_rescue_hostage"]
            },
            {
                "id": 10004,
                "name": "Halted Stream Camp",
                "desc": "A bandit-occupied iron mine north of Whiterun, containing a spell tome for Transmute Ore.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "state_or_condition_current_bandit_controlled_area", "dungeon_minor", "magical_properties_arcane_focus_transmute_ore", "spell_tome_location_transmute", "resource_node_iron"]
            },
            {
                "id": 10005,
                "name": "Chillfurrow Farm",
                "desc": "A prosperous farm run by Wilmuth and his family, just outside Whiterun's walls, known for its diverse crops.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "economic_activity_farming_livestock", "settlement_minor", "terrain_plains_whiterun_outskirts", "family_owned_farm"]
            },
            {
                "id": 10006,
                "name": "Pelagia Farm",
                "desc": "The farmstead of Severio Pelagia, located near Whiterun, contributing to the city's food supply.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "settlement_minor", "terrain_plains_whiterun_outskirts", "quest_giver_potential_farm_issues"]
            },
            {
                "id": 10007,
                "name": "Valtheim Towers",
                "desc": "A pair of fortified towers spanning the White River east of Whiterun, often occupied by bandits demanding tolls.",
                "tags": ["structure_type_ruined_tower_pair", "structure_condition_ruined_extensively", "bandit_minor_camp", "terrain_river_delta_crossing", "dungeon_minor", "strategic_lookout_decayed_river_crossing", "toll_road_illegal_bandit_controlled", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 10008,
                "name": "Greenspring Hollow",
                "desc": "A small, secluded cave known for its natural spring and unique mosses, sometimes used as a hunter's shelter or a troll's den.",
                "tags": ["structure_type_natural_cave", "unique_natural_formation_spring_mosses", "alchemy_ingredient_source_rich_unique_flora", "monster_den_troll_potential", "environment_wilderness", "secluded_nature_spot", "dungeon_minor"]
            },
            {
                "id": 10009,
                "name": "Redoran's Retreat",
                "desc": "A small, damp cave west of Whiterun, often used as a hideout by a lone bandit or a small group of outcasts.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "environment_wilderness", "terrain_hilly_west_whiterun", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 10010,
                "name": "Guldun Rock Overlook",
                "desc": "A rocky outcrop near the Whiterun plains, offering a strategic view. Sometimes used by hunters as a lookout or temporarily inhabited by wildlife.",
                "tags": ["terrain_hilly_rocky_outcrop", "environment_wilderness", "scenic_vista_panoramic_plains_view", "hunter_gathering_spot", "monster_den_wolf_potential", "exploration_point_minor"]
            },
            {
                "id": 10011,
                "name": "Dustman's Cairn",
                "desc": "An ancient Nordic barrow west of Whiterun, a significant site for the Companions and haunted by draugr.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "faction_companions_related_quest", "cultural_historical_significance_nordic_ancient_site", "cultural_historical_significance_ysgramor_related_site_potential", "faction_silver_hand_presence_lair_potential", "artifact_location_wuuthrad_fragment_potential"]
            },
            {
                "id": 10012,
                "name": "Fellglow Keep",
                "desc": "A ruined fort east of Whiterun, now overrun by necromancers and their experiments. It holds forbidden knowledge and dangerous foes.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_necromancer_tower_or_lair", "magical_properties_tainted_by_dark_magic", "dungeon_major", "faction_college_of_winterhold_related_quest", "forbidden_knowledge_dangerous_books", "monster_den_undead_experiments", "mage_lair_hostile_necromancer"]
            },
            {
                "id": 10013,
                "name": "Battle-Born Farm",
                "desc": "A prosperous farm outside Whiterun, owned and operated by the Battle-Born family, known for its crops and livestock.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "economic_activity_farming_livestock", "noble_estate_district_outskirts", "imperial_influence_strong", "political_family_battle_born_farm", "whiterun_outskirts"]
            },
            {
                "id": 10014,
                "name": "Gray-Mane Farm",
                "desc": "A traditional Nord farmstead near Whiterun, belonging to the Gray-Mane family, reflecting their more rustic and independent values.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "economic_activity_farming_livestock", "nordic_culture_strong_traditional", "terrain_plains_whiterun_outskirts", "political_family_gray_mane_farm", "stormcloak_sympathizers_potential"]
            },
            {
                "id": 10015,
                "name": "Whiterun Pass Cave",
                "desc": "A small cave system that cuts through the hills near Whiterun, sometimes used by travelers as a shortcut or by creatures as a den.",
                "tags": ["structure_type_natural_cave", "terrain_mountain_pass_shortcut", "monster_den_bear_potential", "travel_route_alternative_dangerous", "dungeon_minor", "exploration_point_minor"]
            },
            {
                "id": 10016,
                "name": "Granite Hill Redoubt",
                "desc": "A fortified bandit encampment built into the rocky hills west of Whiterun, a source of trouble for local farms and travelers.",
                "tags": ["bandit_main_stronghold", "structure_type_fortified_camp_ruin_integrated", "dungeon_major", "state_or_condition_current_bandit_controlled_area", "terrain_hilly_rocky", "economic_activity_mining_gems_potential_bandit_operated", "quest_location_bounty_leader_potential"]
            },
            {
                "id": 10017,
                "name": "Lone Hunter's Shack",
                "desc": "A small, isolated shack in the plains of Whiterun Hold, home to a reclusive hunter or trapper.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_weathered", "environment_wilderness", "hunter_gathering_spot", "hermit_lair_potential", "terrain_plains", "isolated_location"]
            },
            {
                "id": 10018,
                "name": "Shrine of Talos (Wilderness - Whiterun)",
                "desc": "A small, weathered outdoor shrine dedicated to Talos, hidden among the rocks and trees of Whiterun's plains, a place of quiet worship for loyal Nords.",
                "tags": ["structure_type_shrine_outdoor_structure", "religious_site_aedric_secret_talos", "talos_shrine", "nordic_culture_strong_resistance", "secluded_nature_spot", "magical_properties_holy_ground_aedric", "political_tension_high_religious_banned_worship"]
            },
            {
                "id": 10019,
                "name": "Tundra Homestead",
                "desc": "A modest farmstead with a sturdy house on the plains east of Whiterun, offering a peaceful life for those who can work the land. (Potential player home)",
                "tags": ["structure_type_farmstead", "player_home_available_purchase", "economic_activity_farming_crops", "terrain_plains_east_whiterun", "settlement_minor", "peaceful_area", "structure_condition_well_maintained"]
            },
            {
                "id": 10020,
                "name": "North Skybound Watch",
                "desc": "A ruined Nordic watchtower and barrow complex on a cliff overlooking the northern plains of Whiterun Hold, containing an ancient Word Wall.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_major_complex", "specific_landmark_type_word_wall_location", "dungeon_major", "undead_presence_strong", "draugr_heavy", "terrain_cliffside_overlook", "dragon_lore_ancient_site", "cultural_historical_significance_nordic_ancient_site"]
            },
            {
                "id": 10021,
                "name": "Whitewatch Mill",
                "desc": "A small, independent lumber mill on the plains of Whiterun Hold, supplying timber for local construction and repairs.",
                "tags": ["structure_type_lumber_mill_site", "economic_activity_logging_timber", "settlement_minor", "terrain_plains_whiterun_hold", "resource_node_wood"]
            },
            {
                "id": 10022,
                "name": "Honey-Hand Farm",
                "desc": "A quaint farmstead and apiary known for its uniquely flavored honey, run by a reclusive family.",
                "tags": ["structure_type_farmstead", "structure_type_apiary_location", "economic_activity_farming_crops", "unique_produce_honey_specialty", "settlement_minor", "isolated_location", "family_owned_farm_reclusive"]
            },
            {
                "id": 10023,
                "name": "Whispering Creek Cave",
                "desc": "A small, damp cave system carved by an underground creek, often home to mudcrabs or other cave dwellers. Sometimes used by bandits as a temporary hideout.",
                "tags": ["structure_type_natural_cave", "dungeon_minor", "monster_den_mudcrab", "bandit_minor_camp_potential_temporary", "terrain_river_delta_nearby_underground_creek", "exploration_point_minor"]
            },
            {
                "id": 10024,
                "name": "Old Kynesgrove Road Ruin",
                "desc": "The crumbling stone remnants of an ancient watchpost or small shrine along a disused stretch of road near the path to Kynesgrove. It offers little shelter but hints at older conflicts.",
                "tags": ["structure_type_ruined_shrine_watchpost", "cultural_historical_significance_nordic_ancient_site_minor", "structure_condition_ruined_extensively", "bandit_minor_camp_potential", "roadside_encounter_point_disused_road", "exploration_point_historic_remnants"]
            },
            {
                "id": 10025,
                "name": "Broken Fang Cave",
                "desc": "A dark, fetid cave that has become a den for a small coven of vampires or their thralls, preying on unwary travelers on the plains.",
                "tags": ["structure_type_natural_cave", "dungeon_minor", "specific_landmark_type_vampire_coven_minor", "undead_presence_strong_vampire_thralls", "environment_wilderness_plains", "magical_properties_tainted_by_dark_magic", "state_or_condition_current_lawless_area_vampire"]
            },
            {
                "id": 10026,
                "name": "Shrine of Stendarr (Whiterun Plains)",
                "desc": "A modest, weathered shrine to Stendarr, the God of Mercy and Justice, offering a place for quiet contemplation and prayer on the open plains.",
                "tags": ["structure_type_shrine_outdoor_structure", "religious_site_aedric", "stendarr_shrine", "magical_properties_holy_ground_aedric", "travel_route_marker_plains", "faction_vigilants_of_stendarr_outpost_potential_minor", "peaceful_area_contemplation"]
            },
            {
                "id": 10027,
                "name": "The Ritual Stone",
                "desc": "An ancient Standing Stone east of Whiterun, near the road to Windhelm. It grants the power to reanimate nearby corpses to fight for the activator, once per day.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_arcane_nexus_necromantic", "necromancy_focus_reanimation", "cultural_historical_significance_ancient_magical_site", "terrain_plains_roadside", "power_reanimate_corpses_daily"]
            },
            {
                "id": 10028,
                "name": "Gallows Hall",
                "desc": "A secluded and ominous ruin near the road west of Windhelm, but technically within Whiterun's old borders. It is rumored to be a former place of execution now haunted and possibly used by necromancers.",
                "tags": ["structure_type_ruined_fort_execution_site", "specific_landmark_type_necromancer_tower_or_lair_potential", "dungeon_minor", "cultural_historical_significance_historic_site_ominous", "magical_properties_tainted_by_dark_magic", "undead_presence_strong_ghosts_skeletons", "magical_properties_haunted_aura_strong", "whiterun_eastmarch_border_area"]
            },
            {
                "id": 10029,
                "name": "Shimmermist Grotto",
                "desc": "A damp cave system northeast of Whiterun, containing both Falmer inhabitants and ancient Dwemer ruins deep within. Known for its glowing mushrooms.",
                "tags": ["structure_type_natural_cave_grotto", "dwemer_ruin_minor_outpost_interior", "falmer_presence_strong", "dungeon_major", "unique_natural_formation_glowing_mushrooms", "alchemy_ingredient_source_rich_glowing_mushrooms", "chaurus_nest_potential", "bioluminescent_flora", "cultural_historical_significance_dwemer_ruin_site"]
            },
            {
                "id": 10030,
                "name": "Hamvir's Rest",
                "desc": "An ancient, desecrated Nordic graveyard and small cairn north-west of Whiterun, now haunted by skeletons and a necromancer.",
                "tags": ["nordic_burial_site_minor_cairn", "dungeon_minor", "undead_presence_strong_skeletons", "specific_landmark_type_necromancer_lair_minor", "structure_condition_desecrated", "magical_properties_haunted_aura_potential", "quest_location_minor_investigation_potential"]
            }
        ]
    },

    # THE PALE
    {
        "id": 2,
        "name": "The Pale",
        "desc": "A frozen hold of bleak beauty, stretching from snow-tipped plains to the Sea of Ghosts. Harsh and unforgiving, known for its mining town of Dawnstar and dangerous wildlife. Strong Stormcloak sentiment prevails here.",
        "tags": ["hold", "climate_arctic", "terrain_ice_field", "terrain_tundra_plains", "environment_coastal", "economic_activity_mining_quicksilver", "economic_activity_mining_iron", "nordic_culture_strong", "stormcloak_presence_strong_leaning", "state_or_condition_current_isolated_and_forgotten", "dangerous_wildlife_ice_wraiths_trolls", "travel_hub_sea_northern_ports_potential"],
        "demographics": {"Nord": 90, "Imperial": 5, "Others": 5},
        "travel": {
            "roads": ["Whiterun Hold", "Winterhold", "Eastmarch", "Hjaalmarch"],
            "paths": ["Icespire Trail", "Frostmere Road"]
        },
        "sub_locations": [
            {
                "id": 20,
                "name": "Dawnstar",
                "desc": "A resilient port town on the northern coast, thriving on fishing and mining. It is currently plagued by mysterious nightmares affecting its populace.",
                "tags": ["populated_town", "settlement_features_docks_harbor", "city_affiliation_dawnstar_town", "state_or_condition_current_isolated_and_forgotten", "economic_activity_mining_quicksilver", "economic_activity_fishing_industry_local", "urban_issues_or_atmosphere_haunted_rumors_strong_nightmares", "daedric_influence_subtle_rumor_vaermina", "settlement_features_jarls_longhouse", "climate_arctic", "environment_coastal", "quest_location_daedric_vaermina_nightmares"],
                "sub_locations": [
                    {
                        "id": 2001,
                        "name": "Windpeak Inn",
                        "desc": "The cozy inn of Dawnstar, offering respite from the icy winds and a place for locals to gather and discuss the unsettling dreams.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source_nightmares_local_issues", "food_drink_vendor", "lodging_available", "urban_issues_or_atmosphere_fear_and_superstition_nightmares"]
                    },
                    {
                        "id": 2002,
                        "name": "Quicksilver Mine",
                        "desc": "A productive quicksilver mine that is vital to Dawnstar's economy, though some miners report strange occurrences.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_quicksilver", "resource_node_quicksilver", "urban_issues_or_atmosphere_haunted_rumors_strong_mine_related_potential", "economic_backbone_dawnstar"]
                    },
                    {
                        "id": 2003,
                        "name": "The Mortar and Pestle",
                        "desc": "Frida's alchemy shop, where local brews and potions are concocted. Frida may seek rare ingredients.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_giver_potential_ingredient_gathering"]
                    },
                    {
                        "id": 2004,
                        "name": "The White Hall",
                        "desc": "The seat of Dawnstar's Jarl, Skald the Elder, a staunch supporter of Ulfric Stormcloak.",
                        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local_stormcloak_jarl_skald", "stormcloak_presence_strong", "political_family_stormcloak_jarl"]
                    },
                    {
                        "id": 2005,
                        "name": "Rustleif's House and Smithy",
                        "desc": "The home and workshop of Rustleif, Dawnstar's blacksmith, who dreams of returning to his homeland.",
                        "tags": ["structure_type_shop_building", "structure_type_residence", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "crafting_tools", "item_type_weapon_vendor", "item_type_armor_vendor", "quest_giver_potential_personal_item"]
                    },
                    {
                        "id": 2006,
                        "name": "Dawnstar Sanctuary",
                        "desc": "A forgotten and ruined sanctuary of the Dark Brotherhood, hidden near Dawnstar. Its secrets lie buried in snow and shadow.",
                        "tags": ["structure_type_ruined_shrine_sanctuary", "specific_landmark_type_assassin_guild_hq_abandoned_dark_brotherhood", "dungeon_minor", "secret_location_hidden_entrance", "magical_properties_tainted_by_dark_magic", "structure_condition_collapsed_ruined", "faction_dark_brotherhood_historic_site"]
                    }
                ]
            },
            {
                "id": 21,
                "name": "Nightcaller Temple",
                "desc": "An eerie, abandoned temple on a clifftop overlooking Dawnstar. It is sealed, but dark whispers and nightmares emanate from it, hinting at the Daedric Prince Vaermina's influence.",
                "tags": ["structure_type_temple_building_ruined", "structure_condition_ruined_extensively_sealed", "magical_properties_daedric_influence_overt_vaermina", "dungeon_major", "quest_location_daedric_vaermina_skull_of_corruption", "urban_issues_or_atmosphere_haunted_rumors_strong_nightmares_source", "specific_landmark_type_daedric_shrine_prominent", "terrain_cliffside_overlook"]
            },
            {
                "id": 22,
                "name": "Iron-Breaker Mine",
                "desc": "An iron mine located just outside Dawnstar, contributing to the town's resources.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "resource_node_iron", "dawnstar_outskirts", "economic_support_local"]
            },
            {
                "id": 23,
                "name": "Wreck of the Brinehammer",
                "desc": "The ghostly remains of a long-forgotten shipwreck scattered along the storm-battered coast south of Dawnstar. Rumored to hold lost treasures and spectral guardians.",
                "tags": ["structure_type_shipwreck_site", "structure_condition_ruined_extensively_scattered", "dungeon_minor", "environment_coastal_storm_battered", "undead_presence_rumored_strong_ghosts_skeletons", "treasure_cache_rumored_lost_cargo", "exploration_point_historic_wreck"]
            },
            {
                "id": 24,
                "name": "Frostflow Lighthouse",
                "desc": "A solitary lighthouse west of Dawnstar. Its light has recently gone out, and chilling screams were heard from within. A dark mystery involving Falmer awaits discovery.",
                "tags": ["structure_type_lighthouse_structure", "structure_condition_abandoned_light_extinguished", "dungeon_major", "falmer_presence_strong", "quest_location_investigation_family_tragedy", "tragedy_site_family_massacre", "chaurus_nest_major_potential", "urban_issues_or_atmosphere_haunted_rumors_strong_screams"]
            },
            {
                "id": 25,
                "name": "Loreius Farm",
                "desc": "A small farmstead south of Dawnstar, owned by Vantus Loreius, often struggling against the harsh climate.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_struggling", "state_or_condition_current_isolated_and_forgotten", "climate_arctic_edge", "settlement_minor", "quest_giver_potential_local_issues_cicero_related_potential"]
            },
            {
                "id": 26,
                "name": "Nightgate Inn",
                "desc": "An isolated inn located at a pass on the road between The Pale and Eastmarch, a lonely refuge for travelers.",
                "tags": ["structure_type_inn_building", "settlement_features_tavern", "state_or_condition_current_isolated_and_forgotten", "travel_route_marker_mountain_pass", "lodging_available", "food_drink_vendor", "rumor_source_travelers", "quest_giver_potential_local_issues_orc_related_potential"]
            },
            {
                "id": 27,
                "name": "Red Road Pass",
                "desc": "A bandit-infested pass through the mountains in the southern part of The Pale, dangerous for unwary travelers.",
                "tags": ["terrain_mountain_pass", "bandit_main_stronghold", "dungeon_major", "travel_route_alternative_dangerous", "state_or_condition_current_bandit_controlled_area", "quest_location_bounty_leader_potential"]
            },
            {
                "id": 28,
                "name": "Shearpoint",
                "desc": "A mountain peak in The Pale, home to an ancient dragon lair, a Word Wall, and the tomb of the Dragon Priest Krosis.",
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "cultural_historical_significance_dragon_cult_lair_priest_krosis", "terrain_mountain_peak", "dungeon_major", "undead_presence_strong_draugr_priest", "artifact_location_powerful_mask_krosis", "dragon_presence_potential_guardian"]
            },
            {
                "id": 29,
                "name": "Shrouded Grove",
                "desc": "A small, hidden grove in The Pale, sometimes a site for unusual encounters, minor Daedric worship, or hidden alchemical ingredients.",
                "tags": ["environment_wilderness_grove", "terrain_forest_hidden", "magical_properties_enchanted_neutral_subtle", "ritual_site_minor_potential_daedric_nature", "alchemy_ingredient_source_rich_rare_flora", "secluded_nature_spot", "mystery_local_unusual_encounters"]
            },
            {
                "id": 20001,
                "name": "Silverdrift Lair",
                "desc": "A Nordic ruin west of Nightgate Inn, overrun by draugr and ancient guardians.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "cultural_historical_significance_nordic_ancient_site", "treasure_cache_rumored_ancient_nordic", "puzzle_ancient_nordic_potential"]
            },
            {
                "id": 20002,
                "name": "Weynon Stones",
                "desc": "A small ruin southeast of Dawnstar, a circle of ancient stones that hum with faint magical energy, sometimes attracting bandits or mages.",
                "tags": ["structure_type_standing_stone_circle_ruined", "cultural_historical_significance_ancient_magical_site_minor", "magical_properties_arcane_nexus_minor_faint", "bandit_minor_camp_potential", "mage_lair_hostile_potential_minor", "terrain_tundra_plains", "exploration_point_minor_lore"]
            },
            {
                "id": 20003,
                "name": "Fort Dunstad",
                "desc": "A large fort in The Pale, strategically important. Currently garrisoned by Imperial soldiers, but its loyalty could shift with the rising political tensions.",
                "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion", "imperial_influence_strong", "dungeon_major", "state_or_condition_current_contested_by_factions_potential_stormcloak", "civil_war_quest_historic_site_potential", "strategic_location_pale"]
            },
            {
                "id": 20004,
                "name": "Windward Ruins",
                "desc": "Crumbling Nordic ruins on a windswept hill overlooking the Sea of Ghosts, rumored to be haunted by sailors lost to the ice.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_minor_potential", "environment_coastal_windswept_hill", "structure_condition_ruined_extensively", "magical_properties_haunted_aura_sailors_lost", "undead_presence_skeletons_ghosts_potential", "dungeon_minor", "exploration_point_historic_ruin"]
            },
            {
                "id": 20005,
                "name": "Pale Pass",
                "desc": "A treacherous mountain pass leading towards Cyrodiil from the southern Pale, known for blizzards and ice trolls. Currently lightly patrolled by Imperials.",
                "tags": ["terrain_mountain_pass_treacherous", "cultural_historical_significance_historic_site_cyrodiil_border", "state_or_condition_current_contested_by_factions_potential_stormcloak", "imperial_influence_moderate_patrols", "monster_den_ice_troll_major", "climate_arctic_blizzards", "travel_route_major_dangerous_cyrodiil"]
            },
            {
                "id": 20006,
                "name": "Great Henge of the Ice-Speakers",
                "desc": "An ancient and massive stone circle on the northern tundra, believed to have been used by early Atmoran settlers for sky-worship. Rarely visited.",
                "tags": ["structure_type_standing_stone_circle_massive", "cultural_historical_significance_nordic_ancient_site_atmoran_sky_worship", "magical_properties_arcane_nexus_minor_ancient", "state_or_condition_current_isolated_and_forgotten_rarely_visited", "terrain_tundra_plains_northern", "climate_arctic", "exploration_point_major_lore"]
            },
            {
                "id": 20007,
                "name": "Snowpoint Overlook Cave",
                "desc": "A small ice cave high in the mountains of The Pale, offering a chilling view. It might be used by smugglers or serve as a den for ice wraiths.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial", "economic_activity_smuggling_route_active_potential", "monster_den_ice_wraith", "terrain_mountain_peak_high", "dungeon_minor", "scenic_vista_panoramic_chilling", "exploration_point_hidden_cache_potential"]
            },
            {
                "id": 20008,
                "name": "Forgotten Stones of the North",
                "desc": "A small, weathered circle of ancient stones on the tundra of The Pale. Their original purpose is lost to time, but they emanate a faint, cold energy.",
                "tags": ["structure_type_standing_stone_circle_weathered", "cultural_historical_significance_nordic_ancient_site_lost_purpose", "structure_condition_weathered_ancient", "terrain_tundra_plains", "magical_properties_enchanted_neutral_faint_cold_energy", "mystery_local_lost_history", "exploration_point_minor_lore"]
            },
            {
                "id": 20009,
                "name": "Icerunner's Rest",
                "desc": "A tiny, wind-battered fishing hamlet clinging to the icy northern coast of The Pale. Its few inhabitants are hardy folk, accustomed to the harsh sea.",
                "tags": ["populated_village_hamlet", "settlement_minor_fishing", "economic_activity_fishing_industry_local_subsistence", "environment_coastal_icy_northern", "climate_glacial_harsh", "state_or_condition_current_isolated_and_forgotten_hardy_folk"]
            },
            {
                "id": 20010,
                "name": "Snowdrift Cabin",
                "desc": "A solitary trapper's cabin, half-buried in snowdrifts for much of the year, located deep within the snowy plains of The Pale.",
                "tags": ["structure_type_shack_or_hut_trapper", "structure_condition_weathered_snow_buried", "economic_activity_hunting_furs_meat_trapping", "climate_arctic_deep_snow", "terrain_tundra_plains_isolated", "hermit_lair_potential_trapper"]
            },
            {
                "id": 20011,
                "name": "Frostmoon Crag Cave",
                "desc": "An icy cave system high on a crag in The Pale, often glittering with frost and home to ice wraiths or frost trolls.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial_frosty", "dungeon_minor", "monster_den_frost_troll", "monster_den_ice_wraith", "terrain_mountain_peak_crag", "alchemy_ingredient_source_rich_frost_salts_potential"]
            },
            {
                "id": 20012,
                "name": "Ruins of the Lost Patrol",
                "desc": "A scatter of weathered stones and a broken standard on the bleak tundra, marking the last stand of a forgotten Imperial or Stormcloak patrol from a past conflict.",
                "tags": ["structure_type_ruined_settlement_battle_marker", "cultural_historical_significance_battlefield_historic_forgotten_patrol", "magical_properties_haunted_aura_potential_lost_soldiers", "terrain_tundra_plains_bleak", "state_or_condition_current_isolated_and_forgotten", "exploration_point_historic_remnants"]
            },
            {
                "id": 20013,
                "name": "Yorgrim's Overlook",
                "desc": "The crumbling ruins of an ancient Nordic watchtower, named after a forgotten hero. It offers a commanding view of the surrounding tundra but is now home to bandits or wildlife.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_minor_potential", "dungeon_minor", "bandit_minor_camp_potential", "monster_den_wildlife_potential", "scenic_vista_panoramic_tundra_view", "cultural_historical_significance_nordic_ancient_site_hero_yorgrim"]
            },
            {
                "id": 20014,
                "name": "Stillborn Cave (The Pale)",
                "desc": "A small, cold cave system in The Pale, named for a local tragedy or perhaps the eerie silence within. Often inhabited by frost spiders or other cold-dwelling creatures.",
                "tags": ["structure_type_natural_cave_cold", "climate_arctic", "dungeon_minor", "monster_den_frost_spider", "urban_issues_or_atmosphere_haunted_rumors_strong_eerie_silence", "tragedy_site_minor_local_legend", "alchemy_ingredient_source_rich_frostbite_venom_potential"]
            },
            {
                "id": 20015,
                "name": "The Lord Stone",
                "desc": "Found high in the mountains on the border of The Pale, east of Morthal, this Standing Stone grants increased physical resilience and resistance to magical attacks.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive_defensive", "terrain_mountain_peak_border_pale_hjaalmarch", "cultural_historical_significance_ancient_magical_site", "climate_arctic_alpine", "buff_physical_resistance_increased", "buff_magic_resistance_increased"]
            },
            {
                "id": 20016,
                "name": "Korvanjund",
                "desc": "A large Nordic ruin in The Pale, south of Dawnstar. It is an ancient burial site of Nord heroes and kings, rumored to hold significant historical artifacts, possibly including a crown of legend. Heavily guarded by draugr.",
                "tags": ["nordic_burial_site_major_royal_tomb", "dungeon_major", "undead_presence_strong", "draugr_heavy_heroes_kings", "cultural_historical_significance_nordic_ancient_site_heroes_kings", "quest_location_civil_war_jagged_crown", "specific_landmark_type_word_wall_location_potential", "artifact_location_rumored_jagged_crown", "puzzle_ancient_nordic_potential"]
            },
            {
                "id": 20017,
                "name": "Irkngthand",
                "desc": "A massive and ancient Dwemer ruin in The Pale, west of Nightgate Inn. It is a sprawling complex with many dangers, including Falmer and Dwemer constructs. Rumored to hold significant Dwemer artifacts.",
                "tags": ["dwemer_ruin_major_city_complex", "dungeon_large_complex", "falmer_presence_strong", "mechanical_constructs_dwemer_heavy", "quest_location_thieves_guild_eyes_of_falmer", "cultural_historical_significance_dwemer_ruin_site", "specific_landmark_type_blackreach_elevator_access_potential", "chaurus_nest_major_potential", "ancient_technology_dwemer", "treasure_cache_dwemer_artifacts_rumored"]
            },
            {
                "id": 20018,
                "name": "Duskglow Crevice",
                "desc": "A dark, winding cave system in The Pale, south of Dawnstar, infested with Falmer and their chaurus companions. It is a dangerous place, shunned by locals.",
                "tags": ["structure_type_natural_cave_crevice", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_major", "environment_underground_dark_winding", "state_or_condition_current_lawless_area_dangerous", "alchemy_ingredient_source_rich_falmer_ears_chaurus_eggs"]
            }
        ]
    },

    # WINTERHOLD HOLD
    {
        "id": 3,
        "name": "Winterhold Hold",
        "desc": "A shattered hold on the northern coast, defined by icy gales, ancient ruins, and the dominant presence of the College of Winterhold. Much of the original city was lost to the Great Collapse centuries ago.",
        "tags": ["hold", "climate_glacial_extreme_weather", "terrain_ice_field_coastal", "environment_coastal_northern", "magical_properties_arcane_nexus_college", "cultural_historical_significance_great_collapse_affected_site_major", "nordic_culture_ancient_remnants", "faction_college_of_winterhold_dominant_presence", "state_or_condition_current_economically_depressed_shattered", "structure_condition_ruined_extensively_city_lost", "travel_hub_sea_northern_ports_historic_potential"],
        "demographics": {"Nord": 75, "Altmer": 10, "Dunmer": 10, "Others": 5},
        "travel": {
            "roads": ["The Pale", "Eastmarch"],
            "paths": ["Saarthal Trail", "Glacial Path", "Sea of Ghosts Ice Floes (dangerous)"]
        },
        "sub_locations": [
            {
                "id": 30,
                "name": "Winterhold (Town Remnants)",
                "desc": "A shadow of its former self, this small, windswept town clings to the cliffs, overshadowed by the imposing College. Most of the original grand city now lies beneath the waves due to the Great Collapse.",
                "tags": ["populated_town_remnants", "structure_condition_ruined_extensively_city_lost_to_sea", "city_affiliation_winterhold_town_ruined", "magical_properties_arcane_nexus_college_nearby", "cultural_historical_significance_great_collapse_affected_site_epicenter", "state_or_condition_current_isolated_and_forgotten_shadow_of_former_self", "settlement_features_jarls_longhouse", "urban_issues_or_atmosphere_fear_and_superstition_college_mistrust", "climate_glacial_coastal_windswept", "faction_college_of_winterhold_overshadowing_presence"],
                "sub_locations": [
                    {
                        "id": 3001,
                        "name": "The Frozen Hearth",
                        "desc": "The sole remaining inn in Winterhold, offering shelter and rumors to travelers and College members, run by Dagur.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular_local_college", "rumor_source_college_local_issues", "food_drink_vendor", "lodging_available", "structure_condition_weathered_sole_survivor_inn"]
                    },
                    {
                        "id": 3002,
                        "name": "College of Winterhold",
                        "desc": "A venerable institution of magic, perched precariously on a separated clifftop, a beacon for mages across Tamriel. Led by Arch-Mage Savos Aren.",
                        "tags": ["structure_type_guild_hall_building_college", "settlement_features_college_of_winterhold_main", "magical_properties_arcane_nexus_major", "cultural_historical_significance_ancient_magical_site_venerable", "political_tension_high_town_relations", "unique_landmark_iconic_cliff_perch", "quest_location_college_of_winterhold_main_questline", "faction_college_of_winterhold_hq", "education_magic_arcane_arts"],
                        "sub_locations": [
                            {
                                "id": 30021,
                                "name": "The Midden",
                                "desc": "The dark, forgotten underbelly of the College of Winterhold, a network of icy tunnels and chambers. Used for refuse, dangerous experiments, and rumored to hide darker secrets, including the Atronach Forge.",
                                "tags": ["environment_underground_icy_tunnels", "dungeon_major_college_undercroft", "magical_properties_tainted_by_dark_magic_experiments", "specific_landmark_type_atronach_forge_location", "undead_presence_rumored_strong_failed_experiments", "secret_location_college_secrets", "faction_college_of_winterhold_related_dark_secrets", "monster_den_ice_wraith_skeletons_potential"]
                            }
                        ]
                    },
                    {
                        "id": 3003,
                        "name": "Jarl's Longhouse (Winterhold)",
                        "desc": "The modest seat of Winterhold's Jarl Korir, a man bitter about the College's perceived indifference to the town's plight.",
                        "tags": ["structure_type_palace_or_manor_modest", "settlement_features_jarls_longhouse", "government_local_jarl_korir", "structure_condition_weathered_struggling", "political_tension_high_college_mistrust_bitterness"]
                    },
                    {
                        "id": 3004,
                        "name": "Birna's Oddments",
                        "desc": "A small shop run by Birna, offering a curious selection of goods, often scavenged or of questionable origin.",
                        "tags": ["structure_type_shop_building", "shop_general_goods_oddments", "trade_variety_limited_scavenged", "economic_activity_trade_hub_minor_struggling", "structure_condition_weathered", "quest_giver_potential_coral_dragon_claw"]
                    }
                ]
            },
            {
                "id": 31,
                "name": "Saarthal",
                "desc": "The excavated ruins of one of Skyrim's first human settlements, a site of great magical power and ancient Nordic mysteries, closely tied to the College of Winterhold's studies.",
                "tags": ["nordic_burial_site_major_excavated", "dungeon_major", "undead_presence_strong", "draugr_heavy", "magical_properties_arcane_nexus_powerful", "faction_college_of_winterhold_related_quest_excavation", "cultural_historical_significance_nordic_ancient_site_first_settlement", "artifact_location_powerful_eye_of_magnus_related", "puzzle_ancient_magic_nordic", "quest_location_college_of_winterhold_early"]
            },
            {
                "id": 32,
                "name": "Hob's Fall Cave",
                "desc": "A shadowy coastal cave north of Winterhold, a den for necromancers and their unholy experiments, or perhaps desperate smugglers.",
                "tags": ["structure_type_natural_cave_coastal", "specific_landmark_type_necromancer_lair_potential", "economic_activity_smuggling_route_active_potential", "dungeon_minor", "environment_coastal_northern", "magical_properties_tainted_by_dark_magic_potential", "undead_presence_skeletons_potential", "mage_lair_hostile_potential_necromancer", "quest_giver_potential_purity_of_essence_potion"]
            },
            {
                "id": 33,
                "name": "Yngol Barrow",
                "desc": "A mournful Nordic tomb east of Windhelm (close to Winterhold's border), where ancient magics linger and the ghost of Yngol's shade may be found by those seeking its secrets.",
                "tags": ["nordic_burial_site_major_mournful", "dungeon_major", "undead_presence_strong_ghosts_draugr", "magical_properties_haunted_aura_strong", "cultural_historical_significance_legendary_hero_location_ysgramor_son_yngol", "artifact_location_unique_item_helm_of_yngol", "puzzle_ancient_nordic_coral_claw_potential", "quest_location_investigation_legend"]
            },
            {
                "id": 34,
                "name": "Alftand",
                "desc": "A vast and treacherous Dwemer ruin deep within the mountains of Winterhold, one of the primary known entrances to the subterranean realm of Blackreach. It is a dangerous place, still patrolled by ancient constructs and inhabited by Falmer.",
                "tags": ["dwemer_ruin_major_city_complex", "dungeon_large_complex_treacherous", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "specific_landmark_type_blackreach_elevator_access", "quest_location_main_story_elder_scroll_potential", "cultural_historical_significance_dwemer_ruin_site_major", "chaurus_nest_major_potential", "structure_condition_ruined_extensively_icy", "ancient_technology_dwemer", "terrain_mountainous_winterhold_deep"],
                "sub_locations": [
                    {
                        "id": 3401,
                        "name": "Alftand Glacial Ruins",
                        "desc": "The icy, upper exterior sections of Alftand, often patrolled by Falmer and ice wraiths.",
                        "tags": ["dwemer_ruin_minor_outpost_exterior", "climate_glacial_icy", "monster_den_ice_wraith", "falmer_presence_scouts_patrols", "structure_condition_ruined_extensively_glacial", "dungeon_minor_exterior_section"]
                    },
                    {
                        "id": 3402,
                        "name": "Alftand Animonculory",
                        "desc": "The main Dwemer manufactory within Alftand, filled with constructs, traps, and remnants of Dwemer machinery.",
                        "tags": ["dwemer_ruin_major_city_section_animonculory", "mechanical_constructs_dwemer_heavy_manufactory", "trap_heavy_environment_dwemer", "ancient_technology_dwemer_machinery", "falmer_presence_strong_infestation", "dungeon_major_interior_section"]
                    },
                    {
                        "id": 3403,
                        "name": "Alftand Cathedral",
                        "desc": "The grand central chamber of Alftand, leading deeper into the earth towards Blackreach. A place of significant Dwemer engineering.",
                        "tags": ["dwemer_ruin_major_city_section_cathedral", "structure_type_temple_building_dwemer_grand_chamber", "specific_landmark_type_blackreach_elevator_access_main", "mechanical_constructs_dwemer_boss_potential_centurion", "falmer_presence_strong_guardians", "dungeon_major_central_hub", "ancient_technology_dwemer_engineering_feat"]
                    }
                ]
            },
            {
                "id": 35,
                "name": "Frostmere Crypt",
                "desc": "A Nordic barrow on the border between The Pale and Winterhold, rumored to be home to bandits and a legendary spectral weapon known as 'The Pale Blade'.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong_draugr_ghosts", "bandit_minor_camp_potential_surface_or_interior", "quest_location_local_legend_pale_blade", "artifact_location_unique_item_pale_blade", "magical_properties_haunted_aura_strong", "terrain_pale_winterhold_border"]
            },
            {
                "id": 36,
                "name": "Pilgrim's Trench",
                "desc": "A shipwreck graveyard in the icy waters north of Winterhold, a treacherous area for sailors, rumored to hold lost cargo and attract scavengers.",
                "tags": ["structure_type_shipwreck_site_graveyard", "environment_coastal_icy_waters", "climate_glacial", "treasure_cache_rumored_lost_cargo", "dangerous_underwater_exploration_freezing", "monster_den_slaughterfish_potential", "exploration_point_multiple_wrecks"]
            },
            {
                "id": 37,
                "name": "Sightless Pit",
                "desc": "A deep, dark chasm leading into a Falmer-infested cave system, located in the southwestern mountains of Winterhold. A place of utter darkness and terror.",
                "tags": ["structure_type_natural_cave_chasm", "falmer_presence_strong_major_den", "dungeon_major_deep_dark", "terrain_canyon_deep_chasm", "environment_underground_utter_darkness", "chaurus_nest_major", "state_or_condition_current_lawless_area_falmer_territory", "exploration_challenge_extreme_danger"]
            },
            {
                "id": 38,
                "name": "Skytemple Ruins",
                "desc": "Ruined Nordic towers atop a desolate mountain, offering a commanding view of Winterhold's icy expanse but little shelter from the biting winds.",
                "tags": ["structure_type_ruined_tower_nordic_pair", "nordic_burial_site_minor_potential", "terrain_mountain_peak_desolate", "structure_condition_ruined_extensively_windswept", "climate_glacial_biting_winds", "scenic_vista_panoramic_icy_expanse", "exploration_point_minor_ruin"]
            },
            {
                "id": 39,
                "name": "Snowpoint Beacon",
                "desc": "A ruined watchtower on the northern coast of Winterhold, now a desolate landmark against the frozen sea.",
                "tags": ["structure_type_ruined_tower_watchtower", "environment_coastal_northern", "structure_condition_abandoned_desolate", "state_or_condition_current_isolated_and_forgotten", "climate_glacial", "exploration_point_minor_landmark"]
            },
            {
                "id": 30001,
                "name": "Ysgramor's Tomb",
                "desc": "The final resting place of the legendary Ysgramor, founder of the Companions and leader of the Five Hundred Companions. A revered and dangerous Nordic tomb, closely guarded by the spirits of ancient heroes.",
                "tags": ["nordic_burial_site_major_revered", "cultural_historical_significance_legendary_hero_location_ysgramor", "faction_companions_related_quest_final", "undead_presence_strong_ancient_hero_spirits", "draugr_heavy", "dungeon_major", "quest_location_companions_guild_hall_final_trial", "artifact_location_powerful_wuuthrad_potential_return", "puzzle_ancient_nordic_companions_lore"]
            },
            {
                "id": 30002,
                "name": "The Serpent Stone",
                "desc": "A Standing Stone located on an island in the Sea of Ghosts, north of the College of Winterhold, granting a unique paralytic magical power once per day.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_offensive", "terrain_island_sea_of_ghosts", "environment_coastal_northern", "climate_glacial", "power_paralysis_ranged_daily", "cultural_historical_significance_ancient_magical_site"]
            },
            {
                "id": 30003,
                "name": "Driftshade Refuge",
                "desc": "An abandoned fort in Winterhold, which rumors say was once used by a renegade group of mages or, more recently, became a den for ice wraiths or desperate bandits.",
                "tags": ["structure_type_ruined_fort", "structure_condition_abandoned_ruined", "monster_den_ice_wraith_potential", "bandit_minor_camp_potential", "dungeon_minor", "specific_landmark_type_silver_hand_hq_potential_alt", "mage_lair_hostile_potential_renegade", "exploration_point_historic_ruin"]
            },
            {
                "id": 30004,
                "name": "Bleakcoast Cave",
                "desc": "A desolate ice cave on the northern coast, home to frost trolls and other hardy creatures adapted to the extreme cold.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial_desolate", "monster_den_frost_troll_major", "environment_coastal_northern", "dungeon_minor", "terrain_ice_field_coastal", "alchemy_ingredient_source_rich_troll_fat_potential"]
            },
            {
                "id": 30005,
                "name": "The Wreck of the Winter Warbler",
                "desc": "A shipwreck frozen in the ice along Winterhold's northern coast, its treasures and the fate of its crew preserved in the cold.",
                "tags": ["structure_type_shipwreck_site_frozen_in_ice", "structure_condition_ruined_extensively_preserved_in_ice", "environment_coastal_northern", "climate_glacial", "treasure_cache_rumored_lost_cargo", "undead_presence_skeletons_potential_frozen_crew", "dungeon_minor", "exploration_point_historic_wreck"]
            },
            {
                "id": 30006,
                "name": "Japhet's Folly",
                "desc": "A small, isolated tower on an island far off the coast of Winterhold, rumored to be the retreat of a mad wizard or a hidden pirate cache. Currently, it is mostly a ruin battered by storms.",
                "tags": ["structure_type_ruined_tower_isolated", "terrain_island_remote_sea_of_ghosts", "state_or_condition_current_isolated_and_forgotten_storm_battered", "magical_properties_enchanted_neutral_potential_mad_wizard", "specific_landmark_type_pirate_cove_hidden_potential", "environment_coastal", "climate_glacial", "quest_location_college_of_winterhold_potential_investigation", "dungeon_minor"]
            },
            {
                "id": 30007,
                "name": "Frostedge Fishery",
                "desc": "A struggling fishing outpost on the treacherous icy coast of Winterhold, where a few hardy souls attempt to make a living from the frozen sea.",
                "tags": ["populated_village_outpost", "settlement_minor_fishing", "economic_activity_fishing_industry_local_struggling", "environment_coastal_treacherous_icy", "climate_glacial_harsh", "state_or_condition_current_economically_depressed_isolated"]
            },
            {
                "id": 30008,
                "name": "Hermit's Peak Cave",
                "desc": "A small, somewhat habitable ice cave high in the mountains of Winterhold, rumored to be the dwelling of a reclusive mage or a forgotten scholar.",
                "tags": ["structure_type_natural_cave_ice_habitable", "climate_glacial_high_altitude", "terrain_mountain_peak", "hermit_lair_potential_mage_scholar", "magical_properties_arcane_focus_minor_potential", "dungeon_minor", "exploration_point_hidden_retreat"]
            },
            {
                "id": 30009,
                "name": "Glacial Crevice",
                "desc": "A narrow, icy fissure in the mountains of Winterhold, leading to a small, frigid cave system. Often home to ice wraiths or other cold-dwelling creatures.",
                "tags": ["structure_type_natural_cave_ice_fissure", "climate_glacial_frigid", "dungeon_minor", "monster_den_ice_wraith", "terrain_mountain_pass_narrow", "unique_natural_formation_glacial_crevice", "exploration_point_dangerous_passage"]
            },
            {
                "id": 30010,
                "name": "Forgotten Scholar's Hovel",
                "desc": "The collapsed remains of a small, ancient stone hovel, half-buried in snow. A few weathered books or scrolls might hint at its former occupant.",
                "tags": ["structure_type_ruined_shack_hovel", "cultural_historical_significance_historic_site_minor_scholar", "structure_condition_collapsed_snow_buried", "lore_clue_potential_weathered_books_scrolls", "climate_glacial", "terrain_ice_field_isolated", "exploration_point_historic_remnants"]
            },
            {
                "id": 30011,
                "name": "Snow-Shod Stables & Farm (Winterhold Outskirts)",
                "desc": "A surprisingly resilient farm and stables on the very edge of Winterhold's domain, perhaps benefiting from minor College enchantments to ward off the worst of the cold. They breed hardy northern ponies.",
                "tags": ["structure_type_farmstead", "structure_type_stable_building", "economic_activity_farming_livestock_hardy_ponies", "settlement_minor_resilient", "climate_arctic_edge_winterhold", "magical_properties_enchanted_neutral_potential_college_wards", "resource_node_horses_northern_breed"]
            },
            {
                "id": 30012,
                "name": "Whistling Mine",
                "desc": "A tiny, struggling mining outpost in the northern cliffs of Winterhold, where miners brave the biting winds to extract a rare, ice-infused ore said to hum faintly.",
                "tags": ["populated_village_outpost_mining", "settlement_minor_struggling", "economic_activity_mining_gems_rare_ice_ore", "structure_type_mine_active_small", "climate_glacial_cliffs", "state_or_condition_current_isolated_and_forgotten_struggling", "magical_properties_enchanted_neutral_potential_humming_ore", "resource_node_rare_ore"]
            },
            {
                "id": 30013,
                "name": "Shrine of Jhunal (Lost)",
                "desc": "The snow-swept, crumbling ruins of an ancient shrine dedicated to Jhunal, the Nordic god of knowledge and runes, predating the College's dominance. A few weathered carvings remain.",
                "tags": ["structure_type_ruined_shrine_nordic", "religious_site_aedric_jhunal_runes_knowledge", "cultural_historical_significance_nordic_ancient_site_pre_college", "magical_properties_arcane_focus_minor_potential_runic", "lore_clue_potential_weathered_carvings", "climate_glacial", "terrain_ice_field_snow_swept", "exploration_point_historic_religious_site"]
            },
            {
                "id": 30014,
                "name": "Frozen Mammoth Cave",
                "desc": "A glacial cave where an ancient mammoth was flash-frozen millennia ago. The cave is now home to ice wraiths and other frost creatures, drawn to its intense cold.",
                "tags": ["structure_type_natural_cave_ice", "climate_glacial_intense_cold", "dungeon_minor", "monster_den_ice_wraith_frost_creatures", "unique_natural_formation_flash_frozen_mammoth", "cultural_historical_significance_historic_site_prehistoric_remains", "alchemy_ingredient_source_rich_mammoth_tusk_potential"]
            },
            {
                "id": 30015,
                "name": "The Tower Stone",
                "desc": "Located on a windswept clifftop along Winterhold's icy coast, this Standing Stone grants the power to once a day open any expert-level or lower lock.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_utility", "environment_coastal_icy_clifftop", "terrain_cliffside_windswept", "cultural_historical_significance_ancient_magical_site", "power_unlock_expert_locks_daily", "utility_buff_lockpicking"]
            },
            {
                "id": 30016,
                "name": "Mount Anthor",
                "desc": "A high mountain peak on the border of Winterhold and The Pale, known in ancient legends as a dragon lair. While no dragons have been seen for centuries, it holds an ancient Word Wall.",
                "tags": ["terrain_mountain_peak_high", "specific_landmark_type_dragon_lair_ancient_inactive_legendary", "specific_landmark_type_word_wall_location", "dungeon_minor_lair_potential", "cultural_historical_significance_dragon_lore_site_ancient", "climate_glacial_alpine", "state_or_condition_current_isolated_and_forgotten", "exploration_point_remote_lore"]
            },
            {
                "id": 30018,
                "name": "Yngvild",
                "desc": "An icy Nordic ruin on an island northeast of Dawnstar (near Winterhold border). It is haunted by the ghosts of women enthralled by the necromancer Arondil.",
                "tags": ["nordic_burial_site_major_icy", "structure_condition_ruined_extensively", "dungeon_major", "specific_landmark_type_necromancer_lair_arondil", "magical_properties_haunted_aura_strong_enthralled_ghosts", "undead_presence_strong_ghosts_draugr", "quest_location_investigation_necromancer_arondil", "terrain_island_northeast_dawnstar", "environment_coastal", "climate_glacial", "artifact_location_unique_item_potential_arondils_journals"]
            }
        ]
    },

    # HJAALMARCH (Morthal Hold)
    {
        "id": 4,
        "name": "Hjaalmarch",
        "desc": "A bleak, marshy hold shrouded in perpetual mist and steeped in superstition. Its capital, Morthal, is known for its reclusive nature and recent troubles with strange occurrences and whispers of vampirism.",
        "tags": ["hold", "terrain_marsh_swamp_dominant", "state_or_condition_current_isolated_and_forgotten_bleak", "nordic_culture_local_reclusive", "urban_issues_or_atmosphere_fear_and_superstition_pervasive", "magical_properties_daedric_influence_subtle_rumor_vampirism", "climate_swampy_misty", "environment_wilderness_marshland", "political_tension_high_potential_jarl_seer", "economic_activity_logging_timber_minor", "economic_activity_mining_iron_minor"],
        "demographics": {"Nord": 95, "Others": 5},
        "travel": {
            "roads": ["The Pale", "The Reach", "Haafingar"],
            "paths": ["Stonehills Trail", "Drajkmyr Marsh Path"]
        },
        "sub_locations": [
            {
                "id": 40,
                "name": "Morthal",
                "desc": "A somber town built on the edge of the Drajkmyr Marsh, wrapped in fog and mystery. Its Jarl, Idgrod Ravencrone, is a seer, and the town is currently dealing with unease from a recent fire and talk of vampires.",
                "tags": ["populated_town", "terrain_marsh_edge_drajkmyr", "city_affiliation_morthal_town", "urban_issues_or_atmosphere_fear_and_superstition_vampires_fire", "magical_properties_daedric_influence_subtle_rumor_vampirism", "settlement_features_jarls_longhouse_idgrod_seer", "state_or_condition_current_isolated_and_forgotten_somber", "quest_location_vampire_investigation_laid_to_rest", "climate_swampy_foggy", "nordic_architecture_local_wood"],
                "sub_locations": [
                    {
                        "id": 4001,
                        "name": "Highmoon Hall",
                        "desc": "The austere residence of Jarl Idgrod Ravencrone and her family, where she contemplates her visions.",
                        "tags": ["structure_type_palace_or_manor_austere", "settlement_features_jarls_longhouse", "government_local_jarl_idgrod_ravencrone", "magical_properties_arcane_focus_minor_potential_seer_jarl", "political_family_seer_jarl_idgrod", "quest_giver_potential_jarl_visions"]
                    },
                    {
                        "id": 4002,
                        "name": "Moorside Inn",
                        "desc": "A humble inn providing shelter for travelers daring to brave the murky swamps, run by Jonna.",
                        "tags": ["structure_type_inn_building_humble", "settlement_features_tavern", "social_hub_local", "rumor_source_local_fears_vampires", "food_drink_vendor", "lodging_available", "structure_condition_weathered"]
                    },
                    {
                        "id": 4003,
                        "name": "Thaumaturgist's Hut (Falion's House)",
                        "desc": "The home of Falion, Morthal's resident wizard and expert on all things arcane, including vampirism. He is viewed with suspicion by some.",
                        "tags": ["structure_type_shack_or_hut_wizard", "structure_type_residence_wizard", "settlement_features_alchemy_shop_notable_wizard_hut", "item_type_potion_vendor", "item_type_ingredient_vendor", "magical_properties_arcane_focus_vampire_lore", "quest_giver_vampire_cure_falion", "scholar_retreat_rumor_arcane_expert", "urban_issues_or_atmosphere_fear_and_superstition_falion_suspicion"]
                    },
                    {
                        "id": 4004,
                        "name": "Jorgen and Lami's House",
                        "desc": "The home of Jorgen and Lami, who work at the local lumber mill. Lami is an aspiring alchemist.",
                        "tags": ["structure_type_residence", "commoner_dwelling_logger_alchemist_apprentice", "economic_activity_logging_timber_worker_family", "alchemy_apprentice_potential_lami", "family_dwelling"]
                    },
                    {
                        "id": 4005,
                        "name": "Burned House",
                        "desc": "The charred ruins of Hroggar's house, site of a recent tragedy that has the town on edge and fuels rumors of dark magic.",
                        "tags": ["structure_type_ruined_shack_burned", "structure_condition_collapsed_charred", "tragedy_site_family_fire_death", "quest_location_vampire_investigation_laid_to_rest_clue", "urban_issues_or_atmosphere_haunted_rumors_strong_dark_magic", "mystery_local_fire_origin"]
                    }
                ]
            },
            {
                "id": 41,
                "name": "Movarth's Lair",
                "desc": "A dank cave north of Morthal, rumored to be the den of the master vampire Movarth Piquine and his thralls. Its discovery is key to resolving Morthal's troubles.",
                "tags": ["structure_type_natural_cave_dank", "specific_landmark_type_vampire_ancient_lair_movarth", "dungeon_major", "quest_location_vampire_investigation_laid_to_rest_lair", "undead_presence_strong_vampires_thralls", "magical_properties_tainted_by_dark_magic", "boss_fight_vampire_lord_potential_movarth", "state_or_condition_current_lawless_area_vampire"]
            },
            {
                "id": 42,
                "name": "Ustengrav",
                "desc": "A sprawling ancient Nordic tomb deep within Hjaalmarch's marshes, said to hold the Horn of Jurgen Windcaller, a significant relic sought by the Greybeards.",
                "tags": ["nordic_burial_site_major_sprawling", "dungeon_large_complex", "undead_presence_strong", "draugr_heavy", "quest_location_main_story_early_horn_of_jurgen_windcaller", "specific_landmark_type_word_wall_location", "artifact_location_unique_item_horn_of_jurgen_windcaller", "puzzle_ancient_nordic_traps", "terrain_marsh_edge_hjaalmarch", "cultural_historical_significance_nordic_ancient_site_relic"]
            },
            {
                "id": 43,
                "name": "Stonehills",
                "desc": "A modest mining outpost in Hjaalmarch, focused on excavating iron ore, managed by Pactur.",
                "tags": ["populated_village_outpost_mining", "settlement_minor", "economic_activity_mining_iron", "resource_node_iron", "terrain_hilly_marsh_edge", "climate_swampy_edge", "quest_giver_potential_mine_issues"],
                "sub_locations": [
                    {
                        "id": 4301,
                        "name": "Rockwallow Mine",
                        "desc": "The iron mine that sustains the small settlement of Stonehills.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "resource_node_iron", "economic_backbone_stonehills"]
                    },
                    {
                        "id": 4302,
                        "name": "Sorli's House",
                        "desc": "The residence of Sorli the Builder, an important figure in Stonehills who hopes to see the mine prosper.",
                        "tags": ["structure_type_residence", "commoner_dwelling_mine_owner_family", "community_leader_potential_pactur_sorli"]
                    }
                ]
            },
            {
                "id": 44,
                "name": "Apprentice Stone",
                "desc": "A Standing Stone located in the marshes northwest of Morthal, granting faster Magicka regeneration but also increased susceptibility to magic.",
                "id": 44,
                "name": "Apprentice Stone",
                "desc": "A Standing Stone located in the marshes northwest of Morthal, granting faster Magicka regeneration but also increased susceptibility to magic.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_double_edged", "terrain_marsh_island", "cultural_historical_significance_ancient_magical_site", "buff_magicka_regen_increased", "debuff_magic_weakness_increased", "power_magicka_focused_risky"]
            },
            {
                "id": 45,
                "name": "Brood Cavern",
                "desc": "A small cave in Hjaalmarch, often infested with spiders, chaurus, or other venomous creatures.",
                "tags": ["structure_type_natural_cave", "monster_den_spider_major_potential", "monster_den_chaurus_potential", "dungeon_minor", "terrain_marsh", "alchemy_ingredient_source_rich_potential_venom_eggs", "exploration_point_dangerous_creatures"]
            },
            {
                "id": 46,
                "name": "Chillwind Depths",
                "desc": "A large cave system south of Dragon Bridge (near Hjaalmarch border), inhabited by Falmer, Chaurus, and other subterranean horrors.",
                "tags": ["structure_type_natural_cave_large", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_major", "environment_underground_deep", "terrain_mountain_cave_remote_hjaalmarch_haafingar_border", "state_or_condition_current_lawless_area_falmer_territory", "exploration_challenge_extreme_danger"]
            },
            {
                "id": 47,
                "name": "Dead Men's Respite",
                "desc": "A Nordic ruin southwest of Morthal, connected to the Bards College and the legend of King Olaf One-Eye. It is guarded by draugr and holds ancient secrets.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "faction_bards_college_related_quest_king_olaf", "specific_landmark_type_word_wall_location", "cultural_historical_significance_legendary_hero_location_king_olaf", "puzzle_ancient_nordic_ghostly_bard", "artifact_location_king_olafs_verse_potential"]
            },
            {
                "id": 48,
                "name": "Folgunthur",
                "desc": "An ancient Nordic ruin south of Solitude, near the Hjaalmarch border, where a fragment of the legendary Gauldur Amulet is sought, guarded by Mikrul Gauldurson.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy_gauldurson", "quest_location_artifact_gauldur_amulet_fragment", "cultural_historical_significance_ancient_magical_site_gauldur_legend", "puzzle_dragon_claw_ivory", "artifact_location_powerful_gauldur_fragment", "boss_fight_draugr_lord_mikrul_gauldurson"]
            },
            {
                "id": 49,
                "name": "Kjenstag Ruins",
                "desc": "Ruined Nordic structures in the marshes, sometimes haunted by restless spirits or occupied by desperate bandits seeking shelter.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_minor_potential", "terrain_marsh_isolated", "magical_properties_haunted_aura_potential_restless_spirits", "bandit_minor_camp_potential_shelter", "structure_condition_ruined_extensively", "exploration_point_minor_ruin"]
            },
            {
                "id": 40001,
                "name": "Meeko's Shack",
                "desc": "A small, abandoned shack south of Solitude Sawmill, near the Hjaalmarch border. A loyal dog named Meeko waits here for his deceased master.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_abandoned", "animal_companion_unique_meeko_dog", "tragedy_site_minor_deceased_master", "terrain_forested_area_edge_haafingar_hjaalmarch_border", "quest_giver_potential_adopt_dog"]
            },
            {
                "id": 40002,
                "name": "Robber's Gorge",
                "desc": "A bandit-controlled ravine and bridge southwest of Rorikstead, on the edge of Hjaalmarch, a notorious spot for ambushes.",
                "tags": ["bandit_main_stronghold_ravine", "terrain_canyon_river_gorge", "structure_type_bridge_structure_wooden", "dungeon_major", "state_or_condition_current_bandit_controlled_area", "toll_road_illegal_ambush_spot", "quest_location_bounty_leader_potential"]
            },
            {
                "id": 40003,
                "name": "Wreck of the Icerunner",
                "desc": "A shipwreck on the northern coast of Hjaalmarch, west of Solitude. It is now a den for bandits or pirates who prey on coastal traffic.",
                "tags": ["structure_type_shipwreck_site_coastal", "specific_landmark_type_pirate_cove_hidden_potential", "environment_coastal_northern_hjaalmarch", "dungeon_minor", "treasure_cache_rumored_lost_cargo", "bandit_minor_camp_potential_pirates", "exploration_point_historic_wreck"]
            },
            # New Hjaalmarch Locations
            {
                "id": 40004,
                "name": "The Stumbling Sabrecat",
                "desc": "A rickety, half-sunken shack in the deepest part of the Drajkmyr Marsh, rumored to be the home of a reclusive (and possibly mad) alchemist or a coven of witches.",
                "tags": ["structure_type_shack_or_hut_rickety_sunken", "structure_condition_ruined_extensively_half_sunken", "terrain_marsh_deep_drajkmyr", "hermit_lair_potential_mad_alchemist_witch", "magical_properties_tainted_by_dark_magic_potential", "alchemy_ingredient_source_rich_potential_rare_swamp_flora", "witch_coven_potential_rumor", "mystery_local_reclusive_occupant"]
            },
            {
                "id": 40005,
                "name": "Folkvar's Folly",
                "desc": "A small, abandoned watchtower slowly sinking into the marsh. Local legend says it was built by a foolish Thane who ignored warnings about the unstable ground.",
                "tags": ["structure_type_ruined_tower_sinking", "structure_condition_collapsed_sinking_marsh", "terrain_marsh", "cultural_historical_significance_local_legend_foolish_thane", "bandit_minor_camp_potential", "state_or_condition_current_isolated_and_forgotten", "exploration_point_minor_ruin_legend"]
            },
            {
                "id": 40006,
                "name": "Drajkmyr Crossing",
                "desc": "A tiny, precarious stilt-village built over the murky waters on the edge of the Drajkmyr marsh, known for its unique eel fishing techniques.",
                "tags": ["populated_village_stilt", "settlement_minor_precarious", "economic_activity_fishing_industry_local_eel_specialty", "terrain_marsh_drajkmyr_edge", "structure_type_settlement_minor_stilt_village", "unique_culture_local_eel_fishing", "state_or_condition_current_isolated_and_forgotten", "climate_swampy_misty"]
            },
            {
                "id": 40007,
                "name": "Peatbogger's Hut",
                "desc": "The isolated hut of a solitary peat farmer, who harvests the rich soil of Hjaalmarch for fuel and fertilizer.",
                "tags": ["structure_type_shack_or_hut_peat_farmer", "economic_activity_farming_crops_peat_harvesting", "terrain_marsh_isolated", "hermit_lair_potential_solitary_farmer", "state_or_condition_current_isolated_and_forgotten", "resource_node_peat_fuel_fertilizer"]
            },
            {
                "id": 40008,
                "name": "Murkwater Hollow",
                "desc": "A muddy, flooded cave system deep within Hjaalmarch's swamps, likely home to chaurus, mudcrabs, or even a reclusive giant snake if such existed.",
                "tags": ["structure_type_natural_cave_flooded", "terrain_marsh_swamp_deep", "dungeon_minor", "monster_den_chaurus", "monster_den_mudcrab", "structure_condition_flooded_muddy", "alchemy_ingredient_source_rich_potential_chaurus_eggs_mudcrab_chitin"]
            },
            {
                "id": 40009,
                "name": "Sinking Stones of the Marsh",
                "desc": "A small, barely visible ruin of ancient stones half-sunk in the swamp, perhaps part of an old Nordic watchtower or shrine, now reclaimed by the marsh.",
                "tags": ["structure_type_ruined_shrine_nordic_watchtower_potential", "nordic_burial_site_minor_potential", "terrain_marsh_sinking_stones", "structure_condition_collapsed_half_sunk", "treasure_cache_rumored_meager", "cultural_historical_significance_nordic_ancient_site_reclaimed_by_marsh", "exploration_point_minor_ruin"]
            },
            {
                "id": 40010,
                "name": "Misty Grove Farm",
                "desc": "A small, struggling farm on the edge of the Drajkmyr Marsh, where the farmer battles constant dampness and swamp pests to grow hardy root vegetables.",
                "tags": ["structure_type_farmstead_struggling", "economic_activity_farming_crops_root_vegetables", "terrain_marsh_edge_drajkmyr", "state_or_condition_current_isolated_and_forgotten_struggling", "structure_condition_weathered_damp", "climate_swampy_pests"]
            },
            {
                "id": 40011,
                "name": "Fort Snowhawk (Ruined)",
                "desc": "The dilapidated ruins of an old Imperial fort, now largely swallowed by the marsh. Rumored to be haunted by its former garrison or used as a hideout by bog bandits.",
                "tags": ["structure_type_ruined_fort_imperial_historic", "terrain_marsh_swallowed", "dungeon_minor", "magical_properties_haunted_aura_potential_former_garrison", "bandit_minor_camp_potential_bog_bandits", "cultural_historical_significance_historic_site_imperial_fort", "structure_condition_ruined_extensively_dilapidated"]
            },
            {
                "id": 40012,
                "name": "Shrine of Herma-Mora (Hidden Marsh Shrine)",
                "desc": "A small, hidden shrine of crudely piled stones and waterlogged tomes dedicated to Hermaeus Mora, tucked away in a particularly dense and foggy part of Hjaalmarch. Only those seeking forbidden knowledge would find it.",
                "tags": ["structure_type_shrine_outdoor_structure_crude", "magical_properties_daedric_influence_overt_hermaeus_mora", "terrain_marsh_dense_foggy", "secret_location_hidden_shrine", "forbidden_knowledge_dangerous_waterlogged_tomes", "cult_activity_potential_minor_hermaeus_mora", "hermaeus_mora_shrine", "exploration_point_lore_daedric"]
            },
            {
                "id": 40013,
                "name": "Bogbound Barrow",
                "desc": "A small, partially flooded Nordic barrow slowly being reclaimed by the swamp. It's likely home to draugr who guard meager treasures.",
                "tags": ["nordic_burial_site_minor_barrow", "structure_condition_flooded_partially", "dungeon_minor", "undead_presence_strong", "draugr_heavy_meager_treasure_guardians", "terrain_marsh_reclaimed", "exploration_point_minor_tomb"]
            },
            {
                "id": 40014,
                "name": "Lost Echo Cave",
                "desc": "A large cave system in Hjaalmarch, west of Morthal, known for its unusual acoustics. It is now a den for Falmer and their chaurus, and contains an ancient Word Wall.",
                "tags": ["structure_type_natural_cave_large", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_major", "specific_landmark_type_word_wall_location", "unique_natural_formation_unusual_acoustics", "state_or_condition_current_lawless_area_falmer_territory", "terrain_hjaalmarch_west_morthal"]
            },
            {
                "id": 40015,
                "name": "Ragnvald",
                "desc": "An ancient Nordic ruin in the mountains of Hjaalmarch, north of Markarth. It is a burial site guarded by powerful draugr and the Dragon Priest Otar the Mad.",
                "tags": ["nordic_burial_site_major_dragon_priest_tomb", "dungeon_large_complex", "cultural_historical_significance_dragon_cult_lair_priest_otar_the_mad", "undead_presence_strong_powerful", "draugr_heavy", "specific_landmark_type_word_wall_location", "magical_properties_arcane_nexus_powerful", "dragon_priest_otar", "artifact_location_powerful_mask_otar", "terrain_mountainous_hjaalmarch_north_markarth"]
            },
            {
                "id": 40016,
                "name": "Orotheim",
                "desc": "A small cave system in the western part of Hjaalmarch, often used as a hideout by a desperate group of bandits preying on the sparse traffic through the marshes.",
                "tags": ["structure_type_natural_cave_small", "bandit_minor_camp_desperate", "dungeon_minor", "terrain_marsh_edge_western_hjaalmarch", "state_or_condition_current_bandit_controlled_area", "quest_location_bounty_potential_minor"]
            },
            {
                "id": 40017,
                "name": "Mzinchaleft",
                "desc": "A large Dwemer ruin in Hjaalmarch, south of Dawnstar (near The Pale border). It is a dangerous complex filled with Dwemer constructs, Falmer, and a Great Lift providing access to Blackreach.",
                "tags": ["dwemer_ruin_major_city_complex", "dungeon_large_complex_dangerous", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "specific_landmark_type_blackreach_elevator_access", "cultural_historical_significance_dwemer_ruin_site_major", "ancient_technology_dwemer", "chaurus_nest_major_potential", "terrain_hjaalmarch_pale_border_south_dawnstar", "quest_location_daedric_hermaeus_mora_ogradh_potential"]
            }
        ]
    },

    # FALKREATH HOLD
    {
        "id": 5,
        "name": "Falkreath Hold",
        "desc": "A heavily forested hold in southern Skyrim, known for its ancient woods, towering mountains, and the somber town of Falkreath with its large graveyard. It borders Cyrodiil and is an important Imperial territory.",
        "tags": ["hold", "terrain_forest_dense_ancient", "climate_temperate_continental", "cultural_historical_significance_graveyard_town_falkreath", "terrain_mountainous_southern_skyrim", "cyrodiil_border_region", "nordic_culture_local_somber", "imperial_influence_strong", "economic_activity_logging_timber_major", "state_or_condition_current_politically_stable", "dark_brotherhood_presence_rumored_sanctuary"],
        "demographics": {"Nord": 85, "Imperial": 10, "Others": 5},
        "travel": {
            "roads": ["Whiterun Hold", "The Reach", "Cyrodiil (Fort Neugrad Pass)"],
            "paths": ["Helgen Pass (functional)", "Pine Forest Trail", "Jerall Mountains Path"]
        },
        "sub_locations": [
            {
                "id": 50,
                "name": "Falkreath (Town)",
                "desc": "A quiet, somewhat gloomy town nestled in the southern forests, known for its extensive graveyard and timber industry. It is the seat of Jarl Siddgeir, an Imperial appointee.",
                "tags": ["populated_town", "terrain_forest_southern", "city_affiliation_falkreath_town", "cultural_historical_significance_graveyard_town_largest_in_skyrim", "settlement_features_jarls_longhouse_siddgeir", "daedric_influence_subtle_rumor_clues", "economic_activity_logging_timber", "urban_issues_or_atmosphere_oppressive_atmosphere_gloomy", "imperial_influence_strong", "nordic_architecture_local_wood"],
                "sub_locations": [
                    {
                        "id": 5001,
                        "name": "Dead Man's Drink",
                        "desc": "The local tavern in Falkreath, a place for locals and weary travelers to find mead and solace, run by Valga Vinicia.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "rumor_source_local_legends_daedric_rumors", "food_drink_vendor", "lodging_available"]
                    },
                    {
                        "id": 5002,
                        "name": "Jarl's Longhouse (Falkreath)",
                        "desc": "The seat of authority in Falkreath Hold, residence of Jarl Siddgeir.",
                        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local_jarl_siddgeir", "imperial_influence_strong_appointed_jarl", "quest_giver_potential_jarl_tasks"]
                    },
                    {
                        "id": 5003,
                        "name": "Falkreath Graveyard",
                        "desc": "An expansive and ancient cemetery, the largest in Skyrim, where many Nords, both heroes and common folk, are laid to rest. Restless spirits are sometimes rumored here.",
                        "tags": ["cultural_historical_significance_historic_burial_site_major_largest_skyrim", "religious_site_aedric_arkay", "arkay_presence_strong_priest_runil", "undead_presence_rumored_low_restless_spirits", "unique_landmark_iconic_town_feature", "urban_issues_or_atmosphere_haunted_rumors_strong_graveyard", "quest_location_ancestor_worhsip_runil_journal"]
                    },
                    {
                        "id": 5004,
                        "name": "Gray Pine Goods",
                        "desc": "Solaf's shop in Falkreath, offering general supplies, hunting gear, and lumber from the local mill.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety_local_goods", "item_type_hunting_gear_vendor", "item_type_lumber_vendor", "stormcloak_sympathizers_potential_owner_solaf"]
                    },
                    {
                        "id": 5005,
                        "name": "Lod's House and Smithy",
                        "desc": "The home and workshop of Lod, Falkreath's blacksmith, who can often be found working his forge, sometimes seeking a particular dog.",
                        "tags": ["structure_type_shop_building", "structure_type_residence", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "quest_giver_daedric_clues_barbas_dog", "item_type_weapon_vendor", "item_type_armor_vendor"]
                    },
                    {
                        "id": 5006,
                        "name": "Hall of the Dead (Falkreath)",
                        "desc": "Falkreath's hall for honoring the dead, managed by Runil, a priest of Arkay, who also tends the graveyard.",
                        "tags": ["structure_type_temple_building_hall_of_the_dead", "religious_site_aedric_arkay", "arkay_shrine_priest_runil", "settlement_features_catacombs_burial_access_potential", "quest_giver_potential_runil_ancestor_worhsip"]
                    },
                    {
                        "id": 5007,
                        "name": "Dark Brotherhood Sanctuary (Falkreath Entrance)",
                        "desc": "A hidden sanctuary of the Dark Brotherhood, concealed within the pine forests near Falkreath. Its door is marked by a sinister black hand.",
                        "tags": ["specific_landmark_type_assassin_guild_hq_active_dark_brotherhood", "secret_location_hidden_entrance_black_door", "dungeon_major_entrance_sanctuary", "terrain_forest_pine", "magical_properties_tainted_by_dark_magic_potential", "faction_dark_brotherhood_main_base"]
                    }
                ]
            },
            {
                "id": 51,
                "name": "Pinewatch",
                "desc": "A secluded farmhouse north of Falkreath. While appearing innocent, it serves as a well-concealed front for a secret bandit hideout and smuggling operation.",
                "tags": ["structure_type_farmstead_front_operation", "bandit_main_stronghold_hidden_cave", "dungeon_major_complex", "quest_location_thieves_guild_riggs_note", "economic_activity_smuggling_route_active", "secret_location_hidden_basement_entrance", "terrain_forest_secluded", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 52,
                "name": "Halldir's Cairn",
                "desc": "A solemn Nordic barrow southwest of Falkreath, haunted by the powerful draugr sorcerer Halldir and his elemental thralls.",
                "tags": ["nordic_burial_site_major_cairn", "dungeon_major", "undead_presence_strong_draugr_sorcerer_halldir", "magical_properties_arcane_nexus_elemental_magic", "monster_den_elemental_thralls_fire_frost_shock", "draugr_heavy", "boss_fight_mage_powerful_halldir", "terrain_forest_southwest_falkreath"]
            },
            {
                "id": 53,
                "name": "Helgen",
                "desc": "A modest but strategically important Imperial fortified town at the southern border of Whiterun Hold, known for its lumber trade and guarding the pass to Cyrodiil. It is currently a functional settlement.",
                "tags": ["populated_village_fortified", "imperial_influence_strong_outpost", "economic_activity_logging_timber", "cyrodiil_border_region_pass_guard", "quest_location_main_story_opening_sequence_potential_alt_start", "state_or_condition_current_functional_settlement_pre_dragon_attack", "terrain_whiterun_falkreath_border"],
                 "sub_locations": [
                    {
                        "id": 5301,
                        "name": "Helgen Keep",
                        "desc": "The main keep of Helgen, garrisoned by Imperial soldiers. It serves as the town's primary defense and administrative center.",
                        "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion_garrison", "imperial_influence_strong", "government_local_imperial_command", "structure_condition_pristine_functional"]
                    },
                    {
                        "id": 5302,
                        "name": "Helgen Homestead",
                        "desc": "One of the sturdy wooden homes within the town of Helgen.",
                        "tags": ["structure_type_residence", "commoner_dwelling_wooden_sturdy", "settlement_minor_housing"]
                    },
                    {
                        "id": 5303,
                        "name": "The Dragon's Rest Inn (Helgen)",
                        "desc": "A small, welcoming inn in Helgen, catering to local loggers and Imperial soldiers passing through.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local_loggers_soldiers", "food_drink_vendor", "lodging_available", "rumor_source_local_border_news"]
                    }
                ]
            },
            {
                "id": 54,
                "name": "Ancestor Glade",
                "desc": "A hidden, serene glade sacred to the Moth Priests, located in the southern mountains of Falkreath Hold. It's a place of profound natural beauty and ancient ritual, though its significance is known to few.",
                "tags": ["cultural_historical_significance_sacred_grove_moth_priests_kynareth", "unique_natural_formation_ancestor_moths_canticle_trees", "magical_properties_aedric_blessing_active_ancient_ritual_site", "secluded_nature_spot_profound_beauty", "quest_location_dawnguard_potential_alt_moth_priest_ritual", "alchemy_ingredient_source_rich_unique_ancestor_moth_wings_bark", "terrain_southern_falkreath_mountains_hidden"]
            },
            {
                "id": 55,
                "name": "Bloodlet Throne",
                "desc": "A ruined fort atop a mountain in Falkreath, now a lair for a powerful coven of vampires who prey on unwary travelers.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_vampire_ancient_lair_coven", "dungeon_major", "terrain_mountain_peak_falkreath", "state_or_condition_current_lawless_area_vampire_controlled", "undead_presence_strong_vampires_thralls", "magical_properties_tainted_by_dark_magic", "boss_fight_vampire_lord_potential"]
            },
            {
                "id": 56,
                "name": "Brittleshin Pass",
                "desc": "A small cave system serving as a pass through the mountains south of Falkreath, often inhabited by necromancers, undead, or desperate bandits.",
                "tags": ["structure_type_natural_cave_pass", "terrain_mountain_pass_south_falkreath", "specific_landmark_type_necromancer_lair_potential", "undead_presence_skeletons_potential", "bandit_minor_camp_potential", "dungeon_minor", "travel_route_alternative_dangerous", "exploration_point_shortcut_cave"]
            },
            {
                "id": 57,
                "name": "Embershard Mine",
                "desc": "An iron mine located between Riverwood and Helgen, currently occupied by a band of opportunistic bandits.",
                "tags": ["structure_type_mine_active_iron", "economic_activity_mining_iron", "bandit_minor_camp_opportunistic", "dungeon_minor", "state_or_condition_current_bandit_controlled_area", "resource_node_iron", "quest_location_clear_mine_early_game_potential", "riverwood_helgen_road_nearby"]
            },
            {
                "id": 58,
                "name": "Evergreen Grove",
                "desc": "A small, secluded grove west of Falkreath, known for its spriggans and natural tranquility. Alchemists sometimes seek rare herbs here.",
                "tags": ["environment_wilderness_grove_secluded", "terrain_forest_west_falkreath", "specific_landmark_type_spriggan_sanctuary", "alchemy_ingredient_source_rich_rare_herbs", "secluded_nature_spot_tranquil", "magical_properties_enchanted_neutral_nature_spirits", "monster_den_spriggan_strong"]
            },
            {
                "id": 59,
                "name": "Knifepoint Ridge",
                "desc": "A bandit-occupied mine and camp in the northwestern part of Falkreath Hold, from which raids are launched. Rumored to be connected to a Daedric artifact.",
                "tags": ["structure_type_mine_active_camp_integrated", "economic_activity_mining_corundum_potential", "bandit_main_stronghold_raiding_base", "dungeon_major", "quest_location_daedric_boethiah_champion", "state_or_condition_current_bandit_controlled_area", "terrain_northwestern_falkreath_hold", "artifact_location_daedric_related_potential"]
            },
            {
                "id": 50001,
                "name": "Moss Mother Cavern",
                "desc": "A cave system east of Falkreath, home to various creatures like spriggans and bears, and connected to local legends of nature spirits.",
                "tags": ["structure_type_natural_cave", "monster_den_spriggan", "monster_den_bear", "quest_location_local_legend_valdr_hunt", "dungeon_minor", "unique_natural_formation_mossy_cave", "alchemy_ingredient_source_rich_moss_animal_parts"]
            },
            {
                "id": 50002,
                "name": "Peak's Shade Tower",
                "desc": "A ruined tower south of Falkreath, often a lair for hagravens or other malevolent creatures who perform dark rituals under the forest canopy.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main_potential", "magical_properties_tainted_by_dark_magic", "dungeon_minor", "terrain_forest_south_falkreath", "ritual_site_dark_magic_hagraven", "monster_den_hagraven"]
            },
            {
                "id": 50003,
                "name": "Roadside Ruins",
                "desc": "Crumbling Nordic ruins along the road in Falkreath Hold, sometimes attracting spriggans guarding their territory or bandits lying in ambush.",
                "tags": ["structure_type_ruined_shrine_nordic", "nordic_burial_site_minor_potential", "roadside_encounter_point", "monster_den_spriggan_potential", "bandit_minor_camp_potential_ambush", "structure_condition_ruined_extensively", "exploration_point_minor_ruin"]
            },
            {
                "id": 50004,
                "name": "Sunderstone Gorge",
                "desc": "A large cave system in the southern mountains of Falkreath, housing an ancient Word Wall and various magical inhabitants, including fire-wielding mages or atronachs.",
                "tags": ["structure_type_natural_cave_gorge", "dungeon_major", "specific_landmark_type_word_wall_location", "magical_properties_elemental_fire_dominant", "monster_den_fire_atronach", "mage_lair_hostile_fire_mages", "terrain_southern_falkreath_mountains", "exploration_challenge_elemental_hazard"]
            },
            {
                "id": 50005,
                "name": "Cracked Tusk Keep",
                "desc": "A ruined fort in Falkreath Hold, now occupied by a fierce band of Orc bandits. Rumor has it they guard a fragment of a powerful Daedric artifact.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold_orc", "orc_presence_hostile_bandits", "dungeon_major", "quest_location_daedric_mehrunes_razor_pieces", "artifact_location_daedric_razor_pieces", "state_or_condition_current_bandit_controlled_area_orc"]
            },
            # New Falkreath Hold Locations
            {
                "id": 50006,
                "name": "Angi's Camp",
                "desc": "A secluded cabin in the southern mountains of Falkreath, home to Angi, a skilled archer offering training to those who find her.",
                "tags": ["structure_type_shack_or_hut_cabin", "hermit_lair_archer_angi", "skill_trainer_archery_expert", "terrain_mountainous_southern_falkreath", "state_or_condition_current_isolated_and_forgotten", "hunter_gathering_spot_secluded", "quest_giver_potential_archery_training"]
            },
            {
                "id": 50007,
                "name": "Fort Neugrad",
                "desc": "A large Imperial fort near the Cyrodiilic border, guarding a key mountain pass. Currently well-garrisoned and a symbol of Imperial authority in the region.",
                "tags": ["structure_type_fortified_keep_imperial", "military_presence_imperial_legion_garrison", "imperial_influence_strong_border_fort", "cyrodiil_border_region_pass_guard", "dungeon_major", "state_or_condition_current_contested_by_factions_potential_stormcloak", "civil_war_quest_historic_site_potential", "strategic_location_border_pass"]
            },
            {
                "id": 50008,
                "name": "Lake Ilinalta",
                "desc": "A large, deep lake in western Falkreath Hold, shrouded in mist and legend. Its depths are said to hold ancient secrets and perhaps even a sunken ruin.",
                "tags": ["terrain_lake_large_deep_misty", "climate_temperate", "cultural_historical_significance_local_legend_sunken_ruin", "structure_type_ruined_fort_submerged_potential_ilinaltas_deep", "economic_activity_fishing_industry_local", "unique_natural_formation_lake", "quest_location_daedric_azura_star_related_interior_ruin"],
                "sub_locations": [
                    {
                        "id": 500081,
                        "name": "Ilinalta's Deep",
                        "desc": "The treacherous, flooded ruins of an ancient fort or temple within Lake Ilinalta, rumored to be haunted and guarded by necromancers or dark creatures.",
                        "tags": ["structure_type_ruined_fort_submerged_temple_potential", "specific_landmark_type_necromancer_lair", "undead_presence_strong_skeletons_necromancers", "dungeon_major", "quest_location_daedric_azura_star_broken", "magical_properties_tainted_by_dark_magic", "structure_condition_flooded_treacherous", "boss_fight_necromancer_powerful_potential"]
                    }
                ]
            },
            {
                "id": 50009,
                "name": "The Lady Stone",
                "desc": "A Standing Stone located on an island in Lake Ilinalta, granting enhanced health and stamina regeneration.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive_regenerative", "terrain_island_lake_ilinalta", "cultural_historical_significance_ancient_magical_site", "buff_health_regen_increased", "buff_stamina_regen_increased", "power_regenerative_passive"]
            },
            {
                "id": 50010,
                "name": "Hunter's Rest Clearing",
                "desc": "A small, secluded clearing deep in the forests of Falkreath, often used by hunters as a temporary camp. Signs of recent use are common.",
                "tags": ["hunter_gathering_spot_camp", "environment_wilderness", "terrain_forest_deep_falkreath", "secluded_nature_spot", "bandit_minor_camp_potential_temporary", "exploration_point_minor"]
            },
            {
                "id": 50011,
                "name": "Wolfstooth Den",
                "desc": "A shallow cave system within Falkreath's dense woods, currently serving as a den for a pack of territorial wolves.",
                "tags": ["structure_type_natural_cave_shallow", "monster_den_wolf_pack_major", "terrain_forest_dense_falkreath", "dungeon_minor", "animal_den_wolf_territorial", "alchemy_ingredient_source_rich_wolf_pelts"]
            },
            {
                "id": 50012,
                "name": "Half-Moon Mill",
                "desc": "A lumber mill owned by Hert and Hern, a reclusive couple. Rumors persist about their nocturnal activities and connections to darker elements.",
                "tags": ["structure_type_lumber_mill_site", "settlement_minor", "economic_activity_logging_timber", "specific_landmark_type_vampire_coven_minor_potential_owners_hert_hern", "isolated_location_lake_ilinalta_shore", "mystery_local_nocturnal_activities", "quest_location_dark_brotherhood_target_potential"]
            },
            {
                "id": 50013,
                "name": "Granitehall Farm",
                "desc": "A small, hardy farm nestled near the mountains of Falkreath, known for its resilient goats and strong mead.",
                "tags": ["structure_type_farmstead_hardy", "economic_activity_farming_livestock_goats", "economic_activity_brewing_mead_ale_strong", "terrain_mountainous_falkreath", "isolated_location", "settlement_minor", "unique_produce_goat_cheese_mead"]
            },
            {
                "id": 50014,
                "name": "Shadowed Path Cave",
                "desc": "A dark, winding cave often used by smugglers as a discreet route through Falkreath's forests, or as a den for bears and other forest predators.",
                "tags": ["structure_type_natural_cave_winding", "terrain_forest_falkreath", "dungeon_minor", "economic_activity_smuggling_route_active_potential", "monster_den_bear_potential", "monster_den_wolf_potential", "exploration_point_hidden_path"]
            },
            {
                "id": 50015,
                "name": "Crumbling Border Watch",
                "desc": "The ruins of a small Imperial watchtower near the Cyrodiil border in Falkreath Hold, now overgrown and sometimes used by bandits as a lookout.",
                "tags": ["structure_type_ruined_tower_imperial_watchtower", "military_presence_historic_imperial", "terrain_mountainous_cyrodiil_border", "structure_condition_ruined_extensively_overgrown", "bandit_minor_camp_potential_lookout", "cyrodiil_border_region", "exploration_point_historic_ruin"]
            },
            {
                "id": 50018,
                "name": "South Skybound Watch",
                "desc": "A ruined Nordic watchtower and barrow complex, similar to its northern counterpart, located in the southern mountains of Falkreath Hold. It contains an ancient Word Wall and is guarded by draugr.",
                "tags": ["structure_type_ruined_tower_nordic", "nordic_burial_site_major_complex", "specific_landmark_type_word_wall_location", "dungeon_major", "undead_presence_strong", "draugr_heavy", "terrain_mountainous_southern_falkreath", "cultural_historical_significance_nordic_ancient_site"]
            },
            {
                "id": 50019,
                "name": "Shor's Watchtower",
                "desc": "A ruined watchtower near the border of Falkreath and The Rift, overlooking the road to Shor's Stone. Often occupied by bandits.",
                "tags": ["structure_type_ruined_tower_watchtower", "bandit_minor_camp_potential", "roadside_ruin_falkreath_rift_border", "strategic_lookout_decayed_shors_stone_road", "dungeon_minor"]
            },
            {
                "id": 50020,
                "name": "Bleakwind Basin",
                "desc": "A large, open basin in Falkreath Hold, west of Whiterun, known as a traditional gathering place for giants and their mammoth herds.",
                "tags": ["specific_landmark_type_giant_camp_established_major", "mammoth_herd_grazing", "terrain_plains_open_basin_falkreath_whiterun_border", "neutral_encounter_giant_mammoth_large_group", "cultural_historical_significance_giant_gathering_place"]
            },
            {
                "id": 50021,
                "name": "Shor's Watchtower",
                "desc": "A ruined watchtower near the border of Falkreath and The Rift, overlooking the road to Shor's Stone. Often occupied by bandits.",
                "tags": ["structure_type_ruined_tower_watchtower", "bandit_minor_camp_potential", "roadside_ruin_falkreath_rift_border", "strategic_lookout_decayed_shors_stone_road", "dungeon_minor"]
            },
            {
                "id": 50022,
                "name": "Bannermist Tower",
                "desc": "A ruined watchtower south of Lake Ilinalta in Falkreath Hold, now occupied by bandits who use it to prey on travelers.",
                "tags": ["structure_type_ruined_tower_watchtower", "bandit_minor_camp", "dungeon_minor", "roadside_danger_spot_lake_ilinalta_south", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 50023,
                "name": "Anise's Cabin",
                "desc": "A small, seemingly innocent cabin located near Riverwood, on the edge of Falkreath Hold. Anise is an elderly woman with a hidden cellar revealing her dabbling in witchcraft.",
                "tags": ["structure_type_shack_or_hut_cabin", "witch_coven_potential_hidden_cellar", "secret_location_witchcraft_lair", "alchemy_ingredient_source_rich_cabin_cellar", "neutral_encounter_secret_hostile_potential_anise", "quest_giver_potential_minor_task_or_threat", "terrain_forested_area_edge_riverwood_falkreath"]
            }
        ]
    },

    # THE REACH
    {
        "id": 6,
        "name": "The Reach",
        "desc": "A wild, rugged, and mountainous region in western Skyrim, dominated by steep cliffs, deep valleys, and ancient Dwemer ruins. It is the heartland of the native Forsworn, who wage a bitter insurgency against Nord rule.", # Emphasized Forsworn conflict
        "tags": ["hold", "terrain_mountainous_extreme", "dwemer_ruin_heavy", "state_or_condition_current_forsworn_controlled_area_extensive", "economic_activity_mining_silver", "cultural_historical_significance_breton_reachmen_culture_strong", "state_or_condition_current_active_warzone_nearby_forsworn_insurgency", "climate_temperate_alpine", "environment_wilderness_rugged", "political_tension_high_forsworn_nord_conflict"],
        "demographics": {"Breton (Reachmen/Forsworn)": 60, "Nord": 30, "Orc": 5, "Others": 5}, # Shifted demographics
        "travel": {
            "roads": ["Whiterun Hold", "Haafingar", "Falkreath Hold", "Hjaalmarch"],
            "paths": ["Karth River Valley", "Sundered Hills Pass", "Hag Rock Trail", "Deep Folk Crossing Path"]
        },
        "sub_locations": [
            {
                "id": 60,
                "name": "Markarth",
                "desc": "A city built into the stone cliffs by the Dwemer, now the capital of the Reach under Nord Jarl Igmund. It is known for its silver mines, brutalist architecture, and the simmering Forsworn conspiracy within its walls.",
                "tags": ["populated_city", "structure_type_dwemer_city_repurposed", "terrain_mountain_city", "city_affiliation_the_reach_capital", "urban_issues_or_atmosphere_rampant_corruption_forsworn_conspiracy", "economic_activity_mining_silver", "settlement_features_jarls_longhouse", "imperial_influence_strong", "political_tension_high_forsworn_nord_conflict", "cultural_historical_significance_dwemer_ruin_major_city_integrated", "unique_landmark_iconic_stone_city", "dwemer_architecture_dominant", "urban_issues_or_atmosphere_oppressive_atmosphere", "state_or_condition_current_heavily_guarded"],
                "sub_locations": [
                    {
                        "id": 6001,
                        "name": "Silver-Blood Inn",
                        "desc": "A bustling tavern in Markarth, owned by the influential and often ruthless Silver-Blood family, a common place for rumors, shady deals, and political maneuvering.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "political_intrigue_high", "silver_blood_family_owned", "rumor_source", "food_drink_vendor", "lodging_available", "economic_activity_trade_local_shady"]
                    },
                    {
                        "id": 6002,
                        "name": "Understone Keep",
                        "desc": "An ancient Dwemer fortification carved into the rock, serving as the Jarl's palace. It also houses a Dwemer museum managed by Calcelmo and provides access to the ruins of Nchuand-Zel.",
                        "tags": ["structure_type_fortified_keep", "structure_type_dwemer_ruin_repurposed", "government_local", "settlement_features_jarls_longhouse", "cultural_historical_significance_dwemer_ruin_site", "settlement_features_museum_dwemer", "dungeon_access_nchuand_zel", "scholar_calcelmo_residence", "dwemer_architecture_dominant"] ,
                        "sub_locations": [
                            {
                                "id": 60028, # Corrected ID from previous thought process, ensuring it's unique within The Reach
                                "name": "Nchuand-Zel",
                                "desc": "The vast and ancient Dwemer city ruins located directly beneath Understone Keep in Markarth. It is a dangerous labyrinth of crumbling halls, active Dwemer machinery, Falmer, and potentially a slumbering Centurion.",
                                "tags": ["dwemer_ruin_major_city", "dungeon_large_complex", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "ancient_technology_dwemer", "cultural_historical_significance_dwemer_ruin_site", "understone_keep_access_only", "labyrinthine_layout", "chaurus_nest_potential", "treasure_cache_dwemer_artifacts_rumored"]
                            }
                        ]
                    },
                    {
                        "id": 6003,
                        "name": "Cidhna Mine",
                        "desc": "Markarth's infamous silver mine, which also serves as a brutal prison primarily for accused Forsworn. Conditions are harsh, and escape is said to be impossible.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_silver", "settlement_features_prison_mine", "forsworn_incarceration", "quest_location_forsworn_uprising", "social_issue_forced_labor", "political_tension_high", "state_or_condition_current_brutal_conditions"]
                    },
                    {
                        "id": 6004,
                        "name": "Arnleif and Sons Trading Company",
                        "desc": "A general goods store in Markarth, run by Lisbet. It struggles due to competition and Forsworn activity.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "economic_activity_trade_hub_local", "quest_giver_potential_lisbet_statue", "business_struggling"]
                    },
                    {
                        "id": 6005,
                        "name": "The Hag's Cure",
                        "desc": "Bothela's apothecary shop in Markarth, providing potions, ingredients, and alchemical supplies. Bothela is a wise old woman with knowledge of Reach traditions.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "reach_culture_knowledge_source", "wise_elder_owner"]
                    },
                    {
                        "id": 6006,
                        "name": "Markarth Market Square",
                        "desc": "An open-air market in the heart of the city where various vendors sell their goods, often under the watchful eye of city guards. Tensions between Nords and Reach natives can sometimes spill over here.",
                        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "guard_patrols_heavy", "cultural_tension_point", "urban_issues_or_atmosphere_tense_atmosphere"]
                    },
                    {
                        "id": 6007,
                        "name": "Temple of Dibella",
                        "desc": "A grand temple dedicated to Dibella, the goddess of beauty and love, home to several priestesses and the site of the Sybil of Dibella.",
                        "tags": ["structure_type_temple_building", "religious_site_aedric", "dibella_shrine", "quest_location_dibella", "sacred_site_female_only_inner_sanctum", "unique_landmark_iconic", "art_beauty_focus"]
                    },
                    {
                        "id": 6008,
                        "name": "Ghorza's Smithy",
                        "desc": "The workshop of Ghorza gra-Bagol, an Orc blacksmith in Markarth, who values good craftsmanship and offers training.",
                        "tags": ["settlement_features_blacksmith_forge_active", "structure_type_shop_building", "economic_activity_smithing_production", "orc_craftsman", "skill_trainer_smithing_potential", "item_type_weapon_vendor", "item_type_armor_vendor"]
                    },
                    { # Added Smelter
                        "id": 6009,
                        "name": "Markarth Smelter",
                        "desc": "The industrial smelter used to process ore from Cidhna Mine and other regional mining operations.",
                        "tags": ["industrial_facility", "settlement_features_smelter_active", "economic_activity_mining_silver_processing", "resource_node_processing"]
                    }
                ]
            },
            {
                "id": 61,
                "name": "Karthwasten",
                "desc": "A rugged mining village in the Reach, centered around Sanuarach Mine and Fenn's Gulch Mine. It is frequently caught in the crossfire between Markarth's Silver-Blood family interests and Forsworn raids.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_mining_silver", "political_tension_high_forsworn_conflict_zone", "economic_activity_mining_silver_contested", "political_influence_silver_blood_family", "state_or_condition_current_frequent_raids_local_forsworn", "terrain_mountain_valley", "climate_temperate_alpine"],
                 "sub_locations": [
                    {
                        "id": 6101,
                        "name": "Karthwasten Hall",
                        "desc": "The primary gathering place in Karthwasten, where locals discuss mining rights and Forsworn threats. Often serves as a makeshift inn.",
                        "tags": ["structure_type_community_building", "social_hub_local", "meeting_hall_village", "inn_makeshift", "rumor_source"]
                    },
                    {
                        "id": 6102,
                        "name": "Sanuarach Mine",
                        "desc": "A silver mine in Karthwasten, a key source of income for the village but often disrupted by ownership disputes and Forsworn attacks.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_silver", "resource_node_silver", "conflict_point_ownership_dispute", "forsworn_target_potential"]
                    },
                    {
                         "id": 6103,
                         "name": "Fenn's Gulch Mine",
                         "desc": "Another mine near Karthwasten, primarily for silver, also vulnerable to local conflicts.",
                         "tags": ["structure_type_mine_active", "economic_activity_mining_silver", "resource_node_silver", "dangerous_area_forsworn_raids", "conflict_point"]
                    }
                ]
            },
            {
                "id": 62,
                "name": "Druadach Redoubt",
                "desc": "A major Forsworn encampment and cave system hidden in the mountains southwest of Karthwasten, a formidable stronghold of the Reach's native rebellion.",
                "tags": ["faction_forsworn_stronghold_major", "structure_type_cave_system_fortified", "dungeon_major", "political_faction_rebel_base", "quest_location_faction_alliance_potential_forsworn", "forsworn_presence_strong", "hagraven_presence_potential", "terrain_mountainous_hidden", "state_or_condition_current_forsworn_controlled_area_major_base"]
            },
            {
                "id": 63,
                "name": "Deep Folk Crossing",
                "desc": "An ancient Dwemer bridge spanning a tumultuous river high in the mountains. A breathtaking and perilous relic, rumored to lead to undiscovered ruins.",
                "tags": ["structure_type_bridge_dwemer_ancient", "ruin_landmark_remote", "scenic_vista_panoramic_dangerous", "exploration_challenge_perilous_crossing", "undiscovered_ruins_rumor_dwemer", "terrain_mountain_pass", "terrain_river_gorge", "cultural_historical_significance_dwemer_engineering_feat", "state_or_condition_current_isolated_and_forgotten"]
            },
            {
                "id": 64,
                "name": "Dushnikh Yal",
                "desc": "An Orc stronghold in the southwestern Reach, adhering to the ancient Code of Malacath. Known for its skilled warriors, miners, and adherence to tradition.",
                "tags": ["orc_stronghold", "populated_settlement_orcish", "tribal_community_orcish", "terrain_mountain_settlement_fortified", "economic_activity_mining_orichalcum", "warrior_culture_orcish", "malacath_worship", "structure_type_fortified_settlement", "cultural_historical_significance_orc_tradition", "faction_orc_tribe_dushnikh_yal", "climate_temperate_alpine"],
                 "sub_locations": [
                    {
                        "id": 6401,
                        "name": "Burguk's Longhouse",
                        "desc": "The longhouse of Chief Burguk, the stern but fair leader of Dushnikh Yal.",
                        "tags": ["structure_type_longhouse_orcish", "government_tribal", "chieftains_hall", "residence_chief"]
                    },
                    {
                        "id": 6402,
                        "name": "Dushnikh Mine (Orichalcum)",
                        "desc": "The stronghold's orichalcum mine, providing valuable ore for Orcish smithing and trade.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_orichalcum", "resource_node_orichalcum", "orc_controlled_mine"]
                    },
                    {
                        "id": 6403,
                        "name": "Gharol's Smithy (Dushnikh Yal)", # Specified location
                        "desc": "The forge of Gharol, the skilled blacksmith of Dushnikh Yal, crafting traditional Orcish arms and armor.",
                        "tags": ["settlement_features_blacksmith_forge_active", "structure_type_shop_building", "economic_activity_smithing_production", "crafting_orcish_traditional", "female_orc_smith", "item_type_weapon_vendor", "item_type_armor_vendor"]
                    }
                ]
            },
            {
                "id": 65,
                "name": "Blind Cliff Cave",
                "desc": "A cave system north of Markarth, a den for Forsworn ritualists and their hagraven allies.",
                "tags": ["structure_type_natural_cave", "forsworn_ritual_site", "specific_landmark_type_hagraven_coven_lair_main", "dungeon_minor", "magical_properties_tainted_by_dark_magic", "forsworn_presence_strong", "hagraven_presence_strong", "state_or_condition_current_forsworn_controlled_area"]
            },
            {
                "id": 66,
                "name": "Bruca's Leap Redoubt",
                "desc": "A Forsworn encampment built around a waterfall and river, east of Karthwasten, utilizing the natural defenses of the terrain.",
                "tags": ["structure_type_fortified_camp_forsworn", "forsworn_presence_strong", "unique_natural_formation_waterfall_location_strategic", "dungeon_minor", "terrain_river_delta_outpost", "natural_defenses_utilized", "state_or_condition_current_forsworn_controlled_area"]
            },
            {
                "id": 67,
                "name": "Dead Crone Rock",
                "desc": "A ruined tower and Forsworn stronghold west of Markarth, a place of dark magic and a site for a Daedric quest related to Mehrunes' Razor.",
                "tags": ["structure_type_ruined_tower", "forsworn_stronghold_major", "specific_landmark_type_hagraven_coven_lair_main", "quest_location_daedric_mehrunes_razor_pieces", "dungeon_major", "forsworn_presence_strong", "hagraven_presence_strong", "magical_properties_tainted_by_dark_magic", "artifact_location_daedric_razor_pieces", "state_or_condition_current_forsworn_controlled_area"]
            },
            {
                "id": 68,
                "name": "Deepwood Redoubt",
                "desc": "A large Forsworn encampment and Nordic ruin complex northwest of Markarth, serving as a major base and leading to the hagraven lair of Hag's End.",
                "tags": ["structure_type_fortified_camp_ruin_integrated", "forsworn_stronghold_major", "nordic_ruin_integrated", "dungeon_major_complex", "quest_location_exploration_hags_end", "hags_end_access", "forsworn_presence_strong", "hagraven_presence_potential", "state_or_condition_current_forsworn_controlled_area_major_base"]
            },
            {
                "id": 69,
                "name": "Dragontooth Crater",
                "desc": "An ancient, dormant volcanic crater high in the northern mountains of the Reach. While no dragons have been seen for eras, old tales speak of it as a nesting site.", # Adjusted for no active dragons
                "tags": ["unique_natural_formation_volcanic_crater_dormant", "terrain_mountain_peak_remote_northern_reach", "dungeon_potential_lair_ancient_dragon", "dragon_lore_ancient_site_nesting_rumor", "cultural_historical_significance_legendary_site", "climate_alpine_extreme_weather", "exploration_challenge_remote_dangerous"]
            },
            {
                "id": 60001,
                "name": "Hag Rock Redoubt",
                "desc": "A Forsworn-occupied ruin south of Markarth, a constant threat to travelers and caravans in the area.",
                "tags": ["structure_type_ruined_fort", "forsworn_presence_strong", "dungeon_minor", "quest_location_bounty_target_potential", "state_or_condition_current_forsworn_controlled_area", "roadside_danger_spot_south_markarth"]
            },
            {
                "id": 60002,
                "name": "Hag's End",
                "desc": "A ruined tower accessible through Deepwood Redoubt, home to powerful hagravens and an ancient Word Wall.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main_powerful", "dungeon_major", "specific_landmark_type_word_wall_location", "quest_location_exploration_deepwood_redoubt_access", "magical_properties_tainted_by_dark_magic", "hagraven_presence_strong", "state_or_condition_current_forsworn_controlled_area_deepwood"]
            },
            {
                "id": 60003,
                "name": "Karthspire", # Changed from Karthspire Camp to the mountain itself for Sky Haven Temple context
                "desc": "A towering, craggy mountain in the Reach, infamous for its large Forsworn presence at its base, guarding the hidden ascent to ancient ruins.",
                "tags": ["terrain_mountain_peak_landmark_craggy", "state_or_condition_current_forsworn_controlled_area_heavy_base", "cultural_historical_significance_ancient_ruins_summit_rumor_sky_haven", "dangerous_ascent_perilous_forsworn_guardians", "quest_location_main_story_potential_sky_haven_temple", "cultural_historical_significance_blades_related_rumor"]
            },
            {
                "id": 60004,
                "name": "Kolskeggr Mine",
                "desc": "A rich gold mine east of Markarth, currently abandoned or lightly worked due to frequent and brutal Forsworn attacks that have driven off miners.",
                "tags": ["structure_type_mine_abandoned_gold", "economic_activity_mining_gold_historic_rich", "state_or_condition_current_forsworn_controlled_area_attacks_severe", "quest_location_reclaim_mine_kolskeggr", "state_or_condition_current_abandoned_due_to_danger", "resource_node_gold_valuable", "forsworn_presence_strong_nearby_attacks"]
            },
            {
                "id": 60005,
                "name": "Left Hand Mine",
                "desc": "An iron mine located just outside Markarth, owned by Skaggi Scar-Face, providing steady work for the town.",
                "tags": ["structure_type_mine_active_iron", "economic_activity_mining_iron", "resource_node_iron", "settlement_minor_support_markarth", "local_employer_markarth_outskirts", "quest_giver_potential_mine_owner_skaggi"]
            },
            {
                "id": 60006,
                "name": "Lost Valley Redoubt",
                "desc": "A major Forsworn encampment built around scenic waterfalls and ancient Nordic structures, home to powerful Forsworn Briarhearts and an ancient Word Wall.",
                "tags": ["structure_type_fortified_camp_ruin_integrated", "forsworn_stronghold_major_scenic", "unique_natural_formation_waterfall_location_defensive", "nordic_ruin_integrated", "dungeon_major", "specific_landmark_type_word_wall_location", "briarheart_presence_strong", "forsworn_presence_strong", "state_or_condition_current_forsworn_controlled_area_major_base"]
            },
            {
                "id": 60007,
                "name": "Reachcliff Cave",
                "desc": "A cave south of Markarth. While sometimes occupied by undead, it's also known as a site for a dark Daedric ritual involving Namira.",
                "tags": ["structure_type_natural_cave", "undead_presence_potential_draugr", "quest_location_daedric_namira_cannibalism", "dungeon_minor", "ritual_site_dark_daedric_namira", "magical_properties_daedric_influence_overt_namira", "faction_cannibal_cult_potential_eola", "state_or_condition_current_desecrated_potential"]
            },
            {
                "id": 60008,
                "name": "Reachwind Eyrie",
                "desc": "A ruined Dwemer tower on a clifftop overlooking the Karth River. It's often used as a lookout or minor outpost by Forsworn or bandits.",
                "tags": ["structure_type_ruined_tower_dwemer", "forsworn_outpost_potential", "bandit_lookout_potential", "scenic_vista_strategic_river_view_karth", "terrain_cliffside_eyrie", "cultural_historical_significance_dwemer_ruin_minor", "dungeon_minor_tower_ruin"]
            },
            {
                "id": 60009,
                "name": "Red Eagle Redoubt",
                "desc": "A large Forsworn camp and Nordic ruin complex, central to the legend of the ancient Reach hero, Red Eagle. Many Forsworn revere this site.",
                "tags": ["structure_type_fortified_camp_ruin_integrated", "forsworn_camp_historic_revered", "nordic_ruin_integrated", "dungeon_major", "cultural_historical_significance_legendary_hero_location_red_eagle", "quest_location_lore_artifact_red_eagles_bane", "forsworn_presence_strong", "cultural_historical_significance_forsworn_hero_site", "artifact_location_unique_item_potential_red_eagles_fury", "state_or_condition_current_forsworn_controlled_area_major_base"]
            },
            {
                "id": 60010,
                "name": "Sky Haven Temple", # Corrected State
                "desc": "An ancient, forgotten temple complex high in the Karthspire mountain, rumored to have once been a sanctuary for a lost order of dragon hunters. Its exact location is a mystery, likely hidden behind perilous Forsworn territory and natural barriers.",
                "tags": ["structure_type_temple_ruined_ancient", "cultural_historical_significance_historic_temple_lost_blades", "secret_location_rumored_hidden_karthspire", "dragon_lore_ancient_site_blades_related", "terrain_mountain_peak_hidden_karthspire", "cultural_historical_significance_ancient_ruin_blades", "faction_blades_history_rumored_hq", "cultural_historical_significance_blades_hq_ancient", "quest_location_main_story_potential_elder_scroll_related"],
                "sub_locations": [
                    {
                        "id": 600101,
                        "name": "Alduin's Wall",
                        "desc": "A massive, ancient carved wall rumored to exist deep within the Karthspire ruins. Its intricate carvings are believed by some to depict ancient dragon myths or forgotten histories. Its true meaning is lost to time.",
                        "tags": ["historic_artifact_legendary_prophetic", "ancient_carving_prophetic_rumor_dragon_war", "dragon_myth_depiction_alduin_defeat", "cultural_historical_significance_prophetic_wall_blades", "faction_blades_lore_central", "dwemer_influence_potential_construction_rumor", "unique_landmark_iconic_wall"]
                    }
                    # Armory might not be known or accessible yet
                ]
            },
            {
                "id": 60011,
                "name": "Soljund's Sinkhole",
                "desc": "A moonstone mine east of Markarth that has recently broken into a draugr-infested Nordic ruin, causing terror among the miners.",
                "tags": ["structure_type_mine_active_moonstone", "economic_activity_mining_moonstone", "nordic_ruin_breach_recent_sinkhole", "undead_presence_strong_draugr_infestation", "dungeon_minor_mine_ruin_combo", "resource_node_moonstone_dangerous", "quest_location_clear_mine_soljunds_sinkhole", "state_or_condition_current_recently_attacked_recovering_potential"]
            },
            {
                "id": 60012,
                "name": "Old Hroldan Inn",
                "desc": "An ancient inn located in the Reach, south of Soljund's Sinkhole. Legends claim Tiber Septim himself once stayed here, and a ghostly presence is sometimes felt.",
                "tags": ["structure_type_inn_building_ancient", "tavern_remote_historic", "cultural_historical_significance_historic_site_tiber_septim_stayed", "magical_properties_haunted_aura_potential_ghost_quest", "isolated_lodging", "rumor_source_local_legends_ghosts", "food_drink_vendor", "quest_location_ghost_of_old_hroldan"]
            },
            # New Reach Locations
            {
                "id": 60013,
                "name": "Mor Khazgur",
                "desc": "An Orc stronghold in the northwestern Reach, known for its skilled hunters and fierce warriors, led by Chief Larak.",
                "tags": ["orc_stronghold", "populated_settlement_orcish", "tribal_community_orcish", "terrain_mountain_settlement_fortified_northwestern_reach", "economic_activity_hunting_furs_meat_skilled", "warrior_culture_orcish", "malacath_worship", "structure_type_fortified_settlement", "economic_activity_mining_orichalcum_potential", "cultural_historical_significance_orc_tradition", "faction_orc_tribe_mor_khazgur", "climate_temperate_alpine"],
                "sub_locations": [
                    {
                        "id": 600131,
                        "name": "Larak's Longhouse",
                        "desc": "The longhouse of Chief Larak, leader of Mor Khazgur.",
                        "tags": ["structure_type_longhouse_orcish", "government_tribal", "chieftains_hall", "residence_chief"]
                    },
                    {
                        "id": 600132,
                        "name": "Mor Khazgur Mine (Orichalcum)",
                        "desc": "The stronghold's orichalcum mine, crucial for their smithing and economy.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_orichalcum", "resource_node_orichalcum", "orc_controlled_mine"]
                    }
                ]
            },
            {
                "id": 60014,
                "name": "Purewater Run",
                "desc": "A small, hidden cave system behind a waterfall, known for its remarkably clear stream and rare fish. Sometimes used by outlaws as a discreet meeting place.",
                "tags": ["structure_type_natural_cave_hidden_waterfall", "unique_natural_formation_clear_spring_rare_fish", "economic_activity_fishing_rare_fish_source", "bandit_minor_camp_potential_outlaw_meeting_spot", "dungeon_minor", "terrain_mountainous_reach", "environment_wilderness", "alchemy_ingredient_source_rich_potential_rare_flora_fauna", "secluded_nature_spot_picturesque"],
            },
            {
                "id": 60015,
                "name": "Reachwind Crag",
                "desc": "A series of treacherous, wind-swept cliffs and narrow paths, home to territorial hagravens and offering perilous views over the Karth River valley.",
                "tags": ["terrain_cliff_network_treacherous", "specific_landmark_type_hagraven_coven_lair_main_territory", "dangerous_terrain_high_winds_narrow_paths", "scenic_vista_perilous_river_view_karth", "monster_den_hagraven_strong", "forsworn_presence_potential_allies", "terrain_mountainous_reach", "environment_wilderness", "dungeon_minor_outdoor_cliffside", "state_or_condition_current_lawless_area_hagraven"]
            },
            {
                "id": 60016,
                "name": "Reachwater Rock",
                "desc": "A cave system behind a waterfall in the Reach, containing ancient Nordic ruins and playing a part in the legend of the Gauldur Amulet.",
                "tags": ["structure_type_natural_cave_waterfall_hidden", "nordic_ruin_interior_gauldur_legend", "dungeon_major", "quest_location_artifact_gauldur_amulet_fragment_final_assembly", "cultural_historical_significance_ancient_magical_site_gauldur", "terrain_mountainous_reach", "environment_wilderness", "artifact_location_powerful_gauldur_amulet_complete", "undead_presence_strong_potential_gauldurson_spirits", "puzzle_ancient_nordic_potential_gauldur_lore"],
            },
            {
                "id": 60017,
                "name": "Four Skull Lookout",
                "desc": "A ruined Nordic tower and small barrow complex in the Reach, often occupied by bandits or Forsworn, guarding an ancient Word Wall.",
                "tags": ["structure_type_ruined_tower_nordic_lookout", "nordic_burial_site_minor_complex", "bandit_outpost_potential", "forsworn_camp_potential", "specific_landmark_type_word_wall_location", "dungeon_minor", "terrain_mountainous_reach", "environment_wilderness", "undead_presence_potential_draugr_guardians", "exploration_point_lore_word_wall"]
            },
            {
                "id": 60018,
                "name": "Karthside Hovel",
                "desc": "A tiny, impoverished hamlet of Reach natives clinging to the cliffs near the Karth River, often harassed by both Forsworn and Markarth guards.",
                "tags": ["populated_village_reach_native_poor_hovel", "settlement_minor_cliffside_precarious", "cliffside_dwelling_precarious", "forsworn_sympathizers_potential_oppressed", "state_or_condition_current_conflict_zone_civilian_harassment_guards_forsworn", "terrain_mountainous_karth_river", "environment_wilderness", "social_issue_poverty_extreme", "economic_activity_fishing_subsistence_potential"]
            },
            {
                "id": 60019,
                "name": "Eagles' Nest Farm",
                "desc": "A very remote and high-altitude farm in The Reach, accessible only by treacherous paths, known for its hardy livestock and reclusive owners.",
                "tags": ["structure_type_farmstead_remote_high_altitude", "economic_activity_farming_livestock_hardy_mountain_breeds", "isolated_community_self_sufficient", "dangerous_access_route_treacherous_paths", "terrain_mountain_peak_reach", "environment_wilderness", "hermit_lair_potential_reclusive_family", "unique_produce_mountain_herbs_cheese_potential"]
            },
            {
                "id": 60020,
                "name": "Cliffside Crevice",
                "desc": "A narrow cave system hidden within the steep cliffs of The Reach, a perfect natural hideout for Forsworn scouts or a den for cliff-dwelling creatures.",
                "tags": ["structure_type_natural_cave_cliffside_narrow", "dungeon_minor", "forsworn_hideout_potential_scout_ambush", "monster_den_cliff_creatures_falmer_potential_high_altitude", "natural_fortification_hidden_crevice", "terrain_mountainous_steep_cliffs", "environment_wilderness", "forsworn_presence_potential"]
            },
            {
                "id": 60021,
                "name": "Ruined Dwemer Outpost (Minor)",
                "desc": "The scattered, collapsed remains of a small Dwemer outpost or monitoring station, likely picked clean of valuables long ago but still hinting at their ancient presence.",
                "tags": ["structure_type_ruined_settlement_dwemer_outpost", "dwemer_ruin_minor_outpost_monitoring_station", "cultural_historical_significance_dwemer_ruin_minor", "ancient_technology_remnants_scattered", "exploration_point_minor_lore_dwemer", "terrain_mountainous_reach", "environment_wilderness", "structure_condition_collapsed_extensively_picked_clean"]
            },
            {
                "id": 60022,
                "name": "Fort Sungard (Contested Ruin)",
                "desc": "A large, strategically important fort in the Reach, now mostly in ruins. It's a frequent point of conflict, with Forsworn, bandits, or even small Imperial/Stormcloak scouting parties vying for control of its crumbling walls.",
                "tags": ["structure_type_ruined_fort_major_strategic", "dungeon_major", "state_or_condition_current_forsworn_conflict_zone_contested", "bandit_stronghold_potential", "state_or_condition_current_contested_territory_military_various_factions", "cultural_historical_significance_historic_fort_reach", "terrain_mountainous_reach", "environment_wilderness", "forsworn_presence_potential", "imperial_influence_potential_historic", "stormcloak_influence_potential_historic", "civil_war_quest_historic_site_potential"]
            },
            {
                "id": 60023,
                "name": "Old Gods' Clearing (Reach Wilderness)",
                "desc": "A secluded clearing deep in the Reach wilderness, marked by weathered, primitive stone carvings and arrangements hinting at ancient Reach native worship, pre-dating even the Nords.",
                "tags": ["structure_type_shrine_outdoor_structure_primitive_weathered", "cultural_historical_significance_reachmen_ancient_site_pre_nordic", "forsworn_sacred_site_potential_old_gods", "environment_wilderness_landmark_hidden_clearing", "ritual_site_old_gods_forsworn", "terrain_mountainous_deep_reach", "magical_properties_enchanted_neutral_potential_ancient_power", "forsworn_presence_spiritual_gathering_place"]
            },
            {
                "id": 60024,
                "name": "Briarheart Warren",
                "desc": "A small, thorny cave system hidden in the rugged hills of the Reach, rumored to be a place where Forsworn Briarhearts are created or where they retreat to recover.",
                "tags": ["structure_type_natural_cave_thorny_hidden", "dungeon_minor", "forsworn_ritual_site_briarheart_rumor_creation", "forsworn_hideout_secret_briarheart_retreat", "dangerous_flora_thorns_briars", "terrain_mountainous_rugged_hills_reach", "environment_wilderness", "magical_properties_ritualistic_dark_nature_magic", "forsworn_presence_strong_potential_guardians", "briarheart_presence_potential_recovering_created"]
            },
            {
                "id": 60025,
                "name": "The Lover Stone",
                "desc": "An ancient Standing Stone found in the rugged hills east of Markarth, said to grant those who touch it a quicker aptitude in all endeavors.",
                "tags": ["specific_landmark_type_standing_stone_magical", "buff_skill_learning_all_increased_lovers_comfort_effect", "terrain_mountainous_rugged_hills_east_markarth", "cultural_historical_significance_ancient_magical_site", "environment_wilderness_reach", "magical_properties_enchanted_positive_utility", "power_skill_boost_passive"]
            },
            {
                "id": 60026,
                "name": "Valthume",
                "desc": "An ancient and sprawling Nordic ruin deep in the mountains of The Reach, southeast of Markarth. It is the burial place of the Dragon Priest Hevnoraak and a site of significant old power.",
                "tags": ["nordic_burial_site_major_dragon_priest_tomb", "dungeon_large_complex_sprawling", "cultural_historical_significance_dragon_cult_lair_priest_hevnoraak", "undead_presence_strong_powerful_draugr_priest", "cultural_historical_significance_ancient_magical_site_old_power", "specific_landmark_type_word_wall_location", "quest_location_dragon_priest_hevnoraak", "artifact_location_powerful_mask_hevnoraak", "draugr_heavy", "terrain_mountainous_reach_southeast_markarth"]
            },
            {
                "id": 60029,
                "name": "Rebel's Cairn",
                "desc": "An ancient cairn in the Reach, west of Karthwasten, said to be the burial site of a legendary Forsworn hero. It is a sacred place for some Reachmen and may hold ancient secrets or guardians.",
                "tags": ["structure_type_ruined_shrine_cairn_ancient", "cultural_historical_significance_forsworn_hero_site_legendary", "forsworn_sacred_site_revered", "dungeon_minor_historic_burial", "undead_guardian_potential_hero_spirit", "reach_lore_heroic_figure_red_eagle_related_potential", "terrain_mountainous_west_karthwasten", "environment_wilderness", "forsworn_presence_spiritual_pilgrimage_potential", "quest_location_local_legend_potential_artifact"]
            },
            {
                "id": 60030,
                "name": "Blind Cliff Bastion",
                "desc": "A ruined Nordic tower complex built into the cliffs of the Reach, now a formidable Forsworn stronghold. Distinct from Blind Cliff Cave.",
                "tags": ["structure_type_ruined_fort_nordic_cliffside_bastion", "forsworn_stronghold_major_cliffside", "dungeon_major_vertical_complex", "dangerous_approach_forsworn_defenses", "reach_fortification_native_repurposed", "terrain_mountainous_cliffs_reach", "environment_wilderness", "forsworn_presence_strong", "hagraven_presence_potential", "state_or_condition_current_forsworn_controlled_area_major_base"]
            }
        ]
    },

    # EASTMARCH
    {
        "id": 7,
        "name": "Eastmarch",
        "desc": "A harsh, volcanic hold in eastern Skyrim, dominated by the ancient city of Windhelm, seat of Jarl Ulfric Stormcloak and a center of growing rebellion. Known for its hot springs, giants, and fierce Nordic traditions.", # Adjusted capital status
        "tags": ["hold", "terrain_volcanic_tundra", "nordic_culture_strong_ancient", "stormcloak_presence_strong_capital", "terrain_hot_springs", "specific_landmark_type_giant_camp_region", "political_tension_high_civil_war_epicenter", "morrowind_border_region", "climate_subarctic_volcanic", "environment_geothermal_area", "dunmer_refugee_presence_significant", "argonian_worker_presence_significant"],
        "demographics": {"Nord": 90, "Dunmer": 5, "Argonian": 3, "Others": 2},
        "travel": {
            "roads": ["Whiterun Hold", "The Rift", "The Pale", "Winterhold"],
            "paths": ["Volcanic Tundra Trail", "Dunmeth Pass to Morrowind (treacherous)"]
        },
        "sub_locations": [
            {
                "id": 70,
                "name": "Windhelm",
                "desc": "One of Skyrim's oldest cities, the traditional capital of the First Empire, and current seat of Jarl Ulfric Stormcloak. It is a city of stone, snow, and strong anti-Imperial sentiment, a focal point of brewing rebellion.",
                "tags": ["populated_city", "cultural_historical_significance_historic_capital_nordic_first_empire", "nordic_architecture_ancient_stone", "city_affiliation_eastmarch_capital", "stormcloak_presence_strong_hq_ulfric", "settlement_features_district_ethnic_dunmer_gray_quarter", "settlement_features_district_ethnic_argonian_assemblage_docks", "political_tension_high_civil_war_focus_rebellion_capital", "settlement_features_jarls_longhouse_ulfric_palace_of_kings", "climate_arctic_coastal", "structure_type_fortified_city_wall_ancient", "urban_issues_or_atmosphere_tense_atmosphere_racial_political", "unique_landmark_iconic_palace_of_kings_gray_quarter", "urban_issues_or_atmosphere_racial_tension_overt"],
                "sub_locations": [
                    {
                        "id": 7001,
                        "name": "Candlehearth Hall",
                        "desc": "A historic and popular tavern in Windhelm, known for its large central hearth that has burned for centuries, and its warm atmosphere.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "cultural_historical_significance_historic_site", "rumor_source", "food_drink_vendor", "lodging_available"]
                    },
                    {
                        "id": 7002,
                        "name": "Oengul's Smithy",
                        "desc": "The workshop of Oengul War-Anvil and his apprentice Hermir Strong-Heart, providing quality arms and armor to the Nords of Windhelm.",
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor", "item_type_armor_vendor"]
                    },
                    {
                        "id": 7003,
                        "name": "Palace of the Kings",
                        "desc": "The formidable ancient seat of Ysgramor's dynasty, now serving as Jarl Ulfric Stormcloak's residence and military headquarters for his growing faction.",
                        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local_stormcloak", "military_presence_stormcloak_hq", "cultural_historical_significance_ysgramor_related_site", "stormcloak_presence_strong", "unique_landmark_iconic", "political_tension_high_civil_war_focus"]
                    },
                    {
                        "id": 7004,
                        "name": "The White Phial",
                        "desc": "An esteemed apothecary shop run by the aging and ailing Nurelion, who is obsessed with finding the legendary artifact of the same name.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_location_unique_artifact_white_phial", "unique_item_lore_artifact"]
                    },
                    {
                        "id": 7005,
                        "name": "Sadri's Used Wares",
                        "desc": "Revyn Sadri's shop in the Dunmer Gray Quarter, offering a variety of second-hand goods and curiosities. He strives to be an honest merchant amidst hardship.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "dunmer_culture_local", "settlement_features_district_ethnic_dunmer_gray_quarter"]
                    },
                    {
                        "id": 7006,
                        "name": "Windhelm Market Square",
                        "desc": "A bustling open-air market with various stalls near the city gates, offering food, goods, and services. The atmosphere can be tense due to political climate.",
                        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "urban_issues_or_atmosphere_tense_atmosphere"]
                    },
                    {
                        "id": 7007,
                        "name": "Temple of Talos (Windhelm)",
                        "desc": "A place of clandestine Talos worship, highly significant given the Stormcloak cause and the Thalmor's ban. Attended by those loyal to traditional Nord beliefs.",
                        "tags": ["structure_type_temple_building", "religious_site_aedric_secret", "talos_shrine", "nordic_culture_strong", "political_tension_high_religious", "stormcloak_presence_strong", "thalmor_presence_hostile_potential"]
                    },
                    {
                        "id": 7008,
                        "name": "Gray Quarter (Dunmer District)",
                        "desc": "The segregated district where most of Windhelm's Dunmer refugee population resides, often facing prejudice and harsh living conditions.",
                        "tags": ["settlement_features_district_ethnic_dunmer_gray_quarter", "dunmer_culture_strong", "urban_issues_or_atmosphere_oppressive_atmosphere", "social_issue_racism_segregation", "social_issue_poverty"]
                    },
                    {
                        "id": 7009,
                        "name": "Argonian Assemblage (Docks)",
                        "desc": "The dockside area where Windhelm's Argonian dockworkers are forced to live in cramped and poor conditions, working for low wages.",
                        "tags": ["settlement_features_district_ethnic_argonian_assemblage", "argonian_culture_local", "urban_issues_or_atmosphere_oppressive_atmosphere", "social_issue_racism_segregation", "economic_activity_manual_labor", "settlement_features_docks_harbor"]
                    },
                    {
                        "id": 7010,
                        "name": "Aretino Residence",
                        "desc": "The home of Aventus Aretino, a young boy attempting to perform the Black Sacrament to contact the Dark Brotherhood after the death of his mother.",
                        "tags": ["structure_type_residence", "quest_location_dark_brotherhood_initiation", "social_issue_child_neglect_potential", "urban_dwelling_modest", "magical_properties_ritualistic_dark_sacrament"]
                    },
                    {
                        "id": 7011,
                        "name": "Hall of the Dead (Windhelm)",
                        "desc": "Windhelm's catacombs for honoring the dead, maintained by Helgird, a priestess of Arkay, who also deals with the city's recent murder victims.",
                        "tags": ["structure_type_catacombs_structure", "religious_site_aedric", "arkay_presence", "nordic_burial_site_major", "quest_location_investigation_serial_killer", "undead_presence_rumored_low"]
                    },
                    { # Added Windhelm Port
                        "id": 7012,
                        "name": "Windhelm Port",
                        "desc": "The icy docks of Windhelm, a vital hub for trade with northern Tamriel and Solstheim, despite the harsh conditions. Home to the East Empire Company office.",
                        "tags": ["settlement_features_docks_harbor", "economic_activity_trade_hub_major_maritime", "travel_hub_sea_solstheim", "climate_arctic_coastal", "east_empire_company_presence", "argonian_culture_local_nearby"]
                    }
                ]
            },
            {
                "id": 71,
                "name": "Kynesgrove",
                "desc": "A small, industrious mining village on the slopes of the volcanic tundra, known for its malachite mine. It is also situated near an ancient dragon burial site, a fact known to few.", # Removed recent dragon trouble
                "tags": ["populated_village", "settlement_minor_mining", "economic_activity_mining_malachite", "terrain_volcanic_tundra_slope", "dragon_lore_ancient_site_burial_nearby", "climate_subarctic_volcanic", "quest_location_main_story_early_dragon_sighting_kynesgrove"],
                 "sub_locations": [
                    {
                        "id": 7101,
                        "name": "Braidwood Inn",
                        "desc": "The local inn in Kynesgrove, providing food, lodging, and news to miners and travelers.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source"]
                    },
                    {
                        "id": 7102,
                        "name": "Steamscorch Mine",
                        "desc": "The malachite mine that is the lifeblood of Kynesgrove, a source of valuable ore.", # Removed dragon trouble
                        "tags": ["structure_type_mine_active", "economic_activity_mining_malachite", "resource_node_malachite", "dragon_lore_ancient_site_burial_nearby_mine_entrance_potential_impact", "quest_location_main_story_early_dragon_sahloknir_attack"]
                    }
                ]
            },
            {
                "id": 72,
                "name": "Fort Amol",
                "desc": "A strategic fort in Eastmarch, currently held by Stormcloak-aligned soldiers, guarding the pass to Whiterun. It has seen skirmishes in the past.",
                "tags": ["structure_type_fortified_keep", "military_presence_stormcloak_garrison", "stormcloak_presence_strong", "dungeon_major_potential_if_contested", "civil_war_quest_historic_site_potential", "terrain_mountain_pass_defense_eastmarch_whiterun", "strategic_location_civil_war"]
            },
            {
                "id": 73,
                "name": "Eldergleam Sanctuary",
                "desc": "A sacred, tranquil grove hidden in Eastmarch, home to the ancient and revered Eldergleam tree. A place of pilgrimage and natural wonder, protected by nature spirits.",
                "tags": ["cultural_historical_significance_sacred_grove_kynareth_eldergleam", "unique_natural_formation_magical_tree_eldergleam", "magical_properties_aedric_blessing_active", "quest_location_kynareth_gildergreen_restoration_whiterun", "monster_den_spriggan_potential_guardians", "secluded_nature_spot_pilgrimage", "alchemy_ingredient_source_rich_unique_bark_sap", "terrain_forest_eastmarch_hidden_sanctuary"]
            },
            {
                "id": 74,
                "name": "Narzulbur",
                "desc": "An Orc stronghold in Eastmarch, situated near a rich ebony mine. They adhere strictly to the Code of Malacath and are wary of outsiders.",
                "tags": ["orc_stronghold", "populated_settlement_orcish", "economic_activity_mining_ebony", "malacath_worship", "structure_type_fortified_settlement", "cultural_historical_significance_orc_tradition", "terrain_volcanic_tundra_mountains_eastmarch", "warrior_culture_orcish", "isolated_location", "faction_orc_tribe_narzulbur", "quest_giver_potential_orc_chief_issues"],
                "sub_locations": [
                    {
                        "id": 7401,
                        "name": "Mauhulakh's Longhouse", # More specific name
                        "desc": "The longhouse of Chief Mauhulakh, stern leader of Narzulbur.",
                        "tags": ["structure_type_longhouse_orcish", "government_tribal", "chieftains_hall", "residence_chief"]
                    },
                    {
                        "id": 7402,
                        "name": "Gloombound Mine (Ebony)",
                        "desc": "Narzulbur's productive ebony mine, a source of great wealth and Orcish pride, but also dangers from deep within.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_ebony", "resource_node_ebony", "dungeon_minor_extension_potential", "orc_controlled_mine"]
                    }
                ]
            },
            {
                "id": 75,
                "name": "Ansilvund",
                "desc": "A Nordic ruin in Eastmarch, haunted by powerful draugr and connected to a tragic love story and necromantic rituals performed by Lu'ah Al-Skaven.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong_powerful_draugr_ghosts", "specific_landmark_type_necromancer_lair_luah_al_skaven", "specific_landmark_type_word_wall_location", "magical_properties_tainted_by_dark_magic", "quest_location_local_legend_tragic_love_ansilvund_ghosts", "draugr_heavy", "puzzle_ancient_nordic_lore"]
            },
            {
                "id": 76,
                "name": "Bonestrewn Crest",
                "desc": "A mountain peak in the southern volcanic region of Eastmarch, an ancient dragon lair and site of a Word Wall, though no dragon has roosted here for centuries.", # Adjusted for no active dragons
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "terrain_mountain_peak_volcanic_southern_eastmarch", "dungeon_minor_lair_potential", "cultural_historical_significance_dragon_lore_site_ancient", "climate_subarctic_volcanic", "exploration_point_remote_lore_word_wall"]
            },
            {
                "id": 77,
                "name": "Cronvangr Cave",
                "desc": "A large cave system in the hot springs region of Eastmarch, heavily infested with giant frostbite spiders. Rumors also speak of a hidden vampire presence within.",
                "tags": ["structure_type_natural_cave_large", "monster_den_spider_major_frostbite", "specific_landmark_type_vampire_coven_minor_potential_hidden_section", "dungeon_major", "terrain_hot_springs_nearby_eastmarch", "alchemy_ingredient_source_rich_venom_spider_eggs", "quest_location_bounty_potential_spiders_vampires"]
            },
            {
                "id": 78,
                "name": "Darkwater Crossing",
                "desc": "A small mining settlement on the Darkwater River, primarily focused on corundum ore. A mix of Nords and Argonians work and live here.",
                "tags": ["populated_village_mining", "settlement_minor", "economic_activity_mining_corundum", "argonian_culture_local_workers", "terrain_river_delta_darkwater", "climate_volcanic_tundra_edge", "quest_giver_potential_local_issues_mine_related_argonian_concerns"],
                "sub_locations": [
                    {
                        "id": 7801,
                        "name": "Goldenrock Mine",
                        "desc": "The corundum mine that supports Darkwater Crossing, known for its rich veins.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_corundum", "resource_node_corundum"]
                    }
                ]
            },
            {
                "id": 79,
                "name": "Gallows Rock",
                "desc": "A ruined fort southwest of Windhelm, now serving as a major stronghold for the Silver Hand, hunters of werewolves. A dangerous place for any lycanthrope.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_silver_hand_hq_major", "dungeon_major", "quest_location_companions_guild_hall_silver_hand_conflict", "faction_hostile_silver_hand_stronghold", "state_or_condition_current_enemy_controlled_area_silver_hand", "werewolf_lore_silver_hand_hunters"]
            },
            {
                "id": 70001,
                "name": "Gloomreach",
                "desc": "A dark and winding cave system in the southern mountains of Eastmarch, often inhabited by Falmer, Chaurus, or other dangerous subterranean creatures.",
                "tags": ["structure_type_natural_cave_winding", "falmer_presence_strong_potential", "chaurus_nest_potential", "dungeon_major", "terrain_mountainous_southern_eastmarch", "environment_underground_dark_gloomreach", "state_or_condition_current_lawless_area_falmer_territory_potential", "exploration_challenge_dangerous_subterranean"]
            },
            {
                "id": 70002,
                "name": "Lost Knife Hideout",
                "desc": "A large cave system serving as a major bandit hideout, located near the border with The Rift. Known for its ruthless gang, the 'Lost Knife' bandits.",
                "tags": ["structure_type_natural_cave_large_hideout", "bandit_main_stronghold_lost_knife_gang", "dungeon_major", "state_or_condition_current_bandit_controlled_area", "quest_location_bounty_leader_lost_knife", "economic_activity_looting_storage_bandit_operations", "terrain_eastmarch_rift_border"]
            },
            {
                "id": 70003,
                "name": "Mixwater Mill",
                "desc": "A lumber mill on the White River in Eastmarch, run by Gilfre. A quiet spot, but travelers sometimes report strange noises from the nearby woods at night.",
                "tags": ["structure_type_lumber_mill_site", "settlement_minor", "economic_activity_logging_timber", "terrain_river_delta_white_river", "climate_volcanic_tundra_edge", "mystery_local_rumor_strange_noises_woods", "peaceful_area_potential", "quest_giver_potential_gilfre_marriage_local_issues"]
            },
            {
                "id": 70004,
                "name": "Morvunskar",
                "desc": "A ruined fort south of Windhelm, now occupied by hostile mages. During particular revelries, a portal to Sanguine's realm of Oblivion might be found here.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_mage_lair_hostile_conjurers", "quest_location_daedric_sanguine_a_night_to_remember", "dungeon_major", "magical_properties_daedric_influence_overt_temporary_sanguine_portal", "undead_presence_potential_conjured", "portal_to_oblivion_sanguine_temporary_misty_grove", "terrain_south_windhelm_roadside"]
            },
            {
                "id": 70005,
                "name": "Refugees' Rest",
                "desc": "A small, ruined Nordic structure east of Windhelm, marking a somber historical event related to the Night of Tears or similar ancient tragedy. Often haunted by sorrowful spirits.",
                "tags": ["structure_type_ruined_shrine_nordic_somber", "cultural_historical_significance_nordic_ancient_site_tragedy_night_of_tears_refugees", "magical_properties_haunted_aura_sorrowful_spirits", "undead_presence_ghosts_potential", "terrain_volcanic_tundra_east_windhelm", "night_of_tears_related_rumor", "exploration_point_historic_memorial"]
            },
            {
                "id": 70006,
                "name": "Riverside Shack",
                "desc": "A small, isolated shack on the banks of the White River, sometimes home to a reclusive fisherman, a desperate poacher, or even a territorial creature.",
                "tags": ["structure_type_shack_or_hut_isolated", "terrain_river_delta_white_river", "hermit_lair_potential_fisherman_poacher", "economic_activity_fishing_subsistence_potential", "monster_den_mudcrab_potential", "isolated_location", "exploration_point_minor_dwelling"]
            },
            {
                "id": 70007,
                "name": "Stony Creek Cave",
                "desc": "A cave in the southern part of Eastmarch's volcanic tundra, inhabited by bandits who have discovered a valuable alchemical ingredient deep within - Finn's Lute for the Bards College.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "alchemy_ingredient_source_rich_unique_flora_deep_within", "quest_location_bards_college_finns_lute", "terrain_volcanic_tundra_southern_eastmarch", "treasure_cache_rumored_bandit_loot", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 70008,
                "name": "Traitor's Post",
                "desc": "A small, abandoned shack east of Windhelm, rumored to have been used by outlaws or spies. It's often a meeting point for clandestine activities.",
                "tags": ["structure_type_shack_or_hut_abandoned_ominous", "bandit_minor_camp_potential_clandestine_meeting_spot", "spy_network_rumor_outlaws", "treasure_cache_rumored_hidden", "terrain_volcanic_tundra_roadside_east_windhelm", "quest_location_minor_intrigue_potential", "exploration_point_mystery_shack"]
            },
            {
                "id": 70009,
                "name": "Uttering Hills Cave",
                "desc": "A cave system southwest of Windhelm, serving as a hideout for a group of Summerset Shadows, Altmer bandits.",
                "tags": ["structure_type_natural_cave_system", "bandit_main_stronghold_altmer_summerset_shadows", "dungeon_major", "faction_hostile_summerset_shadows", "quest_location_thieves_guild_potential_summerset_shadows_quest", "altmer_presence_hostile_bandits", "state_or_condition_current_bandit_controlled_area_altmer", "terrain_southwest_windhelm_hills"]
            },
            {
                "id": 70010,
                "name": "Witchmist Grove",
                "desc": "A mystical grove in the southern hot springs region of Eastmarch, home to unique flora, spriggans, and possibly a reclusive hagraven or witch.",
                "tags": ["unique_natural_formation_magical_grove_mystical", "monster_den_spriggan_strong_guardians", "specific_landmark_type_hagraven_coven_lair_potential_reclusive_witch", "terrain_hot_springs_southern_eastmarch", "alchemy_ingredient_source_rich_unique_flora_witchmist", "ritual_site_nature_magic_potential_primal", "magical_properties_enchanted_neutral_wild_magic", "witch_coven_potential_rumor"]
            },
            # New Eastmarch Locations
            {
                "id": 70013,
                "name": "Cragwallow Slope",
                "desc": "A dangerous, rocky slope in the volcanic tundra, known for its frequent rockfalls and as a nesting ground for cliff racers or other aerial predators if they were native.", # Adjusted for Skyrim creatures
                "tags": ["terrain_volcanic_tundra_slope_dangerous", "dangerous_terrain_rockslides_frequent", "monster_den_cliff_racer_skyrim_equivalent_potential_aerial_predators", "environment_wilderness_hazard_zone", "exploration_challenge_environmental_perilous", "climate_subarctic_volcanic", "dungeon_minor_outdoor_hazard_area"]
            },
            {
                "id": 70014,
                "name": "Steamcrag Camp",
                "desc": "A large camp of giants and mammoths situated in the hot springs region of Eastmarch, generally peaceful unless provoked.",
                "tags": ["specific_landmark_type_giant_camp_established_major", "mammoth_herd_grazing_large", "terrain_hot_springs_eastmarch", "neutral_encounter_giant_mammoth_peaceful_unless_provoked", "terrain_volcanic_tundra", "cultural_historical_significance_giant_territory_traditional_camp"]
            },
            {
                "id": 70015,
                "name": "Abandoned Lodge of the Nine Holds",
                "desc": "A once-grand hunting lodge in the eastern forests, now fallen into disrepair and rumored to be haunted by its former occupants or used by bandits.",
                "tags": ["structure_type_lodge_abandoned_grand_historic", "structure_condition_ruined_extensively_dilapidated", "magical_properties_haunted_aura_potential_former_occupants", "bandit_minor_camp_potential_hideout", "terrain_forest_eastmarch_isolated", "dungeon_minor", "cultural_historical_significance_historic_site_minor_nine_holds_lodge"]
            },
            {
                "id": 70016,
                "name": "Witchmist Grove Cave",
                "desc": "A damp, mossy cave system connected to or near Witchmist Grove, likely sharing its magical and dangerous nature, possibly extending the spriggan or hagraven territory.",
                "tags": ["structure_type_natural_cave_damp_mossy", "monster_den_spriggan_potential_witchmist_connection", "specific_landmark_type_hagraven_coven_lair_potential_extension_witchmist", "dungeon_minor", "terrain_hot_springs_nearby_witchmist_grove", "magical_properties_enchanted_neutral_nature_magic", "alchemy_ingredient_source_rich_potential_cave_flora"]
            },
            {
                "id": 70017,
                "name": "Dunmer Refugee Camp (Eastmarch)",
                "desc": "A small, struggling camp of Dunmer refugees who have fled Morrowind, located in a less hospitable part of Eastmarch, seeking safety but finding hardship.",
                "tags": ["populated_village_makeshift_refugee_camp", "settlement_minor_refugee_dunmer", "dunmer_culture_local_displaced", "social_issue_poverty_displacement_hardship", "terrain_volcanic_tundra_edge_eastmarch", "state_or_condition_current_struggling_seeking_safety", "morrowind_border_region_refugees"]
            },
            {
                "id": 70018,
                "name": "Ashfall Farm",
                "desc": "A small, struggling farm in the volcanic tundra of Eastmarch, where hardy Nords attempt to grow crops despite the harsh ashfall and geothermal activity.",
                "tags": ["structure_type_farmstead_struggling", "economic_activity_farming_crops_struggling_hardy_crops", "terrain_volcanic_tundra_ashfall_zone", "climate_harsh_volcanic_geothermal", "settlement_minor", "state_or_condition_current_struggling_resilient_farmers"]
            },
            {
                "id": 70019,
                "name": "Boiling Springs Camp",
                "desc": "A tiny settlement of hunters and trappers who have made their camp near Eastmarch's famous hot springs, utilizing the warm waters and local game.",
                "tags": ["populated_village_makeshift_camp", "settlement_minor_hunter_trapper", "economic_activity_hunting_furs_meat", "terrain_hot_springs_eastmarch", "resource_node_game_geothermal_warmth", "climate_subarctic_volcanic", "unique_lifestyle_hot_springs_campers"]
            },
            {
                "id": 70020,
                "name": "Sulfur-Spring Grotto",
                "desc": "A small cave system near Eastmarch's volcanic hot springs, filled with sulfurous fumes and often home to creatures adapted to the heat, or desperate outcasts.",
                "tags": ["structure_type_natural_cave_grotto", "terrain_hot_springs_volcanic_sulfurous", "monster_den_fire_atronach_potential_heat_adapted_creatures", "alchemy_ingredient_source_rich_sulfur_minerals", "dangerous_environment_fumes_heat", "dungeon_minor", "climate_subarctic_volcanic", "exploration_point_geothermal_cave"]
            },
            {
                "id": 70021,
                "name": "Ruins of Old Amol",
                "desc": "The scattered, ancient foundations and a few crumbling walls of a settlement that predated Fort Amol, now mostly reclaimed by the volcanic tundra.",
                "tags": ["structure_type_ruined_settlement_nordic_ancient", "cultural_historical_significance_nordic_ancient_site_minor_pre_amol", "structure_condition_ruined_extensively_reclaimed_by_tundra", "terrain_volcanic_tundra", "exploration_point_historic_foundations", "archaeology_site_potential_early_nordic"]
            },
            {
                "id": 70022,
                "name": "Shrine of Mara (Eastmarch Hot Springs)",
                "desc": "A small, secluded shrine to Mara, Goddess of Love, nestled among the steaming vents and warm pools of Eastmarch's hot springs. A place of unexpected serenity.",
                "tags": ["structure_type_shrine_outdoor_structure_secluded", "religious_site_aedric", "mara_shrine", "terrain_hot_springs_eastmarch", "secluded_nature_spot_serene", "magical_properties_holy_ground_aedric_potential", "peaceful_area_unexpected_serenity", "exploration_point_religious_hidden"]
            },
            {
                "id": 70023,
                "name": "Shrine of Malacath (Narzulbur Outskirts)",
                "desc": "A crude, outdoor shrine dedicated to Malacath, located a short distance from the Orc stronghold of Narzulbur. Used by Orcs for private offerings or rituals.",
                "tags": ["structure_type_shrine_outdoor_structure_crude_orcish", "religious_site_daedric_orcish_malacath", "malacath_shrine", "orc_culture_strong", "ritual_site_tribal_potential_offerings", "narzulbur_outskirts", "cultural_historical_significance_orc_tradition_worship"]
            },
            {
                "id": 70024,
                "name": "Riverside Shack (Eastmarch Volcanic Plains)",
                "desc": "An isolated, ramshackle hut on the banks of a river cutting through Eastmarch's volcanic plains. Could be home to a reclusive fisherman or a desperate outcast.",
                "tags": ["structure_type_shack_or_hut_ramshackle", "terrain_volcanic_tundra_river_bank", "hermit_lair_potential_fisherman_outcast", "economic_activity_fishing_subsistence_potential", "isolated_location", "climate_subarctic_volcanic", "exploration_point_minor_dwelling_isolated"]
            },
            {
                "id": 70025,
                "name": "Volcanic Vent Cave",
                "desc": "A small cave system formed near an active volcanic vent, filled with heated air and strange mineral deposits. May be home to fire atronachs or other heat-adapted creatures.",
                "tags": ["structure_type_natural_cave_volcanic_vent", "terrain_volcanic_tundra_vent_active", "monster_den_fire_atronach_potential_heat_adapted", "alchemy_ingredient_source_rich_minerals_volcanic", "dangerous_environment_heat_fumes", "dungeon_minor", "climate_subarctic_volcanic", "unique_natural_formation_geothermal_cave"]
            },
            {
                "id": 70026,
                "name": "The Atronach Stone",
                "desc": "A Standing Stone located in the volcanic tundra of Eastmarch, south of Windhelm. It grants a larger pool of magicka but hinders natural regeneration, forcing reliance on absorption or potions.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_powerful_double_edged", "terrain_volcanic_tundra_south_windhelm", "cultural_historical_significance_ancient_magical_site", "buff_magicka_increased_large", "debuff_magicka_regen_slowed_significantly", "power_magic_absorption_passive"]
            },
            {
                "id": 70027,
                "name": "Kagrenzel",
                "desc": "A remote Dwemer ruin in the mountains of Eastmarch, known for its peculiar entrance trap that drops explorers into a deep chasm leading to a Falmer-infested cave system.",
                "tags": ["dwemer_ruin_minor_outpost_remote", "dungeon_major_trap_complex_deadly_entrance", "falmer_presence_strong_connected_cave_system", "ancient_technology_dwemer_trap_peculiar", "terrain_mountainous_eastmarch_velothi_border", "chaurus_nest_potential_deep_within", "cultural_historical_significance_dwemer_ruin_site", "exploration_challenge_deadly_trap_puzzle"]
            },
            {
                "id": 70028,
                "name": "Mistwatch",
                "desc": "A ruined fort in southern Eastmarch, overlooking the road to The Rift. It is currently occupied by a band of bandits led by a charismatic chief, and is connected to a local family's tragedy.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold_charismatic_leader", "dungeon_major", "quest_location_local_legend_rescue_family_tragedy", "terrain_rift_border_overlook_eastmarch", "state_or_condition_current_bandit_controlled_area", "strategic_lookout_decayed_fort"]
            },
            {
                "id": 70029,
                "name": "Mara's Eye Pond",
                "desc": "A small, tranquil pond in Eastmarch, west of Morvunskar. Beneath its surface lies the entrance to Mara's Eye Den, a cave often used by vampires or other creatures.",
                "tags": ["unique_natural_formation_pond_tranquil_surface", "dungeon_access_hidden_underwater_mara_eye_den", "specific_landmark_type_vampire_coven_minor_potential_den", "terrain_volcanic_tundra_edge_west_morvunskar", "mystery_local_hidden_lair", "secluded_nature_spot_deceptive_danger_below"],
                "sub_locations": [
                    {
                        "id": 700291,
                        "name": "Mara's Eye Den",
                        "desc": "A damp cave system accessible from Mara's Eye Pond, often serving as a den for vampires or other creatures seeking a hidden lair.",
                        "tags": ["structure_type_natural_cave", "specific_landmark_type_vampire_coven_minor", "dungeon_minor", "monster_den_vampire", "magical_properties_tainted_by_dark_magic_potential", "secret_location_underwater_access"]
                    }
                ]
            },
            {
                "id": 70030,
                "name": "Abandoned Prison",
                "desc": "A crumbling, forgotten prison in the wilds of Eastmarch, its cells now empty or home to desperate squatters, bandits, or restless spirits of former inmates.",
                "tags": ["structure_type_ruined_prison_forgotten", "structure_condition_abandoned_ruined_crumbling", "dungeon_minor", "bandit_minor_camp_potential_squatters", "magical_properties_haunted_aura_potential_former_inmates", "cultural_historical_significance_historic_site_abandoned_prison", "urban_issues_or_atmosphere_eerie_atmosphere_despair", "exploration_point_historic_ruin_dark_past"]
            }
        ]
    },

    # HAAFINGAR
    {
        "id": 8,
        "name": "Haafingar",
        "desc": "A strategic coastal hold in northwestern Skyrim, dominated by the majestic capital city of Solitude. It is the primary Imperial stronghold in Skyrim and a vital hub for maritime trade.",
        "tags": ["hold", "environment_coastal_major_northwestern_skyrim", "imperial_influence_strong_primary_stronghold_skyrim", "economic_activity_trade_hub_major_maritime_tamriel_wide", "nordic_culture_imperialized_cosmopolitan", "city_affiliation_solitude_capital_skyrim", "settlement_features_bards_college_renowned", "thalmor_presence_strong_embassy_influence", "climate_temperate_coastal", "political_tension_high_imperial_stormcloak_capital_focus", "travel_hub_major_sea_land"],
        "demographics": {"Nord": 65, "Imperial": 25, "Breton": 5, "Others": 5}, # Slightly adjusted for more Imperial presence
        "travel": {
            "roads": ["The Reach", "Whiterun Hold", "Hjaalmarch"],
            "paths": ["Dragon Bridge Road", "Coastal Sea Route (to other ports)", "Northwatch Keep Trail"]
        },
        "sub_locations": [
            {
                "id": 80,
                "name": "Solitude",
                "desc": "The grand capital of Skyrim under Imperial control, perched atop a natural stone arch overlooking the Karth River delta. It is home to High King Torygg in the Blue Palace, the Imperial Legion headquarters at Castle Dour, and the renowned Bards College.", # Updated Jarl
                "tags": ["populated_city_capital_skyrim_grand", "imperial_influence_dominant_seat_of_power", "city_affiliation_haafingar_capital", "economic_activity_trade_hub_major_maritime", "settlement_features_bards_college", "settlement_features_docks_harbor_major", "architecture_grand_imperial_stone_arch", "political_tension_high_imperial_stormcloak_seat_of_power", "unique_landmark_iconic_arch_blue_palace_castle_dour", "structure_type_fortified_city_wall_impressive", "thalmor_presence_strong_embassy_office", "urban_issues_or_atmosphere_bustling_trade_atmosphere_political_intrigue"],
                "sub_locations": [
                    {
                        "id": 8001,
                        "name": "Blue Palace",
                        "desc": "The opulent palace residence of High King Torygg and his court. A center of Imperial administration and Skyrim's nobility.", # Updated Jarl
                        "tags": ["structure_type_palace_or_manor", "government_local_skyrim_capital", "high_king_torygg_residence", "imperial_influence_strong_court", "noble_estate_district", "unique_landmark_iconic"]
                    },
                    {
                        "id": 8002,
                        "name": "Castle Dour",
                        "desc": "A robust Imperial fortification within Solitude, serving as the primary headquarters of the Imperial Legion in Skyrim under the command of a high-ranking Legate (General Tullius not yet arrived or in overall command).", # Adjusted for Tullius
                        "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion_hq", "imperial_influence_dominant_military", "settlement_features_armory_barracks", "government_military_command"]
                    },
                    {
                        "id": 8003,
                        "name": "The Winking Skeever",
                        "desc": "A popular and well-known tavern in Solitude, frequented by locals, travelers, merchants, and a certain boastful mercenary named Gulum-Ei.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available", "quest_giver_potential_gulum_ei"]
                    },
                    {
                        "id": 8004,
                        "name": "Bits and Pieces",
                        "desc": "Sayma's general goods store in Solitude, offering a wide variety of items, from common supplies to imported novelties.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "economic_activity_trade_hub_local"]
                    },
                    {
                        "id": 8005,
                        "name": "Angeline's Aromatics",
                        "desc": "An apothecary shop run by Angeline Morrard, selling potions, ingredients, and alchemical supplies. Angeline is often concerned about her daughter serving in the Legion.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_giver_potential_family_issue"]
                    },
                    {
                        "id": 8006,
                        "name": "Radiant Raiment",
                        "desc": "A fine clothing store run by Taarie and Endarie, Altmer sisters offering fashionable attire and tailoring services, though known for their haughty attitudes.",
                        "tags": ["structure_type_shop_building", "shop_specialty_goods_clothing", "economic_activity_tailoring_high_fashion", "altmer_presence_business", "social_hub_elite_potential"]
                    },
                    {
                        "id": 8007,
                        "name": "Fletcher",
                        "desc": "Fihada's shop specializing in bows, arrows, and other archery supplies, catering to hunters and soldiers alike.",
                        "tags": ["structure_type_shop_building", "shop_specialty_goods_archery", "item_type_weapon_bow_arrow_vendor", "economic_activity_crafting_fletching"]
                    },
                    {
                        "id": 8008,
                        "name": "Solitude Blacksmith (Beirand)",
                        "desc": "Beirand's smithy, located near Castle Dour, providing weapons, armor, and smithing services to the Legion and citizens.",
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor", "item_type_armor_vendor", "imperial_legion_supplier_potential"]
                    },
                    {
                        "id": 8009,
                        "name": "Bards College",
                        "desc": "A renowned institution dedicated to preserving Skyrim's history and fostering the talents of bards, musicians, and performers. They hold an annual festival, the Burning of King Olaf.",
                        "tags": ["structure_type_guild_hall_building_college", "settlement_features_bards_college", "cultural_historical_significance_historic_institution", "quest_location_bards_college_main", "event_festival_king_olaf", "education_arts_music_lore", "unique_landmark_iconic"]
                    },
                    {
                        "id": 8010,
                        "name": "Temple of the Divines (Solitude)",
                        "desc": "A grand temple in Solitude dedicated to the worship of all Eight Divines (Talos worship is suppressed but may occur secretly). A center of religious life and Imperial faith.",
                        "tags": ["structure_type_temple_building_major", "religious_site_aedric_eight_divines", "imperial_influence_strong_religious", "talos_worship_banned_publicly", "event_wedding_location", "settlement_features_temple_divines"]
                    },
                    {
                        "id": 8011,
                        "name": "Solitude Docks",
                        "desc": "The bustling port area of Solitude, handling sea trade from across Tamriel. Home to the East Empire Company Warehouse and various shipping businesses.",
                        "tags": ["settlement_features_docks_harbor_major", "economic_activity_trade_hub_major_maritime", "east_empire_company_presence_hq", "travel_hub_sea_interprovincial", "structure_type_warehouse_district", "economic_activity_shipping_industry"]
                    },
                    {
                        "id": 8012,
                        "name": "Erikur's House",
                        "desc": "The lavish residence of Thane Erikur, an influential and often corrupt noble in Solitude with significant business interests.",
                        "tags": ["structure_type_residence_noble", "noble_estate_district", "political_tension_high_corruption", "economic_activity_trade_shady_deals", "thane_erikur_residence"]
                    },
                    { # Added Thalmor Embassy (conceptual location near Solitude)
                        "id": 8013,
                        "name": "Thalmor Embassy (Access Point/Office in Solitude)",
                        "desc": "While the main embassy is more remote, the Thalmor maintain a significant presence and office within Solitude to oversee Imperial compliance with the White-Gold Concordat, a source of much local resentment.",
                        "tags": ["structure_type_embassy_office", "thalmor_presence_strong_office", "political_tension_high_foreign_occupation_aspect", "white_gold_concordat_enforcement_local", "urban_issues_or_atmosphere_fear_and_superstition_thalmor", "diplomatic_intrigue_high"]
                    }
                ]
            },
            {
                "id": 81,
                "name": "Dragon Bridge",
                "desc": "A quaint village in northwestern Haafingar, built around an ancient and iconic stone bridge spanning the Karth River. It serves as a strategic crossing point and hosts an Imperial outpost.",
                "tags": ["populated_village", "settlement_minor_strategic", "structure_type_bridge_ancient_landmark", "strategic_location_river_crossing", "economic_activity_logging_timber_nearby", "military_presence_imperial_penitus_oculatus", "travel_hub_minor"],
                 "sub_locations": [
                    {
                        "id": 8101,
                        "name": "Four Shields Tavern",
                        "desc": "The inn at Dragon Bridge, a common stop for Imperial soldiers, Penitus Oculatus agents, and travelers on the road to Solitude or the Reach.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source_military_travelers"]
                    },
                    {
                        "id": 8102,
                        "name": "Dragon Bridge Lumber Camp",
                        "desc": "The lumber mill that supports the village of Dragon Bridge, run by Horgeir.",
                        "tags": ["structure_type_lumber_mill_site", "economic_activity_logging_timber", "resource_node_wood"]
                    },
                    {
                        "id": 8103,
                        "name": "Penitus Oculatus Outpost (Dragon Bridge)", # Clarified
                        "desc": "A fortified Imperial outpost near Dragon Bridge, often used by the Penitus Oculatus for operations in Haafingar and the western holds.",
                        "tags": ["structure_type_fortified_outpost", "military_presence_imperial_penitus_oculatus", "imperial_influence_strong_military_intelligence", "strategic_location_monitoring"]
                    }
                ]
            },
            {
                "id": 82,
                "name": "Wolfskull Cave",
                "desc": "A dark, foreboding cave system high in the mountains of Haafingar. Necromancers are rumored to gather here, attempting rituals to resurrect the ancient Wolf Queen Potema.",
                "tags": ["structure_type_natural_cave_large", "dungeon_major", "magical_properties_haunted_aura_strong", "specific_landmark_type_necromancer_ritual_site", "quest_location_potema_wolf_queen", "undead_presence_strong", "magical_properties_tainted_by_dark_magic", "terrain_mountainous_remote"]
            },
            {
                "id": 83,
                "name": "Fort Hraggstad",
                "desc": "An Imperial fort northwest of Solitude, guarding the coastline. It is currently garrisoned by Imperial soldiers, though its readiness might be tested by local banditry or rising Stormcloak sentiment elsewhere.",
                "tags": ["structure_type_fortified_keep_coastal", "military_presence_imperial_legion", "dungeon_major_potential_if_contested", "environment_coastal_defense", "strategic_location_maritime_defense", "civil_war_quest_historic_site_potential"]
            },
            {
                "id": 84,
                "name": "Brinewater Grotto",
                "desc": "A coastal cave system south of Solitude Docks, a known haunt for smugglers and bandits who use its hidden coves to move illicit goods.",
                "tags": ["structure_type_natural_cave_coastal", "economic_activity_smuggling_route_active", "bandit_minor_camp_coastal", "dungeon_minor", "treasure_cache_rumored", "secret_location_cove"]
            },
            {
                "id": 85,
                "name": "Broken Oar Grotto",
                "desc": "A large, hidden coastal cave system north of Solitude, serving as a major pirate and bandit stronghold known as Blackblood Marauders' hideout.",
                "tags": ["structure_type_natural_cave_large_coastal", "specific_landmark_type_pirate_cove_major_blackblood", "bandit_main_stronghold_pirate", "dungeon_major_complex", "quest_location_bounty_leader_pirate", "treasure_cache_major_rumored", "shipwreck_site_potential_interior"]
            },
            {
                "id": 86,
                "name": "Ironback Hideout",
                "desc": "A small, well-hidden cave or ruin serving as a minor bandit hideout in the wilderness of Haafingar, used for ambushing travelers on less-patrolled roads.",
                "tags": ["structure_type_natural_cave_minor_hidden", "bandit_minor_camp_ambush", "dungeon_minor", "wilderness_danger_spot", "terrain_hilly_forested_potential"]
            },
            {
                "id": 87,
                "name": "Pinemoon Cave",
                "desc": "A cave system in the mountains of Haafingar, often inhabited by vampires or other dangerous creatures drawn to its isolation and darkness.",
                "tags": ["structure_type_natural_cave", "specific_landmark_type_vampire_coven_minor_potential", "monster_den_dangerous_creatures", "dungeon_minor_dark", "terrain_mountainous_remote", "magical_properties_tainted_by_dark_magic_potential"]
            },
            {
                "id": 88,
                "name": "Potema's Catacombs",
                "desc": "The extensive catacombs beneath Solitude's Temple of the Divines, where the Wolf Queen Potema's spirit is confronted by those seeking to prevent her return to power.", # Already fitting
                "tags": ["structure_type_catacombs_structure_ancient", "undead_presence_strong_powerful", "dungeon_major_quest_specific", "quest_location_potema_wolf_queen_final", "boss_fight_potema_spirit_powerful", "magical_properties_haunted_aura_strong", "solitude_undercity_access"]
            },
            {
                "id": 89,
                "name": "Ravenscar Hollow",
                "desc": "A small cave on the northern coast of Haafingar, typically home to a coven of hagravens who perform dark rituals overlooking the stormy sea.",
                "tags": ["structure_type_natural_cave_coastal", "specific_landmark_type_hagraven_coven_lair", "ritual_site_dark_magic_coastal", "dungeon_minor", "magical_properties_tainted_by_dark_magic", "monster_den_hagraven"]
            },
            {
                "id": 80001,
                "name": "Shadowgreen Cavern",
                "desc": "A lush, hidden cave system with unique bioluminescent flora and fauna, located southwest of Solitude. A place of surprising beauty and dangerous predators.",
                "tags": ["structure_type_natural_cave_hidden_lush", "unique_natural_formation_bioluminescent_flora", "alchemy_ingredient_source_rich_unique_glowing", "monster_den_spriggan_potential", "monster_den_predator_cave", "dungeon_minor_beautiful_dangerous", "secluded_nature_spot_underground"]
            },
            {
                "id": 80002,
                "name": "Steepfall Burrow",
                "desc": "A small cave system or den, likely inhabited by frost trolls or ice wraiths, in the snowy mountains of Haafingar, guarding a narrow pass.",
                "tags": ["structure_type_natural_cave_ice", "monster_den_frost_troll_ice_wraith", "terrain_mountain_peak_pass", "dungeon_minor", "climate_glacial", "travel_route_alternative_dangerous_potential"]
            },
            {
                "id": 80003,
                "name": "Stillborn Cave",
                "desc": "A small, eerie cave in Haafingar, rumored to be cursed or haunted by a sorrowful spirit. Few dare to enter.",
                "tags": ["structure_type_natural_cave_minor", "magical_properties_cursed_aura_rumor", "magical_properties_haunted_aura_potential_sorrowful", "local_legend_tragedy", "urban_issues_or_atmosphere_eerie_atmosphere"]
            },
            {
                "id": 80004,
                "name": "The Steed Stone",
                "desc": "A Standing Stone located northwest of Solitude on a high ridge, granting increased carry weight and removing movement penalties from armor.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive_utility", "buff_carry_weight_increased", "buff_armor_no_penalty", "terrain_mountain_ridge_scenic", "cultural_historical_significance_ancient_magical_site"]
            },
            {
                "id": 80005,
                "name": "Katla's Farm",
                "desc": "A farm located just outside Solitude's main gates, providing produce and horses for the city and the Legion. Run by Katla.",
                "tags": ["structure_type_farmstead", "settlement_features_stables_active", "economic_activity_farming_crops_livestock", "item_type_horse_vendor", "solitude_outskirts", "resource_node_food_supply"]
            },
            # New Haafingar Locations
            {
                "id": 80014,
                "name": "Northwatch Keep",
                "desc": "A remote coastal fortress controlled by the Thalmor, used as a prison for those they deem enemies of the Aldmeri Dominion. It is heavily guarded and a symbol of Thalmor oppression.",
                "tags": ["structure_type_fortified_keep_coastal_remote", "thalmor_presence_strong_fortress_prison", "settlement_features_prison_political_thalmor", "political_tension_high_foreign_occupation_stronghold_oppression", "dangerous_infiltration_target_heavily_guarded", "quest_location_rescue_thalmor_prisoners_main_quest_related_potential", "state_or_condition_current_enemy_controlled_area_thalmor", "altmer_presence_hostile_dominant", "environment_coastal_northern_haafingar"]
            },
            {
                "id": 80015,
                "name": "Volskygge",
                "desc": "An ancient Nordic ruin high in the mountains of Haafingar, leading to a Dragon Priest's tomb at its peak. Guarded by draugr and powerful magic.",
                "tags": ["nordic_burial_site_major_mountain_top", "cultural_historical_significance_dragon_cult_lair_priest_volsung", "undead_presence_strong_powerful_draugr_priest", "dungeon_major_complex_mountain_peak_ruin", "specific_landmark_type_word_wall_location", "artifact_location_powerful_mask_volsung", "draugr_heavy", "terrain_mountain_peak_haafingar", "puzzle_ancient_nordic_runes_potential"]
            },
            {
                "id": 80016,
                "name": "Clearpine Pond",
                "desc": "A tranquil pond nestled in the forests of Haafingar, known for its clear waters and abundant fish. A popular spot for local hunters and hermits.",
                "tags": ["unique_natural_formation_pond_tranquil", "terrain_forest_haafingar", "economic_activity_fishing_industry_local_potential_abundant_fish", "hunter_gathering_spot_potential_hermit_camp", "peaceful_area_secluded", "secluded_nature_spot", "alchemy_ingredient_source_rich_potential_pond_flora"]
            },
            {
                "id": 80017,
                "name": "Coastal Watch Fishery",
                "desc": "A small fishing village nestled in a cove near a crumbling, ancient watchtower on Haafingar's coast. The villagers are wary of both pirates and the crumbling tower's secrets.",
                "tags": ["populated_village_fishing", "settlement_minor_fishing_coastal_cove", "economic_activity_fishing_industry_local", "structure_type_ruined_tower_nearby_watchtower", "pirate_threat_local_rumor_coastal_raids", "cultural_historical_significance_local_legend_mystery_tower", "environment_coastal_cove_haafingar", "climate_temperate_coastal"]
            },
            {
                "id": 80018,
                "name": "Shepherd's Rest Farm",
                "desc": "A secluded farm high in the hills of Haafingar, known for its hardy mountain sheep and the potent, if rough, cheese made from their milk.",
                "tags": ["structure_type_farmstead_remote_highland", "economic_activity_farming_livestock_sheep_hardy", "unique_produce_cheese_mountain_potent", "isolated_location_haafingar_hills", "terrain_hilly_pastoral", "settlement_minor", "family_owned_farm_reclusive"]
            },
            {
                "id": 80019,
                "name": "Smuggler's Cove (Minor)",
                "desc": "A small, well-hidden sea cave on Haafingar's coast, used by petty smugglers to land illicit goods or hide from patrols. Likely contains a small cache.",
                "tags": ["structure_type_natural_cave_coastal_hidden_sea_cave", "dungeon_minor", "economic_activity_smuggling_cache_small_petty_smugglers", "secret_location_cove_hidden_entrance", "treasure_cache_rumored_minor_illicit_goods", "exploration_point_smugglers_den"]
            },
            {
                "id": 80020,
                "name": "Ruined Coastal Shrine",
                "desc": "The crumbling remains of a small, ancient shrine dedicated to an unknown sea deity or ancestor, battered by the coastal winds and waves of Haafingar.",
                "tags": ["structure_type_ruined_shrine_coastal_ancient", "cultural_historical_significance_ancient_religious_site_unknown_sea_deity_ancestor", "structure_condition_weathered_ruined_battered", "environment_coastal_exposed_windswept", "mystery_local_forgotten_god_sea_worship", "exploration_point_historic_religious_site"]
            },
            {
                "id": 80021,
                "name": "Widow's Watch Ruins",
                "desc": "The crumbling remains of a small watchtower on a lonely cliff overlooking the Sea of Ghosts. Local tales say it was built by a noblewoman awaiting her lost husband's return from sea, and her sorrowful spirit still lingers.",
                "tags": ["structure_type_ruined_tower_coastal_watchtower", "dungeon_minor", "magical_properties_haunted_aura_potential_sorrowful_widow_spirit", "scenic_vista_panoramic_coastal_ruined_sea_of_ghosts", "cultural_historical_significance_local_legend_tragic_lost_husband", "structure_condition_ruined_extensively_crumbling", "exploration_point_haunted_ruin"]
            },
            {
                "id": 80022,
                "name": "Shrine of Dibella (Wilderness - Haafingar)",
                "desc": "A secluded, beautifully maintained outdoor shrine to Dibella, hidden in a picturesque grove or clifftop in Haafingar's wilderness. A place of quiet inspiration and artistic offerings.",
                "tags": ["structure_type_shrine_outdoor_structure_beautiful", "religious_site_aedric", "dibella_shrine", "secluded_nature_spot_picturesque_grove_cliffside", "magical_properties_holy_ground_aedric_potential", "art_beauty_focus_inspiration_offerings", "terrain_grove_cliffside_potential_haafingar_wilderness", "exploration_point_religious_hidden_serene"]
            },
            {
                "id": 80024,
                "name": "The Katariah (Imperial Flagship)",
                "desc": "A massive Imperial warship, often docked at Solitude or patrolling the Sea of Ghosts. It represents the might of the Imperial Navy in Skyrim's waters. (May not be Emperor Titus Mede II's personal vessel in 4E 200, but a significant flagship).",
                "tags": ["structure_type_ship_imperial_warship_major_flagship", "military_presence_imperial_navy_skyrim_fleet", "solitude_docks_visitor_potential_patrol_route", "environment_sea_of_ghosts_patrol_coastal_waters", "unique_landmark_mobile_potential_imperial_might", "imperial_influence_strong_naval_power_projection", "event_encounter_potential_naval_battle_boarding"]
            },
            {
                "id": 80025,
                "name": "Orphan's Tear",
                "desc": "A shipwreck on the northern coast of Haafingar, west of the Solitude Lighthouse. It is rumored to hold lost treasures and is sometimes used as a hideout by coastal scavengers or bandits.",
                "tags": ["structure_type_shipwreck_site_coastal_northern_haafingar", "treasure_cache_rumored_lost_valuable_cargo", "bandit_minor_camp_scavenger_potential_coastal_bandits", "dungeon_minor", "environment_coastal_exploration_wreckage", "quest_location_minor_potential_retrieve_item_clear_scavengers"]
            },
            {
                "id": 80026,
                "name": "Solitude Lighthouse (Structure)",
                "desc": "The tall lighthouse guiding ships into Solitude's harbor. While functional, its keeper might have local concerns or knowledge.",
                "tags": ["structure_type_lighthouse_structure_functional_solitude", "environment_coastal_landmark_navigational_solitude_harbor", "solitude_harbor_aid_shipping_safety", "quest_giver_potential_lighthouse_keeper_concerns_knowledge", "unique_landmark_iconic_local_solitude_skyline", "exploration_point_functional_lighthouse"]
            },
            {
                "id": 80027,
                "name": "The Dainty Sload",
                "desc": "A notorious pirate or smuggler ship that sometimes anchors in hidden coves along Haafingar's coast, or might even brazenly try to trade illicit goods at the Solitude Docks under a false flag.",
                "tags": ["structure_type_ship_pirate_smuggler_notorious_dainty_sload", "faction_hostile_pirate_sload_crew", "environment_coastal_encounter_hostile_potential_hidden_coves_docks", "economic_activity_smuggling_illicit_trade_skooma_contraband", "black_market_connection_rumor_riften_solitude", "unique_encounter_named_ship_pirate_captain", "quest_location_bounty_target_potential_ship_captain"]
            }
        ]
    },

    # THE RIFT
    {
        "id": 9,
        "name": "The Rift",
        "desc": "A temperate, autumnal hold in southeastern Skyrim, known for its golden forests, numerous lakes, and the city of Riften, a haven for the Thieves Guild and rife with corruption. It borders Morrowind and Cyrodiil.",
        "tags": ["hold", "terrain_forest_autumnal_large_golden_woods", "terrain_lake_region_abundant_honrich_geir", "faction_thieves_guild_presence_strong_hq_riften", "nordic_culture_local_rift_traditions", "morrowind_border_region_velothi_mountains", "cyrodiil_border_region_jerall_mountains", "urban_issues_or_atmosphere_corrupt_underbelly_pervasive", "political_influence_black_briar_family_dominance_maven", "climate_temperate_continental", "beautiful_scenery_autumnal_lakes", "economic_activity_brewing_mead_ale_black_briar_honningbrew_rivalry_potential", "economic_activity_fishing_industry_local_lakes"],
        "demographics": {"Nord": 75, "Dunmer": 10, "Argonian": 10, "Khajiit": 3, "Others": 2},
        "travel": {
            "roads": ["Whiterun Hold", "Eastmarch", "Falkreath Hold", "Cyrodiil (Lost Prospect Pass)", "Morrowind (Velothi Mountains route)"], # More specific routes
            "paths": ["Goldenglow Path", "Jerall Mountain Trail", "Velothi Mountains Pass", "Lake Honrich Shoreline"]
        },
        "sub_locations": [
            {
                "id": 90,
                "name": "Riften",
                "desc": "A city built upon a lake, with canals running through its wooden structures. It is infamous for corruption, the powerful Black-Briar family's influence, and being the headquarters of the Thieves Guild under Mercer Frey.", # Mercer Frey leadership if pre-TESV TG questline
                "tags": ["populated_city", "terrain_lake_city_canals_wooden_structures", "city_affiliation_the_rift_capital", "faction_thieves_guild_presence_strong_hq_ratway", "political_influence_black_briar_family_total_maven_control", "urban_issues_or_atmosphere_corrupt_city_major_infamous", "settlement_features_jarls_longhouse_laila_law_giver_figurehead", "mercenary_presence_strong_black_briar_thugs", "structure_type_wooden_architecture_canals_unique", "unique_landmark_iconic_canal_city_mistveil_keep", "urban_issues_or_atmosphere_high_crime_rate_thievery"],
                "sub_locations": [
                    {
                        "id": 9001,
                        "name": "The Bee and Barb",
                        "desc": "A popular tavern in Riften, owned by Keerava and Talen-Jei. A common meeting place and source of rumors, often frequented by Thieves Guild associates.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular_riften", "rumor_source_thieves_guild", "food_drink_vendor", "lodging_available", "quest_giver_potential_local_issues"]
                    },
                    {
                        "id": 9002,
                        "name": "Black-Briar Meadery (Riften Building)",
                        "desc": "The main office and shopfront for the powerful Black-Briar Meadery within Riften, a symbol of Maven Black-Briar's economic and political control over the city.",
                        "tags": ["structure_type_shop_building_meadery", "economic_activity_brewing_mead_ale_major_black_briar", "political_influence_black_briar_family_business", "economic_powerhouse_local", "shop_specialty_goods_mead"]
                    },
                    {
                        "id": 9003,
                        "name": "The Pawned Prawn",
                        "desc": "A general goods store in Riften, run by Bersi Honey-Hand. A place to buy and sell various items, some of questionable origin.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "thieves_guild_fence_connection_potential", "economic_activity_trade_hub_local"]
                    },
                    {
                        "id": 9004,
                        "name": "Mistveil Keep",
                        "desc": "The Jarl's residence in Riften, currently home to Jarl Laila Law-Giver, though her authority is often undermined by Maven Black-Briar.", # Laila is Jarl pre-Civil War changes
                        "tags": ["structure_type_palace_or_manor_keep", "settlement_features_jarls_longhouse", "government_local_laila_law_giver", "political_tension_high_black_briar_shadow_rule", "political_influence_black_briar_family_strong"]
                    },
                    {
                        "id": 9005,
                        "name": "The Ratway",
                        "desc": "A dangerous, labyrinthine network of tunnels beneath Riften, serving as the entrance to the Ragged Flagon and the hidden headquarters of the Thieves Guild.",
                        "tags": ["dungeon_major_city_undercity", "thieves_guild_access_route", "criminal_hideout_network", "state_or_condition_current_lawless_area_city_section", "environment_sewers_forgotten_tunnels", "urban_issues_or_atmosphere_dangerous_undercity"],
                        "sub_locations": [
                            {
                                "id": 90051,
                                "name": "The Ragged Flagon",
                                "desc": "A hidden tavern within the Ratway, serving as the main gathering area, bar, and neutral ground for the Thieves Guild and its associates.",
                                "tags": ["structure_type_inn_building_secret", "settlement_features_tavern_thieves_guild", "thieves_guild_hq_meeting_place", "thieves_guild_fence_location", "information_broker_guild_contacts", "social_hub_criminal_underworld"]
                            },
                            {
                                "id": 90052,
                                "name": "The Cistern",
                                "desc": "The secure, inner sanctum and living quarters of the Thieves Guild, deep within the Ratway, accessible only to trusted members.",
                                "tags": ["thieves_guild_hq_inner_sanctum", "settlement_features_training_area_thief_skills", "structure_type_sleeping_quarters_guild", "treasure_cache_guild_vault_potential", "secret_location_guild_only", "faction_thieves_guild_main_base"]
                            }
                        ]
                    },
                    {
                        "id": 9006,
                        "name": "Temple of Mara (Riften)",
                        "desc": "A prominent temple dedicated to Mara, the Divine of Love and Compassion. It is a place for marriages, seeking guidance on love, and helping the needy.",
                        "tags": ["structure_type_temple_building_major", "religious_site_aedric", "mara_shrine_prominent", "event_wedding_location", "quest_location_agents_of_mara", "settlement_features_temple_divines", "social_hub_religious_community"]
                    },
                    {
                        "id": 9007,
                        "name": "The Scorched Hammer",
                        "desc": "Balimund's smithy in Riften, known for its quality craftsmanship and Balimund's expertise with fire salts in forging.",
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production_skilled", "item_type_weapon_vendor", "item_type_armor_vendor", "crafting_specialty_fire_salts"]
                    },
                     {
                        "id": 9008,
                        "name": "Elgrim's Elixirs",
                        "desc": "An apothecary shop run by Elgrim and his wife Hafjorg, located on Riften's lower platforms. Elgrim is a master alchemist, albeit somewhat reclusive.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable_master", "item_type_potion_vendor", "item_type_ingredient_vendor", "hermit_lair_potential_alchemist", "skill_trainer_alchemy_master_potential"]
                    },
                    {
                        "id": 9009,
                        "name": "Riften Marketplace",
                        "desc": "The central market area of Riften, with various stalls selling food, jewelry, and other goods. A prime location for pickpockets and observant guild members.",
                        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular", "thieves_guild_pickpocket_hotspot", "thieves_guild_observation_post_potential"]
                    },
                    {
                        "id": 9010,
                        "name": "Honorhall Orphanage",
                        "desc": "Riften's orphanage, currently run by the cruel Grelod the Kind. The children suffer under her neglect and abuse.",
                        "tags": ["structure_type_orphanage", "quest_location_dark_brotherhood_initiation_aventus", "social_issue_child_abuse_grelod", "urban_issues_or_atmosphere_oppressive_atmosphere_children", "faction_dark_brotherhood_target"]
                    },
                    {
                        "id": 9011,
                        "name": "Black-Briar Manor",
                        "desc": "The grand residence of the powerful and influential Black-Briar family, heavily guarded and a testament to their wealth and control over Riften.",
                        "tags": ["structure_type_residence_noble_manor", "noble_estate_district", "political_influence_black_briar_family_home", "structure_condition_fortified_private", "maven_black_briar_residence", "political_tension_high_power_center"]
                    },
                    { # Added Beggar's Row
                        "id": 9012,
                        "name": "Beggar's Row",
                        "desc": "A dilapidated section of Riften's lower walkways where the city's poorest and most desperate souls eke out a meager existence.",
                        "tags": ["settlement_features_district_slums", "social_issue_poverty_extreme", "beggars_community_hub", "urban_issues_or_atmosphere_desperation_squalor", "structure_condition_dilapidated"]
                    },
                    {
                        "id": 9013,
                        "name": "Riften Warehouse",
                        "desc": "A large warehouse on the Riften docks, often used for storing goods, both legitimate and illicit. Rumored to be a key point in the city's smuggling operations and sometimes used by the Thieves Guild.",
                        "tags": ["structure_type_warehouse_docks", "economic_activity_storage_commercial", "economic_activity_smuggling_hotspot_potential", "thieves_guild_interest_operations", "political_influence_black_briar_family_connection_rumor", "settlement_features_docks_harbor"]
                    }
                ]
            },
            {
                "id": 91,
                "name": "Shor's Stone",
                "desc": "A small mining village in the northern Rift, primarily focused on an ebony mine that has recently been troubled by giant frostbite spiders from a nearby cave.",
                "tags": ["populated_village", "settlement_minor_mining", "economic_activity_mining_ebony", "resource_node_ebony_rare", "monster_infestation_spider_recent", "quest_location_clear_mine", "terrain_northern_rift_mountains"],
                "sub_locations": [
                    {
                        "id": 9101,
                        "name": "Redbelly Mine",
                        "desc": "The ebony mine that is the main source of livelihood for Shor's Stone, currently unsafe due to spider infestation.",
                        "tags": ["structure_type_mine_active_infested", "economic_activity_mining_ebony", "resource_node_ebony_dangerous", "monster_infestation_spider_major", "quest_location_clear_mine_shors_stone", "dungeon_minor_mine_infested"]
                    },
                    {
                        "id": 9102,
                        "name": "Sylgja's House",
                        "desc": "The home of Sylgja, a miner in Shor's Stone, whose father works in Darkwater Crossing.",
                        "tags": ["structure_type_residence", "commoner_dwelling_miner", "quest_giver_potential_family_related"]
                    },
                    { # Added Filnjar's House (Blacksmith)
                        "id": 9103,
                        "name": "Filnjar's House and Smithy",
                        "desc": "The home and modest smithy of Filnjar, the blacksmith of Shor's Stone.",
                        "tags": ["structure_type_residence", "structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor_potential", "item_type_armor_vendor_potential"]
                    }
                ]
            },
            {
                "id": 92,
                "name": "Ivarstead",
                "desc": "A small village at the foot of the Throat of the World, on the shores of Lake Geir. It is the traditional starting point for the pilgrimage up the Seven Thousand Steps to High Hrothgar.",
                "tags": ["populated_village", "settlement_minor_pilgrimage_base", "travel_hub_pilgrimage_high_hrothgar", "terrain_lake_geir_shoreline", "terrain_mountain_foot_throat_of_world", "cultural_historical_significance_greybeards_path_start", "climate_temperate_mountain_valley"],
                "sub_locations": [
                    {
                        "id": 9201,
                        "name": "Vilemyr Inn",
                        "desc": "The local inn of Ivarstead, offering rest to those journeying to High Hrothgar, run by Wilhelm. He is concerned about Shroud Hearth Barrow.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_local", "food_drink_vendor", "lodging_available", "rumor_source", "quest_giver_potential_barrow_investigation"]
                    },
                    {
                        "id": 9202,
                        "name": "Shroud Hearth Barrow (Ivarstead Entrance)", # Clarified
                        "desc": "An ancient Nordic barrow located within Ivarstead itself. Locals believe it to be haunted and avoid it, though Wilhelm seeks someone to investigate.",
                        "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong_draugr", "magical_properties_haunted_aura", "quest_location_local_investigation_ivarstead", "puzzle_dragon_claw_sapphire", "cultural_historical_significance_nordic_ancient_site", "urban_issues_or_atmosphere_haunted_rumors_strong"]
                    },
                    {
                        "id": 9203,
                        "name": "Klimmek's House",
                        "desc": "The home of Klimmek, a resident of Ivarstead who makes regular supply deliveries to High Hrothgar for the Greybeards.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "quest_giver_potential_high_hrothgar_delivery", "greybeards_related_supplier"]
                    },
                    { # Added Narfi's Wrecked House
                        "id": 9204,
                        "name": "Narfi's Wrecked House",
                        "desc": "The ruined and isolated house of Narfi, a distraught beggar living across the river from Ivarstead, searching for his missing sister.",
                        "tags": ["structure_type_ruined_shack", "structure_condition_collapsed", "hermit_lair_beggar", "quest_location_dark_brotherhood_target_potential", "social_issue_poverty_grief", "isolated_location_river_other_side"]
                    }
                ]
            },
            {
                "id": 93,
                "name": "Lost Prospect Mine",
                "desc": "An abandoned gold mine in the Rift, often occupied by bandits. It is rumored to be played out, but some say a few veins might remain for the determined.",
                "tags": ["structure_type_mine_abandoned", "economic_activity_mining_gold_historic", "resource_node_gold_rumored_depleted", "bandit_minor_camp_potential", "dungeon_minor", "exploration_challenge_potential_reward", "terrain_eastern_rift_mountains"]
            },
            {
                "id": 94,
                "name": "Broken Helm Hollow",
                "desc": "A secluded cave system east of Riften, serving as a well-established bandit hideout with multiple chambers.",
                "tags": ["structure_type_natural_cave", "bandit_main_stronghold", "dungeon_major_multi_level", "state_or_condition_current_bandit_controlled_area", "terrain_eastern_rift_forest", "quest_location_bounty_potential"]
            },
            {
                "id": 95,
                "name": "Avanchnzel",
                "desc": "A large and dangerous Dwemer ruin in the southern mountains of the Rift. It contains ancient technology, Falmer, and is the focus of a quest to retrieve a unique Dwemer lexicon for From-Deepest-Fathoms.",
                "tags": ["dwemer_ruin_major_city", "dungeon_large_complex", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "quest_location_unique_artifact_dwemer_lexicon", "ancient_technology_dwemer", "cultural_historical_significance_dwemer_ruin_site", "terrain_southern_rift_mountains", "chaurus_nest_potential"]
            },
            {
                "id": 96,
                "name": "Boulderfall Cave",
                "desc": "A cave in the eastern Rift, often inhabited by necromancers or other dark mages who use its seclusion for their sinister experiments.",
                "tags": ["structure_type_natural_cave", "specific_landmark_type_necromancer_lair", "magical_properties_tainted_by_dark_magic", "dungeon_minor", "undead_presence_skeletons_experiments", "ritual_site_dark_magic", "terrain_eastern_rift_wilderness"]
            },
            {
                "id": 97,
                "name": "Clearspring Tarn",
                "desc": "A small, picturesque tarn and cave system west of Shor's Stone, often home to trolls guarding a treasure hunter's remains and note.",
                "tags": ["structure_type_natural_cave_tarn", "monster_den_troll_guardian", "unique_natural_formation_tarn", "treasure_cache_minor_hunter_remains", "dungeon_minor", "secluded_nature_spot", "alchemy_ingredient_source_rich_potential"]
            },
            {
                "id": 98,
                "name": "Crystaldrift Cave",
                "desc": "A small ice cave south of Riften, notable for its unique crystal formations. It is sometimes a den for frost creatures or a reclusive hermit.",
                "tags": ["structure_type_natural_cave_ice", "unique_natural_formation_crystal_cave", "monster_den_frost_creatures_potential", "hermit_lair_potential", "dungeon_minor", "climate_cold_cave", "alchemy_ingredient_source_rich_crystals_potential"]
            },
            {
                "id": 99,
                "name": "Darklight Tower",
                "desc": "A ruined tower southwest of Riften, now a den for hagravens and the site of a Daedric quest where Illia attempts to stop her mother from becoming a hagraven.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main", "magical_properties_tainted_by_dark_magic", "dungeon_major_vertical", "quest_location_daedric_related_illia", "monster_den_hagraven_powerful", "witch_coven_powerful", "terrain_southern_rift_mountains"]
            },
            {
                "id": 90001,
                "name": "Faldar's Tooth",
                "desc": "A ruined fort west of Riften, initially overrun by wolves, but later becomes a hideout for bandits or the Silver Hand, depending on unfolding events.",
                "tags": ["structure_type_ruined_fort", "dungeon_major_contested", "monster_den_wolf_initial_large", "bandit_main_stronghold_potential", "specific_landmark_type_silver_hand_hq_potential", "strategic_location_west_riften", "state_or_condition_current_dynamic_occupancy"]
            },
            {
                "id": 90002,
                "name": "Fort Greenwall",
                "desc": "A large fort in the eastern Rift, strategically important. Currently garrisoned by Imperial soldiers, but its control is tenuous given the Rift's leanings.",
                "tags": ["structure_type_fortified_keep", "military_presence_imperial_legion", "dungeon_major_potential_if_contested", "strategic_location_eastern_rift_border", "civil_war_quest_historic_site_potential", "state_or_condition_current_contested_by_factions_potential_stormcloak"]
            },
            {
                "id": 90003,
                "name": "Froki's Shack",
                "desc": "The isolated shack of Froki Whetted-Blade, an old hunter and devout follower of Kyne, located in the southern mountains of the Rift. He offers tasks related to Kyne's sacred trials.",
                "tags": ["structure_type_shack_or_hut", "hermit_lair_hunter_devout", "quest_location_kyne_sacred_trials", "religious_site_aedric_kyne_shrine_nearby", "animal_lore_expert", "isolated_location_mountain", "skill_trainer_archery_potential"]
            },
            {
                "id": 90004,
                "name": "Goldenglow Estate",
                "desc": "A large honey farm and apiary on an island in Lake Honrich, owned by Aringoth. It's a major supplier of honey for the Black-Briar Meadery and becomes a key target in a Thieves Guild questline.",
                "tags": ["structure_type_farmstead_apiary_large", "terrain_island_lake_honrich", "quest_location_thieves_guild_major_sabotage", "economic_activity_brewing_mead_ale_supplier_black_briar", "structure_condition_wealthy_estate_guarded", "faction_thieves_guild_target", "unique_produce_honey_goldenglow"]
            },
            {
                "id": 90005,
                "name": "Heartwood Mill",
                "desc": "A lumber mill on the shores of Lake Honrich, run by Grosta. A peaceful location providing wood for Riften.",
                "tags": ["structure_type_lumber_mill_site", "settlement_minor", "economic_activity_logging_timber", "terrain_lake_honrich_shoreline", "peaceful_area", "resource_node_wood"]
            },
            {
                "id": 90006,
                "name": "Honeystrand Cave",
                "desc": "A small cave south of Ivarstead, often a den for bears or other local wildlife.",
                "tags": ["structure_type_natural_cave", "monster_den_bear_common", "dungeon_minor", "terrain_southern_rift_forest", "alchemy_ingredient_source_rich_potential_animal_parts"]
            },
            {
                "id": 90007,
                "name": "Last Vigil",
                "desc": "A ruined watchtower and ancient dragon burial site high in the mountains of the Rift. While no dragons stir now, it's a place of potent old magic and may attract those interested in such power (like ancient vampire cults or dragon scholars).", # Dawnguard reference made generic
                "tags": ["structure_type_ruined_tower", "dragon_lore_ancient_site_burial", "magical_properties_arcane_nexus_ancient", "terrain_mountain_peak_remote", "specific_landmark_type_vampire_coven_minor_potential_interest", "scholar_retreat_rumor_dragon_lore", "dungeon_minor", "cultural_historical_significance_dragon_cult_site_potential"]
            },
            {
                "id": 90008,
                "name": "Merryfair Farm",
                "desc": "A farmstead located near Riften, owned by Dravin Llanith, who is often worried about his stolen bow.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "quest_giver_potential_stolen_item", "riften_outskirts", "settlement_minor"]
            },
            {
                "id": 90009,
                "name": "Nightingale Hall",
                "desc": "The secret sanctuary and headquarters of the Nightingales, protectors of Nocturnal's shrine, hidden within a cave system in the Rift. Its existence is known only to the highest echelons of the Thieves Guild.",
                "tags": ["structure_type_secret_sanctuary_cave", "faction_nightingales_hq", "religious_site_daedric_nocturnal_shrine", "thieves_guild_elite_order_related", "dungeon_major_quest_specific", "magical_properties_daedric_influence_overt_nocturnal", "secret_location_guild_elite_only", "artifact_location_nightingale_armor_weapons"]
            },
            {
                "id": 90010,
                "name": "Nilheim",
                "desc": "A ruined watchtower east of Ivarstead, occupied by bandits who employ a clever ambush by pretending to be legitimate guards.",
                "tags": ["structure_type_ruined_tower", "bandit_minor_camp_deceptive_ambush", "dungeon_minor", "roadside_danger_spot", "quest_location_minor_investigation_potential", "terrain_eastern_rift_roadside"]
            },
            {
                "id": 90011,
                "name": "Northwind Summit",
                "desc": "A mountain peak in the northern Rift, near Shor's Stone, known as an ancient dragon lair and the site of a Word Wall.", # No active dragon
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "terrain_mountain_peak_high", "dungeon_minor_lair_potential", "cultural_historical_significance_dragon_lore_site_ancient", "undead_presence_draugr_potential"]
            },
            {
                "id": 90012,
                "name": "Pinepeak Cavern",
                "desc": "A cave system near Ivarstead, often inhabited by bears or other forest creatures.",
                "tags": ["structure_type_natural_cave", "monster_den_bear_common", "dungeon_minor", "terrain_forest_ivarstead_nearby", "alchemy_ingredient_source_rich_potential_animal_parts"]
            },
            {
                "id": 90013,
                "name": "Redwater Den",
                "desc": "A rundown shack that serves as a front for a clandestine skooma operation, possibly with ties to a darker, more sinister group dealing in a particularly potent brew.", # Dawnguard ref made generic
                "tags": ["structure_type_shack_or_hut_front", "economic_activity_skooma_production_distribution_hidden", "dungeon_major_underground_complex", "specific_landmark_type_vampire_coven_minor_potential_skooma_blood", "criminal_hideout_network_skooma", "magical_properties_tainted_by_dark_magic_potential", "quest_location_dawnguard_potential_alt"]
            },
            {
                "id": 90014,
                "name": "Sarethi Farm",
                "desc": "A farmstead near Ivarstead, run by Avrusa Sarethi, an alchemist known for successfully cultivating Nirnroot.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_alchemy", "alchemy_ingredient_source_rich_nirnroot_cultivated", "quest_giver_potential_alchemy_research", "settlement_minor", "dunmer_culture_local_farmer_alchemist"]
            },
            {
                "id": 90015,
                "name": "Snapleg Cave",
                "desc": "A cave system south of Ivarstead, often home to spriggans, witches, or hagravens drawn to its primal energies.",
                "tags": ["structure_type_natural_cave", "magical_properties_enchanted_primal", "monster_den_spriggan_strong", "specific_landmark_type_hagraven_coven_lair_potential", "witch_coven_potential", "dungeon_minor", "ritual_site_nature_magic_potential", "terrain_southern_rift_forest"]
            },
            {
                "id": 90016,
                "name": "Snow-Shod Farm",
                "desc": "A farmstead near Riften, owned by the influential Snow-Shod family, who are staunch supporters of Ulfric Stormcloak.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_livestock", "political_influence_stormcloak_family_snow_shod", "riften_outskirts", "settlement_minor", "nordic_culture_strong"]
            },
            {
                "id": 90017,
                "name": "Stendarr's Beacon",
                "desc": "A ruined watchtower in the eastern Rift, now maintained by the Vigilants of Stendarr as an outpost in their crusade against Daedra, vampires, and other abominations.",
                "tags": ["structure_type_ruined_tower_repurposed", "faction_vigilants_of_stendarr_outpost", "religious_military_order_anti_daedra", "dungeon_minor_fortified", "quest_location_vigilant_tasks_potential", "terrain_eastern_rift_mountains", "state_or_condition_current_vigilant_controlled_area"]
            },
            {
                "id": 90018,
                "name": "Treva's Watch",
                "desc": "A ruined fort west of Ivarstead, taken over by bandits. Stalleo, a Nord whose family was driven out, seeks help to reclaim it.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold", "dungeon_major", "quest_location_reclaim_fort_family", "state_or_condition_current_bandit_controlled_area", "terrain_western_rift_river"]
            },
            {
                "id": 90019,
                "name": "Tolvald's Cave",
                "desc": "A very large and dangerous cave system in the Velothi Mountains on the border with Morrowind, infested with Falmer, Chaurus, and possibly other deep-dwelling horrors.",
                "tags": ["structure_type_natural_cave_large_complex", "falmer_presence_strong_major_den", "chaurus_nest_major", "dungeon_large_complex_dangerous", "morrowind_border_region_velothi_mountains", "exploration_challenge_deadly", "state_or_condition_current_lawless_area", "quest_location_investigation_rumor_potential"]
            },
            # New Rift Locations
            {
                "id": 90020,
                "name": "Autumnwatch Tower",
                "desc": "A pair of ruined Nordic towers overlooking the golden forests of the Rift, often used as a lair by dragons in ages past, now possibly home to Forsworn or bandits.", # Dragon reference made ancient
                "tags": ["structure_type_ruined_tower_nordic_pair", "scenic_vista_panoramic_autumnal_forest", "dragon_lore_ancient_site_lair_rumor", "forsworn_presence_potential_outpost", "bandit_minor_camp_potential", "dungeon_minor", "terrain_rift_forest_overlook"]
            },
            {
                "id": 90021,
                "name": "Black-Briar Lodge",
                "desc": "A secluded hunting lodge owned by the Black-Briar family, located northeast of Riften. Used for private gatherings and potentially illicit dealings.",
                "tags": ["structure_type_lodge_private_elite", "political_influence_black_briar_family_retreat", "secret_location_illicit_dealings_potential", "structure_condition_well_guarded", "terrain_rift_forest_secluded", "quest_location_thieves_guild_intrigue_potential"]
            },
            {
                "id": 90022,
                "name": "Forelhost", # Was 108
                "desc": "A massive, ancient Nordic monastery fortress on a mountaintop in The Rift, the last stronghold of the Dragon Cult. It is now sealed and haunted by its former Dragon Priest Rahgot and his draugr followers.",
                "tags": ["nordic_burial_site_major_fortress", "cultural_historical_significance_dragon_cult_lair_priest_rahgot", "undead_presence_strong_powerful_draugr", "dungeon_large_complex_mountain_top", "artifact_location_powerful_mask", "structure_condition_sealed_ruin_dangerous", "quest_location_dragon_priest_mask", "terrain_mountain_peak_rift"],
                "demographics": {"Draugr": 85, "Frost Trolls (exterior)": 10, "Dragon Priest": 1}, # Example demographics
                "travel": { "roads": [], "paths": ["Treacherous mountain path from The Rift plains"] }
            },
            {
                "id": 90023,
                "name": "Giant's Grove",
                "desc": "A small, hidden grove within the Rift's forests, where a reclusive giant tends to a painted cow. A place of unusual peace.",
                "tags": ["unique_natural_formation_hidden_grove", "neutral_encounter_giant_painted_cow", "cultural_historical_significance_local_legend_folk_tale", "secluded_nature_spot", "peaceful_area", "terrain_rift_forest_hidden"]
            },
            {
                "id": 90024,
                "name": "Ruunvald Excavation",
                "desc": "An archaeological dig site in the eastern mountains of the Rift, where Vigilants of Stendarr were investigating ancient ruins before something went terribly wrong. Now a place of danger and dark influence.", # Made pre-Dawnguard
                "tags": ["structure_type_excavation_site_ruined", "faction_vigilants_of_stendarr_tragedy_site", "magical_properties_tainted_by_dark_magic_influence", "dungeon_major_dangerous_investigation", "undead_presence_strong_potential_vigilants_or_other", "quest_location_dawnguard_potential_alt", "terrain_eastern_rift_mountains"]
            },
            {
                "id": 90025,
                "name": "Lakeside Landing",
                "desc": "A small community of fisherfolk and boatwrights on the shores of Lake Honrich in The Rift, known for their sturdy fishing boats and tales of the lake's depths.",
                "tags": ["populated_village", "settlement_minor_fishing_boatwright", "economic_activity_fishing_industry_local", "economic_activity_crafting_boatbuilding", "terrain_lake_honrich_shoreline", "rumor_source_local_legends_lake_monsters"]
            },
            {
                "id": 90026,
                "name": "Goldenleaf Farmstead",
                "desc": "A picturesque farm in The Rift, renowned for its vibrant autumn foliage and the sweet, crisp apples grown in its orchards.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops_orchard_apples", "unique_produce_goldenleaf_apples", "terrain_rift_forest_autumnal", "scenic_vista_picturesque", "settlement_minor", "peaceful_area"]
            },
            {
                "id": 90027,
                "name": "Tanglewood Den",
                "desc": "A dense, overgrown cave system hidden deep within the autumnal forests of The Rift, often serving as a den for bears, spriggans, or a reclusive alchemist.",
                "tags": ["structure_type_natural_cave_overgrown", "dungeon_minor", "monster_den_bear_potential", "monster_den_spriggan_potential", "hermit_lair_potential_alchemist", "terrain_rift_forest_deep", "alchemy_ingredient_source_rich_potential"]
            },
            {
                "id": 90028,
                "name": "Ruins of Autumn's End",
                "desc": "The crumbling remains of an old hunting lodge or minor keep in The Rift, now reclaimed by the forest. It might hold forgotten treasures or be used by local bandits.",
                "tags": ["structure_type_ruined_lodge_keep", "cultural_historical_significance_historic_site_minor", "treasure_cache_rumored_minor", "bandit_minor_camp_potential", "dungeon_minor", "terrain_rift_forest_reclaimed", "structure_condition_ruined_extensively"]
            },
            {
                "id": 90029,
                "name": "Shrine of Zenithar (Rift Forest)",
                "desc": "An outdoor shrine dedicated to Zenithar, the Divine of Work and Commerce, located along an old trade path in the Rift's forests. Merchants and craftsmen sometimes leave offerings here for prosperity.",
                "tags": ["structure_type_shrine_outdoor_structure", "religious_site_aedric", "zenithar_shrine", "economic_activity_trade_route_shrine", "magical_properties_holy_ground_aedric_potential", "terrain_rift_forest_trade_path", "cultural_historical_significance_trade_god_worship"]
            },
            {
                "id": 90030,
                "name": "Angarvunde",
                "desc": "An ancient and extensive Nordic ruin in the mountains of the Rift, deeply buried and heavily guarded by draugr. It is known for a tragic tale of betrayal and a powerful artifact sought by some.",
                "tags": ["nordic_burial_site_major", "dungeon_large_complex", "undead_presence_strong_powerful_draugr", "cultural_historical_significance_nordic_ancient_site_tragic_lore", "artifact_location_rumored_powerful", "specific_landmark_type_word_wall_location_potential", "quest_location_local_legend_investigation", "terrain_rift_mountains_buried"]
            },
            {
                "id": 90031,
                "name": "The Shadow Stone",
                "desc": "A Standing Stone hidden in the forests south of Riften, near the traditional grounds of the Nightingales. It grants the power of invisibility for a short duration, once per day.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral_stealth", "power_invisibility_temporary_daily", "terrain_rift_forest_hidden", "faction_nightingales_lore_associated_potential", "cultural_historical_significance_ancient_magical_site"]
            },
            {
                "id": 90032,
                "name": "Ruins of Bthalft",
                "desc": "Crumbling Dwemer ruins in the southern Rift, notable for an outdoor Dwemer mechanism. Legends say it's an access point to deeper, hidden Dwemer workings and perhaps the legendary Aetherium Forge.",
                "tags": ["dwemer_ruin_minor_outpost_outdoor", "ancient_technology_dwemer_mechanism_exterior", "quest_location_aetherium_forge_access_rumor", "falmer_presence_potential_nearby_ruins", "cultural_historical_significance_dwemer_ruin_site_aetherium", "terrain_southern_rift_ruins", "exploration_challenge_puzzle_potential"]
            },
            {
                "id": 90033,
                "name": "Fallowstone Cave",
                "desc": "A large cave system in the northern Rift, near Shor's Stone. It is often a den for bears or trolls and is one of the sites for Kyne's Sacred Trials.",
                "tags": ["structure_type_natural_cave_large", "monster_den_bear_troll_major", "quest_location_kyne_sacred_trials", "dungeon_major_natural", "terrain_northern_rift_wilderness", "hunting_ground_dangerous_sacred"]
            },
            {
                "id": 90034,
                "name": "Lost Tongue Overlook",
                "desc": "A ruined Nordic watchtower and ancient dragon lair high in the mountains of The Rift, south of Riften. It contains a Word Wall and is often guarded by powerful draugr or other ancient entities.",
                "tags": ["structure_type_ruined_tower_nordic", "specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "dungeon_major", "undead_presence_strong_draugr_powerful", "terrain_mountain_peak_rift_overlook", "cultural_historical_significance_dragon_lore_site_ancient"]
            },
            {
                "id": 90035,
                "name": "Geirmund's Hall",
                "desc": "An ancient Nordic ruin on an island in Lake Geir, east of Ivarstead. It is the tomb of the archmage Geirmund and is guarded by draugr and a powerful necromancer.",
                "tags": ["nordic_burial_site_major_island", "dungeon_major_tomb_archmage", "undead_presence_strong_draugr", "specific_landmark_type_necromancer_lair_guardian", "quest_location_artifact_gauldur_amulet_fragment", "cultural_historical_significance_legendary_hero_location_geirmund", "terrain_island_lake_geir", "artifact_location_powerful"]
            }
        ]
    },

    # ADDITIONAL NOTABLE LOCATIONS & DYNAMIC ADVENTURE SITES
    # (Adjusted for 4E 200 - Dragons are ancient, Dragonborn prophecy not active in current events)
    {
        "id": 100,
        "name": "High Hrothgar",
        "desc": "Perched atop the Throat of the World, High Hrothgar is the ancient and sacred monastery of the Greybeards, masters of the Way of the Voice. Pilgrims rarely brave the Seven Thousand Steps to seek their wisdom.",
        "tags": ["structure_type_monastery_ancient_sacred", "terrain_mountain_peak_settlement_remote_throat_of_world", "religious_site_aedric_kyne_sacred_voice_worship", "faction_greybeards_hq_masters_of_the_voice", "cultural_historical_significance_way_of_the_voice_masters_ancient_nordic_tradition", "unique_landmark_iconic_architecture_nordic_monastery", "travel_hub_pilgrimage_arduous_seven_thousand_steps_ivarstead", "climate_alpine_extreme_weather_blizzards", "quest_location_main_story_early_greybeards_summons", "magical_properties_ancient_wards_active_peaceful_aura"],
        "demographics": {"Nord Greybeards": 100}, # Greybeards are few and reclusive
        "travel": { "roads": [], "paths": ["Seven Thousand Steps from Ivarstead"] }
    },
    {
        "id": 101,
        "name": "Throat of the World",
        "desc": "Tamriel’s highest peak, a snow-clad titan revered by Nords and sacred to Kyne. Its summit holds ancient secrets, a Word Wall, and is the secluded domain of Paarthurnax, ancient leader of the Greybeards, though few know of his true nature or presence.",
        "tags": ["terrain_mountain_peak_summit_sacred_tamriel_highest", "religious_site_aedric_kyne_most_sacred_sky_goddess", "climate_glacial_extreme_weather_thin_air", "dragon_lore_ancient_paarthurnax_hidden_leader_greybeards", "specific_landmark_type_word_wall_location_powerful_ancient", "unique_natural_formation_highest_peak_skyrim", "faction_greybeards_leader_domain_paarthurnax", "cultural_historical_significance_creation_myth_site_potential_nordic_lore", "quest_location_main_story_late_game_paarthurnax_alduin_confrontation", "magical_properties_otherworldly_influence_time_wound_potential"],
        "demographics": {"Dragons (Paarthurnax, hidden)": 1, "Nord Spirits (conceptual)": 99},
        "travel": { "roads": [], "paths": ["Path from High Hrothgar Summit (restricted)"] }
    },
    {
        "id": 102,
        "name": "Blackreach",
        "desc": "A vast, luminous subterranean cavern system beneath Skyrim, filled with bioluminescent flora, ancient Dwemer cities, Falmer hordes, and valuable resources like Crimson Nirnroot. A dangerous and wondrous lost world.",
        "tags": ["environment_underground_realm_vast_luminous", "dwemer_ruin_major_city_extensive_subterranean_blackreach_cities", "falmer_presence_strong_territory_dominant_inhabitants", "unique_natural_formation_bioluminescent_cavern_flora_fauna", "unique_ecosystem_subterranean_flora_fauna_crimson_nirnroot", "alchemy_ingredient_source_rich_crimson_nirnroot_unique", "resource_node_geode_veins_rare_soul_gems_ores", "dungeon_large_complex_dangerous_exploration_interconnected", "mechanical_constructs_dwemer_heavy_potential_guardians_centurions", "chaurus_nest_major_potential_falmer_beasts", "cultural_historical_significance_lost_world_dwemer_falmer_history", "specific_landmark_type_blackreach_elevator_access_multiple"],
        "demographics": {"Falmer": 80, "Chaurus": 15, "Dwemer Constructs (Automated)": 5},
        "travel": { "roads": [], "paths": ["Alftand Elevator", "Mzinchaleft Elevator", "Raldbthar Elevator (hidden access points)"] }
    },
    {
        "id": 103,
        "name": "Sovngarde",
        "desc": "The revered afterlife of the Nords in Aetherius, a realm of valor, feasting, and eternal glory in the Hall of Valor. Normally accessible only to the spirits of worthy departed Nords.", # Removed TESV specific crisis access
        "tags": ["plane_of_existence_aetherius_nordic_afterlife_sovngarde", "cultural_historical_significance_nordic_paradise_valor_eternal_feasting_battle", "unique_landmark_hall_of_valor_legendary_shor_throne", "faction_nord_hero_spirits_ancient_modern", "magical_properties_otherworldly_divine_aedric_influence", "state_or_condition_current_not_normally_accessible_living_spirit_realm", "quest_location_main_story_epic_conclusion_potential_alduin_defeat", "unique_environment_otherworldly_beautiful_misty"],
        "demographics": {"Nord Hero Spirits": 100},
        "travel": { "roads": [], "paths": ["Passage via extreme spiritual/magical means (highly restricted/legendary)"] }
    },
    {
        "id": 104,
        "name": "Labyrinthian",
        "desc": "The sprawling, maze-like ruins of the ancient Nordic city of Bromjunaar, once a center of the Dragon Cult. Now haunted by draugr, ghosts, and the powerful Dragon Priest Morokei, who guards the Staff of Magnus.",
        "tags": ["nordic_burial_site_major_city_ruins_labyrinthian", "cultural_historical_significance_dragon_cult_capital_bromjunaar_ancient", "undead_presence_strong_powerful_draugr_ghosts_skeletal_dragon", "dungeon_large_complex_labyrinthine_dangerous", "cultural_historical_significance_dragon_cult_lair_priest_morokei", "quest_location_college_of_winterhold_staff_of_magnus_archmage_quest", "artifact_location_powerful_staff_of_magnus_mask_morokei", "magical_properties_arcane_nexus_powerful_ancient_magic", "terrain_hjaalmarch_foothills_ruins_snowy", "puzzle_ancient_nordic_dragon_cult_lore"],
        "demographics": {"Draugr": 70, "Skeletons": 20, "Ghosts": 9, "Dragon Priest (Morokei)": 1},
        "travel": { "roads": ["Ancient Nordic Path (decayed)"], "paths": ["Hjaalmarch Foothills (near Morthal, treacherous approach)"] }
    },
    {
        "id": 109,
        "name": "Skuldafn Temple",
        "desc": "An exceptionally remote and legendary Nordic temple complex, rumored to be hidden high in the Velothi Mountains. Ancient tales speak of it as a Dragon Cult stronghold and a gateway to Sovngarde, but its location is lost to modern knowledge, likely inaccessible.", # Corrected for 4E 200
        "tags": ["nordic_burial_site_major_temple_complex_legendary_skuldafn", "cultural_historical_significance_dragon_cult_stronghold_ancient_lost_alduin_portal", "portal_to_sovngarde_rumored_legendary_alduin_access", "structure_condition_highly_inaccessible_ruin_dragon_guarded", "magical_properties_ancient_magic_wards_powerful_dragon_cult", "terrain_velothi_mountains_remote_hidden_skyrim_morrowind_border", "dungeon_large_complex_epic_potential_outdoor_indoor", "dragon_presence_ancient_guardians_potential_alduin_lieutenants", "undead_presence_strong_draugr_priests_powerful", "quest_location_main_story_epic_final_skyrim_approach_alduin"],
        "demographics": {"Draugr (ancient guardians)": 90, "Dragon Priest (lingering spirit - potential)": 10},
        "travel": {"roads": [], "paths": ["Unknown/Magical means only (legendary)"]}
    },
    {
        "id": 110,
        "name": "Shrine of Azura",
        "desc": "A colossal statue and shrine dedicated to the Daedric Prince Azura, located high in the mountains south of Winterhold. A place of pilgrimage for her followers and where prophecies may be received.",
        "tags": ["religious_site_daedric_azura_major_shrine", "structure_type_colossal_statue_shrine_azura", "travel_hub_pilgrimage_daedric_azura_followers", "magical_properties_daedric_influence_overt_prophecy_visions", "quest_location_daedric_artifact_azuras_star", "terrain_mountain_peak_remote_winterhold_border_south", "unique_landmark_iconic_statue_visible_afar", "dunmer_culture_strong_pilgrimage_azura_worship", "faction_azura_cult_priestess_aranea_ienith"],
        "demographics": {"Priestess of Azura (Aranea Ienith)": 1, "Pilgrims (occasional)": 5, "Dunmer Followers (occasional)": 5},
        "travel": {"roads": [], "paths": ["Winding mountain path from Winterhold vicinity (difficult)"]}
    },
    {
        "id": 111,
        "name": "Shrine of Mehrunes Dagon (Mythic Dawn Museum/Shrine)", # Combined with Silus Vesuius context
        "desc": "A hidden shrine and museum dedicated to Mehrunes Dagon, Prince of Destruction, located in the mountains of The Pale, maintained by Silus Vesuius. He seeks to reforge Mehrunes' Razor.",
        "tags": ["religious_site_daedric_mehrunes_dagon_hidden_shrine_museum", "faction_mythic_dawn_remnants_shrine_museum_silus_vesuius", "quest_location_daedric_artifact_mehrunes_razor_reforging", "terrain_mountain_shrine_secret_pale_dawnstar_vicinity", "cultural_historical_significance_oblivion_crisis_related_mythic_dawn", "monster_den_dremora_summoned_potential_ritual_guardians", "artifact_location_daedric_razor_pieces", "magical_properties_daedric_influence_overt_mehrunes_dagon"],
        "demographics": {"Silus Vesuius (Curator/Cultist)": 1, "Dremora (summoned during ritual)": 100},
        "travel": {"roads": [], "paths": ["Obscure path from The Pale foothills, near Dawnstar"]}
    },
    {
        "id": 112,
        "name": "Largashbur (Shrine of Malacath)", # Name clarified
        "desc": "The Orc stronghold of Largashbur in The Rift, which also serves as a shrine to Malacath. The tribe is currently cursed by giants and seeks aid from an outsider to appease their angered god.",
        "tags": ["orc_stronghold_largashbur", "religious_site_daedric_malacath_tribal_shrine", "state_or_condition_current_cursed_by_giants_weakened_tribe", "quest_location_daedric_artifact_volendrung_cursed_tribe", "monster_infestation_giant_attacks_ongoing_curse_related", "orc_culture_strong_shamanism_malacath_code", "terrain_rift_mountains_isolated_southern", "faction_orc_tribe_largashbur_cursed", "artifact_location_daedric_volendrung_hammer", "magical_properties_daedric_influence_overt_malacath_curse"]
        "demographics": {"Orcs (cursed and weakened)": 90, "Giants (hostile)": 10},
        "travel": {"roads": [], "paths": ["Path from The Rift plains, near Forelhost"]}
    },
    {
        "id": 113,
        "name": "Sacellum of Boethiah", # Primary Name
        "desc": "A Daedric shrine high in the mountains east of Windhelm, where followers of Boethiah engage in deadly rituals of sacrifice and combat to prove their worth to the Prince of Plots.",
        "tags": ["religious_site_daedric_boethiah_major_sacellum", "faction_boethiah_cult_arena_tournament_of_souls", "ritual_site_sacrifice_combat_active_prove_worth", "quest_location_daedric_artifact_ebony_mail", "terrain_mountain_shrine_remote_eastmarch_windhelm_east", "structure_type_arena_outdoor_ritualistic_daedric", "magical_properties_daedric_influence_overt_boethiah_prince_of_plots", "artifact_location_daedric_ebony_mail", "state_or_condition_current_active_cultist_gathering_dangerous"]
        "demographics": {"Boethiah Cultists (various races)": 100},
        "travel": {"roads": [], "paths": ["Treacherous path from Eastmarch mountains, east of Traitor's Post"]}
    },
    {
        "id": 114,
        "name": "Shrine to Peryite", # More common name
        "desc": "A remote Daedric shrine in The Reach, dedicated to Peryite, the Taskmaster. His afflicted followers gather here, seeking a cure from their debilitating disease by communing with the Prince.",
        "tags": ["religious_site_daedric_peryite_remote_shrine", "faction_peryite_cult_afflicted_diseased_followers", "quest_location_daedric_artifact_spellbreaker_taskmaster_quest", "terrain_mountain_shrine_remote_reach_karthwasten_northwest", "dangerous_environment_fumes_disease_affliction", "ritual_site_alchemy_communion_incense_fumes", "magical_properties_daedric_influence_overt_peryite_taskmaster", "artifact_location_daedric_spellbreaker_shield", "unique_encounter_kesh_the_clean_khajiit_priest"]
        "demographics": {"Afflicted Followers (Bretons, Nords)": 100, "Kesh the Clean (Khajiit Priest)":1},
        "travel": {"roads": [], "paths": ["Isolated path from The Reach mountains, northwest of Karthwasten"]}
    },
    # ID 115 (Sacellum of Boethiah) is merged with ID 113.
    {
        "id": 116,
        "name": "Statue to Meridia",
        "desc": "A towering statue dedicated to the Daedric Prince Meridia, located on Mount Kilkreath in Haafingar. It is a beacon against the undead, and Meridia offers a quest to cleanse her temple of a necromancer's defilement.",
        "tags": ["religious_site_daedric_meridia_major_statue_temple", "structure_type_colossal_statue_shrine_meridia", "quest_location_daedric_artifact_dawnbreaker_cleanse_temple", "terrain_mountain_peak_kilkreath_haafingar_solitude_west", "magical_properties_holy_ground_daedric_anti_undead_light_magic", "specific_landmark_type_necromancer_lair_defiled_temple_nearby_kilkreath_ruins", "artifact_location_daedric_dawnbreaker_sword", "unique_landmark_iconic_statue_beacon_of_light", "boss_fight_necromancer_malkoran_powerful"]
        "demographics": {"Malkoran (Necromancer Spirit - Boss)": 1, "Corrupted Shades (initially)": 100},
        "travel": {"roads": [], "paths": ["Path from Dragon Bridge area, Mount Kilkreath ascent"]}
    },
    # Dawnguard/Dragonborn DLC locations adjusted for 4E 200 (mostly undiscovered or in a different state)
    {
        "id": 117,
        "name": "Forgotten Vale (Legendary Site)",
        "desc": "A legendary, hidden glacial valley in northwestern Skyrim, whispered to be an ancient sanctuary of the Snow Elves. Its existence is unconfirmed, and access is thought to be through impossibly hidden cave systems like Darkfall Cave.",
        "tags": ["terrain_hidden_valley_legendary_glacial_forgotten_vale", "cultural_historical_significance_snow_elf_sanctuary_mythical_last_refuge", "falmer_presence_ancient_origins_rumored_devolved_snow_elves", "unique_ecosystem_glacial_valley_rumored_unique_flora_fauna", "structure_type_ancient_ruins_snow_elf_lost_temples_wayshrines", "state_or_condition_current_highly_inaccessible_mythical_legendary", "dungeon_large_complex_potential_vale_exploration", "quest_location_dawnguard_potential_alt_auriels_bow", "dragon_lore_ancient_site_potential_dragons_frozen_lair", "artifact_location_powerful_auriels_bow_shield_potential"]
        "demographics": {"Unknown (Legends speak of Falmer, ancient guardians)": 100},
        "travel": {"roads": [], "paths": ["Darkfall Cave system (legendary, undiscovered)"]}
    },
    {
        "id": 118,
        "name": "Soul Cairn (Plane of Oblivion)",
        "desc": "A desolate plane of Oblivion where souls are trapped, often by necromancers or Daedric pacts. A realm of eerie landscapes, undead, and soul husks, rarely accessed by mortals.",
        "tags": ["plane_of_existence_oblivion_soul_cairn_desolate", "undead_presence_strong_realm_eternal_spirits_skeletons_wraiths", "magical_properties_soul_trap_magic_dominant_ideal_masters_control", "faction_vampire_lore_ancient_ideal_masters_soul_bargains", "necromancy_focus_soul_magic_powerful_trapped_souls", "unique_environment_otherworldly_bleak_eerie_landscapes_soul_husks", "travel_hub_portal_access_via_dark_ritual_only_vampire_castle_volkihar_potential", "quest_location_dawnguard_potential_alt_serana_valerica", "monster_den_bonemen_mistmen_wrathmen_keepers"]
        "demographics": {"Undead (various spirits, skeletons, wraiths)": 80, "Soul Husks": 10, "Ideal Masters (conceptual rulers)": 10},
        "travel": {"roads": [], "paths": ["Portal via specific, powerful necromantic ritual or vampire pact (extremely rare)"]}
    },
    {
        "id": 119,
        "name": "Castle Volkihar (Ancient Vampire Lair)",
        "desc": "An ancient, imposing fortress on a remote island off the coast of Haafingar, rumored to be the stronghold of a powerful and reclusive vampire clan, the Volkihar. Few who seek it ever return.",
        "tags": ["structure_type_castle_fortress_gothic_island_volkihar", "specific_landmark_type_vampire_ancient_lair_volkihar_clan", "magical_properties_haunted_aura_strong_ancient_vampiric_magic", "faction_vampire_volkihar_clan_rumored_powerful_lord_harkon", "terrain_island_remote_sea_of_ghosts_haafingar_coast", "dungeon_major_castle_complex_labyrinthine", "quest_location_dawnguard_potential_alt_vampire_lord_storyline", "state_or_condition_current_highly_dangerous_inaccessible_vampire_stronghold", "monster_den_vampires_death_hounds_gargoyles"]
        "demographics": {"Volkihar Vampires (ancient and powerful)": 90, "Death Hounds (spectral/undead)": 10},
        "travel": {"roads": [], "paths": ["Boat from Icewater Jetty (Haafingar north coast - perilous journey)"]}
    },
    {
        "id": 120,
        "name": "Fort Dawnguard (Ruined Fortress)",
        "desc": "A ruined fortress in a secluded canyon in The Rift, once belonging to an ancient order of vampire hunters. It is now dilapidated and forgotten, though some say its old purpose might one day be revived.",
        "tags": ["structure_type_ruined_fort_secluded_canyon_dawnguard", "faction_dawnguard_hq_ancient_ruined_potential_revival", "cultural_historical_significance_vampire_hunter_order_historic_forgotten", "state_or_condition_current_dilapidated_forgotten_awaiting_rediscovery", "quest_location_dawnguard_potential_alt_restoration_recruitment", "terrain_rift_canyon_hidden_dayspring_canyon", "dungeon_minor_ruins_potential_fort_structure", "faction_dawnguard_potential_future_base"]
        "demographics": {"Wildlife": 90, "Bandit Scavengers (potential)": 10},
        "travel": {"roads": [], "paths": ["Hidden path through Dayspring Canyon (The Rift)"]}
    },
    {
        "id": 121,
        "name": "Raven Rock (Solstheim)",
        "desc": "A struggling Dunmer settlement on the southern coast of Solstheim, originally an East Empire Company mining colony. Now under the protection of House Redoran, it faces hardship from ashfall and dwindling resources.",
        "tags": ["populated_town_solstheim_raven_rock", "dunmer_culture_strong_colonial_refugee", "economic_activity_mining_ebony_struggling_red_mountain_eruption_aftermath", "political_influence_house_redoran_protection_councilor_morvayn", "terrain_ashfall_coastal_solstheim_southern", "climate_volcanic_ashland_harsh_red_mountain_proximity", "east_empire_company_presence_historic_founding", "quest_location_dragonborn_dlc_main_potential_alt_miraak_cultists", "travel_hub_sea_windhelm_solstheim_route", "urban_issues_or_atmosphere_struggling_community_ash_blight_potential"]
        "demographics": {"Dunmer": 90, "Nords (few)": 5, "Redoran Guard": 5},
        "travel": {"roads": [], "paths": ["Ship from Windhelm Docks (Solstheim)"]}
    },
    {
        "id": 122,
        "name": "Tel Mithryn (Solstheim)",
        "desc": "The bizarre mushroom tower home of the eccentric but powerful Telvanni wizard, Master Neloth, located in the ashy wastes of Solstheim. A place of strange magical experiments.",
        "tags": ["structure_type_wizard_tower_mushroom_telvanni_tel_mithryn", "faction_telvanni_mage_neloth_residence_master_wizard", "unique_architecture_magical_mushroom_grown_structure", "magical_properties_arcane_nexus_powerful_experimental_telvanni_magic", "terrain_ashfall_wastes_solstheim_southeastern", "monster_den_ash_spawn_nearby_guardians_experiments", "quest_location_dragonborn_dlc_neloth_quests_potential_alt_hermaeus_mora_black_books", "alchemy_ingredient_source_rich_unique_mushroom_parts_solstheim_flora", "scholar_retreat_rumor_eccentric_wizard_neloth"]
        "demographics": {"Telvanni Wizard (Neloth)": 1, "Apprentice (Talvas Fathryon)": 1, "Ash Spawn (surrounding area)": 98},
        "travel": {"roads": [], "paths": ["Path across Solstheim ashlands (dangerous)"]}
    },
    {
        "id": 123,
        "name": "Apocrypha (Plane of Hermaeus Mora)",
        "desc": "The Daedric plane of Oblivion belonging to Hermaeus Mora, Prince of Knowledge and Fate. A vast, endless library filled with forbidden lore, writhing tentacles, and ghostly Seekers. Access is only through forbidden Black Books.",
        "tags": ["plane_of_existence_oblivion_hermaeus_mora_apocrypha", "unique_environment_endless_library_eldritch_shifting_corridors", "forbidden_knowledge_dangerous_repository_countless_tomes", "monster_den_seekers_lurkers_tentacles_guardians_of_lore", "magical_properties_daedric_influence_overt_knowledge_fate_hermaeus_mora", "travel_hub_portal_access_via_black_books_only_solstheim_tamriel", "quest_location_dragonborn_dlc_main_potential_alt_miraak_confrontation", "artifact_location_black_books_forbidden_powers", "unique_landmark_otherworldly_plane_apocrypha"]
        "demographics": {"Seekers (guardians of lore)": 70, "Lurkers (behemoths)": 30},
        "travel": {"roads": [], "paths": ["Black Books (portals from Solstheim and Tamriel, rare and hidden)"]}
    },
    # Adding a few more brand new unique locations for 4E 200
    {
        "id": 124,
        "name": "Hall of the Vigilant (Pre-Destruction)",
        "desc": "A fortified lodge near The Pale, serving as a headquarters for the Vigilants of Stendarr in Skyrim. From here, they coordinate their hunts against Daedra, vampires, and other abominations.",
        "tags": ["structure_type_lodge_fortified_vigilant_hq", "faction_vigilants_of_stendarr_hq_skyrim_pre_destruction", "religious_military_order_anti_daedra_vampire_witch", "stendarr_worship_center_vigilant_order", "quest_location_vigilant_tasks_potential_bounties_investigations", "terrain_pale_border_mountains_near_dawnstar", "state_or_condition_current_functional_active_pre_vampire_attack", "quest_location_dawnguard_potential_alt_start_point_destruction_event"]
        "demographics": {"Vigilants of Stendarr": 100},
        "travel": {"roads": [], "paths": ["Path from Whiterun-Pale border mountains"]}
    },
    {
        "id": 125,
        "name": "Sleeping Giant's Thumb",
        "desc": "A towering rock formation in the plains of Whiterun Hold resembling a colossal thumb, considered a sacred landmark by some local Nord tribes and giants.",
        "tags": ["unique_natural_formation_rock_thumb_colossal", "cultural_historical_significance_local_legend_sacred_site_nordic_giant", "specific_landmark_type_giant_camp_reverence_site_potential_nearby", "terrain_plains_whiterun_hold_landmark_prominent", "folklore_location_nordic_giant_mythology", "scenic_vista_unique_plains_landmark", "exploration_point_natural_wonder"]
        "demographics": {"Giants (nearby)": 20, "Nord Hunters/Pilgrims (occasional)": 80},
        "travel": {"roads": [], "paths": ["Open plains of Whiterun Hold"]}
    },
    {
        "id": 126,
        "name": "The Karthspire Forsworn Camp", # Distinct from Karthspire mountain itself
        "desc": "A large and heavily fortified Forsworn encampment at the foot of the Karthspire mountain, fiercely guarding the only known path leading towards the rumored Sky Haven Temple.",
        "tags": ["structure_type_fortified_camp_forsworn_major_karthspire_base", "faction_forsworn_stronghold_karthspire_base_guardians", "guardian_force_sky_haven_temple_access_fierce", "dangerous_terrain_approach_fortified_narrow_paths", "quest_location_main_story_access_sky_haven_temple", "terrain_mountain_base_reach_karthspire", "state_or_condition_current_forsworn_controlled_area_heavy_fortified", "hagraven_presence_potential_leaders_ritualists"]
        "demographics": {"Forsworn Warriors": 80, "Forsworn Briarhearts": 10, "Hagravens": 10},
        "travel": {"roads": [], "paths": ["Path from Old Hroldan area"]}
    },
    {
        "id": 127,
        "name": "Dunmeth Pass Watchtower (Skyrim Side)",
        "desc": "A sturdy Imperial watchtower on the Skyrim side of Dunmeth Pass, guarding the treacherous route to Morrowind. Manned by a small Imperial garrison.",
        "tags": ["structure_type_watchtower_fortified_border_imperial", "military_presence_imperial_legion_garrison_small", "morrowind_border_region_dunmeth_pass_skyrim_side_watch", "strategic_location_border_defense_monitoring_morrowind", "isolated_location_outpost_remote", "travel_route_major_dangerous_monitoring_dunmeth_pass", "climate_alpine_harsh_pass_conditions"]
        "demographics": {"Imperial Soldiers": 100},
        "travel": {"roads": ["Dunmeth Pass Road"], "paths": []}
    },
    {
        "id": 128,
        "name": "Guldun Rock",
        "desc": "A large, isolated rock formation in the volcanic tundra of Eastmarch, riddled with caves that are often used as a den by trolls or other dangerous creatures. Sometimes bandits try to establish a hideout here.",
        "tags": ["unique_natural_formation_rock_volcanic_caves_guldun", "structure_type_natural_cave_system_riddled", "monster_den_troll_major_potential_cave_trolls", "bandit_minor_camp_potential_hideout_temporary", "terrain_volcanic_tundra_eastmarch_wilderness_isolated", "dungeon_minor_complex_potential_cave_network", "exploration_challenge_dangerous_creatures_terrain", "alchemy_ingredient_source_rich_troll_fat_minerals_potential"]
        "demographics": {"Trolls/Creatures": 80, "Bandits (occasional)": 20},
        "travel": {"roads": [], "paths": ["Path from Kynesgrove vicinity"]}
    }
]
class Location:
    def __init__(self, name, description, is_dark=False):
        self.name = name
        self.description = description
        self.is_dark = is_dark
        self.items = []
        self.npcs = []
        self.exits = {}

    def enter(self, player):
        print(f"You enter {self.name}.")
        print(self.description)
        self.display_items()
        self.display_npcs()

        if self.is_dark:
            # player.has_lit_torch() now updates visibility internally.
            # We just check the result for the message.
            if player.has_lit_torch(): # This call updates player.visibility
                print("The torch illuminates the area, allowing you to see clearly.")
                # player.visibility is already set by has_lit_torch()
            else:
                print("It's too dark to see anything! You stumble around blindly.")
                # player.visibility is already set by has_lit_torch()
        else:
            # If the location is not dark, ensure player visibility is normal.
            # This might be redundant if has_lit_torch() is always called or default visibility is 10.
            # However, explicitly setting it here ensures correctness if the location itself isn't dark.
            player.visibility = 10 # Default visibility for non-dark areas

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_items(self):
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item}")

    def add_npc(self, npc):
        self.npcs.append(npc)

    def remove_npc(self, npc):
        if npc in self.npcs:
            self.npcs.remove(npc)

    def display_npcs(self):
        if self.npcs:
            print("You see the following people:")
            for npc in self.npcs:
                print(f"- {npc.name}")

    def add_exit(self, direction, location):
        self.exits[direction] = location

    def get_exit(self, direction):
        return self.exits.get(direction)