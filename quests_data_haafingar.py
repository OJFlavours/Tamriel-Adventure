# quests_data_haafingar.py

HAAFINGAR_QUEST_TEMPLATES = [
    {
        "id": "haafingar_solitude_bards_college_join", # Specific ID
        "title_template": "Tending the Flames: Joining the Bards College",
        "desc_template": "The esteemed **Bards College in Solitude**, the heart of Skyrim's musical and historical tradition, is always seeking new talent. Viarmo, the headmaster, needs help with the annual festival, specifically by recovering King Olaf's Verse. Join their ranks, contribute to their legacy, and perhaps even uncover ancient secrets through song and story.",
        "lore_tags": ["haafingar", "solitude_city", "bards_college_active_join", "music_lore_tradition", "performance_festival", "recruitment_academic", "cultural_institution_skyrim", "historic_preservation_olaf"],
        "location_tags_required": ["solitude", "bards_college", "festival_event_potential"], # Solitude and Bards College are key
        "level_range": (1, 6), # Accessible early
        "flavor_tags": {"quest": {"type": ["social_faction", "performance_skill", "knowledge_retrieval"], "difficulty": ["easy", "medium_social"], "moral": ["ethical_artistic", "cultural_duty"]}},
        "turn_in_role_hint": ["viarmo_bards_college_headmaster", "giraud_gemane_bards_college_lore"], # Viarmo is primary
        "stages": [
            {
                "stage_name": "An Audition of Talent (and a Task)",
                "objectives": [
                    {"id": "obj_reach_bards_college_solitude_haaf", "type": "reach_location", "location_name": "Bards College (Solitude)", "note": "Travel to the grand **Bards College** in Solitude."},
                    {"id": "obj_talk_to_viarmo_bards_college_haaf", "type": "talk_to_npc", "npc_id": "viarmo_bards_college_headmaster_ID", "note": "Speak with **Viarmo**, the Headmaster of the Bards College, about joining."},
                    {"id": "obj_agree_to_find_olafs_verse_haaf", "type": "event_trigger", "event_type": "bards_college_accept_olafs_verse_task", "note": "Agree to Viarmo's request to find the lost King Olaf's Verse for the Burning of King Olaf festival."}
                ],
                "on_completion_dialogue": "Viarmo is pleased with your willingness. He directs you to Dead Men's Respite, a dangerous barrow where the verse is rumored to be found. Your true test begins.",
                "branch_options": []
            },
            {
                "stage_name": "Dead Men's Respite: The Lost Verse",
                "objectives": [
                    {"id": "obj_reach_dead_mens_respite_haaf", "type": "reach_location", "location_name": "Dead Men's Respite", "note": "Journey to **Dead Men's Respite**, an ancient Nordic barrow."},
                    {"id": "obj_find_king_olafs_verse_haaf", "type": "collect_item", "item_key": "king_olafs_verse_lost", "count": 1, "note": "Navigate the barrow and find **King Olaf's Verse**."},
                    {"id": "obj_defeat_guardian_olafs_verse_optional_haaf", "type": "optional", "objective": {"id": "opt_obj_olaf_guardian", "type": "kill", "target_name": "Draugr Wight Lord (Guardian)", "target_id": "draugr_wight_lord_verse_guardian_ID", "count": 1, "note": " (Optional) Defeat the ancient guardian protecting the verse."}}
                ],
                "on_completion_dialogue": "You've found King Olaf's Verse! The ancient script is faded but legible. Return to Viarmo at the Bards College with your prize.",
                "reward_modifier": {"experience_bonus": 100}, # Partial reward for finding verse
                "final_stage": False # Leads to reconstructing the verse
            },
            {
                "stage_name": "Reconstructing the Masterpiece",
                "objectives": [
                    {"id": "obj_return_verse_to_viarmo_haaf", "type": "talk_to_npc", "npc_id": "viarmo_bards_college_headmaster_ID", "note": "Return King Olaf's Verse to Viarmo."},
                    {"id": "obj_help_viarmo_reconstruct_verse_haaf", "type": "skill_check", "skill": "speech", "dc": 12, "note": "Help Viarmo reconstruct the verse, making choices about its content (Persuasion/Deception options available)."}
                ],
                "on_completion_dialogue": "The verse is reconstructed! Viarmo is delighted and will present it to Jarl Elisif. You are officially welcomed into the Bards College.",
                "reward_modifier": {"reputation_bards_college_member_bonus": 25, "gold_bonus": 250, "experience_bonus": 150, "item_bonus": "bards_college_tunic_fine"},
                "final_stage": True
            }
        ]
    },
    {
        "id": "haafingar_solitude_thalmor_headquarters_incident", # Specific ID
        "title_template": "The Thalmor's Shadow: Whispers from the Embassy",
        "desc_template": "A concerned citizen (or a disgruntled Imperial soldier) in Solitude whispers of suspicious activities at the **Thalmor Embassy**. They believe the Thalmor are overstepping their bounds, possibly imprisoning Talos worshippers or plotting against Skyrim's interests. Infiltrate the heavily guarded Embassy, gather intelligence, and expose their schemes if possible. This is a high-risk espionage mission.",
        "lore_tags": ["haafingar", "solitude_city", "thalmor_embassy_solitude", "espionage_infiltration", "political_intrigue_thalmor", "talos_worship_secret", "imperial_thalmor_tension", "high_risk_stealth"],
        "location_tags_required": ["solitude", "thalmor_embassy", "imperial_capital_city", "high_security_area"], # Thalmor Embassy is key
        "level_range": (10, 18), # A challenging infiltration quest
        "flavor_tags": {"quest": {"type": ["espionage", "infiltration_stealth", "political_intrigue_faction"], "difficulty": ["very_hard_stealth"], "moral": ["gray_area_justice", "anti_thalmor_resistance"]}},
        "turn_in_role_hint": ["general_tullius_imperial_solitude", "blade_contact_skyrim", "stormcloak_sympathizer_solitude"], # Depends on player's allegiance or goals
        "stages": [
            {
                "stage_name": "The Invitation (or a Diversion)",
                "objectives": [
                    {"id": "obj_gain_access_thalmor_embassy_haaf", "type": "event_trigger", "event_type": "thalmor_embassy_access_method", "note": "Find a way to gain access to the Thalmor Embassy (e.g., forge an invitation, create a diversion during a party, sneak in)."}
                    # This objective is intentionally vague to allow for multiple solutions by the game's event system or player creativity.
                ],
                "on_completion_dialogue": "You've managed to get inside the Thalmor Embassy. The air is thick with arrogance and suspicion. Now, find the evidence.",
                "branch_options": []
            },
            {
                "stage_name": "Gathering Intelligence",
                "objectives": [
                    {"id": "obj_search_thalmor_embassy_dossiers_haaf", "type": "collect_item", "item_key": "thalmor_intelligence_dossier_skyrim", "count": 1, "location_name": "Thalmor Embassy (Commander's Office/Interrogation Chamber)", "note": "Search the Embassy for incriminating **dossiers, prisoner lists, or strategic plans** (requires high Sneak, Lockpicking, or finding keys)."},
                    {"id": "obj_rescue_prisoner_optional_thalmor_embassy_haaf", "type": "optional", "objective": {"id": "opt_obj_rescue_thalmor_prisoner", "type": "rescue", "npc_id": "thalmor_embassy_prisoner_ID", "note": " (Optional) Locate and **rescue a prisoner** being held by the Thalmor (e.g., a Blade agent, a Talos worshipper)."}}
                ],
                "on_completion_dialogue": "You've found damning evidence of the Thalmor's activities. If you rescued a prisoner, they thank you profusely. Now, escape the Embassy before you're discovered.",
                "branch_options": []
            },
            {
                "stage_name": "Escape and Report",
                "objectives": [
                    {"id": "obj_escape_thalmor_embassy_haaf", "type": "reach_location", "location_name": "Solitude (Safe Location outside Embassy)", "note": "Escape the Thalmor Embassy with the intelligence."},
                    {"id": "obj_report_findings_thalmor_embassy_haaf", "type": "talk_to_npc", "npc_id": "[QUEST_GIVER_ID]", "note": "Report your findings to your contact ([QUEST_GIVER_NAME])."}
                ],
                "on_completion_dialogue": "You've successfully exposed (or at least gathered intelligence on) the Thalmor's operations. Your actions will have repercussions. [QUEST_GIVER_NAME] is grateful for your bravery.",
                "reward_modifier": {"gold_bonus": 1500, "experience_bonus": 300, "reputation_chosen_faction_bonus": 20, "reputation_thalmor_penalty": -30, "item_bonus": "elven_dagger_enchanted_soul_trap"}, # Faction rep depends on who the quest giver is
                "final_stage": True
            }
        ]
    },
    {
        "id": "haafingar_solitude_east_empire_company_warehouse", # Specific ID
        "title_template": "The Restless East Empire: Solitude Warehouse Woes",
        "desc_template": "The prestigious **East Empire Company** faces mounting troubles at its **Solitude Docks warehouse**. Goods are vanishing, manifests are tampered with, and their agents suspect sabotage by pirates or a rival company. Investigate the disruptions, uncover the source of their woes, and restore security to their vital Solitude operations.",
        "lore_tags": ["haafingar", "solitude_city", "east_empire_company_solitude", "trade_dispute_piracy", "sabotage_warehouse", "investigation_economic", "maritime_commerce_security"],
        "location_tags_required": ["solitude", "docks_major_port", "east_empire_company_warehouse", "warehouse_large"], # EEC Warehouse in Solitude is key
        "level_range": (7, 12),
        "flavor_tags": {"quest": {"type": ["investigate", "economic_security", "intrigue_corporate"], "difficulty": ["medium_investigation"], "moral": ["gray_area_business", "mercenary_work"]}},
        "turn_in_role_hint": ["vittoria_vici_east_empire_solitude", "solitude_guard_captain_docks", "east_empire_company_official"], # Vittoria Vici or similar EEC contact
        "stages": [
            {
                "stage_name": "A Tangled Web of Trade",
                "objectives": [
                    {"id": "obj_talk_to_eec_agent_solitude_haaf", "type": "talk_to_npc", "npc_id": "vittoria_vici_ID", "note": "Speak with the **East Empire Company representative** (e.g., Vittoria Vici) at the Solitude Docks office/warehouse about their troubles."},
                    {"id": "obj_investigate_eec_warehouse_solitude_haaf", "type": "investigate", "location_name": "East Empire Company Warehouse (Solitude)", "note": "Investigate the **EEC Warehouse**, looking for suspicious activity, hidden caches, or disgruntled workers (requires Perception or Sneak check DC 13)."},
                    {"id": "obj_find_pirate_note_optional_eec_haaf", "type": "optional", "objective": {"id": "opt_obj_pirate_note_eec", "type": "collect_item", "item_key": "pirate_coded_message_eec", "count": 1, "note": " (Optional) Find a **coded note** hinting at a pirate smuggling operation or a rival's involvement."}}
                ],
                "on_completion_dialogue": "Your investigation reveals a pattern of subtle sabotage and pilfering, orchestrated by a band of pirates, the Blood Horkers, using a hidden sea cave near Solitude, **Brinewater Grotto**, as their base.",
                "branch_options": []
            },
            {
                "stage_name": "Unmasking the Saboteurs: Brinewater Grotto",
                "objectives": [
                    {"id": "obj_reach_brinewater_grotto_eec_haaf", "type": "reach_location", "location_name": "Brinewater Grotto", "note": "Infiltrate **Brinewater Grotto**, the coastal cave hideout of the Blood Horker pirates."},
                    {"id": "obj_defeat_blood_horkers_eec_haaf", "type": "kill", "target_name": "Blood Horker Pirate", "target_id": "blood_horker_pirate_ID", "count": 5, "note": "Neutralize the **Blood Horker pirates** responsible for the disruptions."},
                    {"id": "obj_retrieve_stolen_eec_manifest_haaf", "type": "collect_item", "item_key": "stolen_eec_shipment_manifest", "count": 1, "note": "Retrieve the **stolen East Empire Company shipment manifest** as proof of their crimes."}
                ],
                "on_completion_dialogue": "The Blood Horker pirates are dealt with, and the East Empire Company's troubles should cease. You have restored order to the Solitude docks. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 800, "experience_bonus": 100, "reputation_east_empire_company_bonus": 15, "reputation_solitude_guards_bonus": 5, "item_bonus": "east_empire_pendant_valuable"},
                "final_stage": True
            }
        ]
    }
    # Add more Haafingar/Solitude specific quests here
]