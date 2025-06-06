# npc_entities.py
import random
from typing import Any, List, Dict
from stats import Stats, RACES
from items import Item
from ui import UI
from spells import get_spell, Spell
from npc_names import NAME_POOLS, NORD_SURNAMES # <-- IMPORT NORD_SURNAMES
from npc_dialogue_generation import generate_greeting, generate_purpose
import json

# --- Roles for Random Generation ---
NOBLE_ROLES = {
    "noble",
    "thane",
    "steward",
    "court_wizard",
    "advisor",
}

COMMONER_ROLES = {
    # Basic Professions
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand",
    "alchemist", "fletcher", "lumberjack", "woodcutter", "ferryman", "carriage_driver",
    "pawnbroker", "shopkeeper", "beggar", "elder", "child", "courier", "executioner",

    # Faction-Specific (Non-Hostile)
    "companion", "college_mage", "blade", "greybeard", "vigilant_of_stendarr",
    "penitus_oculatus", "thieves_guild_member", "dark_brotherhood_member",
    "imperial_soldier", "stormcloak_soldier", "orc_stronghold_member",

    # Misc Roles
    "mercenary", "pilgrim", "refugee"
}

HOSTILE_ROLES = {
    # Humanoid Enemies
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "warlock", "conjurer", "illusionist", "pyromancer",
    "vampire", "vampire_thrall", "vampire_lord",
    "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thalmor_justiciar", "thalmor_soldier", "reaver", "cultist", "silver_hand",

    # Undead
    "draugr", "draugr_wight", "draugr_scourge", "draugr_deathlord",
    "skeleton", "ghost", "wraith", "dragon_priest",

    # Creatures
    "wolf", "ice_wolf", "bear", "cave_bear", "snow_bear",
    "spider", "frostbite_spider", "troll", "frost_troll",
    "hagraven", "spriggan", "wisp", "wispmother", "ice_wraith",
    "giant", "mammoth",

    # Daedra & Constructs
    "dremora", "atronach_flame", "atronach_frost", "atronach_storm",
    "dwarven_sphere", "dwarven_spider", "dwarven_centurion",

    # Subterranean
    "falmer", "falmer_shaman", "chaurus", "chaurus_hunter"
}

FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES


class NPC:
    def __init__(self, name: str, race: str, role: str, level: int, disposition: int = 50, gold: int = 0, patrol_route: List[str] = None, location_context: dict = None):
        self.race = race.lower() if race else "nord"
        self.role = role
        self.level = max(1, level)
        self.disposition = disposition
        self.gold = gold
        self.location_context = location_context # <-- STORE LOCATION CONTEXT
        self.patrol_route = patrol_route if patrol_route else []
        self.current_patrol_index = 0
        self.dialogue_history = []
        self.quest_giver = False # Can be updated based on quests
        self.vendor_inventory = [] # For merchants
        self.has_offered_quest = False
        self._generate_name_and_id(name)
        self.stats = Stats(level=self.level) # Create a Stats instance
        self.skills = {} # Populate based on role/class
        self.tags = {}
        self._initialize_npc_tags()
        self._initialize_stats_and_skills()
        self.known_spells: List[Spell] = []

    def _generate_name_and_id(self, name: str):
        if name is None:
            gender = random.choice(["male", "female"])
            name_type = "noble" if self.role in NOBLE_ROLES else "commoner"
            
            race_name_pool_data = NAME_POOLS.get(self.race, NAME_POOLS.get("nord", {}))
            specific_name_pool = race_name_pool_data.get(name_type, race_name_pool_data.get("commoner", {}))
            gender_specific_pool = specific_name_pool.get(gender, [])
            if not gender_specific_pool:
                gender_specific_pool = [f"unknown_npc_{random.randint(10,99)}"]

            self.unique_id = random.choice(gender_specific_pool)
            first_name_base = self.unique_id.split('_')[0].capitalize()

            final_surname = ""
            if self.race == "nord":
                hold_name = self.location_context.get("hold_name", "generic") if self.location_context else "generic"
                surname_pool = NORD_SURNAMES.get(hold_name, NORD_SURNAMES["generic"])
                if surname_pool:
                    final_surname = random.choice(surname_pool)
            
            if final_surname:
                self.name = f"{first_name_base} {final_surname}"
            else:
                self.name = first_name_base
        else:
            self.name = name
            self.unique_id = f"{self.name.lower().replace(' ', '_')}_{self.role.lower().replace(' ', '_')}_{random.randint(100,999)}"

    def _initialize_npc_tags(self):
        self.tags['npc'] = {
            "race": self.race,
            "role": self.role,
            "attitude": "friendly" if self.role in FRIENDLY_ROLES else "hostile"
        }

    def _initialize_stats_and_skills(self):
        # Basic stat generation based on role
        if self.role in HOSTILE_ROLES or "warrior" in self.role:
            self.stats.strength += 10
            self.stats.endurance += 5
        elif "mage" in self.role or "scholar" in self.role:
            self.stats.intelligence += 10
            self.stats.willpower += 5
        elif "thief" in self.role or "assassin" in self.role:
            self.stats.agility += 10
            self.stats.speed += 5
        # ... more detailed logic can be added ...
    
    def talk(self, player, current_location):
        greeting = generate_greeting(self.role, self.race, self.disposition, self.tags)
        purpose = generate_purpose(self.role, self.race, self.disposition, self.tags)
        
        UI.slow_print(f"{self.name} says: \"{greeting}\"")
        # Further dialogue logic would go here
        
    @property
    def full_name(self):
        return self.name