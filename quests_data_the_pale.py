# quests_data_the_pale.py

THE_PALE_QUEST_TEMPLATES = [
    {
        "id": "pale_nightmare_investigation",
        "title_template": "The Whispering Dreams of Dawnstar",
        "desc_template": "The residents of Dawnstar are plagued by terrible nightmares. Investigate the cause of these unsettling dreams, which some attribute to the abandoned Nightcaller Temple.",
        "lore_tags": ["pale", "dawnstar", "nightmares", "vaermina", "daedric_influence", "mystery", "temple_sealed"],
        "location_tags_required": ["dawnstar", "temple_sealed", "daedric_influence_vaermina"], # Dawnstar and Nightcaller Temple are key
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["investigate", "supernatural", "daedric"], "difficulty": ["hard"], "moral": ["ethical", "gray"], "urgency": ["urgent"]}},
        "turn_in_role_hint": ["jarl_dawnstar", "priest_mara", "scholar_arcane"], # Jarl Skald, Erandur (if available), or a general scholar
        "stages": [
            {
                "stage_name": "Gather Information in Dawnstar",
                "objectives": [
                    {"id": "obj_talk_jarl_dawnstar_nightmare", "type": "talk_to_npc", "npc_id": "jarl_skald_the_elder_ID", "note": "Speak to Jarl Skald the Elder in Dawnstar about the nightmares."},
                    {"id": "obj_talk_innkeeper_dawnstar_nightmare", "type": "talk_to_npc", "npc_id": "innkeeper_windpeak_inn_ID", "note": "Gather rumors from the Windpeak Inn about the dreams."}
                ],
                "on_completion_dialogue": "The Jarl and locals confirm the nightmares are widespread and point to Nightcaller Temple as the source. A priest of Mara, Erandur, who is troubled by the same dreams, might know more.",
                "branch_options": []
            },
            {
                "stage_name": "Investigate Nightcaller Temple",
                "objectives": [
                    {"id": "obj_reach_nightcaller_pale", "type": "reach_location", "location_name": "Nightcaller Temple", "note": "Travel to the eerie Nightcaller Temple overlooking Dawnstar."},
                    {"id": "obj_find_entrance_nightcaller_pale", "type": "investigate", "location_name": "Nightcaller Temple", "note": "Find a way to enter the sealed temple (perhaps with Erandur's help, or Lockpicking check DC 15)."},
                    {"id": "obj_deal_with_cultists_nightcaller_pale", "type": "kill", "target_name": "vaermina cultist", "target_id": "vaermina_cultist_ID", "count": 5, "note": "Deal with the cultists or afflicted within the temple."}
                ],
                "on_completion_dialogue": "You've entered the temple and cleared a path. The source of the nightmares, the Skull of Corruption, is deeper within. Erandur reveals a ritual to destroy it, but its power is tempting. A decision awaits: cleanse the temple or harness its power?",
                "branch_options": [
                    {"choice_id": "cleanse_temple_pale", "text": "Aid Erandur to cleanse the temple and destroy the Skull (Ethical/Good).", "next_stage_index": 2},
                    {"choice_id": "harness_power_pale", "text": "Betray Erandur and claim the Skull of Corruption for yourself (Daedric/Selfish).", "next_stage_index": 3}
                ]
            },
            { # Stage 2: Cleanse Temple
                "stage_name": "Cleanse the Temple",
                "objectives": [
                    {"id": "obj_perform_cleansing_pale", "type": "event_trigger", "event_type": "nightcaller_temple_cleansing_ritual", "note": "Assist Erandur in performing the cleansing ritual at the temple's core."},
                    {"id": "obj_defeat_boss_cleanse_pale", "type": "kill", "target_name": "dream_corruptor_spirit", "target_id": "vermina_dreamstrider_ID", "count": 1, "note": "Defeat the lingering spirit of Vaermina's influence or corrupted guardians."}
                ],
                "on_completion_dialogue": "The nightmares cease. A quiet peace settles over Dawnstar. Erandur thanks you for your aid. Return to [QUEST_GIVER_NAME] or Jarl Skald.",
                "reward_modifier": {"reputation_dawnstar_bonus": 20, "gold_bonus": 300, "experience_bonus": 200, "item_bonus": "amulet_of_mara_blessed"},
                "final_stage": True
            },
            { # Stage 3: Harness Power
                "stage_name": "Harness the Temple's Power",
                "objectives": [
                    {"id": "obj_betray_erandur_pale", "type": "kill", "target_name": "Erandur", "target_id": "erandur_priest_ID", "count": 1, "note": "Eliminate Erandur before he completes the ritual."},
                    {"id": "obj_claim_skull_corruption_pale", "type": "collect_item", "item_key": "skull_of_corruption", "count": 1, "note": "Claim the Skull of Corruption for yourself."}
                ],
                "on_completion_dialogue": "The Skull of Corruption is yours. Its dark power pulses in your hand, though its whispers may linger. You feel a surge of arcane might. Dawnstar's fate is now uncertain. (No direct turn-in for this path, quest completes)",
                "reward_modifier": {"gold_bonus": 100, "experience_bonus": 250, "item_bonus": "skull_of_corruption", "magicka_permanent_gain": 20, "reputation_daedric_princes_minor_bonus": 5, "reputation_dawnstar_bonus": -15},
                "final_stage": True,
                "failure_state": True # Can be considered a morally grey/failed outcome for the town
            }
        ]
    },
    {
        "id": "pale_ice_troll_hunt",
        "title_template": "The Ice Troll of [MOUNTAIN_NAME]",
        "desc_template": "A monstrous Ice Troll has made its lair in the mountains near [LOCATION_NAME] in The Pale, terrorizing travelers and hunters. Hunt down the beast and make the roads safe.",
        "lore_tags": ["pale", "troll_ice", "hunt_dangerous", "mountain_cold", "road_safety"],
        "location_tags_required": ["mountain", "wilderness_cold", "arctic", "cave_lair"], # Specific to cold, mountainous regions of The Pale
        "level_range": (5, 9),
        "flavor_tags": {"quest": {"type": ["hunt", "extermination"], "difficulty": ["medium"], "moral": ["ethical", "survival"]}},
        "turn_in_role_hint": ["hunter_pale", "guard_dawnstar", "jarl_steward_dawnstar"],
        "stages": [
            {
                "stage_name": "Track the Troll",
                "objectives": [
                    {"id": "obj_track_troll_pale", "type": "track", "target_name": "ice troll", "note": "Follow the tracks of the Ice Troll into its mountain lair in The Pale (Survival check DC 13)."},
                    {"id": "obj_reach_troll_lair_pale", "type": "reach_location", "location_name": "[CAVE_TYPE]", "note": "Locate the Ice Troll's cave."} # [CAVE_TYPE] to be resolved
                ],
                "on_completion_dialogue": "You've found the troll's lair. Its growls echo from within. The air is frigid.",
                "branch_options": []
            },
            {
                "stage_name": "Slay the Beast",
                "objectives": [
                    {"id": "obj_kill_ice_troll_pale", "type": "kill", "target_name": "ice troll", "target_id": "ice_troll_alpha_pale_ID", "count": 1, "note": "Slay the monstrous Ice Troll."},
                    {"id": "obj_collect_trophy_troll_pale", "type": "collect_item", "item_key": "ice_troll_heart_trophy", "count": 1, "note": "Collect a trophy as proof."}
                ],
                "on_completion_dialogue": "The Ice Troll is defeated. Its reign of terror in The Pale is over. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 180, "experience_bonus": 100, "item_bonus": "potion_resist_frost_superior"},
                "final_stage": True
            }
        ]
    }
    # Add more quests specific to The Pale here
]