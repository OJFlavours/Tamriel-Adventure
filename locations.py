# locations.py
import json
import os
from typing import Dict, List, Optional

# REMOVED: Imports of individual Python location files (e.g., locations_whiterun.py)

class Location:
    """Represents a single location in the game world."""
    def __init__(self, loc_data: dict, parent_id: Optional[int] = None):
        self.id = loc_data.get('id')
        self.name = loc_data.get('name')
        self.parent_id = parent_id
        self.sub_location_ids: List[int] = [sub.get('id') for sub in loc_data.get('sub_locations', []) if sub.get('id') is not None]

        # Initialize attributes to default values
        self.description: str = "A mysterious place."
        self.travel_desc: str = "A mysterious place."
        self.deep_description: str = "" # New attribute
        self.secret_description: str = "" # New attribute
        self.tags: List[str] = []
        self.demographics: Dict[str, int] = {}
        self.density: str = "sparse"
        self.travel: dict = {}
        self.context_tags: List[str] = []
        self.exit_label_from_parent: str = f"Exit to parent of {self.name}" # Default changed for clarity
        self.exit_label_to_parent: str = f"Enter {self.name}" # Default changed for clarity
        self.exits: Dict[str, 'Location'] = {}
        self.travel_time: int = 60 # Default travel time in minutes, can be overridden by travel data

    def populate_attributes_from_data(self, data_sources: dict):
        """Populates the location's attributes from various data sources."""
        loc_id_str = str(self.id)
        
        # Start with a base, which for a JSON-only system comes from map_hierarchy name if no other name exists.
        # However, for attributes, we'll primarily rely on explicit JSON files.
        merged_data = {} # Initialize empty, as Python lists are no longer the primary data source

        # Overlay data from all JSON files. JSON data takes precedence.
        # Load names from names.json, prioritize it if it exists for the ID
        self.name = data_sources['names'].get(loc_id_str, self.name) #

        # General descriptions (desc, travel_desc)
        if loc_id_str in data_sources['descriptions']:
            merged_data.update(data_sources['descriptions'][loc_id_str]) #

        # Deep descriptions (deep_description, secret_description)
        if loc_id_str in data_sources['deep_descriptions']:
            merged_data.update(data_sources['deep_descriptions'][loc_id_str]) #

        # Environmental attributes
        if loc_id_str in data_sources['environmental']:
            merged_data.update(data_sources['environmental'][loc_id_str]) #

        # Lore and unique attributes
        if loc_id_str in data_sources['lore_unique']:
            merged_data.update(data_sources['lore_unique'][loc_id_str]) #

        # Miscellaneous attributes
        if loc_id_str in data_sources['misc']:
            merged_data.update(data_sources['misc'][loc_id_str]) #

        # Population data
        if loc_id_str in data_sources['population']:
            merged_data.update(data_sources['population'][loc_id_str]) #
        
        # Assign attributes from the merged_data
        self.description = merged_data.get('desc', self.description) #
        self.travel_desc = merged_data.get('travel_desc', self.travel_desc) #
        self.deep_description = merged_data.get('deep_description', self.deep_description) #
        self.secret_description = merged_data.get('secret_description', self.secret_description) #
        self.demographics = merged_data.get('demographics', self.demographics) #
        self.density = merged_data.get('density', self.density) #

        # Tags: direct assignment from location_tags.json
        self.tags = data_sources['tags'].get(loc_id_str, []) #

        # Travel: direct assignment from location_travel.json, with default travel_time
        self.travel = data_sources['travel'].get(loc_id_str, {}) #
        self.travel_time = self.travel.get('time_to_travel', 60) # Assume 'time_to_travel' in minutes in travel.json

        # Context tags: Combine uncategorized_tags from various sources
        misc_context_tags = data_sources['misc'].get(loc_id_str, {}).get('uncategorized_tags', []) #
        env_context_tags = data_sources['environmental'].get(loc_id_str, {}).get('uncategorized_tags', []) #
        lore_context_tags = data_sources['lore_unique'].get(loc_id_str, {}).get('uncategorized_tags', []) #
        self.context_tags = list(set(misc_context_tags + env_context_tags + lore_context_tags)) # Combine and remove duplicates

        # Custom exit labels from descriptions.json (or deep_descriptions.json if they were there)
        self.exit_label_from_parent = merged_data.get('exit_label_from_parent', f"Exit to parent of {self.name}") #
        self.exit_label_to_parent = merged_data.get('exit_label_to_parent', f"Enter {self.name}") #

    def enter(self, player):
        """Called when a player enters this location."""
        # This can be expanded to trigger events, NPC greetings, etc.
        pass

    def __str__(self) -> str:
        return self.name

class LocationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LocationManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.locations: Dict[int, Location] = {}
        self._load_all_locations()

    def _load_json_data(self, filename: str) -> dict:
        # Assumes JSON files are in 'game_data/locations/' relative to the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(script_dir, 'game_data', 'locations')
        full_path = os.path.join(data_dir, filename)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: {full_path} not found.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Could not decode {full_path}. Error: {e}")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred while loading {full_path}: {e}")
            return {}

    def _load_all_locations(self):
        # REMOVED: all_location_lists_from_python and recurse_extract_python_data.
        # Python data is now entirely superseded by JSON.
        python_loc_data_flat = {} # This will remain empty as Python lists are no longer the source of base data.
        
        # Load all JSON data sources
        data_sources = {
            'python_data': python_loc_data_flat, # Now effectively an empty placeholder
            'descriptions': self._load_json_data('location_descriptions.json'), #
            'deep_descriptions': self._load_json_data('location_descriptions_deep.json'), #
            'environmental': self._load_json_data('location_environmental_attributes.json'), #
            'lore_unique': self._load_json_data('location_lore_and_unique_attributes.json'), #
            'misc': self._load_json_data('location_misc_attributes.json'), #
            'names': self._load_json_data('location_names.json'), #
            'population': self._load_json_data('location_population.json'), #
            'tags': self._load_json_data('location_tags.json'), #
            'travel': self._load_json_data('location_travel.json') #
        }
        
        # The map_hierarchy.json dictates the *primary structure* and IDs for creating Location objects
        map_hierarchy_data = self._load_json_data('map_hierarchy.json') #

        # Process the main hierarchy from map_hierarchy.json
        def process_recursive(loc_data_list, parent_id=None):
            for loc_data in loc_data_list:
                loc_id = loc_data['id']
                # Create a bare Location object with just ID/Name/Parent from hierarchy
                loc_obj = Location({'id': loc_id, 'name': loc_data.get('name')}, parent_id) #
                loc_obj.sub_location_ids = [sub.get('id') for sub in loc_data.get('sub_locations', []) if sub.get('id') is not None] #

                loc_obj.populate_attributes_from_data(data_sources) # Populate with all JSON data
                self.locations[loc_id] = loc_obj #
                if 'sub_locations' in loc_data:
                    process_recursive(loc_data['sub_locations'], loc_id) #
        
        process_recursive(map_hierarchy_data) # Start building from map_hierarchy
        self._connect_exits() #

    def _connect_exits(self):
        # This method is now more robust in how it finds connected locations by name.
        # It relies on all locations being loaded into self.locations first.
        for loc_id, loc_obj in self.locations.items(): #
            # Connect to parent
            if loc_obj.parent_id and loc_obj.parent_id in self.locations:
                parent_obj = self.locations[loc_obj.parent_id] #
                # Child adds an exit UP to its parent
                loc_obj.exits[loc_obj.exit_label_to_parent] = parent_obj #
                # Parent adds an exit DOWN to its child
                parent_obj.exits[loc_obj.exit_label_from_parent] = loc_obj #

            # Connect to explicitly adjacent locations from travel.json
            if loc_obj.travel and 'links' in loc_obj.travel: #
                for link in loc_obj.travel['links']: #
                    linked_name = link['name'] #
                    # Attempt to find the linked location by name in the loaded locations
                    linked_loc_obj = self.get_location_by_name(linked_name) #
                    if linked_loc_obj and linked_loc_obj.id != loc_obj.id: # Avoid linking to self
                        # Use a more generic label for adjacent paths if specific one not defined in `travel.json` link itself
                        exit_label = f"{link.get('connection_type', 'Path')} to {linked_loc_obj.name}" #
                        
                        # Ensure the reverse link is also created if it's a two-way path
                        if exit_label not in loc_obj.exits:
                            loc_obj.exits[exit_label] = linked_loc_obj #
                        
                        # Assuming adjacency is reciprocal, create the reverse link too
                        reverse_label = f"{link.get('connection_type', 'Path')} to {loc_obj.name}" #
                        if reverse_label not in linked_loc_obj.exits:
                            linked_loc_obj.exits[reverse_label] = loc_obj #

    def get_location(self, loc_id: int) -> Optional[Location]:
        return self.locations.get(loc_id) #

    def get_location_by_name(self, name: str) -> Optional[Location]:
        for loc in self.locations.values(): #
            if loc.name.lower() == name.lower():
                return loc #
        return None