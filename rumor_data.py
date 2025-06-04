import random
from typing import List, Dict, Any, Callable, Optional

class Rumor:
    def __init__(
        self,
        category: str,
        text: str,
        location_tags: Optional[List[str]] = None,
        effects: Optional[List[Callable]] = None,
        dynamic: bool = False,
        condition: Optional[Callable[[], bool]] = None,
    ):
        self.category = category
        self.text = text
        self.location_tags = location_tags or []
        self.effects = effects or []
        self.dynamic = dynamic
        self.condition = condition

    def __repr__(self):
        return f"Rumor(category='{self.category}', text='{self.text[:50]}...', dynamic={self.dynamic})"

# --- Quest Rewards and Templates ---
QUEST_REWARDS_TEMPLATE: Dict[str, Any] = {
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

QUEST_TEMPLATES: List[Dict[str, Any]] = [
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
        "location_tags_required": ["camp", "bandit_camp", "ruin_occupied", "wilderness_outpost"],
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
        "location_tags_required": ["barrow", "dungeon", "undead_presence", "historic_site", "tavern", "inn", "social", "college"],
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
            {"id": "mp_discover_fate", "type": "discover_fate", "target_name": "missing person", "note": "Determine what happened to the missing person."}
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

# --- Dynamic Placeholder Data ---
RANDOM_MOUNTAIN_RANGES: List[str] = ["Jerall Mountains", "Velothi Mountains", "Druadach Mountains", "Throat of the World foothills"]
RANDOM_ITEM_TYPES: List[str] = ["amulet", "ring", "sword", "book", "potion ingredient", "map", "valuable gem"]
RANDOM_CREATURE_TYPES: List[str] = ["wolf pack", "frostbite spider", "cave bear", "troll", "skeever infestation", "mudcrab cluster"]
RANDOM_RUIN_TYPES: List[str] = ["Nordic barrow", "Dwemer ruin", "Imperial fort", "ancient watchtower"]
RANDOM_NOBLE_FAMILY_NAMES: List[str] = ["Black-Briar", "Silver-Blood", "Battle-Born", "Gray-Mane", "Shatter-Shield", "Cruel-Sea"]
RANDOM_GUILD_NAMES: List[str] = ["Thieves Guild", "Companions", "College of Winterhold", "Dark Brotherhood (whispers, of course)", "Bards College"]
RANDOM_DIVINE_NAMES: List[str] = ["Akatosh", "Mara", "Dibella", "Kynareth", "Stendarr", "Zenithar", "Julianos", "Arkay", "(and some still say Talos...)"]
RANDOM_DAEDRIC_PRINCE_NAMES: List[str] = ["Mehrunes Dagon", "Molag Bal", "Vaermina", "Sheogorath", "Hermaeus Mora", "Namira", "Boethiah", "Azura"]
RANDOM_JASCO_ADJECTIVES: List[str] = ["fierce","cunning","shadowy","ancient","forgotten","cursed","sacred","hidden","lost","powerful","dangerous","mysterious"]
RANDOM_ENEMIES: List[str] = ["bandits", "Forsworn", "draugr", "necromancers", "vampires", "Falmer", "hagravens", "Thalmor patrols"]

# --- Flavor Rumor Templates ---
FLAVOR_RUMOR_TEMPLATES: List[Rumor] = [
    Rumor(
        category="general_skyrim",
        text="They say the civil war could flare up again any day now. Best keep your head down and your blade sharp.",
    ),
    Rumor(
        category="general_skyrim",
        text="Heard the Greybeards up on the Throat of the World are as silent as ever. Wonder what portents they're seeing in these troubled times?",
    ),
    Rumor(
        category="general_skyrim",
        text="Another merchant caravan went missing in the [Mountain_Range] pass. Bad business, that. Some blame bandits, others... something older.",
    ),
    Rumor(
        category="general_skyrim",
        text="The Thalmor are getting bolder, asking questions everywhere. Makes you wonder what they're truly after.",
    ),
    Rumor(
        category="general_skyrim",
        text="Magic is a dangerous thing. Some say the College of Winterhold meddles too much. Others say they're Skyrim's only hope against... well, you know.",
    ),
    Rumor(
        category="general_skyrim",
        text="Skyrim's an ancient land. Full of old grudges and even older secrets buried beneath the snow.",
    ),
    Rumor(
        category="general_skyrim",
        text="You hear about that [Adjective_Mysterious] artifact found near [Ruin_Name_Specific]? Probably just a story, but still...",
    ),
    Rumor(
        category="general_skyrim",
        text="Word is, the [Guild_Name] is looking for new blood. Risky work, but the coin can be good, if you've got the stomach for it.",
    ),
    Rumor(
        category="general_skyrim",
        text="The Divines seem distant these days, don't they? Or perhaps we've just forgotten how to listen. Pray to [Divine_Name], just in case.",
    ),
    Rumor(
        category="general_skyrim",
        text="Some folk whisper that the [Daedric_Prince_Name] cults are stirring again. Nasty business, that. Stay away from their shrines.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="The mead here is [Adjective_Mead_Quality], if you ask me. But the [Innkeeper_Name] tells a good tale if you buy 'em a round.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="Saw [NPC_Name_Guard] hassling some poor [Race_Minority] by the docks earlier. Shameful, that is. This city's changing.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="This inn's seen better days, but it's cozier than sleeping under the stars with the [Creature_Type_Common] howling.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="Someone was in here earlier, asking about a lost [Item_Type_Valuable]. Looked quite desperate. Probably long gone by now.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="Heard [Local_Figure_Name] is in trouble with the [Noble_Family_Name] again. Never a dull moment in [ParentLocationName].",
    ),
    Rumor(
        category="tavern_inn_social",
        text="This war... it's bad for business. But good for sell-swords, I suppose. More coin, more blood.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="Careful who you trust in a place like this. Walls have ears, and loose lips sink ships... or get throats slit.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="They say the best rumors are found at the bottom of an ale mug. Or was it the worst decisions?",
    ),
    Rumor(
        category="tavern_inn_social",
        text="If you're looking for trouble, or trying to avoid it, you've come to the right (or wrong) place.",
    ),
    Rumor(
        category="market_shop",
        text="Fresh [Food_Type] from [Nearby_Farm_Region_Name] just came in, or so [Merchant_Name] claims. Smells fresh enough.",
    ),
    Rumor(
        category="market_shop",
        text="That merchant, [Suspicious_Merchant_Name], is trying to pass off painted glass as soul gems again. Watch out for that one.",
    ),
    Rumor(
        category="market_shop",
        text="Guards are cracking down on pickpockets. Or so they say. Still wouldn't leave your coin purse unattended for long.",
    ),
    Rumor(
        category="market_shop",
        text="Prices for [Material_Type] have gone through the roof since the [Enemy_Type_Plural] started raiding the trade routes.",
    ),
    Rumor(
        category="market_shop",
        text="Heard [Competitor_Shop_Owner_Name] is spreading rumors about this place. Dirty business, competition.",
    ),
    Rumor(
        category="market_shop",
        text="Looking for something specific, outlander? Or just Browse? We get all sorts here.",
    ),
    Rumor(
        category="market_shop",
        text="If you've got the coin, I've got the goods. And if you don't have the coin... well, maybe we can make a different kind of arrangement.",
    ),
    Rumor(
        category="city_town_village",
        text="The [Jarl_Name_Current_Hold] has been in a foul mood. Something about taxes, or was it those [Enemy_Type_Plural] again?",
    ),
    Rumor(
        category="city_town_village",
        text="There's talk of a festival next season to honor [Divine_Name]. Or maybe it was cancelled due to 'unforeseen circumstances'. Hard to keep track.",
    ),
    Rumor(
        category="city_town_village",
        text="That [Local_Building_Type] on the edge of town? They say it's haunted. Or maybe just infested with [Creature_Type_Common].",
    ),
   Rumor(
        category="city_town_village",
        text="Heard young [NPC_Name_Local_Youth] got into trouble with the guards again. That one's heading for a life in Cidhna Mine, I reckon.",
    ),
    Rumor(
        category="city_town_village",
        text="The local alchemist is looking for rare [Ingredient_Type]. Pays well, if you don't mind braving the [Wilderness_Type] to find it.",
    ),
    Rumor(
        category="city_town_village",
        text="Keep an eye on the notice board. Sometimes there's actual work posted, not just complaints about the [Jarl_Name_Current_Hold]'s latest decree.",
    ),
    Rumor(
        category="city_town_village",
        text="This place used to be quieter before the war. Now everyone's on edge.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="The [Creature_Type_Dangerous] in these [Wilderness_Type] are getting bolder. Saw one the size of a pony the other day.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="There's an old hermit who lives deeper in these [Wilderness_Type]. Some say he's mad, others say he knows ancient secrets of the land.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="Found some strange glowing [Plant_or_Mushroom_Type] near the [RiverName_or_Landmark] last night. Didn't dare touch them.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="That old [Ruin_Type] up on [HillName_or_MountainName]? Haunted, I tell you. Best stay clear, especially when the moons are full.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="Treasure hunters went into [CaveName_or_DungeonName] a week ago. Haven't seen hide nor hair of 'em since.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="They say the ancient Nords buried their dead with great treasures. But the draugr... they don't like their rest disturbed.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="The coast is treacherous. Storms can whip up in an instant, and there are things in the deep waters best left undisturbed.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="If you see a sabre cat, don't try to outrun it. Just... pray to Kynareth.",
    ),
    Rumor(
        category="whiterun_hold_general",
        text="Balgruuf is a strong Jarl, but even he's caught between the Empire and Stormcloaks. Tough spot to be in.",
    ),
    Rumor(
        category="whiterun_hold_general",
        text="The Companions in Jorrvaskr? Honorable warriors, every one of them. Though some say their new recruits are a bit... wild.",
    ),
    Rumor(
        category="whiterun_hold_general",
        text="Dragonsreach... imagine a dragon truly imprisoned there. Gives you chills.",
    ),
    Rumor(
        category="eastmarch_general",
        text="Windhelm is an ancient city, but the Grey Quarter... tensions are high there. Ulfric needs to address it.",
    ),
    Rumor(
        category="eastmarch_general",
        text="The hot springs in Eastmarch are a blessing, but even they can't wash away the bitterness of this war.",
    ),
    Rumor(
        category="eastmarch_general",
        text="Watch out for giants and their mammoths on the volcanic tundra. Best to give them a wide berth.",
    ),
    # Add more diverse rumors
    Rumor(
        category="general_skyrim",
        text="Heard there's a dragon sighting near [Town_Name]. People are scared.",
    ),
    Rumor(
        category="tavern_inn_social",
        text="The [Bard_Name] at the bar is playing a sad song tonight. Must be missing someone.",
    ),
    Rumor(
        category="market_shop",
        text="Got a rare [Gem_Name] for sale. Only the finest quality.",
    ),
    Rumor(
        category="city_town_village",
        text="The Jarl is hosting a feast next week. Everyone's invited.",
    ),
    Rumor(
        category="wilderness_forest_mountain_plains_coastal",
        text="Saw a strange light in the sky last night. What could it be?",
    ),
    Rumor(
        category="winterhold_college",
        text="The College of Winterhold is accepting new students. If you have the talent, apply.",
    ),
    Rumor(
        category="riften_thievesguild",
        text="Word on the street is the Thieves Guild is looking for new recruits. If you're good with your hands, seek them out.",
    ),
    Rumor(
        category="darkbrotherhood",
        text="I heard whispers of a shadowy organization that lurks in the shadows, offering their services for a price. They say their name is the Dark Brotherhood.",
    ),
    Rumor(
        category="companions",
        text="The Companions are always looking for strong arms and brave hearts. If you seek glory and honor, join their ranks.",
    ),
    Rumor(
        category="dynamic_rumor",
        text="I overheard some guards talking about a recent theft from the Jarl's palace. They suspect someone from the Thieves Guild.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="There's a bounty on a bandit leader who's been terrorizing the roads. The Jarl is offering a hefty reward for their capture.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="I heard that a powerful mage is searching for rare ingredients to create a potent potion. They're willing to pay handsomely for any assistance.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="A group of adventurers discovered a hidden cave filled with treasure. But they say it's guarded by a fearsome creature.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="I overheard some merchants discussing a secret trade route that bypasses the city gates. They say it's dangerous, but the profits are immense.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="There's a rumor going around that a dragon egg has been found. If true, it could change the course of the war.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="I heard that a powerful artifact has been unearthed in a nearby ruin. But it's said to be cursed, bringing misfortune to anyone who possesses it.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="A group of refugees arrived in the city, fleeing from a war-torn land. They're seeking shelter and assistance.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="I overheard some scholars discussing a prophecy that foretells the end of the world. They say the signs are all around us.",
        dynamic=True,
    ),
    Rumor(
        category="dynamic_rumor",
        text="There's a rumor going around that a secret society is plotting to overthrow the government. They say their influence is growing.",
        dynamic=True,
    ),
]