# event_data.py
from locations import LocationManager
from typing import List, Dict

# --- DYNAMICALLY GENERATED DUNGEON_NAMES (from your provided code) ---
def get_all_dungeon_style_locations(locations_data: List):
    dungeon_names = set()
    def find_dungeons_recursive(location_list):
        for loc in location_list:
            loc_tags = loc.tags if hasattr(loc, 'tags') else loc.get("tags", [])
            is_settlement = "city" in loc_tags or "town" in loc_tags or "village" in loc_tags or "hold" in loc_tags
            is_dungeon_type = "dungeon" in loc_tags or \
                              "dwemer" in loc_tags or \
                              "barrow" in loc_tags or \
                              ("ruin" in loc_tags and not is_settlement) or \
                              ("cave" in loc_tags and not is_settlement) or \
                              (("mine" in loc_tags and not is_settlement) and ("abandoned" in loc_tags or "infested" in loc_tags or "haunted" in loc_tags))

            if is_dungeon_type:
                dungeon_names.add(loc.name if hasattr(loc, 'name') else loc["name"])

            if hasattr(loc, 'sub_locations') and loc.sub_locations:
                sub_locations = [location_manager.get_location(sub_id) for sub_id in loc.sub_locations]
                find_dungeons_recursive(sub_locations)
            #elif "sub_locations" in loc: # Removed this line
            #    find_dungeons_recursive(loc["sub_locations"])
    find_dungeons_recursive(locations_data)
    return list(dungeon_names)

location_manager = LocationManager()
DUNGEON_NAMES = get_all_dungeon_style_locations(location_manager.locations.values())
if not DUNGEON_NAMES: # Fallback (from original)
    DUNGEON_NAMES = [
        "Bleak Falls Barrow", "Quicksilver Mine", "Nightcaller Temple", "Iron-Breaker Mine",
        "Saarthal", "Hob's Fall Cave", "Yngol Barrow", "Movarth's Lair", "Ustengrav",
        "Pinewatch", "Halldir's Cairn", "Cidhna Mine", "Druadach Redoubt", "Shroud Hearth Barrow",
        "Wolfskull Cave", "Lost Prospect Mine", "The Ratway", "Labyrinthian", "Dustman's Cairn",
        "Alftand", "Mzinchaleft", "Forelhost", "Silent Moons Camp", "Reachwind Eyrie", "Blind Cliff Cave"
    ]

# --- Define SPECIFIC_LOCATION_TAGS (from your original code) ---
SPECIFIC_LOCATION_TAGS = [
    "tavern", "inn", "market", "mine", "camp", "cave", "ruin", "barrow", "dwemer",
    "keep", "meadhall", "blacksmith", "alchemy_shop", "temple", "college", "palace",
    "meadery", "brewery", "watchtower", "lighthouse", "wreck", "shop", "port",
    "government", "guild", "prison", "graveyard", "sanctuary", "monastery",
    "fort", "fortified", "city", "town", "village", "dragon_lair_ancient",
    "enchanted_forest", "cursed_swamp", "volcanic_caldera", "glacial_cave", "ashland_waste"
]

