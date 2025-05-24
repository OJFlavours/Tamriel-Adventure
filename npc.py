import random
from stats import Stats
from items import generate_random_item
from tags import TAGS, RUMOR_POOL, FLAVOR_VIGNETTES
from ui import UI
from quests import generate_location_appropriate_quest

# Define roles that imply noble or commoner status
NOBLE_ROLES = {"noble", "jarl", "thane", "baron", "lady", "duke", "duchess"}
COMMONER_ROLES = {"merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer", "innkeeper", "bard", "bandit", "thief", "vampire", "forsworn", "necromancer"}
# Backwards-compatible friendly/hostile role sets
HOSTILE_ROLES = {"bandit", "necromancer", "vampire", "forsworn", "thief"}
FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES)

# Name pools for main Skyrim races, with separate noble and commoner lists
NAME_POOLS = {
    "nord": {
        "noble": {
            "male": ["Ulfric", "Torvald", "Jarlson", "Rolfrick", "Stahlund"],
            "female": ["Brynhild", "Elfarra", "Sofira", "Hildrun", "Thyra"]
        },
        "commoner": {
            "male": ["Ragnar", "Bjorn", "Sven", "Eirik", "Sigurd"],
            "female": ["Astrid", "Freya", "Ylva", "Ingrid", "Solveig"]
        }
    },
    "imperial": {
        "noble": {
            "male": ["Septimus", "Octavian", "Cassius", "Marcellus", "Tiberius"],
            "female": ["Octavia", "Aurelia", "Cornelia", "Vibia", "Domitia"]
        },
        "commoner": {
            "male": ["Marcus", "Cassian", "Darius", "Gaius", "Lucius"],
            "female": ["Livia", "Sabina", "Claudia", "Marina", "Valeria"]
        }
    },
    "breton": {
        "noble": {
            "male": ["Darius", "Lucien", "Ademar", "Corbin", "Roland"],
            "female": ["Brienne", "Fiona", "Isabeau", "Sibylle", "Camille"]
        },
        "commoner": {
            "male": ["Alain", "Benoit", "Claude", "Etienne", "Gaston"],
            "female": ["Amelie", "Cecile", "Elise", "Marie", "Sabine"]
        }
    },
    "dunmer": {
        "noble": {
            "male": ["Nerath", "Voryn", "Ravyn", "Drovas", "Serethi"],
            "female": ["Aranea", "Brelyna", "Mehra", "Visenya", "Drana"]
        },
        "commoner": {
            "male": ["Adril", "Beryn", "Feryn", "Garyn", "Llevule"],
            "female": ["Dratha", "Eldrin", "Faryna", "Ienith", "Milore"]
        }
    },
    "altmer": {
        "noble": {
            "male": ["Saerendil", "Elenwen", "Therion", "Faelwen", "Adalind"],
            "female": ["Calia", "Sylendra", "Myrrha", "Ondree", "Thuul"]
        },
        "commoner": {
            "male": ["Ancarion", "Eaigle", "Fathras", "Ilmali", "Lloran"],
            "female": ["Aevarrel", "Fayeth", "Lunwara", "Ylesius", "Venya"]
        }
    },
    "dwemer": {
        "noble": {
            "male": ["Kagrenac", "Dumac", "Nherit", "Vharnan", "Uleran"],
            "female": ["Modryn", "Siglina", "Eldara", "Thoryn", "Diveth"]
        },
        "commoner": {
            "male": ["Bzukle", "Nchardum", "Imdur", "Vulzun", "Fenram"],
            "female": ["Trobri", "Lurind", "Solgrun", "Yzgara", "Uthurra"]
        }
    },
    "orc": {
        "noble": {
            "male": ["Ghorbash", "Mogrosh", "Dhargosh", "Krahl", "Urzgu"],
            "female": ["Durga", "Khazgra", "Sharngra", "Yashgra", "Othog"]
        },
        "commoner": {
            "male": ["Lashaj", "Uzgash", "Zoklak", "Shraug", "Ghruv-zok"],
            "female": ["Bela", "Guldur", "Mogrim", "Krusk", "Nulgra"]
        }
    },
    "khajiit": {
        "noble": {
            "male": ["J'zargo", "Ra'zirr", "Ma'randru-jo", "S'rendarr", "K'rajn"],
            "female": ["Ayrenn", "Zahra", "S'randarr", "Khansha", "Drala"]
        },
        "commoner": {
            "male": ["Kharjo", "J'Khajiit", "J'Zaran", "M'raaj-Dar", "S'rrex"],
            "female": ["Kerah", "Daro'Vas", "Nivrel", "Ziera", "Ma'shara"]
        }
    },
    "argonian": {
        "noble": {
            "male": ["Teezhar", "Shazrune", "Iizashi", "Xhal-Jir", "Rees-Ja"],
            "female": ["Sa-Sara", "Jasreet", "H'Ra", "Ti'Green", "Mala-Ja"]
        },
        "commoner": {
            "male": ["Ra'zirr", "X-Tso", "Uxith'reth", "Sithis-Tza", "Pelur-Ja"],
            "female": ["Ti'Step", "Ib-Tet", "Oggra", "Wee-Gas", "Sisithis"]
        }
    },
    "redguard": {
        "noble": {
            "male": ["Samid", "Khamir", "Nadir", "Aramir", "Rashid"],
            "female": ["Amirah", "Layla", "Zafira", "Riyana", "Tahlia"]
        },
        "commoner": {
            "male": ["Niruin", "Al-Nir", "Fahir", "Rashad", "Zahir"],
            "female": ["Salma", "Yamila", "Hafiza", "Laila", "Mina"]
        }
    },
    "bosmer": {
        "noble": {
            "male": ["Rajh", "Miner Gray-Mane", "Faendal", "Fane", "Sharuil"],
            "female": ["Leshra", "Shaeli", "Sathorys", "Brya", "Laina"]
        },
        "commoner": {
            "male": ["Sanos", "Ilo", "Travo", "Ruil", "Auson"],
            "female": ["Aeri", "Raen", "Ramil", "Fela", "Cesina"]
        }
    },
}


