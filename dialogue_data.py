"""
Stores dialogue trees for NPCs.

Each tree is a dictionary of nodes.
Each node has:
    - npc_line: String or list of strings (for random selection). Can include placeholders.
    - player_responses: List of dictionaries, each representing a player choice.
        - text: Player's dialogue. Can include placeholders.
        - next_node_id: ID of the next node if this response is chosen.
        - condition: Optional string or list of strings representing conditions to meet for this option to appear.
                     (e.g., "disposition >= 70", "has_item:gold_ring", "quest_active:main_quest_01_step_2", "skill_check:speech:15")
        - action: Optional string or list of strings representing actions to take.
                  (e.g., "start_quest:retrieve_amulet", "give_item:health_potion:1", "change_disposition:10", "set_flag:met_stenvar")
        - ends_dialogue: Boolean, if True, ends the conversation.
        - disposition_change: Integer, how much to change NPC disposition.
    - on_enter_action: Optional string or list of strings, actions to execute when this node is entered.
    - greeting_variant: Optional boolean. If true, this node can serve as a varied greeting.
"""

DIALOGUE_TREES = {
    "GENERIC_GUARD_NEUTRAL": {
        "start_node": "guard_neutral_greet",
        "nodes": {
            "guard_neutral_greet": {
                "npc_line": [
                    "Citizen. Keep your nose clean while you're in [LocationName].",
                    "State your business. Quickly.",
                    "Everything in order here. Move along."
                ],
                "player_responses": [
                    {"text": "Just passing through, officer.", "next_node_id": "guard_passing_through_reply"},
                    {"text": "Any news or trouble I should be aware of?", "next_node_id": "guard_rumors_work"},
                    {"text": "What's your duty here?", "next_node_id": "guard_explain_duty"},
                    {"text": "Farewell.", "ends_dialogue": True}
                ]
            },
            "guard_passing_through_reply": {
                "npc_line": "See that you do. We don't tolerate troublemakers.",
                "ends_dialogue": True
            },
            "guard_rumors_work": {
                "npc_line": "Mostly quiet. Though I did hear some talk about [GenericRumorTopic] down at the [LocalTavernName]. As for work, if you're looking to help, the Jarl's steward sometimes posts bounties for bandits or troublesome beasts.",
                "action": "share_rumor:generic", # This will call a generic rumor function
                "player_responses": [
                    {"text": "Thanks for the information.", "next_node_id": "guard_neutral_greet", "disposition_change": 2},
                    {"text": "I might look into those bounties.", "next_node_id": "guard_bounty_interest", "condition": "player_level >= 3"},
                    {"text": "Farewell.", "ends_dialogue": True}
                ]
            },
            "guard_bounty_interest": {
                "npc_line": "Good. More swords helping keep the peace is always welcome. Check the notice board near the keep.",
                "ends_dialogue": True
            },
            "guard_explain_duty": {
                "npc_line": "My duty? To protect the good people of [LocationName] and uphold the Jarl's law. It's a thankless job sometimes, but someone has to do it.",
                "player_responses": [
                    {"text": "Sounds important. Keep up the good work.", "disposition_change": 5, "ends_dialogue": True},
                    {"text": "Must be boring.", "next_node_id": "guard_duty_boring_reply", "disposition_change": -5},
                    {"text": "Farewell.", "ends_dialogue": True}
                ]
            },
            "guard_duty_boring_reply": {
                "npc_line": "Boring is better than a sword in your gut, citizen. Now, move along.",
                "ends_dialogue": True
            }
        }
    },
    "GENERIC_MERCHANT_FRIENDLY": {
        "start_node": "merchant_friendly_greet",
        "nodes": {
            "merchant_friendly_greet": {
                "npc_line": "Welcome, friend! Finest wares in [LocationName]! What can I get for you today?",
                "player_responses": [
                    {"text": "Let's see what you have. (Trade)", "action": "open_trade_window", "ends_dialogue": True}, # Special action
                    {"text": "I'm looking for something specific.", "next_node_id": "merchant_specific_item_query"},
                    {"text": "Any interesting news or rumors?", "next_node_id": "merchant_rumors_friendly"},
                    {"text": "Just looking around for now.", "ends_dialogue": True, "disposition_change": -1}
                ]
            },
            "merchant_specific_item_query": {
                "npc_line": "Oh? What might that be? I have a wide selection, and if I don't have it, I might know who does.",
                "player_responses": [
                    # These would ideally be more dynamic based on actual items, but for now:
                    {"text": "Looking for a sturdy weapon.", "next_node_id": "merchant_show_weapons_friendly"},
                    {"text": "Need some potions.", "next_node_id": "merchant_show_potions_friendly"},
                    {"text": "Never mind, I'll browse. (Trade)", "action": "open_trade_window", "ends_dialogue": True},
                    {"text": "Actually, nothing for now. Farewell.", "ends_dialogue": True}
                ]
            },
            "merchant_show_weapons_friendly": {
                "npc_line": "Weapons, eh? Got some fine steel, and a few enchanted pieces if your coin purse is heavy enough. Take a look!",
                "action": "open_trade_window:weapon", # Trade window filtered for weapons
                "ends_dialogue": True
            },
            "merchant_show_potions_friendly": {
                "npc_line": "Potions! Wise choice for any adventurer. Healing, magicka, resistances... I've got a good stock.",
                "action": "open_trade_window:potion", # Trade window filtered for potions
                "ends_dialogue": True
            },
            "merchant_rumors_friendly": {
                "npc_line": "Always something stirring. Just the other day, I heard [GenericRumorTopic]. And there's talk of a [QuestHintAdjective] [QuestHintNoun] over at [QuestHintLocation]. Might be worth looking into if you're the adventurous type.",
                "action": ["share_rumor:local", "offer_quest_if_available:merchant_delivery_task"], # Example of multiple actions
                "player_responses": [
                    {"text": "Interesting. Thanks for the tip.", "ends_dialogue": True, "disposition_change": 2},
                    {"text": "Tell me more about that [QuestHintNoun].", "next_node_id": "merchant_quest_details_delivery", "condition": "quest_available:merchant_delivery_task"}
                ]
            },
            "merchant_quest_details_delivery": { # Example quest node
                "npc_line": "Ah, the [QuestHintNoun]! Yes, I need a package delivered to [QuestTargetLocation]. It's a bit out of the way, and the roads can be dangerous. I can offer [QuestRewardGoldAmount] gold for your trouble. Interested?",
                "player_responses": [
                    {"text": "I'll do it.", "action": "start_quest:merchant_delivery_task:[QuestTargetLocation]:[QuestRewardGoldAmount]", "disposition_change": 10, "next_node_id": "merchant_quest_accepted_delivery"},
                    {"text": "Sounds too dangerous for me.", "disposition_change": -3, "ends_dialogue": True},
                    {"text": "Let me think about it.", "ends_dialogue": True}
                ]
            },
            "merchant_quest_accepted_delivery": {
                "npc_line": "Excellent! Here's the package. Deliver it to [QuestTargetNPC] in [QuestTargetLocation]. Be careful out there!",
                "ends_dialogue": True
            }
        }
    },
    "STENVAR_BARD_MAIN": { # Example for a specific NPC
        "start_node": "stenvar_intro",
        "nodes": {
            "stenvar_intro": {
                "on_enter_action": "set_flag:met_stenvar",
                "npc_line": "{Purpose} \"{Greeting} What can an old bard do for you, [PlayerName]? Or perhaps you have a tale for my repertoire?\"",
                "player_responses": [
                    {"text": "Tell me a story of old Skyrim.", "next_node_id": "stenvar_story_ysgramor"},
                    {"text": "What do you know of this place, [LocationName]?", "next_node_id": "stenvar_discuss_location_generic"},
                    {"text": "I'm looking for rumors or work.", "next_node_id": "stenvar_rumors_work", "condition": "not npc.has_offered_quest_today"},
                    {"text": "Your purpose seems noble, Stenvar.", "next_node_id": "stenvar_purpose_acknowledged", "disposition_change": 3},
                    {"text": "Farewell, bard.", "ends_dialogue": True}
                ]
            },
            "stenvar_story_ysgramor": {
                "npc_line": "\"Ah, a classic! They say Ysgramor, when he first set foot on these shores, wept for the beauty of the land, even as he prepared to conquer it. A true Nord paradox, eh? Full of passion and fury, love and war, all mixed in one hearty stew!\"",
                "player_responses": [
                    {"text": "A fine tale. Do you know others?", "next_node_id": "stenvar_story_dragon_cult", "disposition_change": 2},
                    {"text": "Inspiring words.", "next_node_id": "stenvar_intro", "disposition_change": 1}
                ]
            },
            "stenvar_story_dragon_cult": {
                "npc_line": "\"Indeed! Ever heard of the Dragon Cult? Ancient priests who worshipped the Dov, the dragons themselves! Their temples dot the highest peaks, filled with draugr and secrets best left undisturbed. Or so the sensible folk say... adventurers rarely listen!\"",
                "player_responses": [
                    {"text": "Fascinating. You're a wellspring of lore.", "next_node_id": "stenvar_intro", "disposition_change": 3},
                    {"text": "Perhaps I'll visit one of those temples.", "next_node_id": "stenvar_temple_warning"}
                ]
            },
            "stenvar_temple_warning": {
                "npc_line": "\"Brave, or foolish! If you do, tread carefully. The old magic lingers, and the guardians do not sleep soundly. May Kyne watch over your steps.\"",
                "ends_dialogue": True
            },
            "stenvar_discuss_location_generic": {
                "npc_line": "\"Ah, [LocationName]? {LocationFlavor}. It has its own rhythm, its own secrets, like any place touched by the long hand of history.\"", # {LocationFlavor} will be filled by a helper
                "player_responses": [
                    {"text": "Well said.", "next_node_id": "stenvar_intro"}
                ]
            },
            "stenvar_rumors_work": {
                "npc_line": "\"Rumors, eh? This old bard hears many whispers on the wind. For instance, they say [GenericRumorTopic]. As for work... well, my old lute, 'Whisperwind', was stolen by some ruffians who mistook it for something valuable. It's precious to me, sentimentally. If you could retrieve it from their hideout at [DynamicBanditCampName], I'd be in your debt.\"",
                "action": ["share_rumor:local_legends", "offer_quest_if_available:stenvar_lost_lute"],
                "player_responses": [
                    {"text": "Tell me more about this stolen lute.", "next_node_id": "stenvar_lute_quest_details", "condition": "quest_available:stenvar_lost_lute"},
                    {"text": "I'll keep an ear out for those rumors. Farewell.", "ends_dialogue": True}
                ]
            },
            "stenvar_lute_quest_details": {
                "npc_line": "\"Whisperwind... a simple wooden lute, but it's seen me through countless nights and sung countless tales. Those bandits at [DynamicBanditCampName] probably think it's worthless. I can offer you what little coin I have, say 150 septims, and perhaps a song in your honor?\"",
                "player_responses": [
                    {"text": "I will retrieve your lute, Stenvar.", "action": "start_quest:stenvar_lost_lute:[DynamicBanditCampName]:150", "disposition_change": 15, "next_node_id": "stenvar_lute_quest_accepted"},
                    {"text": "150 septims isn't much for facing bandits.", "next_node_id": "stenvar_lute_quest_haggle", "condition": "skill_check:speech:12", "disposition_change": -2},
                    {"text": "I'm not interested in such a task right now.", "ends_dialogue": True, "disposition_change": -5}
                ]
            },
            "stenvar_lute_quest_accepted": {
                "npc_line": "\"Blessings of the Divines upon you, [PlayerName]! Be careful at [DynamicBanditCampName]. Those thugs are not known for their hospitality.\"",
                "ends_dialogue": True
            },
             "stenvar_lute_quest_haggle": {
                "npc_line": "\"Ah, a sharp one! True, it's not a king's ransom. But it's all an old bard can offer. Perhaps... 200 septims, and I'll compose a verse about your bravery, win or lose?\"",
                "player_responses": [
                    {"text": "Alright, 200 septims and a song it is. I'll get your lute.", "action": "start_quest:stenvar_lost_lute:[DynamicBanditCampName]:200", "disposition_change": 10, "next_node_id": "stenvar_lute_quest_accepted"},
                    {"text": "Still not enough. Good day.", "ends_dialogue": True, "disposition_change": -8}
                ]
            },
            "stenvar_purpose_acknowledged":{
                "npc_line": "\"Thank you, [PlayerName]. In these fractured times, a little harmony can go a long way. Perhaps you too seek to mend what is broken?\"",
                "player_responses": [
                    {"text": "I try my best.", "next_node_id": "stenvar_intro", "disposition_change": 2},
                    {"text": "I'm just looking out for myself.", "next_node_id": "stenvar_intro", "disposition_change": -2}
                ]
            }
            # More nodes for Stenvar, handling quest completion, other stories, etc.
        }
    }
    # Add more dialogue trees for different NPC roles, dispositions, specific characters, etc.
}

