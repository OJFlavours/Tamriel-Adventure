import random

# Location Tags
LOCATIONS = {
    "environment": ["urban", "rural", "wilderness", "coastal", "underground", "aerial", "aquatic"],
    "climate": ["temperate", "tropical", "arid", "arctic", "swampy"],
    "terrain": ["mountainous", "hilly", "plains", "forest", "desert", "island"],
    "structure": ["natural", "ruined", "fortified", "populated", "abandoned"],
    "magical": ["enchanted", "cursed", "holy", "arcane", "tainted"],
    # City Specific tags.
    "city_affiliation": ["whiterun", "riften", "windhelm", "solitude", "markarth", "falkreath", "dawnstar", "winterhold", "morthal"],
    "city_features": ["market", "jarls_seat", "temple", "thieves_guild", "companions_guild", "college", "imperial_presence", "stormcloak_presence", "dwemer_influence"],
    "urban_issues": ["crime", "poverty", "corruption", "political_unrest", "monster_attacks"]
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

def get_random_tag(tag_category):
    """Returns a random tag from the specified category within the master TAGS dictionary."""
    category_dict = TAGS.get(tag_category.upper())  # Access from the new TAGS dictionary
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