# quests.py - Main interface for quest system
from typing import List, Dict, Any, Optional

# Import core logic, classes, and utility functions
from quest_entities import Quest, QuestLog
from quest_utils import (
    generate_reward,
    find_locations_by_tag,
    get_npc_name_by_role_hint,
    list_player_quests_for_display,
    DummyRumor
)
from quest_config import QUEST_REWARDS_TEMPLATE
from quests_logic import process_quest_rewards # generate_location_appropriate_quest is imported separately later

# Import quest template lists from data files
from quests_data_general import GENERAL_QUEST_TEMPLATES
from quests_data_whiterun import WHITERUN_QUEST_TEMPLATES
from quests_data_the_pale import THE_PALE_QUEST_TEMPLATES
from quests_data_winterhold import WINTERHOLD_QUEST_TEMPLATES
from quests_data_hjaalmarch import HJAALMARCH_QUEST_TEMPLATES
from quests_data_falkreath import FALKREATH_QUEST_TEMPLATES
from quests_data_the_reach import THE_REACH_QUEST_TEMPLATES
from quests_data_eastmarch import EASTMARCH_QUEST_TEMPLATES
from quests_data_the_rift import THE_RIFT_QUEST_TEMPLATES
from quests_data_haafingar import HAAFINGAR_QUEST_TEMPLATES

# Combine all quest templates into a single list
ALL_QUEST_TEMPLATES: List[Dict[str, Any]] = (
    GENERAL_QUEST_TEMPLATES +
    WHITERUN_QUEST_TEMPLATES +
    THE_PALE_QUEST_TEMPLATES +
    WINTERHOLD_QUEST_TEMPLATES +
    HJAALMARCH_QUEST_TEMPLATES +
    FALKREATH_QUEST_TEMPLATES +
    THE_REACH_QUEST_TEMPLATES +
    EASTMARCH_QUEST_TEMPLATES +
    THE_RIFT_QUEST_TEMPLATES +
    HAAFINGAR_QUEST_TEMPLATES
)

# Import the main quest generation function from quests_logic
# It needs ALL_QUEST_TEMPLATES, so we define it after combining them.
from quests_logic import generate_location_appropriate_quest as _generate_location_appropriate_quest_logic

# Wrapper for generate_location_appropriate_quest to pass ALL_QUEST_TEMPLATES automatically
def generate_location_appropriate_quest(
    player_level: int,
    current_location_obj: Dict[str, Any],
    quest_giver_id: str | None = None
) -> Quest | None:
    """
    Generates a quest based on player level and current location tags,
    using the combined list of all defined quest templates.
    """
    return _generate_location_appropriate_quest_logic(
        player_level,
        current_location_obj,
        ALL_QUEST_TEMPLATES, # Pass the combined list
        quest_giver_id
    )

# Re-export key components to maintain the public API of this module
__all__ = [
    "Quest",
    "QuestLog",
    "generate_reward",
    "find_locations_by_tag",
    "get_npc_name_by_role_hint",
    "generate_location_appropriate_quest",
    "process_quest_rewards",
    "list_player_quests_for_display",
    "ALL_QUEST_TEMPLATES",
    "QUEST_REWARDS_TEMPLATE",
    "DummyRumor",
    # Individual quest template lists, now part of the public API
    "GENERAL_QUEST_TEMPLATES",
    "WHITERUN_QUEST_TEMPLATES",
    "THE_PALE_QUEST_TEMPLATES",
    "WINTERHOLD_QUEST_TEMPLATES",
    "HJAALMARCH_QUEST_TEMPLATES",
    "FALKREATH_QUEST_TEMPLATES",
    "THE_REACH_QUEST_TEMPLATES",
    "EASTMARCH_QUEST_TEMPLATES",
    "THE_RIFT_QUEST_TEMPLATES",
    "HAAFINGAR_QUEST_TEMPLATES"
]

# Example of how you might initialize a QuestLog if it's commonly done from here
# def create_new_quest_log() -> QuestLog:
# return QuestLog()