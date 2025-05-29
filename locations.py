LOCATIONS = [
    # WHITERUN HOLD
    {
        "id": 1,
        "name": "Whiterun Hold",
        "desc": "The fertile heartland of Skyrim, marked by golden plains and the bustling city of Whiterun. A center of commerce, Imperial influence, and ancient Nordic tradition.",
        "tags": ["hold", "climate_temperate", "terrain_plains", "environment_rural", "economic_activity_farming_crops", "economic_activity_farming_livestock", "economic_activity_trade_hub_regional", "nordic_culture_local", "imperial_influence_moderate", "politically_stable", "central_location"],
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
                "tags": ["populated_city", "city_affiliation_whiterun_hold_capital", "economic_activity_trade_hub_major", "settlement_features_market_square", "settlement_features_jarls_longhouse", "settlement_features_companions_guild_hall", "settlement_features_temple_divines", "imperial_influence_strong", "nordic_settlement_ancient", "structure_type_fortified_city_wall", "cultural_historical_significance_ysgramor_related_site", "urban_issues_or_atmosphere_bustling_trade_atmosphere", "environment_urban"],
                "sub_locations": [
                    {
                        "id": 1001,
                        "name": "Dragonsreach",
                        "desc": "The imposing keep of the Jarl, an iconic symbol of Nord authority and power, once used to imprison the dragon Numinex in ages past.",
                        "tags": ["structure_type_fortified_keep", "settlement_features_jarls_longhouse", "cultural_historical_significance_historic_site", "government_local", "unique_landmark_iconic", "dragon_lore_ancient_site", "interior_large", "ruling_class_residence"],
                    },
                    {
                        "id": 1002,
                        "name": "Jorrvaskr",
                        "desc": "The ancient mead hall and headquarters of the Companions, where warriors forge bonds in battle and honor tradition.",
                        "tags": ["structure_type_guild_hall_building", "settlement_features_companions_guild_hall", "cultural_historical_significance_historic_site", "warrior_culture_strong", "nordic_settlement_ancient", "interior_large", "guild_hq_prominent"]
                    },
                    {
                        "id": 1003,
                        "name": "The Bannered Mare",
                        "desc": "A lively tavern where travelers and locals share stories over hearty ale, a central hub of Whiterun's social life.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "interior_medium", "lodging_available"]
                    },
                    {
                        "id": 1004,
                        "name": "Warmaiden's",
                        "desc": "A masterful smithy known for crafting sturdy weapons and armor, run by Adrianne Avenicci and Ulfberth War-Bear.",
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "item_type_weapon_vendor", "item_type_armor_vendor", "interior_small", "crafting_tools"]
                    },
                    {
                        "id": 1005,
                        "name": "Arcadia's Cauldron",
                        "desc": "A cozy apothecary brimming with ingredients and potions, run by the alchemist Arcadia.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "economic_activity_alchemy_ingredient_source_rich", "item_type_potion_vendor", "item_type_ingredient_vendor", "interior_small", "alchemy_equipment"]
                    },
                    {
                        "id": 1006,
                        "name": "Temple of Kynareth",
                        "desc": "A serene temple devoted to the wind and healing, centered around the ancient Gildergreen tree and frequented by worshippers.",
                        "tags": ["structure_type_temple_building", "settlement_features_temple_specific_god", "religious_site_aedric", "magical_properties_holy_ground_aedric", "healing_services", "kynareth_shrine", "unique_landmark_iconic"]
                    },
                    {
                        "id": 1007,
                        "name": "Plains District Market",
                        "desc": "Bustling stalls offering regional produce, crafts, and curiosities, the commercial heart of Whiterun.",
                        "tags": ["settlement_features_market_square", "economic_activity_trade_hub_local", "social_hub_popular"]
                    },
                    {
                        "id": 1008,
                        "name": "The Drunken Huntsman",
                        "desc": "A tavern popular with hunters and adventurers, known for its rustic charm and owned by Elrindir.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "hunter_gathering_spot", "bosmer_influence_minor"]
                    },
                    {
                        "id": 1009,
                        "name": "Belethor's General Goods",
                        "desc": "A shop stocking a wide variety of items, where Belethor claims everything is for sale... if the price is right.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "eccentric_merchant_owner"]
                    },
                    {
                        "id": 1010,
                        "name": "Hall of the Dead",
                        "desc": "A solemn place beneath the Temple of Kynareth where the Nords of Whiterun honor their ancestors and inter their dead.",
                        "tags": ["structure_type_catacombs_structure", "religious_site_aedric", "nordic_burial_site_major", "arkay_presence", "undead_presence_rumored_low"]
                    },
                    {
                        "id": 1011,
                        "name": "Carlotta Valentia's House",
                        "desc": "The home of Carlotta Valentia, a food vendor in the market, and her daughter Mila.",
                        "tags": ["structure_type_residence", "commoner_dwelling"]
                    },
                    {
                        "id": 1012,
                        "name": "House Gray-Mane",
                        "desc": "A prominent and respected Nord family in Whiterun, known for their traditional values and quiet concerns about Imperial policies.",
                        "tags": ["structure_type_residence", "noble_estate_district", "nordic_culture_strong", "political_tension_high", "stormcloak_sympathizers_potential"]
                    },
                    {
                        "id": 1013,
                        "name": "House Battle-Born",
                        "desc": "A wealthy and influential Nord family in Whiterun, strong supporters of the Empire and Imperial traditions.",
                        "tags": ["structure_type_residence", "noble_estate_district", "imperial_influence_strong", "political_tension_high"]
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
                "tags": ["populated_village", "settlement_minor", "economic_activity_logging_timber", "terrain_river_delta", "climate_temperate", "forested_area", "travel_hub_minor"],
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
                        "tags": ["structure_type_shop_building", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "crafting_tools", "imperial_sympathizers_potential"]
                    },
                    {
                        "id": 1104,
                        "name": "Faendal's House",
                        "desc": "The home of Faendal, a Bosmer archer and lumberjack in Riverwood.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "wood_elf_architecture_influence_minor"]
                    },
                    {
                        "id": 1105,
                        "name": "Sven and Hilde's House",
                        "desc": "The home of Sven, a local bard, and his mother Hilde.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "bard_dwelling"]
                    }
                ]
            },
            {
                "id": 12,
                "name": "Rorikstead",
                "desc": "A fertile farming village that supplies Whiterun with produce. Despite its prosperity, some whisper of strange pacts or hidden influences behind its unusual success.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_farming_crops", "terrain_plains", "climate_temperate", "magical_properties_enchanted_neutral", "daedric_influence_subtle_rumor"],
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
                "tags": ["structure_type_meadery_building", "economic_activity_brewing_mead_ale", "shop_specialty_goods", "quest_location_thieves_guild", "sabotage_target_potential"]
            },
            {
                "id": 14,
                "name": "Western Watchtower",
                "desc": "An old, ruined guard tower on the outskirts of Whiterun, fallen into disrepair over the years. It stands as a lonely sentinel over the plains, a relic of past conflicts.",
                "tags": ["structure_type_ruined_tower", "cultural_historical_significance_historic_site", "dragon_sighting_recent_rumor", "state_or_condition_current_recently_attacked_recovering", "battlefield_minor_historic"]
            },
            {
                "id": 15,
                "name": "Bleak Falls Barrow",
                "desc": "An ancient Nordic tomb high among the mountains overlooking Riverwood, crawling with draugr and secrets of old, including a Word Wall.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "specific_landmark_type_word_wall_location", "quest_location_main_story_early", "puzzle_dragon_claw", "cultural_historical_significance_nordic_ancient_site"]
            },
            {
                "id": 16,
                "name": "Silent Moons Camp",
                "desc": "A clandestine bandit camp hidden in the wilderness north-west of Whiterun, known for its lunar-enchanted weapons.",
                "tags": ["bandit_minor_camp", "structure_type_ruined_settlement", "dungeon_minor", "magical_properties_enchanted_neutral", "specific_landmark_type_lunar_forge", "weapon_enchanting_site"]
            },
            {
                "id": 17,
                "name": "Lund's Hut",
                "desc": "A small, isolated hut north of Rorikstead, once home to the unfortunate Lund.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_abandoned", "wilderness", "tragedy_site_minor", "ghost_encounter_potential"]
            },
            {
                "id": 18,
                "name": "Gjukar's Monument",
                "desc": "A stone monument south of Rorikstead, marking the site of an ancient battle and the resting place of the warrior Gjukar.",
                "tags": ["structure_type_monument_historic_site", "cultural_historical_significance_battlefield_historic", "ghost_encounter_potential", "nordic_burial_site_major_nearby"]
            },
            {
                "id": 19,
                "name": "Secunda's Kiss",
                "desc": "A giant's camp located west of Whiterun, named for the nearby moon Secunda.",
                "tags": ["specific_landmark_type_giant_camp_established", "wilderness", "terrain_plains", "mammoth_herd_grazing"]
            },
            {
                "id": 10001,
                "name": "Sleeping Tree Camp",
                "desc": "A giant's camp west of Whiterun, notable for a strange, glowing tree and the potent sap it produces.",
                "tags": ["specific_landmark_type_giant_camp_established", "unique_natural_formation", "alchemy_ingredient_source_rich", "magical_properties_enchanted_neutral", "mystery_local"]
            },
            {
                "id": 10002,
                "name": "Swindler's Den",
                "desc": "A cave system west of Whiterun, serving as a hideout for bandits and perhaps some Alik'r warriors if circumstances align.",
                "tags": ["structure_type_natural_cave", "bandit_main_stronghold", "dungeon_multi_level", "quest_location_main_story_early", "alikr_warriors_presence_potential"]
            },
            {
                "id": 10003,
                "name": "White River Watch",
                "desc": "A small cave east of Honningbrew Meadery, inhabited by bandits led by Hajvarr Iron-Hand.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "overlook_strategic"]
            },
            {
                "id": 10004,
                "name": "Halted Stream Camp",
                "desc": "A bandit-occupied iron mine north of Whiterun, containing a spell tome for Transmute Ore.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "bandit_controlled_area", "dungeon_minor", "magical_properties_arcane_focus", "spell_tome_location"]
            },
            # New Whiterun Hold Locations
            {
                "id": 10005,
                "name": "Chillfurrow Farm",
                "desc": "A prosperous farm run by Wilmuth and his family, just outside Whiterun's walls, known for its diverse crops.",
                "tags": ["structure_type_farmstead", "structure_type_residence", "economic_activity_farming_crops", "economic_activity_farming_livestock", "settlement_minor", "whiterun_plains"]
            },
            {
                "id": 10006,
                "name": "Pelagia Farm",
                "desc": "The farmstead of Severio Pelagia, located near Whiterun, contributing to the city's food supply.",
                "tags": ["structure_type_farmstead", "structure_type_residence", "economic_activity_farming_crops", "settlement_minor", "whiterun_plains"]
            },
            {
                "id": 10007,
                "name": "Valtheim Towers",
                "desc": "A pair of fortified towers spanning the White River east of Whiterun, often occupied by bandits demanding tolls.",
                "tags": ["structure_type_tower_structure", "structure_condition_ruined_extensively", "bandit_minor_camp", "terrain_river_delta", "dungeon_minor", "strategic_lookout_decayed", "toll_road_illegal"]
            },
            {
                "id": 10008,
                "name": "Greenspring Hollow",
                "desc": "A small, secluded cave known for its natural spring and unique mosses, sometimes used as a hunter's shelter or a troll's den.",
                "tags": ["structure_type_natural_cave", "unique_natural_formation", "alchemy_ingredient_source_rich", "monster_den_troll_potential", "wilderness", "secluded_nature_spot"]
            },
            {
                "id": 10009,
                "name": "Redoran's Retreat",
                "desc": "A small, damp cave west of Whiterun, often used as a hideout by a lone bandit or a small group of outcasts.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "wilderness", "terrain_hilly"]
            },
            {
                "id": 10010,
                "name": "Guldun Rock Overlook",
                "desc": "A rocky outcrop near the Whiterun plains, offering a strategic view. Sometimes used by hunters as a lookout or temporarily inhabited by wildlife.",
                "tags": ["terrain_hilly", "wilderness", "scenic_vista_panoramic", "hunter_gathering_spot", "animal_den_wolf_potential"]
            },
            {
                "id": 10011,
                "name": "Dustman's Cairn",
                "desc": "An ancient Nordic barrow west of Whiterun, a significant site for the Companions and haunted by draugr.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "companions_guild_hall_related", "cultural_historical_significance_nordic_ancient_site", "ysgramor_related_site_potential", "silver_hand_lair_potential"]
            },
            {
                "id": 10012,
                "name": "Fellglow Keep",
                "desc": "A ruined fort east of Whiterun, now overrun by necromancers and their experiments. It holds forbidden knowledge and dangerous foes.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_necromancer_tower_or_lair", "magical_properties_tainted_by_dark_magic", "dungeon_major", "college_of_winterhold_main_related", "forbidden_knowledge_dangerous", "undead_experiments"]
            },
            {
                "id": 10013,
                "name": "Battle-Born Farm",
                "desc": "A prosperous farm outside Whiterun, owned and operated by the Battle-Born family, known for its crops and livestock.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "economic_activity_farming_livestock", "noble_estate_district_outskirts", "imperial_influence_strong", "political_family_imperial"]
            },
            {
                "id": 10014,
                "name": "Gray-Mane Farm",
                "desc": "A traditional Nord farmstead near Whiterun, belonging to the Gray-Mane family, reflecting their more rustic and independent values.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "economic_activity_farming_livestock", "nordic_culture_strong", "whiterun_plains", "political_family_stormcloak_sympathizers"]
            },
            {
                "id": 10015,
                "name": "Whiterun Pass Cave",
                "desc": "A small cave system that cuts through the hills near Whiterun, sometimes used by travelers as a shortcut or by creatures as a den.",
                "tags": ["structure_type_natural_cave", "terrain_mountain_pass", "monster_den_bear_potential", "travel_route_alternative_dangerous"]
            },
            {
                "id": 10016,
                "name": "Granite Hill Redoubt",
                "desc": "A fortified bandit encampment built into the rocky hills west of Whiterun, a source of trouble for local farms and travelers.",
                "tags": ["bandit_main_stronghold", "structure_type_fortified_keep", "dungeon_major", "state_or_condition_current_bandit_controlled_area", "terrain_hilly", "economic_activity_mining_gems_potential"]
            },
            {
                "id": 10017,
                "name": "Lone Hunter's Shack",
                "desc": "A small, isolated shack in the plains of Whiterun Hold, home to a reclusive hunter or trapper.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_weathered", "wilderness", "hunter_gathering_spot", "hermit_lair_potential", "terrain_plains"]
            },
            {
                "id": 10018,
                "name": "Shrine of Talos (Wilderness - Whiterun)",
                "desc": "A small, weathered outdoor shrine dedicated to Talos, hidden among the rocks and trees of Whiterun's plains, a place of quiet worship for loyal Nords.",
                "tags": ["structure_type_shrine_outdoor_structure", "religious_site_aedric", "talos_worship_banned", "nordic_culture_strong", "secluded_nature_spot", "magical_properties_holy_ground_aedric"]
            },
            {
                "id": 10019,
                "name": "Tundra Homestead",
                "desc": "A modest farmstead with a sturdy house on the plains east of Whiterun, offering a peaceful life for those who can work the land. (Potential player home)",
                "tags": ["structure_type_farmstead", "player_home_available", "economic_activity_farming_crops", "terrain_plains", "settlement_minor", "peaceful_area"]
            },
            {
                "id": 10020,
                "name": "North Skybound Watch",
                "desc": "A ruined Nordic watchtower and barrow complex on a cliff overlooking the northern plains of Whiterun Hold, containing an ancient Word Wall.",
                "tags": ["structure_type_ruined_tower", "nordic_burial_site_major", "specific_landmark_type_word_wall_location", "dungeon_major", "undead_presence_strong", "draugr_heavy", "terrain_cliffside", "dragon_lore_ancient_site"]
            },
            {
                "id": 10021,
                "name": "Whitewatch Mill",
                "desc": "A small, independent lumber mill on the plains of Whiterun Hold, supplying timber for local construction and repairs.",
                "tags": ["structure_type_lumber_mill_site", "economic_activity_logging_timber", "settlement_minor", "terrain_plains"]
            },
            {
                "id": 10022,
                "name": "Honey-Hand Farm",
                "desc": "A quaint farmstead and apiary known for its uniquely flavored honey, run by a reclusive family.",
                "tags": ["structure_type_farmstead", "structure_type_apiary_location", "economic_activity_farming_crops", "unique_produce_honey", "settlement_minor", "isolated_location"]
            },
            {
                "id": 10023,
                "name": "Whispering Creek Cave",
                "desc": "A small, damp cave system carved by an underground creek, often home to mudcrabs or other cave dwellers. Sometimes used by bandits as a temporary hideout.",
                "tags": ["structure_type_natural_cave", "dungeon_minor", "monster_den_mudcrab", "bandit_minor_camp_potential", "terrain_river_delta_nearby"]
            },
            {
                "id": 10024,
                "name": "Old Kynesgrove Road Ruin",
                "desc": "The crumbling stone remnants of an ancient watchpost or small shrine along a disused stretch of road near the path to Kynesgrove. It offers little shelter but hints at older conflicts.",
                "tags": ["structure_type_ruined_shrine", "cultural_historical_significance_nordic_ancient_site", "structure_condition_ruined_extensively", "bandit_minor_camp_potential", "roadside_encounter_point"]
            },
            {
                "id": 10025,
                "name": "Broken Fang Cave",
                "desc": "A dark, fetid cave that has become a den for a small coven of vampires or their thralls, preying on unwary travelers on the plains.",
                "tags": ["structure_type_natural_cave", "dungeon_minor", "specific_landmark_type_vampire_coven_minor", "undead_presence_strong", "wilderness", "magical_properties_tainted_by_dark_magic"]
            },
            {
                "id": 10026,
                "name": "Shrine of Stendarr (Whiterun Plains)",
                "desc": "A modest, weathered shrine to Stendarr, the God of Mercy and Justice, offering a place for quiet contemplation and prayer on the open plains.",
                "tags": ["structure_type_shrine_outdoor_structure", "religious_site_aedric", "stendarr_shrine", "magical_properties_holy_ground_aedric", "travel_route_marker", "vigilant_of_stendarr_outpost_potential_minor"]
            },
            {
                "id": 10027,
                "name": "The Ritual Stone",
                "desc": "An ancient Standing Stone east of Whiterun, near the road to Windhelm. It grants the power to reanimate nearby corpses to fight for the activator, once per day.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_arcane_nexus", "necromancy_focus", "cultural_historical_significance_ancient_magical_site", "terrain_plains"]
            },
            {
                "id": 10028,
                "name": "Gallows Hall",
                "desc": "A secluded and ominous ruin near the road west of Windhelm, but technically within Whiterun's old borders. It is rumored to be a former place of execution now haunted and possibly used by necromancers.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_necromancer_tower_or_lair", "dungeon_minor", "cultural_historical_significance_historic_site", "magical_properties_tainted_by_dark_magic", "undead_presence_strong", "haunted_aura"]
            },
            {
                "id": 10029,
                "name": "Shimmermist Grotto",
                "desc": "A damp cave system northeast of Whiterun, containing both Falmer inhabitants and ancient Dwemer ruins deep within. Known for its glowing mushrooms.",
                "tags": ["structure_type_natural_cave", "dwemer_outpost_minor", "falmer_presence_strong", "dungeon_major", "unique_natural_formation", "alchemy_ingredient_source_rich", "chaurus_nest_potential", "bioluminescent_flora"]
            },
            {
                "id": 10030,
                "name": "Hamvir's Rest",
                "desc": "An ancient, desecrated Nordic graveyard and small cairn north-west of Whiterun, now haunted by skeletons and a necromancer.",
                "tags": ["nordic_burial_site_major", "dungeon_minor", "undead_presence_strong", "specific_landmark_type_necromancer_hideout", "structure_condition_desecrated", "ghost_encounter_potential"]
            }
        ]
    },

    # THE PALE
    {
        "id": 2,
        "name": "The Pale",
        "desc": "A frozen hold of bleak beauty, stretching from snow-tipped plains to the Sea of Ghosts. Harsh and unforgiving, known for its mining town of Dawnstar and dangerous wildlife. Strong Stormcloak sentiment prevails here.",
        "tags": ["hold", "climate_arctic", "terrain_ice_field", "terrain_tundra_plains", "environment_coastal", "economic_activity_mining_quicksilver", "economic_activity_mining_iron", "nordic_culture_strong", "stormcloak_leaning", "state_or_condition_current_isolated_and_forgotten", "dangerous_wildlife"],
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
                "tags": ["populated_town", "settlement_features_docks_harbor", "city_affiliation_dawnstar_town", "state_or_condition_current_isolated_and_forgotten", "economic_activity_mining_quicksilver", "economic_activity_fishing_industry_local", "urban_issues_or_atmosphere_haunted_rumors_strong", "daedric_influence_subtle_rumor", "settlement_features_jarls_longhouse", "climate_arctic", "environment_coastal"],
                "sub_locations": [
                    {
                        "id": 2001,
                        "name": "Windpeak Inn",
                        "desc": "The cozy inn of Dawnstar, offering respite from the icy winds and a place for locals to gather and discuss the unsettling dreams.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available", "urban_issues_or_atmosphere_fear_and_superstition"]
                    },
                    {
                        "id": 2002,
                        "name": "Quicksilver Mine",
                        "desc": "A productive quicksilver mine that is vital to Dawnstar's economy, though some miners report strange occurrences.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_quicksilver", "economic_activity_trade_hub_local", "urban_issues_or_atmosphere_haunted_rumors_strong"]
                    },
                    {
                        "id": 2003,
                        "name": "The Mortar and Pestle",
                        "desc": "Frida's alchemy shop, where local brews and potions are concocted. Frida may seek rare ingredients.",
                        "tags": ["structure_type_shop_building", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "quest_giver_potential"]
                    },
                    {
                        "id": 2004,
                        "name": "The White Hall",
                        "desc": "The seat of Dawnstar's Jarl, Skald the Elder, a staunch supporter of Ulfric Stormcloak.",
                        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local", "stormcloak_presence_strong", "political_family_stormcloak"]
                    },
                    {
                        "id": 2005,
                        "name": "Rustleif's House and Smithy",
                        "desc": "The home and workshop of Rustleif, Dawnstar's blacksmith, who dreams of returning to his homeland.",
                        "tags": ["structure_type_shop_building", "structure_type_residence", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "crafting_tools"]
                    },
                    {
                        "id": 2006,
                        "name": "Dawnstar Sanctuary",
                        "desc": "A forgotten and ruined sanctuary of the Dark Brotherhood, hidden near Dawnstar. Its secrets lie buried in snow and shadow.",
                        "tags": ["structure_type_ruined_shrine", "specific_landmark_type_assassin_guild_hq_abandoned", "dungeon_minor", "secret_location", "magical_properties_tainted_by_dark_magic", "structure_condition_collapsed"]
                    }
                ]
            },
            {
                "id": 21,
                "name": "Nightcaller Temple",
                "desc": "An eerie, abandoned temple on a clifftop overlooking Dawnstar. It is sealed, but dark whispers and nightmares emanate from it, hinting at the Daedric Prince Vaermina's influence.",
                "tags": ["structure_type_temple_building", "structure_condition_ruined_extensively", "magical_properties_daedric_influence_overt", "dungeon_major", "quest_location_daedric_vaermina", "urban_issues_or_atmosphere_haunted_rumors_strong", "specific_landmark_type_daedric_shrine_prominent"]
            },
            {
                "id": 22,
                "name": "Iron-Breaker Mine",
                "desc": "An iron mine located just outside Dawnstar, contributing to the town's resources.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "resource_node", "dawnstar_outskirts"]
            },
            {
                "id": 23,
                "name": "Wreck of the Brinehammer",
                "desc": "The ghostly remains of a long-forgotten shipwreck scattered along the storm-battered coast south of Dawnstar. Rumored to hold lost treasures and spectral guardians.",
                "tags": ["structure_type_shipwreck_site", "structure_condition_ruined_extensively", "dungeon_minor", "environment_coastal", "undead_presence_rumored_strong", "treasure_cache_rumored"]
            },
            {
                "id": 24,
                "name": "Frostflow Lighthouse",
                "desc": "A solitary lighthouse west of Dawnstar. Its light has recently gone out, and chilling screams were heard from within. A dark mystery involving Falmer awaits discovery.",
                "tags": ["structure_type_lighthouse_structure", "structure_condition_abandoned", "dungeon_major", "falmer_presence_strong", "quest_location_investigation", "tragedy_site_family", "chaurus_nest_potential"]
            },
            {
                "id": 25,
                "name": "Loreius Farm",
                "desc": "A small farmstead south of Dawnstar, owned by Vantus Loreius, often struggling against the harsh climate.",
                "tags": ["structure_type_farmstead", "structure_type_residence", "economic_activity_farming_crops", "state_or_condition_current_isolated_and_forgotten", "climate_arctic_edge"]
            },
            {
                "id": 26,
                "name": "Nightgate Inn",
                "desc": "An isolated inn located at a pass on the road between The Pale and Eastmarch, a lonely refuge for travelers.",
                "tags": ["structure_type_inn_building", "settlement_features_tavern", "state_or_condition_current_isolated_and_forgotten", "travel_route_marker", "lodging_available", "food_drink_vendor", "rumor_source_travelers"]
            },
            {
                "id": 27,
                "name": "Red Road Pass",
                "desc": "A bandit-infested pass through the mountains in the southern part of The Pale, dangerous for unwary travelers.",
                "tags": ["terrain_mountain_pass", "bandit_main_stronghold", "dungeon_major", "travel_route_alternative_dangerous", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 28,
                "name": "Shearpoint",
                "desc": "A mountain peak in The Pale, home to an ancient dragon lair, a Word Wall, and the tomb of the Dragon Priest Krosis.",
                "tags": ["specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "cultural_historical_significance_dragon_cult_lair_priest", "terrain_mountain_peak", "dungeon_major", "undead_presence_strong", "dragon_priest_krosis"]
            },
            {
                "id": 29,
                "name": "Shrouded Grove",
                "desc": "A small, hidden grove in The Pale, sometimes a site for unusual encounters, minor Daedric worship, or hidden alchemical ingredients.",
                "tags": ["environment_wilderness", "terrain_forest", "magical_properties_enchanted_neutral", "ritual_site_minor_potential", "alchemy_ingredient_source_rich", "secluded_nature_spot"]
            },
            {
                "id": 20001,
                "name": "Silverdrift Lair",
                "desc": "A Nordic ruin west of Nightgate Inn, overrun by draugr and ancient guardians.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "cultural_historical_significance_nordic_ancient_site"]
            },
            {
                "id": 20002,
                "name": "Weynon Stones",
                "desc": "A small ruin southeast of Dawnstar, a circle of ancient stones that hum with faint magical energy, sometimes attracting bandits or mages.",
                "tags": ["structure_type_standing_stone_circle", "cultural_historical_significance_ancient_magical_site", "magical_properties_arcane_nexus_minor", "bandit_minor_camp_potential", "terrain_tundra_plains"]
            },
            {
                "id": 20003,
                "name": "Fort Dunstad",
                "desc": "A large fort in The Pale, strategically important. Currently garrisoned by Imperial soldiers, but its loyalty could shift with the rising political tensions.",
                "tags": ["structure_type_fortified_keep", "military_presence", "imperial_influence_strong", "dungeon_major", "state_or_condition_current_contested_by_factions_potential", "civil_war_quest_historic_site_potential"]
            },
            # New Pale Locations
            {
                "id": 20004,
                "name": "Windward Ruins",
                "desc": "Crumbling Nordic ruins on a windswept hill overlooking the Sea of Ghosts, rumored to be haunted by sailors lost to the ice.",
                "tags": ["structure_type_ruined_tower", "nordic_burial_site_minor", "environment_coastal", "structure_condition_ruined_extensively", "magical_properties_haunted_aura", "undead_presence_skeletons", "dungeon_minor"]
            },
            {
                "id": 20005,
                "name": "Pale Pass",
                "desc": "A treacherous mountain pass leading towards Cyrodiil from the southern Pale, known for blizzards and ice trolls. Currently lightly patrolled by Imperials.",
                "tags": ["terrain_mountain_pass", "cultural_historical_significance_historic_site", "state_or_condition_current_contested_by_factions_potential", "imperial_influence_moderate", "monster_den_ice_troll", "climate_arctic", "travel_route_major_dangerous"]
            },
            {
                "id": 20006,
                "name": "Great Henge of the Ice-Speakers",
                "desc": "An ancient and massive stone circle on the northern tundra, believed to have been used by early Atmoran settlers for sky-worship. Rarely visited.",
                "tags": ["structure_type_standing_stone_circle", "cultural_historical_significance_nordic_ancient_site", "magical_properties_arcane_nexus_minor", "state_or_condition_current_isolated_and_forgotten", "terrain_tundra_plains", "climate_arctic"]
            },
            {
                "id": 20007,
                "name": "Snowpoint Overlook Cave",
                "desc": "A small ice cave high in the mountains of The Pale, offering a chilling view. It might be used by smugglers or serve as a den for ice wraiths.",
                "tags": ["structure_type_natural_cave", "climate_glacial", "economic_activity_smuggling_route_active_potential", "monster_den_ice_wraith", "terrain_mountain_peak", "dungeon_minor", "scenic_vista_panoramic"]
            },
            {
                "id": 20008,
                "name": "Forgotten Stones of the North",
                "desc": "A small, weathered circle of ancient stones on the tundra of The Pale. Their original purpose is lost to time, but they emanate a faint, cold energy.",
                "tags": ["structure_type_standing_stone_circle", "cultural_historical_significance_nordic_ancient_site", "structure_condition_weathered", "terrain_tundra_plains", "magical_properties_enchanted_neutral", "mystery_local"]
            },
            {
                "id": 20009,
                "name": "Icerunner's Rest",
                "desc": "A tiny, wind-battered fishing hamlet clinging to the icy northern coast of The Pale. Its few inhabitants are hardy folk, accustomed to the harsh sea.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_fishing_industry_local", "environment_coastal", "climate_glacial", "state_or_condition_current_isolated_and_forgotten"]
            },
            {
                "id": 20010,
                "name": "Snowdrift Cabin",
                "desc": "A solitary trapper's cabin, half-buried in snowdrifts for much of the year, located deep within the snowy plains of The Pale.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_weathered", "economic_activity_hunting_furs_meat", "climate_arctic", "terrain_tundra_plains", "hermit_lair_potential"]
            },
            {
                "id": 20011,
                "name": "Frostmoon Crag Cave",
                "desc": "An icy cave system high on a crag in The Pale, often glittering with frost and home to ice wraiths or frost trolls.",
                "tags": ["structure_type_natural_cave", "climate_glacial", "dungeon_minor", "monster_den_frost_troll", "monster_den_ice_wraith", "terrain_mountain_peak"]
            },
            {
                "id": 20012,
                "name": "Ruins of the Lost Patrol",
                "desc": "A scatter of weathered stones and a broken standard on the bleak tundra, marking the last stand of a forgotten Imperial or Stormcloak patrol from a past conflict.",
                "tags": ["structure_type_ruined_settlement", "cultural_historical_significance_battlefield_historic", "magical_properties_haunted_aura", "terrain_tundra_plains", "state_or_condition_current_isolated_and_forgotten"]
            },
            {
                "id": 20013,
                "name": "Yorgrim's Overlook",
                "desc": "The crumbling ruins of an ancient Nordic watchtower, named after a forgotten hero. It offers a commanding view of the surrounding tundra but is now home to bandits or wildlife.",
                "tags": ["structure_type_ruined_tower", "nordic_burial_site_minor", "dungeon_minor", "bandit_minor_camp_potential", "scenic_vista_panoramic", "cultural_historical_significance_nordic_ancient_site"]
            },
            {
                "id": 20014,
                "name": "Stillborn Cave (The Pale)",
                "desc": "A small, cold cave system in The Pale, named for a local tragedy or perhaps the eerie silence within. Often inhabited by frost spiders or other cold-dwelling creatures.",
                "tags": ["structure_type_natural_cave", "climate_arctic", "dungeon_minor", "monster_den_frost_spider", "urban_issues_or_atmosphere_haunted_rumors_strong", "tragedy_site_minor"]
            },
            {
                "id": 20015,
                "name": "The Lord Stone",
                "desc": "Found high in the mountains on the border of The Pale, east of Morthal, this Standing Stone grants increased physical resilience and resistance to magical attacks.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive", "terrain_mountain_peak", "cultural_historical_significance_ancient_magical_site", "climate_arctic"]
            },
            {
                "id": 20016,
                "name": "Korvanjund",
                "desc": "A large Nordic ruin in The Pale, south of Dawnstar. It is an ancient burial site of Nord heroes and kings, rumored to hold significant historical artifacts, possibly including a crown of legend. Heavily guarded by draugr.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "cultural_historical_significance_nordic_ancient_site", "quest_location_civil_war_jagged_crown", "specific_landmark_type_word_wall_location_potential", "artifact_location_rumored"]
            },
            {
                "id": 20017,
                "name": "Irkngthand",
                "desc": "A massive and ancient Dwemer ruin in The Pale, west of Nightgate Inn. It is a sprawling complex with many dangers, including Falmer and Dwemer constructs. Rumored to hold significant Dwemer artifacts.",
                "tags": ["dwemer_ruin_major_city", "dungeon_major", "falmer_presence_strong", "mechanical_constructs_dwemer_heavy", "quest_location_thieves_guild", "cultural_historical_significance_dwemer_ruin_site", "blackreach_elevator_access_potential", "chaurus_nest_potential"]
            },
            {
                "id": 20018,
                "name": "Duskglow Crevice",
                "desc": "A dark, winding cave system in The Pale, south of Dawnstar, infested with Falmer and their chaurus companions. It is a dangerous place, shunned by locals.",
                "tags": ["structure_type_natural_cave", "falmer_presence_strong", "chaurus_nest_major", "dungeon_major", "environment_underground", "state_or_condition_current_lawless_area"]
            }
        ]
    },

    # WINTERHOLD HOLD
    {
        "id": 3,
        "name": "Winterhold Hold",
        "desc": "A shattered hold on the northern coast, defined by icy gales, ancient ruins, and the dominant presence of the College of Winterhold. Much of the original city was lost to the Great Collapse centuries ago.",
        "tags": ["hold", "climate_glacial", "terrain_ice_field", "environment_coastal", "magical_properties_arcane_nexus", "cultural_historical_significance_great_collapse_affected_site", "nordic_culture_ancient", "college_of_winterhold_main_related", "state_or_condition_current_economically_depressed", "structure_condition_ruined_extensively"],
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
                "tags": ["populated_town", "structure_condition_ruined_extensively", "city_affiliation_winterhold_town_ruined", "magical_properties_arcane_nexus", "cultural_historical_significance_great_collapse_affected_site", "state_or_condition_current_isolated_and_forgotten", "settlement_features_jarls_longhouse", "urban_issues_or_atmosphere_fear_and_superstition", "climate_glacial"],
                "sub_locations": [
                    {
                        "id": 3001,
                        "name": "The Frozen Hearth",
                        "desc": "The sole remaining inn in Winterhold, offering shelter and rumors to travelers and College members, run by Dagur.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available", "structure_condition_weathered"]
                    },
                    {
                        "id": 3002,
                        "name": "College of Winterhold",
                        "desc": "A venerable institution of magic, perched precariously on a separated clifftop, a beacon for mages across Tamriel. Led by Arch-Mage Savos Aren.",
                        "tags": ["structure_type_guild_hall_building", "settlement_features_college_of_winterhold_main", "magical_properties_arcane_nexus", "cultural_historical_significance_ancient_magical_site", "political_tension_high", "unique_landmark_iconic", "quest_line_college_of_winterhold"],
                        "sub_locations": [
                            {
                                "id": 30021,
                                "name": "The Midden",
                                "desc": "The dark, forgotten underbelly of the College of Winterhold, a network of icy tunnels and chambers. Used for refuse, dangerous experiments, and rumored to hide darker secrets, including the Atronach Forge.",
                                "tags": ["environment_underground", "dungeon_major", "magical_properties_tainted_by_dark_magic", "specific_landmark_type_atronach_forge_location", "undead_presence_rumored_strong", "secret_location", "college_of_winterhold_main_related"]
                            }
                        ]
                    },
                    {
                        "id": 3003,
                        "name": "Jarl's Longhouse (Winterhold)",
                        "desc": "The modest seat of Winterhold's Jarl Korir, a man bitter about the College's perceived indifference to the town's plight.",
                        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local", "structure_condition_weathered", "political_tension_high"]
                    },
                    {
                        "id": 3004,
                        "name": "Birna's Oddments",
                        "desc": "A small shop run by Birna, offering a curious selection of goods, often scavenged or of questionable origin.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety_limited", "economic_activity_trade_hub_minor", "structure_condition_weathered"]
                    }
                ]
            },
            {
                "id": 31,
                "name": "Saarthal",
                "desc": "The excavated ruins of one of Skyrim's first human settlements, a site of great magical power and ancient Nordic mysteries, closely tied to the College of Winterhold's studies.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "magical_properties_arcane_nexus", "college_of_winterhold_main_related", "cultural_historical_significance_nordic_ancient_site", "artifact_location_powerful", "puzzle_ancient_magic"]
            },
            {
                "id": 32,
                "name": "Hob's Fall Cave",
                "desc": "A shadowy coastal cave north of Winterhold, a den for necromancers and their unholy experiments, or perhaps desperate smugglers.",
                "tags": ["structure_type_natural_cave", "specific_landmark_type_necromancer_tower_or_lair_potential", "economic_activity_smuggling_route_active_potential", "dungeon_minor", "environment_coastal", "magical_properties_tainted_by_dark_magic_potential", "undead_presence_skeletons_potential"]
            },
            {
                "id": 33,
                "name": "Yngol Barrow",
                "desc": "A mournful Nordic tomb east of Windhelm (close to Winterhold's border), where ancient magics linger and the ghost of Yngol's shade may be found by those seeking its secrets.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "magical_properties_haunted_aura", "cultural_historical_significance_legendary_hero_location", "artifact_location_unique_item", "puzzle_ancient_nordic"]
            },
            {
                "id": 34,
                "name": "Alftand",
                "desc": "A vast and treacherous Dwemer ruin deep within the mountains of Winterhold, one of the primary known entrances to the subterranean realm of Blackreach. It is a dangerous place, still patrolled by ancient constructs and inhabited by Falmer.",
                "tags": ["dwemer_ruin_major_city", "dungeon_large_complex", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "specific_landmark_type_blackreach_elevator_access", "quest_location_main_story_potential", "cultural_historical_significance_dwemer_ruin_site", "chaurus_nest_potential", "structure_condition_ruined_extensively"],
                "sub_locations": [
                    {
                        "id": 3401,
                        "name": "Alftand Glacial Ruins",
                        "desc": "The icy, upper exterior sections of Alftand, often patrolled by Falmer and ice wraiths.",
                        "tags": ["dwemer_ruin_minor_outpost", "climate_glacial", "monster_den_ice_wraith", "falmer_presence_scouts", "structure_condition_ruined_extensively"]
                    },
                    {
                        "id": 3402,
                        "name": "Alftand Animonculory",
                        "desc": "The main Dwemer manufactory within Alftand, filled with constructs, traps, and remnants of Dwemer machinery.",
                        "tags": ["dwemer_ruin_major_city_section", "mechanical_constructs_dwemer_heavy", "trap_heavy_environment", "ancient_technology_dwemer", "falmer_presence_strong"]
                    },
                    {
                        "id": 3403,
                        "name": "Alftand Cathedral",
                        "desc": "The grand central chamber of Alftand, leading deeper into the earth towards Blackreach. A place of significant Dwemer engineering.",
                        "tags": ["dwemer_ruin_major_city_section", "structure_type_temple_building_dwemer", "specific_landmark_type_blackreach_elevator_access", "mechanical_constructs_dwemer_boss_potential", "falmer_presence_strong"]
                    }
                ]
            },
            {
                "id": 35,
                "name": "Frostmere Crypt",
                "desc": "A Nordic barrow on the border between The Pale and Winterhold, rumored to be home to bandits and a legendary spectral weapon known as 'The Pale Blade'.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "bandit_minor_camp_potential", "quest_location_local_legend", "artifact_location_unique_item", "magical_properties_haunted_aura"]
            },
            {
                "id": 36,
                "name": "Pilgrim's Trench",
                "desc": "A shipwreck graveyard in the icy waters north of Winterhold, a treacherous area for sailors, rumored to hold lost cargo and attract scavengers.",
                "tags": ["structure_type_shipwreck_site", "environment_coastal", "climate_glacial", "treasure_cache_rumored", "dangerous_underwater_exploration", "monster_den_slaughterfish_potential"]
            },
            {
                "id": 37,
                "name": "Sightless Pit",
                "desc": "A deep, dark chasm leading into a Falmer-infested cave system, located in the southwestern mountains of Winterhold. A place of utter darkness and terror.",
                "tags": ["structure_type_natural_cave", "falmer_presence_strong", "dungeon_major", "terrain_canyon", "environment_underground", "chaurus_nest_major", "state_or_condition_current_lawless_area"]
            },
            {
                "id": 38,
                "name": "Skytemple Ruins",
                "desc": "Ruined Nordic towers atop a desolate mountain, offering a commanding view of Winterhold's icy expanse but little shelter from the biting winds.",
                "tags": ["structure_type_ruined_tower", "nordic_burial_site_minor", "terrain_mountain_peak", "structure_condition_ruined_extensively", "climate_glacial", "scenic_vista_panoramic"]
            },
            {
                "id": 39,
                "name": "Snowpoint Beacon",
                "desc": "A ruined watchtower on the northern coast of Winterhold, now a desolate landmark against the frozen sea.",
                "tags": ["structure_type_ruined_tower", "environment_coastal", "structure_condition_abandoned", "state_or_condition_current_isolated_and_forgotten", "climate_glacial"]
            },
            {
                "id": 30001,
                "name": "Ysgramor's Tomb",
                "desc": "The final resting place of the legendary Ysgramor, founder of the Companions and leader of the Five Hundred Companions. A revered and dangerous Nordic tomb, closely guarded by the spirits of ancient heroes.",
                "tags": ["nordic_burial_site_major", "cultural_historical_significance_legendary_hero_location", "companions_guild_hall_related", "undead_presence_strong", "draugr_heavy", "dungeon_major", "quest_location_companions_guild_hall", "artifact_location_powerful"]
            },
            {
                "id": 30002,
                "name": "The Serpent Stone",
                "desc": "A Standing Stone located on an island in the Sea of Ghosts, north of the College of Winterhold, granting a unique paralytic magical power once per day.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral", "terrain_island", "environment_coastal", "climate_glacial", "power_paralysis_ranged"]
            },
            {
                "id": 30003,
                "name": "Driftshade Refuge",
                "desc": "An abandoned fort in Winterhold, which rumors say was once used by a renegade group of mages or, more recently, became a den for ice wraiths or desperate bandits.",
                "tags": ["structure_type_ruined_fort", "structure_condition_abandoned", "monster_den_ice_wraith_potential", "bandit_minor_camp_potential", "dungeon_minor", "silver_hand_lair_potential_alt"]
            },
            # New Winterhold Hold Locations
            {
                "id": 30004,
                "name": "Bleakcoast Cave",
                "desc": "A desolate ice cave on the northern coast, home to frost trolls and other hardy creatures adapted to the extreme cold.",
                "tags": ["structure_type_natural_cave", "climate_glacial", "monster_den_frost_troll", "environment_coastal", "dungeon_minor", "terrain_ice_field"]
            },
            {
                "id": 30005,
                "name": "The Wreck of the Winter Warbler",
                "desc": "A shipwreck frozen in the ice along Winterhold's northern coast, its treasures and the fate of its crew preserved in the cold.",
                "tags": ["structure_type_shipwreck_site", "structure_condition_ruined_extensively", "environment_coastal", "climate_glacial", "treasure_cache_rumored", "undead_presence_skeletons_potential", "dungeon_minor"]
            },
            {
                "id": 30006,
                "name": "Japhet's Folly",
                "desc": "A small, isolated tower on an island far off the coast of Winterhold, rumored to be the retreat of a mad wizard or a hidden pirate cache. Currently, it is mostly a ruin battered by storms.",
                "tags": ["structure_type_ruined_tower", "terrain_island", "state_or_condition_current_isolated_and_forgotten", "magical_properties_enchanted_neutral_potential", "pirate_cove_hidden_potential", "environment_coastal", "climate_glacial", "quest_location_college_of_winterhold_potential"]
            },
            {
                "id": 30007,
                "name": "Frostedge Fishery",
                "desc": "A struggling fishing outpost on the treacherous icy coast of Winterhold, where a few hardy souls attempt to make a living from the frozen sea.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_fishing_industry_local", "environment_coastal", "climate_glacial", "state_or_condition_current_economically_depressed"]
            },
            {
                "id": 30008,
                "name": "Hermit's Peak Cave",
                "desc": "A small, somewhat habitable ice cave high in the mountains of Winterhold, rumored to be the dwelling of a reclusive mage or a forgotten scholar.",
                "tags": ["structure_type_natural_cave", "climate_glacial", "terrain_mountain_peak", "hermit_lair_potential", "magical_properties_arcane_focus_minor_potential", "dungeon_minor"]
            },
            {
                "id": 30009,
                "name": "Glacial Crevice",
                "desc": "A narrow, icy fissure in the mountains of Winterhold, leading to a small, frigid cave system. Often home to ice wraiths or other cold-dwelling creatures.",
                "tags": ["structure_type_natural_cave", "climate_glacial", "dungeon_minor", "monster_den_ice_wraith", "terrain_mountain_pass", "natural_formation_unique"]
            },
            {
                "id": 30010,
                "name": "Forgotten Scholar's Hovel",
                "desc": "The collapsed remains of a small, ancient stone hovel, half-buried in snow. A few weathered books or scrolls might hint at its former occupant.",
                "tags": ["structure_type_ruined_shack", "cultural_historical_significance_historic_site", "structure_condition_collapsed", "lore_clue_potential", "climate_glacial", "terrain_ice_field"]
            },
            {
                "id": 30011,
                "name": "Snow-Shod Stables & Farm (Winterhold Outskirts)",
                "desc": "A surprisingly resilient farm and stables on the very edge of Winterhold's domain, perhaps benefiting from minor College enchantments to ward off the worst of the cold. They breed hardy northern ponies.",
                "tags": ["structure_type_farmstead", "structure_type_stable_building", "economic_activity_farming_livestock", "settlement_minor", "climate_arctic_edge", "magical_properties_enchanted_neutral_potential"]
            },
            {
                "id": 30012,
                "name": "Whistling Mine",
                "desc": "A tiny, struggling mining outpost in the northern cliffs of Winterhold, where miners brave the biting winds to extract a rare, ice-infused ore said to hum faintly.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_mining_gems", "structure_type_mine_active", "climate_glacial", "state_or_condition_current_isolated_and_forgotten", "magical_properties_enchanted_neutral_potential"]
            },
            {
                "id": 30013,
                "name": "Shrine of Jhunal (Lost)",
                "desc": "The snow-swept, crumbling ruins of an ancient shrine dedicated to Jhunal, the Nordic god of knowledge and runes, predating the College's dominance. A few weathered carvings remain.",
                "tags": ["structure_type_ruined_shrine", "religious_site_aedric", "cultural_historical_significance_nordic_ancient_site", "magical_properties_arcane_focus_minor_potential", "lore_clue_potential", "climate_glacial", "terrain_ice_field"]
            },
            {
                "id": 30014,
                "name": "Frozen Mammoth Cave",
                "desc": "A glacial cave where an ancient mammoth was flash-frozen millennia ago. The cave is now home to ice wraiths and other frost creatures, drawn to its intense cold.",
                "tags": ["structure_type_natural_cave", "climate_glacial", "dungeon_minor", "monster_den_ice_wraith", "unique_natural_formation", "cultural_historical_significance_historic_site"]
            },
            {
                "id": 30015,
                "name": "The Tower Stone",
                "desc": "Located on a windswept clifftop along Winterhold's icy coast, this Standing Stone grants the power to once a day open any expert-level or lower lock.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral", "environment_coastal", "terrain_cliffside", "cultural_historical_significance_ancient_magical_site", "utility_buff_lockpicking"]
            },
            {
                "id": 30016,
                "name": "Mount Anthor",
                "desc": "A high mountain peak on the border of Winterhold and The Pale, known in ancient legends as a dragon lair. While no dragons have been seen for centuries, it holds an ancient Word Wall.",
                "tags": ["terrain_mountain_peak", "specific_landmark_type_dragon_lair_ancient_inactive", "specific_landmark_type_word_wall_location", "dungeon_minor", "cultural_historical_significance_dragon_lore_site_ancient", "climate_glacial", "state_or_condition_current_isolated_and_forgotten"]
            },
            {
                "id": 30018,
                "name": "Yngvild",
                "desc": "An icy Nordic ruin on an island northeast of Dawnstar (near Winterhold border). It is haunted by the ghosts of women enthralled by the necromancer Arondil.",
                "tags": ["nordic_burial_site_major", "structure_condition_ruined_extensively", "dungeon_major", "specific_landmark_type_necromancer_tower_or_lair", "magical_properties_haunted_aura", "undead_presence_strong", "quest_location_investigation", "terrain_island", "environment_coastal", "climate_glacial"]
            }
        ]
    },

    # HJAALMARCH (Morthal Hold)
    {
        "id": 4,
        "name": "Hjaalmarch",
        "desc": "A bleak, marshy hold shrouded in perpetual mist and steeped in superstition. Its capital, Morthal, is known for its reclusive nature and recent troubles with strange occurrences and whispers of vampirism.",
        "tags": ["hold", "terrain_marsh", "terrain_swamp", "state_or_condition_current_isolated_and_forgotten", "nordic_culture_local", "urban_issues_or_atmosphere_fear_and_superstition", "magical_properties_daedric_influence_subtle_rumor", "climate_swampy", "environment_wilderness", "political_tension_high_potential"],
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
                "tags": ["populated_town", "terrain_marsh", "city_affiliation_morthal_town", "urban_issues_or_atmosphere_fear_and_superstition", "magical_properties_daedric_influence_subtle_rumor", "settlement_features_jarls_longhouse", "state_or_condition_current_isolated_and_forgotten", "quest_location_vampire_investigation", "climate_swampy"],
                "sub_locations": [
                    {
                        "id": 4001,
                        "name": "Highmoon Hall",
                        "desc": "The austere residence of Jarl Idgrod Ravencrone and her family, where she contemplates her visions.",
                        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local", "magical_properties_arcane_focus_minor_potential", "political_family_seer"]
                    },
                    {
                        "id": 4002,
                        "name": "Moorside Inn",
                        "desc": "A humble inn providing shelter for travelers daring to brave the murky swamps, run by Jonna.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available", "structure_condition_weathered"]
                    },
                    {
                        "id": 4003,
                        "name": "Thaumaturgist's Hut (Falion's House)",
                        "desc": "The home of Falion, Morthal's resident wizard and expert on all things arcane, including vampirism. He is viewed with suspicion by some.",
                        "tags": ["structure_type_shop_building", "structure_type_residence", "settlement_features_alchemy_shop_notable", "item_type_potion_vendor", "item_type_ingredient_vendor", "magical_properties_arcane_focus", "quest_giver_vampire_cure", "scholar_retreat_rumor"]
                    },
                    {
                        "id": 4004,
                        "name": "Jorgen and Lami's House",
                        "desc": "The home of Jorgen and Lami, who work at the local lumber mill. Lami is an aspiring alchemist.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "economic_activity_logging_timber_worker", "alchemy_apprentice_potential"]
                    },
                    {
                        "id": 4005,
                        "name": "Burned House",
                        "desc": "The charred ruins of Hroggar's house, site of a recent tragedy that has the town on edge and fuels rumors of dark magic.",
                        "tags": ["structure_type_ruined_shack", "structure_condition_collapsed", "tragedy_site_family", "quest_location_vampire_investigation", "urban_issues_or_atmosphere_haunted_rumors_strong"]
                    }
                ]
            },
            {
                "id": 41,
                "name": "Movarth's Lair",
                "desc": "A dank cave north of Morthal, rumored to be the den of the master vampire Movarth Piquine and his thralls. Its discovery is key to resolving Morthal's troubles.",
                "tags": ["structure_type_natural_cave", "specific_landmark_type_vampire_ancient_lair", "dungeon_major", "quest_location_vampire_investigation", "undead_presence_strong", "magical_properties_tainted_by_dark_magic", "boss_fight_vampire_lord_potential"]
            },
            {
                "id": 42,
                "name": "Ustengrav",
                "desc": "A sprawling ancient Nordic tomb deep within Hjaalmarch's marshes, said to hold the Horn of Jurgen Windcaller, a significant relic sought by the Greybeards.",
                "tags": ["nordic_burial_site_major", "dungeon_large_complex", "undead_presence_strong", "draugr_heavy", "quest_location_main_story_early", "specific_landmark_type_word_wall_location", "artifact_location_unique_item", "puzzle_ancient_nordic", "terrain_marsh_edge"]
            },
            {
                "id": 43,
                "name": "Stonehills",
                "desc": "A modest mining outpost in Hjaalmarch, focused on excavating iron ore, managed by Pactur.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_mining_iron", "resource_node", "terrain_hilly_marsh_edge", "climate_swampy_edge"],
                "sub_locations": [
                    {
                        "id": 4301,
                        "name": "Rockwallow Mine",
                        "desc": "The iron mine that sustains the small settlement of Stonehills.",
                        "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "resource_node"]
                    },
                    {
                        "id": 4302,
                        "name": "Sorli's House",
                        "desc": "The residence of Sorli the Builder, an important figure in Stonehills who hopes to see the mine prosper.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "community_leader_potential"]
                    }
                ]
            },
            {
                "id": 44,
                "name": "Apprentice Stone",
                "desc": "A Standing Stone located in the marshes northwest of Morthal, granting faster Magicka regeneration but also increased susceptibility to magic.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_neutral", "terrain_marsh", "terrain_island", "buff_magicka_regen_increased", "debuff_magic_weakness_increased"]
            },
            {
                "id": 45,
                "name": "Brood Cavern",
                "desc": "A small cave in Hjaalmarch, often infested with spiders, chaurus, or other venomous creatures.",
                "tags": ["structure_type_natural_cave", "monster_den_spider", "monster_den_chaurus_potential", "dungeon_minor", "terrain_marsh", "alchemy_ingredient_source_rich_potential"]
            },
            {
                "id": 46,
                "name": "Chillwind Depths",
                "desc": "A large cave system south of Dragon Bridge (near Hjaalmarch border), inhabited by Falmer, Chaurus, and other subterranean horrors.",
                "tags": ["structure_type_natural_cave", "falmer_presence_strong", "chaurus_nest_major", "dungeon_major", "environment_underground", "terrain_mountain_cave_remote", "state_or_condition_current_lawless_area"]
            },
            {
                "id": 47,
                "name": "Dead Men's Respite",
                "desc": "A Nordic ruin southwest of Morthal, connected to the Bards College and the legend of King Olaf One-Eye. It is guarded by draugr and holds ancient secrets.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "bards_college_location_related", "specific_landmark_type_word_wall_location", "cultural_historical_significance_legendary_hero_location", "puzzle_ancient_nordic"]
            },
            {
                "id": 48,
                "name": "Folgunthur",
                "desc": "An ancient Nordic ruin south of Solitude, near the Hjaalmarch border, where a fragment of the legendary Gauldur Amulet is sought, guarded by Mikrul Gauldurson.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "draugr_heavy", "quest_location_artifact_gauldur_amulet", "cultural_historical_significance_ancient_magical_site", "puzzle_dragon_claw"]
            },
            {
                "id": 49,
                "name": "Kjenstag Ruins",
                "desc": "Ruined Nordic structures in the marshes, sometimes haunted by restless spirits or occupied by desperate bandits seeking shelter.",
                "tags": ["structure_type_ruined_tower", "nordic_burial_site_minor", "terrain_marsh", "magical_properties_haunted_aura_potential", "bandit_minor_camp_potential", "structure_condition_ruined_extensively"]
            },
            {
                "id": 40001,
                "name": "Meeko's Shack",
                "desc": "A small, abandoned shack south of Solitude Sawmill, near the Hjaalmarch border. A loyal dog named Meeko waits here for his deceased master.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_abandoned", "animal_companion_unique", "tragedy_site_minor", "terrain_forested_area_edge"]
            },
            {
                "id": 40002,
                "name": "Robber's Gorge",
                "desc": "A bandit-controlled ravine and bridge southwest of Rorikstead, on the edge of Hjaalmarch, a notorious spot for ambushes.",
                "tags": ["bandit_main_stronghold", "terrain_canyon", "structure_type_bridge_structure", "dungeon_major", "state_or_condition_current_bandit_controlled_area", "toll_road_illegal"]
            },
            {
                "id": 40003,
                "name": "Wreck of the Icerunner",
                "desc": "A shipwreck on the northern coast of Hjaalmarch, west of Solitude. It is now a den for bandits or pirates who prey on coastal traffic.",
                "tags": ["structure_type_shipwreck_site", "specific_landmark_type_pirate_cove_hidden", "environment_coastal", "dungeon_minor", "treasure_cache_rumored", "bandit_minor_camp_potential"]
            },
            # New Hjaalmarch Locations
            {
                "id": 40004,
                "name": "The Stumbling Sabrecat",
                "desc": "A rickety, half-sunken shack in the deepest part of the Drajkmyr Marsh, rumored to be the home of a reclusive (and possibly mad) alchemist or a coven of witches.",
                "tags": ["structure_type_shack_or_hut", "structure_condition_ruined_extensively", "terrain_marsh", "hermit_lair_potential", "magical_properties_tainted_by_dark_magic_potential", "alchemy_ingredient_source_rich_potential", "witch_coven_potential"]
            },
            {
                "id": 40005,
                "name": "Folkvar's Folly",
                "desc": "A small, abandoned watchtower slowly sinking into the marsh. Local legend says it was built by a foolish Thane who ignored warnings about the unstable ground.",
                "tags": ["structure_type_ruined_tower", "structure_condition_collapsed", "terrain_marsh", "cultural_historical_significance_local_legend", "bandit_minor_camp_potential", "state_or_condition_current_isolated_and_forgotten"]
            },
            {
                "id": 40006,
                "name": "Drajkmyr Crossing",
                "desc": "A tiny, precarious stilt-village built over the murky waters on the edge of the Drajkmyr marsh, known for its unique eel fishing techniques.",
                "tags": ["populated_village", "settlement_minor", "economic_activity_fishing_industry_local", "terrain_marsh", "structure_type_settlement_minor", "unique_culture_local", "state_or_condition_current_isolated_and_forgotten"]
            },
            {
                "id": 40007,
                "name": "Peatbogger's Hut",
                "desc": "The isolated hut of a solitary peat farmer, who harvests the rich soil of Hjaalmarch for fuel and fertilizer.",
                "tags": ["structure_type_shack_or_hut", "economic_activity_farming_crops", "terrain_marsh", "hermit_lair_potential", "state_or_condition_current_isolated_and_forgotten"]
            },
            {
                "id": 40008,
                "name": "Murkwater Hollow",
                "desc": "A muddy, flooded cave system deep within Hjaalmarch's swamps, likely home to chaurus, mudcrabs, or even a reclusive giant snake if such existed.",
                "tags": ["structure_type_natural_cave", "terrain_marsh", "dungeon_minor", "monster_den_chaurus", "monster_den_mudcrab", "structure_condition_flooded"]
            },
            {
                "id": 40009,
                "name": "Sinking Stones of the Marsh",
                "desc": "A small, barely visible ruin of ancient stones half-sunk in the swamp, perhaps part of an old Nordic watchtower or shrine, now reclaimed by the marsh.",
                "tags": ["structure_type_ruined_shrine", "nordic_burial_site_minor", "terrain_marsh", "structure_condition_collapsed", "treasure_cache_rumored", "cultural_historical_significance_nordic_ancient_site"]
            },
            {
                "id": 40010,
                "name": "Misty Grove Farm",
                "desc": "A small, struggling farm on the edge of the Drajkmyr Marsh, where the farmer battles constant dampness and swamp pests to grow hardy root vegetables.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_crops", "terrain_marsh_edge", "state_or_condition_current_isolated_and_forgotten", "structure_condition_weathered"]
            },
            {
                "id": 40011,
                "name": "Fort Snowhawk (Ruined)",
                "desc": "The dilapidated ruins of an old Imperial fort, now largely swallowed by the marsh. Rumored to be haunted by its former garrison or used as a hideout by bog bandits.",
                "tags": ["structure_type_ruined_fort", "terrain_marsh", "dungeon_minor", "magical_properties_haunted_aura_potential", "bandit_minor_camp_potential", "cultural_historical_significance_historic_site", "structure_condition_ruined_extensively"]
            },
            {
                "id": 40012,
                "name": "Shrine of Herma-Mora (Hidden Marsh Shrine)",
                "desc": "A small, hidden shrine of crudely piled stones and waterlogged tomes dedicated to Hermaeus Mora, tucked away in a particularly dense and foggy part of Hjaalmarch. Only those seeking forbidden knowledge would find it.",
                "tags": ["structure_type_shrine_outdoor_structure", "magical_properties_daedric_influence_overt", "terrain_marsh", "secret_location", "forbidden_knowledge_dangerous", "cult_activity_potential_minor", "hermaeus_mora_shrine"]
            },
            {
                "id": 40013,
                "name": "Bogbound Barrow",
                "desc": "A small, partially flooded Nordic barrow slowly being reclaimed by the swamp. It's likely home to draugr who guard meager treasures.",
                "tags": ["nordic_burial_site_minor", "structure_condition_flooded", "dungeon_minor", "undead_presence_strong", "draugr_heavy", "terrain_marsh"]
            },
            {
                "id": 40014,
                "name": "Lost Echo Cave",
                "desc": "A large cave system in Hjaalmarch, west of Morthal, known for its unusual acoustics. It is now a den for Falmer and their chaurus, and contains an ancient Word Wall.",
                "tags": ["structure_type_natural_cave", "falmer_presence_strong", "chaurus_nest_major", "dungeon_major", "specific_landmark_type_word_wall_location", "unique_natural_formation", "state_or_condition_current_lawless_area"]
            },
            {
                "id": 40015,
                "name": "Ragnvald",
                "desc": "An ancient Nordic ruin in the mountains of Hjaalmarch, north of Markarth. It is a burial site guarded by powerful draugr and the Dragon Priest Otar the Mad.",
                "tags": ["nordic_burial_site_major", "dungeon_large_complex", "cultural_historical_significance_dragon_cult_lair_priest", "undead_presence_strong", "draugr_heavy", "specific_landmark_type_word_wall_location", "magical_properties_arcane_nexus", "dragon_priest_otar"]
            },
            {
                "id": 40016,
                "name": "Orotheim",
                "desc": "A small cave system in the western part of Hjaalmarch, often used as a hideout by a desperate group of bandits preying on the sparse traffic through the marshes.",
                "tags": ["structure_type_natural_cave", "bandit_minor_camp", "dungeon_minor", "terrain_marsh_edge", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 40017,
                "name": "Mzinchaleft",
                "desc": "A large Dwemer ruin in Hjaalmarch, south of Dawnstar (near The Pale border). It is a dangerous complex filled with Dwemer constructs, Falmer, and a Great Lift providing access to Blackreach.",
                "tags": ["dwemer_ruin_major_city", "dungeon_large_complex", "mechanical_constructs_dwemer_heavy", "falmer_presence_strong", "specific_landmark_type_blackreach_elevator_access", "cultural_historical_significance_dwemer_ruin_site", "ancient_technology_dwemer", "chaurus_nest_potential"]
            }
        ]
    },

    # FALKREATH HOLD
    {
        "id": 5,
        "name": "Falkreath Hold",
        "desc": "A heavily forested hold in southern Skyrim, known for its ancient woods, towering mountains, and the somber town of Falkreath with its large graveyard. It borders Cyrodiil and is an important Imperial territory.",
        "tags": ["hold", "terrain_forest", "climate_temperate", "cultural_historical_significance_graveyard_town", "terrain_mountainous", "cyrodiil_border_region", "nordic_culture_local", "imperial_influence_strong", "economic_activity_logging_timber", "state_or_condition_current_politically_stable"],
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
                "tags": ["populated_town", "terrain_forest", "city_affiliation_falkreath_town", "cultural_historical_significance_graveyard_town", "settlement_features_jarls_longhouse", "daedric_influence_subtle_rumor", "economic_activity_logging_timber", "urban_issues_or_atmosphere_oppressive_atmosphere", "imperial_influence_strong"],
                "sub_locations": [
                    {
                        "id": 5001,
                        "name": "Dead Man's Drink",
                        "desc": "The local tavern in Falkreath, a place for locals and weary travelers to find mead and solace, run by Valga Vinicia.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "rumor_source", "food_drink_vendor", "lodging_available"]
                    },
                    {
                        "id": 5002,
                        "name": "Jarl's Longhouse (Falkreath)",
                        "desc": "The seat of authority in Falkreath Hold, residence of Jarl Siddgeir.",
                        "tags": ["structure_type_palace_or_manor", "settlement_features_jarls_longhouse", "government_local", "imperial_influence_strong"]
                    },
                    {
                        "id": 5003,
                        "name": "Falkreath Graveyard",
                        "desc": "An expansive and ancient cemetery, the largest in Skyrim, where many Nords, both heroes and common folk, are laid to rest. Restless spirits are sometimes rumored here.",
                        "tags": ["cultural_historical_significance_historic_burial_site_major", "religious_site_aedric", "arkay_presence", "undead_presence_rumored_low", "unique_landmark_iconic", "urban_issues_or_atmosphere_haunted_rumors_strong"]
                    },
                    {
                        "id": 5004,
                        "name": "Gray Pine Goods",
                        "desc": "Solaf's shop in Falkreath, offering general supplies, hunting gear, and lumber from the local mill.",
                        "tags": ["structure_type_shop_building", "shop_general_goods", "trade_variety", "economic_activity_hunting_furs_meat_vendor", "economic_activity_logging_timber_vendor"]
                    },
                    {
                        "id": 5005,
                        "name": "Lod's House and Smithy",
                        "desc": "The home and workshop of Lod, Falkreath's blacksmith, who can often be found working his forge, sometimes seeking a particular dog.",
                        "tags": ["structure_type_shop_building", "structure_type_residence", "settlement_features_blacksmith_forge_active", "economic_activity_smithing_production", "quest_giver_daedric_clues"]
                    },
                    {
                        "id": 5006,
                        "name": "Hall of the Dead (Falkreath)",
                        "desc": "Falkreath's hall for honoring the dead, managed by Runil, a priest of Arkay, who also tends the graveyard.",
                        "tags": ["structure_type_temple_building", "religious_site_aedric", "arkay_shrine", "settlement_features_catacombs_burial_access_potential"]
                    },
                    {
                        "id": 5007,
                        "name": "Dark Brotherhood Sanctuary (Falkreath Entrance)",
                        "desc": "A hidden sanctuary of the Dark Brotherhood, concealed within the pine forests near Falkreath. Its door is marked by a sinister black hand.",
                        "tags": ["specific_landmark_type_assassin_guild_hq_active", "secret_location", "dungeon_major_entrance", "terrain_forest", "magical_properties_tainted_by_dark_magic_potential"]
                    }
                ]
            },
            {
                "id": 51,
                "name": "Pinewatch",
                "desc": "A secluded farmhouse north of Falkreath. While appearing innocent, it serves as a well-concealed front for a secret bandit hideout and smuggling operation.",
                "tags": ["structure_type_farmstead", "bandit_main_stronghold", "dungeon_major", "quest_location_thieves_guild", "economic_activity_smuggling_route_active", "secret_location", "terrain_forest"]
            },
            {
                "id": 52,
                "name": "Halldir's Cairn",
                "desc": "A solemn Nordic barrow southwest of Falkreath, haunted by the powerful draugr sorcerer Halldir and his elemental thralls.",
                "tags": ["nordic_burial_site_major", "dungeon_major", "undead_presence_strong", "magical_properties_arcane_nexus", "monster_den_elemental", "draugr_heavy", "boss_fight_mage_powerful"]
            },
            {
                "id": 53,
                "name": "Helgen",
                "desc": "A modest but strategically important Imperial fortified town at the southern border of Whiterun Hold, known for its lumber trade and guarding the pass to Cyrodiil. It is currently a functional settlement.",
                "tags": ["village", "imperial_outpost", "lumber_town", "cyrodiil_border_pass", "quest_start_location_potential", "functional_settlement"],
                 "sub_locations": [
                    {
                        "id": 5301,
                        "name": "Helgen Keep",
                        "desc": "The main keep of Helgen, garrisoned by Imperial soldiers. It serves as the town's primary defense and administrative center.",
                        "tags": ["structure_type_fortified_keep", "military_presence", "imperial_influence_strong", "government_local", "structure_condition_pristine"]
                    },
                    {
                        "id": 5302,
                        "name": "Helgen Homestead",
                        "desc": "One of the sturdy wooden homes within the town of Helgen.",
                        "tags": ["structure_type_residence", "commoner_dwelling", "settlement_minor"]
                    },
                    {
                        "id": 5303,
                        "name": "The Dragon's Rest Inn (Helgen)",
                        "desc": "A small, welcoming inn in Helgen, catering to local loggers and Imperial soldiers passing through.",
                        "tags": ["structure_type_inn_building", "settlement_features_tavern", "social_hub_popular", "food_drink_vendor", "lodging_available"]
                    }
                ]
            },
            {
                "id": 54,
                "name": "Ancestor Glade",
                "desc": "A hidden, serene glade sacred to the Moth Priests, located in the southern mountains of Falkreath Hold. It's a place of profound natural beauty and ancient ritual, though its significance is known to few.",
                "tags": ["cultural_historical_significance_sacred_grove_kynareth", "unique_natural_formation", "magical_properties_aedric_blessing_active", "secluded_nature_spot", "quest_location_dawnguard_potential", "alchemy_ingredient_source_rich_unique"]
            },
            {
                "id": 55,
                "name": "Bloodlet Throne",
                "desc": "A ruined fort atop a mountain in Falkreath, now a lair for a powerful coven of vampires who prey on unwary travelers.",
                "tags": ["structure_type_ruined_fort", "specific_landmark_type_vampire_ancient_lair", "dungeon_major", "terrain_mountain_peak", "state_or_condition_current_lawless_area", "undead_presence_strong", "magical_properties_tainted_by_dark_magic"]
            },
            {
                "id": 56,
                "name": "Brittleshin Pass",
                "desc": "A small cave system serving as a pass through the mountains south of Falkreath, often inhabited by necromancers, undead, or desperate bandits.",
                "tags": ["structure_type_natural_cave", "terrain_mountain_pass", "specific_landmark_type_necromancer_hideout_potential", "undead_presence_skeletons_potential", "bandit_minor_camp_potential", "dungeon_minor", "travel_route_alternative_dangerous"]
            },
            {
                "id": 57,
                "name": "Embershard Mine",
                "desc": "An iron mine located between Riverwood and Helgen, currently occupied by a band of opportunistic bandits.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_iron", "bandit_minor_camp", "dungeon_minor", "state_or_condition_current_bandit_controlled_area", "resource_node"]
            },
            {
                "id": 58,
                "name": "Evergreen Grove",
                "desc": "A small, secluded grove west of Falkreath, known for its spriggans and natural tranquility. Alchemists sometimes seek rare herbs here.",
                "tags": ["environment_wilderness", "terrain_forest", "specific_landmark_type_spriggan_sanctuary", "alchemy_ingredient_source_rich", "secluded_nature_spot", "magical_properties_enchanted_neutral"]
            },
            {
                "id": 59,
                "name": "Knifepoint Ridge",
                "desc": "A bandit-occupied mine and camp in the northwestern part of Falkreath Hold, from which raids are launched. Rumored to be connected to a Daedric artifact.",
                "tags": ["structure_type_mine_active", "economic_activity_mining_corundum_potential", "bandit_main_stronghold", "dungeon_major", "quest_location_daedric_boethiah", "state_or_condition_current_bandit_controlled_area"]
            },
            {
                "id": 50001,
                "name": "Moss Mother Cavern",
                "desc": "A cave system east of Falkreath, home to various creatures like spriggans and bears, and connected to local legends of nature spirits.",
                "tags": ["structure_type_natural_cave", "monster_den_spriggan", "monster_den_bear", "quest_location_local_legend", "dungeon_minor", "unique_natural_formation", "alchemy_ingredient_source_rich"]
            },
            {
                "id": 50002,
                "name": "Peak's Shade Tower",
                "desc": "A ruined tower south of Falkreath, often a lair for hagravens or other malevolent creatures who perform dark rituals under the forest canopy.",
                "tags": ["structure_type_ruined_tower", "specific_landmark_type_hagraven_coven_lair_main_potential", "magical_properties_tainted_by_dark_magic", "dungeon_minor", "terrain_forest", "ritual_site_dark_magic"]
            },
            {
                "id": 50003,
                "name": "Roadside Ruins",
                "desc": "Crumbling Nordic ruins along the road in Falkreath Hold, sometimes attracting spriggans guarding their territory or bandits lying in ambush.",
                "tags": ["structure_type_ruined_shrine", "nordic_burial_site_minor", "roadside_encounter_point", "monster_den_spriggan_potential", "bandit_minor_camp_potential", "structure_condition_ruined_extensively"]
            },
            {
                "id": 50004,
                "name": "Sunderstone Gorge",
                "desc": "A large cave system in the southern mountains of Falkreath, housing an ancient Word Wall and various magical inhabitants, including fire-wielding mages or atronachs.",
                "tags": ["structure_type_natural_cave", "dungeon_major", "specific_landmark_type_word_wall_location", "magical_properties_elemental_fire_dominant", "monster_den_fire_atronach", "mage_lair_hostile_fire"]
            },
            {
                "id": 50005,
                "name": "Cracked Tusk Keep",
                "desc": "A ruined fort in Falkreath Hold, now occupied by a fierce band of Orc bandits. Rumor has it they guard a fragment of a powerful Daedric artifact.",
                "tags": ["structure_type_ruined_fort", "bandit_main_stronghold", "orc_presence_hostile", "dungeon_major", "quest_location_daedric_mehrunes_razor", "artifact_location_daedric"]
            },
            # New Falkreath Hold Locations
            {
                "id": 50006,
                "name": "Angi's Camp",
                "desc": "A secluded cabin in the southern mountains of Falkreath, home to Angi, a skilled archer offering training to those who find her.",
                "tags": ["structure_type_shack_or_hut", "hermit_lair", "skill_trainer_archery", "terrain_mountainous", "state_or_condition_current_isolated_and_forgotten", "hunter_gathering_spot"]
            },
            {
                "id": 50007,
                "name": "Fort Neugrad",
                "desc": "A large Imperial fort near the Cyrodiilic border, guarding a key mountain pass. Currently well-garrisoned and a symbol of Imperial authority in the region.",
                "tags": ["structure_type_fortified_keep", "military_presence", "imperial_influence_strong", "cyrodiil_border_region", "dungeon_major", "state_or_condition_current_contested_by_factions_potential", "civil_war_quest_historic_site_potential"]
            },
            {
                "id": 50008,
                "name": "Lake Ilinalta",
                "desc": "A large, deep lake in western Falkreath Hold, shrouded in mist and legend. Its depths are said to hold ancient secrets and perhaps even a sunken ruin.",
                "tags": ["terrain_lake_large", "climate_temperate", "cultural_historical_significance_local_legend", "structure_type_ruined_fort_submerged_potential", "economic_activity_fishing_industry_local", "unique_natural_formation", "quest_location_daedric_azura_star_related"],
                "sub_locations": [
                    {
                        "id": 500081,
                        "name": "Ilinalta's Deep",
                        "desc": "The treacherous, flooded ruins of an ancient fort or temple within Lake Ilinalta, rumored to be haunted and guarded by necromancers or dark creatures.",
                        "tags": ["structure_type_ruined_fort_submerged", "specific_landmark_type_necromancer_tower_or_lair", "undead_presence_strong", "dungeon_major", "quest_location_daedric_azura_star", "magical_properties_tainted_by_dark_magic", "structure_condition_flooded"]
                    }
                ]
            },
            {
                "id": 50009,
                "name": "The Lady Stone",
                "desc": "A Standing Stone located on an island in Lake Ilinalta, granting enhanced health and stamina regeneration.",
                "tags": ["specific_landmark_type_standing_stone_magical", "magical_properties_enchanted_positive", "terrain_island", "terrain_lake_large_nearby", "buff_health_regen_increased", "buff_stamina_regen_increased"]
            },
            {
                "id": 50010,
                "name": "Hunter's Rest Clearing",
                "desc": "A small, secluded clearing deep in the forests of Falkreath, often used by hunters as a temporary camp. Signs of recent use are common.",
                "tags": ["hunter_gathering_spot", "environment_wilderness", "terrain_forest", "secluded_nature_spot", "bandit_minor_camp_potential"]
            },
            {
                "id": 50011,
                "name": "Wolfstooth Den",
                "desc": "A shallow cave system within Falkreath's dense woods, currently serving as a den for a pack of territorial wolves.",
                "tags": ["structure_type_natural_cave", "monster_den_wolf", "terrain_forest", "dungeon_minor", "animal_den_wolf_major"]
            },
            {
                "id": 50012,
                "name": "Half-Moon Mill",
                "desc": "A lumber mill owned by Hert and Hern, a reclusive couple. Rumors persist about their nocturnal activities and connections to darker elements.",
                "tags": ["structure_type_lumber_mill_site", "settlement_minor", "economic_activity_logging_timber", "specific_landmark_type_vampire_coven_minor_potential", "isolated_location", "mystery_local", "terrain_lake_large_nearby"]
            },
            {
                "id": 50013,
                "name": "Granitehall Farm",
                "desc": "A small, hardy farm nestled near the mountains of Falkreath, known for its resilient goats and strong mead.",
                "tags": ["structure_type_farmstead", "economic_activity_farming_livestock", "economic_activity_brewing_mead_ale", "terrain_mountainous", "isolated_location", "settlement_minor"]
            },
            {
                "id": 50014,
                "name": "Shadowed Path Cave",
                "desc": "A dark, winding cave often used by smugglers as a discreet route through Falkreath's forests, or as a den for bears and other forest predators.",
                "tags": ["structure_type_natural_cave", "terrain_forest", "dungeon_minor", "economic_activity_smuggling_route_active_potential", "monster_den_bear_potential", "monster_den_wolf_potential"]
            },
            {
                "id": 50015,
                "name": "Crumbling Border Watch",
                "desc": "The ruins of a small Imperial watchtower near the Cyrodiil border in Falkreath Hold, now overgrown and sometimes used by bandits as a lookout.",
                "tags": ["structure_type_ruined_tower", "military_presence", "terrain_mountainous", "structure_condition_ruined_extensively", "bandit_minor_camp_potential", "cyrodiil_border_region"]
            },
            {
                "id": 50018,
                "name": "South Skybound Watch",
                "desc": "A ruined Nordic watchtower and barrow complex, similar to its northern counterpart, located in the southern mountains of Falkreath Hold. It contains an ancient Word Wall and is guarded by draugr.",
                "tags": ["structure_type_ruined_tower", "nordic_burial_site_major", "specific_landmark_type_word_wall_location", "dungeon_major", "undead_presence_strong", "draugr_heavy", "terrain_mountainous"]
            },
            {
                "id": 50019,
                "name": "Shor's Watchtower",
                "desc": "A ruined watchtower near the border of Falkreath and The Rift, overlooking the road to Shor's Stone. Often occupied by bandits.",
                "tags": ["watchtower_ruined", "bandit_outpost_potential", "roadside_ruin", "strategic_lookout_decayed"]
            },
            {
                "id": 50020,
                "name": "Bleakwind Basin",
                "desc": "A large, open basin in Falkreath Hold, west of Whiterun, known as a traditional gathering place for giants and their mammoth herds.",
                "tags": ["giant_camp_major", "mammoth_herd_grazing", "plains_landmark_open", "neutral_encounter_large_potential"]
            },
            {
                "id": 50021,
                "name": "Shor's Watchtower",
                "desc": "A ruined watchtower near the border of Falkreath and The Rift, overlooking the road to Shor's Stone. Often occupied by bandits.",
                "tags": ["structure_type_ruined_tower", "bandit_minor_camp_potential", "roadside_ruin", "strategic_lookout_decayed"]
            },
            {
                "id": 50022,
                "name": "Bannermist Tower",
                "desc": "A ruined watchtower south of Lake Ilinalta in Falkreath Hold, now occupied by bandits who use it to prey on travelers.",
                "tags": ["watchtower_ruined_bandit", "bandit_camp_tower", "dungeon_minor", "roadside_danger_spot"]
            },
            {
                "id": 50023,
                "name": "Anise's Cabin",
                "desc": "A small, seemingly innocent cabin located near Riverwood, on the edge of Falkreath Hold. Anise is an elderly woman with a hidden cellar revealing her dabbling in witchcraft.",
                "tags": ["cabin_isolated_witch", "secret_cellar_witchcraft", "alchemy_ingredients_cabin", "neutral_encounter_secret_hostile_potential"]
            }
        ]
    },

    # THE REACH
    {
        "id": 6,
        "name": "The Reach",
        "desc": "A wild, rugged, and mountainous region in western Skyrim, dominated by steep cliffs, deep valleys, and ancient Dwemer ruins. It is the heartland of the native Forsworn, who wage a bitter insurgency against Nord rule.", # Emphasized Forsworn conflict
        "tags": ["hold", "mountain_extreme", "dwemer_ruin_heavy", "forsworn_territory_active", "mining_region_silver", "nordic_minority", "breton_reachmen_culture", "rebellion_ongoing"],
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
                "tags": ["city", "dwemer_architecture_ancient", "mountain_city_unique", "markarth", "forsworn_conspiracy_active", "silver_mine_major", "jarls_seat_nord", "imperial_influence_strong", "political_tension"], # Added more tags
                "sub_locations": [
                    {
                        "id": 6001,
                        "name": "Silver-Blood Inn",
                        "desc": "A bustling tavern in Markarth, owned by the influential and often ruthless Silver-Blood family, a common place for rumors, shady deals, and political maneuvering.",
                        "tags": ["tavern", "social", "inn", "intrigue_hub", "silver_blood_family_owned"]
                    },
                    {
                        "id": 6002,
                        "name": "Understone Keep",
                        "desc": "An ancient Dwemer fortification carved into the rock, serving as the Jarl's palace. It also houses a Dwemer museum managed by Calcelmo and provides access to the ruins of Nchuand-Zel.",
                        "tags": ["keep", "government", "dwemer_ruin_integrated", "museum_dwemer", "jarls_seat", "nchuand_zel_access", "calcelmo_research_site"],
                        "sub_locations": [
                            {
                                "id": 60028, # Corrected ID from previous thought process, ensuring it's unique within The Reach
                                "name": "Nchuand-Zel",
                                "desc": "The vast and ancient Dwemer city ruins located directly beneath Understone Keep in Markarth. It is a dangerous labyrinth of crumbling halls, active Dwemer machinery, Falmer, and potentially a slumbering Centurion.",
                                "tags": ["dwemer_ruin_city_subterranean", "dungeon_major_underkeep", "mechanical_constructs_dwemer_heavy", "falmer_presence_deep", "ancient_city_excavation", "markarth_secret_depths"]
                            }
                        ]
                    },
                    {
                        "id": 6003,
                        "name": "Cidhna Mine",
                        "desc": "Markarth's infamous silver mine, which also serves as a brutal prison primarily for accused Forsworn. Conditions are harsh, and escape is said to be impossible.",
                        "tags": ["mine_silver", "prison_harsh", "silver_resource", "forsworn_incarceration", "quest_location_forsworn_conspiracy", "forced_labor"]
                    },
                    {
                        "id": 6004,
                        "name": "Arnleif and Sons Trading Company",
                        "desc": "A general goods store in Markarth, run by Lisbet. It struggles due to competition and Forsworn activity.",
                        "tags": ["shop", "general", "local_business"]
                    },
                    {
                        "id": 6005,
                        "name": "The Hag's Cure",
                        "desc": "Bothela's apothecary shop in Markarth, providing potions, ingredients, and alchemical supplies. Bothela is a wise old woman with knowledge of Reach traditions.",
                        "tags": ["alchemy", "shop", "magic_vendor", "local_herbalist", "reach_lore_knowledge"]
                    },
                    {
                        "id": 6006,
                        "name": "Markarth Market Square",
                        "desc": "An open-air market in the heart of the city where various vendors sell their goods, often under the watchful eye of city guards. Tensions between Nords and Reach natives can sometimes spill over here.",
                        "tags": ["market", "trade", "social_hub", "guard_patrols", "cultural_tension_point"]
                    },
                    {
                        "id": 6007,
                        "name": "Temple of Dibella",
                        "desc": "A grand temple dedicated to Dibella, the goddess of beauty and love, home to several priestesses and the site of the Sybil of Dibella.",
                        "tags": ["temple_major", "religious", "dibella_shrine", "quest_location_dibella", "sacred_site_female_only_inner_sanctum"]
                    },
                    {
                        "id": 6008,
                        "name": "Ghorza's Smithy",
                        "desc": "The workshop of Ghorza gra-Bagol, an Orc blacksmith in Markarth, who values good craftsmanship and offers training.",
                        "tags": ["blacksmith", "shop", "crafting", "orc_craftsman", "skill_trainer_smithing_potential"]
                    },
                    { # Added Smelter
                        "id": 6009,
                        "name": "Markarth Smelter",
                        "desc": "The industrial smelter used to process ore from Cidhna Mine and other regional mining operations.",
                        "tags": ["industrial_facility", "smelter", "mining_process"]
                    }
                ]
            },
            {
                "id": 61,
                "name": "Karthwasten",
                "desc": "A rugged mining village in the Reach, centered around Sanuarach Mine and Fenn's Gulch Mine. It is frequently caught in the crossfire between Markarth's Silver-Blood family interests and Forsworn raids.",
                "tags": ["village", "mining_town", "forsworn_conflict_zone", "resource_silver_contested", "silver_blood_interest"],
                 "sub_locations": [
                    {
                        "id": 6101,
                        "name": "Karthwasten Hall",
                        "desc": "The primary gathering place in Karthwasten, where locals discuss mining rights and Forsworn threats. Often serves as a makeshift inn.",
                        "tags": ["social_hub", "meeting_hall", "community_center", "inn_makeshift"]
                    },
                    {
                        "id": 6102,
                        "name": "Sanuarach Mine",
                        "desc": "A silver mine in Karthwasten, a key source of income for the village but often disrupted by ownership disputes and Forsworn attacks.",
                        "tags": ["mine", "resource_silver", "conflict_point"]
                    },
                    {
                         "id": 6103,
                         "name": "Fenn's Gulch Mine",
                         "desc": "Another mine near Karthwasten, primarily for silver, also vulnerable to local conflicts.",
                         "tags": ["mine", "resource_silver", "dangerous_area"]
                    }
                ]
            },
            {
                "id": 62,
                "name": "Druadach Redoubt",
                "desc": "A major Forsworn encampment and cave system hidden in the mountains southwest of Karthwasten, a formidable stronghold of the Reach's native rebellion.",
                "tags": ["forsworn_stronghold", "cave_system_fortified", "dungeon_major", "rebel_base", "quest_location_forsworn_alliance_potential"]
            },
            {
                "id": 63,
                "name": "Deep Folk Crossing",
                "desc": "An ancient Dwemer bridge spanning a tumultuous river high in the mountains. A breathtaking and perilous relic, rumored to lead to undiscovered ruins.",
                "tags": ["dwemer_bridge_ancient", "ruin_landmark_remote", "scenic_view_dangerous", "exploration_challenge", "undiscovered_ruins_rumor"]
            },
            {
                "id": 64,
                "name": "Dushnikh Yal",
                "desc": "An Orc stronghold in the southwestern Reach, adhering to the ancient Code of Malacath. Known for its skilled warriors, miners, and adherence to tradition.",
                "tags": ["orc_stronghold", "tribal_community", "mountain_settlement_fortified", "mining_community_orichalcum", "warrior_culture_orcish", "malacath_worship"],
                 "sub_locations": [
                    {
                        "id": 6401,
                        "name": "Burguk's Longhouse",
                        "desc": "The longhouse of Chief Burguk, the stern but fair leader of Dushnikh Yal.",
                        "tags": ["government_tribal", "chieftains_hall", "residence_chief"]
                    },
                    {
                        "id": 6402,
                        "name": "Dushnikh Mine (Orichalcum)",
                        "desc": "The stronghold's orichalcum mine, providing valuable ore for Orcish smithing and trade.",
                        "tags": ["mine", "resource_orichalcum", "orc_controlled_mine"]
                    },
                    {
                        "id": 6403,
                        "name": "Gharol's Smithy (Dushnikh Yal)", # Specified location
                        "desc": "The forge of Gharol, the skilled blacksmith of Dushnikh Yal, crafting traditional Orcish arms and armor.",
                        "tags": ["blacksmith", "shop_tribal", "crafting_orcish", "female_orc_smith"]
                    }
                ]
            },
            {
                "id": 65,
                "name": "Blind Cliff Cave",
                "desc": "A cave system north of Markarth, a den for Forsworn ritualists and their hagraven allies.",
                "tags": ["cave", "forsworn_ritual_site", "hagraven_lair", "dungeon_dark_magic"]
            },
            {
                "id": 66,
                "name": "Bruca's Leap Redoubt",
                "desc": "A Forsworn encampment built around a waterfall and river, east of Karthwasten, utilizing the natural defenses of the terrain.",
                "tags": ["forsworn_camp_defensive", "waterfall_location", "dungeon", "river_outpost"]
            },
            {
                "id": 67,
                "name": "Dead Crone Rock",
                "desc": "A ruined tower and Forsworn stronghold west of Markarth, a place of dark magic and a site for a Daedric quest related to Mehrunes' Razor.",
                "tags": ["tower_ruined_forsworn", "forsworn_stronghold", "hagraven_coven", "daedric_artifact_mehrunes_razor_piece", "dungeon_boss_fight"]
            },
            {
                "id": 68,
                "name": "Deepwood Redoubt",
                "desc": "A large Forsworn encampment and Nordic ruin complex northwest of Markarth, serving as a major base and leading to the hagraven lair of Hag's End.",
                "tags": ["forsworn_stronghold_major", "nordic_ruin_integrated", "dungeon_complex", "quest_location_exploration", "hags_end_access"]
            },
            {
                "id": 69,
                "name": "Dragontooth Crater",
                "desc": "An ancient, dormant volcanic crater high in the northern mountains of the Reach. While no dragons have been seen for eras, old tales speak of it as a nesting site.", # Adjusted for no active dragons
                "tags": ["volcanic_crater_ancient", "mountain_peak_remote", "dungeon_potential", "dragon_lore_ancient_site"] # Removed "dragon_lair"
            },
            {
                "id": 60001,
                "name": "Hag Rock Redoubt",
                "desc": "A Forsworn-occupied ruin south of Markarth, a constant threat to travelers and caravans in the area.",
                "tags": ["forsworn_camp", "ruin_fortified", "dungeon", "bounty_target_potential"]
            },
            {
                "id": 60002,
                "name": "Hag's End",
                "desc": "A ruined tower accessible through Deepwood Redoubt, home to powerful hagravens and an ancient Word Wall.",
                "tags": ["tower_ruined_hagraven", "hagraven_lair_powerful", "dungeon_boss", "dragon_word_ancient", "quest_location"]
            },
            {
                "id": 60003,
                "name": "Karthspire", # Changed from Karthspire Camp to the mountain itself for Sky Haven Temple context
                "desc": "A towering, craggy mountain in the Reach, infamous for its large Forsworn presence at its base, guarding the hidden ascent to ancient ruins.",
                "tags": ["mountain_landmark", "forsworn_territory_heavy", "ancient_ruins_summit_rumor", "dangerous_ascent"]
            },
            {
                "id": 60004,
                "name": "Kolskeggr Mine",
                "desc": "A rich gold mine east of Markarth, currently abandoned or lightly worked due to frequent and brutal Forsworn attacks that have driven off miners.",
                "tags": ["mine_gold_rich", "forsworn_conflict_severe", "quest_location_reclaim", "abandoned_due_to_danger", "resource_gold"]
            },
            {
                "id": 60005,
                "name": "Left Hand Mine",
                "desc": "An iron mine located just outside Markarth, owned by Skaggi Scar-Face, providing steady work for the town.",
                "tags": ["mine_iron", "resource_iron", "mining_town_minor", "local_employer"]
            },
            {
                "id": 60006,
                "name": "Lost Valley Redoubt",
                "desc": "A major Forsworn encampment built around scenic waterfalls and ancient Nordic structures, home to powerful Forsworn Briarhearts and an ancient Word Wall.",
                "tags": ["forsworn_stronghold_scenic", "waterfall_location_defensive", "nordic_ruin_integrated", "dungeon_major", "dragon_word_ancient", "briarheart_presence"]
            },
            {
                "id": 60007,
                "name": "Reachcliff Cave",
                "desc": "A cave south of Markarth. While sometimes occupied by undead, it's also known as a site for a dark Daedric ritual involving Namira.",
                "tags": ["cave", "undead_potential", "daedric_quest_namira", "dungeon", "ritual_site_dark"]
            },
            {
                "id": 60008,
                "name": "Reachwind Eyrie",
                "desc": "A ruined Dwemer tower on a clifftop overlooking the Karth River. It's often used as a lookout or minor outpost by Forsworn or bandits.",
                "tags": ["dwemer_tower_ruined", "forsworn_outpost_potential", "bandit_lookout_potential", "scenic_view_strategic"]
            },
            {
                "id": 60009,
                "name": "Red Eagle Redoubt",
                "desc": "A large Forsworn camp and Nordic ruin complex, central to the legend of the ancient Reach hero, Red Eagle. Many Forsworn revere this site.",
                "tags": ["forsworn_camp_historic", "nordic_ruin_integrated", "dungeon_major", "legendary_figure_red_eagle", "quest_location_lore"]
            },
            {
                "id": 60010,
                "name": "Sky Haven Temple", # Corrected State
                "desc": "An ancient, forgotten temple complex high in the Karthspire mountain, rumored to have once been a sanctuary for a lost order of dragon hunters. Its exact location is a mystery, likely hidden behind perilous Forsworn territory and natural barriers.",
                "tags": ["historic_temple_lost", "secret_location_rumored", "dragon_lore_site_ancient", "mountain_stronghold_ruined", "ancient_ruin", "blades_history_rumored"],
                "sub_locations": [
                    {
                        "id": 600101,
                        "name": "Alduin's Wall",
                        "desc": "A massive, ancient carved wall rumored to exist deep within the Karthspire ruins. Its intricate carvings are believed by some to depict ancient dragon myths or forgotten histories. Its true meaning is lost to time.",
                        "tags": ["historic_artifact_legendary", "ancient_carving_prophetic_rumor", "dragon_myth_depiction"]
                    }
                    # Armory might not be known or accessible yet
                ]
            },
            {
                "id": 60011,
                "name": "Soljund's Sinkhole",
                "desc": "A moonstone mine east of Markarth that has recently broken into a draugr-infested Nordic ruin, causing terror among the miners.",
                "tags": ["mine_moonstone", "nordic_ruin_breach_recent", "undead_infestation", "dungeon", "resource_moonstone_dangerous"]
            },
            {
                "id": 60012,
                "name": "Old Hroldan Inn",
                "desc": "An ancient inn located in the Reach, south of Soljund's Sinkhole. Legends claim Tiber Septim himself once stayed here, and a ghostly presence is sometimes felt.",
                "tags": ["inn_historic", "tavern_remote", "historic_site_tiber_septim", "ghost_quest_potential", "isolated_lodging"]
            },
            # New Reach Locations
            {
                "id": 60013,
                "name": "Mor Khazgur",
                "desc": "An Orc stronghold in the northwestern Reach, known for its skilled hunters and fierce warriors, led by Chief Larak.",
                "tags": ["orc_stronghold", "tribal_community", "mountain_settlement_fortified", "hunting_culture_orcish", "warrior_culture_orcish", "malacath_worship"],
                "sub_locations": [
                    {
                        "id": 600131,
                        "name": "Larak's Longhouse",
                        "desc": "The longhouse of Chief Larak, leader of Mor Khazgur.",
                        "tags": ["government_tribal", "chieftains_hall", "residence_chief"]
                    },
                    {
                        "id": 600132,
                        "name": "Mor Khazgur Mine (Orichalcum)",
                        "desc": "The stronghold's orichalcum mine, crucial for their smithing and economy.",
                        "tags": ["mine", "resource_orichalcum", "orc_controlled_mine"]
                    }
                ]
            },
            {
                "id": 60014,
                "name": "Purewater Run",
                "desc": "A small, hidden cave system behind a waterfall, known for its remarkably clear stream and rare fish. Sometimes used by outlaws as a discreet meeting place.",
                "tags": ["cave_hidden_waterfall", "natural_spring_pristine", "rare_fish_source", "outlaw_meeting_spot_potential", "dungeon_minor"]
            },
            {
                "id": 60015,
                "name": "Reachwind Crag",
                "desc": "A series of treacherous, wind-swept cliffs and narrow paths, home to territorial hagravens and offering perilous views over the Karth River valley.",
                "tags": ["cliff_network", "hagraven_territory", "dangerous_terrain", "scenic_vista_perilous", "windy_location"]
            },
            {
                "id": 60016,
                "name": "Reachwater Rock",
                "desc": "A cave system behind a waterfall in the Reach, containing ancient Nordic ruins and playing a part in the legend of the Gauldur Amulet.",
                "tags": ["cave_waterfall_hidden", "nordic_ruin_interior", "dungeon", "quest_location_artifact", "gauldur_amulet_related", "ancient_magic_site"]
            },
            {
                "id": 60017,
                "name": "Four Skull Lookout",
                "desc": "A ruined Nordic tower and small barrow complex in the Reach, often occupied by bandits or Forsworn, guarding an ancient Word Wall.",
                "tags": ["nordic_ruin_tower", "barrow_minor", "bandit_outpost_potential", "forsworn_camp_potential", "dragon_word_ancient", "dungeon_minor"]
            },
            {
                "id": 60018,
                "name": "Karthside Hovel",
                "desc": "A tiny, impoverished hamlet of Reach natives clinging to the cliffs near the Karth River, often harassed by both Forsworn and Markarth guards.",
                "tags": ["village_reach_native_poor", "cliffside_dwelling_precarious", "forsworn_sympathizers_potential", "conflict_zone_civilian"]
            },
            {
                "id": 60019,
                "name": "Eagles' Nest Farm",
                "desc": "A very remote and high-altitude farm in The Reach, accessible only by treacherous paths, known for its hardy livestock and reclusive owners.",
                "tags": ["farm_mountain_extreme_remote", "agriculture_high_altitude", "isolated_community_self_sufficient", "dangerous_access_route"]
            },
            {
                "id": 60020,
                "name": "Cliffside Crevice",
                "desc": "A narrow cave system hidden within the steep cliffs of The Reach, a perfect natural hideout for Forsworn scouts or a den for cliff-dwelling creatures.",
                "tags": ["cave_cliffside_narrow", "dungeon_minor", "forsworn_hideout_potential_scout", "creature_den_cliff", "natural_fortification"]
            },
            {
                "id": 60021,
                "name": "Ruined Dwemer Outpost (Minor)",
                "desc": "The scattered, collapsed remains of a small Dwemer outpost or monitoring station, likely picked clean of valuables long ago but still hinting at their ancient presence.",
                "tags": ["dwemer_ruin_minor_outpost", "historic_site_dwemer_small", "ancient_technology_remnants", "exploration_point_minor_lore"]
            },
            {
                "id": 60022,
                "name": "Fort Sungard (Contested Ruin)",
                "desc": "A large, strategically important fort in the Reach, now mostly in ruins. It's a frequent point of conflict, with Forsworn, bandits, or even small Imperial/Stormcloak scouting parties vying for control of its crumbling walls.",
                "tags": ["fort_ruined_major", "dungeon_major", "forsworn_conflict_zone", "bandit_stronghold_potential", "contested_territory_military", "historic_fort_skyrim"]
            },
            {
                "id": 60023,
                "name": "Old Gods' Clearing (Reach Wilderness)",
                "desc": "A secluded clearing deep in the Reach wilderness, marked by weathered, primitive stone carvings and arrangements hinting at ancient Reach native worship, pre-dating even the Nords.",
                "tags": ["shrine_ancient_native_reach", "historic_site_religious_primitive", "forsworn_sacred_site_potential", "wilderness_landmark_hidden", "ritual_site_old_gods"]
            },
            {
                "id": 60024,
                "name": "Briarheart Warren",
                "desc": "A small, thorny cave system hidden in the rugged hills of the Reach, rumored to be a place where Forsworn Briarhearts are created or where they retreat to recover.",
                "tags": ["cave_forsworn_ritual", "dungeon_minor", "briarheart_creation_site_rumor", "forsworn_hideout_secret", "dangerous_flora_thorns"]
            },
            {
                "id": 60025,
                "name": "The Lover Stone",
                "desc": "An ancient Standing Stone found in the rugged hills east of Markarth, said to grant those who touch it a quicker aptitude in all endeavors.",
                "tags": ["standing_stone", "buff_skill_learning_all", "reach_wilderness_shrine", "ancient_magic_site"]
            },
            {
                "id": 60026,
                "name": "Valthume",
                "desc": "An ancient and sprawling Nordic ruin deep in the mountains of The Reach, southeast of Markarth. It is the burial place of the Dragon Priest Hevnoraak and a site of significant old power.",
                "tags": ["nordic_ruin_major", "dungeon_large_complex", "dragon_priest_tomb_hevnoraak", "undead_heavy_powerful", "ancient_magic_site", "dragon_word_ancient", "quest_location_dragon_priest"]
            },
            {
                "id": 60029,
                "name": "Rebel's Cairn",
                "desc": "An ancient cairn in the Reach, west of Karthwasten, said to be the burial site of a legendary Forsworn hero. It is a sacred place for some Reachmen and may hold ancient secrets or guardians.",
                "tags": ["cairn_ancient_forsworn", "forsworn_sacred_site", "dungeon_minor_historic", "undead_guardian_potential", "reach_lore_heroic_figure"]
            },
            {
                "id": 60030,
                "name": "Blind Cliff Bastion",
                "desc": "A ruined Nordic tower complex built into the cliffs of the Reach, now a formidable Forsworn stronghold. Distinct from Blind Cliff Cave.",
                "tags": ["nordic_ruin_tower_complex", "forsworn_stronghold_cliffside", "dungeon_major_vertical", "dangerous_approach_forsworn", "reach_fortification_native"]
            }
        ]
    },

    # EASTMARCH
    {
        "id": 7,
        "name": "Eastmarch",
        "desc": "A harsh, volcanic hold in eastern Skyrim, dominated by the ancient city of Windhelm, seat of Jarl Ulfric Stormcloak and a center of growing rebellion. Known for its hot springs, giants, and fierce Nordic traditions.", # Adjusted capital status
        "tags": ["hold", "volcanic_tundra", "nordic_stronghold_ancient", "stormcloak_hotbed", "hot_springs_region", "giant_country", "imperial_conflict_brewing", "morrowind_border"], # Adjusted tags
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
                "tags": ["city", "historic_capital_nordic", "nordic_architecture_ancient", "windhelm", "historic_city_major", "stormcloak_presence_strong", "dunmer_quarter_segregated", "argonian_assemblage_docks", "imperial_conflict_focus", "jarls_seat_ulfric"],
                "sub_locations": [
                    {
                        "id": 7001,
                        "name": "Candlehearth Hall",
                        "desc": "A historic and popular tavern in Windhelm, known for its large central hearth that has burned for centuries, and its warm atmosphere.",
                        "tags": ["tavern", "social", "inn", "historic_building", "rumor_mill"]
                    },
                    {
                        "id": 7002,
                        "name": "Oengul's Smithy",
                        "desc": "The workshop of Oengul War-Anvil and his apprentice Hermir Strong-Heart, providing quality arms and armor to the Nords of Windhelm.",
                        "tags": ["blacksmith", "shop", "crafting_weapons_armor"]
                    },
                    {
                        "id": 7003,
                        "name": "Palace of the Kings",
                        "desc": "The formidable ancient seat of Ysgramor's dynasty, now serving as Jarl Ulfric Stormcloak's residence and military headquarters for his growing faction.",
                        "tags": ["government", "jarls_seat", "military_hq_stormcloak", "historic_palace_ysgramor", "stormcloak_leader_residence", "political_center_rebellion"]
                    },
                    {
                        "id": 7004,
                        "name": "The White Phial",
                        "desc": "An esteemed apothecary shop run by the aging and ailing Nurelion, who is obsessed with finding the legendary artifact of the same name.",
                        "tags": ["alchemy", "shop", "magic_vendor", "quest_location_artifact_white_phial", "unique_item_lore"]
                    },
                    {
                        "id": 7005,
                        "name": "Sadri's Used Wares",
                        "desc": "Revyn Sadri's shop in the Dunmer Gray Quarter, offering a variety of second-hand goods and curiosities. He strives to be an honest merchant amidst hardship.",
                        "tags": ["shop", "general", "dunmer_business", "gray_quarter_shop"]
                    },
                    {
                        "id": 7006,
                        "name": "Windhelm Market Square",
                        "desc": "A bustling open-air market with various stalls near the city gates, offering food, goods, and services. The atmosphere can be tense due to political climate.",
                        "tags": ["market", "trade", "social_hub_tense"]
                    },
                    {
                        "id": 7007,
                        "name": "Temple of Talos (Windhelm)",
                        "desc": "A place of clandestine Talos worship, highly significant given the Stormcloak cause and the Thalmor's ban. Attended by those loyal to traditional Nord beliefs.",
                        "tags": ["temple_secret", "religious", "talos_worship_banned", "stormcloak_ideology_center", "thalmor_target_potential"]
                    },
                    {
                        "id": 7008,
                        "name": "Gray Quarter (Dunmer District)",
                        "desc": "The segregated district where most of Windhelm's Dunmer refugee population resides, often facing prejudice and harsh living conditions.",
                        "tags": ["district_dunmer_refugee", "social_tension_high", "poverty_stricken_area", "cultural_enclave"]
                    },
                    {
                        "id": 7009,
                        "name": "Argonian Assemblage (Docks)",
                        "desc": "The dockside area where Windhelm's Argonian dockworkers are forced to live in cramped and poor conditions, working for low wages.",
                        "tags": ["district_argonian_laborer", "docks_area", "social_tension_high", "worker_exploitation"]
                    },
                    {
                        "id": 7010,
                        "name": "Aretino Residence",
                        "desc": "The home of Aventus Aretino, a young boy attempting to perform the Black Sacrament to contact the Dark Brotherhood after the death of his mother.",
                        "tags": ["residence", "dark_brotherhood_quest_start_rumor", "orphan_distraught"]
                    },
                    {
                        "id": 7011,
                        "name": "Hall of the Dead (Windhelm)",
                        "desc": "Windhelm's catacombs for honoring the dead, maintained by Helgird, a priestess of Arkay, who also deals with the city's recent murder victims.",
                        "tags": ["catacombs", "religious", "arkay_shrine", "murder_investigation_connection"]
                    },
                    { # Added Windhelm Port
                        "id": 7012,
                        "name": "Windhelm Port",
                        "desc": "The icy docks of Windhelm, a vital hub for trade with northern Tamriel and Solstheim, despite the harsh conditions. Home to the East Empire Company office.",
                        "tags": ["docks", "port_major", "trade_hub_northern", "east_empire_company_office", "ship_travel_solstheim_potential"]
                    }
                ]
            },
            {
                "id": 71,
                "name": "Kynesgrove",
                "desc": "A small, industrious mining village on the slopes of the volcanic tundra, known for its malachite mine. It is also situated near an ancient dragon burial site, a fact known to few.", # Removed recent dragon trouble
                "tags": ["village", "mining", "resource_malachite", "dragon_burial_site_nearby_ancient"], # Adjusted tag
                 "sub_locations": [
                    {
                        "id": 7101,
                        "name": "Braidwood Inn",
                        "desc": "The local inn in Kynesgrove, providing food, lodging, and news to miners and travelers.",
                        "tags": ["inn", "tavern", "social"]
                    },
                    {
                        "id": 7102,
                        "name": "Steamscorch Mine",
                        "desc": "The malachite mine that is the lifeblood of Kynesgrove, a source of valuable ore.", # Removed dragon trouble
                        "tags": ["mine", "resource_malachite"]
                    }
                ]
            },
            {
                "id": 72,
                "name": "Fort Amol",
                "desc": "A strategic fort in Eastmarch, currently held by Stormcloak-aligned soldiers, guarding the pass to Whiterun. It has seen skirmishes in the past.",
                "tags": ["fort", "military", "stormcloak_garrison", "dungeon_potential", "strategic_pass_defense"] # Changed to Stormcloak given Windhelm's status
            },
            {
                "id": 73,
                "name": "Eldergleam Sanctuary",
                "desc": "A sacred, tranquil grove hidden in Eastmarch, home to the ancient and revered Eldergleam tree. A place of pilgrimage and natural wonder, protected by nature spirits.",
                "tags": ["sacred_grove_ancient", "kynareth_shrine_associated", "unique_tree_magical", "quest_location_nature", "natural_wonder", "spriggan_guardians_potential"]
            },
            {
                "id": 74,
                "name": "Narzulbur",
                "desc": "An Orc stronghold in Eastmarch, situated near a rich ebony mine. They adhere strictly to the Code of Malacath and are wary of outsiders.",
                "tags": ["orc_stronghold_isolated", "tribal_community_orcish", "mining_community_ebony_rich", "warrior_culture_strong", "malacath_worship_strict"],
                "sub_locations": [
                    {
                        "id": 7401,
                        "name": "Mauhulakh's Longhouse", # More specific name
                        "desc": "The longhouse of Chief Mauhulakh, stern leader of Narzulbur.",
                        "tags": ["government_tribal", "chieftains_hall", "residence_chief"]
                    },
                    {
                        "id": 7402,
                        "name": "Gloombound Mine (Ebony)",
                        "desc": "Narzulbur's productive ebony mine, a source of great wealth and Orcish pride, but also dangers from deep within.",
                        "tags": ["mine_ebony_major", "resource_ebony_valuable", "orc_controlled_mine", "dungeon_mine_extension_potential"]
                    }
                ]
            },
            {
                "id": 75,
                "name": "Ansilvund",
                "desc": "A Nordic ruin in Eastmarch, haunted by powerful draugr and connected to a tragic love story and necromantic rituals performed by Lu'ah Al-Skaven.",
                "tags": ["nordic_ruin_haunted", "dungeon_major", "undead_powerful", "necromancer_lair_active", "quest_location_story", "dragon_word_ancient"]
            },
            {
                "id": 76,
                "name": "Bonestrewn Crest",
                "desc": "A mountain peak in the southern volcanic region of Eastmarch, an ancient dragon lair and site of a Word Wall, though no dragon has roosted here for centuries.", # Adjusted for no active dragons
                "tags": ["dragon_lair_ancient_empty", "dragon_word_ancient", "mountain_peak_volcanic", "dungeon_lair_potential"]
            },
            {
                "id": 77,
                "name": "Cronvangr Cave",
                "desc": "A large cave system in the hot springs region of Eastmarch, heavily infested with giant frostbite spiders. Rumors also speak of a hidden vampire presence within.",
                "tags": ["cave_large", "spider_nest_major", "vampire_lair_hidden_potential", "dungeon_dangerous", "hot_springs_area_cave"]
            },
            {
                "id": 78,
                "name": "Darkwater Crossing",
                "desc": "A small mining settlement on the Darkwater River, primarily focused on corundum ore. A mix of Nords and Argonians work and live here.",
                "tags": ["village_minor", "mining_corundum", "resource_corundum", "argonian_presence_workers", "river_settlement"],
                "sub_locations": [
                    {
                        "id": 7801,
                        "name": "Goldenrock Mine",
                        "desc": "The corundum mine that supports Darkwater Crossing, known for its rich veins.",
                        "tags": ["mine", "resource_corundum"]
                    }
                ]
            },
            {
                "id": 79,
                "name": "Gallows Rock",
                "desc": "A ruined fort southwest of Windhelm, now serving as a major stronghold for the Silver Hand, hunters of werewolves. A dangerous place for any lycanthrope.",
                "tags": ["fort_ruined_occupied", "silver_hand_stronghold", "companions_quest_conflict", "dungeon_enemy_base", "werewolf_hunters"]
            },
            {
                "id": 70001,
                "name": "Gloomreach",
                "desc": "A dark and winding cave system in the southern mountains of Eastmarch, often inhabited by Falmer, Chaurus, or other dangerous subterranean creatures.",
                "tags": ["cave_dangerous", "falmer_den_potential", "chaurus_nest_potential", "dungeon_dark"]
            },
            {
                "id": 70002,
                "name": "Lost Knife Hideout",
                "desc": "A large cave system serving as a major bandit hideout, located near the border with The Rift. Known for its ruthless gang, the 'Lost Knife' bandits.",
                "tags": ["cave_extensive", "bandit_stronghold_major", "dungeon_large_gang", "quest_location_bounty_high_value"]
            },
            {
                "id": 70003,
                "name": "Mixwater Mill",
                "desc": "A lumber mill on the White River in Eastmarch, run by Gilfre. A quiet spot, but travelers sometimes report strange noises from the nearby woods at night.",
                "tags": ["lumber_mill", "settlement_minor", "resource_wood", "river_location", "wilderness_edge_unease"]
            },
            {
                "id": 70004,
                "name": "Morvunskar",
                "desc": "A ruined fort south of Windhelm, now occupied by hostile mages. During particular revelries, a portal to Sanguine's realm of Oblivion might be found here.",
                "tags": ["fort_ruined_magic", "mage_lair_hostile", "daedric_quest_sanguine", "dungeon", "oblivion_portal_temporary"]
            },
            {
                "id": 70005,
                "name": "Refugees' Rest",
                "desc": "A small, ruined Nordic structure east of Windhelm, marking a somber historical event related to the Night of Tears or similar ancient tragedy. Often haunted by sorrowful spirits.",
                "tags": ["nordic_ruin_minor_historic", "historic_marker_somber", "ghost_encounter_sorrowful", "ancient_tragedy_site"]
            },
            {
                "id": 70006,
                "name": "Riverside Shack",
                "desc": "A small, isolated shack on the banks of the White River, sometimes home to a reclusive fisherman, a desperate poacher, or even a territorial creature.",
                "tags": ["hut_isolated_river", "hermit_dwelling_potential", "poacher_camp_potential", "monster_lair_minor_potential"]
            },
            {
                "id": 70007,
                "name": "Stony Creek Cave",
                "desc": "A cave in the southern part of Eastmarch's volcanic tundra, inhabited by bandits who have discovered a valuable alchemical ingredient deep within - Finn's Lute for the Bards College.",
                "tags": ["cave", "bandit_lair_resourceful", "dungeon", "alchemy_ingredient_cave_unique", "bards_college_quest_item"]
            },
            {
                "id": 70008,
                "name": "Traitor's Post",
                "desc": "A small, abandoned shack east of Windhelm, rumored to have been used by outlaws or spies. It's often a meeting point for clandestine activities.",
                "tags": ["hut_abandoned_suspicious", "bandit_outpost_potential", "spy_rendezvous_rumor", "hidden_cache_potential"]
            },
            {
                "id": 70009,
                "name": "Uttering Hills Cave",
                "desc": "A cave system southwest of Windhelm, serving as a hideout for a group of Summerset Shadows, Altmer bandits.",
                "tags": ["cave", "bandit_hideout_altmer", "dungeon", "summerset_shadows_lair"]
            },
            {
                "id": 70010,
                "name": "Witchmist Grove",
                "desc": "A mystical grove in the southern hot springs region of Eastmarch, home to unique flora, spriggans, and possibly a reclusive hagraven or witch.",
                "tags": ["grove_magical", "spriggan_den_strong", "hagraven_lair_potential", "hot_springs_area_enchanted", "alchemy_ingredients_rare", "ritual_site_potential"]
            },
            # New Eastmarch Locations
            {
                "id": 70013,
                "name": "Cragwallow Slope",
                "desc": "A dangerous, rocky slope in the volcanic tundra, known for its frequent rockfalls and as a nesting ground for cliff racers or other aerial predators if they were native.", # Adjusted for Skyrim creatures
                "tags": ["volcanic_slope", "dangerous_terrain_rockfall", "monster_den_cliff_creatures", "wilderness_hazard"]
            },
            {
                "id": 70014,
                "name": "Steamcrag Camp",
                "desc": "A large camp of giants and mammoths situated in the hot springs region of Eastmarch, generally peaceful unless provoked.",
                "tags": ["giant_camp_major", "mammoth_herd", "hot_springs_area", "neutral_encounter_large", "volcanic_tundra_settlement"]
            },
            {
                "id": 70015,
                "name": "Abandoned Lodge of the Nine Holds",
                "desc": "A once-grand hunting lodge in the eastern forests, now fallen into disrepair and rumored to be haunted by its former occupants or used by bandits.",
                "tags": ["lodge_abandoned", "ruin_hunting", "haunted_potential", "bandit_lair_potential", "forest_isolated"]
            },
            {
                "id": 70016,
                "name": "Witchmist Grove Cave",
                "desc": "A damp, mossy cave system connected to or near Witchmist Grove, likely sharing its magical and dangerous nature, possibly extending the spriggan or hagraven territory.",
                "tags": ["cave_magical", "spriggan_den_extension", "hagraven_lair_nearby", "dungeon_natural_magic", "hot_springs_area_cave"]
            },
            {
                "id": 70017,
                "name": "Dunmer Refugee Camp (Eastmarch)",
                "desc": "A small, struggling camp of Dunmer refugees who have fled Morrowind, located in a less hospitable part of Eastmarch, seeking safety but finding hardship.",
                "tags": ["refugee_camp_dunmer", "settlement_makeshift_poor", "social_issue_displacement", "morrowind_border_region_life"]
            },
            {
                "id": 70018,
                "name": "Ashfall Farm",
                "desc": "A small, struggling farm in the volcanic tundra of Eastmarch, where hardy Nords attempt to grow crops despite the harsh ashfall and geothermal activity.",
                "tags": ["farm_volcanic_tundra", "agriculture_struggling_harsh_environment", "ashfall_impacted_settlement", "geothermal_proximity"]
            },
            {
                "id": 70019,
                "name": "Boiling Springs Camp",
                "desc": "A tiny settlement of hunters and trappers who have made their camp near Eastmarch's famous hot springs, utilizing the warm waters and local game.",
                "tags": ["hunter_camp_hot_springs", "trapper_outpost_volcanic", "settlement_minor_resourceful", "geothermal_feature_nearby"]
            },
            {
                "id": 70020,
                "name": "Sulfur-Spring Grotto",
                "desc": "A small cave system near Eastmarch's volcanic hot springs, filled with sulfurous fumes and often home to creatures adapted to the heat, or desperate outcasts.",
                "tags": ["cave_volcanic_hot_springs", "dungeon_minor", "geothermal_feature_cave", "monster_den_heat_adapted", "outcast_shelter_potential"]
            },
            {
                "id": 70021,
                "name": "Ruins of Old Amol",
                "desc": "The scattered, ancient foundations and a few crumbling walls of a settlement that predated Fort Amol, now mostly reclaimed by the volcanic tundra.",
                "tags": ["nordic_ruin_minor_settlement", "historic_site_ancient_village", "archaeology_interest_minor", "volcanic_tundra_ruin"]
            },
            {
                "id": 70022,
                "name": "Shrine of Mara (Eastmarch Hot Springs)",
                "desc": "A small, secluded shrine to Mara, Goddess of Love, nestled among the steaming vents and warm pools of Eastmarch's hot springs. A place of unexpected serenity.",
                "tags": ["shrine_aedric_outdoor", "mara_shrine", "religious_site_minor", "hot_springs_location", "tranquil_spot"]
            },
            {
                "id": 70023,
                "name": "Shrine of Malacath (Narzulbur Outskirts)",
                "desc": "A crude, outdoor shrine dedicated to Malacath, located a short distance from the Orc stronghold of Narzulbur. Used by Orcs for private offerings or rituals.",
                "tags": ["shrine_daedric_outdoor", "malacath_shrine_orcish", "orc_stronghold_related", "ritual_site_minor", "tribal_worship_site"]
            },
            {
                "id": 70024,
                "name": "Riverside Shack (Eastmarch Volcanic Plains)",
                "desc": "An isolated, ramshackle hut on the banks of a river cutting through Eastmarch's volcanic plains. Could be home to a reclusive fisherman or a desperate outcast.",
                "tags": ["hut_isolated_river", "volcanic_plains_dwelling", "hermit_refuge_potential", "fishing_spot_rough"]
            },
            {
                "id": 70025,
                "name": "Volcanic Vent Cave",
                "desc": "A small cave system formed near an active volcanic vent, filled with heated air and strange mineral deposits. May be home to fire atronachs or other heat-adapted creatures.",
                "tags": ["cave_volcanic_vent", "dungeon_minor", "geothermal_feature_cave", "monster_den_fire_elemental", "rare_mineral_source_potential"]
            },
            {
                "id": 70026,
                "name": "The Atronach Stone",
                "desc": "A Standing Stone located in the volcanic tundra of Eastmarch, south of Windhelm. It grants a larger pool of magicka but hinders natural regeneration, forcing reliance on absorption or potions.",
                "tags": ["standing_stone", "buff_magicka_increased", "debuff_magicka_regen_slowed", "magic_absorption_potential", "volcanic_tundra_landmark"]
            },
            {
                "id": 70027,
                "name": "Kagrenzel",
                "desc": "A remote Dwemer ruin in the mountains of Eastmarch, known for its peculiar entrance trap that drops explorers into a deep chasm leading to a Falmer-infested cave system.",
                "tags": ["dwemer_ruin_remote", "dungeon_trap_entrance_unique", "falmer_den_connected_cave", "dangerous_exploration_dwemer", "unique_dwemer_mechanism"]
            },
            {
                "id": 70028,
                "name": "Mistwatch",
                "desc": "A ruined fort in southern Eastmarch, overlooking the road to The Rift. It is currently occupied by a band of bandits led by a charismatic chief, and is connected to a local family's tragedy.",
                "tags": ["fort_ruined_bandit", "bandit_stronghold_story", "dungeon_fort", "quest_location_family_rescue", "strategic_overlook_ruined"]
            },
            {
                "id": 70029,
                "name": "Mara's Eye Pond",
                "desc": "A small, tranquil pond in Eastmarch, west of Morvunskar. Beneath its surface lies the entrance to Mara's Eye Den, a cave often used by vampires or other creatures.",
                "tags": ["pond_landmark_tranquil", "cave_entrance_hidden_underwater", "vampire_lair_potential_pond", "natural_beauty_spot_deceptive"],
                "sub_locations": [
                    {
                        "id": 700291,
                        "name": "Mara's Eye Den",
                        "desc": "A damp cave system accessible from Mara's Eye Pond, often serving as a den for vampires or other creatures seeking a hidden lair.",
                        "tags": ["cave_vampire_lair", "dungeon_minor", "monster_den_hidden", "underwater_access"]
                    }
                ]
            },
            {
                "id": 70030,
                "name": "Abandoned Prison",
                "desc": "A crumbling, forgotten prison in the wilds of Eastmarch, its cells now empty or home to desperate squatters, bandits, or restless spirits of former inmates.",
                "tags": ["ruin_prison_abandoned", "dungeon_minor_eerie", "bandit_lair_potential_prison", "haunted_potential_inmates", "historic_site_justice_decayed"]
            }
        ]
    },

    # HAAFINGAR
    {
        "id": 8,
        "name": "Haafingar",
        "desc": "A strategic coastal hold in northwestern Skyrim, dominated by the majestic capital city of Solitude. It is the primary Imperial stronghold in Skyrim and a vital hub for maritime trade.",
        "tags": ["hold", "coastal_major", "imperial_stronghold_primary", "maritime_trade_hub", "nordic_culture_imperialized", "solitude_capital_skyrim", "bards_college_location", "thalmor_presence_notable"], # Added Thalmor presence
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
                "tags": ["city_capital_skyrim", "imperial_city_major", "solitude", "wealth_power_center", "imperial_presence_dominant", "bards_college", "major_port_sea", "architecture_grand_imperial", "high_king_seat"],
                "sub_locations": [
                    {
                        "id": 8001,
                        "name": "Blue Palace",
                        "desc": "The opulent palace residence of High King Torygg and his court. A center of Imperial administration and Skyrim's nobility.", # Updated Jarl
                        "tags": ["palace_royal", "government_skyrim", "high_king_residence", "imperial_court_skyrim", "noble_gatherings"]
                    },
                    {
                        "id": 8002,
                        "name": "Castle Dour",
                        "desc": "A robust Imperial fortification within Solitude, serving as the primary headquarters of the Imperial Legion in Skyrim under the command of a high-ranking Legate (General Tullius not yet arrived or in overall command).", # Adjusted for Tullius
                        "tags": ["fort_major_city", "military_hq_imperial_legion", "imperial_legion_base_skyrim", "armory_barracks"]
                    },
                    {
                        "id": 8003,
                        "name": "The Winking Skeever",
                        "desc": "A popular and well-known tavern in Solitude, frequented by locals, travelers, merchants, and a certain boastful mercenary named Gulum-Ei.",
                        "tags": ["tavern", "social_hub_popular", "inn_city", "quest_giver_potential", "rumor_source"]
                    },
                    {
                        "id": 8004,
                        "name": "Bits and Pieces",
                        "desc": "Sayma's general goods store in Solitude, offering a wide variety of items, from common supplies to imported novelties.",
                        "tags": ["shop_general_goods", "trade_variety"]
                    },
                    {
                        "id": 8005,
                        "name": "Angeline's Aromatics",
                        "desc": "An apothecary shop run by Angeline Morrard, selling potions, ingredients, and alchemical supplies. Angeline is often concerned about her daughter serving in the Legion.",
                        "tags": ["alchemy_shop", "magic_vendor_potions", "local_herbalist", "family_concerns"]
                    },
                    {
                        "id": 8006,
                        "name": "Radiant Raiment",
                        "desc": "A fine clothing store run by Taarie and Endarie, Altmer sisters offering fashionable attire and tailoring services, though known for their haughty attitudes.",
                        "tags": ["shop_clothing_fine", "tailor_high_fashion", "altmer_business"]
                    },
                    {
                        "id": 8007,
                        "name": "Fletcher",
                        "desc": "Fihada's shop specializing in bows, arrows, and other archery supplies, catering to hunters and soldiers alike.",
                        "tags": ["shop_archery_specialty", "archery_vendor", "crafting_archery_supplies"]
                    },
                    {
                        "id": 8008,
                        "name": "Solitude Blacksmith (Beirand)",
                        "desc": "Beirand's smithy, located near Castle Dour, providing weapons, armor, and smithing services to the Legion and citizens.",
                        "tags": ["blacksmith_city", "shop_weapons_armor", "crafting_smithing"]
                    },
                    {
                        "id": 8009,
                        "name": "Bards College",
                        "desc": "A renowned institution dedicated to preserving Skyrim's history and fostering the talents of bards, musicians, and performers. They hold an annual festival, the Burning of King Olaf.",
                        "tags": ["college_arts", "guild_bards", "learning_center_music_lore", "historic_institution", "quest_line_bards_college", "festival_king_olaf"]
                    },
                    {
                        "id": 8010,
                        "name": "Temple of the Divines (Solitude)",
                        "desc": "A grand temple in Solitude dedicated to the worship of all Eight Divines (Talos worship is suppressed but may occur secretly). A center of religious life and Imperial faith.",
                        "tags": ["temple_major_divines", "religious_center_imperial", "eight_divines_shrines", "talos_worship_suppressed", "wedding_location"]
                    },
                    {
                        "id": 8011,
                        "name": "Solitude Docks",
                        "desc": "The bustling port area of Solitude, handling sea trade from across Tamriel. Home to the East Empire Company Warehouse and various shipping businesses.",
                        "tags": ["docks_major_port", "trade_hub_maritime", "east_empire_company_hq_skyrim", "ship_travel_services", "warehouse_district"]
                    },
                    {
                        "id": 8012,
                        "name": "Erikur's House",
                        "desc": "The lavish residence of Thane Erikur, an influential and often corrupt noble in Solitude with significant business interests.",
                        "tags": ["residence_noble_wealthy", "noble_house_influential", "political_intrigue_corruption", "business_magnate"]
                    },
                    { # Added Thalmor Embassy (conceptual location near Solitude)
                        "id": 8013,
                        "name": "Thalmor Embassy (Access Point/Office in Solitude)",
                        "desc": "While the main embassy is more remote, the Thalmor maintain a significant presence and office within Solitude to oversee Imperial compliance with the White-Gold Concordat, a source of much local resentment.",
                        "tags": ["thalmor_presence_city", "political_office_foreign", "white_gold_concordat_enforcement", "local_resentment_focus", "diplomatic_intrigue"]
                    }
                ]
            },
            {
                "id": 81,
                "name": "Dragon Bridge",
                "desc": "A quaint village in northwestern Haafingar, built around an ancient and iconic stone bridge spanning the Karth River. It serves as a strategic crossing point and hosts an Imperial outpost.",
                "tags": ["village_strategic", "bridge_landmark_ancient", "strategic_location_river_crossing", "lumber_mill_nearby", "imperial_outpost_penitus_oculatus"],
                 "sub_locations": [
                    {
                        "id": 8101,
                        "name": "Four Shields Tavern",
                        "desc": "The inn at Dragon Bridge, a common stop for Imperial soldiers, Penitus Oculatus agents, and travelers on the road to Solitude or the Reach.",
                        "tags": ["inn", "tavern", "social", "travel_stop_imperial", "rumor_source_military"]
                    },
                    {
                        "id": 8102,
                        "name": "Dragon Bridge Lumber Camp",
                        "desc": "The lumber mill that supports the village of Dragon Bridge, run by Horgeir.",
                        "tags": ["lumber_mill", "resource_wood"]
                    },
                    {
                        "id": 8103,
                        "name": "Penitus Oculatus Outpost (Dragon Bridge)", # Clarified
                        "desc": "A fortified Imperial outpost near Dragon Bridge, often used by the Penitus Oculatus for operations in Haafingar and the western holds.",
                        "tags": ["military_outpost_fortified", "imperial_penitus_oculatus_base"]
                    }
                ]
            },
            {
                "id": 82,
                "name": "Wolfskull Cave",
                "desc": "A dark, foreboding cave system high in the mountains of Haafingar. Necromancers are rumored to gather here, attempting rituals to resurrect the ancient Wolf Queen Potema.",
                "tags": ["cave_dangerous_remote", "dungeon_major", "haunted_legends", "necromancer_ritual_site_active", "potema_wolf_queen_resurrection", "quest_location_major_evil"]
            },
            {
                "id": 83,
                "name": "Fort Hraggstad",
                "desc": "An Imperial fort northwest of Solitude, guarding the coastline. It is currently garrisoned by Imperial soldiers, though its readiness might be tested by local banditry or rising Stormcloak sentiment elsewhere.",
                "tags": ["fort_coastal", "military_imperial_garrison", "dungeon_potential_if_contested", "coastal_defense_active", "strategic_location_maritime"]
            },
            {
                "id": 84,
                "name": "Brinewater Grotto",
                "desc": "A coastal cave system south of Solitude Docks, a known haunt for smugglers and bandits who use its hidden coves to move illicit goods.",
                "tags": ["cave_coastal_hidden", "smuggler_den_active", "bandit_lair_coastal", "dungeon_smuggling", "illicit_trade_route"]
            },
            {
                "id": 85,
                "name": "Broken Oar Grotto",
                "desc": "A large, hidden coastal cave system north of Solitude, serving as a major pirate and bandit stronghold known as Blackblood Marauders' hideout.",
                "tags": ["cave_coastal_large", "pirate_stronghold_blackblood", "bandit_base_major", "dungeon_complex", "quest_location_bounty_pirate"]
            },
            {
                "id": 86,
                "name": "Ironback Hideout",
                "desc": "A small, well-hidden cave or ruin serving as a minor bandit hideout in the wilderness of Haafingar, used for ambushing travelers on less-patrolled roads.",
                "tags": ["cave_minor_hidden", "bandit_outpost_ambush", "dungeon_minor", "wilderness_danger_spot"]
            },
            {
                "id": 87,
                "name": "Pinemoon Cave",
                "desc": "A cave system in the mountains of Haafingar, often inhabited by vampires or other dangerous creatures drawn to its isolation and darkness.",
                "tags": ["cave_mountain_remote", "vampire_lair_potential_strong", "monster_den_dangerous", "dungeon_dark"]
            },
            {
                "id": 88,
                "name": "Potema's Catacombs",
                "desc": "The extensive catacombs beneath Solitude's Temple of the Divines, where the Wolf Queen Potema's spirit is confronted by those seeking to prevent her return to power.", # Already fitting
                "tags": ["catacombs_ancient_city", "undead_heavy_powerful", "dungeon_major_quest", "quest_location_potema_final", "boss_fight_potema_spirit"]
            },
            {
                "id": 89,
                "name": "Ravenscar Hollow",
                "desc": "A small cave on the northern coast of Haafingar, typically home to a coven of hagravens who perform dark rituals overlooking the stormy sea.",
                "tags": ["cave_coastal_isolated", "hagraven_coven_lair", "dark_ritual_site_coastal", "dungeon_minor_witchcraft"]
            },
            {
                "id": 80001,
                "name": "Shadowgreen Cavern",
                "desc": "A lush, hidden cave system with unique bioluminescent flora and fauna, located southwest of Solitude. A place of surprising beauty and dangerous predators.",
                "tags": ["cave_hidden_lush", "unique_environment_subterranean", "alchemy_ingredients_rare_glowing", "spriggan_den_potential", "predator_lair", "dungeon_beautiful_dangerous"]
            },
            {
                "id": 80002,
                "name": "Steepfall Burrow",
                "desc": "A small cave system or den, likely inhabited by frost trolls or ice wraiths, in the snowy mountains of Haafingar, guarding a narrow pass.",
                "tags": ["cave_ice_mountain", "monster_den_frost_troll_wraith", "mountain_location_high_altitude", "dungeon_minor_cold"]
            },
            {
                "id": 80003,
                "name": "Stillborn Cave",
                "desc": "A small, eerie cave in Haafingar, rumored to be cursed or haunted by a sorrowful spirit. Few dare to enter.",
                "tags": ["cave_minor_eerie", "cursed_site_rumor", "haunted_potential_sorrowful", "local_superstition"]
            },
            {
                "id": 80004,
                "name": "The Steed Stone",
                "desc": "A Standing Stone located northwest of Solitude on a high ridge, granting increased carry weight and removing movement penalties from armor.",
                "tags": ["standing_stone_utility", "buff_carry_weight_speed", "mountain_location_scenic"]
            },
            {
                "id": 80005,
                "name": "Katla's Farm",
                "desc": "A farm located just outside Solitude's main gates, providing produce and horses for the city and the Legion. Run by Katla.",
                "tags": ["farm_city_outskirts", "stables_horses", "resource_food_supply", "horse_vendor_solitude"]
            },
            # New Haafingar Locations
            {
                "id": 80014,
                "name": "Northwatch Keep",
                "desc": "A remote coastal fortress controlled by the Thalmor, used as a prison for those they deem enemies of the Aldmeri Dominion. It is heavily guarded and a symbol of Thalmor oppression.",
                "tags": ["fort_coastal_thalmor", "thalmor_stronghold_prison", "political_prison", "oppression_symbol", "dangerous_infiltration_target", "quest_location_rescue_thalmor"]
            },
            {
                "id": 80015,
                "name": "Volskygge",
                "desc": "An ancient Nordic ruin high in the mountains of Haafingar, leading to a Dragon Priest's tomb at its peak. Guarded by draugr and powerful magic.",
                "tags": ["nordic_ruin_major_mountain", "dragon_priest_tomb_volsung", "undead_heavy", "dungeon_complex_peak", "dragon_word_ancient"]
            },
            {
                "id": 80016,
                "name": "Clearpine Pond",
                "desc": "A tranquil pond nestled in the forests of Haafingar, known for its clear waters and abundant fish. A popular spot for local hunters and hermits.",
                "tags": ["pond_forest", "fishing_spot_good", "hunter_camp_potential", "tranquil_location", "natural_beauty"]
            },
            {
                "id": 80017,
                "name": "Coastal Watch Fishery",
                "desc": "A small fishing village nestled in a cove near a crumbling, ancient watchtower on Haafingar's coast. The villagers are wary of both pirates and the crumbling tower's secrets.",
                "tags": ["village_fishing_coastal", "watchtower_ruined_nearby", "pirate_threat_local", "historic_landmark_local_mystery"]
            },
            {
                "id": 80018,
                "name": "Shepherd's Rest Farm",
                "desc": "A secluded farm high in the hills of Haafingar, known for its hardy mountain sheep and the potent, if rough, cheese made from their milk.",
                "tags": ["farm_mountain_secluded", "agriculture_sheep_hardy", "cheese_production_local", "residence_isolated_pastoral"]
            },
            {
                "id": 80019,
                "name": "Smuggler's Cove (Minor)",
                "desc": "A small, well-hidden sea cave on Haafingar's coast, used by petty smugglers to land illicit goods or hide from patrols. Likely contains a small cache.",
                "tags": ["cave_sea_smuggler", "dungeon_minor", "smuggler_cache_small", "coastal_hideout_secret"]
            },
            {
                "id": 80020,
                "name": "Ruined Coastal Shrine",
                "desc": "The crumbling remains of a small, ancient shrine dedicated to an unknown sea deity or ancestor, battered by the coastal winds and waves of Haafingar.",
                "tags": ["ruin_shrine_coastal", "historic_site_religious_ancient", "weathered_landmark", "offering_spot_forgotten"]
            },
            {
                "id": 80021,
                "name": "Widow's Watch Ruins",
                "desc": "The crumbling remains of a small watchtower on a lonely cliff overlooking the Sea of Ghosts. Local tales say it was built by a noblewoman awaiting her lost husband's return from sea, and her sorrowful spirit still lingers.",
                "tags": ["ruin_tower_coastal", "dungeon_minor", "haunted_potential_ghostly_widow", "scenic_overlook_ruined", "local_legend_tragic"]
            },
            {
                "id": 80022,
                "name": "Shrine of Dibella (Wilderness - Haafingar)",
                "desc": "A secluded, beautifully maintained outdoor shrine to Dibella, hidden in a picturesque grove or clifftop in Haafingar's wilderness. A place of quiet inspiration and artistic offerings.",
                "tags": ["shrine_aedric_outdoor", "dibella_shrine", "religious_site_secluded", "natural_beauty_spot", "artistic_inspiration_site"]
            },
            {
                "id": 80024,
                "name": "The Katariah (Imperial Flagship)",
                "desc": "A massive Imperial warship, often docked at Solitude or patrolling the Sea of Ghosts. It represents the might of the Imperial Navy in Skyrim's waters. (May not be Emperor Titus Mede II's personal vessel in 4E 200, but a significant flagship).",
                "tags": ["ship_imperial_warship_major", "naval_presence_imperial", "solitude_docks_visitor_potential", "sea_of_ghosts_patrol", "military_vessel_flagship_class"]
            },
            {
                "id": 80025,
                "name": "Orphan's Tear",
                "desc": "A shipwreck on the northern coast of Haafingar, west of the Solitude Lighthouse. It is rumored to hold lost treasures and is sometimes used as a hideout by coastal scavengers or bandits.",
                "tags": ["shipwreck_site_coastal", "treasure_potential_lost", "bandit_lair_scavenger_potential", "dungeon_minor_wreckage", "coastal_exploration_point"]
            },
            {
                "id": 80026,
                "name": "Solitude Lighthouse (Structure)",
                "desc": "The tall lighthouse guiding ships into Solitude's harbor. While functional, its keeper might have local concerns or knowledge.",
                "tags": ["lighthouse_functional", "coastal_landmark_navigational", "solitude_harbor_aid", "quest_giver_potential_keeper"]
            },
            {
                "id": 80027,
                "name": "The Dainty Sload",
                "desc": "A notorious pirate or smuggler ship that sometimes anchors in hidden coves along Haafingar's coast, or might even brazenly try to trade illicit goods at the Solitude Docks under a false flag.",
                "tags": ["ship_pirate_smuggler", "criminal_vessel_notorious", "coastal_encounter_hostile_potential", "illicit_trade_source", "black_market_connection"]
            }
        ]
    },

    # THE RIFT
    {
        "id": 9,
        "name": "The Rift",
        "desc": "A temperate, autumnal hold in southeastern Skyrim, known for its golden forests, numerous lakes, and the city of Riften, a haven for the Thieves Guild and rife with corruption. It borders Morrowind and Cyrodiil.",
        "tags": ["hold", "forest_autumnal_large", "lake_region_abundant", "thieves_guild_stronghold", "nordic_culture_local", "morrowind_border_region", "cyrodiil_border_region", "beautiful_scenery_corrupt_underbelly", "black_briar_dominance"],
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
                "tags": ["city", "lake_city_canals", "riften_city_of_thieves", "thieves_guild_hq_active", "black_briar_influence_total", "corrupt_city_major", "jarls_seat_laila", "mercenary_presence"], # Added Laila
                "sub_locations": [
                    {
                        "id": 9001,
                        "name": "The Bee and Barb",
                        "desc": "A popular tavern in Riften, owned by Keerava and Talen-Jei. A common meeting place and source of rumors, often frequented by Thieves Guild associates.",
                        "tags": ["tavern", "social_hub_riften", "inn", "quest_giver_potential", "rumor_source_guild"]
                    },
                    {
                        "id": 9002,
                        "name": "Black-Briar Meadery (Riften Building)",
                        "desc": "The main office and shopfront for the powerful Black-Briar Meadery within Riften, a symbol of Maven Black-Briar's economic and political control over the city.",
                        "tags": ["shop_meadery", "meadery_hq_black_briar", "black_briar_family_business", "economic_powerhouse", "political_influence_source"]
                    },
                    {
                        "id": 9003,
                        "name": "The Pawned Prawn",
                        "desc": "A general goods store in Riften, run by Bersi Honey-Hand. A place to buy and sell various items, some of questionable origin.",
                        "tags": ["shop_general_goods", "trade_variety", "fence_connection_potential"]
                    },
                    {
                        "id": 9004,
                        "name": "Mistveil Keep",
                        "desc": "The Jarl's residence in Riften, currently home to Jarl Laila Law-Giver, though her authority is often undermined by Maven Black-Briar.", # Laila is Jarl pre-Civil War changes
                        "tags": ["keep_jarls_residence", "government_local", "jarls_seat_laila", "political_intrigue_maven", "black_briar_shadow_rule"]
                    },
                    {
                        "id": 9005,
                        "name": "The Ratway",
                        "desc": "A dangerous, labyrinthine network of tunnels beneath Riften, serving as the entrance to the Ragged Flagon and the hidden headquarters of the Thieves Guild.",
                        "tags": ["dungeon_city_undercity_ratway", "thieves_guild_access_route", "criminal_hideout_network", "dangerous_area_city", "sewers_forgotten"],
                        "sub_locations": [
                            {
                                "id": 90051,
                                "name": "The Ragged Flagon",
                                "desc": "A hidden tavern within the Ratway, serving as the main gathering area, bar, and neutral ground for the Thieves Guild and its associates.",
                                "tags": ["tavern_secret_guild", "thieves_guild_bar_meeting_place", "fence_location_guild", "information_broker_potential"]
                            },
                            {
                                "id": 90052,
                                "name": "The Cistern",
                                "desc": "The secure, inner sanctum and living quarters of the Thieves Guild, deep within the Ratway, accessible only to trusted members.",
                                "tags": ["thieves_guild_inner_sanctum_secure", "training_area_thief_skills", "sleeping_quarters_guild", "treasure_vault_guild_potential"]
                            }
                        ]
                    },
                    {
                        "id": 9006,
                        "name": "Temple of Mara (Riften)",
                        "desc": "A prominent temple dedicated to Mara, the Divine of Love and Compassion. It is a place for marriages, seeking guidance on love, and helping the needy.",
                        "tags": ["temple_major_divine", "religious_center_love", "mara_shrine_prominent", "marriage_location_skyrim", "quest_line_mara_agents"]
                    },
                    {
                        "id": 9007,
                        "name": "The Scorched Hammer",
                        "desc": "Balimund's smithy in Riften, known for its quality craftsmanship and Balimund's expertise with fire salts in forging.",
                        "tags": ["blacksmith_city_skilled", "shop_weapons_armor", "crafting_fire_salts_specialty"]
                    },
                     {
                        "id": 9008,
                        "name": "Elgrim's Elixirs",
                        "desc": "An apothecary shop run by Elgrim and his wife Hafjorg, located on Riften's lower platforms. Elgrim is a master alchemist, albeit somewhat reclusive.",
                        "tags": ["alchemy_shop_master", "magic_vendor_potions_ingredients", "reclusive_alchemist"]
                    },
                    {
                        "id": 9009,
                        "name": "Riften Marketplace",
                        "desc": "The central market area of Riften, with various stalls selling food, jewelry, and other goods. A prime location for pickpockets and observant guild members.",
                        "tags": ["market_city_center", "trade_local_goods", "pickpocket_hotspot", "thieves_guild_observation_post"]
                    },
                    {
                        "id": 9010,
                        "name": "Honorhall Orphanage",
                        "desc": "Riften's orphanage, currently run by the cruel Grelod the Kind. The children suffer under her neglect and abuse.",
                        "tags": ["orphanage_riften", "dark_brotherhood_quest_start_avenuts", "social_issue_child_abuse", "grelod_the_kind_tyrant"]
                    },
                    {
                        "id": 9011,
                        "name": "Black-Briar Manor",
                        "desc": "The grand residence of the powerful and influential Black-Briar family, heavily guarded and a testament to their wealth and control over Riften.",
                        "tags": ["residence_noble_powerful", "noble_house_black_briar", "black_briar_family_home_fortified", "political_power_center_riften", "maven_black_briar_residence"]
                    },
                    { # Added Beggar's Row
                        "id": 9012,
                        "name": "Beggar's Row",
                        "desc": "A dilapidated section of Riften's lower walkways where the city's poorest and most desperate souls eke out a meager existence.",
                        "tags": ["poverty_district", "slums_city", "beggars_community", "desperation_hub"]
                    },
                    {
                        "id": 9013,
                        "name": "Riften Warehouse",
                        "desc": "A large warehouse on the Riften docks, often used for storing goods, both legitimate and illicit. Rumored to be a key point in the city's smuggling operations and sometimes used by the Thieves Guild.",
                        "tags": ["warehouse_docks", "storage_commercial", "smuggling_hotspot_potential", "thieves_guild_interest", "black_briar_connection_rumor"]
                    }
                ]
            },
            {
                "id": 91,
                "name": "Shor's Stone",
                "desc": "A small mining village in the northern Rift, primarily focused on an ebony mine that has recently been troubled by giant frostbite spiders from a nearby cave.",
                "tags": ["village_mining_small", "mining_ebony", "resource_ebony_rare", "spider_infestation_recent", "quest_location_clear_mine"],
                "sub_locations": [
                    {
                        "id": 9101,
                        "name": "Redbelly Mine",
                        "desc": "The ebony mine that is the main source of livelihood for Shor's Stone, currently unsafe due to spider infestation.",
                        "tags": ["mine_ebony_infested", "resource_ebony_dangerous", "spider_cave_connected"]
                    },
                    {
                        "id": 9102,
                        "name": "Sylgja's House",
                        "desc": "The home of Sylgja, a miner in Shor's Stone, whose father works in Darkwater Crossing.",
                        "tags": ["residence_miner"]
                    },
                    { # Added Filnjar's House (Blacksmith)
                        "id": 9103,
                        "name": "Filnjar's House and Smithy",
                        "desc": "The home and modest smithy of Filnjar, the blacksmith of Shor's Stone.",
                        "tags": ["residence", "blacksmith_village"]
                    }
                ]
            },
            {
                "id": 92,
                "name": "Ivarstead",
                "desc": "A small village at the foot of the Throat of the World, on the shores of Lake Geir. It is the traditional starting point for the pilgrimage up the Seven Thousand Steps to High Hrothgar.",
                "tags": ["village_pilgrimage_base", "pilgrimage_start_high_hrothgar", "lake_settlement_geir", "greybeards_path_start", "historic_route"],
                "sub_locations": [
                    {
                        "id": 9201,
                        "name": "Vilemyr Inn",
                        "desc": "The local inn of Ivarstead, offering rest to those journeying to High Hrothgar, run by Wilhelm. He is concerned about Shroud Hearth Barrow.",
                        "tags": ["inn", "tavern", "social", "quest_giver_barrow"]
                    },
                    {
                        "id": 9202,
                        "name": "Shroud Hearth Barrow (Ivarstead Entrance)", # Clarified
                        "desc": "An ancient Nordic barrow located within Ivarstead itself. Locals believe it to be haunted and avoid it, though Wilhelm seeks someone to investigate.",
                        "tags": ["barrow_local", "nordic_ruin_village", "dungeon_undead", "undead_presence_strong", "quest_location_local_investigation", "puzzle_dragon_claw"]
                    },
                    {
                        "id": 9203,
                        "name": "Klimmek's House",
                        "desc": "The home of Klimmek, a resident of Ivarstead who makes regular supply deliveries to High Hrothgar for the Greybeards.",
                        "tags": ["residence", "quest_giver_minor_delivery", "greybeards_supplier"]
                    },
                    { # Added Narfi's Wrecked House
                        "id": 9204,
                        "name": "Narfi's Wrecked House",
                        "desc": "The ruined and isolated house of Narfi, a distraught beggar living across the river from Ivarstead, searching for his missing sister.",
                        "tags": ["ruin_dwelling", "beggar_isolated", "missing_person_plot", "quest_giver_dark_brotherhood_potential"]
                    }
                ]
            },
            {
                "id": 93,
                "name": "Lost Prospect Mine",
                "desc": "An abandoned gold mine in the Rift, often occupied by bandits. It is rumored to be played out, but some say a few veins might remain for the determined.",
                "tags": ["mine_abandoned_gold", "resource_gold_rumored", "bandit_lair_potential", "dungeon_minor", "exploration_risky"]
            },
            {
                "id": 94,
                "name": "Broken Helm Hollow",
                "desc": "A secluded cave system east of Riften, serving as a well-established bandit hideout with multiple chambers.",
                "tags": ["cave_bandit_camp", "bandit_hideout_established", "dungeon_multi_level"]
            },
            {
                "id": 95,
                "name": "Avanchnzel",
                "desc": "A large and dangerous Dwemer ruin in the southern mountains of the Rift. It contains ancient technology, Falmer, and is the focus of a quest to retrieve a unique Dwemer lexicon for From-Deepest-Fathoms.",
                "tags": ["dwemer_ruin_major_dangerous", "dungeon_complex_falmer", "mechanical_constructs_dwemer", "falmer_presence_strong", "quest_location_artifact_lexicon", "unique_dwemer_artifact"]
            },
            {
                "id": 96,
                "name": "Boulderfall Cave",
                "desc": "A cave in the eastern Rift, often inhabited by necromancers or other dark mages who use its seclusion for their sinister experiments.",
                "tags": ["cave_secluded", "necromancer_lair_active", "dark_magic_site", "dungeon_undead_experiments"]
            },
            {
                "id": 97,
                "name": "Clearspring Tarn",
                "desc": "A small, picturesque tarn and cave system west of Shor's Stone, often home to trolls guarding a treasure hunter's remains and note.",
                "tags": ["cave_tarn", "troll_den_guardian", "scenic_spot_hidden", "treasure_hunter_lore_note", "dungeon_minor_treasure"]
            },
            {
                "id": 98,
                "name": "Crystaldrift Cave",
                "desc": "A small ice cave south of Riften, notable for its unique crystal formations. It is sometimes a den for frost creatures or a reclusive hermit.",
                "tags": ["cave_ice_crystal", "frost_creature_den_potential", "unique_geology_crystals", "hermit_lair_potential"]
            },
            {
                "id": 99,
                "name": "Darklight Tower",
                "desc": "A ruined tower southwest of Riften, now a den for hagravens and the site of a Daedric quest where Illia attempts to stop her mother from becoming a hagraven.",
                "tags": ["tower_ruined_hagraven", "hagraven_coven_powerful", "daedric_quest_repentance", "dungeon_vertical", "quest_companion_illia"]
            },
            {
                "id": 90001,
                "name": "Faldar's Tooth",
                "desc": "A ruined fort west of Riften, initially overrun by wolves, but later becomes a hideout for bandits or the Silver Hand, depending on unfolding events.",
                "tags": ["fort_ruined_strategic", "wolf_den_initial_large", "bandit_lair_potential_strong", "silver_hand_lair_potential_alt", "dungeon_contested_territory"]
            },
            {
                "id": 90002,
                "name": "Fort Greenwall",
                "desc": "A large fort in the eastern Rift, strategically important. Currently garrisoned by Imperial soldiers, but its control is tenuous given the Rift's leanings.",
                "tags": ["fort_major_border", "military_imperial_garrison", "dungeon_potential_if_contested", "strategic_location_east_rift"]
            },
            {
                "id": 90003,
                "name": "Froki's Shack",
                "desc": "The isolated shack of Froki Whetted-Blade, an old hunter and devout follower of Kyne, located in the southern mountains of the Rift. He offers tasks related to Kyne's sacred trials.",
                "tags": ["hut_isolated_mountain", "hunter_hermitage_devout", "quest_giver_kyne_trials", "kyne_worship_shrine_nearby", "animal_lore"]
            },
            {
                "id": 90004,
                "name": "Goldenglow Estate",
                "desc": "A large honey farm and apiary on an island in Lake Honrich, owned by Aringoth. It's a major supplier of honey for the Black-Briar Meadery and becomes a key target in a Thieves Guild questline.",
                "tags": ["farm_apiary_large", "island_location_lake", "thieves_guild_quest_major", "mead_production_supplier", "wealthy_estate_guarded", "economic_target"]
            },
            {
                "id": 90005,
                "name": "Heartwood Mill",
                "desc": "A lumber mill on the shores of Lake Honrich, run by Grosta. A peaceful location providing wood for Riften.",
                "tags": ["lumber_mill_lakeside", "settlement_minor_industrial", "resource_wood", "lake_location_scenic"]
            },
            {
                "id": 90006,
                "name": "Honeystrand Cave",
                "desc": "A small cave south of Ivarstead, often a den for bears or other local wildlife.",
                "tags": ["cave_wilderness", "bear_den_common", "dungeon_minor_natural"]
            },
            {
                "id": 90007,
                "name": "Last Vigil",
                "desc": "A ruined watchtower and ancient dragon burial site high in the mountains of the Rift. While no dragons stir now, it's a place of potent old magic and may attract those interested in such power (like ancient vampire cults or dragon scholars).", # Dawnguard reference made generic
                "tags": ["watchtower_ruined_remote", "dragon_burial_site_ancient", "ancient_magic_site", "mountain_peak_isolated", "vampire_cult_interest_potential", "dragon_scholar_interest_potential"]
            },
            {
                "id": 90008,
                "name": "Merryfair Farm",
                "desc": "A farmstead located near Riften, owned by Dravin Llanith, who is often worried about his stolen bow.",
                "tags": ["farm_local", "residence_farmer", "quest_item_stolen_bow"]
            },
            {
                "id": 90009,
                "name": "Nightingale Hall",
                "desc": "The secret sanctuary and headquarters of the Nightingales, protectors of Nocturnal's shrine, hidden within a cave system in the Rift. Its existence is known only to the highest echelons of the Thieves Guild.",
                "tags": ["secret_sanctuary_guild", "nightingale_hq_hidden", "daedric_shrine_nocturnal_protected", "thieves_guild_elite_order", "dungeon_quest_sacred", "oathsworn_guardians"]
            },
            {
                "id": 90010,
                "name": "Nilheim",
                "desc": "A ruined watchtower east of Ivarstead, occupied by bandits who employ a clever ambush by pretending to be legitimate guards.",
                "tags": ["watchtower_ruined_bandit", "bandit_camp_deceptive", "ambush_site_clever", "dungeon_tower"]
            },
            {
                "id": 90011,
                "name": "Northwind Summit",
                "desc": "A mountain peak in the northern Rift, near Shor's Stone, known as an ancient dragon lair and the site of a Word Wall.", # No active dragon
                "tags": ["dragon_lair_ancient_empty", "dragon_word_ancient", "mountain_peak_high", "dungeon_lair_potential"]
            },
            {
                "id": 90012,
                "name": "Pinepeak Cavern",
                "desc": "A cave system near Ivarstead, often inhabited by bears or other forest creatures.",
                "tags": ["cave_forest", "bear_den_common", "dungeon_minor_natural"]
            },
            {
                "id": 90013,
                "name": "Redwater Den",
                "desc": "A rundown shack that serves as a front for a clandestine skooma operation, possibly with ties to a darker, more sinister group dealing in a particularly potent brew.", # Dawnguard ref made generic
                "tags": ["skooma_den_hidden", "criminal_front_operation", "dungeon_underground_facility", "dangerous_substances", "vampire_influence_rumored_subtle"]
            },
            {
                "id": 90014,
                "name": "Sarethi Farm",
                "desc": "A farmstead near Ivarstead, run by Avrusa Sarethi, an alchemist known for successfully cultivating Nirnroot.",
                "tags": ["farm_alchemical", "residence_alchemist", "alchemy_ingredient_nirnroot_cultivation", "quest_giver_alchemy_related"]
            },
            {
                "id": 90015,
                "name": "Snapleg Cave",
                "desc": "A cave system south of Ivarstead, often home to spriggans, witches, or hagravens drawn to its primal energies.",
                "tags": ["cave_primal_magic", "spriggan_den_strong", "hagraven_lair_potential", "witch_coven_potential", "dungeon_natural_magic"]
            },
            {
                "id": 90016,
                "name": "Snow-Shod Farm",
                "desc": "A farmstead near Riften, owned by the influential Snow-Shod family, who are staunch supporters of Ulfric Stormcloak.",
                "tags": ["farm_prominent_family", "residence_nord_loyalist", "political_family_stormcloak"]
            },
            {
                "id": 90017,
                "name": "Stendarr's Beacon",
                "desc": "A ruined watchtower in the eastern Rift, now maintained by the Vigilants of Stendarr as an outpost in their crusade against Daedra, vampires, and other abominations.",
                "tags": ["watchtower_ruined_vigilant", "vigilant_of_stendarr_outpost_active", "daedra_hunting_base_fortified", "anti_abomination_stronghold"]
            },
            {
                "id": 90018,
                "name": "Treva's Watch",
                "desc": "A ruined fort west of Ivarstead, taken over by bandits. Stalleo, a Nord whose family was driven out, seeks help to reclaim it.",
                "tags": ["fort_ruined_bandit_occupied", "bandit_lair_fortified", "quest_location_reclaim_family", "dungeon_battle"]
            },
            {
                "id": 90019,
                "name": "Tolvald's Cave",
                "desc": "A very large and dangerous cave system in the Velothi Mountains on the border with Morrowind, infested with Falmer, Chaurus, and possibly other deep-dwelling horrors.",
                "tags": ["cave_major_borderland", "falmer_den_extensive", "chaurus_nest_large", "dungeon_large_dangerous", "morrowind_border_area_remote", "exploration_deadly"]
            },
            # New Rift Locations
            {
                "id": 90020,
                "name": "Autumnwatch Tower",
                "desc": "A pair of ruined Nordic towers overlooking the golden forests of the Rift, often used as a lair by dragons in ages past, now possibly home to Forsworn or bandits.", # Dragon reference made ancient
                "tags": ["tower_ruined_nordic", "scenic_overlook_autumnal", "dragon_lair_ancient_rumored", "forsworn_outpost_potential", "bandit_camp_potential"]
            },
            {
                "id": 90021,
                "name": "Black-Briar Lodge",
                "desc": "A secluded hunting lodge owned by the Black-Briar family, located northeast of Riften. Used for private gatherings and potentially illicit dealings.",
                "tags": ["lodge_private_black_briar", "hunting_retreat_elite", "secret_meetings_potential", "black_briar_property_guarded"]
            },
            {
                "id": 90022,
                "name": "Forelhost", # Was 108
                "desc": "A massive, ancient Nordic monastery fortress on a mountaintop in The Rift, the last stronghold of the Dragon Cult. It is now sealed and haunted by its former Dragon Priest Rahgot and his draugr followers.",
                "tags": ["nordic_ruin_fortress_major", "dragon_cult_stronghold_last", "undead_heavy_powerful", "dragon_priest_rahgot", "sealed_ruin_dangerous", "dungeon_large_mountain_top", "quest_location_artifact"],
                "demographics": {"Draugr": 85, "Frost Trolls (exterior)": 10, "Dragon Priest": 1}, # Example demographics
                "travel": { "roads": [], "paths": ["Treacherous mountain path from The Rift plains"] }
            },
            {
                "id": 90023,
                "name": "Giant's Grove",
                "desc": "A small, hidden grove within the Rift's forests, where a reclusive giant tends to a painted cow. A place of unusual peace.",
                "tags": ["grove_hidden_giant", "giant_peaceful_encounter", "unique_animal_painted_cow", "folk_tale_location"]
            },
            {
                "id": 90024,
                "name": "Ruunvald Excavation",
                "desc": "An archaeological dig site in the eastern mountains of the Rift, where Vigilants of Stendarr were investigating ancient ruins before something went terribly wrong. Now a place of danger and dark influence.", # Made pre-Dawnguard
                "tags": ["excavation_site_ruined", "vigilant_of_stendarr_tragedy", "dark_influence_site", "dungeon_dangerous_investigation", "undead_presence_likely"]
            },
            {
                "id": 90025,
                "name": "Lakeside Landing",
                "desc": "A small community of fisherfolk and boatwrights on the shores of Lake Honrich in The Rift, known for their sturdy fishing boats and tales of the lake's depths.",
                "tags": ["village_fishing_lakeside", "boatwright_community", "lake_honrich_settlement", "local_folklore_lake_monsters_potential"]
            },
            {
                "id": 90026,
                "name": "Goldenleaf Farmstead",
                "desc": "A picturesque farm in The Rift, renowned for its vibrant autumn foliage and the sweet, crisp apples grown in its orchards.",
                "tags": ["farm_picturesque_autumnal", "agriculture_orchard_apple", "scenic_location_rift", "unique_produce_apples"]
            },
            {
                "id": 90027,
                "name": "Tanglewood Den",
                "desc": "A dense, overgrown cave system hidden deep within the autumnal forests of The Rift, often serving as a den for bears, spriggans, or a reclusive alchemist.",
                "tags": ["cave_forest_overgrown", "dungeon_minor", "bear_den_potential", "spriggan_grove_cave", "alchemist_hideout_potential"]
            },
            {
                "id": 90028,
                "name": "Ruins of Autumn's End",
                "desc": "The crumbling remains of an old hunting lodge or minor keep in The Rift, now reclaimed by the forest. It might hold forgotten treasures or be used by local bandits.",
                "tags": ["ruin_lodge_forest", "historic_site_minor_keep", "treasure_cache_rumored", "bandit_outpost_potential_ruin"]
            },
            {
                "id": 90029,
                "name": "Shrine of Zenithar (Rift Forest)",
                "desc": "An outdoor shrine dedicated to Zenithar, the Divine of Work and Commerce, located along an old trade path in the Rift's forests. Merchants and craftsmen sometimes leave offerings here for prosperity.",
                "tags": ["shrine_aedric_outdoor", "zenithar_shrine", "religious_site_trade_route", "commerce_shrine", "craftsmanship_blessing_site"]
            },
            {
                "id": 90030,
                "name": "Angarvunde",
                "desc": "An ancient and extensive Nordic ruin in the mountains of the Rift, deeply buried and heavily guarded by draugr. It is known for a tragic tale of betrayal and a powerful artifact sought by some.",
                "tags": ["nordic_ruin_major", "dungeon_large_complex", "undead_heavy_powerful", "historic_site_tragic_lore", "artifact_location_rumored", "dragon_word_ancient_potential"]
            },
            {
                "id": 90031,
                "name": "The Shadow Stone",
                "desc": "A Standing Stone hidden in the forests south of Riften, near the traditional grounds of the Nightingales. It grants the power of invisibility for a short duration, once per day.",
                "tags": ["standing_stone", "power_invisibility_temporary", "stealth_buff", "forest_shrine_hidden", "nightingale_lore_associated_potential"]
            },
            {
                "id": 90032,
                "name": "Ruins of Bthalft",
                "desc": "Crumbling Dwemer ruins in the southern Rift, notable for an outdoor Dwemer mechanism. Legends say it's an access point to deeper, hidden Dwemer workings and perhaps the legendary Aetherium Forge.",
                "tags": ["dwemer_ruin_outdoor", "ancient_mechanism_dwemer", "aetherium_forge_access_rumor", "falmer_presence_potential_nearby", "exploration_point_dwemer_lore"]
            },
            {
                "id": 90033,
                "name": "Fallowstone Cave",
                "desc": "A large cave system in the northern Rift, near Shor's Stone. It is often a den for bears or trolls and is one of the sites for Kyne's Sacred Trials.",
                "tags": ["cave_large_wilderness", "monster_den_bear_troll", "kyne_sacred_trials_site", "dungeon_natural", "hunting_ground_dangerous"]
            },
            {
                "id": 90034,
                "name": "Lost Tongue Overlook",
                "desc": "A ruined Nordic watchtower and ancient dragon lair high in the mountains of The Rift, south of Riften. It contains a Word Wall and is often guarded by powerful draugr or other ancient entities.",
                "tags": ["nordic_ruin_tower", "dragon_lair_ancient_empty", "dragon_word_ancient", "dungeon_major_overlook", "undead_presence_strong", "mountain_peak_ruin"]
            },
            {
                "id": 90035,
                "name": "Geirmund's Hall",
                "desc": "An ancient Nordic ruin on an island in Lake Geir, east of Ivarstead. It is the tomb of the archmage Geirmund and is guarded by draugr and a powerful necromancer.",
                "tags": ["nordic_ruin_lakeside", "dungeon_tomb_mage", "undead_draugr", "necromancer_guardian_powerful", "quest_location_artifact_gauldur_amulet_related_potential", "historic_figure_geirmund"]
            }
        ]
    },

    # ADDITIONAL NOTABLE LOCATIONS & DYNAMIC ADVENTURE SITES
    # (Adjusted for 4E 200 - Dragons are ancient, Dragonborn prophecy not active in current events)
    {
        "id": 100,
        "name": "High Hrothgar",
        "desc": "Perched atop the Throat of the World, High Hrothgar is the ancient and sacred monastery of the Greybeards, masters of the Way of the Voice. Pilgrims rarely brave the Seven Thousand Steps to seek their wisdom.",
        "tags": ["monastery_ancient_sacred", "mountain_peak_settlement_remote", "sacred_site_kyne", "greybeards_home_isolated", "way_of_the_voice_masters", "unique_architecture_nordic", "pilgrimage_arduous"],
        "demographics": {"Nord Greybeards": 100}, # Greybeards are few and reclusive
        "travel": { "roads": [], "paths": ["Seven Thousand Steps from Ivarstead"] }
    },
    {
        "id": 101,
        "name": "Throat of the World",
        "desc": "Tamriel’s highest peak, a snow-clad titan revered by Nords and sacred to Kyne. Its summit holds ancient secrets, a Word Wall, and is the secluded domain of Paarthurnax, ancient leader of the Greybeards, though few know of his true nature or presence.",
        "tags": ["mountain_summit_sacred", "sacred_peak_kyne", "snowy_extreme_weather", "dragon_lore_paarthurnax_hidden", "dragon_word_ancient_powerful", "unique_vista_skyrim", "greybeards_leader_domain"],
        "demographics": {"Dragons (Paarthurnax, hidden)": 1, "Nord Spirits (conceptual)": 99},
        "travel": { "roads": [], "paths": ["Path from High Hrothgar Summit (restricted)"] }
    },
    {
        "id": 102,
        "name": "Blackreach",
        "desc": "A vast, luminous subterranean cavern system beneath Skyrim, filled with bioluminescent flora, ancient Dwemer cities, Falmer hordes, and valuable resources like Crimson Nirnroot. A dangerous and wondrous lost world.",
        "tags": ["underground_realm_vast", "dwemer_city_ruined_extensive", "falmer_territory_dangerous", "cavern_bioluminescent_unique", "unique_ecosystem_subterranean", "alchemy_ingredient_crimson_nirnroot", "geode_veins_rare", "dangerous_exploration_major"],
        "demographics": {"Falmer": 80, "Chaurus": 15, "Dwemer Constructs (Automated)": 5},
        "travel": { "roads": [], "paths": ["Alftand Elevator", "Mzinchaleft Elevator", "Raldbthar Elevator (hidden access points)"] }
    },
    {
        "id": 103,
        "name": "Sovngarde",
        "desc": "The revered afterlife of the Nords in Aetherius, a realm of valor, feasting, and eternal glory in the Hall of Valor. Normally accessible only to the spirits of worthy departed Nords.", # Removed TESV specific crisis access
        "tags": ["afterlife_nordic_paradise", "aetherius_realm_spiritual", "hall_of_valor_legendary", "heroic_spirits_nordic", "unique_celestial_plane", "not_normally_accessible_living"],
        "demographics": {"Nord Hero Spirits": 100},
        "travel": { "roads": [], "paths": ["Passage via extreme spiritual/magical means (highly restricted/legendary)"] }
    },
    {
        "id": 104,
        "name": "Labyrinthian",
        "desc": "The sprawling, maze-like ruins of the ancient Nordic city of Bromjunaar, once a center of the Dragon Cult. Now haunted by draugr, ghosts, and the powerful Dragon Priest Morokei, who guards the Staff of Magnus.",
        "tags": ["nordic_ruin_major_ancient", "city_ruined_dragon_cult", "undead_heavy_powerful", "maze_complex_dangerous", "dragon_priest_morokei_guardian", "college_of_winterhold_quest_major", "staff_of_magnus_location", "dungeon_large_epic"],
        "demographics": {"Draugr": 70, "Skeletons": 20, "Ghosts": 9, "Dragon Priest (Morokei)": 1},
        "travel": { "roads": ["Ancient Nordic Path (decayed)"], "paths": ["Hjaalmarch Foothills (near Morthal, treacherous approach)"] }
    },
    {
        "id": 109,
        "name": "Skuldafn Temple",
        "desc": "An exceptionally remote and legendary Nordic temple complex, rumored to be hidden high in the Velothi Mountains. Ancient tales speak of it as a Dragon Cult stronghold and a gateway to Sovngarde, but its location is lost to modern knowledge, likely inaccessible.", # Corrected for 4E 200
        "tags": ["nordic_temple_remote_legendary", "dragon_cult_site_ancient_lost", "sovngarde_portal_rumored", "highly_inaccessible_ruin", "ancient_magic_wards_powerful"],
        "demographics": {"Draugr (ancient guardians)": 90, "Dragon Priest (lingering spirit - potential)": 10},
        "travel": {"roads": [], "paths": ["Unknown/Magical means only (legendary)"]}
    },
    {
        "id": 110,
        "name": "Shrine of Azura",
        "desc": "A colossal statue and shrine dedicated to the Daedric Prince Azura, located high in the mountains south of Winterhold. A place of pilgrimage for her followers and where prophecies may be received.",
        "tags": ["daedric_shrine_azura_major", "colossal_statue_landmark", "pilgrimage_site_daedric", "prophecy_location_azura", "quest_location_daedric_artifact_azuras_star", "mountain_shrine_remote", "scenic_vista_panoramic"],
        "demographics": {"Priestess of Azura (Aranea Ienith)": 1, "Pilgrims (occasional)": 5, "Dunmer Followers (occasional)": 5},
        "travel": {"roads": [], "paths": ["Winding mountain path from Winterhold vicinity (difficult)"]}
    },
    {
        "id": 111,
        "name": "Shrine of Mehrunes Dagon (Mythic Dawn Museum/Shrine)", # Combined with Silus Vesuius context
        "desc": "A hidden shrine and museum dedicated to Mehrunes Dagon, Prince of Destruction, located in the mountains of The Pale, maintained by Silus Vesuius. He seeks to reforge Mehrunes' Razor.",
        "tags": ["daedric_shrine_dagon_hidden", "destruction_cult_remnants", "quest_location_daedric_artifact_razor", "mountain_shrine_secret", "mythic_dawn_collection", "dremora_guardians_summoned_potential"],
        "demographics": {"Silus Vesuius (Curator/Cultist)": 1, "Dremora (summoned during ritual)": 100},
        "travel": {"roads": [], "paths": ["Obscure path from The Pale foothills, near Dawnstar"]}
    },
    {
        "id": 112,
        "name": "Largashbur (Shrine of Malacath)", # Name clarified
        "desc": "The Orc stronghold of Largashbur in The Rift, which also serves as a shrine to Malacath. The tribe is currently cursed by giants and seeks aid from an outsider to appease their angered god.",
        "tags": ["orc_stronghold_cursed", "daedric_shrine_malacath_tribal", "cursed_tribe_giants", "quest_location_daedric_artifact_volendrung", "giant_attack_ongoing", "orc_shamanism"],
        "demographics": {"Orcs (cursed and weakened)": 90, "Giants (hostile)": 10},
        "travel": {"roads": [], "paths": ["Path from The Rift plains, near Forelhost"]}
    },
    {
        "id": 113,
        "name": "Sacellum of Boethiah", # Primary Name
        "desc": "A Daedric shrine high in the mountains east of Windhelm, where followers of Boethiah engage in deadly rituals of sacrifice and combat to prove their worth to the Prince of Plots.",
        "tags": ["daedric_shrine_boethiah_major", "deceit_cult_arena", "ritual_sacrifice_site_active", "quest_location_daedric_artifact_ebony_mail", "mountain_shrine_remote", "arena_combat_ritualistic"],
        "demographics": {"Boethiah Cultists (various races)": 100},
        "travel": {"roads": [], "paths": ["Treacherous path from Eastmarch mountains, east of Traitor's Post"]}
    },
    {
        "id": 114,
        "name": "Shrine to Peryite", # More common name
        "desc": "A remote Daedric shrine in The Reach, dedicated to Peryite, the Taskmaster. His afflicted followers gather here, seeking a cure from their debilitating disease by communing with the Prince.",
        "tags": ["daedric_shrine_peryite_remote", "plague_cult_afflicted", "quest_location_daedric_artifact_spellbreaker", "remote_shrine_dangerous_fumes", "alchemy_ritual_communion"],
        "demographics": {"Afflicted Followers (Bretons, Nords)": 100, "Kesh the Clean (Khajiit Priest)":1},
        "travel": {"roads": [], "paths": ["Isolated path from The Reach mountains, northwest of Karthwasten"]}
    },
    # ID 115 (Sacellum of Boethiah) is merged with ID 113.
    {
        "id": 116,
        "name": "Statue to Meridia",
        "desc": "A towering statue dedicated to the Daedric Prince Meridia, located on Mount Kilkreath in Haafingar. It is a beacon against the undead, and Meridia offers a quest to cleanse her temple of a necromancer's defilement.",
        "tags": ["daedric_shrine_meridia_light", "colossal_statue_landmark", "quest_location_daedric_artifact_dawnbreaker", "mountain_shrine_high_altitude", "undead_cleansing_quest_active", "anti_necromancy_beacon"],
        "demographics": {"Malkoran (Necromancer Spirit - Boss)": 1, "Corrupted Shades (initially)": 100},
        "travel": {"roads": [], "paths": ["Path from Dragon Bridge area, Mount Kilkreath ascent"]}
    },
    # Dawnguard/Dragonborn DLC locations adjusted for 4E 200 (mostly undiscovered or in a different state)
    {
        "id": 117,
        "name": "Forgotten Vale (Legendary Site)",
        "desc": "A legendary, hidden glacial valley in northwestern Skyrim, whispered to be an ancient sanctuary of the Snow Elves. Its existence is unconfirmed, and access is thought to be through impossibly hidden cave systems like Darkfall Cave.",
        "tags": ["hidden_valley_legendary", "snow_elf_sanctuary_mythical", "glacial_landscape_lost", "falmer_origins_rumored", "unique_ecosystem_rumored", "ancient_ruins_snow_elf_lost", "highly_inaccessible_myth"],
        "demographics": {"Unknown (Legends speak of Falmer, ancient guardians)": 100},
        "travel": {"roads": [], "paths": ["Darkfall Cave system (legendary, undiscovered)"]}
    },
    {
        "id": 118,
        "name": "Soul Cairn (Plane of Oblivion)",
        "desc": "A desolate plane of Oblivion where souls are trapped, often by necromancers or Daedric pacts. A realm of eerie landscapes, undead, and soul husks, rarely accessed by mortals.",
        "tags": ["oblivion_plane_soul_trap", "undead_realm_eternal", "trapped_souls_countless", "vampire_lore_ancient", "necromancy_focus_soul_magic", "unique_otherworldly_bleak", "access_via_dark_ritual_only"],
        "demographics": {"Undead (various spirits, skeletons, wraiths)": 80, "Soul Husks": 10, "Ideal Masters (conceptual rulers)": 10},
        "travel": {"roads": [], "paths": ["Portal via specific, powerful necromantic ritual or vampire pact (extremely rare)"]}
    },
    {
        "id": 119,
        "name": "Castle Volkihar (Ancient Vampire Lair)",
        "desc": "An ancient, imposing fortress on a remote island off the coast of Haafingar, rumored to be the stronghold of a powerful and reclusive vampire clan, the Volkihar. Few who seek it ever return.",
        "tags": ["vampire_stronghold_ancient_legendary", "castle_gothic_remote", "island_fortress_haunted", "volkihar_clan_rumored", "powerful_vampires_ancient", "dangerous_sea_approach"],
        "demographics": {"Volkihar Vampires (ancient and powerful)": 90, "Death Hounds (spectral/undead)": 10},
        "travel": {"roads": [], "paths": ["Boat from Icewater Jetty (Haafingar north coast - perilous journey)"]}
    },
    {
        "id": 120,
        "name": "Fort Dawnguard (Ruined Fortress)",
        "desc": "A ruined fortress in a secluded canyon in The Rift, once belonging to an ancient order of vampire hunters. It is now dilapidated and forgotten, though some say its old purpose might one day be revived.",
        "tags": ["vampire_hunter_hq_ancient_ruined", "fort_ruined_secluded", "dawnguard_order_historic_lost", "military_order_forgotten", "potential_for_restoration_rumor"],
        "demographics": {"Wildlife": 90, "Bandit Scavengers (potential)": 10},
        "travel": {"roads": [], "paths": ["Hidden path through Dayspring Canyon (The Rift)"]}
    },
    {
        "id": 121,
        "name": "Raven Rock (Solstheim)",
        "desc": "A struggling Dunmer settlement on the southern coast of Solstheim, originally an East Empire Company mining colony. Now under the protection of House Redoran, it faces hardship from ashfall and dwindling resources.",
        "tags": ["solstheim_settlement_dunmer", "dunmer_town_colonial", "mining_colony_struggling", "house_redoran_protection", "ashfall_environment_harsh", "morrowind_culture_transplant"],
        "demographics": {"Dunmer": 90, "Nords (few)": 5, "Redoran Guard": 5},
        "travel": {"roads": [], "paths": ["Ship from Windhelm Docks (Solstheim)"]}
    },
    {
        "id": 122,
        "name": "Tel Mithryn (Solstheim)",
        "desc": "The bizarre mushroom tower home of the eccentric but powerful Telvanni wizard, Master Neloth, located in the ashy wastes of Solstheim. A place of strange magical experiments.",
        "tags": ["solstheim_location_telvanni", "telvanni_wizard_tower_mushroom", "mushroom_architecture_magical", "powerful_mage_residence_neloth", "unique_magical_research_site", "ash_spawn_threat_nearby"],
        "demographics": {"Telvanni Wizard (Neloth)": 1, "Apprentice (Talvas Fathryon)": 1, "Ash Spawn (surrounding area)": 98},
        "travel": {"roads": [], "paths": ["Path across Solstheim ashlands (dangerous)"]}
    },
    {
        "id": 123,
        "name": "Apocrypha (Plane of Hermaeus Mora)",
        "desc": "The Daedric plane of Oblivion belonging to Hermaeus Mora, Prince of Knowledge and Fate. A vast, endless library filled with forbidden lore, writhing tentacles, and ghostly Seekers. Access is only through forbidden Black Books.",
        "tags": ["oblivion_plane_hermaeus_mora_library", "endless_library_forbidden_knowledge", "forbidden_knowledge_dangerous", "tentacles_seekers_lurkers_guardians", "unique_otherworldly_books_eldritch", "access_via_black_books_only"],
        "demographics": {"Seekers (guardians of lore)": 70, "Lurkers (behemoths)": 30},
        "travel": {"roads": [], "paths": ["Black Books (portals from Solstheim and Tamriel, rare and hidden)"]}
    },
    # Adding a few more brand new unique locations for 4E 200
    {
        "id": 124,
        "name": "Hall of the Vigilant (Pre-Destruction)",
        "desc": "A fortified lodge near The Pale, serving as a headquarters for the Vigilants of Stendarr in Skyrim. From here, they coordinate their hunts against Daedra, vampires, and other abominations.",
        "tags": ["vigilant_of_stendarr_hq", "fortified_lodge", "daedra_hunter_base", "anti_abomination_order", "religious_military_order", "stendarr_worship"],
        "demographics": {"Vigilants of Stendarr": 100},
        "travel": {"roads": [], "paths": ["Path from Whiterun-Pale border mountains"]}
    },
    {
        "id": 125,
        "name": "Sleeping Giant's Thumb",
        "desc": "A towering rock formation in the plains of Whiterun Hold resembling a colossal thumb, considered a sacred landmark by some local Nord tribes and giants.",
        "tags": ["natural_landmark_rock_formation", "sacred_site_local_tribes", "giant_reverence_site", "plains_landmark", "folklore_location"],
        "demographics": {"Giants (nearby)": 20, "Nord Hunters/Pilgrims (occasional)": 80},
        "travel": {"roads": [], "paths": ["Open plains of Whiterun Hold"]}
    },
    {
        "id": 126,
        "name": "The Karthspire Forsworn Camp", # Distinct from Karthspire mountain itself
        "desc": "A large and heavily fortified Forsworn encampment at the foot of the Karthspire mountain, fiercely guarding the only known path leading towards the rumored Sky Haven Temple.",
        "tags": ["forsworn_stronghold_major", "mountain_base_camp", "guardian_force_blades_ruin", "dangerous_approach", "quest_location_access_point"],
        "demographics": {"Forsworn Warriors": 80, "Forsworn Briarhearts": 10, "Hagravens": 10},
        "travel": {"roads": [], "paths": ["Path from Old Hroldan area"]}
    },
    {
        "id": 127,
        "name": "Dunmeth Pass Watchtower (Skyrim Side)",
        "desc": "A sturdy Imperial watchtower on the Skyrim side of Dunmeth Pass, guarding the treacherous route to Morrowind. Manned by a small Imperial garrison.",
        "tags": ["watchtower_border", "imperial_garrison_remote", "morrowind_border_pass", "strategic_defense_point", "isolated_outpost"],
        "demographics": {"Imperial Soldiers": 100},
        "travel": {"roads": ["Dunmeth Pass Road"], "paths": []}
    },
    {
        "id": 128,
        "name": "Guldun Rock",
        "desc": "A large, isolated rock formation in the volcanic tundra of Eastmarch, riddled with caves that are often used as a den by trolls or other dangerous creatures. Sometimes bandits try to establish a hideout here.",
        "tags": ["rock_formation_volcanic", "cave_system_monster_den", "troll_lair_potential", "bandit_hideout_attempted", "eastmarch_wilderness_danger"],
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