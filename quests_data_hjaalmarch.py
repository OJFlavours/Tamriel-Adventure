# quests_data_hjaalmarch.py

HJAALMARCH_QUEST_TEMPLATES = [
    {
        "id": "hjaalmarch_vampire_investigation_morthal", # Specific ID
        "title_template": "The Shadow Over Morthal: Laid to Rest",
        "desc_template": "Strange deaths and whispers of vampirism plague Morthal. A child's house burned down, and her ghost haunts the ruins. Investigate the unsettling occurrences, uncover the truth behind the shadow creeping over the marsh, and bring peace to the tormented spirits.",
        "lore_tags": ["hjaalmarch", "morthal", "vampire_conspiracy", "superstition_marsh", "mystery_ghost", "investigation_dark", "laid_to_rest"],
        "location_tags_required": ["morthal", "marsh_gloomy", "vampire_rumors_strong", "haunted_location"], # Morthal and its eerie surroundings
        "level_range": (6, 11),
        "flavor_tags": {"quest": {"type": ["investigate", "supernatural", "exorcism"], "difficulty": ["medium", "hard"], "moral": ["ethical_justice"], "urgency": ["urgent_community"]}},
        "turn_in_role_hint": ["jarl_morthal", "falion_morthal_wizard", "concerned_citizen_morthal"], # Jarl Idgrod, Falion
        "stages": [
            {
                "stage_name": "Gather Clues in Morthal",
                "objectives": [
                    {"id": "obj_talk_jarl_morthal_vamp", "type": "talk_to_npc", "npc_id": "jarl_idgrod_ravencrone_ID", "note": "Speak to Jarl Idgrod Ravencrone in Morthal about the strange occurrences."},
                    {"id": "obj_investigate_burned_house_morthal", "type": "investigate", "location_name": "Burned House (Morthal)", "note": "Examine the recently burned house for clues and speak to the ghost of Helgi (Investigation check DC 14)."},
                    {"id": "obj_talk_falion_morthal_vamp", "type": "talk_to_npc", "npc_id": "falion_wizard_morthal_ID", "note": "Consult Falion, Morthal's wizard, about the nature of the evil and how to deal with vampires."}
                ],
                "on_completion_dialogue": "Falion confirms your fears: a master vampire, Movarth Piquine, is responsible, hiding in Movarth's Lair. He offers a way to deal with it, but you'll need to be prepared. The ghost of Helgi also points towards the vampire Alva.",
                "branch_options": []
            },
            {
                "stage_name": "Confront the Vampire Coven",
                "objectives": [
                    {"id": "obj_deal_with_alva_morthal", "type": "confront", "npc_id": "alva_vampire_morthal_ID", "note": "Confront Alva in her house. She may attack or offer information if intimidated."},
                    {"id": "obj_reach_movarth_lair_morthal", "type": "reach_location", "location_name": "Movarth's Lair", "note": "Infiltrate Movarth's Lair, the master vampire's den."},
                    {"id": "obj_kill_movarth_piquine", "type": "kill", "target_name": "Movarth Piquine (Master Vampire)", "target_id": "movarth_piquine_vampire_ID", "count": 1, "note": "Slay Movarth Piquine, the master vampire, and his thralls."}
                ],
                "on_completion_dialogue": "Movarth and his coven are defeated. The shadow over Morthal lifts, and Helgi's spirit can find peace. Return to [QUEST_GIVER_NAME] or Jarl Idgrod.",
                "reward_modifier": {"reputation_morthal_bonus": 20, "gold_bonus": 350, "experience_bonus": 200, "item_bonus": "silver_sword_enchanted_undead"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "hjaalmarch_lost_horn_of_jurgen_ustengrav", # Specific ID
        "title_template": "The Horn of Jurgen Windcaller: Ustengrav's Trial",
        "desc_template": "The Greybeards of High Hrothgar seek a lost relic: the Horn of Jurgen Windcaller, believed to be hidden deep within the ancient Nordic tomb of Ustengrav in Hjaalmarch's marshes. This is a crucial step in proving yourself to them if you are Dragonborn.",
        "lore_tags": ["hjaalmarch", "greybeards_quest", "ustengrav_tomb", "way_of_the_voice", "ancient_nords_trial", "relic_hunt_sacred", "dragonborn_path"],
        "location_tags_required": ["barrow_major", "dungeon_ancient_nordic", "marsh_hjaalmarch", "greybeards_quest_active", "ustengrav"], # Ustengrav is key
        "level_range": (8, 13), # Assumes player has met Greybeards
        "flavor_tags": {"quest": {"type": ["fetch", "explore", "trial_sacred"], "difficulty": ["hard"], "moral": ["ethical_duty"], "urgency": ["important_dragonborn"]}},
        "turn_in_role_hint": ["greybeard_arngeir", "delphine_blades_contact"], # Arngier, or Delphine if Horn is missing
        "stages": [
            {
                "stage_name": "Journey to Ustengrav",
                "objectives": [
                    {"id": "obj_reach_ustengrav_hjaal", "type": "reach_location", "location_name": "Ustengrav Depths", "note": "Travel to the ancient and treacherous tomb of Ustengrav in the marshes of Hjaalmarch."}
                ],
                "on_completion_dialogue": "Ustengrav's entrance looms, shrouded in mist. The air is heavy with ancient echoes and the weight of history.",
                "branch_options": []
            },
            {
                "stage_name": "Retrieve the Horn (or a Note)",
                "objectives": [
                    {"id": "obj_navigate_ustengrav_hjaal", "type": "investigate", "location_name": "Ustengrav Puzzle Gauntlet", "note": "Navigate the complex traps, puzzles (like the three runestones), and restless dead within Ustengrav (Perception/Acrobatics check DC 15)."},
                    {"id": "obj_find_horn_or_note_ustengrav", "type": "collect_item", "item_key": "note_from_friend_horn_location", "count": 1, "note": "Reach the pedestal where the Horn of Jurgen Windcaller should be. (It will be missing, find the note instead)."}
                ],
                "on_completion_dialogue": "The Horn is gone! In its place, you find a mysterious note addressed to the Dragonborn, instructing you to rent the attic room at the Sleeping Giant Inn in Riverwood. Someone knows you're coming.",
                "reward_modifier": {"experience_bonus": 100}, # Partial reward for this stage
                # This quest naturally leads into "A Blade in the Dark"
                "final_stage": False # Not the true final stage of the Horn retrieval
            },
            { # This stage is more of a bridge to the next main quest part
                "stage_name": "A Secret Meeting",
                "objectives": [
                     {"id": "obj_rent_attic_room_riverwood", "type": "reach_location", "location_name": "Sleeping Giant Inn (Attic Room)", "note": "Travel to Riverwood and rent the attic room at the Sleeping Giant Inn."},
                     {"id": "obj_meet_delphine_horn", "type": "talk_to_npc", "npc_id": "delphine_innkeeper_ID", "note": "Meet with Delphine, who will return the Horn of Jurgen Windcaller to you."}
                ],
                "on_completion_dialogue": "Delphine reveals herself and returns the Horn. She has her own agenda concerning the dragons. Now, you can return the Horn to the Greybeards.",
                "reward_modifier": {"reputation_greybeards_bonus": 25, "gold_bonus": 0, "experience_bonus": 150, "item_bonus": "horn_of_jurgen_windcaller_actual"}, # Actual Horn is the item
                "final_stage": True # This completes the "Horn of Jurgen Windcaller" quest itself
            }
        ]
    }
    # Add more Hjaalmarch specific quests here
]