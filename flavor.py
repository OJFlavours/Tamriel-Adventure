import random
from tags import get_tags, TAGS # Import get_tags and TAGS
from flavor_data import * # Import flavor vignettes

def get_flavor(entity):
    """
    Retrieves a random flavor text vignette for a given entity based on its tags.
    The entity is expected to have a 'tags' attribute, which is a dictionary
    mapping tag categories (e.g., "location", "npc") to sub-dictionaries of tags.
    
    Example entity.tags structure:
    entity.tags = {
        "location": {"environment": ["urban", "city"], "climate": ["temperate"]},
        "npc": {"race": ["nord"], "class": ["warrior"]}
    }
    """
    entity_tags = get_tags(entity)

    # Prioritize inn-specific flavor texts
    if hasattr(entity, 'tags') and "npc" in entity.tags and "location" in entity.tags:
        if "role" in entity.tags["npc"] and "innkeeper" in entity.tags["npc"]["role"]:
            location_name = entity.tags["location"].get("name", "").lower().replace(" ", "_")
            inn_flavor_key = "location_specific_" + location_name
            if inn_flavor_key in LOCATION_FLAVORS["unique_establishments"]:
                return [random.choice(LOCATION_FLAVORS["unique_establishments"][inn_flavor_key])]
    possible_vignettes = []

    # Iterate through the entity's tag categories
    for tag_category, tag_types_dict in entity_tags.items():
        # Check if this tag category exists in the master LOCATION_FLAVORS
        if tag_category in LOCATION_FLAVORS:
            category_flavors = LOCATION_FLAVORS[tag_category]
            
            # Iterate through the specific tag types within this category (e.g., "environment", "race")
            for tag_type, actual_tags in tag_types_dict.items():
                # Ensure actual_tags is always a list for iteration
                if not isinstance(actual_tags, list):
                    actual_tags = [actual_tags] # Make it a list if it's a single string

                # Check if this tag_type exists in the category's flavors
                if tag_type in category_flavors:
                    type_flavors = category_flavors[tag_type]
                    
                    # Iterate through the actual tags (e.g., "urban", "nord")
                    for tag in actual_tags:
                        if tag in type_flavors:
                            possible_vignettes.extend(type_flavors[tag])
    
    if possible_vignettes:
        print("Flavor Text:", possible_vignettes[0])
        return [random.choice(possible_vignettes)]
    return []

# Example usage (for testing purposes within flavor.py)
if __name__ == "__main__":
    # Mock entity for testing
    class MockEntity:
        def __init__(self, tags_dict):
            self.tags = tags_dict

    # Test with a location entity
    location_entity = MockEntity({
        "location": {
            "environment": ["urban"],
            "climate": ["temperate"]
        }
    })
    print("Location Flavor:", get_flavor(location_entity))

    # Test with an NPC entity
    npc_entity = MockEntity({
        "npc": {
            "race": ["nord"],
            "class": ["warrior"],
            "attitude": ["friendly"]
        }
    })
    print("NPC Flavor:", get_flavor(npc_entity))

    # Test with a quest entity
    quest_entity = MockEntity({
        "quest": {
            "type": ["fetch"],
            "difficulty": ["medium"]
        }
    })
    print("Quest Flavor:", get_flavor(quest_entity))

    # Test with no matching tags
    no_tags_entity = MockEntity({
        "nonexistent": {"type": ["invalid"]}
    })
    print("No Matching Flavor:", get_flavor(no_tags_entity))

    # Test with mixed tags
    mixed_entity = MockEntity({
        "location": {"environment": ["forest"]},
        "npc": {"attitude": ["hostile"]}
    })
    print("Mixed Flavor:", get_flavor(mixed_entity))

def get_flavor_text(item_name):
    """
    Retrieves a random flavor text vignette for a given item name.
    """
    if item_name in ITEM_FLAVORS:
        return random.choice(ITEM_FLAVORS[item_name])
    return None
