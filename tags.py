import random

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
    "specific_landmark_type": ["dragon_lair_active_story", "dragon_lair_ancient_inactive", "dragon_burial_site_mound", "giant_camp_established", "hagraven_coven_lair_main", "spriggan_sanctuary", "vampire_ancient_lair", "vampire_coven_minor", "necromancer_tower_or_lair", "bandit_main_stronghold", "bandit_minor_camp", "smuggler_main_den", "smuggler_cache_minor", "pirate_ship_base", "pirate_cove_hidden", "word_wall_location", "standing_stone_magical", "unique_natural_formation", "quest_specific_dungeon_entrance", "blackreach_elevator_access", "dragon_priest_lair", "faction_guild_hq", "scholar_residence_notable", "named_ship_unique", "lunar_forge", "atronach_forge_location", "silver_hand_hq", "mythic_dawn_museum_shrine", "vampire_hunter_hq_ruined", "rock_formation_unique", "bridge_ancient_landmark", "waterfall_location_scenic", "volcanic_crater", "geothermal_vent_cave", "bioluminescent_cave", "ice_cave_crystal", "hidden_grove_magical", "ancestral_tomb_named_hero", "battle_monument", "ancient_battlefield_marker", "sacred_tree_unique", "colossal_statue_daedric", "otherworldly_portal_site", "arena_ritualistic", "fortified_outpost_border", "lighthouse_functional_navigational", "ship_imperial_warship_major", "ship_pirate_notorious"]
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
    "personality": ["brave", "cowardly", "intelligent", "foolish", "optimistic", "pessimistic", "ambitious", "lazy", "loyal", "treacherous"]
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
    "size": ["small", "medium", "large"]
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

# Master TAGS dictionary for universal compatibility
TAGS = {
    "LOCATIONS": LOCATIONS,
    "FACTIONS": FACTIONS,
    "NPCS": NPCS,
    "QUESTS": QUESTS,
    "EVENTS": EVENTS,
    "DIALOGUE": DIALOGUE,
    "ITEMS": ITEMS,
    "WORLD_STATE": WORLD_STATE,
    "RELATIONSHIPS": RELATIONSHIPS,
}

# Set of tags that can be inherited from parent locations (e.g., Hold to City, City to Venue)
# for contextual flavor text or other game logic.
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
 
def get_random_tag(tag_category):
    """Returns a random tag from the specified category within the master TAGS dictionary."""
    category_dict = TAGS.get(tag_category.upper())
    if category_dict:
        # If the category is a dictionary (like LOCATIONS, FACTIONS, etc.),
        # we want to pick a random value from one of its sub-categories.
        # For example, if tag_category is "LOCATIONS", we might pick a random
        # environment tag like "urban".
        if isinstance(category_dict, dict):
            # Get all possible values from all sub-categories
            all_values = []
            for sub_category_list in category_dict.values():
                all_values.extend(sub_category_list)
            if all_values:
                return random.choice(all_values)
            else:
                return None
        # If the category itself is a list (though currently all are dictionaries),
        # this would handle it.
        elif isinstance(category_dict, list):
            return random.choice(category_dict)
    return None

def add_tag(entity, tag_category, tag_type, tag_value):  # Modified to accept tag_type and tag_value
    """Adds a tag to the specified entity (e.g., NPC, Location, Quest) with a nested structure."""
    if not hasattr(entity, "tags"):
        entity.tags = {}
    if tag_category not in entity.tags:
        entity.tags[tag_category] = {}  # Initialize as a dictionary for nested tags
    entity.tags[tag_category][tag_type] = tag_value  # Assign the tag_value to the specific type

def get_tags(entity):
    """returns all tags from an entity"""
    if hasattr(entity, "tags"):
        return entity.tags
    else:
        return {}

def get_flavor(entity, flavor_file):
    """Returns the flavor text for the entity"""
    # This function would typically interact with the flavor module
    # to get flavor text based on the entity's tags.
    # Assuming flavor_file has a get_flavor method.
    return flavor_file.get_flavor(entity)


def filter_entities_by_tags(entity_list, tag_criteria):
    """Filters a list of entities based on tag criteria."""
    filtered_entities = []
    for entity in entity_list:
        match = True
        for category, criteria in tag_criteria.items():
            entity_tags = get_tags(entity)
            if category not in entity_tags:
                match = False
                break
            if isinstance(criteria, dict):
                for sub_category, sub_criteria in criteria.items():
                    if sub_category not in entity_tags[category] or entity_tags[category][sub_category] != sub_criteria:
                        match = False
                        break
                if not match:
                    break
            elif entity_tags[category] != criteria:
                match = False
                break
        if match:
            filtered_entities.append(entity)
    return filtered_entities

def generate_quest_from_tags(quest_giver, quest_location, quest_type, quest_difficulty):
    """Generates a quest based on specified tags."""
    quest = {}  # Replace with your Quest object creation
    # Call add_tag with tag_type and tag_value
    add_tag(quest, "quest", "giver", quest_giver)
    add_tag(quest, "quest", "location", quest_location)
    add_tag(quest, "quest", "type", quest_type)
    add_tag(quest, "quest", "difficulty", quest_difficulty)
    return quest

def generate_event_from_tags(event_location, event_type, event_scale):
    """Generates an event based on specified tags."""
    event = {}  # Replace with your Event object creation
    # Call add_tag with tag_type and tag_value
    add_tag(event, "event", "location", event_location)
    add_tag(event, "event", "type", event_type)
    add_tag(event, "event", "scale", event_scale)
    return event

def get_dialogue_options(npc, player_relationship):
    """Generates dialogue options based on NPC tags and player relationship."""
    options = []  # Replace with your dialogue option generation logic
    # This is a placeholder - you'll need to define how dialogue options
    # are generated based on the tags and relationship.  This might
    # involve looking up dialogue snippets in a database.
    npc_tags = get_tags(npc)
    # Access DIALOGUE from the new TAGS dictionary
    # Example adjusted to new tag structure assuming 'location' is a tag category
    # options.append(f"Ask about rumors in the {npc_tags.get('location', {}).get('environment', 'area')}")
    options.append(f"Ask about rumors in the area")  # Simplified, as specific location tags are complex here
    options.append(f"Attempt to {TAGS['DIALOGUE'].get('persuasion')}")
    return options

def get_all_tags_by_category(category):
    """Returns a list of all valid tags within a specified category from the master TAGS dictionary."""
    category_dict = TAGS.get(category.upper())  # Access from the new TAGS dictionary
    if category_dict:
        # If it's a dictionary of lists (like LOCATIONS), return all values from all sub-categories
        if isinstance(category_dict, dict):
            all_tags = []
            for sub_category_list in category_dict.values():
                all_tags.extend(sub_category_list)
            return all_tags
        # If it's a direct list (not currently the case for top-level categories, but for completeness)
        elif isinstance(category_dict, list):
            return category_dict
    else:
        return []

def remove_tag(entity, tag_category, tag_type):  # Modified to accept tag_type
    """Removes a tag from a specific entity."""
    if hasattr(entity, "tags") and tag_category in entity.tags:
        if tag_type in entity.tags[tag_category]:
            del entity.tags[tag_category][tag_type]
            # Optionally remove the category if it becomes empty
            if not entity.tags[tag_category]:
                del entity.tags[tag_category]