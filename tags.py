import random

# Import data from tags_data.py
from tags_data import (
    LOCATIONS,
    FACTIONS,
    NPCS,
    QUESTS,
    EVENTS,
    DIALOGUE,
    ITEMS,
    WORLD_STATE,
    RELATIONSHIPS,
    INHERITABLE_TAGS
)

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
 
def get_random_tag(tag_category: str) -> str | None:
    """Returns a random tag from the specified category within the master TAGS dictionary."""
    category_dict = TAGS.get(tag_category.upper())
    if category_dict:
        if isinstance(category_dict, dict):
            all_values = []
            for sub_category_list in category_dict.values():
                if isinstance(sub_category_list, list):
                    all_values.extend(sub_category_list)
            if all_values:
                return random.choice(all_values)
            else:
                return None # No tags found in sub-categories
        elif isinstance(category_dict, list): # Should not happen with current TAGS structure
            return random.choice(category_dict)
    return None # Category not found

def add_tag(entity: any, tag_category: str, tag_type: str, tag_value: any):
    """Adds a tag to the specified entity (e.g., NPC, Location, Quest) with a nested structure."""
    if not hasattr(entity, "tags"):
        entity.tags = {}
    if tag_category not in entity.tags:
        entity.tags[tag_category] = {}
    entity.tags[tag_category][tag_type] = tag_value

def get_tags(entity: any) -> dict:
    """Returns all tags from an entity."""
    if hasattr(entity, "tags"):
        return entity.tags
    else:
        return {}


def filter_entities_by_tags(entity_list: list, tag_criteria: dict) -> list:
    """Filters a list of entities based on tag criteria."""
    filtered_entities = []
    for entity in entity_list:
        match = True
        entity_tags = get_tags(entity) # Get tags once per entity
        for category, criteria in tag_criteria.items():
            if category not in entity_tags:
                match = False
                break
            
            # Criteria can be a direct value or a dictionary of sub-criteria
            if isinstance(criteria, dict): # e.g., {"LOCATIONS": {"environment": "urban"}}
                if not isinstance(entity_tags.get(category), dict): # Ensure entity's category tags is a dict
                    match = False
                    break
                for sub_category, sub_criteria in criteria.items():
                    if entity_tags[category].get(sub_category) != sub_criteria:
                        match = False
                        break
                if not match: # If inner loop broke
                    break
            elif isinstance(criteria, list): # e.g., {"LOCATIONS": {"environment": ["urban", "coastal"]}} - match any
                # This assumes the entity's tag for this category and type is a single value
                # and we check if it's in the list of criteria.
                # Or, if the entity can have multiple values for a tag type (e.g. entity.tags[category][type] = ["tag1", "tag2"])
                # then we'd check for intersection. For simplicity, assuming single value for now.
                # Let's assume criteria is a list of acceptable values for a specific tag_type.
                # This function's design might need refinement based on how tags are structured and queried.
                # For now, if criteria is a list, we assume it's for a direct tag value, not a sub-category.
                # This part is ambiguous from the original code. Assuming simple value match for now.
                # If LOCATIONS: ["urban", "coastal"] means entity must have BOTH, it's different.
                # If it means entity can have EITHER, it's different.
                # The original code implies direct match or sub-category match.
                # Let's stick to the original logic: if criteria is not a dict, it's a direct value comparison.
                # This means a list as criteria is not directly handled by the original logic for sub-types.
                # For a direct tag (not a sub-category), if criteria is a list, check if entity's tag is in it.
                if entity_tags.get(category) not in criteria: # Example: if entity_tags["FACTIONS"]["type"] must be in ["military", "religious"]
                    match = False
                    break
            else: # Direct value comparison
                # This case is tricky if entity_tags[category] is a dict itself (e.g. for LOCATIONS)
                # The original code seems to imply this for non-dict criteria.
                # This would only work if entity_tags[category] was a simple value, not a dict of types.
                # Given the structure of TAGS, entity_tags[category] is usually a dict.
                # This path in the original logic might be flawed or intended for simpler tag structures.
                # For safety, let's assume if criteria is not a dict, we are checking a direct value of a top-level category if it's not a dict.
                # However, all our top-level TAGS categories ARE dicts.
                # This suggests `tag_criteria` should always have dicts for categories like LOCATIONS, FACTIONS, etc.
                # e.g. {"LOCATIONS": {"environment": "urban"}, "FACTIONS": {"type": "military"}}
                # If criteria is like {"FACTION_ALIGNMENT": "good"}, this won't work with current TAGS.
                # Re-evaluating: The original code's `elif entity_tags[category] != criteria:` implies
                # that `entity_tags[category]` is expected to be a simple value if `criteria` is not a dict.
                # This is inconsistent with how `add_tag` stores them (always `entity.tags[category][tag_type] = tag_value`).
                #
                # Let's assume the intent for non-dict criteria is to check if ANY tag_type within that category matches.
                # This is still an assumption. A clearer query structure would be better.
                # For now, to maintain some functionality, if criteria is not a dict,
                # we'll assume it's a value that one of the tag_types in that category should match.
                found_in_subtypes = False
                if isinstance(entity_tags.get(category), dict):
                    for sub_val in entity_tags[category].values():
                        if sub_val == criteria:
                            found_in_subtypes = True
                            break
                    if not found_in_subtypes:
                        match = False
                        break
                elif entity_tags.get(category) != criteria: # If entity_tags[category] is somehow a direct value
                     match = False
                     break


        if match:
            filtered_entities.append(entity)
    return filtered_entities

