# npc.py
# This file now serves as a high-level module for NPC-related functionalities,
# importing specific components from more specialized files.

# Core NPC class definition
from npc_entities import NPC

# NPC dialogue handling logic
from npc_dialogue_logic import handle_npc_dialogue

# Other NPC-related utilities or data that might have been in the original npc.py
# and are not part of the NPC class itself or specific dialogue logic could remain here
# or be moved to other appropriate files (e.g., npc_utils.py, npc_data.py).

# For example, if there were any standalone utility functions in the old npc.py
# that operated on NPCs or NPC data, they would be reviewed.
# Based on the provided npc.py, most content was the NPC class.

# assign_unique_npc_ids was imported in the original npc.py but not directly used by the class.
# It's part of npc_names.py, so it's correctly placed there.
# If npc.py needs to expose it for some reason, it could re-export it:
# from npc_names import assign_unique_npc_ids

# Similarly, role lists (NOBLE_ROLES, etc.) are in npc_roles.py.

# The goal is for npc.py to be lean, focusing on orchestrating or providing
# a clear access point to the refactored NPC system.

# Example of how the refactored components might be used by other game modules:
# from npc import NPC, handle_npc_dialogue
#
# some_npc = NPC(name="Lydia", race="Nord", role="Housecarl", level=10)
# # ... later, in an interaction ...
# # handle_npc_dialogue(some_npc, player_object, current_location_object)

# Any constants or global configurations related to NPCs that don't fit elsewhere
# could potentially reside here, but the preference is for specialized files.
# For now, npc.py will primarily be for these imports.

# It's important to ensure that all previous imports in the original npc.py
# are now correctly handled by either npc_entities.py, npc_dialogue_logic.py,
# or are no longer needed in this top-level npc.py if they were only supporting
# the internal implementation of the old NPC class.

# Imports that were in the original npc.py:
# import random -> Used by NPC class, now in npc_entities.py
# from typing import Any, List -> Used by NPC class and dialogue, now in respective files
# from stats import Stats, RACES -> Used by NPC class, now in npc_entities.py
# from items import Item -> Used by NPC class and dialogue, now in respective files
# from ui import UI -> Used by NPC class and dialogue, now in respective files
# from quests import Quest, generate_location_appropriate_quest, QuestLog, process_quest_rewards -> Used in dialogue, now in npc_dialogue_logic.py
# from locations import RAW_LOCATION_DATA_MAP -> Used in dialogue, now in npc_dialogue_logic.py
# from tags import TAGS, get_tags -> Used by NPC class, now in npc_entities.py
# import flavor -> Used in dialogue, now in npc_dialogue_logic.py
# from exploration_data import EXPLORATION_RESULTS -> Was imported but not directly used by NPC class or dialogue methods shown.
# from rumors import generate_rumor -> Used in dialogue, now in npc_dialogue_logic.py
# from spells import get_spell, Spell -> Used by NPC class, now in npc_entities.py
# from npc_roles import NOBLE_ROLES, COMMONER_ROLES, HOSTILE_ROLES, FRIENDLY_ROLES -> Used by NPC class, now in npc_entities.py
# from npc_names import NAME_POOLS, assign_unique_npc_ids -> NAME_POOLS used by NPC class (in npc_entities.py), assign_unique_npc_ids not directly by class.
# from npc_dialogue_generation import generate_greeting, generate_purpose -> Used by NPC class, now in npc_entities.py

# This simplified npc.py reflects the refactoring.