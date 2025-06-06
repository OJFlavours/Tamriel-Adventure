# npc_entities.py
import random
from typing import Any, List, Dict # Added Dict
from stats import Stats, RACES
from items import Item
from ui import UI # For debug messages during name generation
# Quest-related imports are not directly used by NPC class methods after refactor,
# but QuestLog might be part of player state, which NPC interacts with via dialogue logic.
# For now, keeping imports minimal to what NPC class directly uses.
# from quests import Quest, generate_location_appropriate_quest, QuestLog
from locations import RAW_LOCATION_DATA_MAP # Used if NPC needs to know about locations for non-dialogue reasons
from tags import TAGS, get_tags # For NPC tagging
# import flavor # Flavor is used in dialogue, not directly by NPC entity
# from exploration_data import EXPLORATION_RESULTS # Not directly used by NPC entity
# from rumors import generate_rumor # Rumor generation is part of dialogue logic
from spells import get_spell, Spell # For NPC spell list
# from npc_roles import NOBLE_ROLES, COMMONER_ROLES, HOSTILE_ROLES, FRIENDLY_ROLES # For role-based logic
from npc_names import NAME_POOLS # assign_unique_npc_ids is not used directly by the class
from npc_dialogue_generation import generate_greeting, generate_purpose # For initial greeting/purpose
import json

# Define roles that imply noble or commoner status
NOBLE_ROLES = {"noble", "jarl", "thane", "baron", "lady", "duke", "duchess", "court_mage", "advisor"}
COMMONER_ROLES = {
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand",
    "stormcloak_supporter", "imperial_citizen", "mage_apprentice", "warrior",
    "thief_lookout", "pickpocket", "guild_rogue", "db_initiate",
    "explorer", "sailor", "dock_worker", "ship_captain_ashore", "fishmonger", "acolyte", "temple_guardian",
    "stall_owner", "shop_assistant", "city_guard", "mine_foreman", "farmer_spouse",
    "server", "cook", "beggar", "elder", "stormcloak_recruiter", "imperial_deserter", "publican", "tavern_staff_server", "mine_owner", "alchemist_merchant", "jarl_advisor", "blacksmith_spouse", "jarl_stormcloak", "merchant_general_goods", "blacksmith", "blacksmith_trainer", "alchemist_apprentice", "untalented_bard", "mage_conjurer_scholar_vampire_expert", "merchant_clothing_tailor_haughty", "merchant_fletcher", "shop_assistant_woodcutter", "merchant_clothing_tailor", "stormcloak_officer", "jarl", "thane", "blacksmith_spouse", "bard_local", "mine_patron"
}

# Define roles that are typically hostile
HOSTILE_ROLES = {
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "vampire", "vampire_thrall", "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thief",
    "draugr", "skeleton", "ghost",
    "bear", "wolf", "spider",
    "dwarven_sphere", "falmer", "chaurus",
    "mage", "cultist", "thalmor_justiciar", "dominion_spy"
}

FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES

