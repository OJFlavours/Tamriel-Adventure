# quest_config.py

import json

QUEST_REWARDS_TEMPLATE = {
    "gold": {"min": 50, "max": 150},
    "experience": {"min": 25, "max": 75},
    "item_quality_levels": {
        (1, 5): ["common", "uncommon"],
        (6, 10): ["uncommon", "rare"],
        (11, 20): ["uncommon", "epic"],
        (21, 99): ["epic", "legendary"]
    },
    "reputation": {"min": 5, "max": 15},
    "favor": ["with local Jarl", "with merchant guild", "with College of Winterhold", "with Thieves Guild", "with Companions", "with Imperial Legion", "with Stormcloaks", "with a Daedric Prince (minor)"],
    "prerequisites": [],  # List of quest IDs that must be completed before this quest can be started
    "dependencies": [],   # List of quest IDs that must be active while this quest is active
    "time_limit": None    # Maximum time allowed to complete the quest (in seconds)
}


def load_quest_config(file_path):
    """Loads quest configuration from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
            validate_quest_config(config)
            return config
    except FileNotFoundError:
        print(f"Error: Quest configuration file not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in quest configuration file at {file_path}")
        return None
    except ValueError as e:
        print(f"Error: Invalid quest configuration: {e}")
        return None


def validate_quest_config(config):
    """Validates the quest configuration."""
    if not isinstance(config, dict):
        raise ValueError("Quest configuration must be a dictionary.")
    # Add more validation checks here, e.g., check if required fields are present,
    # if values are of the correct type, etc.
    if "gold" in config and not isinstance(config["gold"], dict):
        raise ValueError("Gold reward must be a dictionary with 'min' and 'max' keys.")
    if "experience" in config and not isinstance(config["experience"], dict):
        raise ValueError("Experience reward must be a dictionary with 'min' and 'max' keys.")
    if "prerequisites" in config and not isinstance(config["prerequisites"], list):
        raise ValueError("Quest prerequisites must be a list of quest IDs.")
    if "dependencies" in config and not isinstance(config["dependencies"], list):
        raise ValueError("Quest dependencies must be a list of quest IDs.")
    if "time_limit" in config and config["time_limit"] is not None and not isinstance(config["time_limit"], (int, float)):
        raise ValueError("Quest time limit must be a number (int or float) in seconds.")