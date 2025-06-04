# quests_data_whiterun.py

WHITERUN_QUEST_TEMPLATES = [
    {
        "id": "whiterun_lost_shipment_investigation",
        "title_template": "The Missing Caravan from Whiterun",
        "desc_template": "A merchant caravan carrying valuable goods from Whiterun has gone missing on the plains. Investigate its disappearance and recover what you can.",
        "lore_tags": ["whiterun", "commerce", "trade", "plains", "investigation"],
        "location_tags_required": ["whiterun", "plains", "trade_route"], # More specific than just "trade"
        "level_range": (3, 7),
        "flavor_tags": {"quest": {"type": ["investigate", "fetch"], "difficulty": ["medium"], "moral": ["ethical"]}},
        "turn_in_role_hint": ["merchant", "guard_captain", "jarl_steward"], # Whiterun specific roles
        "stages": [
            {
                "stage_name": "Search the Plains",
                "objectives": [
                    {"id": "obj_search_plains_whiterun", "type": "investigate", "location_name": "Whiterun Hold Plains", "note": "Search the plains outside Whiterun for signs of the missing caravan (Survival check DC 12)."},
                    {"id": "obj_find_wreckage_whiterun", "type": "reach_location", "location_name": "Caravan Wreckage Site", "note": "Locate the wreckage of the caravan."}
                ],
                "on_completion_dialogue": "You find the remains of the caravan, clearly ambushed. Bandits, perhaps? Or something worse... A survivor might still be here.",
                "branch_options": []
            },
            {
                "stage_name": "Uncover the Truth",
                "objectives": [
                    {"id": "obj_talk_survivor_whiterun", "type": "talk_to_npc", "npc_id": "caravan_survivor_whiterun_ID", "note": "Speak to the lone, injured survivor of the attack."},
                    {"id": "obj_collect_manifest_whiterun", "type": "collect_item", "item_key": "caravan_manifest_whiterun", "count": 1, "note": "Retrieve the caravan's manifest from the wreckage."}
                ],
                "on_completion_dialogue": "The survivor points to a nearby cave, [CAVE_TYPE], as the raiders' lair. They were not bandits, but a strange cult seeking specific artifacts listed on the manifest. You have a choice: pursue the cult or report back to [QUEST_GIVER_NAME].",
                "branch_options": [
                    {"choice_id": "pursue_cult_whiterun", "text": "Pursue the cult to recover the artifacts.", "next_stage_index": 2},
                    {"choice_id": "report_back_whiterun", "text": "Report back to [QUEST_GIVER_NAME] with the manifest and survivor's tale.", "next_stage_index": 3}
                ]
            },
            { # Stage 2: Pursue Cult
                "stage_name": "Confront the Cult",
                "objectives": [
                    {"id": "obj_reach_cult_lair_whiterun", "type": "reach_location", "location_name": "[CAVE_TYPE]", "note": "Infiltrate the cult's lair."}, # [CAVE_TYPE] will be resolved
                    {"id": "obj_kill_cult_leader_whiterun", "type": "kill", "target_name": "cultist leader", "target_id": "cult_leader_ID", "count": 1, "note": "Defeat the cult leader."},
                    {"id": "obj_recover_artifacts_whiterun", "type": "collect_item", "item_key": "stolen_cult_artifact_whiterun", "count": 3, "note": "Recover the stolen artifacts."}
                ],
                "on_completion_dialogue": "The cult is dispersed, and the artifacts are retrieved. You now have a choice: return them to the merchant in Whiterun, or seek a scholar at the College of Winterhold who might pay more for them.",
                "branch_options": [
                    {"choice_id": "return_to_merchant_whiterun", "text": "Return artifacts to [QUEST_GIVER_NAME] in Whiterun.", "next_stage_index": 4},
                    {"choice_id": "seek_scholar_whiterun", "text": "Seek a scholar at the College of Winterhold.", "next_stage_index": 5}, # This could lead to a new quest or just a different turn-in
                    {"choice_id": "investigate_stormcloak_connection", "text": "Investigate the cult's potential ties to the Stormcloaks.", "next_stage_index": 6}
                ]
            },
            { # Stage 3: Report Back (Early Completion)
                "stage_name": "Report Findings",
                "objectives": [
                    {"id": "obj_report_to_giver_whiterun", "type": "talk_to_npc", "npc_id": "[QUEST_GIVER_ID]", "note": "Report your findings to [QUEST_GIVER_NAME] in Whiterun."}
                ],
                "on_completion_dialogue": "You've provided crucial information, though the goods remain lost. [QUEST_GIVER_NAME] thanks you for your honesty.",
                "reward_modifier": {"gold_bonus": 50, "reputation_whiterun_merchants_bonus": 5},
                "final_stage": True,
                "failure_state": True # Considered a "partial success" or "failure" for full recovery
            },
            { # Stage 4: Return to Merchant (Full Reward)
                "stage_name": "Return Artifacts to Merchant",
                "objectives": [
                    {"id": "obj_return_artifacts_merchant_whiterun", "type": "talk_to_npc", "npc_id": "[QUEST_GIVER_ID]", "note": "Return the recovered artifacts to [QUEST_GIVER_NAME] in Whiterun."}
                ],
                "on_completion_dialogue": "The merchant is overjoyed! These artifacts are more valuable than the original goods. Your efforts are greatly appreciated.",
                "reward_modifier": {"gold_bonus": 300, "experience_bonus": 150, "reputation_whiterun_merchants_bonus": 15, "item_bonus": "fine_whiterun_steel_dagger"},
                "final_stage": True
            },
            { # Stage 5: Seek Scholar (Alternative Reward)
                "stage_name": "Seek Scholar at College",
                "objectives": [
                    {"id": "obj_reach_college_whiterun_alt", "type": "reach_location", "location_name": "College of Winterhold", "note": "Travel to the College of Winterhold."},
                    {"id": "obj_talk_scholar_artifacts_whiterun_alt", "type": "talk_to_npc", "npc_id": "college_scholar_contacts_ID", "note": "Present the artifacts to a scholar at the College."}
                ],
                "on_completion_dialogue": "The scholar is fascinated by the artifacts' unique properties and offers a generous sum, along with some arcane knowledge.",
                "reward_modifier": {"gold_bonus": 400, "experience_bonus": 200, "reputation_college_of_winterhold_bonus": 10, "item_bonus": "apprentice_destruction_tome"},
                "final_stage": True
            },
            { # Stage 6: Investigate Stormcloak Connection
                "stage_name": "Investigate Stormcloak Connection",
                "objectives": [
                    {"id": "obj_talk_stormcloak_informant", "type": "talk_to_npc", "npc_id": "stormcloak_informant_ID", "note": "Speak to a Stormcloak informant in Whiterun."},
                    {"id": "obj_collect_evidence_stormcloak", "type": "collect_item", "item_key": "stormcloak_orders", "count": 1, "note": "Collect evidence of the cult's support for the Stormcloaks."}
                ],
                "on_completion_dialogue": "The informant reveals that the cult has been providing financial support to the Stormcloaks in exchange for protection. You now have a choice: report this information to the Imperial authorities or remain silent.",
                "branch_options": [
                    {"choice_id": "report_to_imperials", "text": "Report the cult's support for the Stormcloaks to the Imperial authorities.", "next_stage_index": 7},
                    {"choice_id": "remain_silent", "text": "Remain silent and allow the cult to continue supporting the Stormcloaks.", "next_stage_index": 8}
                ]
            },
            { # Stage 7: Report to Imperials
                "stage_name": "Report to Imperials",
                "objectives": [
                    {"id": "obj_talk_imperial_officer", "type": "talk_to_npc", "npc_id": "imperial_officer_ID", "note": "Report the cult's support for the Stormcloaks to an Imperial officer in Whiterun."},
                ],
                "on_completion_dialogue": "The Imperial officer thanks you for your information and promises to investigate the matter further. You have struck a blow against the Stormcloak rebellion.",
                "reward_modifier": {"gold_bonus": 200, "reputation_imperial_bonus": 15},
                "final_stage": True
            },
            { # Stage 8: Remain Silent
                "stage_name": "Remain Silent",
                "objectives": [
                    {"id": "obj_remain_silent", "type": "wait", "duration": 24, "note": "Remain silent about the cult's support for the Stormcloaks."}
                ],
                "on_completion_dialogue": "You have chosen to remain silent about the cult's support for the Stormcloaks. The rebellion continues to gain strength.",
                "reward_modifier": {"gold_bonus": 100, "reputation_stormcloak_bonus": 5},
                "final_stage": True
            }
        ]
    },
    {
        "id": "whiterun_companions_initiation",
        "title_template": "Proving Your Worth to the Companions",
        "desc_template": "The Companions of Jorrvaskr in Whiterun seek new recruits. Prove your strength and loyalty by undertaking a task for them, perhaps clearing a local beast den or recovering a lost weapon.",
        "lore_tags": ["whiterun", "companions_guild", "warrior_guild", "honor", "jorrvaskr"],
        "location_tags_required": ["whiterun", "tavern", "inn", "social_hub_popular"], # Broaden to allow starting from taverns in Whiterun
        "level_range": (1, 4),
        "flavor_tags": {"quest": {"type": ["hunt", "trial", "initiation"], "difficulty": ["easy"], "moral": ["ethical", "honorable"]}},
        "turn_in_role_hint": ["companion_warrior_leader"], # e.g. Kodlak, Skjor, Aela
        "stages": [
            {
                "stage_name": "Seek Out the Companions",
                "objectives": [
                    {"id": "obj_reach_jorrvaskr_comp", "type": "reach_location", "location_name": "Jorrvaskr", "note": "Travel to Jorrvaskr in Whiterun."},
                    {"id": "obj_talk_kodlak_comp", "type": "talk_to_npc", "npc_id": "kodlak_whitemane_ID", "note": "Speak to Kodlak Whitemane, the Harbinger of the Companions."}
                ],
                "on_completion_dialogue": "Kodlak has a task for you: clear out a troublesome [BEAST_DEN_TYPE] near [LOCATION_NAME]. A simple test of your mettle.", # [BEAST_DEN_TYPE] and [LOCATION_NAME] to be resolved
                "branch_options": []
            },
            {
                "stage_name": "Clear the Beast Den",
                "objectives": [
                    {"id": "obj_reach_den_comp", "type": "reach_location", "location_name": "[BEAST_DEN_NAME]", "note": "Journey to the beast den."}, # [BEAST_DEN_NAME] to be resolved
                    {"id": "obj_kill_beasts_comp", "type": "kill", "target_name": "wolf", "target_id": "wolf_packleader_ID", "count": 3, "note": "Eliminate the beasts within the den."},
                    {"id": "obj_collect_trophy_comp", "type": "collect_item", "item_key": "beast_fang_trophy_companions", "count": 1, "note": "Collect a trophy as proof of your success."}
                ],
                "on_completion_dialogue": "The den is clear. The beasts are no more. Return to Jorrvaskr with your trophy.",
                "reward_modifier": {"reputation_companions_bonus": 10, "gold_bonus": 80, "item_bonus": "skyforge_steel_sword"}, # Companions specific reward
                "final_stage": True
            }
        ]
    }
    # Add more Whiterun specific quests here
]