import random
from locations import LOCATIONS
import tags
import flavor

# Constant defined for quest rewards, used elsewhere if needed.
# QUEST_REWARDS is now a template for possible reward types and their base values/ranges.
QUEST_REWARDS_TEMPLATE = {
    "gold": {"min": 50, "max": 150},
    "experience": {"min": 25, "max": 75},
    "item": ["Potion of Healing", "Iron Sword", "Leather Armor", "Small Soul Gem", "Gold Ring"], # Example items
    "reputation": {"min": 5, "max": 15}, # Reputation gain
    "favor": ["with local Jarl", "with merchant guild", "with College of Winterhold"] # Abstract favor
}

# Utility function to generate a reward based on quest_tags and player level.
def generate_reward(player_level, quest_tags):
    """
    Generate a diverse reward (gold, experience, item, etc.) based on quest type and player level.
    Returns a dictionary of rewards.
    """
    reward = {}
    reward_type_choices = list(QUEST_REWARDS_TEMPLATE.keys())
    
    # Always include gold, maybe experience, then a random additional reward type
    reward["gold"] = random.randint(QUEST_REWARDS_TEMPLATE["gold"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["gold"]["max"] * player_level)
    
    if random.random() < 0.7: # 70% chance for experience
        reward["experience"] = random.randint(QUEST_REWARDS_TEMPLATE["experience"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["experience"]["max"] * player_level)

    # Add a chance for an additional diverse reward
    additional_reward_types = [rt for rt in reward_type_choices if rt not in ["gold", "experience"]]
    if additional_reward_types and random.random() < 0.6: # 60% chance for another reward type
        chosen_type = random.choice(additional_reward_types)
        if chosen_type == "item":
            # For items, generate a random item appropriate for player level
            # Assuming generate_random_item can take a generic category and level
            from items import generate_random_item as gr_item_func # Use alias to avoid conflict
            reward["item"] = gr_item_func(random.choice(["weapon", "armor", "potion", "jewelry", "misc"]), player_level)
        elif chosen_type in ["reputation", "favor"]:
            value_source = QUEST_REWARDS_TEMPLATE[chosen_type]
            if isinstance(value_source, list):
                reward[chosen_type] = random.choice(value_source)
            else:
                reward[chosen_type] = random.randint(value_source["min"], value_source["max"])

    return reward

# Define a Quest class with integrated location and completion condition.
class Quest:
    def __init__(self, title, description, reward, level_requirement, location, completion_condition, quest_id=None):
        self.quest_id = quest_id or random.randint(1000, 9999)
        self.title = title
        self.description = description
        self.reward = reward # This is now a dictionary of rewards
        self.level_requirement = level_requirement
        # location: a dict representing a location (or sub-location) from our LOCATIONS data.
        self.location = location
        # completion_condition is either a function that evaluates the game state or a string flag.
        self.completion_condition = completion_condition
        self.tags = {}  # Initialize the tags dictionary

    def add_tag(self, tag_category, tag_type, tag):
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        self.tags[tag_category][tag_type] = tag
        # Removed redundant calls to tags.add_tag as Quest.tags is managed internally
        # tags.add_tag(self, tag_category, tag_type)
        # tags.add_tag(self, tag_category, tag)

    def is_complete(self, game_state):
        """
        Checks whether this quest's completion condition is met.
        Expects game_state to carry in-game events such as collected items, defeated bosses, or NPC interactions.
        """
        if callable(self.completion_condition):
            return self.completion_condition(game_state)
        else:
            return game_state.get(self.completion_condition, False)

    def __str__(self):
        # Adjusted __str__ to display the new reward dictionary
        reward_str_parts = []
        for key, value in self.reward.items():
            if isinstance(value, Item):
                reward_str_parts.append(f"{value.name} (Item)")
            else:
                reward_str_parts.append(f"{value} {key.capitalize()}")
        reward_display = ", ".join(reward_str_parts)

        flavor_texts = flavor.get_flavor(self) # Need to ensure flavor.get_flavor handles Quest objects properly
        description_prefix = f"Quest[{self.quest_id}] {self.title} (Lvl {self.level_requirement}) at {self.location.get('name', 'Unknown')}:"
        
        if flavor_texts:
            full_description = f"{description_prefix} {' '.join(flavor_texts)}. Reward: {reward_display}"
        else:
            full_description = f"{description_prefix} {self.description}. Reward: {reward_display}"
            
        return full_description

# Define a QuestLog class to hold and manage multiple quests.
class QuestLog:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def remove_quest(self, quest_id):
        self.quests = [q for q in self.quests if q.quest_id != quest_id]

    def list_quests(self):
        return self.quests

    def __str__(self):
        if not self.quests:
            return "Quest Log is empty."
        return "\n".join(str(q) for q in self.quests)

# Utility function to list a player's current quests.
def list_player_quests(player_state):
    """
    Returns a list of quests assigned to the player.
    The player_state must contain a 'quests' key with active Quest objects.
    """
    # This function should probably interact with player.quest_log.list_quests()
    # For now, it assumes player_state can directly have a 'quests' list.
    # If player_state is the player object itself, it would be player_state.quest_log.list_quests()
    return player_state.get("quests", [])

# Sample completion condition functions.
def kill_boss_condition_factory(boss_name):
    def condition(game_state):
        # Expects game_state to have a list under 'defeated_bosses'.
        return boss_name in game_state.get("defeated_bosses", [])
    return condition

def retrieve_item_condition_factory(item_name):
    def condition(game_state):
        # Expects game_state's inventory to be a dict mapping item names to their counts.
        # This will need to be updated to check player.inventory (list of Item objects)
        if "player_inventory" in game_state: # Assume game_state can pass player_inventory
            return any(item.name == item_name for item in game_state["player_inventory"])
        return False
    return condition

def talk_to_npc_condition_factory(npc_name):
    def condition(game_state):
        # Expects game_state to contain a dict 'talked_to' marking which NPCs have been interacted with.
        return game_state.get("talked_to", {}).get(npc_name, False)
    return condition

# Helper function to search the LOCATIONS structure by matching tags.
def find_locations_by_tag(tag):
    matching = []
    for loc in LOCATIONS:
        if tag in loc.get("tags", []):
            matching.append(loc)
        for sub in loc.get("sub_locations", []):
            if tag in sub.get("tags", []):
                sub_copy = sub.copy()
                sub_copy["parent"] = loc["name"]
                matching.append(sub_copy)
            for sub2 in sub.get("sub_locations", []):
                if tag in sub2.get("tags", []):
                    sub2_copy = sub2.copy()
                    sub2_copy["parent"] = f'{loc["name"]} -> {sub["name"]}'
                    matching.append(sub2_copy)
    return matching

# Generate a quest that is appropriate for a player's level and desired quest type (tags).
def generate_location_appropriate_quest(player_level, location_tags):
    """
    Generate a quest using location data. location_tags is a list such as ["dungeon", "undead"] or ["mine", "bandit"].
    This function selects a location or sub-location whose tags match the location_tags.
    """
    possible_locations = []
    # Use generic tags for quest generation if specific location tags are not available
    quest_tags = ["explore"] # Default quest type
    if "dungeon" in location_tags:
        quest_tags.append("dungeon")
    if "mine" in location_tags:
        quest_tags.append("mine")
    if "tavern" in location_tags or "inn" in location_tags or "market" in location_tags:
        quest_tags.append("social") # A new tag for social quests
        quest_tags.append("trade")
    if "undead" in location_tags:
        quest_tags.append("undead")
    if "bandit" in location_tags:
        quest_tags.append("hunt")

    for tag in location_tags: # Iterate through actual location tags for finding a suitable place
        possible_locations += find_locations_by_tag(tag)
    # Remove possible duplicate locations by using the location name as the key.
    possible_locations = {loc["name"]: loc for loc in possible_locations}.values()
    possible_locations = list(possible_locations)

    # If no location was found based on specific tags, fall back on all locations and their sub_locations.
    if not possible_locations:
        for loc in LOCATIONS:
            possible_locations.append(loc)
            for sub in loc.get("sub_locations", []):
                # Ensure sub-locations have a parent for proper display
                sub_copy = sub.copy()
                sub_copy["parent"] = loc["name"]
                possible_locations.append(sub_copy)
    
    if not possible_locations: # Fallback if no locations are found at all (shouldn't happen with LOCATIONS list)
        chosen_location = {"name": "Unknown Location", "desc": "A mysterious place.", "tags": []}
    else:
        chosen_location = random.choice(possible_locations)

    # Determine quest type based on effective quest_tags
    chosen_quest_type = random.choice(tags.TAGS["QUESTS"]["type"]) # Use a random quest type from tags.py

    title = "A Simple Task"
    description = "Someone needs help."
    completion_condition = None
    
    # Logic to build quest details based on chosen_quest_type and location tags
    if chosen_quest_type == "fetch":
        item_to_fetch = "a rare artifact" # Placeholder, could generate specific item
        title = f"Retrieve {item_to_fetch}"
        description = f"A local asks you to retrieve {item_to_fetch} from {chosen_location.get('name', 'a nearby area')}."
        completion_condition = retrieve_item_condition_factory(item_to_fetch) # Need to ensure item generation matches this
    elif chosen_quest_type == "hunt":
        enemy_type = random.choice(["bandits", "wild beasts", "undead"])
        title = f"Clear out the {enemy_type.capitalize()}"
        description = f"Eliminate the {enemy_type} terrorizing {chosen_location.get('name', 'the area')}."
        completion_condition = f"defeated_{enemy_type}_in_{chosen_location.get('name')}" # Simple flag
    elif chosen_quest_type == "escort":
        npc_to_escort = "a wary traveler"
        title = f"Escort {npc_to_escort.capitalize()}"
        description = f"Escort {npc_to_escort} safely to a nearby settlement from {chosen_location.get('name', 'here')}."
        completion_condition = f"escorted_{npc_to_escort}_from_{chosen_location.get('name')}"
    elif chosen_quest_type == "investigate":
        mystery = random.choice(["strange disappearances", "unusual lights", "whispers of cult activity"])
        title = f"Investigate {mystery.capitalize()}"
        description = f"Investigate {mystery} around {chosen_location.get('name', 'this area')} and report back."
        completion_condition = f"investigated_{mystery.replace(' ', '_')}_at_{chosen_location.get('name')}"
    elif chosen_quest_type == "deliver":
        delivery_item = random.choice(["a package", "a message", "medical supplies"])
        recipient = "a contact"
        title = f"Deliver {delivery_item.capitalize()} to {recipient}"
        description = f"Deliver {delivery_item} from {chosen_location.get('name', 'here')} to {recipient}."
        completion_condition = f"delivered_{delivery_item.replace(' ', '_')}_to_{recipient.replace(' ', '_')}"
    # Default fallback if no specific type is matched well
    else:
        title = "A General Request"
        description = f"A local resident needs help in {chosen_location.get('name', 'the area')} with a minor issue."
        completion_condition = "general_assistance_rendered"

    reward = generate_reward(player_level, quest_tags) # Pass player_level

    quest = Quest(
        title=title,
        description=description,
        reward=reward, # Reward is now a dictionary
        level_requirement=player_level,
        location=chosen_location,
        completion_condition=completion_condition
    )

    for tag in quest_tags:
        quest.add_tag("quest", "type", tag) # Use 'type' as tag_type for quest tags

    return quest

# Example testing usage.
if __name__ == "__main__":
    # Example: Generate a quest for a level 10 player targeting a dungeon with undead enemies.
    player_level = 10
    quest_tags = ["dungeon", "undead"]
    quest = generate_location_appropriate_quest(player_level, quest_tags)
    print("Generated Quest:")
    print(quest)
    print("Quest Details:")
    print(f"  Title: {quest.title}")
    print(f"  Description: {quest.description}")
    print(f"  Reward: {quest.reward} gold") # This will now print the reward dictionary
    print(f"  Location: {quest.location.get('name')} (Parent: {quest.location.get('parent', 'N/A')})")
    print(f"  Level Requirement: {quest.level_requirement}")

    # Simulated game state for testing the completion condition.
    class MockPlayer:
        def __init__(self):
            self.inventory = [Item("a rare artifact", "misc", "steel")] # Mock item for testing
    
    mock_player = MockPlayer()
    game_state = {
        "defeated_bosses": [f"The Warden of {quest.location.get('name')}"],
        "player_inventory": mock_player.inventory, # Pass player inventory for item checks
        "talked_to": {f"Elder of {quest.location.get('name')}": True}
    }
    print(f"Quest Completion Status: {'Complete' if quest.is_complete(game_state) else 'Incomplete'}")

    # Example player state with quests.
    example_player_state = {
        "player_id": 1,
        "quests": [quest],
        "inventory": {},
        "defeated_bosses": [],
        "talked_to": {}
    }
    print("Player's Quest Log:")
    quest_log = QuestLog()
    for q in list_player_quests(example_player_state):
        quest_log.add_quest(q)
    print(quest_log)
