import random
from typing import List, Dict, Any
from locations import LOCATIONS # Assuming LOCATIONS is a list of location dicts
import tags # Assuming tags.py exists and is used by various classes
import flavor # Crucial for flavor text
# Assuming Item, generate_random_item, generate_item_from_key are in items.py
from items import Item, generate_random_item as gr_item_func, generate_item_from_key
from ui import UI # Ensure UI is imported for capitalization and other UI needs
from quests import Quest, find_locations_by_tag # Import the Quest class and find_locations_by_tag

# --- Constants ---
PROBABILITY_OF_QUEST_RUMOR = 0.20 # 20% chance an NPC offers a quest

# --- Existing Quest Rewards and Templates ---
QUEST_REWARDS_TEMPLATE = {
    "gold": {"min": 50, "max": 150},
    "experience": {"min": 25, "max": 75},
    "item_quality_levels": {
        (1, 5): ["common", "uncommon"],
        (6, 10): ["uncommon", "rare"],
        (11, 20): ["rare", "epic"],
        (21, 99): ["epic", "legendary"]
    },
    "reputation": {"min": 5, "max": 15},
    "favor": ["with local Jarl", "with merchant guild", "with College of Winterhold"]
}

QUEST_TEMPLATES = [
    {
        "id": "clear_bandit_camp_rumors",
        "title_template": "Clearing out [LOCATION_NAME]",
        "desc_template": "Bandits have taken over [LOCATION_NAME], causing trouble for anyone nearby. Someone needs to deal with their leader and thin their ranks.",
        "objectives_template": [
            {"id": "rb_kill_leader", "type": "kill", "target_name": "bandit leader", "target_id": "bandit_leader_generic", "count": 1, "note": "Defeat the bandit leader at [LOCATION_NAME]."},
            {"id": "rb_kill_thugs", "type": "kill", "target_name": "bandit thug", "target_id": "bandit_thug_generic", "count": 3, "note": "Eliminate ## bandit thugs in the vicinity of [LOCATION_NAME]."}
        ],
        "reward_tags": ["gold", "experience", "item"],
        "lore_tags": ["bandits", "road_safety", "local_threat"],
        "location_tags_required": ["camp", "bandit_camp", "ruin_occupied", "wilderness_outpost"], # Removed "tavern", "inn"
        "level_range": (1, 5),
        "flavor_tags": {"quest": {"type": ["hunt", "clear"], "difficulty": ["easy","medium"]}},
        "turn_in_role_hint": ["guard_captain", "jarl_steward", "local_merchant"]
    },
    {
        "id": "ancient_relic_retrieval_rumors",
        "title_template": "The Lost [ARTIFACT_NAME] of [RUIN_NAME]",
        "desc_template": "Legends speak of the [ARTIFACT_NAME], a relic of ancient power, lost within the depths of [RUIN_NAME]. Many have sought it, but the Draugr guardians are formidable. Perhaps a scholar at the College of Winterhold would reward its recovery.",
        "objectives_template": [
            {"id": "ar_reach_ruin", "type": "reach_location", "location_name": "[RUIN_NAME]", "note": "Journey to the ancient ruins of [RUIN_NAME]."},
            {"id": "ar_collect_item", "type": "collect_item", "item_key": "[ARTIFACT_KEY]", "count": 1, "note": "Find the legendary [ARTIFACT_NAME]."},
            {"id": "ar_kill_guardian", "type": "kill", "target_name": "draugr death overlord", "target_id": "draugr_death_overlord_generic", "count": 1, "note": "Defeat the guardian of the relic within [RUIN_NAME]."}
        ],
        "reward_tags": ["gold", "experience", "unique_spell_tome", "reputation_college"],
        "lore_tags": ["nordic_ruin", "ancient_artifact", "magic_relic", "college_of_winterhold_interest"],
        "location_tags_required": ["barrow", "dungeon", "undead_presence", "historic_site", "tavern", "inn", "social", "college"], # Broadened
        "level_range": (5, 10),
        "flavor_tags": {"quest": {"type": ["fetch", "investigate", "exploration"], "difficulty": ["medium", "hard"]}},
        "turn_in_role_hint": ["scholar_college", "court_mage_jarl", "antiquarian_collector"]
    },
    {
        "id": "missing_person_investigation_rumors",
        "title_template": "The Vanishing at [LOCAL_LANDMARK_NAME]",
        "desc_template": "Someone's gone missing near [LOCAL_LANDMARK_NAME]. Last seen heading towards the [WILDERNESS_TYPE]. Their family is worried sick. Might be worth looking into, could be beasts, could be bandits, could be something darker.",
        "objectives_template": [
            {"id": "mp_search_area", "type": "investigate", "location_name": "[LOCAL_LANDMARK_NAME]", "note": "Search the area around [LOCAL_LANDMARK_NAME] for clues."},
            {"id": "mp_follow_trail", "type": "track", "target_name": "missing person's trail", "note": "Follow any trail you find into the [WILDERNESS_TYPE]. (Survival DC 12)"},
            {"id": "mp_discover_fate", "type": "discover_fate", "target_name": "missing person", "note": "Determine what happened to the missing person."} # This would need game logic
        ],
        "reward_tags": ["gold", "reputation_local", "item_sentimental"],
        "lore_tags": ["missing_person", "local_mystery", "wilderness_danger"],
        "location_tags_required": ["village", "town", "farm", "inn", "tavern"],
        "level_range": (2, 7),
        "flavor_tags": {"quest": {"type": ["investigate", "rescue_potential", "search"], "difficulty": ["easy", "medium"]}},
        "turn_in_role_hint": ["family_member", "local_guard", "village_elder"]
    },
    {
        "id": "beast_hunt_rumors",
        "title_template": "The Terror of [FOREST_OR_MOUNTAIN_NAME]",
        "desc_template": "A fearsome [BEAST_TYPE] has been sighted near [FOREST_OR_MOUNTAIN_NAME], attacking livestock and travelers. The local Jarl, or perhaps just a worried farmer, is offering a bounty for its head.",
        "objectives_template": [
            {"id": "bh_track_beast", "type": "track", "target_name": "[BEAST_TYPE]", "location_name": "[FOREST_OR_MOUNTAIN_NAME]", "note": "Track the [BEAST_TYPE] in the wilds of [FOREST_OR_MOUNTAIN_NAME]. (Survival DC 13)"},
            {"id": "bh_slay_beast", "type": "kill", "target_name": "[BEAST_TYPE]", "target_id": "[BEAST_TYPE_ID]_alpha", "count": 1, "note": "Slay the monstrous [BEAST_TYPE]."}
        ],
        "reward_tags": ["gold", "experience", "beast_trophy"],
        "lore_tags": ["monster_hunt", "bounty", "local_danger_beast"],
        "location_tags_required": ["village", "town", "hunter_lodge", "tavern", "farm"],
        "level_range": (3, 8),
        "flavor_tags": {"quest": {"type": ["hunt", "bounty_clear"], "difficulty": ["medium"]}},
        "turn_in_role_hint": ["jarl_steward", "farmer_noble", "captain_of_guard"]
    }
]

