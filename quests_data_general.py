# quests_data_general.py

GENERAL_QUEST_TEMPLATES = [
    {
        "id": "clear_bandit_camp",
        "title_template": "The Shadowed Road: Clearing [LOCATION_NAME]",
        "desc_template": "A vile band of cutthroats has established a menacing camp near **[LOCATION_NAME]**, choking the life out of trade routes and terrorizing honest travelers. The local populace lives in fear. You must venture forth, eliminate their ruthless leader, and scatter their ranks to restore peace to these lands.",
        "lore_tags": ["bandits", "road_safety", "road_danger", "wilderness_threat"],
        "location_tags_required": ["camp", "bandit", "ruin", "wilderness"], # Generic tags, can fit many places
        "level_range": (1, 5),
        "flavor_tags": {"quest": {"type": ["hunt", "clear", "protection"], "difficulty": ["easy", "medium"], "moral": ["ethical", "just"]}},
        "turn_in_role_hint": ["guard", "merchant", "jarl", "caravan_master"], # NPC role to turn quest into
        "stages": [
            {
                "stage_name": "Reclaim the Road",
                "objectives": [
                    {"id": "obj_bandit_leader", "type": "kill", "target_name": "bandit leader", "target_id": "bandit_leader_ID", "count": 1, "note": "Silence the **bandit leader**, the architect of this misery."},
                    {"id": "obj_bandit_thugs", "type": "kill", "target_name": "bandit thug", "target_id": "bandit_thug_ID", "count": 3, "note": "Cull the remaining **bandit thugs** to break their stranglehold."},
                    {"id": "obj_bandit_missive_optional", "type": "optional", "objective": {"id": "opt_obj_missive", "type": "collect_item", "item_key": "bandit_missive", "count": 1, "note": " (Optional) Seek out any incriminating **documents or hidden plans** among their belongings. Who truly backs these ruffians?"}},
                    {"id": "obj_stormcloak_connection_optional", "type": "optional", "objective": {"id": "opt_obj_stormcloak", "type": "collect_item", "item_key": "stormcloak_orders", "count": 1, "note": " (Optional) Look for evidence of the bandits' connection to the Stormcloaks."}}
                ],
                "on_completion_dialogue": "The air in the camp is still, save for the whisper of the wind. The road to [LOCATION_NAME] is clear. You should carry word of your success to [QUEST_GIVER_NAME]; they await news anxiously.",
                "branch_options": []
            }
        ]
    },
    {
        "id": "wolf_infestation",
        "title_template": "The Howling Scourge of [FARM_NAME]",
        "desc_template": "A terrifying infestation of bloodthirsty wolves has descended upon **[FARM_NAME]**, a solitary homestead nestled near **[LOCATION_NAME]**. Their relentless attacks have decimated livestock and instilled terror in the farmer's heart. You must aid them in protecting their remaining animals and eradicate this savage threat from the wilds.",
        "lore_tags": ["wolves", "farm", "protection", "rural_life", "wilderness_danger", "survival"],
        "location_tags_required": ["farm", "rural", "village"],
        "level_range": (2, 6),
        "flavor_tags": {"quest": {"type": ["hunt", "defend", "aid"], "moral": ["ethical", "compassionate"], "urgency": ["important", "immediate"]}},
        "turn_in_role_hint": ["farmer", "villager", "steward"],
        "stages": [
            {
                "stage_name": "Silence the Predator's Call",
                "objectives": [
                    {"id": "obj_kill_wolves", "type": "kill", "target_name": "wolf", "target_id": "wolf_alpha_ID", "count": 5, "note": "Silence the **howling pack** that plagues the farm. Fewer wolves mean safer herds."},
                    {"id": "obj_protect_livestock", "type": "protect", "object": "livestock", "count": 2, "note": "Stand guard and **ensure the safety of the farmer's precious livestock**. Be ready; the wolves may strike again."} # This objective might require a trigger from game logic
                ],
                "on_completion_dialogue": "The sounds of the pack have faded into the quiet wilderness. The immediate threat to the farm is lifted, and a relieved sigh escapes the farmer. Report your success to [QUEST_GIVER_NAME].",
                "branch_options": []
            },
            {
                "stage_name": "Optional: A Stronger Defense",
                "objectives": [
                    {"id": "obj_craft_wolf_traps_optional", "type": "optional", "objective": {"id": "opt_obj_traps", "type": "craft", "item_key": "wolf_trap", "count": 3, "note": " (Optional) Forge and strategically place **wolf traps** around the farm's perimeter to deter future attacks. This requires a keen eye and skill in smithing or woodcutting."}}
                ],
                "on_completion_dialogue": "With the traps expertly set, the farmer expresses profound gratitude. This extra measure of security brings them true peace of mind. Your foresight and dedication will not be forgotten.",
                "reward_modifier": {"reputation_local_bonus": 5, "gold_bonus": 50}, # Specific reputation gain
                "optional_completion_stage": True # Indicate this stage is optional for overall quest completion
            }
        ]
    },
    {
        "id": "the_missing_farmer",
        "title_template": "The Empty Plow: The Missing Farmer of [FARM_NAME]",
        "desc_template": "Panic grips the humble homestead of **[FARM_NAME]**. Old Man Theron (or a similar placeholder), a beloved farmer, has vanished without a trace after venturing into the perilous **[WILDERNESS_TYPE]** to gather essential supplies. His worried family fears the worst. You are implored to track his path, discover his fate, and ensure his safe return to his distraught kin.",
        "lore_tags": ["farmer", "missing_person", "wilderness", "rural_danger", "rescue", "humanitarian"],
        "location_tags_required": ["farm", "rural", "wilderness"],
        "level_range": (1, 6),
        "flavor_tags": {"quest": {"type": ["search", "rescue", "aid"], "moral": ["ethical", "compassionate"], "urgency": ["urgent", "desperate"]}},
        "turn_in_role_hint": ["farmer_spouse", "villager_elder", "local_guard"],
        "stages": [
            {
                "stage_name": "Search the Wilderness",
                "objectives": [
                    {"id": "obj_search_area_farmer", "type": "investigate", "location_name": "[WILDERNESS_TYPE]", "note": "Search the specified wilderness area for signs of the missing farmer (Survival check DC 10)."},
                    {"id": "obj_find_clue_farmer", "type": "collect_item", "item_key": "torn_clothing_fragment", "count": 1, "note": "Find a clue indicating the farmer's direction or what happened."}
                ],
                "on_completion_dialogue": "You've found a chilling trail. It seems the farmer was dragged away into a dark, nearby **[CAVE_TYPE]**! His fate hangs in the balance.",
                "branch_options": []
            },
            {
                "stage_name": "A Desperate Rescue",
                "objectives": [
                    {"id": "obj_reach_lair_farmer", "type": "reach_location", "location_name": "[CAVE_TYPE]", "note": "Brave the gloom and enter the **[CAVE_TYPE]** where the farmer was taken captive. Prepare for a confrontation."},
                    {"id": "obj_kill_captor_farmer", "type": "kill", "target_name": "bandit", "target_id": "bandit_thug_ID", "count": 2, "note": "Overwhelm and **defeat the vile captors** holding the innocent farmer hostage."},
                    {"id": "obj_talk_to_farmer_rescue", "type": "talk_to_npc", "npc_id": "missing_farmer_ID", "note": "Speak to the **rescued farmer** to ensure he is safe and uninjured."}
                ],
                "on_completion_dialogue": "The farmer, though shaken and bruised, is safe thanks to your swift intervention. A wave of immense relief washes over him. Now, escort him back to the warmth and safety of his home.",
                "reward_modifier": {"reputation_local_bonus": 10, "gold_bonus": 75},
                "final_stage": True
            }
        ]
    },
    {
        "id": "the_plague_of_rats",
        "title_template": "The Gnawing Menace: Plague of [CITY_NAME] Sewers",
        "desc_template": "A grotesque **swarm of giant rats** has erupted from the putrid depths of the sewers, infesting the lower districts of **[CITY_NAME]**. Their relentless scuttling spreads disease, gnaws through provisions, and sows chaos among the terrified populace. You are needed to descend into the festering darkness, eliminate the heart of this infestation, and cleanse the city of this vile plague.",
        "lore_tags": ["city", "plague", "pest_control", "sewers", "disease", "urban_threat", "sanitation"],
        "location_tags_required": ["city", "sewers", "underground"],
        "level_range": (3, 7),
        "flavor_tags": {"quest": {"type": ["hunt", "clear", "cleansing"], "moral": ["ethical", "public_service"], "urgency": ["urgent", "spreading_threat"]}},
        "turn_in_role_hint": ["guard_captain", "city_official", "healer", "head_of_sanitation"],
        "stages": [
            {
                "stage_name": "Into the Stench",
                "objectives": [
                    {"id": "obj_reach_sewers_rats", "type": "reach_location", "location_name": "[CITY_NAME] Sewers", "note": "Brave the foul air and dripping darkness to **venture into the infested sewers** beneath [CITY_NAME]. The source of the plague awaits."}
                ],
                "on_completion_dialogue": "The stench of decay and vermin assaults your senses. You've found their gnawing, squealing lair. The true horror of the infestation reveals itself.",
                "branch_options": []
            },
            {
                "stage_name": "Cleansing the Underbelly",
                "objectives": [
                    {"id": "obj_kill_rats_city", "type": "kill", "target_name": "giant rat", "target_id": "giant_rat_ID", "count": 20, "note": "Relentlessly **cull the swarming population of giant rats**. Leave no corner untouched."},
                    {"id": "obj_destroy_nests_rats", "type": "destroy", "object": "rat_nest", "count": 5, "note": "Locate and **destroy the vile rat nests** to prevent further breeding and resurgence of the plague."},
                    {"id": "obj_collect_poison_optional_rats", "type": "optional", "objective": {"id": "opt_obj_poison", "type": "collect_item", "item_key": "rat_poison_ingredients", "count": 3, "note": " (Optional) Gather specific, noxious herbs and fungi to **create a stronger rat poison**, ensuring their complete eradication. (Requires Alchemy check)."}}
                ],
                "on_completion_dialogue": "The horrifying squealing has ceased, replaced by an unsettling quiet. The sewers are largely clear, their foul occupants reduced to lifeless piles. You have done the city a great service. Return to [QUEST_GIVER_NAME].",
                "reward_modifier": {"gold_bonus": 100, "experience_bonus": 50, "reputation_local_bonus": 10},
                "final_stage": True
            }
        ]
    },
    {
        "id": "assist_refugees",
        "title_template": "Aiding the Displaced: Helping Refugees near [LOCATION_NAME]",
        "desc_template": "A group of refugees, displaced by the ongoing war, has arrived near [LOCATION_NAME]. They are in desperate need of supplies and assistance. Provide them with food, water, and medical aid to ease their suffering.",
        "lore_tags": ["refugees", "war_refugees", "stormcloak_rebellion", "imperial_conflict", "humanitarian_aid"],
        "location_tags_required": ["roadside", "wilderness", "camp"],
        "level_range": (1, 5),
        "flavor_tags": {"quest": {"type": ["aid", "rescue", "support"], "moral": ["ethical", "compassionate"], "urgency": ["urgent"]}},
        "turn_in_role_hint": ["refugee_leader", "local_official", "priest"],
        "stages": [
            {
                "stage_name": "Provide Aid",
                "objectives": [
                    {"id": "obj_give_food", "type": "collect_item", "item_key": "food_rations", "count": 5, "note": "Provide the refugees with food rations."},
                    {"id": "obj_give_water", "type": "collect_item", "item_key": "water_skins", "count": 3, "note": "Provide the refugees with water skins."},
                    {"id": "obj_give_medicine", "type": "collect_item", "item_key": "healing_potion_minor", "count": 2, "note": "Provide medical aid to the sick and injured refugees."}
                ],
                "on_completion_dialogue": "The refugees are grateful for your assistance. Your kindness has brought them hope in these dark times.",
                "reward_modifier": {"gold_bonus": 50, "reputation_local_bonus": 5, "item_bonus": "scroll_minor_healing"},
                "final_stage": True
            }
        ]
    }
    # Add more general quests here if needed
]