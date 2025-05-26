# npc.py
import random
from stats import Stats, RACES
from items import Item
from ui import UI # Import UI for capitalization and debug messages
from quests import generate_location_appropriate_quest, Quest, process_quest_rewards
from tags import TAGS, get_tags
import flavor
from exploration_data import EXPLORATION_RESULTS
from rumors import generate_rumor

# Define roles that imply noble or commoner status
NOBLE_ROLES = {"noble", "jarl", "thane", "baron", "lady", "duke", "duchess", "court_mage", "advisor"}
COMMONER_ROLES = {
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand", "local",
    "stormcloak_supporter", "imperial_citizen", "mage_apprentice", "warrior", "companion_warrior",
    "new_blood", "circle_member", "thief_lookout", "pickpocket", "guild_rogue", "db_initiate",
    "explorer", "sailor", "dock_worker", "ship_captain_ashore", "fishmonger", "acolyte", "temple_guardian",
    "stall_owner", "shop_assistant", "city_guard_patrolling", "mine_foreman", "farmer_spouse"
}

# Define roles that are typically hostile
HOSTILE_ROLES = {
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "vampire", "vampire_thrall", "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thief_hostile",
    "draugr_restless", "skeleton_warrior", "ghost_ancient",
    "cave_bear_young", "wolf_alpha", "giant_spider_cave",
    "dwarven_sphere_guardian", "falmer_warrior", "chaurus_hunter_small",
    "mage_hostile", "cultist"
}
FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES

# NAME_POOLS (ensure this is complete as per your uploaded npc.py)
NAME_POOLS = {
    "nord": {
        "noble": {
            "male": ["Ulfric", "Torvald", "Jarlson", "Rolfrick", "Stahlund", "Brynjolf", "Kodlak", "Skjor", "Galmar", "Harkon", "Vignar", "Balgrüf"],
            "female": ["Brynhild", "Elfarra", "Sofira", "Hildrun", "Thyra", "Laila", "Astrid", "Elisif", " Maven", "Rikke", "Freyja", "Ingjard"]
        },
        "commoner": {
            "male": ["Ragnar", "Bjorn", "Sven", "Eirik", "Sigurd", "Hadvar", "Ralof", "Vilkas", "Farkas", "Stenvar", "Benor", "Cosnach", "Vorstag", "Hod", "Gerdur's Husband"],
            "female": ["Astrid", "Freya", "Ylva", "Ingrid", "Solveig", "Gerdur", "Sigrid", "Mjoll", "Lydia", "Uthgerd", "Annekke", "Sylgja", "Temba"]
        }
    },
    "imperial": {
        "noble": {
            "male": ["Titus", "Valerius", "Cassius", "Hadrian", "Septimus", "General Tullius", "Proventus Avenicci", "Legate Quentin Cipius", "Commander Maro", "Atticus", "Lucan"],
            "female": ["Serana", "Valeria", "Aurelia", "Livia", "Octavia", "Legate Rikke", "Vittoria Vici", "Elissia", "Claudia", "Antonia"]
        },
        "commoner": {
            "male": ["Gaius", "Marcus", "Tiber", "Lucius", "Rufus", "Marcurio", "Belrand", "Severio Pelagia", "Amaund Motierre", "Quintus Navale", "Adrian"],
            "female": ["Claudia", "Julia", "Fausta", "Silvia", "Vespasia", "Carlotta Valentia", "Wilmuth", "Herminia Cinna", "Gisli", "Alessia"]
        }
    },
    "breton": {
        "noble": {
            "male": ["Gaston", "Didier", "Armand", "Guillaume", "Thierry", "Farengar Secret-Fire", "Ainethach", "Gallus", " Mercer Frey", "Alain Dufont"],
            "female": ["Genevieve", "Isabelle", "Marguerite", "Annette", "Elodie", "Sybille Stentor", "Tonilia", "Muiri", "Lisette", "Vivienne"]
        },
        "commoner": {
            "male": ["Pierre", "Jean", "Louis", "François", "Antoine", "Belethor", "Enthir", "Delvin Mallory", "Orthus Endario", "Pascal", "Luc"],
            "female": ["Marie", "Sophie", "Jeanne", "Claire", "Nicole", "Colette Marence", "Ysolda", "Lisbet", "Hroki", "Sorine Jurard"]
        }
    },
    "redguard": {
        "noble": {
            "male": ["Ahmad", "Jamal", "Khalid", "Rashid", "Zafir", "Isran", "Nazir", "Sayyid", "Kematu", "Prince A'tor"],
            "female": ["Zafira", "Yasmina", "Samira", "Layla", "Aisha", "Iman", "Anora", "Rayya", "Faleen"]
        },
        "commoner": {
            "male": ["Cyrus", "Nazir", "Kematu", "Sadir", "Malik", "Nazeem", "Brenuin", "Revus Sarvani", "Ahlam"],
            "female": ["Imani", "Sana", "Nadia", "Zara", "Amina", "Saadia", "Shiri", "Safia", "Umana"]
        }
    },
    "dunmer": {
        "noble": {
            "male": ["Indoril Nerevar", "Redoran Drathis", "Telvanni Aryon", "Dres Aralen", "Hlaalu Othral", "Neloth", "Savos Aren", "Jiub", "Adril Arano", "Brandyl Telvanni"],
            "female": ["Morwen Indoril", "Fjola Redoran", "Jenassa Telvanni", "Brelyna Hlaalu", "Aranea Dres", "Karliah", "Irileth", "Serjo Lythandas", "Vendil Ulen"]
        },
        "commoner": {
            "male": ["Brand-Shei", "Revyn Sadri", "Adril Arano", "Malborn", "Erandur", "Romlyn Dreth", "Tythis Ulen", "Garyn Ienth", "Belyn Hlaalu", "Fethis Alor's brother"],
            "female": ["Jenassa", "Fethis Alor", "Mogrul", "Nilene Hulren", "Brelyna Maryon", "Suvaris Atheron", "Dravynea the Stoneweaver", "Avrusa Sarethi", "Mirri Severin"]
        }
    },
    "altmer": {
        "noble": {
            "male": ["Ancano", "Ondolemar", "Elenwen", "Rulindil", "Estormo", "Vingalmo", "Lord Naarifin", "Mannimarco", "Quaranir", "Chancellor Ocato"],
            "female": ["Elenwen", "Niranye", "Taarie", "Linwe", "Summerset Shadow", "High Chancellor Alwinarwe", "Ayrenn"]
        },
        "commoner": {
            "male": ["Faralda", "Calcelmo", "Enthir", "Runil", "Aicantar", "Nelacar", "Nirya", "Orthorn", "Melaran", "Falion"],
            "female": ["Endarie", "Vivienne Onis", "Legate Fasendil", "Nenya", "Atahba", "Minette Vinius"]
        }
    },
    "bosmer": {
        "noble": {
            "male": ["Faelan", "Niruin", "Borvir", "Maluril", "Orion", "Aengoth the Jeweler", "Glavis", "Cuinanthil"],
            "female": ["Niruin", "Grelka", "Nimphaneth", "Caminda", "Eridor", "The Green Lady"]
        },
        "commoner": {
            "male": ["Faendal", "Anoriath", "Valindor", "Elrindir", "Ma'randru-jo", "Gwilin", "Eothram", "Pavo Attius"],
            "female": ["Camilla Valerius", "Nimrodel", "Gilfre", "Indara Caerellia", "Ardwen", "Drynea"]
        }
    },
    "orc": {
        "noble": {
            "male": ["Ghorbash gro-Dushnikh", "Urag gro-Shub", "Yashnag gro-Yazguul", "Burguk gro-Bol", "Chief Larak gro-Dushnikh", "Murob gro-Largash", "Gularzob gro-Batul", "Ogol gro-Bagol"],
            "female": ["Mogakh gra-Dushnikh", "Shel gra-Yazguul", "Borba gra-Uzg", "Batul gra-Sharob", "Gharol gra-Lagash", "Ugor gra-Shamub", "Shuftharz gra-Larguk"]
        },
        "commoner": {
            "male": ["Grogmar gro-Burzag", "Muzgonk gro-Bulfim", "Shagrol gro-Yarug", "Urzog gro-Shamub", "Yamorz gro-Ghorak", "Gat gro-Shargakh", "Oglub gro-Largashbur", "Durak"],
            "female": ["Urzoga gra-Sharn", "Yatul gra-Lag", "Bagrak gra-Lazga", "Gharol gra-Phorkh", "Uglarz gra-Gasnouk", "Borgakh the Steel Heart", "Dulug gra-Shug"]
        }
    },
    "argonian": {
        "noble": {
            "male": ["Swims-in-Deep-Waters", "Hides-His-Eyes", "Chal-Ei", "Meer-Zish", "Raises-The-Spine", "Teeba-Ei", "Veezara"],
            "female": ["From-Deepest-Fathoms", "Scales-of-Steel", "Druja", "Wanan-To", "Sheer-Meedish", "Pale-Heart-Washes", "Neetrenaza"]
        },
        "commoner": {
            "male": ["Derkeethus", "Stands-In-Shadows", "Walks-Softly", "Madesi", "Talendri", "Beem-Ja", "Scouts-Many-Marshes", "Deep-In-His-Cups"],
            "female": ["Shahvee", "Keerava", "Deekus", "Wujeeta", "Reek-Neeus", "Gives-No-Fuss", "Brand-Shei's mother"]
        }
    },
    "khajiit": {
        "noble": {
            "male": ["J'zargo", "Ma'iq the Liar", "Dro'marash", "Ra'virr", "Ri'saad", "Kharjo", "J'darr", "Ma'jhad", "Razum-dar"],
            "female": ["Ahkari", "Razhinda", "Zaynabi", "Shavari", "Tsrava", "Ma'kara", "Atahbah", "Ri'zhaja"]
        },
        "commoner": {
            "male": ["M'aiq", "J'datharr", "Qa'jo", "Dro'shavir", "Kesh the Clean", "Vasha", "Ahjmal", "Zaymar"],
            "female": ["Shuravi", "Ra'kheran", "Dro'barri", "Kharjo's sister", "Skooma Cat's Friend", "Bahb-Bi", "Tsrasuna"]
        }
    },
     "undead_nord": {"noble": {"male":["Ysgramor", "High King Torygg"], "female":[]}, "commoner": {"male": ["Olaf One-Eye", " Jurgen Windcaller", "Red Eagle"], "female": ["Ancient Nord Huntress"]}},
     "undead_skeleton": {"noble": {}, "commoner": {"male": ["Cursed Guardian", "Bone-Clatter Warrior", "Rattling Archer"], "female": ["Decrepit Mage"]}},
     "spirit": {"noble": {}, "commoner": {"male": ["Fading Echo", "Wispmother's Attendant"], "female": ["Wailing Shade", "Lost Soul"]}},
     "falmer": {"noble": {"male":["Nightprowler Alpha"], "female":["Shadowseer Matriarch"]}, "commoner": {"male": ["Skulker Gloomdweller", "Chaurus-Tender Falmer", "Falmer Slave"], "female": ["Chanter of the Depths", "Falmer Gloomlurker"]}},
     "dwemer_construct_race": {"noble": {}, "commoner": {"male": ["CX-Series Guardian Unit 734", "Acutronic Spider MKIII", "Ballista Defense Unit 03"], "female": []}},
     "wolf_creature": {"noble": {}, "commoner": {"male": ["Dire Wolf Alpha", "Ice Wolf Pack Leader", "Timber Wolf Veteran"], "female": ["Alpha Female Wolf", "Shadow Wolf Matriarch"]}},
     "bear_creature": {"noble": {}, "commoner": {"male": ["Grizzled Cave Bear Patriarch", "Snow Bear Elder", "Giant Forest Bear"], "female": ["Cave Bear Matriarch", "Protective Mother Bear"]}},
     "spider_creature": {"noble": {}, "commoner": {"male": ["Venomfang Broodfather", "Giant Frostbite Spider Patriarch"], "female": ["Venomfang Broodmother", "Ancient Frostbite Spider Queen"]}},
     "chaurus_creature": {"noble": {}, "commoner": {"male": ["Chaurus Reaper Prime", "Chaurus Hunter Alpha"], "female": ["Chaurus Queen"]}},
}

