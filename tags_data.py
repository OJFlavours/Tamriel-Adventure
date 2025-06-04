# tags_data.py

# Location Tags
LOCATIONS = {
    "environment": ["urban", "rural", "wilderness", "coastal", "underground", "aerial", "aquatic", "volcanic_tundra", "glacial", "ashland", "geothermal_area", "mountain_valley", "subterranean_city", "otherworldly_plane"],
    "climate": ["temperate", "tropical", "arid", "arctic", "swampy", "volcanic_geothermal", "subarctic", "alpine", "temperate_coastal", "temperate_continental", "arctic_coastal", "subarctic_volcanic", "glacial_extreme_weather", "alpine_extreme_weather"],
    "terrain": ["mountainous", "hilly", "plains", "forest", "desert", "island", "canyon", "geyser_field", "hot_springs", "marsh", "tundra_plains", "cliffside", "river_delta", "mountain_pass", "ice_field", "ash_waste", "river_gorge", "volcanic_slope", "ashfall_zone", "mountain_peak", "mountain_ridge", "lake_shoreline", "cove_hidden", "wasteland_barren", "subterranean_cavern_network"],
    "structure_type": ["natural_cave", "natural_grotto", "ruined_fort", "ruined_tower", "ruined_settlement", "ruined_shrine", "fortified_keep", "fortified_city_wall", "populated_city", "populated_town", "populated_village", "abandoned_shack", "abandoned_mine", "settlement_minor", "outpost_military", "outpost_civilian", "shack_or_hut", "tower_structure", "bridge_structure", "shipwreck_site", "lighthouse_structure", "mine_active", "mine_depleted", "cave_entrance_prominent", "monument_historic_site", "standing_stone_circle", "shrine_outdoor_structure", "wall_ancient_structure", "farmstead", "meadery_building", "apiary_location", "lumber_mill_site", "fishing_dock", "smelter_works", "prison_building", "barracks_building", "library_archive_building", "museum_building", "catacombs_structure", "arena_structure", "palace_or_manor", "temple_building", "guild_hall_building", "shop_building", "inn_building", "stable_building", "dwemer_city_repurposed", "cave_system_fortified", "longhouse_generic", "wizard_tower", "lodge_building", "prison_mine_combined", "community_hall", "embassy_office", "watchtower_fortified", "ship_generic", "colossal_statue", "monastery_building", "excavation_site", "warehouse_building", "orphanage_building"],
    "structure_condition": ["pristine", "well_maintained", "weathered", "damaged", "ruined_extensively", "collapsed", "overgrown", "flooded", "frozen_over", "ash_covered", "haunted_aura", "recently_looted", "under_construction", "newly_built", "abandoned_dangerous", "sealed_inaccessible", "fortified_private_residence", "functional_active", "dilapidated", "desecrated", "partially_submerged"],
    "magical_properties": ["enchanted_positive", "enchanted_neutral", "enchanted_negative", "cursed_major", "cursed_minor", "holy_ground_aedric", "unholy_ground_daedric", "arcane_nexus", "tainted_by_dark_magic", "elemental_fire_dominant", "elemental_frost_dominant", "elemental_shock_dominant", "wild_magic_zone", "null_magic_zone", "daedric_influence_subtle", "daedric_influence_overt", "aedric_blessing_active", "ancient_wards_active", "geomantic_power_spot", "ritual_site_active", "otherworldly_influence", "prophetic_site", "soul_trap_magic_dominant", "necromancy_focus", "illusion_magic_strong"],
    "city_affiliation": ["whiterun_hold_capital", "riften_city", "windhelm_city", "solitude_city", "markarth_city", "falkreath_town", "dawnstar_town", "winterhold_town_ruined", "morthal_town", "eastmarch_capital", "the_reach_capital", "haafingar_capital", "the_rift_capital"],
    "settlement_features": ["market_square", "jarls_longhouse", "temple_divines", "temple_specific_god", "thieves_guild_presence", "companions_guild_hall", "college_of_winterhold_main", "mages_guild_local_hall", "imperial_legion_hq", "stormcloak_army_hq", "dwemer_architecture_prominent", "docks_harbor", "warehouse_storage", "slums_poor_district", "noble_estate_district", "military_garrison_active", "prison_jailhouse", "smelter_industrial", "apiary_honey_farm", "lumber_mill_active", "fishing_community_hub", "alchemy_shop_notable", "blacksmith_forge_active", "library_public_or_private", "museum_artifacts", "catacombs_burial", "arena_combat_local", "barracks_guards", "player_home_available", "unique_landmark_iconic", "ethnic_district", "smelter_active", "training_facility", "sleeping_quarters_communal", "port_major", "east_empire_company_office", "armory_barracks", "chieftains_hall", "named_ship_docked"],
    "urban_issues_or_atmosphere": ["high_crime_rate", "pervasive_poverty", "rampant_corruption", "political_tension_high", "frequent_monster_raids", "racial_tension_overt", "fear_and_superstition", "bustling_trade_atmosphere", "oppressive_atmosphere", "scholarly_atmosphere", "militaristic_atmosphere", "pious_atmosphere", "decadent_atmosphere", "secretive_atmosphere", "haunted_rumors_strong", "eerie_silence", "social_unrest_simmering", "tense_atmosphere", "desperation_squalor", "brutal_conditions"],
    "economic_activity": ["mining_iron", "mining_silver", "mining_gold", "mining_ebony", "mining_malachite", "mining_quicksilver", "mining_moonstone", "mining_corundum", "mining_gems", "logging_timber", "farming_crops", "farming_livestock", "fishing_industry_local", "trade_hub_major", "trade_hub_minor", "alchemy_ingredient_source_rich", "smithing_center_renowned", "brewing_mead_ale", "skooma_trade_illicit", "smuggling_route_active", "hunting_furs_meat", "caravan_stopover", "shipbuilding_port", "ore_processing", "tailoring_services", "fletching_services", "skooma_production_illicit", "contraband_storage", "manual_labor", "fishing_subsistence", "brewing_potions", "enchanting_services", "horse_breeding_sales", "shipping_industry", "trade_variety_limited", "trade_variety_extensive", "trade_local_shady", "smithing_production_skilled", "crafting_specialty"],
    "cultural_historical_significance": ["nordic_settlement_ancient", "nordic_burial_site_major", "dwemer_ruin_major_city", "dwemer_outpost_minor", "dragon_cult_temple_ruin", "dragon_cult_lair_priest", "forsworn_ancestral_site", "orc_stronghold_traditional", "imperial_fort_historic", "stormcloak_rebellion_site", "battlefield_major_historic", "pilgrimage_site_religious", "legendary_hero_location", "sacred_grove_kynareth", "daedric_shrine_prominent", "natural_wonder_revered", "ancient_magical_site", "great_collapse_affected_site", "ysgramor_related_site", "nightingale_shrine_hidden", "dwemer_architecture_prominent", "reachmen_culture_strong", "orcish_culture_strong", "blades_historical_site", "tiber_septim_linked_site", "local_folk_tale_site", "prophetic_site_rumored", "dragon_lore_site_ancient", "oblivion_crisis_related", "vampire_hunter_order_historic", "creation_myth_site", "local_legend_tragic", "ancient_religious_site_unknown_deity", "historic_burial_site_minor", "battlefield_minor_historic", "historic_marker_somber", "night_of_tears_related_rumor"],
    "state_or_condition_current": ["contested_by_factions", "active_warzone_nearby", "peaceful_and_prosperous", "isolated_and_forgotten", "densely_populated_urban", "sparsely_populated_rural", "recently_attacked_recovering", "under_siege_rumored", "plague_outbreak_rumored", "supernatural_event_ongoing", "economically_depressed", "politically_stable", "politically_unstable", "heavily_guarded", "lightly_patrolled", "lawless_area", "neutral_territory_faction", "thalmor_controlled_area", "forsworn_controlled_area", "bandit_controlled_area", "giant_territory", "dragon_sighting_recent_rumor", "frequent_raids_local", "dynamic_faction_control_potential", "abandoned_due_to_danger", "struggling_community", "enemy_controlled_area", "vigilant_controlled_area", "highly_dangerous_inaccessible"],
    "specific_landmark_type": ["dragon_lair_active_story", "dragon_lair_ancient_inactive", "dragon_burial_site_mound", "giant_camp_established", "hagraven_coven_lair_main", "spriggan_sanctuary", "vampire_ancient_lair", "vampire_coven_minor", "necromancer_tower_or_lair", "bandit_main_stronghold", "bandit_minor_camp", "smuggler_main_den", "smuggler_cache_minor", "pirate_ship_base", "pirate_cove_hidden", "word_wall_location", "standing_stone_magical", "unique_natural_formation", "quest_specific_dungeon_entrance", "blackreach_elevator_access", "dragon_priest_lair", "faction_guild_hq", "scholar_residence_notable", "named_ship_unique", "lunar_forge", "atronach_forge_location", "silver_hand_hq", "mythic_dawn_museum_shrine", "vampire_hunter_hq_ruined", "rock_formation_unique", "bridge_ancient_landmark", "waterfall_location_scenic", "volcanic_crater", "geothermal_vent_cave", "bioluminescent_cave", "ice_cave_crystal", "hidden_grove_magical", "ancestral_tomb_named_hero", "battle_monument", "ancient_battlefield_marker", "sacred_tree_unique", "colossal_statue_daedric", "otherworldly_portal_site", "arena_ritualistic", "fortified_outpost_border", "lighthouse_functional_navigational", "ship_imperial_warship_major", "ship_pirate_notorious"],
    "unique_establishments": ["location_specific_vilemyr_inn", "location_specific_windpeak_inn", "location_specific_silver_blood_inn", "location_specific_moorside_inn", "location_specific_winking_skeever", "location_specific_nightgate_inn", "location_specific_dead_mans_drink", "location_specific_braidwood_inn"], # For highly specific named location flavor
    "resources": ["ore_vein", "timber_source", "hunting_ground", "farmland"]
}

