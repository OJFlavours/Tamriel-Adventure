# quests_data_falkreath.py

FALKREATH_QUEST_TEMPLATES = [
    {
        "id": "falkreath_cursed_locket_sorrow", # Specific ID
        "title_template": "A Glimmer of Sorrow: The Locket of Kael",
        "desc_template": "A cursed silver locket found in a ruined watchtower near Falkreath emanates profound sorrow. It seems to be tied to a vengeful spirit named Kael and a tragic love story. Uncover its history and put the spirit to rest.",
        "lore_tags": ["falkreath", "ghost_vengeful", "cursed_item_locket", "undead_sorrowful", "tragic_lore_love", "graveyard_secrets"],
        "location_tags_required": ["falkreath_hold", "ruin_watchtower", "graveyard_ancient", "cursed_presence"], # Falkreath and its gloomy surroundings
        "level_range": (3, 7),
        "flavor_tags": {"quest": {"type": ["investigate", "supernatural", "exorcism_gentle"], "moral": ["ethical_compassion", "gray_justice"], "urgency": ["important_local"]}},
        "turn_in_role_hint": ["priest_arkay_falkreath", "scholar_local_history", "elder_falkreath"], # Runil or similar
        "stages": [
            {
                "stage_name": "Examine the Locket and Seek Knowledge",
                "objectives": [
                    {"id": "obj_examine_locket_falkreath", "type": "collect_item", "item_key": "silver_locket_kael_cursed", "count": 1, "note": "Obtain and examine the cursed locket. Its sorrow chills you."},
                    {"id": "obj_talk_to_priest_runil_falkreath", "type": "talk_to_npc", "npc_id": "runil_priest_of_arkay_ID", "note": "Consult Runil, the priest of Arkay in Falkreath, about the locket's history and the spirit."},
                    {"id": "obj_visit_graveyard_falkreath_clues", "type": "reach_location", "location_name": "Falkreath Graveyard", "note": "Search the Falkreath graveyard for clues about Kael and his lost love, Elara."}
                ],
                "on_completion_dialogue": "Runil tells you a tale of Kael, a soldier, and Elara, his love, separated by war. Kael's spirit is bound to the locket, unable to find peace. Elara's grave might hold the key. Kael's restless spirit is likely at the place he fell, the [RUIN_NAME].",
                "branch_options": []
            },
            {
                "stage_name": "Confront and Resolve the Spirit",
                "objectives": [
                    {"id": "obj_reach_kael_tomb_ruin_falkreath", "type": "reach_location", "location_name": "[RUIN_NAME]", "note": "Travel to Kael's restless haunting ground at the [RUIN_NAME]."}, # [RUIN_NAME] to be resolved
                    {"id": "obj_commune_kael_spirit_falkreath", "type": "talk_to_npc", "npc_id": "vengeful_spirit_kael_ID", "note": "Communicate with Kael's vengeful spirit. He yearns for Elara."}
                ],
                "on_completion_dialogue": "Kael's spirit reveals its deepest sorrow: to be reunited with Elara by placing the locket on her grave. You can help him find peace, or forcibly banish him if diplomacy fails.",
                "branch_options": [
                    {"choice_id": "help_kael_peace_falkreath", "text": "Help Kael find peace by finding Elara's grave and placing the locket there (Persuasion/Restoration check DC 14).", "next_stage_index": 2},
                    {"choice_id": "banish_kael_force_falkreath", "text": "Banish Kael's spirit by force (Destruction/Conjuration check DC 16, or combat).", "next_stage_index": 3}
                ]
            },
            { # Stage 2: Help Kael Find Peace
                "stage_name": "Peaceful Resolution",
                "objectives": [
                    {"id": "obj_find_elara_grave_falkreath", "type": "reach_location", "location_name": "Falkreath Graveyard (Elara's Grave)", "note": "Find Elara's specific grave in the Falkreath Graveyard."},
                    {"id": "obj_place_locket_elara_falkreath", "type": "use_item", "item_key": "silver_locket_kael_cursed", "location_name": "Falkreath Graveyard (Elara's Grave)", "note": "Place Kael's locket at Elara's grave."}
                ],
                "on_completion_dialogue": "Kael's spirit appears, now peaceful, and fades into a gentle light with Elara. The locket's curse lifts. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_falkreath_arkay_bonus": 15, "gold_bonus": 150, "experience_bonus": 100, "item_bonus": "amulet_of_arkay_enhanced"},
                "final_stage": True
            },
            { # Stage 3: Banish Kael by Force
                "stage_name": "Forceful Banishment",
                "objectives": [
                    {"id": "obj_kill_kael_spirit_falkreath", "type": "kill", "target_name": "vengeful spirit of Kael", "target_id": "vengeful_spirit_kael_ID", "count": 1, "note": "Banish Kael's spirit by force."}
                ],
                "on_completion_dialogue": "Kael's spirit is violently dispersed, but the haunting sorrow lingers faintly. The place feels colder. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"reputation_falkreath_arkay_bonus": 5, "gold_bonus": 200, "experience_bonus": 120, "item_bonus": "silver_sword"}, # Less reputation for forceful approach
                "final_stage": True
            }
        ]
    },
    {
        "id": "falkreath_dark_brotherhood_initiation_aventus", # Specific ID
        "title_template": "Innocence Lost: Aventus Aretino's Plea",
        "desc_template": "Rumors speak of a child in Windhelm, Aventus Aretino, attempting the Black Sacrament to summon the Dark Brotherhood. Investigate this dark ritual. Your actions may lead you to the hidden sanctuary of the Dark Brotherhood near Falkreath, should you choose to follow their bloody path.",
        "lore_tags": ["dark_brotherhood_recruitment", "assassins_guild", "black_sacrament_ritual", "falkreath_sanctuary", "windhelm_aventus", "secret_society_dark", "moral_choice_contract"],
        "location_tags_required": ["windhelm_aretino_residence", "falkreath_dark_brotherhood_active", "dark_brotherhood_sanctuary"], # Links Windhelm to Falkreath
        "level_range": (5, 10), # Adjusted level, as it's an early DB quest
        "flavor_tags": {"quest": {"type": ["investigate", "spy", "assassination_contract"], "difficulty": ["medium","hard"], "moral": ["unethical_choice", "gray_area"], "urgency": ["important_faction"]}},
        "turn_in_role_hint": ["astrid_dark_brotherhood_leader"], # Astrid is the key turn-in
        "stages": [
            {
                "stage_name": "Investigate the Black Sacrament",
                "objectives": [
                    {"id": "obj_reach_windhelm_aventus_db", "type": "reach_location", "location_name": "Aretino Residence (Windhelm)", "note": "Travel to Windhelm and investigate the Aretino Residence, where the Black Sacrament was performed."},
                    {"id": "obj_talk_aventus_aretino_db", "type": "talk_to_npc", "npc_id": "aventus_aretino_child_ID", "note": "Speak to Aventus Aretino about his ritual and his target: Grelod the Kind."}
                ],
                "on_completion_dialogue": "Aventus confirms he performed the Black Sacrament. He wants Grelod the Kind, the cruel orphanage matron in Riften, dead. You now have a choice: fulfill the contract or report it.",
                "branch_options": [
                    {"choice_id": "fulfill_contract_grelod", "text": "Fulfill the contract and kill Grelod the Kind.", "next_stage_index": 1},
                    {"choice_id": "report_contract_grelod", "text": "Report the contract to the Riften guards.", "next_stage_index": 2}
                ]
            },
            { # Stage 1: Fulfill Contract
                "stage_name": "Execute the Contract",
                "objectives": [
                    {"id": "obj_reach_orphanage_riften_db", "type": "reach_location", "location_name": "Honorhall Orphanage (Riften)", "note": "Travel to Honorhall Orphanage in Riften."},
                    {"id": "obj_kill_grelod_the_kind_db", "type": "kill", "target_name": "Grelod the Kind", "target_id": "grelod_the_kind_matron_ID", "count": 1, "note": "Assassinate Grelod the Kind."}
                ],
                "on_completion_dialogue": "Grelod is dead. Upon sleeping, you receive a mysterious note: 'We know.' You awaken in an Abandoned Shack, a captive of Astrid, leader of the Dark Brotherhood. This leads to the quest 'With Friends Like These...'",
                # This quest effectively ends here, leading to the next DB quest.
                "reward_modifier": {"reputation_dark_brotherhood_contact_made": 5, "experience_bonus": 50},
                "final_stage": True # Marks completion of "Innocence Lost"
            },
            { # Stage 2: Report Contract (Quest Failure/Alternative)
                "stage_name": "Report the Contract",
                "objectives": [
                    {"id": "obj_talk_guard_contract_riften_db", "type": "talk_to_npc", "npc_id": "riften_guard_captain_ID", "note": "Report the Black Sacrament and Aventus's request to a Riften guard captain."},
                    {"id": "obj_witness_grelod_investigation_db", "type": "event_trigger", "event_type": "grelod_investigation_starts", "note": "The guards will investigate Grelod. Aventus will be disappointed."}
                ],
                "on_completion_dialogue": "Grelod is investigated, and Aventus is likely taken care of by the authorities. The Dark Brotherhood will not contact you. This path ends here.",
                "reward_modifier": {"reputation_riften_guards_bonus": 5, "reputation_dark_brotherhood_contact_failed": -10, "gold_bonus": 50},
                "final_stage": True,
                "failure_state": True # Failure from DB perspective
            }
        ]
    }
    # Add more Falkreath specific quests here
]