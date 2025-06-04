from locations_whiterun import WHITERUN_LOCATIONS
from locations_the_pale import THE_PALE_LOCATIONS
from locations_winterhold import WINTERHOLD_LOCATIONS
from locations_hjaalmarch import HJAALMARCH_LOCATIONS
from locations_falkreath import FALKREATH_LOCATIONS
from locations_the_reach import THE_REACH_LOCATIONS
from locations_eastmarch import EASTMARCH_LOCATIONS
from locations_haafingar import HAAFINGAR_LOCATIONS
from locations_the_rift import THE_RIFT_LOCATIONS
from locations_misc import MISC_LOCATIONS
# Global storage for all location instances and raw data
ALL_LOCATIONS_INSTANCES = {}  # Maps ID to Location object
RAW_LOCATION_DATA_MAP = {}    # Maps ID to raw location dict
HOLD_NAME_TO_MAIN_ID_MAP = {} # Maps Hold Name string to its main Location ID

LOCATIONS = (
    WHITERUN_LOCATIONS +
    THE_PALE_LOCATIONS +
    WINTERHOLD_LOCATIONS +
    HJAALMARCH_LOCATIONS +
    FALKREATH_LOCATIONS +
    THE_REACH_LOCATIONS +
    EASTMARCH_LOCATIONS +
    HAAFINGAR_LOCATIONS +
    THE_RIFT_LOCATIONS +
    MISC_LOCATIONS
)

class Location:
    def __init__(self, id, name, description, parent_id=None, is_dark=False): # Added id, parent_id
        self.id = id
        self.name = name
        self.description = description
        self.parent_id = parent_id  # Store the ID of the parent location
        self.is_dark = is_dark  # Added from original
        self.dynamic = False  # Flag for dynamic locations
        self.secrets = []
        self.quests = []
        self.resources = {}
        self.items = []
        self.npcs = []
        self.exits = {}  # e.g., {"north": location_object, "enter shop": location_object}
        self.travel_time = 1  # Base travel time, can be modified based on distance/terrain

    def enter(self, player):
        print(f"You enter {self.name}.")
        print(self.description)
        self.display_items()
        self.display_npcs()
        self.display_exits() # Display available exits

        if self.is_dark:
            # player.has_lit_torch() now updates visibility internally.
            # We just check the result for the message.
            if player.has_lit_torch(): # This call updates player.visibility
                print("The torch illuminates the area, allowing you to see clearly.")
                # player.visibility is already set by has_lit_torch()
            else:
                print("It's too dark to see anything! You stumble around blindly.")
                # player.visibility is already set by has_lit_torch()
        else:
            # If the location is not dark, ensure player visibility is normal.
            # This might be redundant if has_lit_torch() is always called or default visibility is 10.
            # However, explicitly setting it here ensures correctness if the location itself isn't dark.
            player.visibility = 10 # Default visibility for non-dark areas

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_items(self):
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item}")

    def add_npc(self, npc):
        self.npcs.append(npc)

    def remove_npc(self, npc):
        if npc in self.npcs:
            self.npcs.remove(npc)

    def display_npcs(self):
        if self.npcs:
            print("You see the following people:")
            for npc in self.npcs:
                print(f"- {npc.name}")

    def add_exit(self, direction, location_obj): # Renamed location to location_obj for clarity
        self.exits[direction] = location_obj

    def get_exit(self, direction):
        return self.exits.get(direction)

    def display_exits(self):
        if self.exits:
            print("\nAvailable exits:")
            for direction in self.exits.keys():
                print(f"- {direction}")
        else:
            print("\nThere are no obvious exits from here.")

    def discover_secret(self, secret):
        self.secrets.append(secret)
        print(f"You discovered a secret at {self.name}: {secret}")

    def complete_quest(self, quest):
        self.quests.append(quest)
        print(f"You completed a quest at {self.name}: {quest}")

    def claim_resources(self, resource, amount):
        if resource in self.resources:
            self.resources[resource] += amount
        else:
            self.resources[resource] = amount
        print(f"You claimed {amount} {resource} at {self.name}.")

def update_location(self, new_description=None, new_exits=None, new_items=None, new_npcs=None):
        """
        Updates the location's properties dynamically.
        """
        if new_description:
            self.description = new_description
        if new_exits:
            self.exits = new_exits
        if new_items:
            self.items = new_items
        if new_npcs:
            self.npcs = new_npcs
        print(f"{self.name} has been updated.")
# --- New functions for map generation ---