# Faction Tags
FACTIONS = {
    "type": ["military", "religious", "criminal", "political", "mercantile", "tribal", "academic"],
    "alignment": ["good", "evil", "neutral", "lawful", "chaotic"],
    "size": ["small", "medium", "large", "massive"],
    "influence": ["local", "regional", "national", "global"],
    "status": ["active", "inactive", "growing", "declining", "secret"]
}

# NPC Tags
NPCS = {
    "class": ["warrior", "mage", "thief", "rogue", "priest", "merchant", "bard", "scholar", "peasant", "noble", "monster"],
    "attitude": ["friendly", "hostile", "neutral", "cautious", "greedy", "honest", "deceitful", "fanatical", "zealous", "eccentric", "mysterious"],
    "race": ["nord", "imperial", "breton", "redguard", "dunmer", "altmer", "bosmer", "orc", "argonian", "khajiit", "dwemer", "giant", "goblin"],
    "condition": ["healthy", "injured", "sick", "cursed", "possessed", "wealthy", "poor", "insane", "powerful", "weak"],
    "personality": ["brave", "cowardly", "intelligent", "foolish", "optimistic", "pessimistic", "ambitious", "lazy", "loyal", "treacherous"],
    "enemy_type": ["undead", "humanoid", "animal", "daedra", "dragon"],
    "profession": ["blacksmith", "alchemist", "enchanter", "trainer"]
}