# Helper function to get a random line if npc_line is a list
def get_npc_line(node):
    if isinstance(node["npc_line"], list):
        return random.choice(node["npc_line"])
    return node["npc_line"]

# Helper function to replace placeholders in text
def format_dialogue_text(text, player, npc, current_location, game_data=None):
    # game_data could be a dictionary holding dynamic elements like quest item names, etc.
    if game_data is None:
        game_data = {}

    replacements = {
        "[PlayerName]": player.full_name if player else "Traveler",
        "[NPCName]": npc.name if npc else "Stranger",
        "[LocationName]": current_location.get("name", "this place") if current_location else "these parts",
        "[NPCRace]": npc.race.capitalize() if npc and hasattr(npc, 'race') else "Unknown Race",
        "[PlayerRace]": player.race.capitalize() if player and hasattr(player, 'race') else "Unknown Race",
        "[JarlName]": game_data.get("jarl_name", "the Jarl"), # Needs to be populated by game logic
        "[LocalTavernName]": game_data.get("local_tavern_name", "the local tavern"), # Needs to be populated
        "[GenericRumorTopic]": game_data.get("generic_rumor_topic", "strange lights in the sky"), # Needs to be populated
        "[QuestHintAdjective]": game_data.get("quest_hint_adjective", "ancient"),
        "[QuestHintNoun]": game_data.get("quest_hint_noun", "artifact"),
        "[QuestHintLocation]": game_data.get("quest_hint_location", "a nearby ruin"),
        "[QuestTargetLocation]": game_data.get("quest_target_location", "a distant city"), # Specific to quest
        "[QuestTargetNPC]": game_data.get("quest_target_npc", "a contact"), # Specific to quest
        "[QuestRewardGoldAmount]": str(game_data.get("quest_reward_gold", "a fair sum of")), # Specific to quest
        "[DynamicBanditCampName]": game_data.get("dynamic_bandit_camp_name", "a nearby bandit camp"), # Needs dynamic generation
        # Add more placeholders as needed
    }
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, str(value))
    
    # Special placeholder for NPC's own greeting and purpose if used in a node
    if "{Greeting}" in text and hasattr(npc, '_generate_greeting'):
        text = text.replace("{Greeting}", npc._generate_greeting())
    if "{Purpose}" in text and hasattr(npc, '_generate_purpose'):
        text = text.replace("{Purpose}", npc._generate_purpose())
    if "{LocationFlavor}" in text and current_location and hasattr(flavor, 'get_flavor'):
        # Simplified flavor fetching for location within dialogue
        class DummyLoc:
            def __init__(self, tags): self.tags = {"location": {"environment": tags if isinstance(tags, list) else [tags]}} # Basic
        
        loc_flavor_tags = current_location.get("tags", [])
        # Prioritize more specific tags for flavor if available
        priority_tags = [t for t in ["city", "town", "village", "forest", "mountain", "cave", "ruin", "tavern"] if t in loc_flavor_tags]
        
        flavor_text_for_loc = ""
        if priority_tags:
            flavors = flavor.get_flavor(DummyLoc(priority_tags[0])) # Get flavor for the most specific tag
            if flavors: flavor_text_for_loc = random.choice(flavors)
        
        if not flavor_text_for_loc and loc_flavor_tags: # Fallback to any tag
             flavors = flavor.get_flavor(DummyLoc(loc_flavor_tags[0]))
             if flavors: flavor_text_for_loc = random.choice(flavors)

        text = text.replace("{LocationFlavor}", flavor_text_for_loc if flavor_text_for_loc else "It's a place with its own stories, that's for sure.")


    return UI.capitalize_dialogue(text)