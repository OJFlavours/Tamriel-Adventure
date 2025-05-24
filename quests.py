import random
from ui import UI

QUEST_DESCRIPTIONS = {
    "fetch": [
        "Retrieve a lost artifact from a dangerous ruin.",
        "Gather rare ingredients for a powerful potion.",
        "Recover a stolen heirloom from a bandit camp.",
        "Find a missing person in a haunted forest.",
        "Collect debts from unruly citizens.",
        "Steal a valuable item from a heavily guarded location."
    ],
    "escort": [
        "Escort a merchant caravan through a perilous mountain pass.",
        "Protect a pilgrim on their journey to a sacred shrine.",
        "Guide a refugee family to a safe haven.",
        "Accompany a scholar to an ancient library.",
        "Guard a prisoner being transported to a distant jail.",
        "Help a wounded soldier return to their unit."
    ],
    "investigate": [
        "Investigate a series of mysterious disappearances.",
        "Uncover a conspiracy within the city guard.",
        "Examine a haunted location for paranormal activity.",
        "Discover the source of a strange plague.",
        "Track down a band of smugglers operating in the area.",
        "Reveal the secrets of a hidden cult."
    ],
    "eliminate": [
        "Eliminate a dangerous beast terrorizing the countryside.",
        "Assassinate a corrupt official.",
        "Defeat a rival gang leader.",
        "Purge a vampire nest.",
        "Destroy a coven of witches.",
        "Vanquish a powerful necromancer."
    ],
    "explore": [
        "Explore a newly discovered cave system.",
        "Chart a previously unknown region of the map.",
        "Discover the secrets of an ancient ruin.",
        "Find a lost city.",
        "Search for a legendary treasure.",
        "Uncover a hidden portal to another dimension."
    ]
}

QUEST_REWARDS = {
    "gold": [
        "a hefty sum of gold",
        "a share of the treasure",
        "a generous bounty",
        "a valuable reward",
        "payment for services rendered",
        "a king's ransom"
    ],
    "item": [
        "a powerful weapon",
        "a suit of enchanted armor",
        "a rare potion",
        "an ancient scroll",
        "a magical artifact",
        "a unique trinket"
    ],
    "reputation": [
        "the gratitude of the people",
        "the respect of the guards",
        "the favor of the nobles",
        "recognition as a hero",
        "a place in the history books",
        "a title of nobility"
    ]
}

class Quest:
    def __init__(self, quest_type, description, reward, location_tags=None):
        self.quest_type = quest_type
        self.description = description
        self.reward = reward
        self.status = "active"
        self.location_tags = location_tags or []

    def __str__(self):
        return f"{self.quest_type.capitalize()}: {self.description} (Reward: {self.reward})"

class QuestLog:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def remove_quest(self, quest):
        self.quests.remove(quest)

    def list_quests(self):
        if not self.quests:
            UI.slow_print("You have no active quests.")
        else:
            UI.header("Quest Log")
            for quest in self.quests:
                UI.slow_print(f"- {quest}")
            UI.divider()

    def generate_quest(self, level=1, location_tags=[]):
        quest_type = random.choice(list(QUEST_DESCRIPTIONS.keys()))
        description = random.choice(QUEST_DESCRIPTIONS[quest_type])
        reward_type = random.choice(list(QUEST_REWARDS.keys()))
        reward = random.choice(QUEST_REWARDS[reward_type])
        return Quest(quest_type, description, reward, location_tags)

    def accept_quest(self, quest):
        self.add_quest(quest)
        UI.slow_print(f"Accepted quest: {quest}")

    def complete_quest(self, quest):
        if quest in self.quests:
            quest.status = "completed"
            self.remove_quest(quest)
            UI.slow_print(f"Completed quest: {quest}. You receive {quest.reward}!")
        else:
            UI.slow_print("That quest is not in your log.")

# Helper Functions for Quest Integration
def generate_location_appropriate_quest(level, location_tags):
    """Generates a quest appropriate for the location."""
    quest_log = QuestLog()
    return quest_log.generate_quest(level, location_tags)

def add_quest_to_log(player, quest):
    """Adds a quest to the player's quest log."""
    if hasattr(player, "quest_log"):
        player.quest_log.add_quest(quest)
    else:
        UI.slow_print("You have no way to track this quest.")

def list_player_quests(player):
     if hasattr(player, "quest_log"):
        player.quest_log.list_quests()
     else:
        UI.slow_print("You have no way to track this quest.")