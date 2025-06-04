# quests_data_the_reach.py
import random # For random choices in templates

THE_REACH_QUEST_TEMPLATES = [
    {
        "id": "reach_forsworn_conspiracy_markarth", # Specific ID
        "title_template": "The Forsworn Conspiracy: Markarth's Bloody Secret",
        "desc_template": "A seemingly simple brawl in Markarth's marketplace uncovers a deep-seated conspiracy involving the native Forsworn, the powerful Silver-Blood family, and a history of violence and oppression. You are drawn into a web of intrigue that could ignite the Reach.",
        "lore_tags": ["the_reach", "markarth_city", "forsworn_uprising", "silver_blood_family_corrupt", "political_intrigue_deep", "conspiracy_unravel", "cidnha_mine_prison"],
        "location_tags_required": ["markarth", "city_stone", "forsworn_presence_city", "silver_blood_influence_strong", "cidnha_mine"], # Markarth is central
        "level_range": (10, 18), # A more involved quest
        "flavor_tags": {"quest": {"type": ["investigate", "conspiracy", "political_drama"], "difficulty": ["hard", "complex"], "moral": ["gray_area_choices", "justice_ambiguous"]}},
        "turn_in_role_hint": ["forsworn_leader_madanoch", "thongvor_silver_blood", "jarl_igmund_markarth"], # Multiple potential outcomes/alliances
        "stages": [
            {
                "stage_name": "A Brawl and a Warning",
                "objectives": [
                    {"id": "obj_witness_brawl_markarth", "type": "event_trigger", "event_type": "markarth_market_brawl_start", "note": "Witness (or get involved in) a brawl in the Markarth marketplace that turns deadly."},
                    {"id": "obj_receive_note_eltrys_markarth", "type": "talk_to_npc", "npc_id": "eltrys_concerned_citizen_ID", "note": "Receive a mysterious note from Eltrys, urging you to investigate the recent killings."}
                ],
                "on_completion_dialogue": "Eltrys believes the killings are part of a larger Forsworn conspiracy. He asks you to gather evidence, starting by investigating Weylin, one of the brawlers.",
                "branch_options": []
            },
            {
                "stage_name": "Uncovering the Threads",
                "objectives": [
                    {"id": "obj_investigate_weylin_room_markarth", "type": "investigate", "location_name": "The Warrens (Weylin's Room)", "note": "Search Weylin's room in the Warrens for clues about his motives (Investigation DC 15)."},
                    {"id": "obj_question_margret_markarth", "type": "talk_to_npc", "npc_id": "margret_noblewoman_markarth_ID", "note": "Question Margret, another victim, about who might want her dead."},
                    {"id": "obj_find_nepos_journal_markarth", "type": "collect_item", "item_key": "nepos_the_nose_journal", "location_name": "Nepos's House", "count": 1, "note": "Find Nepos the Nose's journal, implicating him in the conspiracy."}
                ],
                "on_completion_dialogue": "The evidence mounts, pointing to a vast network involving key figures in Markarth. Eltrys urges you to confront Thonar Silver-Blood or Nepos directly. But the city guard, influenced by the Silver-Bloods, frames you for the murders!",
                "branch_options": [] # Leads to Cidhna Mine
            },
            {
                "stage_name": "Escape from Cidhna Mine",
                "objectives": [
                    {"id": "obj_get_arrested_markarth", "type": "event_trigger", "event_type": "player_arrested_markarth_conspiracy", "note": "You are arrested and thrown into Cidhna Mine, the notorious prison quarry."},
                    {"id": "obj_meet_madanoch_cidhna", "type": "talk_to_npc", "npc_id": "madanoch_king_in_rags_ID", "note": "Meet Madanach, the 'King in Rags,' leader of the Forsworn in Cidhna Mine."},
                    {"id": "obj_choose_escape_path_cidhna", "type": "choice", "options_text": ["Side with Madanach and escape with the Forsworn.", "Find your own way out, possibly betraying Madanach."], "note": "Decide how to escape Cidhna Mine: with Madanach or alone."}
                ],
                "on_completion_dialogue": "You've escaped Cidhna Mine! If you sided with Madanach, the Forsworn are now rampaging through Markarth. If you escaped alone, you have evidence against Thonar Silver-Blood. The city is in chaos.",
                "branch_options": [ # These represent the major outcomes
                    {"choice_id": "forsworn_rampage_markarth", "text": "The Forsworn are attacking Markarth!", "next_stage_index": 3, "consequences": {"forsworn_control_markarth_temporary": True}},
                    {"choice_id": "expose_silver_blood_markarth", "text": "You have evidence against Thonar Silver-Blood.", "next_stage_index": 4, "consequences": {"silver_blood_power_weakened": True}}
                ]
            },
            { # Stage 3: Forsworn Uprising
                "stage_name": "The Liberation of Markarth (Forsworn Path)",
                "objectives": [
                    {"id": "obj_aid_forsworn_markarth_battle", "type": "kill", "target_name": "Markarth City Guard", "target_id": "markarth_city_guard_ID", "count": 10, "note": "Aid Madanach and the Forsworn in their battle against the Markarth City Guard."},
                    {"id": "obj_confront_thonar_forsworn_path", "type": "kill", "target_name": "Thonar Silver-Blood", "target_id": "thonar_silver_blood_ID", "count": 1, "note": "Confront and eliminate Thonar Silver-Blood."}
                ],
                "on_completion_dialogue": "Markarth is (temporarily) under Forsworn control. Madanach grants you your freedom and a powerful Forsworn item. The future of the Reach is uncertain.",
                "reward_modifier": {"reputation_forsworn_bonus": 30, "reputation_markarth_city_penalty": -50, "item_bonus": "armor_of_the_old_gods_set", "gold_bonus": 500},
                "final_stage": True
            },
            { # Stage 4: Expose Silver-Blood (Player Alone Path)
                "stage_name": "Justice for Markarth (Independent Path)",
                "objectives": [
                    {"id": "obj_present_evidence_jarl_igmund_markarth", "type": "talk_to_npc", "npc_id": "jarl_igmund_markarth_ID", "note": "Present the evidence of Thonar's treachery to Jarl Igmund."},
                    {"id": "obj_witness_thonar_arrest_markarth", "type": "event_trigger", "event_type": "thonar_silver_blood_arrested", "note": "Witness the arrest of Thonar Silver-Blood."}
                ],
                "on_completion_dialogue": "Thonar Silver-Blood is brought to justice, his family's grip on Markarth weakened. The Jarl rewards you for your efforts in cleansing the city of corruption.",
                "reward_modifier": {"reputation_markarth_city_bonus": 25, "reputation_silver_blood_penalty": -30, "item_bonus": "silver_blood_family_ring_enchanted", "gold_bonus": 1000},
                "final_stage": True
            }
        ]
    },
    {
        "id": "reach_kolskeggr_mine_reclamation", # Specific ID
        "title_template": "The Gold of Kolskeggr: A Miner's Desperate Plea",
        "desc_template": "The rich **Kolskeggr Mine**, a source of valuable gold east of Markarth, lies abandoned. Fierce and relentless **Forsworn attacks** have driven off the miners, threatening the economic stability of the Reach. Pavo Attius, the mine foreman, seeks a brave soul to reclaim the mine, clear out the Forsworn, and restore the flow of precious gold.",
        "lore_tags": ["the_reach", "kolskeggr_mine", "mine_gold_rich", "forsworn_conflict_severe", "reclamation_economic", "combat_intense"],
        "location_tags_required": ["mine_gold_major", "forsworn_occupied_mine", "kolskeggr_mine"], # Kolskeggr Mine is key
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["clear", "reclaim", "economic_aid"], "difficulty": ["medium", "hard"], "moral": ["ethical_mercenary", "community_support"]}},
        "turn_in_role_hint": ["pavo_attius_mine_foreman", "markarth_jarl_steward_reach"],
        "stages": [
            {
                "stage_name": "A Vein of Trouble",
                "objectives": [
                    {"id": "obj_talk_to_pavo_attius_kolskeggr", "type": "talk_to_npc", "npc_id": "pavo_attius_kolskeggr_ID", "note": "Speak with **Pavo Attius**, the mine foreman (likely found in Markarth or a nearby inn), about the Forsworn infestation at Kolskeggr Mine."},
                    {"id": "obj_reach_kolskeggr_mine_reach", "type": "reach_location", "location_name": "Kolskeggr Mine", "note": "Travel to the deserted **Kolskeggr Mine**."},
                    {"id": "obj_clear_forsworn_exterior_kolskeggr", "type": "kill", "target_name": "Forsworn Pillager", "target_id": "forsworn_pillager_ID", "count": 5, "note": "Clear the **Forsworn encampment** outside the mine entrance."}
                ],
                "on_completion_dialogue": "The exterior of Kolskeggr is clear, but the mine's depths still echo with the shouts of Forsworn. The main threat is within.",
                "branch_options": []
            },
            {
                "stage_name": "Reclaiming the Gold",
                "objectives": [
                    {"id": "obj_clear_forsworn_interior_kolskeggr", "type": "kill", "target_name": "Forsworn Ravager", "target_id": "forsworn_ravager_ID", "count": 7, "note": "Clear the remaining **Forsworn** from deep within Kolskeggr Mine."},
                    {"id": "obj_defeat_forsworn_leader_kolskeggr", "type": "kill", "target_name": "Forsworn Briarheart (Mine Boss)", "target_id": "forsworn_briarheart_kolskeggr_ID", "count": 1, "note": "Defeat the **Forsworn leader** guarding the richest veins."},
                    {"id": "obj_secure_mine_entrance_kolskeggr", "type": "event_trigger", "event_type": "kolskeggr_mine_secured_signal", "note": "Signal that the mine is secure (e.g., light a beacon, report to a waiting miner)."}
                ],
                "on_completion_dialogue": "Kolskeggr Mine is now free of the Forsworn menace! The gold once again awaits the miners. Return to [QUEST_GIVER_NAME] with the good news.",
                "reward_modifier": {"gold_bonus": 750, "experience_bonus": 120, "reputation_markarth_miners_bonus": 10, "reputation_markarth_jarl_bonus": 5, "item_bonus": "gold_ingot_pile"}, # More gold focused reward
                "final_stage": True
            }
        ]
    },
    {
        "id": "reach_orc_stronghold_aid_dushnikh_yal", # Specific ID
        "title_template": "The Forgemaster's Fingers: Aid to Dushnikh Yal",
        "desc_template": "The mighty **Orc stronghold of Dushnikh Yal**, usually a bastion of strength and tradition, requires a rare set of tongs, the Forgemaster's Fingers, to complete a tribute to Malacath. Their current smith, Gharol, is too old to retrieve them from a dangerous giant's camp. Prove your mettle, earn their respect, and aid the Orcs in their sacred task.",
        "lore_tags": ["the_reach", "orc_stronghold_dushnikh_yal", "malacath_worship_ritual", "giant_threat_camp", "aid_tribal", "honor_orcish", "warrior_culture_test", "forgemasters_fingers"],
        "location_tags_required": ["orc_stronghold", "malacath_shrine_active", "dushnikh_yal", "giant_camp_nearby"], # Dushnikh Yal and a nearby giant camp
        "level_range": (9, 14),
        "flavor_tags": {"quest": {"type": ["fetch_dangerous", "aid_tribal", "combat_giant"], "difficulty": ["medium", "hard"], "moral": ["ethical_respect", "honor_bound"]}},
        "turn_in_role_hint": ["gharol_orc_smith_dushnikh", "chief_burguk_dushnikh_yal"],
        "stages": [
            {
                "stage_name": "A Chieftain's Request",
                "objectives": [
                    {"id": "obj_talk_to_gharol_dushnikh", "type": "talk_to_npc", "npc_id": "gharol_orc_smith_dushnikh_yal_ID", "note": "Speak with **Gharol**, the smith of Dushnikh Yal, about the Forgemaster's Fingers."},
                    {"id": "obj_learn_location_giants_camp_dushnikh", "type": "investigate", "location_name": "Dushnikh Yal surroundings", "note": "Learn the location of the **giant's camp** where the tongs were lost (from Gharol or other Orcs)."}
                ],
                "on_completion_dialogue": "Gharol explains the importance of the Forgemaster's Fingers for their tribute to Malacath. The giants at [GIANT_CAMP_NAME] have them. You must retrieve them.",
                "branch_options": []
            },
            {
                "stage_name": "Retrieve the Forgemaster's Fingers",
                "objectives": [
                    {"id": "obj_reach_giants_camp_dushnikh", "type": "reach_location", "location_name": "[GIANT_CAMP_NAME]", "note": "Journey to the designated **giant's camp**."}, # [GIANT_CAMP_NAME] to be resolved
                    {"id": "obj_defeat_giants_dushnikh", "type": "kill", "target_name": "Giant", "target_id": "giant_camp_guardian_ID", "count": 2, "note": "Defeat the **giants** guarding the camp."},
                    {"id": "obj_collect_forgemasters_fingers", "type": "collect_item", "item_key": "forgemasters_fingers_tongs", "count": 1, "note": "Retrieve the **Forgemaster's Fingers** from the giant's stash."}
                ],
                "on_completion_dialogue": "The Forgemaster's Fingers are recovered! The giants are dealt with. You've earned the respect of Dushnikh Yal. Return to [QUEST_GIVER_NAME]. Your actions speak louder than words in this stronghold.",
                "reward_modifier": {"reputation_orc_strongholds_bonus": 18, "gold_bonus": 280, "experience_bonus": 140, "item_bonus": "orcish_armor_improved_set_piece"},
                "final_stage": True
            }
        ]
    }
    # Add more Reach specific quests here
]