import json
import os
from typing import Dict, List, Optional

# Import location data from all python modules
from locations_whiterun import WHITERUN_LOCATIONS
from locations_the_pale import THE_PALE_LOCATIONS
from locations_winterhold import WINTERHOLD_LOCATIONS
from locations_eastmarch import EASTMARCH_LOCATIONS
from locations_the_rift import THE_RIFT_LOCATIONS
from locations_hjaalmarch import HJAALMARCH_LOCATIONS
from locations_falkreath import FALKREATH_LOCATIONS
from locations_haafingar import HAAFINGAR_LOCATIONS
from locations_misc import MISC_LOCATIONS

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
        self.tags: List[str] = []
        self.demographics: Dict[str, int] = {}
        self.density: str = "sparse"
        self.travel: dict = {}
        self.context_tags: List[str] = []
        self.exit_label_from_parent: str = f"Enter {self.name}"
        self.exit_label_to_parent: str = f"Exit to {self.name}'s parent"
        self.exits: Dict[str, 'Location'] = {}

    def populate_attributes_from_data(self, data_sources: dict):
        """Populates the location's attributes from various data sources."""
        loc_id_str = str(self.id)
        
        # Merge data from all sources, with python file data as base
        merged_data = data_sources['python_data'].get(self.id, {})
        merged_data.update(data_sources['descriptions'].get(loc_id_str, {}))
        merged_data.update(data_sources['population'].get(loc_id_str, {}))
        merged_data.update(data_sources['misc'].get(loc_id_str, {}))
        
        # Overwrite or set specific attributes
        self.name = data_sources['names'].get(loc_id_str, self.name)
        self.description = merged_data.get('desc', self.description)
        self.travel_desc = merged_data.get('travel_desc', self.travel_desc)
        self.tags = data_sources['tags'].get(loc_id_str, self.tags)
        self.demographics = merged_data.get('demographics', self.demographics)
        self.density = merged_data.get('density', self.density)
        self.travel = data_sources['travel'].get(loc_id_str, self.travel)
        self.context_tags = merged_data.get('context_tags', self.context_tags)
        self.exit_label_from_parent = merged_data.get('exit_label_from_parent', f"Enter {self.name}")
        self.exit_label_to_parent = merged_data.get('exit_label_to_parent', f"Exit to parent of {self.name}")

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

    def _load_json_data(self, filepath: str) -> dict:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        full_path = os.path.join(script_dir, filepath)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading {filepath}: {e}")
            return {}

    def _load_all_locations(self):
        all_location_lists = [
            WHITERUN_LOCATIONS, THE_PALE_LOCATIONS, WINTERHOLD_LOCATIONS,
            EASTMARCH_LOCATIONS, THE_RIFT_LOCATIONS, HJAALMARCH_LOCATIONS,
            FALKREATH_LOCATIONS, HAAFINGAR_LOCATIONS, MISC_LOCATIONS
        ]

        python_loc_data = {}
        def recurse_extract(loc_list):
            for loc in loc_list:
                python_loc_data[loc['id']] = loc
                if 'sub_locations' in loc:
                    recurse_extract(loc['sub_locations'])
        for data_list in all_location_lists:
            recurse_extract(data_list)
        
        data_sources = {
            'python_data': python_loc_data,
            'descriptions': self._load_json_data('location_descriptions.json'),
            'tags': self._load_json_data('location_tags.json'),
            'population': self._load_json_data('location_population.json'),
            'travel': self._load_json_data('location_travel.json'),
            'misc': self._load_json_data('location_misc_attributes.json'),
            'names': self._load_json_data('location_names.json')
        }
        
        map_hierarchy = self._load_json_data('map_hierarchy.json')

        def process_recursive(loc_data_list, parent_id=None):
            for loc_data in loc_data_list:
                loc_id = loc_data['id']
                loc_obj = Location(loc_data, parent_id)
                loc_obj.populate_attributes_from_data(data_sources)
                self.locations[loc_id] = loc_obj
                if 'sub_locations' in loc_data:
                    process_recursive(loc_data['sub_locations'], loc_id)
        
        process_recursive(map_hierarchy)
        self._connect_exits()

    def _connect_exits(self):
        for loc_id, loc_obj in self.locations.items():
            if loc_obj.parent_id and loc_obj.parent_id in self.locations:
                parent_obj = self.locations[loc_obj.parent_id]
                parent_exit_label = parent_obj.exit_label_to_parent if hasattr(parent_obj, 'exit_label_to_parent') else f"Exit to {parent_obj.name}"
                loc_obj.exits[loc_obj.exit_label_to_parent] = parent_obj
                parent_obj.exits[loc_obj.exit_label_from_parent] = loc_obj

            adjacent_ids = loc_obj.travel.get('adjacent_locations', [])
            for adj_id in adjacent_ids:
                if adj_id in self.locations:
                    adj_loc = self.locations[adj_id]
                    loc_obj.exits[f"Path to {adj_loc.name}"] = adj_loc
                    adj_loc.exits[f"Path to {loc_obj.name}"] = loc_obj

    def get_location(self, loc_id: int) -> Optional[Location]:
        return self.locations.get(loc_id)

    def get_location_by_name(self, name: str) -> Optional[Location]:
        for loc in self.locations.values():
            if loc.name.lower() == name.lower():
                return loc
        return None