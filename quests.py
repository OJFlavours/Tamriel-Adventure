import random
from locations import LOCATIONS

# Constant defined for quest rewards, used elsewhere if needed.
QUEST_REWARDS = {
    "gold": 100,
    "experience": 50,
    "item": "Mysterious Relic"
}

# Utility function to generate a reward based on quest_tags.
def generate_reward(quest_tags):
    """
    Generate a numerical gold reward based on quest type.
    This function looks at specific keywords in quest_tags to scale rewards.
    """
    base_reward = 50
    if "dungeon" in quest_tags or "ruin" in quest_tags or "barrow" in quest_tags:
        return random.randint(base_reward + 50, base_reward + 100)
    elif "mine" in quest_tags or "bandit" in quest_tags:
        return random.randint(base_reward + 25, base_reward + 75)
    elif "shop" in quest_tags or "market" in quest_tags or "tavern" in quest_tags:
        return random.randint(base_reward, base_reward + 50)
    else:
        return random.randint(base_reward, base_reward + 75)

# Define a Quest class with integrated location and completion condition.
class Quest:
    def __init__(self, title, description, reward, level_requirement, location, completion_condition, quest_id=None):
        self.quest_id = quest_id or random.randint(1000, 9999)
        self.title = title
        self.description = description
        self.reward = reward
        self.level_requirement = level_requirement
        # location: a dict representing a location (or sub-location) from our LOCATIONS data.
        self.location = location  
        # completion_condition is either a function that evaluates the game state or a string flag.
        self.completion_condition = completion_condition

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
        parent = self.location.get("parent", "N/A")
        return (f"Quest[{self.quest_id}] {self.title} (Lvl {self.level_requirement}) at "
                f"{self.location.get('name', 'Unknown')} (Parent: {parent})")

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

# Utility function to add a quest to a player's quest log stored in player_state.
def add_quest_to_log(player_state, quest):
    """
    Adds a quest to the player's quest log within the player_state dictionary.
    If no quest log exists, this function initializes it.
    """
    if "quests" not in player_state:
        player_state["quests"] = []
    player_state["quests"].append(quest)
    return player_state["quests"]

# Sample completion condition functions.
def kill_boss_condition_factory(boss_name):
    def condition(game_state):
        # Expects game_state to have a list under 'defeated_bosses'.
        return boss_name in game_state.get("defeated_bosses", [])
    return condition

def retrieve_item_condition_factory(item_name):
    def condition(game_state):
        # Expects game_state's inventory to be a dict mapping item names to their counts.
        return game_state.get("inventory", {}).get(item_name, 0) > 0
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
def generate_location_appropriate_quest(player_level, quest_tags):
    """
    Generate a quest using location data. quest_tags is a list such as ["dungeon", "undead"] or ["mine", "bandit"].
    This function selects a location or sub-location whose tags match the quest_tags.
    """
    possible_locations = []
    for tag in quest_tags:
        possible_locations += find_locations_by_tag(tag)
    # Remove possible duplicate locations by using the location name as the key.
    possible_locations = {loc["name"]: loc for loc in possible_locations}.values()
    possible_locations = list(possible_locations)

    # If no location was found, fallback on all locations and their sub_locations.
    if not possible_locations:
        for loc in LOCATIONS:
            possible_locations.append(loc)
            for sub in loc.get("sub_locations", []):
                possible_locations.append(sub)
    chosen_location = random.choice(possible_locations)

    # Build the quest details based on quest_tags.
    if "dungeon" in quest_tags or "ruin" in quest_tags or "barrow" in quest_tags:
        title = "Explore the Forgotten Halls"
        description = (
            f"Venture into the depths of {chosen_location.get('name', 'the ancient ruins')}, "
            "clear out the draugr, and uncover lost treasures. Beware – darkness hides unseen perils."
        )
        reward = generate_reward(quest_tags)
        boss_name = f"The Warden of {chosen_location.get('name', 'the Ruins')}"
        completion_condition = kill_boss_condition_factory(boss_name)
    elif "mine" in quest_tags or "bandit" in quest_tags:
        title = "Secure the Resource"
        description = (
            f"Investigate {chosen_location.get('name', 'the mine')} and clear out bandits or hostile forces. "
            "Ensure the safety of local workers and recover valuable ore."
        )
        reward = generate_reward(quest_tags)
        item_name = f"Purified Ore from {chosen_location.get('name', 'the Mine')}"
        completion_condition = retrieve_item_condition_factory(item_name)
    elif "shop" in quest_tags or "market" in quest_tags or "tavern" in quest_tags:
        title = "Deliver a Vital Message"
        description = (
            f"Travel to {chosen_location.get('name', 'the bustling settlement')} and deliver a message critical to local affairs. "
            "Speak with the town elder to ensure the connection is made."
        )
        reward = generate_reward(quest_tags)
        npc_name = f"Elder of {chosen_location.get('name', 'the Settlement')}"
        completion_condition = talk_to_npc_condition_factory(npc_name)
    else:
        title = "A Mysterious Request"
        description = (
            f"A local resident has requested your assistance near {chosen_location.get('name', 'a distant locale')}. "
            "Investigate the area, resolve emerging troubles, and return for your reward."
        )
        reward = generate_reward(quest_tags)
        item_name = f"Mysterious Relic from {chosen_location.get('name', 'the Region')}"
        completion_condition = retrieve_item_condition_factory(item_name)

    return Quest(
        title=title,
        description=description,
        reward=reward,
        level_requirement=player_level,
        location=chosen_location,
        completion_condition=completion_condition
    )

# Utility function to list a player's current quests.
def list_player_quests(player_state):
    """
    Returns a list of quests assigned to the player.
    The player_state must contain a 'quests' key with active Quest objects.
    """
    return player_state.get("quests", [])

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
    print(f"  Reward: {quest.reward} gold")
    print(f"  Location: {quest.location.get('name')} (Parent: {quest.location.get('parent', 'N/A')})")
    print(f"  Level Requirement: {quest.level_requirement}")

    # Simulated game state for testing the completion condition.
    game_state = {
        "defeated_bosses": [f"The Warden of {quest.location.get('name')}"],
        "inventory": {},
        "talked_to": {}
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