def _create_location_objects_recursive(location_data_list, parent_obj=None):
    """
    Recursively creates Location objects from raw data and sets up parent-child exits.
    """
    for loc_data in location_data_list:
        loc_id = loc_data.get('id')
        loc_name = loc_data.get('name')
        loc_desc = loc_data.get('desc', 'A non-descript location.')
        loc_is_dark = loc_data.get('is_dark', False)

        if loc_id is None or loc_name is None:
            # print(f"Warning: Skipping location data due to missing 'id' or 'name': {loc_data}")
            continue

        if loc_id in ALL_LOCATIONS_INSTANCES:
            # This case means the location (e.g. a shared sub-location referenced multiple times)
            # might have already been created. We should use the existing object.
            # However, parentage might differ based on context if truly shared.
            # For now, assume IDs are unique and first creation is authoritative for basic props.
            # Parent/child links are specific to the recursive path.
            loc_obj = ALL_LOCATIONS_INSTANCES[loc_id]
            # Update parent_id if it's being processed under a new parent context.
            # This part is tricky if a location can have multiple parents.
            # For a strict tree, parent_id is set once.
            # If we are just linking, we add exits.
            # The current model implies a single parent_id for the object's primary hierarchy.
        else:
            loc_obj = Location(
                id=loc_id,
                name=loc_name,
                description=loc_desc,
                parent_id=parent_obj.id if parent_obj else None,
                is_dark=loc_is_dark
            )
            ALL_LOCATIONS_INSTANCES[loc_id] = loc_obj
        
        RAW_LOCATION_DATA_MAP[loc_id] = loc_data # Store/update raw data mapping

        if parent_obj:
            # Exit from parent to child, using custom label if available
            custom_label_from_parent = loc_data.get("exit_label_from_parent")
            if custom_label_from_parent:
                base_parent_to_child_exit_name = f"{custom_label_from_parent} to {loc_obj.name}"
            else:
                base_parent_to_child_exit_name = f"Enter {loc_obj.name}"
            parent_to_child_exit_name = ' '.join(word.capitalize() for word in base_parent_to_child_exit_name.split())
            parent_obj.add_exit(parent_to_child_exit_name, loc_obj)

            # Exit from child to parent, using custom label if available
            custom_label_to_parent = loc_data.get("exit_label_to_parent")
            if custom_label_to_parent:
                base_child_to_parent_exit_name = f"{custom_label_to_parent} to {parent_obj.name}"
            else:
                base_child_to_parent_exit_name = f"Exit to {parent_obj.name}"
            child_to_parent_exit_name = ' '.join(word.capitalize() for word in base_child_to_parent_exit_name.split())
            loc_obj.add_exit(child_to_parent_exit_name, parent_obj)

        if "sub_locations" in loc_data and loc_data["sub_locations"]:
            _create_location_objects_recursive(loc_data["sub_locations"], loc_obj)

