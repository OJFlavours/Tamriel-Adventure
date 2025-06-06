# dialogue_data.py

"""
Stores dialogue trees for NPCs, now structured with a priority system in mind.
The system will look for trees in this order:
1. Unique NPC ID (e.g., "LUCAN_VALERIUS_DIALOGUE")
2. Specific Role (e.g., "INNKEEPER_DIALOGUE")
3. Generic Disposition (e.g., "GENERIC_NEUTRAL")
"""

DIALOGUE_TREES = {
    # --- UNIQUE NPC DIALOGUE (Highest Priority) ---
    "LUCAN_VALERIUS_DIALOGUE": {
        "start_node": "start",
        "nodes": {
            "start": {
                "npc_line": "Welcome to the Riverwood Trader. We've got a little bit of everything. Or... we used to.",
                "player_responses": [
                    {"text": "What's wrong?", "next_node_id": "explain_theft"},
                    {"text": "Let me see what you have.", "action": "open_trade_window", "ends_dialogue": True},
                    {"text": "I'm just looking.", "ends_dialogue": True}
                ]
            },
            "explain_theft": {
                "npc_line": "A thief, that's what's wrong! Broke in and stole my prized possession - an antique golden claw! The guards won't do anything. Say, you look capable. If you could get it back, the reward would be substantial.",
                "player_responses": [
                    {"text": "I'll get your claw back.", "action": "start_quest:golden_claw", "next_node_id": "quest_accepted"},
                    {"text": "That's a shame. Good luck.", "ends_dialogue": True}
                ]
            },
            "quest_accepted": {
                "npc_line": "You will? Thank the Divines! The thief mumbled something about Bleak Falls Barrow as he fled. Be careful, it's not a safe place.",
                "ends_dialogue": True
            }
        }
    },

    # --- ROLE-SPECIFIC DIALOGUE (Second Priority) ---
    "INNKEEPER_DIALOGUE": {
        "start_node": "start",
        "nodes": {
            "start": {
                "npc_line": "Welcome, traveler. Looking for a room, a drink, or just some rumors?",
                "player_responses": [
                    {"text": "I'd like to rent a room. (10 Gold)", "action": "rent_room", "next_node_id": "room_rented"},
                    {"text": "What rumors have you heard?", "action": "share_rumor:local", "next_node_id": "start"},
                    {"text": "Just a drink for now.", "action": "open_trade_window:drink", "ends_dialogue": True}
                ]
            },
            "room_rented": {
                "npc_line": "It's yours for the day. A warm bed is a true luxury in Skyrim. Let me know if you need anything else.",
                "ends_dialogue": True
            }
        }
    },
    
    "BLACKSMITH_DIALOGUE": {
        "start_node": "start",
        "nodes": {
            "start": {
                "npc_line": "Got some good steel here. Need a new blade? Or maybe some armor patched up?",
                "player_responses": [
                    {"text": "Let me see your wares.", "action": "open_trade_window", "ends_dialogue": True},
                    {"text": "Can you tell me about smithing?", "next_node_id": "smithing_talk"}
                ]
            },
            "smithing_talk": {
                "npc_line": "It's hard work, but honest work. Takes a hot fire and a strong arm. Nothing beats the ring of hammer on steel.",
                "ends_dialogue": True
            }
        }
    },

    # --- GENERIC DIALOGUE (Fallback) ---
    "GENERIC_NEUTRAL": {
        "start_node": "start",
        "nodes": {
            "start": {
                "npc_line": ["Hmm?", "Need something?", "Yes, citizen?"],
                "player_responses": [
                    {"text": "Just passing by.", "ends_dialogue": True},
                    {"text": "Any news in the hold?", "action": "share_rumor:generic", "next_node_id": "start"}
                ]
            }
        }
    },
}

# (Helper functions like get_npc_line and format_dialogue_text remain the same)