class NPC:
    def __init__(self, name: str, race: str, role: str, level: int, disposition: int = 50, gold: int = 0, patrol_route: List[str] = None):
        self.race = race.lower() if race else "nord"
        self.role = role
        self.level = max(1, level)
        self.disposition = disposition
        self.gold = gold
        self.has_offered_quest = False # Tracks if NPC has gone through a quest offer sequence
        self.is_follower = False
        self.mercenary_hire_cost = 0
        if "mercenary" in self.role.lower():
            self.mercenary_hire_cost = 50 + self.level * 10
        
        self.known_spells: list[Spell] = []
        
        self.eligible_for_quest_offer_roll: bool = True # One-time chance to offer a quest via rumor
        self.rumor_pool: List[str] = [] # For cycling non-quest rumors
        self.current_rumor_index: int = 0

        # Patrol Route
        self.patrol_route = patrol_route if patrol_route else []
        self.current_patrol_index = 0

        self._generate_name_and_id(name)
        self._initialize_stats_and_skills()
        self._apply_race_modifiers()
        self._finalize_stats()
        self._initialize_inventory()
        self._initialize_tags()
        self._generate_greeting_and_purpose()
        self.combat_archetype = self._determine_combat_archetype()

    def _generate_name_and_id(self, name: str):
        if name is None:
            gender = random.choice(["male", "female"])
            name_type = "noble" if self.role in NOBLE_ROLES else "commoner"

            race_name_pool_data = NAME_POOLS.get(self.race)
            if not race_name_pool_data:
                UI.print_system_message(f"DEBUG: NPC Init - No name pool found for race '{self.race}'.")
                if self.race == "orc":
                    race_name_pool_data = NAME_POOLS.get("orc", {})
                    if not race_name_pool_data:
                        race_name_pool_data = NAME_POOLS.get("orsimer", {})
                else:
                    UI.print_system_message(f"Falling back to 'nord'.")
                    race_name_pool_data = NAME_POOLS.get("nord", {}) # Added default {}

            specific_name_pool = race_name_pool_data.get(name_type)
            if not specific_name_pool:
                UI.print_system_message(f"DEBUG: NPC Init - No '{name_type}' name pool for race '{self.race}'. Falling back to 'commoner'.")
                specific_name_pool = race_name_pool_data.get("commoner", {}) # Added default {}

            gender_specific_pool = specific_name_pool.get(gender)
            if not gender_specific_pool:
                UI.print_system_message(f"DEBUG: NPC Init - No '{gender}' names for '{name_type}' '{self.race}'. Falling back to generic 'unknown_npc'.")
                gender_specific_pool = [f"unknown_npc_{random.randint(10,99)}"]

            self.unique_id = random.choice(gender_specific_pool) # This is the ID like "ulfric_stormcloak_123"
            first_name_base = self.unique_id.split('_')[0].capitalize()

            final_surname = ""
            races_without_surnames = {"khajiit", "argonian", "bosmer"}
            # Ensure specific_name_pool is not None before trying .get()
            if self.race in NAME_POOLS and self.race not in races_without_surnames and specific_name_pool:
                surname_key_type = "noble_surnames" if name_type == "noble" else "commoner_surnames"
                surname_pool_ids = specific_name_pool.get(surname_key_type, [])
                
                if surname_pool_ids:
                    chosen_surname_id = random.choice(surname_pool_ids)
                    base_surname_part = chosen_surname_id.split('_')[0]
                    
                    if '-' in base_surname_part:
                        final_surname = '-'.join(word.capitalize() for word in base_surname_part.split('-'))
                    else:
                        final_surname = base_surname_part.capitalize()
            
            if final_surname:
                self.name = f"{first_name_base} {final_surname}"
            else:
                self.name = first_name_base
        else:
            self.name = name
            self.unique_id = f"{self.name.lower().replace(' ', '_')}_{self.role.lower().replace(' ', '_')}_{random.randint(100,999)}"

    def _initialize_stats_and_skills(self):
        base_stat = 30
        self.stats = Stats(
            strength=random.randint(base_stat -5, base_stat + 10) + self.level,
            intelligence=random.randint(base_stat -5, base_stat + 10) + self.level,
            willpower=random.randint(base_stat -5, base_stat + 10) + self.level,
            agility=random.randint(base_stat -5, base_stat + 10) + self.level,
            speed=random.randint(base_stat -5, base_stat + 10) + self.level,
            endurance=random.randint(base_stat -5, base_stat + 10) + self.level,
            personality=random.randint(base_stat, base_stat + 20),
            luck=random.randint(base_stat - 10, base_stat + 5),
            level=self.level,
            gold=self.gold
        )
        self.skills: Dict[str, int] = {} # Explicitly type skills
        base_skill_val = 5

        role_l = self.role.lower()
        if role_l == "spectral_ally":
            self.skills["one_handed"] = 20 + self.level * 2
            self.skills["light_armor"] = 10 + self.level
            self.stats.strength = 30 + self.level * 3
            self.stats.agility = 40 + self.level * 3
            self.stats.endurance = 25 + self.level * 2
            basic_attack_spell = get_spell("flames")
            if basic_attack_spell: self.known_spells.append(basic_attack_spell)

        elif any(s_role in role_l for s_role in ["mage", "scholar", "priest", "shaman", "necromancer", "cultist", "healer", "mage_hostile"]):
            self.skills["destruction"] = random.randint(15, 30) + self.level * 2
            self.skills["restoration"] = random.randint(15, 30) + self.level * 2
            self.skills["alteration"] = random.randint(10, 25) + self.level
            self.skills["conjuration"] = random.randint(10, 25) + self.level if "mage" in role_l or "necromancer" in role_l or "shaman" in role_l else base_skill_val
            self.skills["illusion"] = random.randint(10, 20) + self.level if "mage" in role_l or "illusionist_role" in role_l else base_skill_val
            
            spell_keys_to_add: List[str] = []
            if "mage" in role_l or "scholar" in role_l or "mage_hostile" in role_l:
                spell_keys_to_add = ["firebolt", "flames"]
                if self.level > 5: spell_keys_to_add.append("lesser_ward")
            elif "priest" in role_l or "healer" in role_l:
                spell_keys_to_add = ["healing", "lesser_ward"]
            elif "necromancer" in role_l or "cultist" in role_l:
                spell_keys_to_add = ["firebolt"]
            if self.level > 3: spell_keys_to_add.append("conjure_familiar")
            elif "shaman" in role_l:
                spell_keys_to_add = ["flames"]
                if self.level > 4: spell_keys_to_add.append("healing")
            
            for key in spell_keys_to_add:
                spell = get_spell(key)
                if spell: self.known_spells.append(spell)

        elif any(s_role in role_l for s_role in ["warrior", "guard", "bandit", "companion", "forsworn", "soldier", "legionnaire", "thug", "raider", "mercenary", "thalmor_justiciar"]):
            self.skills["one_handed"] = random.randint(20, 35) + self.level * 2
            self.skills["block"] = random.randint(15, 30) + self.level
            self.skills[random.choice(["light_armor", "heavy_armor"])] = random.randint(15, 30) + self.level
            if random.random() < 0.3: self.skills["two_handed"] = random.randint(15,30) + self.level
            if "archer" in role_l: self.skills["archery"] = random.randint(20,35) + self.level *2 # Ensure archer role gets archery
        elif any(s_role in role_l for s_role in ["thief", "assassin", "scout", "rogue", "pickpocket"]): # Added pickpocket
            self.skills["sneak"] = random.randint(20, 35) + self.level * 2
            self.skills["archery"] = random.randint(15, 30) + self.level if "scout" in role_l or "archer" in role_l else random.randint(10,20) + self.level
            self.skills["light_armor"] = random.randint(15, 30) + self.level
            self.skills["one_handed"] = random.randint(15,25) + self.level
            if "pickpocket" in role_l : self.skills["pickpocket"] = random.randint(25,40) + self.level * 2
        else: # Default for other roles (e.g., commoners, nobles not covered above)
            self.skills["speech"] = random.randint(10, 30) + self.level
            self.skills[random.choice(["one_handed", "archery"])] = random.randint(5,15) + self.level

    def _apply_race_modifiers(self):
        base_skill_val = 5
        race_mods = RACES.get(self.race, {})
        for attr, mod_val in race_mods.items():
            if attr.endswith("_mod") and hasattr(self.stats, attr.replace("_mod","")):
                stat_name = attr.replace("_mod","")
                setattr(self.stats, stat_name, getattr(self.stats, stat_name) + mod_val)
            elif attr.endswith("_resist") and hasattr(self.stats, attr): # Assuming resists are direct attributes on Stats
                setattr(self.stats, attr, getattr(self.stats, attr, 0) + mod_val) # Default to 0 if not present
            elif attr == "magicka_mod" and hasattr(self.stats, "max_magicka"):
                self.stats.max_magicka += mod_val
            elif attr.endswith("_skill"): # e.g. "destruction_skill"
                skill_name = attr.replace("_skill","")
                self.skills[skill_name] = self.skills.get(skill_name, base_skill_val) + mod_val

    def _finalize_stats(self):
        self.stats.max_health = int(75 + (self.stats.endurance * 2) + (self.level * 5))
        race_mods = RACES.get(self.race, {})
        if not race_mods.get("magicka_mod"): # Only set default if no race mod applied
            self.stats.max_magicka = int(40 + (self.stats.intelligence * 1.5) + (self.level * 3))
        self.stats.max_fatigue = int(80 + (self.stats.endurance * 1.5) + (self.level * 4))

        self.stats.current_health = self.stats.max_health
        self.stats.current_magicka = self.stats.max_magicka
        self.stats.current_fatigue = self.stats.max_fatigue

    def _initialize_inventory(self):
        self.inventory: List[Item] = self.stats.inventory # Ensure inventory is typed
        self.equipment: List[Item] = [] # Ensure equipment is typed
        self.status_effects: List[Any] = [] # Type for status effects if defined

    def _initialize_tags(self):
        self.tags: Dict[str, Dict[str, Any]] = {} # Explicitly type tags
        self.add_tag("npc", "role_primary", self.role)
        self.add_tag("npc", "race", self.race)
        initial_attitude = "hostile" if self.role in HOSTILE_ROLES else "neutral"
        if self.role in FRIENDLY_ROLES and self.role not in HOSTILE_ROLES: # Ensure friendly roles aren't overridden if also hostile (e.g. complex faction NPC)
            initial_attitude = "friendly"
        self.add_tag("npc", "attitude", initial_attitude)

    def _generate_greeting_and_purpose(self):
        # Greeting and Purpose are generated at initialization for the NPC's persona
        self.greeting = generate_greeting(self.role, self.race, self.disposition, self.tags)
        self.purpose = generate_purpose(self.role, self.race, self.disposition, self.tags)

    def _determine_combat_archetype(self) -> str:
        """Determines the NPC's combat archetype based on their role."""
        role_l = self.role.lower()
        if any(r in role_l for r in ["mage_hostile", "necromancer", "cultist", "court_mage", "shaman"]):
            return "CautiousMage"
        if any(r in role_l for r in ["priest", "healer"]):
            return "SupportPriest"
        if any(r in role_l for r in ["bandit_leader", "forsworn_briarheart", "warrior", "companion_warrior", "guard", "thalmor_justiciar"]):
            return "AggressiveWarrior"
        if any(r in role_l for r in ["bandit_archer", "forsworn_raider", "hunter", "scout", "thief_hostile"]):
            return "SkirmisherArcher"
        if any(r in role_l for r in ["bandit", "bandit_thug", "forsworn_raider", "draugr_restless", "skeleton_warrior"]):
            return "StandardMelee"
        if "spectral_ally" in role_l:
            return "AggressiveSummon"
        # Broader creature matching, ensure "_creature" is specific enough or handled by role definitions
        if any(r in role_l for r in ["wolf", "bear", "spider", "chaurus"]) or "creature" in role_l or "_creature" in role_l:
            return "AggressiveCreature"
        return "StandardMelee" # Default for roles not fitting other archetypes

    def __str__(self):
        return f"{self.name} ({self.role.replace('_',' ').capitalize()}, Level {self.level})"

    @property
    def full_name(self):
        return self.name # self.name is pre-formatted during __init__

    def add_tag(self, category: str, key: str, value: Any):
        if category not in self.tags:
            self.tags[category] = {}
        self.tags[category][key] = value

    def move(self):
        """Moves the NPC along their patrol route."""
        try:
            if self.patrol_route:
                self.current_patrol_index = (self.current_patrol_index + 1) % len(self.patrol_route)
                current_location = self.patrol_route[self.current_patrol_index]
                print(f"{self.name} is moving to {current_location}")
                # Simulate movement by updating the NPC's location tag
                if "location" in self.tags and "lives_in" in self.tags["location"]:
                    self.tags["location"]["lives_in"] = current_location
                else:
                    self.add_tag("location", "lives_in", current_location)
        except Exception as e:
            print(f"Error moving {self.name}: {e}")

    def save_npc(self, filename: str):
        """Saves the NPC data to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.__dict__, f, indent=4)
            print(f"Saved {self.name} to {filename}")
        except Exception as e:
            print(f"Error saving {self.name}: {e}")

    @staticmethod
    def load_npc(filename: str):
        """Loads NPC data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                npc_data = json.load(f)
            npc = NPC(name=npc_data['name'], race=npc_data['race'], role=npc_data['role'], level=npc_data['level'])
            npc.__dict__.update(npc_data)
            print(f"Loaded {npc.name} from {filename}")
            return npc
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except Exception as e:
            print(f"Error loading NPC: {e}")
            return None

    # Dialogue-related methods (dialogue, share_rumor, _offer_quest, _discuss_place)
    # have been moved to npc_dialogue_logic.py