def generate_quest_from_tags(quest_giver: str, quest_location: str, quest_type: str, quest_difficulty: str) -> dict:
    """Generates a quest dictionary based on specified tags."""
    # This is a placeholder. In a real system, this would likely create an instance of a Quest class.
    quest_dict = {} 
    add_tag(quest_dict, "QUESTS", "giver", quest_giver) # Using "QUESTS" as category to match TAGS
    add_tag(quest_dict, "QUESTS", "location", quest_location)
    add_tag(quest_dict, "QUESTS", "type", quest_type)
    add_tag(quest_dict, "QUESTS", "difficulty", quest_difficulty)
    # Example: add_tag(quest_obj, "QUESTS", "objective_type", "item_artifact")
    return quest_dict

def generate_event_from_tags(event_location: str, event_type: str, event_scale: str) -> dict:
    """Generates an event dictionary based on specified tags."""
    # Placeholder for Event object creation
    event_dict = {}
    add_tag(event_dict, "EVENTS", "location", event_location) # Using "EVENTS" as category
    add_tag(event_dict, "EVENTS", "type", event_type)
    add_tag(event_dict, "EVENTS", "scale", event_scale)
    return event_dict

def get_dialogue_options(npc: any, player_relationship: dict) -> list: # player_relationship might be an object or dict
    """Generates dialogue options based on NPC tags and player relationship."""
    options = []
    # This is a placeholder. Actual logic would be more complex.
    npc_tags = get_tags(npc)
    
    # Example: Accessing NPC's attitude tag
    npc_attitude = npc_tags.get("NPCS", {}).get("attitude", "neutral")
    
    options.append(f"Ask about local rumors. (Attitude: {npc_attitude})")
    
    # Example: Accessing a specific dialogue tone from TAGS
    persuasion_tone = TAGS.get("DIALOGUE", {}).get("tone", [])
    if "persuasion" in TAGS.get("DIALOGUE", {}).get("topic", []): # Check if persuasion is a topic
        options.append(f"Attempt to persuade. (Tone: {random.choice(persuasion_tone) if persuasion_tone else 'neutral'})")

    # Example based on player relationship (assuming player_relationship has 'type' and 'trust')
    rel_type = player_relationship.get("type", "stranger")
    rel_trust = player_relationship.get("trust", "none")
    if rel_type == "friend" and rel_trust == "high":
        options.append("Share a personal story.")
    
    return options

def get_all_tags_by_category(category: str) -> list:
    """Returns a list of all valid tags within a specified category from the master TAGS dictionary."""
    category_data = TAGS.get(category.upper())
    if category_data:
        if isinstance(category_data, dict): # e.g., LOCATIONS, FACTIONS
            all_tags_in_category = []
            for sub_category_key, sub_category_list_of_tags in category_data.items():
                if isinstance(sub_category_list_of_tags, list):
                    all_tags_in_category.extend(sub_category_list_of_tags)
            return list(set(all_tags_in_category)) # Return unique tags
        elif isinstance(category_data, list): # Should not happen with current TAGS structure
            return category_data
    return []

def remove_tag(entity: any, tag_category: str, tag_type: str):
    """Removes a specific tag type from an entity's tag category."""
    if hasattr(entity, "tags") and tag_category in entity.tags:
        if isinstance(entity.tags[tag_category], dict) and tag_type in entity.tags[tag_category]:
            del entity.tags[tag_category][tag_type]
            if not entity.tags[tag_category]: # If the category dict becomes empty
                del entity.tags[tag_category]
        # If entity.tags[tag_category] was not a dict or tag_type wasn't in it, do nothing.

# Expose key variables for other modules if they were importing them directly
# (though using functions like get_all_tags_by_category is preferred)
__all__ = [
    "TAGS",
    "LOCATIONS",
    "FACTIONS",
    "NPCS",
    "QUESTS",
    "EVENTS",
    "DIALOGUE",
    "ITEMS",
    "WORLD_STATE",
    "RELATIONSHIPS",
    "INHERITABLE_TAGS",
    "get_random_tag",
    "add_tag",
    "get_tags",
    "filter_entities_by_tags",
    "generate_quest_from_tags",
    "generate_event_from_tags",
    "get_dialogue_options",
    "get_all_tags_by_category",
    "remove_tag"
]