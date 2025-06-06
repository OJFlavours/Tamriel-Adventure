import json
import os
from typing import Dict, Optional, List

class Location:
    def __init__(self, id: int, name: str, description: str, travel_desc: str, tags: List[str], demographics: Dict[str, int], density: str, is_dark: bool, travel: dict, sub_locations: List[int], parent_id: Optional[int] = None, adjacent_locations: Optional[List[int]] = None):
        self.id = id
        self.name = name
        self.description = description
        self.travel_desc = travel_desc
        self.tags = tags
        self.demographics = demographics
        self.density = density
        self.is_dark = is_dark
        self.travel = travel
        self.sub_locations = sub_locations
        self.parent_id = parent_id
        self.adjacent_locations = adjacent_locations if adjacent_locations is not None else []
        self.exits: Dict[str, Location] = {}

    def add_exit(self, direction: str, location: 'Location'):
        self.exits[direction] = location

    def __str__(self):
        return self.name

class LocationManager:
    def __init__(self, data_dir: str = 'game_data/locations/'):
        self.data_dir = data_dir
        self.locations: Dict[int, Location] = {}
        self.load_locations()
        self.connect_locations()

    def load_locations(self):
        """Loads location data from JSON files in the specified directory."""
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.data_dir, filename)
                self.load_location_data(filename, filepath)

    def load_location_data(self, filename: str, filepath: str):
        """Loads location data from a single JSON file."""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    for loc_id_str, location_data in data.items():
                        try:
                            loc_id = int(loc_id_str)
                            if filename == "location_tags.json":
                                self.load_location_tags(loc_id, location_data, filepath)
                            elif filename == "map_hierarchy.json":
                                self.load_location_hierarchy(loc_id, location_data, filepath)
                            elif filename == "location_travel.json":
                                self.load_location_travel(loc_id, location_data, filepath)
                            elif filename == "location_names.json":
                                self.load_location_names(loc_id, location_data, filepath)
                            else:
                                self.load_location(loc_id, location_data, filepath)
                        except ValueError:
                            print(f"Warning: Invalid location ID: {loc_id_str} in {filepath}")
                elif isinstance(data, list):
                    if filename == "map_hierarchy.json":
                        for location_data in data:
                            if isinstance(location_data, dict):
                                loc_id_str = str(location_data.get('id'))
                                try:
                                    loc_id = int(loc_id_str)
                                    self.load_location_hierarchy(loc_id, location_data, filepath)
                                except ValueError:
                                    print(f"Warning: Invalid location ID: {loc_id_str} in {filepath}")
                            else:
                                print(f"Warning: Unexpected data format in {filepath}. Expected dict, got {type(location_data)}.")
                    else:
                        print(f"Warning: Unexpected data format in {filepath}. Expected dict, got list.")
                else:
                    print(f"Warning: Unexpected data format in {filepath}. Expected dict or list.")
        except FileNotFoundError:
            print(f"Error: File not found: {filepath}")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {filepath}")
        except Exception as e:
            print(f"Error loading {filepath}: {e}")

    def load_location(self, loc_id: int, location_data: any, filepath: str):
        """Loads a single location from a dictionary."""
        try:
            name = None
            description = None
            travel_desc = None
            tags = None
            demographics = None
            density = None
            is_dark = None
            travel = None
            sub_locations = None
            parent_id = None
            adjacent_locations = None

            if isinstance(location_data, dict):
                name = location_data.get('name')
                description = location_data.get('desc', "A mysterious place.")
                travel_desc = location_data.get('travel_desc', "A mysterious place.")
                tags = location_data.get('tags', [])
                demographics = location_data.get('demographics', {})
                density = location_data.get('density', 'sparse')
                is_dark = location_data.get('is_dark', False)
                travel = location_data.get('travel', {})
                sub_locations = location_data.get('sub_locations', [])
                parent_id = location_data.get('parent_id')
                adjacent_locations = location_data.get('adjacent_locations')
            else:
                print(f"Warning: Unexpected data format for location ID: {loc_id} in {filepath}. Expected dict, got {type(location_data)}.")
                # If the location data is not a dict, it's likely a string or a list
                # We can't load a location from this, so we just skip it
                return

            location = Location(loc_id, name, description, travel_desc, tags, demographics, density, is_dark, travel, sub_locations, parent_id, adjacent_locations)
            self.locations[loc_id] = location
        except ValueError as ve:
            print(f"Error loading location: {ve}")
        except Exception as e:
            print(f"Error loading location data: {e} - Data: {location_data}")

    def load_location_tags(self, loc_id: int, location_data: any, filepath: str):
        """Loads location tags from a dictionary."""
        try:
            if loc_id not in self.locations:
                print(f"Warning: Location ID {loc_id} not found while loading tags from {filepath}")
                return

            location = self.locations[loc_id]

            if isinstance(location_data, list):
                location.tags.extend(location_data)
            else:
                print(f"Warning: Unexpected data format for location ID: {loc_id} in {filepath}. Expected list, got {type(location_data)}.")

        except Exception as e:
            print(f"Error loading location tags: {e} - Data: {location_data}")

    def load_location_hierarchy(self, loc_id: int, location_data: any, filepath: str):
        """Loads location hierarchy data from a dictionary."""
        try:
            if loc_id not in self.locations:
                print(f"Warning: Location ID {loc_id} not found while loading hierarchy from {filepath}")
                return

            location = self.locations[loc_id]

            if isinstance(location_data, dict):
                parent_id = location_data.get('parent_id')
                location.parent_id = parent_id
            else:
                print(f"Warning: Unexpected data format for location ID: {loc_id} in {filepath}. Expected dict, got {type(location_data)}.")

        except Exception as e:
            print(f"Error loading location hierarchy: {e} - Data: {location_data}")

    def load_location_travel(self, loc_id: int, location_data: any, filepath: str):
        """Loads location travel data from a dictionary."""
        try:
            if loc_id not in self.locations:
                print(f"Warning: Location ID {loc_id} not found while loading travel data from {filepath}")
            return

            location = self.locations[loc_id]

            if isinstance(location_data, dict):
                adjacent_locations = location_data.get('adjacent_locations')
                if adjacent_locations is not None:
                    location.adjacent_locations = adjacent_locations
                else:
                    location.adjacent_locations = []
            else:
                print(f"Warning: Unexpected data format for location ID: {loc_id} in {filepath}. Expected dict, got {type(location_data)}.")

        except Exception as e:
            print(f"Error loading location travel data: {e} - Data: {location_data}")

    def load_location_names(self, loc_id: int, location_data: any, filepath: str):
        """Loads location names from a dictionary."""
        try:
            if loc_id not in self.locations:
                print(f"Warning: Location ID {loc_id} not found while loading names from {filepath}")
                return

            location = self.locations[loc_id]

            if isinstance(location_data, str):
                location.name = location_data
            else:
                print(f"Warning: Unexpected data format for location ID: {loc_id} in {filepath}. Expected str, got {type(location_data)}.")

        except Exception as e:
            print(f"Error loading location names: {e} - Data: {location_data}")

    def connect_locations(self):
        """Connects locations based on the 'travel' data."""
        for location in self.locations.values():
            if location.adjacent_locations:
                for adjacent_location_id in location.adjacent_locations:
                    target_location = self.get_location(adjacent_location_id)
                    if target_location:
                        location.add_exit("to", target_location)
                    else:
                        print(f"Warning: Could not connect {location.name} to {adjacent_location_id}. Location not found.")
            else:
                print(f"Warning: Location {location.name} has no adjacent locations.")

    def get_location(self, location_id: int) -> Optional[Location]:
        """Returns a location object by its ID."""
        return self.locations.get(location_id)

    def get_location_by_name(self, location_name: str) -> Optional[Location]:
        """Returns a location object by its name."""
        for location in self.locations.values():
            if location.name == location_name:
                return location
        return None

location_manager = LocationManager()
# Example usage (for testing):
if __name__ == '__main__':
    location_manager = LocationManager()

    # Get a location by ID
    whiterun = location_manager.get_location(1)
    if whiterun:
        print(f"Location ID 1: {whiterun.name}, {whiterun.description}")

        # Check its exits
        if whiterun.exits:
            print(f"Exits from Whiterun:")
            for direction, exit_location in whiterun.exits.items():
                print(f"- {direction}: {exit_location.name}")
        else:
            print("No exits found for Whiterun.")
    else:
        print("Location ID 1 not found.")

    # Get a location by name
    riften = location_manager.get_location_by_name("Riften")
    if riften:
        print(f"Location Riften: {riften.name}, {riften.description}")
    else:
        print("Location Riften not found.")

    # Example of iterating through all locations
    print("\nAll Locations:")
    for loc_id, loc_obj in location_manager.locations.items():
        print(f"  - {loc_obj.name} (ID: {loc_id})")

# To maintain compatibility with scripts that might import from the top-level
#LOCATIONS = location_manager.locations # Removed this line