def define_specific_npcs():
    """Defines specific NPCs for the game world."""
    from npc_entities import NPC # Import here to avoid circular dependency

    # Jarls
    jarl_laila_lawgiver = NPC(name="Laila Law-Giver", race="nord", role="jarl", level=25, disposition=60, gold=500)
    jarl_laila_lawgiver.add_tag("location", "governs", "riften")
    jarl_laila_lawgiver.add_tag("political", "affiliation", "empire")

    jarl_korir = NPC(name="Korir", race="nord", role="jarl", level=28, disposition=40, gold=600)
    jarl_korir.add_tag("location", "governs", "winterhold")
    jarl_korir.add_tag("political", "affiliation", "empire")

    # Important Merchants
    birna = NPC(name="Birna", race="nord", role="merchant", level=15, disposition=50, gold=300)
    birna.add_tag("location", "lives_in", "winterhold")
    birna.add_tag("trade", "sells", "general_goods")

    # Guild Leaders (if applicable in 200 4E)
    endrast_direnni = NPC(name="Endrast Direnni", race="altmer", role="mage_guild_leader", level=35, disposition=45, gold=700)
    endrast_direnni.add_tag("location", "lives_in", "winterhold")
    endrast_direnni.add_tag("guild", "leader_of", "college_of_winterhold")

    # Other Influential Figures
    vulwulf_snow_shod = NPC(name="Vulwulf Snow-Shod", race="nord", role="thane", level=22, disposition=55, gold=400)
    vulwulf_snow_shod.add_tag("location", "lives_in", "windhelm")
    vulwulf_snow_shod.add_tag("political", "affiliation", "stormcloak")
    # Adding more specific NPCs for 200 4E

    # Jarls
    jarl_elisif_the_fair = NPC(name="Elisif the Fair", race="nord", role="jarl", level=27, disposition=65, gold=550)
    jarl_elisif_the_fair.add_tag("location", "governs", "solitude")
    jarl_elisif_the_fair.add_tag("political", "affiliation", "empire")

    bryling = NPC(name="Bryling", race="nord", role="merchant", level=18, disposition=52, gold=350)
    bryling.add_tag("location", "lives_in", "solitude")
    bryling.add_tag("trade", "sells", "clothing")

    galmar_stone_fist = NPC(name="Galmar Stone-Fist", race="nord", role="stormcloak_officer", level=30, disposition=48, gold=650)
    galmar_stone_fist.add_tag("location", "lives_in", "windhelm")
    galmar_stone_fist.add_tag("political", "affiliation", "stormcloak")
    # Additional NPCs for 200 4E

    # Jarls
    jarl_vignar_gray_mane = NPC(name="Vignar Gray-Mane", race="nord", role="jarl", level=26, disposition=55, gold=520)
    jarl_vignar_gray_mane.add_tag("location", "governs", "whiterun")
    jarl_vignar_gray_mane.add_tag("political", "affiliation", "neutral")

    # Merchants
    aeri = NPC(name="Aeri", race="wood elf", role="merchant", level=12, disposition=45, gold=250)
    aeri.add_tag("location", "lives_in", "angas_mill")
    aeri.add_tag("location", "region", "the_pale")
    aeri.add_tag("trade", "sells", "wood")

    hroki = NPC(name="Hroki", race="nord", role="blacksmith", level=17, disposition=58, gold=330)
    hroki.add_tag("location", "lives_in", "markarth")
    hroki.add_tag("trade", "sells", "weapons_armor")

    lisbet = NPC(name="Lisbet", race="nord", role="merchant", level=15, disposition=50, gold=300)
    lisbet.add_tag("location", "lives_in", "markarth")
    lisbet.add_tag("trade", "sells", "jewelry")

    return {
        "jarl_laila_lawgiver": jarl_laila_lawgiver,
        "jarl_korir": jarl_korir,
        "birna": birna,
        "endrast_direnni": endrast_direnni,
        "vulwulf_snow_shod": vulwulf_snow_shod,
        "jarl_elisif_the_fair": jarl_elisif_the_fair,
        "bryling": bryling,
        "galmar_stone_fist": galmar_stone_fist,
        "jarl_vignar_gray_mane": jarl_vignar_gray_mane,
        "aeri": aeri,
        "hroki": hroki,
        "lisbet": lisbet,
    }