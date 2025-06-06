import json
from typing import Dict, List, Optional
import os # Import the 'os' module to handle file paths

# --- Data Loading (Corrected) ---
def load_json_data(filepath: str) -> dict:
    """Loads data from a JSON file, handling paths correctly."""
    try:
        # Get the directory where this script (locations.py) is located.
        script_dir = os.path.dirname(os.path.realpath(__file__))
        # Construct the full, absolute path to the data file.
        full_path = os.path.join(script_dir, filepath)
        with open(full_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"FATAL ERROR: Data file not found at {full_path}. Ensure 'game_data' directory is in the same folder as your scripts.")
        return {}
    except json.JSONDecodeError:
        print(f"FATAL ERROR: Could not decode JSON from {full_path}. Check for syntax errors.")
        return {}

# Load all location data using the corrected loader
LOCATION_DESCRIPTIONS = load_json_data('game_data/locations/location_descriptions.json')
LOCATION_TAGS = load_json_data('game_data/locations/location_tags.json')
LOCATION_POPULATION_DATA = load_json_data('game_data/locations/location_population.json')
LOCATION_TRAVEL_CONNECTIONS = load_json_data('game_data/locations/location_travel.json')
LOCATION_MISC_ATTRIBUTES = load_json_data('game_data/locations/location_misc_attributes.json')
LOCATION_STRUCTURES = load_json_data('game_data/locations/map_hierarchy.json')


# --- Global Registries ---
ALL_LOCATIONS_INSTANCES: Dict[int, 'Location'] = {}
RAW_LOCATION_DATA_MAP: Dict[int, dict] = {} # This will be rebuilt for compatibility


class Location:
    def __init__(self, id: int, name: str, parent_id: Optional[int] = None):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        
        # Initialize attributes to default values
        self.description: str = "A mysterious place."
        self.travel_desc: str = "A mysterious place."
        self.tags: List[str] = []
        self.demographics: Dict[str, int] = {}
        self.density: str = "sparse"
        self.is_dark: bool = False
        self.exits: Dict[str, 'Location'] = {}
        self.travel_links: dict = {}
        self.sub_location_ids: List[int] = []

    def populate_attributes(self):
        """Populates the location's attributes from the centrally loaded data."""
        desc_data = LOCATION_DESCRIPTIONS.get(str(self.id), {})
        self.description = desc_data.get("desc", self.description)
        self.travel_desc = desc_data.get("travel_desc", self.travel_desc)

        self.tags = LOCATION_TAGS.get(str(self.id), [])

        pop_data = LOCATION_POPULATION_DATA.get(str(self.id), {})
        self.demographics = pop_data.get("demographics", {})
        self.density = pop_data.get("density", "sparse")
        
        self.travel_links = LOCATION_TRAVEL_CONNECTIONS.get(str(self.id), {})

        misc_data = LOCATION_MISC_ATTRIBUTES.get(str(self.id), {})
        self.is_dark = misc_data.get("is_dark", False)

    def add_exit(self, direction: str, location_obj: 'Location'):
        self.exits[direction] = location_obj
        
    def __str__(self) -> str:
        return self.name

def _create_location_objects_recursive(location_data_list: List[dict], parent_obj: Optional[Location] = None):
    """Recursively creates Location objects, populates them, and links them."""
    for loc_data in location_data_list:
        loc_id = loc_data['id']
        
        loc_obj = Location(id=loc_id, name=loc_data['name'], parent_id=parent_obj.id if parent_obj else None)
        loc_obj.populate_attributes()
        
        ALL_LOCATIONS_INSTANCES[loc_id] = loc_obj

        if parent_obj:
            parent_obj.sub_location_ids.append(loc_id)
            misc_attrs = LOCATION_MISC_ATTRIBUTES.get(str(loc_id), {})
            exit_label = misc_attrs.get("exit_label_from_parent", f"Enter {loc_obj.name}")
            parent_obj.add_exit(exit_label, loc_obj)
            
            exit_label_to_parent = misc_attrs.get("exit_label_to_parent", f"Exit to {parent_obj.name}")
            loc_obj.add_exit(exit_label_to_parent, parent_obj)

        if "sub_locations" in loc_data:
            _create_location_objects_recursive(loc_data["sub_locations"], loc_obj)

def _connect_travel_routes():
    """Connects locations based on the travel connections data."""
    for loc_id_str, travel_data in LOCATION_TRAVEL_CONNECTIONS.items():
        loc_id = int(loc_id_str)
        origin_loc = ALL_LOCATIONS_INSTANCES.get(loc_id)
        if not origin_loc: continue

        for link in travel_data.get("links", []):
            dest_name = link.get("name")
            conn_type = link.get("connection_type", "Path")
            
            dest_loc = next((loc for loc in ALL_LOCATIONS_INSTANCES.values() if loc.name == dest_name), None)

            if dest_loc:
                origin_loc.add_exit(f"{conn_type} to {dest_loc.name}", dest_loc)
                dest_loc.add_exit(f"{conn_type} to {origin_loc.name}", origin_loc)

def initialize_skyrim_map() -> Dict[int, Location]:
    """Initializes all locations, populates their data, and connects them."""
    if ALL_LOCATIONS_INSTANCES:
        return ALL_LOCATIONS_INSTANCES

    _create_location_objects_recursive(LOCATION_STRUCTURES)
    _connect_travel_routes()

    for loc_id, loc_obj in ALL_LOCATIONS_INSTANCES.items():
        sub_locs_data = [RAW_LOCATION_DATA_MAP.get(sub_id, {}) for sub_id in loc_obj.sub_location_ids]
        RAW_LOCATION_DATA_MAP[loc_id] = {
            "id": loc_id,
            "name": loc_obj.name,
            "desc": loc_obj.description,
            "travel_desc": loc_obj.travel_desc,
            "tags": loc_obj.tags,
            "demographics": loc_obj.demographics,
            "density": loc_obj.density,
            "is_dark": loc_obj.is_dark,
            "travel": loc_obj.travel_links,
            "sub_locations": sub_locs_data
        }
    return ALL_LOCATIONS_INSTANCES

# To maintain compatibility with scripts that might import from the top-level
LOCATIONS = LOCATION_STRUCTURES