# Quest Tags
QUESTS = {
    "type": ["fetch", "escort", "rescue", "investigate", "hunt", "assassinate", "raid", "defend", "explore", "deliver", "negotiate", "diplomacy", "spy"],
    "objective": ["item", "person", "location", "information", "artifact"],
    "reward": ["gold", "item", "knowledge", "favor", "title", "land", "power", "reputation", "experience"],
    "difficulty": ["easy", "medium", "hard", "dangerous", "impossible", "trivial"],
    "urgency": ["urgent", "important", "routine", "optional", "trivial", "critical"],
    "moral": ["ethical", "unethical", "gray"]
}

# Event Tags
EVENTS = {
    "type": ["battle", "festival", "storm", "earthquake", "plague", "fire", "discovery", "invasion", "assassination", "ritual", "election", "migration", "economic"],
    "scale": ["minor", "major", "global", "regional", "local"],
    "impact": ["positive", "negative", "neutral", "economic", "social", "political"],
    "frequency": ["rare", "common", "annual", "unpredictable"],
    "duration": ["short", "medium", "long", "permanent"]
}

# Dialogue Tags
DIALOGUE = {
    "tone": ["formal", "informal", "aggressive", "friendly", "sarcastic", "humorous", "serious", "mysterious", "threatening", "pleading"],
    "topic": ["gossip", "rumor", "lore", "quest", "trade", "persuasion", "threat", "flattery", "bargaining", "accusation", "apology", "complaint"],
    "speaker": ["npc", "player"],
    "result": ["success", "failure", "partial", "information", "alliance", "enemy", "agreement", "disagreement", "compromise"],
    "emotional": ["happy", "sad", "angry", "fearful", "surprised", "disgusted"]
}