# Add a unique ID to each NPC name in NAME_POOLS for tracking purposes
def assign_unique_npc_ids(name_pools):
    # This assigns a unique ID to each *predefined* name in the pools.
    # When creating an NPC, you'd pick a name from here, and its ID would be self.unique_id.
    # For dynamically generated NPCs (like generic bandits), a generic ID is used.
    for race_data in name_pools.values():
        for name_type_data in race_data.values():
            for gender_name_list in name_type_data.values():
                for i in range(len(gender_name_list)):
                    original_name = gender_name_list[i]
                    # Create a simple unique ID from the name and add a random suffix for more uniqueness
                    unique_id = f"{original_name.lower().replace(' ', '_')}_{random.randint(100, 999)}"
                    gender_name_list[i] = unique_id # Store the ID directly in the list
assign_unique_npc_ids(NAME_POOLS) # Call this once at module load

class NPC:
    def __init__(self, name: str, race: str, role: str, level: int, disposition: int = 50, gold: int = 0):
        self.race = race.lower() if race else "nord"
        self.role = role
        self.level = max(1, level)
        self.disposition = disposition
        self.gold = gold
        self.has_offered_quest = False # Flag to prevent offering the same quest repeatedly

        # Assign unique_id for this NPC instance
        # If name is provided (e.g., specific NPC), base ID on name+role
        # If name is None (e.g., generic NPC), pull from NAME_POOLS and use its ID, or generate generic.
        if name is None:
            gender = random.choice(["male", "female"])
            name_type = "noble" if self.role in NOBLE_ROLES else "commoner"
            
            race_name_pool_data = NAME_POOLS.get(self.race)
            if not race_name_pool_data:
                UI.print_system_message(f"DEBUG: NPC Init - No name pool found for race '{self.race}'. Falling back to 'nord'.")
                race_name_pool_data = NAME_POOLS.get("nord")

            specific_name_pool = race_name_pool_data.get(name_type)
            if not specific_name_pool:
                UI.print_system_message(f"DEBUG: NPC Init - No '{name_type}' name pool for race '{self.race}'. Falling back to 'commoner'.")
                specific_name_pool = race_name_pool_data.get("commoner")
            
            gender_specific_pool = specific_name_pool.get(gender)
            if not gender_specific_pool:
                UI.print_system_message(f"DEBUG: NPC Init - No '{gender}' names for '{name_type}' '{self.race}'. Falling back to generic 'unknown_npc'.")
                gender_specific_pool = ["unknown_npc_6"] # Final fallback

            chosen_id_from_pool = random.choice(gender_specific_pool)
            self.name = chosen_id_from_pool.split('_')[0].capitalize() # Display name is first part of ID
            self.unique_id = chosen_id_from_pool # Use the full ID from NAME_POOLS

        else: # If a specific name is provided (e.g., for quest givers)
            self.name = name
            # Generate a unique ID for this specific named NPC
            self.unique_id = f"{self.name.lower().replace(' ', '_')}_{self.role.lower().replace(' ', '_')}_{random.randint(100,999)}"

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

        # Initialize skills dictionary *before* applying racial or role-based skills
        self.skills = {}
        base_skill_val = 5

        # Assign skills based on ROLE first
        role_l = self.role.lower()
        if any(s_role in role_l for s_role in ["mage", "scholar", "priest", "shaman", "necromancer", "cultist", "healer"]):
            self.skills["destruction"] = random.randint(15, 30) + self.level * 2
            self.skills["restoration"] = random.randint(15, 30) + self.level * 2
            self.skills["alteration"] = random.randint(10, 25) + self.level
            self.skills["conjuration"] = random.randint(10, 25) + self.level if "mage" in role_l or "necromancer" in role_l else base_skill_val
            self.skills["illusion"] = random.randint(10, 20) + self.level if "mage" in role_l or "illusionist_role" in role_l else base_skill_val
        elif any(s_role in role_l for s_role in ["warrior", "guard", "bandit", "companion", "forsworn", "soldier", "legionnaire", "thug", "raider", "mercenary"]):
            self.skills["one_handed"] = random.randint(20, 35) + self.level * 2
            self.skills["block"] = random.randint(15, 30) + self.level
            self.skills[random.choice(["light_armor", "heavy_armor"])] = random.randint(15, 30) + self.level
            if random.random() < 0.3: self.skills["two_handed"] = random.randint(15,30) + self.level
            if "archer" in role_l: self.skills["archery"] = random.randint(20,35) + self.level *2
        elif any(s_role in role_l for s_role in ["thief", "assassin", "scout", "rogue", "pickpocket"]):
            self.skills["sneak"] = random.randint(20, 35) + self.level * 2
            self.skills["archery"] = random.randint(15, 30) + self.level if "scout" in role_l or "archer" in role_l else random.randint(10,20) + self.level
            self.skills["light_armor"] = random.randint(15, 30) + self.level
            self.skills["one_handed"] = random.randint(15,25) + self.level
            if "pickpocket" in role_l : self.skills["pickpocket"] = random.randint(25,40) + self.level * 2
        else:
            self.skills["speech"] = random.randint(10, 30) + self.level
            self.skills[random.choice(["one_handed", "archery"])] = random.randint(5,15) + self.level

        # Apply RACIAL modifiers to stats and skills
        race_mods = RACES.get(self.race, {})
        for attr, mod_val in race_mods.items():
            if attr.endswith("_mod") and hasattr(self.stats, attr.replace("_mod","")):
                 stat_name = attr.replace("_mod","")
                 setattr(self.stats, stat_name, getattr(self.stats, stat_name) + mod_val)
            elif attr.endswith("_resist") and hasattr(self.stats, attr):
                 setattr(self.stats, attr, getattr(self.stats, attr) + mod_val)
            elif attr == "magicka_mod" and hasattr(self.stats, "max_magicka"):
                self.stats.max_magicka += mod_val
            elif attr.endswith("_skill"): # Apply racial skill bonuses
                skill_name = attr.replace("_skill","")
                self.skills[skill_name] = self.skills.get(skill_name, base_skill_val) + mod_val

        # Recalculate derived stats after all modifications
        self.stats.max_health = int(75 + (self.stats.endurance * 2) + (self.level * 5))
        if not race_mods.get("magicka_mod"):
             self.stats.max_magicka = int(40 + (self.stats.intelligence * 1.5) + (self.level * 3))
        self.stats.max_fatigue = int(80 + (self.stats.endurance * 1.5) + (self.level * 4))

        self.stats.current_health = self.stats.max_health
        self.stats.current_magicka = self.stats.max_magicka
        self.stats.current_fatigue = self.stats.max_fatigue

        self.inventory = self.stats.inventory
        self.equipment = []
        self.status_effects = []

        self.tags = {}
        self.add_tag("npc", "role_primary", self.role)
        self.add_tag("npc", "race", self.race)
        initial_attitude = "hostile" if self.role in HOSTILE_ROLES else "neutral"
        if self.role in FRIENDLY_ROLES and self.role not in HOSTILE_ROLES:
            initial_attitude = "friendly"
        self.add_tag("npc", "attitude", initial_attitude)

        self.greeting = self._generate_greeting()
        self.purpose = self._generate_purpose()

    def __str__(self):
        return f"{self.name} ({self.role.replace('_',' ').capitalize()}, Level {self.level})"

    def add_tag(self, category, key, value):
        if category not in self.tags:
            self.tags[category] = {}
        self.tags[category][key] = value

    def _generate_greeting(self):
        base_greetings = {
            "friendly": ["Greetings, friend!", "Well met!", "A pleasure to see you.", "Welcome, traveler."],
            "neutral": ["Hello.", "What do you want?", "State your business.", "Can I help you?"],
            "hostile": ["You're not welcome here!", "Lost, little one?", "Another fool come to die!", "You'll regret crossing me!"]
        }
        attitude = self.tags.get("npc", {}).get("attitude", "neutral")

        # Use flavor.py to get more nuanced greetings if available
        if hasattr(flavor, 'NPC_FLAVORS') and 'attitude' in flavor.NPC_FLAVORS and attitude in flavor.NPC_FLAVORS['attitude']:
            possible_greetings = flavor.NPC_FLAVORS['attitude'][attitude]
            if self.race in flavor.NPC_FLAVORS.get('race', {}): # Add race specific greetings
                possible_greetings.extend(flavor.NPC_FLAVORS['race'][self.race])
            return UI.capitalize_dialogue(random.choice(possible_greetings))

        # Fallback to simpler disposition-based greetings, applying capitalization
        if attitude != "hostile":
            if self.disposition >= 70:
                return UI.capitalize_dialogue(random.choice(base_greetings["friendly"] + ["The gods smile upon this meeting!", "May your roads lead you to warm sands."]))
            elif self.disposition >= 30:
                return UI.capitalize_dialogue(random.choice(base_greetings["neutral"] + ["Need something?", "Speak if you must."]))
            else:
                return UI.capitalize_dialogue(random.choice(["Hmph.", "Don't waste my time.", "What is it now?"]))
        else:
            return UI.capitalize_dialogue(random.choice(base_greetings["hostile"]))

    def _generate_purpose(self):
        role_lower = self.role.lower()
        # Check flavor.py for role-specific purposes first
        if hasattr(flavor, 'NPC_FLAVORS') and 'class' in flavor.NPC_FLAVORS: # Assuming 'class' in flavor matches 'role'
            role_flavor_key = None
            for key in flavor.NPC_FLAVORS['class'].keys(): # Find a matching key (e.g., "warrior" for "bandit_warrior")
                if key in role_lower:
                    role_flavor_key = key
                    break
            if role_flavor_key and flavor.NPC_FLAVORS['class'][role_flavor_key]:
                return UI.capitalize_dialogue(random.choice(flavor.NPC_FLAVORS['class'][role_flavor_key]))

        # Fallback to existing purpose generation, applying capitalization
        if "merchant" in role_lower: return UI.capitalize_dialogue(random.choice(["am here to trade fine goods.", "offer the best prices in this hold.", "seek to make a profit, of course."]))
        elif "guard" in role_lower: return UI.capitalize_dialogue(random.choice(["am keeping the peace.", "protect this place and its people.", "am on duty, move along."]))
        elif "farmer" in role_lower or "farm_hand" in role_lower: return UI.capitalize_dialogue(random.choice(["tend to my crops.", "work this land from dawn till dusk.", "pray for a good harvest this year."]))
        elif "innkeeper" in role_lower: return UI.capitalize_dialogue(random.choice(["run this fine establishment.", "offer a warm bed and a hot meal to weary travelers.", "hear many tales, some true, some not so much."]))
        elif "bard" in role_lower: return UI.capitalize_dialogue(random.choice(["share songs and stories of old.", "bring a little light into this world with my music.", "seek inspiration for my next great ballad."]))
        elif "scholar" in role_lower or "mage" in role_lower: return UI.capitalize_dialogue(random.choice(["delve into ancient lore and forgotten secrets.", "study the mysteries of Aetherius and Oblivion.", "seek knowledge above all else, for knowledge is power."]))
        elif "priest" in role_lower or "healer" in role_lower or "acolyte" in role_lower: return UI.capitalize_dialogue(random.choice(["serve the Divines and their will.", "offer comfort and healing to the needy and the sick.", "guide the lost and protect the faithful from darkness."]))
        elif "hunter" in role_lower: return UI.capitalize_dialogue(random.choice(["track game in the wilds to provide for my kin.", "know these lands like the back of my hand, every stream and shadow.", "live by the bow and the quiet footfall."]))
        elif "miner" in role_lower: return UI.capitalize_dialogue(random.choice(["toil in the depths for ore and precious gems.", "seek riches beneath the stone, hoping for a lucky strike.", "earn my keep with the sweat of my brow and the swing of my pickaxe."]))
        elif any(s_role in role_lower for s_role in ["adventurer", "warrior", "mercenary", "companion", "explorer"]): return UI.capitalize_dialogue(random.choice(["seek fortune and glory wherever they may be found.", "live by my blade and my wits.", "am always ready for a new challenge or a worthy cause."]))
        elif any(s_role in role_lower for s_role in ["bandit", "thief", "forsworn"]): return UI.capitalize_dialogue(random.choice(["take what this land owes me.", "believe this world is for the taking.", "survive by my own rules."]))
        else: return UI.capitalize_dialogue(random.choice(["live my life as best I can in these trying times.", "am just trying to get by, same as anyone.", "mind my own affairs mostly, if you please.", "have my duties to attend to, like everyone else."]))


    def share_rumor(self, player, current_location) -> None:
        """
        Shares a rumor with the player, generated contextually.
        Can also lead to the offering of a quest.
        """
        if self.disposition < 35:
            UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['I have no time for idle gossip.', 'Find someone else to bother with your trivial questions.'])}”"))
            return

        # Call the dedicated rumor generation function, passing NPC's unique ID as quest_giver_id
        rumor_output = generate_rumor(player.level, current_location, self.unique_id)
        rumor_text = rumor_output["text"] # This is already capitalized by rumors.py
        quest_data = rumor_output.get("quest_data")

        UI.slow_print(f"“{rumor_text}”")

        # Logic for offering quest if rumor generates one
        if quest_data:
            # Check if player already has this quest or has completed it
            if player.quest_log.get_quest_by_id(quest_data.quest_id):
                UI.slow_print(UI.capitalize_dialogue(f"“It seems you're already familiar with that matter, {player.name}.”"))
            else:
                self._offer_quest(player, quest_data)


    def _offer_quest(self, player, quest: Quest) -> None:
        """Internal method to handle the quest offering dialogue."""
        # Capitalize the relevant part of the quest description for dialogue
        quest_intro_text = UI.capitalize_dialogue(quest.description.split('.')[0])
        UI.slow_print(f"“And speaking of such things... I've heard there's a need for someone to {quest_intro_text.lower()}.”")
        UI.print_line('-')
        UI.print_info(f"Quest: {quest.title}")
        UI.print_info(f"Objective: {quest.description}") # Quest's main description
        # Optionally display objectives in more detail here if desired
        
        reward_parts = []
        if isinstance(quest.reward, dict):
            for r_type, r_value in quest.reward.items():
                if isinstance(r_value, Item):
                    reward_parts.append(f"{r_value.name} (Item)")
                else:
                    reward_parts.append(f"{r_value} {r_type.capitalize()}")
        else:
            reward_parts.append(str(quest.reward))
        reward_display_str = ", ".join(reward_parts) if reward_parts else "a token of my gratitude"
        UI.print_info(f"Reward: {reward_display_str}")
        UI.print_line('-')

        while True:
            quest_action_prompt = UI.print_prompt("Your response? [1] Accept [2] Decline [3] Consider it further").strip()
            if quest_action_prompt == "1":
                if player.quest_log.add_quest(quest):
                    UI.slow_print(UI.capitalize_dialogue(f"“Excellent! I knew I could count on you, {player.name}. The details are in your journal.”"))
                    self.disposition = min(100, self.disposition + random.randint(3, 7))
                else:
                    UI.slow_print(UI.capitalize_dialogue("“It seems you already have this task, or your journal is full. A pity.”"))
                self.has_offered_quest = True
                break
            elif quest_action_prompt == "2":
                UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['A pity. I had hoped for assistance.', 'Very well. The task will fall to another, then.', 'Understandable. Not all are suited for such endeavors.'])}”"))
                self.disposition = max(0, self.disposition - random.randint(1, 4))
                self.has_offered_quest = True
                break
            elif quest_action_prompt == "3":
                UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['As you wish. The opportunity may not last indefinitely.', 'Do not tarry too long if you intend to help.', 'Consider it, then. But time is often a factor.'])}”"))
                break
            else:
                UI.slow_print("A clear answer is expected, traveler.")


    def _discuss_place(self, current_location) -> None:
        """Provides a tag/flavor related answer when asked about the location."""
        loc_name = current_location.get("name", "this place")
        loc_tags = current_location.get("tags", [])
        
        # Create a dummy entity for flavor.get_flavor based on location tags
        class DummyLocationForFlavor:
            def __init__(self, tags_list):
                self.tags = {"location": {}}
                for tag_type, possible_values in TAGS["LOCATIONS"].items():
                    found_tags = [t for t in tags_list if t in possible_values]
                    if found_tags:
                        self.tags["location"][tag_type] = found_tags
        
        dummy_loc_entity = DummyLocationForFlavor(loc_tags)
        flavor_vignettes = flavor.get_flavor(dummy_loc_entity)
        
        if flavor_vignettes:
            chosen_flavor = random.choice(flavor_vignettes)
            UI.slow_print(UI.capitalize_dialogue(f"“Ah, {loc_name}. {chosen_flavor}”"))
        else:
            # Fallback to general comments if no specific flavor found
            comments = []
            if "city" in loc_tags: comments.append("It's a major hub, always something happening, for better or worse.")
            if "town" in loc_tags: comments.append("A decent enough place. Quieter than the big cities, which suits some folk.")
            if "village" in loc_tags: comments.append("A small, tight-knit community. We look out for each other here.")
            if "tavern" in loc_tags or "inn" in loc_tags: comments.append("A good place to rest your feet, share a drink, and hear the latest news... or tall tales.")
            if "mountain" in loc_tags: comments.append("The air here is thin, and the peaks are unforgiving. Beautiful, but dangerous.")
            if "forest" in loc_tags: comments.append("The woods are deep and old here. Many secrets, and many dangers, lie within.")
            if "mine" in loc_tags: comments.append("Many fortunes have been made and lost in these mines. A hard life, but honest work.")

            if comments:
                UI.slow_print(UI.capitalize_dialogue(f"“Ah, {loc_name}. {random.choice(comments)}”"))
            else:
                UI.slow_print(UI.capitalize_dialogue(f"“{loc_name}... It is what it is. Not much else to say about it, really.”"))


    def dialogue(self, player, current_location) -> None:
        """
        Handles the dialogue interaction with the player.
        """
        UI.clear_screen()
        # Add NPC's unique ID to player's talked-to tracker
        player.add_talked_to_npc(self.unique_id)

        UI.slow_print(f"You approach {self.name} ({self.role.replace('_',' ').capitalize()}). Disposition: {self.disposition}")
        UI.slow_print(f"“{self.greeting} {self.purpose}”")
        
        # Options for the player dialogue menu
        options_texts = []

        # Check for quests to turn in FIRST
        quests_to_turn_in = player.quest_log.get_quests_for_turn_in(self.unique_id)
        if quests_to_turn_in:
            options_texts.append("Turn in a completed quest")

        # Now add other standard options
        options_texts.append("Ask for rumors or work") # Combined option
        options_texts.append("Ask about your work/purpose") # Still distinct, but less direct quest-ask
        options_texts.append("Discuss this place")
        options_texts.append("Farewell")

        while True:
            UI.print_menu(options_texts)
            choice_input = UI.print_prompt("Your response? (Enter number)").strip()

            if not choice_input.isdigit():
                UI.slow_print("Please enter a valid number for your choice.")
                UI.press_enter()
                continue
            
            choice_idx = int(choice_input)
            action_taken = False

            chosen_option_text = None
            if 1 <= choice_idx <= len(options_texts):
                chosen_option_text = options_texts[choice_idx - 1]

            if chosen_option_text == "Turn in a completed quest":
                if quests_to_turn_in:
                    UI.slow_print("Which quest do you wish to turn in?")
                    for i, quest in enumerate(quests_to_turn_in):
                        UI.slow_print(f"[{i+1}] {quest.title}")
                    
                    turn_in_choice = UI.print_prompt("Enter number: ")
                    if turn_in_choice.isdigit():
                        turn_in_idx = int(turn_in_choice) - 1
                        if 0 <= turn_in_idx < len(quests_to_turn_in):
                            quest_to_process = quests_to_turn_in[turn_in_idx]
                            UI.slow_print(UI.capitalize_dialogue(f"“Ah, you've completed '{quest_to_process.title}'! Excellent work!”"))
                            process_quest_rewards(player, quest_to_process)
                            player.quest_log.remove_quest(quest_to_process.quest_id)
                            UI.slow_print(UI.capitalize_dialogue(f"“Thank you, {player.name}. Your efforts are much appreciated.”"))
                            self.disposition = min(100, self.disposition + random.randint(5, 10))
                            quests_to_turn_in = player.quest_log.get_quests_for_turn_in(self.unique_id)
                            if not quests_to_turn_in and "Turn in a completed quest" in options_texts:
                                options_texts.remove("Turn in a completed quest")
                        else:
                            UI.slow_print("Invalid choice.")
                    else:
                        UI.slow_print("Invalid input.")
                else:
                    UI.slow_print("You have no completed quests to turn in to me.")
                action_taken = True

            elif chosen_option_text == "Ask for rumors or work": # New combined option
                self.share_rumor(player, current_location)
                action_taken = True

            elif chosen_option_text == "Ask about your work/purpose":
                UI.slow_print(f"“As I said, I {self.purpose}”")
                if self.disposition > 60 and "merchant" in self.role.lower():
                    UI.slow_print(UI.capitalize_dialogue(f"“Perhaps you're looking to buy or sell, {player.name}? I have a few things that might interest you, or I might be interested in what you carry.”"))
                elif self.disposition > 55 and "guard" in self.role.lower():
                    UI.slow_print(UI.capitalize_dialogue(f"“Just try to stay out of trouble. That makes my job easier.”"))
                
                # Chance to offer a quest based on their 'work' if they haven't already offered one
                if not self.has_offered_quest and random.random() < 0.4: # 40% chance
                     UI.slow_print(UI.capitalize_dialogue(f"“Actually, since you're asking, there is something that's been bothering me about my work...”"))
                     # Generate a quest here (similar to how share_rumor does it)
                     quest = generate_location_appropriate_quest(player.stats.level, current_location.get("tags", []), self.unique_id)
                     if quest and not player.quest_log.get_quest_by_id(quest.quest_id): # Ensure not a duplicate
                         self._offer_quest(player, quest)
                     else:
                         UI.slow_print(UI.capitalize_dialogue(random.choice(["“But perhaps it's best not to burden you with my troubles.”", "“Nevermind, I'll handle it myself.”"])))
                action_taken = True

            elif chosen_option_text == "Discuss this place":
                self._discuss_place(current_location) # Call new helper method
                action_taken = True

            elif chosen_option_text == "Farewell":
                UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['Farewell, traveler.', 'May your path be clear.', 'Until next time.'])}”"))
                return # Exit dialogue
            else:
                UI.slow_print("A clear answer is expected, traveler.")
            
            if action_taken:
                UI.press_enter()
                UI.clear_screen()
                UI.slow_print(f"You are speaking with {self.name}. Disposition: {self.disposition}")
                UI.slow_print(f"“{self.greeting} {self.purpose}”")