# --- Helper Functions (Minor changes for robustness) ---
def _get_random_from_list(lst: List[Any]) -> Any:
    return random.choice(lst) if lst else None

def get_npc_name_by_role_hint(role_hint: str) -> Dict[str, str]:
    try:
        from npc import NAME_POOLS
        if role_hint in NAME_POOLS: # Check if role_hint itself is a direct key (for specific NPCs)
             race_data = NAME_POOLS[role_hint]
             name_type = next(iter(race_data)) # "noble" or "commoner"
             gender = next(iter(race_data[name_type])) # "male" or "female"
             name_pool_entry = race_data[name_type][gender]
        else:
            random_race = random.choice(list(NAME_POOLS.keys()))
            # Avoid trying to get names for non-character races if they aren't defined for commoners/nobles
            if random_race in ["undead_nord", "undead_skeleton", "spirit", "falmer", "dwemer_construct_race", "wolf_creature", "bear_creature", "spider_creature", "chaurus_creature"]:
                random_race = "nord" # Fallback to a common race

            random_gender = random.choice(["male", "female"])
            name_pool_entry = NAME_POOLS.get(random_race, {}).get("commoner", {}).get(random_gender, NAME_POOLS["nord"]["commoner"]["male"])
        
        if not name_pool_entry: # Further fallback
             name_pool_entry = NAME_POOLS["nord"]["commoner"]["male"]

        chosen_name_with_id = random.choice(name_pool_entry)
        name_display = chosen_name_with_id.split('_')[0].capitalize()
        return {"name": name_display, "id": chosen_name_with_id}
    except (ImportError, KeyError) as e: # Catch KeyError if NAME_POOLS structure is unexpected
        UI.print_warning(f"DEBUG: Error in get_npc_name_by_role_hint for '{role_hint}': {e}. Using fallback.")
        return {"name": role_hint.replace("_", " ").title(), "id": f"{role_hint}_{random.randint(1000,9999)}"}