# --- EXPANDED AND REFINED RANDOM_EVENTS (4E 200 LORE APPLIED) ---
RANDOM_EVENTS = {
    "generic_travel": [
        {
            "description": "You spot a weathered Shrine of Akatosh by the roadside, its eternal flame flickering valiantly. You feel a sense of timelessness and renewed purpose upon offering a brief prayer.",
            "type": "flavor_and_buff",
            "location_tags": ["roadside", "wilderness", "plains", "mountain_pass"], # More specific where it can appear
            "context_tags": ["exterior"], # Must be outside
            "details": {
                "god_mention": "Akatosh",
                "minor_buff_debuff": {"stat": "magicka_regen_rate", "amount": 0.1, "duration_turns": 180, "is_buff": True, "buff_name": "Akatosh's Endurance"}
            }
        },
        {
            "description": "A rickety cart has broken an axle. Its merchant owner, a weary Dunmer named Drevis, sighs. 'Azura's curse! My shipment of ash yams for Windhelm's Gray Quarter will spoil if I don't get this fixed!'",
            "type": "npc_interaction_and_quest_lead",
            "details": {
                "npc_spawn_info": {"name": "Drevis", "race": "dunmer", "role": "merchant", "level": 3, "disposition": 60, "unique_id": "drevis_dunmer_merchant"},
                "dialogue_lead": "'Stendarr's Mercy, can anyone assist a humble merchant? I have coin, and perhaps some rare goods from Morrowind for your trouble.'",
                "quest_hint_template_id": "escort_merchant_or_repair_cart", # Point to a quest template
                "related_tags": ["merchant", "dunmer_refugee", "ash_yams", "roadside_assistance"]
            }
        },
        {
            "description": "You find a hastily written, bloodstained note clutched in the hand of a dead Imperial courier. It speaks of rising tensions and a planned attack by 'Nord patriots' on a strategic bridge near [DynamicNearbyLandmark - e.g., Dragon Bridge].",
            "type": "quest_lead_and_item",
            "details": {
                "item_key": "imperial_dispatch_sealed_bloodied",
                "quest_hint_template_id": "imperial_courier_dispatch", # Point to a quest template
                "related_tags": ["political_unrest", "nord_dissidents", "imperial_courier", "ambush_warning"],
                "moral_choice_hint": "Inform Imperials, warn dissidents, or use information for personal gain."
            }
        },
        {
            "description": "A group of stern-faced Vigilants of Stendarr are interrogating a frightened Khajiit traveler on the road. Their leader, a zealous Breton, eyes you suspiciously. 'Unless you bear witness to Daedric corruption, move along. Stendarr's light has no time for idle gawkers!'",
            "type": "npc_interaction_choice",
            "details": {
                "npc_spawn_info": {"name": None, "race": "breton", "role": "vigilant_of_stendarr_leader", "level": 8, "disposition": 40, "unique_id": "vigilant_leader_event_ID"},
                "secondary_npc_spawn_info": {"name": None, "race": "khajiit", "role": "traveler", "level": 4, "disposition": 70, "unique_id": "khajiit_traveler_event_ID"},
                "dialogue_lead": "", # Made empty to prevent the second quote
                "quest_hint_template_id": "thalmor_interrogation", # Link to the specific quest
                "related_tags": ["vigilants_of_stendarr", "khajiit_traveler", "religious_zealots", "daedra_hunting"],
            }
        },
        {
            "description": "A sudden, unnatural tremor shakes the ground violently! Loose rocks tumble from nearby cliffs, and the air fills with dust. You hear a faint, guttural roar from deep within the earth.",
            "type": "environmental_hazard_and_lore_hint",
            "details": {
                "hazard_type": "magical_earthquake_minor",
                "effect_desc": "The world shudders! You must keep your footing (Acrobatics DC 14) or risk minor injury (1d6 bludgeoning) from falling debris.",
                "lore_hint": "Such tremors are sometimes associated with ancient Dwemer machinery reactivating or the stirring of slumbering subterranean beasts.",
                "related_tags": ["earthquake", "dwemer_rumor", "monster_rumor", "skill_challenge_acrobatics"],
                "skill_challenge": {"skill":"agility", "dc":14, "success_desc":"You deftly keep your footing, avoiding the falling rocks.", "failure_desc":"You lose your balance and take 1d6 bludgeoning damage from falling debris."}
            }
        },
        {
            "description": "You encounter a Thalmor patrol on the road. Their Justiciar leader, with a chillingly polite demeanor, questions your travel and adherence to the White-Gold Concordat, specifically inquiring about any Talos worship.",
            "type": "npc_interaction_tense",
            "details": {
                "npc_spawn_info": {"name": None, "race":"altmer", "role":"thalmor_justiciar", "level": 10, "disposition": 30, "unique_id": "thalmor_justiciar_patrol_ID"},
                "secondary_npc_spawn_info": {"name": None, "race":"altmer", "role":"thalmor_soldier", "count": 2, "level": 8, "unique_id": "thalmor_soldier_patrol_ID"},
                "dialogue_lead": "'Citizen. We are ensuring compliance with the terms of the White-Gold Concordat. Have you witnessed any heresy regarding the false god Talos?'",
                "related_tags": ["thalmor_patrol", "white_gold_concordat", "talos_ban", "political_tension", "imperial_law"],
                "quest_hint_template_id": "thalmor_interrogation" # Link to the specific quest
            }
        },
        {
            "description": "A wandering scholar, hunched over a heavy tome, asks if you've seen any unusual ancient carvings or ruins nearby, unrelated to the Dwemer. They seem particularly interested in early Atmoran settlements.",
            "type": "npc_interaction_and_lore_reveal",
            "details": {
                "npc_spawn_info": {"name": "Historian Elmsworth", "race": "imperial", "role": "scholar", "level": 6, "disposition": 70, "unique_id": "historian_elmsworth_ID"},
                "dialogue_lead": "'Pardon me, traveler. My research into pre-Nordic Skyrim leads me to believe this region holds many secrets. Have you encountered any particularly ancient, non-Dwemer stonework?'",
                "lore_hint": "The scholar shares a snippet about the complexity of Atmoran migrations and their early interactions with Skyrim's native creatures and elves.",
                "related_tags": ["scholar", "atmora_lore", "ancient_history", "ruin_research"],
                "quest_lead_potential_simple": {"title": "Atmoran Remains", "description": "Find an ancient Atmoran ruin or artifact.", "turn_in_npc_id": "historian_elmsworth_ID"}
            }
        },
        {
            "description": "You encounter a group of weary refugees on the road, fleeing the war in Skyrim. They are in desperate need of food, water, and medical attention. They claim to have been displaced by the fighting between the Imperials and the Stormcloaks.",
            "type": "npc_interaction_and_quest_lead",
            "location_tags": ["roadside", "wilderness", "plains", "mountain_pass"],
            "context_tags": ["exterior"],
            "details": {
                "npc_spawn_info": {"name": "Refugee Leader", "race": "nord", "role": "refugee_leader", "level": 3, "disposition": 60, "unique_id": "refugee_leader_ID"},
                "secondary_npc_spawn_info": {"name": "Refugee", "race": "nord", "role": "refugee", "count": 4, "level": 1, "disposition": 70, "unique_id": "refugee_ID"},
                "dialogue_lead": "'Please, stranger, can you spare any food or water? We have been traveling for days and are in desperate need of assistance.'",
                "quest_hint_template_id": "assist_refugees",
                "related_tags": ["refugees", "war_refugees", "stormcloak_rebellion", "imperial_conflict", "humanitarian_aid"]
            }
        }
    ]
}