# Item Tags
ITEMS = {
    "type": ["weapon", "armor", "potion", "scroll", "food", "tool", "artifact", "container", "ingredient"],
    "material": ["iron", "steel", "silver", "elven", "dwarven", "glass", "ebony", "dragonbone", "daedric", "wood", "leather", "cloth"],
    "quality": ["common", "uncommon", "rare", "epic", "legendary"],
    "properties": ["magical", "enchanted", "cursed", "poisoned", "holy", "flammable", "fragile", "durable"],
    "size": ["small", "medium", "large"],
    "effects": ["healing", "damage", "buff", "debuff"],
    "restrictions": ["equippable_by_race", "equippable_by_class"]
}

# World State Tags
WORLD_STATE = {
    "faction_relations": ["alliance", "war", "trade", "neutral", "rivalry"],
    "economic_stability": ["prosperous", "stable", "struggling", "depressed"],
    "political_climate": ["peaceful", "tense", "unstable", "tyrannical", "democratic"],
    "magical_influence": ["strong", "weak", "growing", "waning"],
    "monster_activity": ["low", "medium", "high"]
}

# Relationship Tags (Between NPCs or Player and NPC)
RELATIONSHIPS = {
    "type": ["friend", "enemy", "ally", "rival", "lover", "family", "acquaintance", "stranger"],
    "trust": ["high", "medium", "low", "none"],
    "attitude": ["positive", "negative", "neutral"]
}

# Combat Tags
COMBAT = {
    "damage_type": ["fire_damage", "frost_damage", "shock_damage", "poison_damage", "physical_damage"]
}

# Set of tags that can be inherited from parent locations
INHERITABLE_TAGS = {
    "nordic", "imperial", "stormcloak", "thieves_guild_presence", "corrupt_influence", # Faction/Influence
    "military_presence", "bards_college_influence", "mages_guild_influence",
    "city", "town", "village", "hold", # Settlement Types
    "plains", "central_location", "snowy_region", "coastal_area", "magical_aura", # Environment/Geography
    "marshland", "swamp_terrain", "forested_area", "southern_region", "mountainous_terrain",
    "dwemer_ruins_nearby", "volcanic_activity", "water_dominant_landscape", # Specific Features
    "urban", "rural", "wilderness", "underground", # General Environment
    "temperate", "arctic", "arid", # Climate
    "fortified", "populated", "abandoned", "ruined", # Structure Status
    "enchanted", "cursed", "holy_site", "arcane_focus", "tainted_area" # Magical properties
}