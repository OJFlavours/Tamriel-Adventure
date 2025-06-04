# npc_utils.py
import random
from npc_names import NAME_POOLS
from npc_roles import COMMONER_ROLES, NOBLE_ROLES

def generate_npc_name(race, social_class, gender):
    """Generates a random NPC name based on race, social class, and gender."""
    try:
        name_pool = NAME_POOLS.get(race.lower())
        if not name_pool:
            raise ValueError(f"Invalid race: {race}")

        social_class_pool = name_pool.get(social_class.lower())
        if not social_class_pool:
            raise ValueError(f"Invalid social class: {social_class}")

        name_list = social_class_pool.get(gender.lower())
        if not name_list:
            raise ValueError(f"Invalid gender: {gender}")

        return random.choice(name_list)
    except ValueError as e:
        print(f"Error generating name: {e}")
        return "ErrorName"  # Default error name

def assign_npc_role(social_class):
    """Assigns a random NPC role based on social class."""
    try:
        if social_class.lower() == "noble":
            return random.choice(list(NOBLE_ROLES))
        elif social_class.lower() == "commoner":
            return random.choice(list(COMMONER_ROLES))
        else:
            raise ValueError(f"Invalid social class: {social_class}")
    except ValueError as e:
        print(f"Error assigning role: {e}")
        return "ErrorRole"  # Default error role

# Example of adding a customization option (appearance)
def customize_npc_appearance(npc, appearance_details):
    """Customizes the NPC's appearance based on provided details."""
    try:
        # Example: appearance_details = {"hair_color": "brown", "eye_color": "blue"}
        npc.hair_color = appearance_details.get("hair_color", "brown") # Default to brown if not provided
        npc.eye_color = appearance_details.get("eye_color", "blue") # Default to blue if not provided
        # Add more appearance customization options here
    except Exception as e:
        print(f"Error customizing appearance: {e}")

# Example of basic error handling
def some_npc_function(npc_data):
    """Example function with basic error handling."""
    try:
        if not isinstance(npc_data, dict):
            raise TypeError("NPC data must be a dictionary.")
        # Perform some operations with npc_data
        print("NPC data processed successfully.")
    except TypeError as e:
        print(f"Error processing NPC data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")