class NPC:
    def __init__(self, name=None, level=1, culture_tag="nord", role_tag="commoner", gender=None):
        self.culture_tag = culture_tag
        self.role_tag = role_tag
        # Determine social status by role
        self.social_status = "Noble" if role_tag in NOBLE_ROLES else "commoner"
        
        self.level = level
        self.gender = gender or random.choice(["male", "female"])
        self.name = name or self.generate_name()
        self.stats = self.generate_stats()
        self.skills = self.generate_skills()
        self.alignment = self.determine_alignment()
        self.equipment = self.generate_equipment()
        self.disposition = random.randint(30, 70)
        self.told_rumor = False
        self.greeting = self._generate_greeting()
        self.purpose = self._generate_purpose()
        self.farewell = self._generate_farewell()

    def determine_alignment(self) -> str:
        if self.role_tag in HOSTILE_ROLES:
            return "hostile"
        if self.role_tag in FRIENDLY_ROLES:
            return "friendly"
        return "neutral"

    def generate_name(self) -> str:
        pool = NAME_POOLS.get(self.culture_tag, {})
        status_key = "noble" if self.social_status == "Noble" else "commoner"
        nameset = pool.get(status_key, pool.get("commoner", {}))
        gender_list = nameset.get(self.gender, ["Unknown"])
        return random.choice(gender_list)

    def generate_stats(self) -> Stats:
        return Stats(
            strength=random.randint(30, 50), intelligence=random.randint(30, 50),
            willpower=random.randint(30, 50), agility=random.randint(30, 50),
            speed=random.randint(30, 50), endurance=random.randint(30, 50),
            personality=random.randint(30, 50), luck=random.randint(30, 50)
        )

    def generate_skills(self) -> dict:
        base = {s:15 for s in ["blade","blunt","hand_to_hand","armorer","block",
                                 "heavy_armor","athletics","alchemy","alteration",
                                 "conjuration","destruction","illusion","mysticism",
                                 "restoration","acrobatics","light_armor","marksman",
                                 "mercantile","security","sneak","speechcraft"]}
        if self.role_tag in ["bandit","warrior"]:
            for sk in ["blade","blunt","heavy_armor"]: base[sk]+=10
        if self.role_tag in ["mage","necromancer"]:
            for sk in ["destruction","conjuration","mysticism"]: base[sk]+=10
        if self.role_tag=="thief":
            for sk in ["sneak","security","light_armor"]: base[sk]+=10
        return base

    def generate_equipment(self) -> list:
        eq=[]
        if self.alignment=="hostile":
            eq.append(generate_random_item("weapon",self.level))
            eq.extend(generate_random_item("armor",self.level) for _ in range(2))
        else:
            eq.append(generate_random_item("armor",self.level))
            if self.role_tag in {"merchant","blacksmith","noble","jarl","thane"}:
                eq.append(generate_random_item("weapon",self.level))
        return eq

    def is_alive(self) -> bool:
        return self.stats.is_alive()

    def __str__(self) -> str:
        align = "hostile" if self.alignment=="hostile" else "friendly"
        return f"{self.name}, a {align} {self.culture_tag} {self.role_tag}"

    def _generate_greeting(self) -> str:
        gm={
            "merchant":"Hail, traveler! My wares are the finest in the land.",
            "guard":"State your business, or move along.",
            "bandit":"Your coin or your life, stranger!",
            "priest":"The Divines smile upon us this day.",
            "blacksmith":"Need a blade sharpened or armor mended?",
            "innkeeper":"Welcome! A warm bed and hearty meal await.",
            "bard":"A song for your travels, friend?",
            "noble":"Ah, a person of renown graces me!",
            "jarl":"By the authority of my hold, state your purpose!"
        }
        return gm.get(self.role_tag, "Greetings, wanderer.")

    def _generate_purpose(self) -> str:
        pm={
            "merchant":"trade goods across Tamriel.",
            "healer":"mend the wounded with skill and care.",
            "blacksmith":"forge steel worthy of heroes.",
            "innkeeper":"offer respite to weary souls.",
            "bard":"weave tales that echo through time.",
            "bandit":"take what I please from the weak.",
            "thief":"slip through shadows for profit.",
            "noble":"serve my lineage with honor.",
            "jarl":"govern these lands with fairness and strength."
        }
        return pm.get(self.role_tag, "seek my fortune.")

    def _generate_farewell(self) -> str:
        fm={
            "merchant":"May your coin purse stay heavy.",
            "guard":"Keep the peace, traveler.",
            "bandit":"Cross my path again, and you’ll regret it.",
            "priest":"Walk with the Divines’ blessing.",
            "blacksmith":"May your steel never break.",
            "innkeeper":"Return when you need rest.",
            "bard":"Let our paths cross again in song.",
            "noble":"May your reputation precede you.",
            "jarl":"Go with the blessings of Skyrim."
        }
        return fm.get(self.role_tag, "Safe travels.")

    def share_random_rumor(self, current_location) -> None:
        if current_location and current_location["tags"]:
            rumors = RUMOR_POOL.get(current_location["tags"][0], ["A strange tale circulates..."])
        else:
            rumors = ["A strange tale circulates..."]
        rumor = random.choice(rumors)
        UI.slow_print(f"“Rumor has it: {rumor}”")

    def dialogue(self, player, current_location) -> None:
        UI.slow_print(f"You approach {self}. Disposition: {self.disposition}")
        UI.slow_print(f"“{self.greeting} I {self.purpose}”")
        options=["Rumor","Work","This Place","Quest","Farewell"]
        while True:
            for i,opt in enumerate(options,1): print(f"[{i}] {opt}")
            choice=input("Choose: ")
            if choice=="1":
                if not self.told_rumor:
                    self.share_random_rumor(current_location)
                    self.told_rumor=True
                else:
                    UI.slow_print("“I’ve shared all I know.”")
            elif choice=="2": UI.slow_print(f"“I {self.purpose}”")
            elif choice=="3":
                vigs=[FLAVOR_VIGNETTES.get(tag) for tag in current_location.get("tags",[])]
                vigs=[random.choice(v) if isinstance(v,list) else v for v in vigs if v]
                UI.slow_print(f"“{random.choice(vigs) if vigs else 'Just another place.'}”")
            elif choice=="4":
                quest=generate_location_appropriate_quest(player.level,current_location.get("tags",[]))
                UI.slow_print(f"“{quest.description} Reward: {quest.reward}”")
                player.quest_log.add_quest(quest)
            elif choice=="5":
                UI.slow_print(f"“{self.farewell}”")
                break
            else: UI.slow_print("“Pardon?”")