def generate_reward(player_level: int, quest_tags: List[str]) -> Dict[str, Any]:
    reward: Dict[str, Any] = {}
    reward["gold"] = random.randint(QUEST_REWARDS_TEMPLATE["gold"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["gold"]["max"] * player_level)
    if random.random() < 0.7:
        reward["experience"] = random.randint(QUEST_REWARDS_TEMPLATE["experience"]["min"] * player_level, QUEST_REWARDS_TEMPLATE["experience"]["max"] * player_level)
    
    chosen_item_quality = "common"
    for level_range, qualities in QUEST_REWARDS_TEMPLATE["item_quality_levels"].items():
        if level_range[0] <= player_level <= level_range[1]:
            chosen_item_quality = random.choice(qualities)
            break
    
    # Favor "item" tag for item rewards, but allow others if not present
    if ("item" in quest_tags or not quest_tags) and random.random() < 0.45: # Increased chance slightly
        item_category_choice = random.choice(["weapon", "armor", "potion", "jewelry", "misc", "scroll"])
        # Consider chosen_item_quality if gr_item_func supports it
        reward_item = gr_item_func(item_category_choice, player_level) 
        if reward_item: reward["item"] = reward_item
            
    additional_reward_types = [rt for rt in QUEST_REWARDS_TEMPLATE.keys() if rt not in ["gold", "experience", "item_quality_levels", "item"]]
    if additional_reward_types and random.random() < 0.3:
        chosen_type = random.choice(additional_reward_types)
        value_source = QUEST_REWARDS_TEMPLATE[chosen_type]
        if isinstance(value_source, list): reward[chosen_type] = _get_random_from_list(value_source)
        else: reward[chosen_type] = random.randint(value_source["min"], value_source["max"])
    return reward

class DummyRumor:
    def __init__(self): self.tags = {}
    def add_tag(self, cat: str, type: str, val: str) -> None:
        if cat not in self.tags: self.tags[cat] = {}
        self.tags[cat][type] = val

# --- Dynamic Placeholder Data ---
# These would ideally be more dynamic or pulled from game data
RANDOM_MOUNTAIN_RANGES = ["Jerall Mountains", "Velothi Mountains", "Druadach Mountains", "Throat of the World foothills"]
RANDOM_ITEM_TYPES = ["amulet", "ring", "sword", "book", "potion ingredient", "map", "valuable gem"]
RANDOM_CREATURE_TYPES = ["wolf pack", "frostbite spider", "cave bear", "troll", "skeever infestation", "mudcrab cluster"]
RANDOM_RUIN_TYPES = ["Nordic barrow", "Dwemer ruin", "Imperial fort", "ancient watchtower"]
RANDOM_NOBLE_FAMILY_NAMES = ["Black-Briar", "Silver-Blood", "Battle-Born", "Gray-Mane", "Shatter-Shield", "Cruel-Sea"]
RANDOM_GUILD_NAMES = ["Thieves Guild", "Companions", "College of Winterhold", "Dark Brotherhood (whispers, of course)", "Bards College"]
RANDOM_DIVINE_NAMES = ["Akatosh", "Mara", "Dibella", "Kynareth", "Stendarr", "Zenithar", "Julianos", "Arkay", "(and some still say Talos...)"]
RANDOM_DAEDRIC_PRINCE_NAMES = ["Mehrunes Dagon", "Molag Bal", "Vaermina", "Sheogorath", "Hermaeus Mora", "Namira", "Boethiah", "Azura"]
RANDOM_JASCO_ADJECTIVES = ["fierce","cunning","shadowy","ancient","forgotten","cursed","sacred","hidden","lost","powerful","dangerous","mysterious"]
RANDOM_ENEMIES = ["bandits", "Forsworn", "draugr", "necromancers", "vampires", "Falmer", "hagravens", "Thalmor patrols"]

def _get_dynamic_placeholder(placeholder_type: str, current_location: Dict[str, Any] = None) -> str:
    """Helper to get a random value for a placeholder based on type."""
    if placeholder_type == "[NPC_Name_Local]": return get_npc_name_by_role_hint(random.choice(["merchant", "farmer", "guard", "innkeeper"]))["name"]
    if placeholder_type == "[NPC_Name_Suspicious]": return get_npc_name_by_role_hint(random.choice(["thief", "smuggler", "shady character"]))["name"]
    if placeholder_type == "[Location_Name_Nearby_Minor]":
        # Try to find a minor known location (village, camp, cave) in the same hold
        if current_location and current_location.get("parent_name"):
            parent_hold_name = current_location["parent_name"]
            hold_obj = next((loc for loc in LOCATIONS if loc["name"] == parent_hold_name), None)
            if hold_obj and hold_obj.get("sub_locations"):
                minor_locs = [s_loc["name"] for s_loc in hold_obj["sub_locations"] if any(tag in s_loc.get("tags",[]) for tag in ["village", "camp", "cave", "mine", "shack"])]
                if minor_locs: return random.choice(minor_locs)
        return random.choice(["a nearby cave", "an old watchtower", "that farmstead down the road"]) # Fallback
    if placeholder_type == "[Item_Type_Common]": return random.choice(["axe", "some firewood", "a healing poultice", "some bread"])
    if placeholder_type == "[Item_Type_Valuable]": return random.choice(RANDOM_ITEM_TYPES)
    if placeholder_type == "[Creature_Type_Common]": return random.choice(["wolf", "skeever", "mudcrab"])
    if placeholder_type == "[Creature_Type_Dangerous]": return random.choice(RANDOM_CREATURE_TYPES)
    if placeholder_type == "[Ruin_Name_Specific]": # Find actual ruin name
        ruin_locs = find_locations_by_tag("ruin") + find_locations_by_tag("barrow") + find_locations_by_tag("dwemer_ruin")
        return random.choice(ruin_locs)["name"] if ruin_locs else "some old ruins"
    if placeholder_type == "[Ruin_Type]": return random.choice(RANDOM_RUIN_TYPES)
    if placeholder_type == "[Mountain_Range]": return random.choice(RANDOM_MOUNTAIN_RANGES)
    if placeholder_type == "[Noble_Family_Name]": return random.choice(RANDOM_NOBLE_FAMILY_NAMES)
    if placeholder_type == "[Guild_Name]": return random.choice(RANDOM_GUILD_NAMES)
    if placeholder_type == "[Divine_Name]": return random.choice(RANDOM_DIVINE_NAMES)
    if placeholder_type == "[Daedric_Prince_Name]": return random.choice(RANDOM_DAEDRIC_PRINCE_NAMES)
    if placeholder_type == "[Jarl_Name_Current_Hold]":
        if current_location and current_location.get("parent_name"): # Assuming parent_name is the hold
            # This requires a mapping of Holds to Jarls, or dynamic lookup
            hold_jarls = {"Whiterun Hold": "Balgruuf", "Eastmarch": "Ulfric", "Haafingar": "Elisif", "The Reach": "Igmund", "The Rift": "Laila", "Falkreath Hold": "Siddgeir", "Hjaalmarch":"Idgrod", "The Pale":"Skald", "Winterhold Hold": "Korir"}
            return hold_jarls.get(current_location["parent_name"], "the Jarl")
        return "the Jarl"
    if placeholder_type == "[Enemy_Type_Plural]": return random.choice(RANDOM_ENEMIES)
    if placeholder_type == "[Adjective_Mysterious]": return random.choice(RANDOM_JASCO_ADJECTIVES)

    return placeholder_type # Return as is if no match

# --- Flavor Rumor Templates ---
FLAVOR_RUMOR_TEMPLATES = {
    "general_skyrim": [
        "They say the civil war could flare up again any day now. Best keep your head down and your blade sharp.",
        "Heard the Greybeards up on the Throat of the World are as silent as ever. Wonder what portents they're seeing in these troubled times?",
        "Another merchant caravan went missing in the [Mountain_Range] pass. Bad business, that. Some blame bandits, others... something older.",
        "The Thalmor are getting bolder, asking questions everywhere. Makes you wonder what they're truly after.",
        "Magic is a dangerous thing. Some say the College of Winterhold meddles too much. Others say they're Skyrim's only hope against... well, you know.",
        "Skyrim's an ancient land. Full of old grudges and even older secrets buried beneath the snow.",
        "You hear about that [Adjective_Mysterious] artifact found near [Ruin_Name_Specific]? Probably just a story, but still...",
        "Word is, the [Guild_Name] is looking for new blood. Risky work, but the coin can be good, if you've got the stomach for it.",
        "The Divines seem distant these days, don't they? Or perhaps we've just forgotten how to listen. Pray to [Divine_Name], just in case.",
        "Some folk whisper that the [Daedric_Prince_Name] cults are stirring again. Nasty business, that. Stay away from their shrines."
    ],
    "tavern_inn_social": [ # Tags for the current location if it's a tavern/inn
        "The mead here is [Adjective_Mead_Quality], if you ask me. But the [Innkeeper_Name] tells a good tale if you buy 'em a round.",
        "Saw [NPC_Name_Guard] hassling some poor [Race_Minority] by the docks earlier. Shameful, that is. This city's changing.",
        "This inn's seen better days, but it's cozier than sleeping under the stars with the [Creature_Type_Common] howling.",
        "Someone was in here earlier, asking about a lost [Item_Type_Valuable]. Looked quite desperate. Probably long gone by now.",
        "Heard [Local_Figure_Name] is in trouble with the [Noble_Family_Name] again. Never a dull moment in [ParentLocationName].",
        "This war... it's bad for business. But good for sell-swords, I suppose. More coin, more blood.",
        "Careful who you trust in a place like this. Walls have ears, and loose lips sink ships... or get throats slit.",
        "They say the best rumors are found at the bottom of an ale mug. Or was it the worst decisions?",
        "If you're looking for trouble, or trying to avoid it, you've come to the right (or wrong) place."
    ],
    "market_shop": [
        "Fresh [Food_Type] from [Nearby_Farm_Region_Name] just came in, or so [Merchant_Name] claims. Smells fresh enough.",
        "That merchant, [Suspicious_Merchant_Name], is trying to pass off painted glass as soul gems again. Watch out for that one.",
        "Guards are cracking down on pickpockets. Or so they say. Still wouldn't leave your coin purse unattended for long.",
        "Prices for [Material_Type] have gone through the roof since the [Enemy_Type_Plural] started raiding the trade routes.",
        "Heard [Competitor_Shop_Owner_Name] is spreading rumors about this place. Dirty business, competition.",
        "Looking for something specific, outlander? Or just Browse? We get all sorts here.",
        "If you've got the coin, I've got the goods. And if you don't have the coin... well, maybe we can make a different kind of arrangement."
    ],
    "city_town_village": [ # General settlement rumors
        "The [Jarl_Name_Current_Hold] has been in a foul mood. Something about taxes, or was it those [Enemy_Type_Plural] again?",
        "There's talk of a festival next season to honor [Divine_Name]. Or maybe it was cancelled due to 'unforeseen circumstances'. Hard to keep track.",
        "That [Local_Building_Type] on the edge of town? They say it's haunted. Or maybe just infested with [Creature_Type_Common].",
        "Heard young [NPC_Name_Local_Youth] got into trouble with the guards again. That one's heading for a life in Cidhna Mine, I reckon.",
        "The local alchemist is looking for rare [Ingredient_Type]. Pays well, if you don't mind braving the [Wilderness_Type] to find it.",
        "Keep an eye on the notice board. Sometimes there's actual work posted, not just complaints about the [Jarl_Name_Current_Hold]'s latest decree.",
        "This place used to be quieter before the war. Now everyone's on edge."
    ],
    "wilderness_forest_mountain_plains_coastal": [ # For NPCs encountered in the wild or referring to wild areas
        "The [Creature_Type_Dangerous] in these [Wilderness_Type] are getting bolder. Saw one the size of a pony the other day.",
        "There's an old hermit who lives deeper in these [Wilderness_Type]. Some say he's mad, others say he knows ancient secrets of the land.",
        "Found some strange glowing [Plant_or_Mushroom_Type] near the [RiverName_or_Landmark] last night. Didn't dare touch them.",
        "That old [Ruin_Type] up on [HillName_or_MountainName]? Haunted, I tell you. Best stay clear, especially when the moons are full.",
        "Treasure hunters went into [CaveName_or_DungeonName] a week ago. Haven't seen hide nor hair of 'em since.",
        "They say the ancient Nords buried their dead with great treasures. But the draugr... they don't like their rest disturbed.",
        "The coast is treacherous. Storms can whip up in an instant, and there are things in the deep waters best left undisturbed.",
        "If you see a sabre cat, don't try to outrun it. Just... pray to Kynareth."
    ],
    # Hold-specific rumor categories (examples, expand these greatly)
    "whiterun_hold_general": [
        "Balgruuf is a strong Jarl, but even he's caught between the Empire and Stormcloaks. Tough spot to be in.",
        "The Companions in Jorrvaskr? Honorable warriors, every one of them. Though some say their new recruits are a bit... wild.",
        "Dragonsreach... imagine a dragon truly imprisoned there. Gives you chills."
    ],
    "eastmarch_general": [
        "Windhelm is an ancient city, but the Grey Quarter... tensions are high there. Ulfric needs to address it.",
        "The hot springs in Eastmarch are a blessing, but even they can't wash away the bitterness of this war.",
        "Watch out for giants and their mammoths on the volcanic tundra. Best to give them a wide berth."
    ],
    # ... (more categories for other holds, specific ruin types, factions, etc.)
}

def _replace_placeholders_in_rumor(rumor_template: str, current_location: Dict[str, Any]) -> str:
    """Replaces placeholders in a rumor string with dynamic content."""
    # A more robust way would be to find all placeholders and replace them iteratively.
    # For now, a series of replaces.
    rumor = rumor_template # Start with the template

    # Location-based placeholders
    rumor = rumor.replace("[LocationName]", current_location.get("name", "this strange place"))
    parent_name = current_location.get("parent_name")
    if not parent_name and "hold" in current_location.get("tags",[]): # If current_location is a Hold itself
        parent_name = current_location.get("name")
    elif not parent_name: # Absolute fallback if no parent
        parent_name = "the nearest major city"
    rumor = rumor.replace("[ParentLocationName]", parent_name)
    rumor = rumor.replace("[Jarl_Name_Current_Hold]", _get_dynamic_placeholder("[Jarl_Name_Current_Hold]", current_location))


    # General placeholders (order can matter if one placeholder could be part of another)
    placeholders = [
        "[NPC_Name_Local]", "[NPC_Name_Guard]", "[NPC_Name_Suspicious]", "[Innkeeper_Name]", "[Merchant_Name]", "[Suspicious_Merchant_Name]", "[Local_Figure_Name]", "[Competitor_Shop_Owner_Name]", "[NPC_Name_Local_Youth]",
        "[Location_Name_Nearby_Minor]", "[Ruin_Name_Specific]", "[CaveName_or_DungeonName]", "[HillName_or_MountainName]", "[RiverName_or_Landmark]",
        "[Item_Type_Common]", "[Item_Type_Valuable]",
        "[Creature_Type_Common]", "[Creature_Type_Dangerous]",
        "[Food_Type]", "[Material_Type]", "[Ingredient_Type]", "[Plant_or_Mushroom_Type]",
        "[Race_Minority]", "[Noble_Family_Name]", "[Guild_Name]", "[Divine_Name]", "[Daedric_Prince_Name]",
        "[Ruin_Type]", "[Mountain_Range]", "[Wilderness_Type]", "[Local_Building_Type]",
        "[Enemy_Type_Plural]", "[Adjective_Mysterious]", "[Adjective_Mead_Quality]"
    ]
    # Example values for some less common placeholders for variety
    adjective_mead_quality = random.choice(["strong", "weak", "surprisingly good", "terrible", "passable"])


    for ph in placeholders:
        if ph in rumor: # Only try to replace if placeholder exists
            if ph == "[Innkeeper_Name]": replacement = get_npc_name_by_role_hint("innkeeper")["name"]
            elif ph == "[Merchant_Name]": replacement = get_npc_name_by_role_hint("merchant")["name"]
            elif ph == "[Suspicious_Merchant_Name]": replacement = get_npc_name_by_role_hint("thief")["name"] # or shady merchant
            elif ph == "[NPC_Name_Guard]": replacement = get_npc_name_by_role_hint("guard")["name"]
            elif ph == "[Local_Figure_Name]": replacement = get_npc_name_by_role_hint(random.choice(["noble","mage","warrior"]))["name"]
            elif ph == "[Competitor_Shop_Owner_Name]": replacement = get_npc_name_by_role_hint("merchant")["name"]
            elif ph == "[NPC_Name_Local_Youth]": replacement = get_npc_name_by_role_hint("child")["name"] if "child" in NAME_POOLS else get_npc_name_by_role_hint("peasant")["name"] # Requires child names
            elif ph == "[Race_Minority]": replacement = random.choice(["Dunmer", "Argonian", "Khajiit", "Bosmer"])
            elif ph == "[Food_Type]": replacement = random.choice(["apples", "fish", "venison", "potatoes"])
            elif ph == "[Material_Type]": replacement = random.choice(["iron ore", "firewood", "linen", "hides"])
            elif ph == "[Ingredient_Type]": replacement = random.choice(["nightshade", "deathbell", "mountain flower", "nirnroot"])
            elif ph == "[Plant_or_Mushroom_Type]": replacement = random.choice(["glowing mushrooms", "bloodgrass", "mana bloom"])
            elif ph == "[Local_Building_Type]": replacement = random.choice(["old mill", "abandoned shack", "ruined tower", "fishery"])
            elif ph == "[Adjective_Mead_Quality]": replacement = adjective_mead_quality
            else: replacement = _get_dynamic_placeholder(ph, current_location)
            rumor = rumor.replace(ph, replacement, 1) # Replace only first instance to avoid runaway loops if placeholders are substrings of replacements

    return rumor


def generate_location_appropriate_quest(player_level: int, current_location_tags: List[str], quest_giver_id: str | None = None, rumor_text: str | None = None) -> Quest | None:
    possible_templates = []
    for template in QUEST_TEMPLATES:
        if not (template["level_range"][0] <= player_level <= template["level_range"][1]): continue
        if template["location_tags_required"]:
            if not any(tag in current_location_tags for tag in template["location_tags_required"]): continue
        possible_templates.append(template)

    if rumor_text and hasattr(tags, 'filter_entities_by_tags'):
        rumor_obj = DummyRumor()
        rumor_obj.add_tag("rumor", "text", rumor_text)
        rumor_criteria = {"rumor": {"text": rumor_text}}
        possible_templates = tags.filter_entities_by_tags(possible_templates, rumor_criteria)

    if not possible_templates:
        UI.print_system_message(f"DEBUG: No specific quest template matched for level {player_level} and tags {current_location_tags}. Generating generic quest.")
        potential_loc_names_in_tags = [loc['name'] for loc in LOCATIONS if loc['name'].lower().replace(" ", "_") in current_location_tags]
        chosen_location_for_generic_quest = random.choice(LOCATIONS) # Default
        if potential_loc_names_in_tags:
             chosen_loc_name_for_generic_quest = random.choice(potential_loc_names_in_tags)
             chosen_location_for_generic_quest = next((loc for loc in LOCATIONS if loc['name'] == chosen_loc_name_for_generic_quest), chosen_location_for_generic_quest)

        title = f"An Errand in {chosen_location_for_generic_quest.get('name', 'a nearby area')}"
        description = f"Word is that someone in {chosen_location_for_generic_quest.get('name', 'a nearby area')} could use a hand. Might be a simple delivery, finding a lost trinket, or just lending an ear. Small tasks for small coin, most likely."
        
        objectives_list = [{"id": f"generic_obj_{random.randint(100,999)}", "type": "reach_location", "location_name": chosen_location_for_generic_quest.get("name", "the area"), "note": f"Investigate the small task mentioned in {chosen_location_for_generic_quest.get('name', 'the area')}."}]
        stages_list = [{"stage_name": "Complete Errand", "objectives": objectives_list, "on_completion_dialogue": "You've handled the matter. Well done."}]
        reward = generate_reward(player_level, current_location_tags)
        quest = Quest(title=title, description=description, reward=reward, level_requirement=player_level, location=chosen_location_for_generic_quest, stages=stages_list, status="active", turn_in_npc_id=quest_giver_id, quest_id=f"generic_errand_{random.randint(1000,9999)}")
        quest.add_tag("quest", "type", "generic_errand")
        return quest

    chosen_template = random.choice(possible_templates)
    final_quest_location_obj = random.choice(LOCATIONS)
    if chosen_template["location_tags_required"]:
        candidate_locations_for_quest_events = []
        for tag_needed_for_event in chosen_template["location_tags_required"]:
            candidate_locations_for_quest_events.extend(find_locations_by_tag(tag_needed_for_event))
        if candidate_locations_for_quest_events:
            candidate_locations_for_quest_events = list({loc["id"]: loc for loc in candidate_locations_for_quest_events}.values())
            final_quest_location_obj = random.choice(candidate_locations_for_quest_events)
    
    actual_ruin_name = _get_dynamic_placeholder("[Ruin_Name_Specific]")
    actual_artifact_name = _get_dynamic_placeholder("[Item_Type_Valuable]") # More generic for artifact name
    actual_artifact_key = actual_artifact_name.lower().replace(" ","_") + "_relic"
    
    # Specific placeholders for beast hunt template
    beast_type = "Cave Bear"
    beast_type_id = "cave_bear"
    forest_or_mountain_name = _get_dynamic_placeholder("[Location_Name_Nearby_Minor]")
    if "beast_hunt_rumors" == chosen_template["id"]:
        beast_type = random.choice(["Frostbite Spider Broodmother", "Alpha Wolf", "Grizzled Bear", "Ice Wraith Matriarch", "Sabre Cat Packleader"])
        beast_type_id = beast_type.lower().replace(" ", "_")
        forest_or_mountain_name = random.choice(find_locations_by_tag("forest") + find_locations_by_tag("mountain"))["name"]


    title = chosen_template["title_template"].replace("[LOCATION_NAME]", final_quest_location_obj["name"]).replace("[RUIN_NAME]", actual_ruin_name).replace("[ARTIFACT_NAME]", actual_artifact_name).replace("[BEAST_TYPE]", beast_type).replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name)
    description = chosen_template["desc_template"].replace("[LOCATION_NAME]", final_quest_location_obj["name"]).replace("[RUIN_NAME]", actual_ruin_name).replace("[ARTIFACT_NAME]", actual_artifact_name).replace("[BEAST_TYPE]", beast_type).replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name).replace("[LOCAL_LANDMARK_NAME]", _get_dynamic_placeholder("[Location_Name_Nearby_Minor]")).replace("[WILDERNESS_TYPE]", random.choice(["the dark woods","the craggy hills","the misty fens"]))
    
    objectives_list = []
    for i, obj_template in enumerate(chosen_template["objectives_template"]):
        new_obj = obj_template.copy()
        new_obj["id"] = f"obj_{chosen_template['id']}_{i}_{random.randint(100,999)}"
        
        new_obj["note"] = new_obj.get("note", "Complete this objective.") # Default note
        # Replace all placeholders in note
        new_obj["note"] = new_obj["note"].replace("[LOCATION_NAME]", final_quest_location_obj["name"])
        new_obj["note"] = new_obj["note"].replace("[RUIN_NAME]", actual_ruin_name)
        new_obj["note"] = new_obj["note"].replace("[ARTIFACT_NAME]", actual_artifact_name)
        new_obj["note"] = new_obj["note"].replace("[LOCAL_LANDMARK_NAME]", _get_dynamic_placeholder("[Location_Name_Nearby_Minor]", final_quest_location_obj))
        new_obj["note"] = new_obj["note"].replace("[WILDERNESS_TYPE]", random.choice(["the dark woods","the craggy hills","the misty fens"]))
        new_obj["note"] = new_obj["note"].replace("[BEAST_TYPE]", beast_type)
        new_obj["note"] = new_obj["note"].replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name)

        if "##" in new_obj["note"] and "count" in new_obj: new_obj["note"] = new_obj["note"].replace("##", str(new_obj["count"]))
        
        if "location_name" in new_obj: new_obj["location_name"] = new_obj["location_name"].replace("[RUIN_NAME]", actual_ruin_name).replace("[LOCAL_LANDMARK_NAME]", _get_dynamic_placeholder("[Location_Name_Nearby_Minor]", final_quest_location_obj)).replace("[FOREST_OR_MOUNTAIN_NAME]", forest_or_mountain_name)
        if "item_key" in new_obj: new_obj["item_key"] = new_obj["item_key"].replace("[ARTIFACT_KEY]", actual_artifact_key)
        if "target_name" in new_obj : new_obj["target_name"] = new_obj["target_name"].replace("[BEAST_TYPE]", beast_type)
        if "target_id" in new_obj : new_obj["target_id"] = new_obj["target_id"].replace("[BEAST_TYPE_ID]", beast_type_id)

        objectives_list.append(new_obj)

    stage_name_template = chosen_template.get("stage_name_template", "Primary Objectives")
    stage_name = stage_name_template.replace("[LOCATION_NAME]", final_quest_location_obj["name"]).replace("[RUIN_NAME]", actual_ruin_name).replace("[BEAST_TYPE]", beast_type)
    stages_list = [{"stage_name": stage_name, "objectives": objectives_list, "on_completion_dialogue": f"The matter concerning {stage_name} appears to be resolved."}]
    if chosen_template.get("stages"): stages_list = chosen_template["stages"] # For multi-stage templates (would need placeholder replacement too)

    reward = generate_reward(player_level, chosen_template.get("reward_tags", []))
    initial_flavor_text = ""
    if "flavor_tags" in chosen_template:
        dummy_entity = DummyRumor()
        for cat, types_dict in chosen_template["flavor_tags"].items():
            for tag_type, tags_list_val in types_dict.items():
                if tags_list_val: dummy_entity.add_tag(cat, tag_type, random.choice(tags_list_val))
        retrieved_flavors = flavor.get_flavor(dummy_entity) if hasattr(flavor, 'get_flavor') else []
        if retrieved_flavors: initial_flavor_text = random.choice(retrieved_flavors)

    quest = Quest(
        quest_id=chosen_template["id"] + f"_{random.randint(100,999)}", # Ensure unique ID for instances
        title=title, description=description, reward=reward, level_requirement=player_level,
        location=final_quest_location_obj, stages=stages_list, status="active",
        turn_in_npc_id=quest_giver_id, initial_flavor_text=initial_flavor_text
    )
    if "lore_tags" in chosen_template:
        for lore_tag in chosen_template["lore_tags"]: quest.add_tag("quest", "lore", lore_tag)
    if "flavor_tags" in chosen_template and "quest" in chosen_template["flavor_tags"] and \
       "type" in chosen_template["flavor_tags"]["quest"] and chosen_template["flavor_tags"]["quest"]["type"]:
        quest.add_tag("quest", "type", random.choice(chosen_template["flavor_tags"]["quest"]["type"]))
    else: quest.add_tag("quest", "type", "general_adventure")
    return quest

