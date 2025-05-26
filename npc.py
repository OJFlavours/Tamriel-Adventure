# npc.py
import random
from stats import Stats, RACES # Import RACES directly from stats
from items import Item, generate_random_item # Added Item for type checking in reward display
from ui import UI # Import UI
from quests import generate_location_appropriate_quest 
from tags import TAGS, get_tags 
import flavor 

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

# --- NAME_POOLS (Expanded) ---
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

class NPC:
    def __init__(self, name: str, race: str, role: str, level: int, disposition: int = 50, gold: int = 0):
        self.race = race.lower() if race else "nord" # Default to nord if race is None
        self.role = role
        self.level = max(1, level) 
        self.disposition = disposition 
        self.gold = gold
        self.has_offered_quest = False 

        if name is None:
            gender = random.choice(["male", "female"])
            name_type = "noble" if self.role in NOBLE_ROLES else "commoner"
            
            race_name_pool_data = NAME_POOLS.get(self.race, NAME_POOLS.get("nord")) 
            if not race_name_pool_data: 
                race_name_pool_data = {"noble": {"male":["Nobilus"],"female":["Nobilia"]}, "commoner": {"male":["Comminus"],"female":["Commina"]}}

            specific_name_pool = race_name_pool_data.get(name_type, race_name_pool_data.get("commoner", {"male": ["Nameless One"], "female": ["Nameless One"]}))
            
            # Ensure the gender pool exists, fallback to male if not, then to a generic name.
            gender_specific_pool = specific_name_pool.get(gender, specific_name_pool.get("male"))
            if not gender_specific_pool: # If "male" pool also missing for some reason
                 gender_specific_pool = ["Unknown NPC"]
            self.name = random.choice(gender_specific_pool)
        else:
            self.name = name

        # --- Stats Initialization (As previously defined, with slight scaling adjustment) ---
        base_stat = 30 # Average base for attributes
        self.stats = Stats(
            strength=random.randint(base_stat -5, base_stat + 10) + self.level, 
            intelligence=random.randint(base_stat -5, base_stat + 10) + self.level,
            willpower=random.randint(base_stat -5, base_stat + 10) + self.level,
            agility=random.randint(base_stat -5, base_stat + 10) + self.level,
            speed=random.randint(base_stat -5, base_stat + 10) + self.level, # Speed might be less influenced by level for some NPCs
            endurance=random.randint(base_stat -5, base_stat + 10) + self.level,
            personality=random.randint(base_stat, base_stat + 20), 
            luck=random.randint(base_stat - 10, base_stat + 5),
            level=self.level,
            gold=self.gold
        )
        
        race_mods = RACES.get(self.race, {}) 
        for attr, mod_val in race_mods.items():
            # Handle primary attributes
            if attr.endswith("_mod") and hasattr(self.stats, attr.replace("_mod","")):
                 stat_name = attr.replace("_mod","")
                 setattr(self.stats, stat_name, getattr(self.stats, stat_name) + mod_val)
            # Handle resistances
            elif attr.endswith("_resist") and hasattr(self.stats, attr):
                 setattr(self.stats, attr, getattr(self.stats, attr) + mod_val)
            # Handle direct magicka bonus (e.g. Altmer)
            elif attr == "magicka_mod" and hasattr(self.stats, "max_magicka"): # Max Magicka specifically
                self.stats.max_magicka += mod_val
            # Handle skill bonuses if NPC skills are detailed enough
            elif attr.endswith("_skill") and isinstance(self.skills, dict):
                skill_name = attr.replace("_skill","")
                self.skills[skill_name] = self.skills.get(skill_name, 10) + mod_val # Add to base or existing


        # Recalculate derived stats after all modifications
        self.stats.max_health = 75 + (self.stats.endurance * 2) + (self.level * 5) 
        self.stats.max_magicka = self.stats.max_magicka if race_mods.get("magicka_mod") else (40 + int(self.stats.intelligence * 1.5) + (self.level * 3)) # Apply magicka_mod correctly
        self.stats.max_fatigue = 80 + int(self.stats.endurance * 1.5) + (self.level * 4)
        self.stats.current_health = self.stats.max_health
        self.stats.current_magicka = self.stats.max_magicka
        self.stats.current_fatigue = self.stats.max_fatigue

        # --- Skills Initialization (As previously defined) ---
        self.skills = {} 
        role_l = self.role.lower()
        if any(s_role in role_l for s_role in ["mage", "scholar", "priest", "shaman", "necromancer", "cultist", "healer"]):
            self.skills["destruction"] = random.randint(15, 30) + self.level * 2
            self.skills["restoration"] = random.randint(15, 30) + self.level * 2
            self.skills["alteration"] = random.randint(10, 25) + self.level
            self.skills["conjuration"] = random.randint(10, 25) + self.level if "mage" in role_l or "necromancer" in role_l else 5
            self.skills["illusion"] = random.randint(10, 20) + self.level if "mage" in role_l or "illusionist_role" in role_l else 5
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
            self.skills["one_handed"] = random.randint(15,25) + self.level # Daggers/short swords
            if "pickpocket" in role_l : self.skills["pickpocket"] = random.randint(25,40) + self.level * 2
        else: 
            self.skills["speech"] = random.randint(10, 30) + self.level 
            self.skills[random.choice(["one_handed", "archery"])] = random.randint(5,15) + self.level # Basic self-defense
        # Add racial skill bonuses after general role assignment
        for skill_key, bonus_value in race_mods.items():
            if skill_key.endswith("_skill"):
                actual_skill_name = skill_key.replace("_skill", "")
                self.skills[actual_skill_name] = self.skills.get(actual_skill_name, 5) + bonus_value # Add to existing or a base of 5


        self.inventory = self.stats.inventory 
        self.equipment = [] 
        self.status_effects = [] 

        self.tags = {}
        self.add_tag("npc", "role_primary", self.role) # Using "role_primary" to avoid conflict with "class" if used differently
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
        
        if attitude != "hostile":
            if self.disposition >= 70:
                return random.choice(base_greetings["friendly"] + ["The gods smile upon this meeting!", "May your roads lead you to warm sands."])
            elif self.disposition >= 30:
                return random.choice(base_greetings["neutral"] + ["Need something?", "Speak if you must."])
            else: 
                return random.choice(["Hmph.", "Don't waste my time.", "What is it now?"])
        else: 
            return random.choice(base_greetings["hostile"])

    def _generate_purpose(self):
        role_lower = self.role.lower()
        # This can be greatly expanded with more specific flavor text per role
        if "merchant" in role_lower: return random.choice(["am here to trade fine goods.", "offer the best prices in this hold.", "seek to make a profit, of course."])
        elif "guard" in role_lower: return random.choice(["am keeping the peace.", "protect this place and its people.", "am on duty, move along."])
        elif "farmer" in role_lower or "farm_hand" in role_lower: return random.choice(["tend to my crops.", "work this land from dawn till dusk.", "pray for a good harvest this year."])
        elif "innkeeper" in role_lower: return random.choice(["run this fine establishment.", "offer a warm bed and a hot meal to weary travelers.", "hear many tales, some true, some not so much."])
        elif "bard" in role_lower: return random.choice(["share songs and stories of old.", "bring a little light into this world with my music.", "seek inspiration for my next great ballad."])
        elif "scholar" in role_lower or "mage" in role_lower: return random.choice(["delve into ancient lore and forgotten secrets.", "study the mysteries of Aetherius and Oblivion.", "seek knowledge above all else, for knowledge is power."])
        elif "priest" in role_lower or "healer" in role_lower or "acolyte" in role_lower: return random.choice(["serve the Divines and their will.", "offer comfort and healing to the needy and the sick.", "guide the lost and protect the faithful from darkness."])
        elif "hunter" in role_lower: return random.choice(["track game in the wilds to provide for my kin.", "know these lands like the back of my hand, every stream and shadow.", "live by the bow and the quiet footfall."])
        elif "miner" in role_lower: return random.choice(["toil in the depths for ore and precious gems.", "seek riches beneath the stone, hoping for a lucky strike.", "earn my keep with the sweat of my brow and the swing of my pickaxe."])
        elif any(s_role in role_lower for s_role in ["adventurer", "warrior", "mercenary", "companion", "explorer"]): return random.choice(["seek fortune and glory wherever they may be found.", "live by my blade and my wits.", "am always ready for a new challenge or a worthy cause."])
        elif any(s_role in role_lower for s_role in ["bandit", "thief", "forsworn"]): return random.choice(["take what this land owes me.", "believe this world is for the taking.", "survive by my own rules."]) # Usually hostile, but for context
        else: return random.choice(["live my life as best I can in these trying times.", "am just trying to get by, same as anyone.", "mind my own affairs mostly, if you please.", "have my duties to attend to, like everyone else."])

    def share_rumor(self, current_location) -> None:
        if self.disposition < 35:
            UI.slow_print(f"“{random.choice(['I have no time for idle gossip.', 'Find someone else to bother with your trivial questions.'])}”")
            return

        rumor_flavor_key = random.choice(TAGS.get("DIALOGUE", {}).get("topic", ["gossip"])) 
        
        rumor_text = None
        # Prioritize location-specific rumors if flavor.py supports it
        if hasattr(flavor, 'LOCATION_RUMORS') and isinstance(flavor.LOCATION_RUMORS, dict):
            loc_tags = current_location.get("tags", [])
            for tag in loc_tags:
                if tag in flavor.LOCATION_RUMORS:
                    possible_rumors = flavor.LOCATION_RUMORS[tag]
                    if possible_rumors:
                        rumor_text = random.choice(possible_rumors)
                        break
        
        # Fallback to general or topic-based rumors
        if not rumor_text and hasattr(flavor, 'RUMORS') and isinstance(flavor.RUMORS, dict):
            possible_rumors = flavor.RUMORS.get(rumor_flavor_key, [])
            if not possible_rumors and rumor_flavor_key != "gossip": 
                possible_rumors = flavor.RUMORS.get("gossip", [])
            if possible_rumors:
                rumor_text = random.choice(possible_rumors)
        
        if rumor_text:
            prefix = random.choice(["I overheard someone saying that ", "Word around here is ", "Can you believe that ", "They say that ", "Whispers on the wind suggest "])
            UI.slow_print(f"“{prefix}{rumor_text}”")
        else: 
            loc_name = current_location.get('name', 'this area')
            generic_rumors = [
                f"something strange is stirring in the {random.choice(['old ruins', 'deep caves', 'dark woods'])} not far from {loc_name}.",
                f"the Jarl of {random.choice(['a neighboring hold', loc_name if 'city' in current_location.get('tags',[]) else 'the capital'])} is planning some new decree.",
                f"a new band of {random.choice(['adventurers', 'mercenaries', 'troublemakers'])} just passed through {loc_name}, heading towards the {random.choice(['mountains', 'coast', 'border'])}.",
                f"the price of {random.choice(['ale', 'iron ingots', 'fresh bread', 'healing potions'])} is {random.choice(['going up again', 'surprisingly fair lately'])} in {loc_name}."
            ]
            UI.slow_print(f"“{random.choice(generic_rumors)}”")

    def dialogue(self, player, current_location) -> None:
        UI.clear_screen()
        UI.slow_print(f"You approach {self.name} ({self.role.replace('_',' ').capitalize()}). Disposition: {self.disposition}")
        UI.slow_print(f"“{self.greeting} {self.purpose}”")
        
        options_texts = ["Rumors", "Ask about their work/purpose", "Discuss this place", "Any tasks for me? (Quest)", "Farewell"]

        while True:
            UI.print_menu(options_texts) 
            choice_input = UI.print_prompt("Your response? (Enter number)").strip()

            if not choice_input.isdigit():
                UI.slow_print("Please enter a valid number for your choice.")
                UI.press_enter()
                continue
            
            choice_idx = int(choice_input)

            action_taken = False
            if choice_idx == 1:
                self.share_rumor(current_location)
                action_taken = True
            elif choice_idx == 2:
                UI.slow_print(f"“As I said, I {self.purpose}”")
                if self.disposition > 60 and "merchant" in self.role.lower() :
                    UI.slow_print(f"“Perhaps you're looking to buy or sell, {player.name}? I have a few things that might interest you, or I might be interested in what you carry.”")
                elif self.disposition > 55 and "guard" in self.role.lower():
                    UI.slow_print(f"“Just try to stay out of trouble. That makes my job easier.”")
                action_taken = True
            elif choice_idx == 3:
                loc_name = current_location.get("name", "this place")
                loc_tags = current_location.get("tags", [])
                place_description = f"Ah, {loc_name}..."
                
                comments = []
                if "city" in loc_tags: comments.append("It's a major hub, always something happening, for better or worse.")
                if "town" in loc_tags: comments.append("A decent enough place. Quieter than the big cities, which suits some folk.")
                if "village" in loc_tags: comments.append("A small, tight-knit community. We look out for each other here.")
                if "capital" in loc_tags: comments.append("The heart of the Hold, you know. All important matters pass through here.")
                if "port" in loc_tags: comments.append("The sea brings trade and travelers, but also its share of trouble.")
                if "farm" in loc_tags or "farming" in loc_tags : comments.append("Good, honest work to be done on the land here, if you've the stomach for it.")
                if "mine" in loc_tags: comments.append("Rich veins around here, if you're not afraid of the dark and a bit of hard work... or what lurks below.")
                if "forest" in loc_tags: comments.append("The woods are ancient and deep. Beautiful, but they hide their dangers well.")
                if "mountain" in loc_tags: comments.append("The peaks watch over us. Harsh, but a stark beauty to them.")
                if "ruin" in loc_tags or "barrow" in loc_tags: comments.append("Best to stay clear of such places. Old stones hide old sorrows... and sometimes worse.")
                if "tavern" in loc_tags or "inn" in loc_tags: comments.append("A good place to rest your feet, share a drink, and hear the latest news... or tall tales.")
                if "shop" in loc_tags or "market" in loc_tags: comments.append("You can find most anything you need, if you've the coin.")

                if comments:
                    place_description += " " + random.choice(comments)
                else:
                    place_description += " It is what it is. Not much else to say about it, really."
                UI.slow_print(f"“{place_description}”")
                action_taken = True
            elif choice_idx == 4:
                action_taken = True
                if self.has_offered_quest:
                    UI.slow_print(f"“{random.choice(['I have no other tasks for you right now, traveler.', 'Perhaps another time, I have nothing suitable for your skills.'])}”")
                elif random.random() > 0.7: 
                    UI.slow_print(f"“{random.choice(['I appreciate the offer, but I have nothing that needs doing at the moment.', 'All is quiet on my end, thankfully.'])}”")
                    self.has_offered_quest = True 
                else:
                    quest = generate_location_appropriate_quest(player.level, current_location.get("tags", []))
                    if not quest: 
                        UI.slow_print("“I thought I had something... but it seems to have slipped my mind. Apologies.”")
                        self.has_offered_quest = True
                    else:
                        UI.slow_print(f"“{random.choice(['Indeed, there is something you could assist me with.', 'Hmm, perhaps your skills could be of use...'])}”")
                        UI.print_line('-')
                        UI.print_info(f"Quest: {quest.title}")
                        UI.print_info(f"Objective: {quest.description}")
                        
                        reward_parts = []
                        if isinstance(quest.reward, dict):
                            for r_type, r_value in quest.reward.items():
                                if isinstance(r_value, Item): 
                                    reward_parts.append(f"{r_value.name} ({r_value.category.capitalize()})")
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
                                if hasattr(player, 'quest_log') and player.quest_log is not None:
                                    player.quest_log.add_quest(quest)
                                    UI.slow_print(f"“Excellent! I knew I could count on you, {player.name}. The details are in your journal.”")
                                    self.disposition = min(100, self.disposition + random.randint(3, 7)) 
                                else: 
                                    UI.slow_print("“I would give you the task, but it seems you have no way to record it. A pity.”")
                                self.has_offered_quest = True 
                                break
                            elif quest_action_prompt == "2": 
                                UI.slow_print(f"“{random.choice(['A pity. I had hoped for assistance.', 'Very well. The task will fall to another, then.', 'Understandable. Not all are suited for such endeavors.'])}”")
                                self.disposition = max(0, self.disposition - random.randint(1, 4)) 
                                self.has_offered_quest = True 
                                break
                            elif quest_action_prompt == "3": 
                                UI.slow_print(f"“{random.choice(['As you wish. The opportunity may not last indefinitely.', 'Do not tarry too long if you intend to help.', 'Consider it, then. But time is often a factor.'])}”")
                                self.has_offered_quest = True 
                                break
                            else:
                                UI.slow_print("A clear answer is expected, traveler.")
            
            elif choice_idx == 5:
                UI.slow_print(f"“{random.choice(['Farewell, traveler.', 'May your path be clear.', 'Until next time.'])}”")
                return
            else:
                UI.slow_print("Your will wavers, or the choice is unclear.")
            
            if action_taken:
                UI.press_enter()
                UI.clear_screen()
                UI.slow_print(f"You are speaking with {self.name}. Disposition: {self.disposition}") 
                UI.slow_print(f"“{self.greeting} {self.purpose}”")