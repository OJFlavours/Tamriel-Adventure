# location_loader.py
import json
import os

def load_location_data():
    """
    Loads all location data from JSON files in the game_data/locations/ directory.
    This function is primarily for verification during development or for direct JSON access.
    The LocationManager in locations.py handles the actual loading into Location objects.
    """
    location_data = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    location_dir = os.path.join(script_dir, "game_data", "locations")
    json_files = [
        "location_descriptions.json", #
        "location_environmental_attributes.json", #
        "location_lore_and_unique_attributes.json", #
        "location_misc_attributes.json", #
        "location_names.json", #
        "location_population.json", #
        "location_tags.json", #
        "location_travel.json", #
        "location_descriptions_deep.json", #
        "map_hierarchy.json" # Important to load this here for complete verification
    ]

    for filename in json_files: #
        filepath = os.path.join(location_dir, filename) #
        key = filename.replace(".json", "") #
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f) #
                location_data[key] = data #
            print(f"Successfully loaded {filename}") #
        except FileNotFoundError:
            print(f"Error: {filename} not found at {filepath}.") #
        except json.JSONDecodeError as e:
            print(f"Error: Could not decode {filename}. Error: {e}") #
        except Exception as e:
            print(f"An unexpected error occurred while loading {filename}: {e}") #

    # Optional: Add a simple check for ID consistency (basic level)
    print("\n--- Basic ID Consistency Check (from location_loader.py) ---")
    
    # Extract all IDs from map_hierarchy for structural verification
    hierarchy_ids = set()
    if 'map_hierarchy' in location_data: #
        def extract_hierarchy_ids(nodes):
            for node in nodes:
                hierarchy_ids.add(node['id']) #
                if 'sub_locations' in node:
                    extract_hierarchy_ids(node['sub_locations']) #
        extract_hierarchy_ids(location_data['map_hierarchy']) #
    else:
        print("Warning: map_hierarchy.json not loaded, cannot perform full ID consistency check.")
        return location_data # Exit if hierarchy is missing

    # Check that all IDs in other JSON files are integers and match hierarchy IDs
    for key, data in location_data.items():
        if key == 'map_hierarchy': # Skip map_hierarchy itself for this check, it's the source
            continue
        if isinstance(data, dict):
            for loc_id_str in data.keys():
                try:
                    loc_id = int(loc_id_str)
                    if loc_id not in hierarchy_ids:
                        print(f"Warning: ID {loc_id} found in {key}.json but not in map_hierarchy.json.")
                except ValueError:
                    print(f"Warning: Non-integer ID '{loc_id_str}' found in {key}.json. This ID will not be loaded by LocationManager.")
        else:
            print(f"Warning: Unexpected data type for {key}.json (expected dict). Skipping ID check for this file.")

    # Check that all IDs in map_hierarchy have corresponding entries in essential files
    essential_files = ['location_names', 'location_descriptions', 'location_descriptions_deep', 'location_tags', 'location_population']
    for loc_id in hierarchy_ids:
        loc_id_str = str(loc_id)
        for essential_file_key in essential_files:
            if essential_file_key in location_data and loc_id_str not in location_data[essential_file_key]:
                print(f"Warning: Location ID {loc_id} from map_hierarchy.json is missing an entry in {essential_file_key}.json.")
    
    print("--- End of Basic ID Consistency Check ---\n")

    return location_data

if __name__ == "__main__":
    # This block will now print status messages to show the loading and basic checks.
    # The actual game will use LocationManager, which has its own loading logic.
    loaded_data = load_location_data()
    # You can add more debugging here if needed, e.g., to print parts of loaded_data