def process_quest_rewards(player: Any, quest: Quest) -> None:
    UI.print_subheading(f"Quest Completed: {quest.title}!")
    UI.slow_print("You have received your rewards:")
    for reward_type, reward_value in quest.reward.items():
        if reward_type == "gold":
            player.stats.gold += reward_value
            UI.print_success(f"- {reward_value} Gold.")
        elif reward_type == "experience": player.gain_experience(reward_value)
        elif reward_type == "item" and isinstance(reward_value, Item):
            if player.add_item(reward_value): UI.print_success(f"- Acquired: {reward_value.name}!")
            else: UI.print_warning(f"- You found {reward_value.name}, but your inventory is full!")
        elif reward_type == "reputation": UI.print_success(f"- Your reputation with local factions has improved by {reward_value}.")
        elif reward_type == "favor": UI.print_success(f"- You have gained {reward_value}.")
    UI.press_enter()

def generate_rumor(player_level: int, current_location: Dict[str, Any], quest_giver_id: str | None = None) -> Dict[str, Any]:
    quest_data_object = None
    rumor_text = ""

    if random.random() < PROBABILITY_OF_QUEST_RUMOR:
        quest_data_object = generate_location_appropriate_quest(player_level, current_location.get("tags", []), quest_giver_id)

    if quest_data_object and isinstance(quest_data_object, Quest):
        action_verb = "looking into"
        quest_type_tags_list = quest_data_object.tags.get("quest", {}).get("type", [])
        if not isinstance(quest_type_tags_list, list): quest_type_tags_list = [quest_type_tags_list] # ensure list

        if any(verb in quest_type_tags_list for verb in ["hunt", "clear"]): action_verb = "dealing with"
        elif any(verb in quest_type_tags_list for verb in ["fetch", "retrieve"]): action_verb = "finding"
        
        short_desc_snippet = quest_data_object.description.split('.')[0] # First sentence of quest description
        if "errand" in quest_data_object.quest_id or "generic_errand" in quest_type_tags_list :
             rumor_text = f"Heard that someone over in {quest_data_object.location.get('name', 'a nearby place')} might have a small task, if you're not too busy for simple work."
        else:
             # Combine the initial hook, first sentence of description, and flavor text
             short_desc_snippet = quest_data_object.description.split('.')[0] # First sentence of quest description
             # Add a space if flavor text exists, otherwise just use the snippet
             flavor_snippet = f" {quest_data_object.initial_flavor_text}" if quest_data_object.initial_flavor_text else ""
             rumor_text = f"There's talk of trouble over at {quest_data_object.location.get('name', 'a place nearby')}. {short_desc_snippet}.{flavor_snippet} Sounds like it could use a capable hand."
    else:
        location_tags = current_location.get("tags", [])
        parent_loc_name = current_location.get("parent_name", "the capital city")
        current_loc_name = current_location.get("name", "these parts")

        chosen_rumor_category_key = "general_skyrim"
        tag_precedence = [
            # Specific venue types present at current_location
            *(tag for tag in ["tavern", "inn", "market", "shop", "blacksmith", "alchemy_shop", "temple", "college", "palace", "keep", "docks"] if tag in location_tags),
            # General location types
            *(tag for tag in ["city", "town", "village"] if tag in location_tags),
            # Environmental types
            *(tag for tag in ["forest", "mountain", "cave", "ruin", "barrow", "mine", "wilderness", "coastal", "ashland_waste", "volcanic_caldera"] if tag in location_tags),
            # Hold-specific, if applicable
            current_location.get("parent_name", "impossible_match_for_hold").lower().replace(" ", "_") + "_general",
            "general_skyrim" # Absolute fallback
        ]

        for tag_key in tag_precedence:
            if tag_key in FLAVOR_RUMOR_TEMPLATES:
                chosen_rumor_category_key = tag_key
                break
        
        rumor_list_for_category = FLAVOR_RUMOR_TEMPLATES.get(chosen_rumor_category_key, FLAVOR_RUMOR_TEMPLATES["general_skyrim"])
        rumor_template = random.choice(rumor_list_for_category)
        rumor_text = _replace_placeholders_in_rumor(rumor_template, current_location)

    return {"text": UI.capitalize_dialogue(rumor_text.strip()), "quest_data": quest_data_object}