def _connect_inter_hold_travel():
    """
    Connects top-level hold locations and specific path destinations based on 'travel' information.
    """
    for loc_id_key, raw_data_entry in RAW_LOCATION_DATA_MAP.items():
        if "travel" in raw_data_entry:
            current_loc_obj = ALL_LOCATIONS_INSTANCES.get(loc_id_key)
            if not current_loc_obj:
                continue

        travel_info = raw_data_entry.get("travel", {})
        
        # New structure: travel_info = {"links": [{"name": "Dest", "connection_type": "Road"}, ...]}
        if "links" in travel_info and isinstance(travel_info["links"], list):
            for link_spec in travel_info["links"]:
                if not isinstance(link_spec, dict): continue
                dest_name_str = link_spec.get("name")
                conn_type_str = link_spec.get("connection_type", "Path") # Default to "Path"

                if not dest_name_str: continue

                target_loc_obj = None
                target_hold_main_id = HOLD_NAME_TO_MAIN_ID_MAP.get(dest_name_str)
                if target_hold_main_id:
                    target_loc_obj = ALL_LOCATIONS_INSTANCES.get(target_hold_main_id)
                
                if not target_loc_obj:
                    for inst_id, inst_obj_search in ALL_LOCATIONS_INSTANCES.items():
                        if inst_obj_search.name == dest_name_str:
                            target_loc_obj = inst_obj_search
                            break
                
                if target_loc_obj and target_loc_obj != current_loc_obj:
                    base_exit_to_target = f"{conn_type_str} to {dest_name_str}"
                    exit_name_to_target = ' '.join(word.capitalize() for word in base_exit_to_target.split())
                    
                    # Assume symmetrical connection type for the return path for now
                    base_exit_from_target = f"{conn_type_str} to {current_loc_obj.name}"
                    exit_name_from_target = ' '.join(word.capitalize() for word in base_exit_from_target.split())

                    current_loc_obj.add_exit(exit_name_to_target, target_loc_obj)
                    target_loc_obj.add_exit(exit_name_from_target, current_loc_obj)
        else:
            # Fallback to old structure for "travel" if "links" is not present
            for connection_type_key, dest_names_list in travel_info.items(): # "roads", "paths"
                if not isinstance(dest_names_list, list): continue
                
                processed_conn_type_key = connection_type_key.rstrip('s') # "road", "path"

                for dest_name_str in dest_names_list:
                    target_loc_obj = None
                    target_hold_main_id = HOLD_NAME_TO_MAIN_ID_MAP.get(dest_name_str)
                    if target_hold_main_id:
                        target_loc_obj = ALL_LOCATIONS_INSTANCES.get(target_hold_main_id)
                    
                    if not target_loc_obj:
                        for inst_id, inst_obj_search in ALL_LOCATIONS_INSTANCES.items():
                            if inst_obj_search.name == dest_name_str:
                                target_loc_obj = inst_obj_search
                                break
                    
                    if target_loc_obj and target_loc_obj != current_loc_obj:
                        base_connection_to = f"{processed_conn_type_key} to {dest_name_str}"
                        exit_name_to_target = ' '.join(word.capitalize() for word in base_connection_to.split())
                        
                        base_connection_from = f"{processed_conn_type_key} to {current_loc_obj.name}"
                        exit_name_from_target = ' '.join(word.capitalize() for word in base_connection_from.split())

                        current_loc_obj.add_exit(exit_name_to_target, target_loc_obj)
                        target_loc_obj.add_exit(exit_name_from_target, current_loc_obj)
                    # else:
                        # print(f"Warning: Could not establish travel connection from '{current_loc_obj.name}' to '{dest_name_str}'. Target not found or is self.")

def initialize_skyrim_map():
    """
    Initializes all locations, creates objects, and sets up the exit network.
    Returns the dictionary of all location instances.
    """
    ALL_LOCATIONS_INSTANCES.clear()
    RAW_LOCATION_DATA_MAP.clear()
    HOLD_NAME_TO_MAIN_ID_MAP.clear()

    # LOCATIONS is defined at the top of the file, concatenating all hold location lists.
    # It should be a list of dictionaries, where each dictionary is a top-level hold's data.
    
    # Populate HOLD_NAME_TO_MAIN_ID_MAP for top-level holds
    # LOCATIONS is already the flat list like [ {hold1_data}, {hold2_data}, ... ]
    for hold_data in LOCATIONS: # Iterate directly over the combined list
        if isinstance(hold_data, dict) and 'name' in hold_data and 'id' in hold_data:
            HOLD_NAME_TO_MAIN_ID_MAP[hold_data['name']] = hold_data['id']
        # else:
            # print(f"Warning: Invalid data structure in LOCATIONS for hold mapping: {hold_data}")

    # Create all location objects and basic parent-child connections
    _create_location_objects_recursive(LOCATIONS)

    # Connect inter-hold travel routes and specific path destinations
    _connect_inter_hold_travel()
    
    # print(f"Skyrim map initialized. {len(ALL_LOCATIONS_INSTANCES)} locations processed.")
    # # Optional: Detailed print for debugging
    # for loc_id_debug, loc_obj_debug in ALL_LOCATIONS_INSTANCES.items():
    #     print(f"Location: {loc_obj_debug.name} (ID: {loc_id_debug}, ParentID: {loc_obj_debug.parent_id})")
    #     if loc_obj_debug.exits:
    #         print("  Exits:")
    #         for direction_debug, dest_loc_debug in loc_obj_debug.exits.items():
    #             print(f"    - {direction_debug} -> {dest_loc_debug.name} (ID: {dest_loc_debug.id})")
    #     else:
    #         print("  No exits defined.")
    #     print("-" * 10)

    return ALL_LOCATIONS_INSTANCES

# Example of how the game might use this:
# game_locations = initialize_skyrim_map()
# player_current_location = game_locations.get(10) # Assuming 10 is Whiterun City ID
# if player_current_location:
#    player_current_location.enter(player_object) # player_object would be an instance of Player class