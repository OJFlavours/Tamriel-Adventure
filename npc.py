# npc.py
import random
from stats import Stats, RACES
from items import Item
from ui import UI # Import UI for capitalization and debug messages
# Import Quest and generate_location_appropriate_quest from quests.py
from quests import Quest, generate_location_appropriate_quest, QuestLog, process_quest_rewards
from tags import TAGS, get_tags
import flavor
from exploration_data import EXPLORATION_RESULTS # Needed if NPCs can provide specific exploration hints
from rumors import generate_rumor # for generating rumors in NPC dialogue

# Define roles that imply noble or commoner status (from original)
NOBLE_ROLES = {"noble", "jarl", "thane", "baron", "lady", "duke", "duchess", "court_mage", "advisor"}
COMMONER_ROLES = {
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand", "local",
    "stormcloak_supporter", "imperial_citizen", "mage_apprentice", "warrior", "companion_warrior",
    "new_blood", "circle_member", "thief_lookout", "pickpocket", "guild_rogue", "db_initiate",
    "explorer", "sailor", "dock_worker", "ship_captain_ashore", "fishmonger", "acolyte", "temple_guardian",
    "stall_owner", "shop_assistant", "city_guard_patrolling", "mine_foreman", "farmer_spouse"
}

# Define roles that are typically hostile (from original)
HOSTILE_ROLES = {
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "vampire", "vampire_thrall", "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thief_hostile",
    "draugr_restless", "skeleton_warrior", "ghost_ancient",
    "cave_bear_young", "wolf_alpha", "giant_spider_cave",
    "dwarven_sphere_guardian", "falmer_warrior", "chaurus_hunter_small",
    "mage_hostile", "cultist", "thalmor_justiciar" # Added thalmor_justiciar
}
FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES

# Expanded NAME_POOLS dictionary for npc.py
NAME_POOLS = {
    "nord": {
        "noble": {
            "male": ["Ulfric", "Torvald", "Jarlson", "Rolfrick", "Stahlund", "Brynjolf", "Kodlak", "Skjor", "Galmar", "Harkon", "Vignar", "Balgruuf", "Korir", "Thongvor", "Dengeir", "Siddgeir", "Igmund", "Arngeir"],
            "female": ["Brynhild", "Elfarra", "Sofira", "Hildrun", "Thyra", "Laila", "Astrid", "Elisif", "Maven", "Rikke", "Freyja", "Ingjard", "Idgrod", "Skald", "Frida", "Jonna", "Miraak"],
            "noble_surnames": ["Stormblade", "Ice-Veins", "Iron-Hand", "Snow-Strider", "Winter-Kissed", "Silver-Blood", "Ravencrone", "Black-Briar", "Sky-Born", "Frost-Beard"]
        },
        "commoner": {
            "male": ["Ragnar", "Bjorn", "Sven", "Eirik", "Sigurd", "Hadvar", "Ralof", "Vilkas", "Farkas", "Stenvar", "Benor", "Cosnach", "Vorstag", "Hod", "Torvar", "Athis", "Njada", "Ria", "Skuli", "Torsten"],
            "female": ["Astrid", "Freya", "Ylva", "Ingrid", "Solveig", "Gerdur", "Sigrid", "Mjoll", "Lydia", "Uthgerd", "Annekke", "Sylgja", "Temba", "Hroki", "Hilde", "Gunmar", "Aela", "Jorunn", "Bodil", "Greta"],
            "commoner_surnames": ["Battle-Born", "Gray-Mane", "Shatter-Shield", "Cruel-Sea", "Icestorm", "Snow-Shod", "Oath-Breaker", "Stone-Fist", "Winter-Heart", "Rime-Gazer", "Wind-Caller", "Snow-Hammer", "War-Bear", "Ice-Shield", "Rune-Carver", "Sky-Singer"]
        }
    },
    "imperial": {
        "noble": {
            "male": ["Titus", "Valerius", "Cassius", "Hadrian", "Septimus", "Tullius", "Proventus", "Quentin", "Maro", "Atticus", "Lucan", "Vittorio", "Caius", "Marcellus", "Flavius", "Aventus"],
            "female": ["Serana", "Valeria", "Aurelia", "Livia", "Octavia", "Rikke", "Vittoria", "Elissia", "Claudia", "Antonia", "Marcia", "Aeliana", "Flavia", "Cornelia", "Licinia"],
            "noble_surnames": ["Antonius", "Aurelius", "Julianos", "Valerius", "Platorius", "Flavius", "Aventus", "Septim", "Cosades", "Caecilius"]
        },
        "commoner": {
            "male": ["Gaius", "Marcus", "Tiber", "Lucius", "Rufus", "Marcurio", "Belrand", "Severio", "Amaund", "Quintus", "Adrian", "Silus", "Festus", "Pavo", "Nura", "Vinius"],
            "female": ["Claudia", "Julia", "Fausta", "Silvia", "Vespasia", "Carlotta", "Wilmuth", "Herminia", "Gisli", "Alessia", "Camilla", "Lucia", "Sabina", "Minerva", "Petra"],
            "commoner_surnames": ["Licinius", "Sextius", "Cassia", "Vitellia", "Servilius", "Pomponius", "Atius", "Livius", "Pelagia", "Vesuius", "Valentius", "Cinna"]
        }
    },
    "breton": {
        "noble": {
            "male": ["Gaston", "Didier", "Armand", "Guillaume", "Thierry", "Farengar", "Ainethach", "Gallus", "Mercer", "Alain", "Etienne", "Tristan", "Jorunn", "Roland", "Benoit"],
            "female": ["Genevieve", "Isabelle", "Marguerite", "Annette", "Elodie", "Sybille", "Tonilia", "Muiri", "Lisette", "Vivienne", "Cecile", "Aurore", "Giselle", "Madeleine", "Seraphine"],
            "noble_surnames": ["Gardner", "Lirielle", "Montclair", "Beaufort", "Tournel", "Jurard", "Secret-Fire", "Ravencourt", "Daggerfall", "Evermore"]
        },
        "commoner": {
            "male": ["Pierre", "Jean", "Louis", "François", "Antoine", "Belethor", "Enthir", "Delvin", "Orthus", "Pascal", "Luc", "Mathieu", "Claude", "Remy", "Sebastien", "Michel"],
            "female": ["Marie", "Sophie", "Jeanne", "Claire", "Nicole", "Colette", "Ysolda", "Lisbet", "Sorine", "Amelie", "Brigitte", "Eloise", "Laurentia", "Celeste", "Valerie"],
            "commoner_surnames": ["Mallory", "Endario", "Marence", "Jurard", "Bourne", "Camroic", "Corvus", "Duclair", "Ervine", "Giraud", "Hervier", "Jarnet", "Bisset", "Leclair", "Fontaine"]
        }
    },
    "redguard": {
        "noble": {
            "male": ["Ahmad", "Jamal", "Khalid", "Rashid", "Zafir", "Isran", "Nazir", "Sayyid", "Kematu", "A'tor", "Hassim", "Tariq", "Malik", "Ibrahim", "Yusuf"],
            "female": ["Zafira", "Yasmina", "Samira", "Layla", "Aisha", "Iman", "Anora", "Rayya", "Faleen", "Nura", "Fatima", "Amira", "Safiya", "Lamia", "Zahra"],
            "noble_surnames": ["A'tor", "Suhail", "Nooria", "Lirielle", "Alik'r", "Crownblade", "Yokuda", "Sandwalker"]
        },
        "commoner": {
            "male": ["Cyrus", "Nazir", "Kematu", "Sadir", "Malik", "Nazeem", "Brenuin", "Revus", "Ahlam", "Hassan", "Omar", "Jalal", "Faris", "Karim", "Salih"],
            "female": ["Imani", "Sana", "Nadia", "Zara", "Amina", "Saadia", "Shiri", "Safia", "Umana", "Laila", "Halima", "Rania", "Jamila", "Soraya", "Mina"],
            "commoner_surnames": ["al-Sadun", "al-Nasir", "al-Hassan", "al-Mansur", "ibn-Faris", "ibn-Jafari", "al-Hakim", "ibn-Zahra", "al-Nur", "Salih", "Kazim", "Habib", "Al-Din", "Ibn-Zahir", "Sand-Singer"]
        }
    },
    "dunmer": {
        "noble": {
            "male": ["Nerevar", "Drathis", "Aryon", "Aralen", "Othral", "Neloth", "Savos", "Jiub", "Adril", "Brandyl", "Theryn", "Voryn", "Falen", "Ravyn", "Galyn"],
            "female": ["Morwen", "Fjola", "Jenassa", "Brelyna", "Aranea", "Karliah", "Irileth", "Lythandas", "Vendil", "Almalexia", "Drasa", "Selveni", "Vevrana", "Nisswo", "Milore"],
            "noble_surnames": ["Indoril", "Redoran", "Telvanni", "Dres", "Hlaalu", "Sadras", "Sotha", "Dagoth", "Morag", "Veloth"]
        },
        "commoner": {
            "male": ["Brand-Shei", "Revyn", "Adril", "Malborn", "Erandur", "Romlyn", "Tythis", "Garyn", "Belyn", "Fethis", "Drovas", "Talen", "Ralen", "Velyn", "Nerano"],
            "female": ["Jenassa", "Fethis", "Mogrul", "Nilene", "Brelyna", "Suvaris", "Dravynea", "Avrusa", "Mirri", "Eldrin", "Selvura", "Nirya", "Vaynelle", "Idesa", "Talmoro"],
            "commoner_surnames": ["Sadri", "Arano", "Dreth", "Ulen", "Ienth", "Hlaalu", "Alor", "Atheron", "Sarethi", "Severin", "Hulren", "Maryon", "Stoneweaver", "Ravani", "Telvayn"]
        }
    },
    "altmer": {
        "noble": {
            "male": ["Ancano", "Ondolemar", "Rulindil", "Estormo", "Vingalmo", "Naarifin", "Mannimarco", "Quaranir", "Ocato", "Alandro", "Calindil", "Tandilwe", "Lorcalin", "Faelar", "Eldrin"],
            "female": ["Elenwen", "Niranye", "Taarie", "Linwe", "Alwinarwe", "Ayrenn", "Nalime", "Celmire", "Liriel", "Arandil", "Sinderion", "Valinwe", "Elanwe", "Merildor", "Alandra"],
            "noble_surnames": ["Sunweaver", "Goldenshine", "Starbloom", "Highborn", "Dawnstrider"]
        },
        "commoner": {
            "male": ["Faralda", "Calcelmo", "Enthir", "Runil", "Aicantar", "Nelacar", "Nirya", "Orthorn", "Melaran", "Falion", "Taurion", "Vinglor", "Nelandil", "Sanyon", "Eldrin"],
            "female": ["Endarie", "Vivienne", "Fasendil", "Nenya", "Atahba", "Minette", "Lirien", "Saliache", "Alandra", "Celmine", "Tindoria", "Merethil", "Valerwe", "Nalanya", "Elandra"]
        }
    },
    "bosmer": {
        "noble": {
            "male": ["Faelan", "Niruin", "Borvir", "Maluril", "Orion", "Aengoth", "Glavis", "Cuinanthil", "Faelar", "Thalindor", "Eldrin", "Balfiera", "Gwilinwe"],
            "female": ["Niruin", "Grelka", "Nimphaneth", "Caminda", "Eridor", "Finna", "Anori", "Lirien", "Selvyn", "Aralindel"],
            "noble_surnames": ["Greenleaf", "Woodshade", "Barkborn", "Vinesinger", "Forestwalker"]
        },
        "commoner": {
            "male": ["Faendal", "Anoriath", "Valindor", "Elrindir", "Ma'randru-jo", "Gwilin", "Eothram", "Pavo", "Thalindra", "Beron", "Faelar", "Cirdir", "Lorcalin"],
            "female": ["Nimrodel", "Gilfre", "Indara", "Ardwen", "Drynea", "Elrinde", "Lirienwe", "Celmine", "Anoriel", "Selvynia", "Faelindra", "Thalindra", "Vindrel"]
        }
    },
    "orc": {
        "noble": {
            "male": ["Ghorbash", "Urag", "Yashnag", "Burguk", "Larak", "Murob", "Gularzob", "Ogol", "Dushnamub", "Yamarz", "Gorzod", "Shuftharz", "Bazrag"],
            "female": ["Mogakh", "Shel", "Borba", "Batul", "Gharol", "Ugor", "Shuftharz", "Lashgra", "Bagrak", "Gul", "Atub", "Sharamph", "Urgarlag"],
            "noble_surnames": ["gro-Dushnikh", "gro-Shub", "gro-Yazguul", "gro-Bol", "gro-Largash", "gro-Batul", "gro-Bagol", "gra-Dushnikh", "gra-Yazguul", "gra-Uzg", "gra-Sharob", "gra-Lagash", "gra-Shamub", "gra-Larguk", "gro-Nar", "gro-Fel"]
        },
        "commoner": {
            "male": ["Grogmar", "Muzgonk", "Shagrol", "Urzog", "Yamorz", "Gat", "Oglub", "Durak", "Bazgrol", "Ulag", "Garoth", "Malkus", "Durgash"],
            "female": ["Urzoga", "Yatul", "Bagrak", "Gharol", "Uglarz", "Borgakh", "Dulug", "Lash", "Sharamph", "Gul", "Borzog", "Orzoga", "Murgol"],
            "commoner_surnames": ["gro-Burzag", "gro-Bulfim", "gro-Yarug", "gro-Shamub", "gro-Ghorak", "gro-Shargakh", "gro-Largashbur", "gra-Sharn", "gra-Lag", "gra-Lazga", "gra-Phorkh", "gra-Gasnouk", "the Steel Heart", "gra-Shug", "gro-Narzul", "gra-Bol"]
        }
    },
    "argonian": {
        "noble": {
            "male": ["Swims-in-Deep-Waters", "Hides-His-Eyes", "Chal-Ei", "Meer-Zish", "Raises-The-Spine", "Teeba-Ei", "Veezara", "Jaree-Ra", "From-His-Shell", "Walks-in-Darkness"],
            "female": ["From-Deepest-Fathoms", "Scales-of-Steel", "Druja", "Wanan-To", "Sheer-Meedish", "Pale-Heart-Washes", "Neetrenaza", "Waves-of-Dusk", "Sees-All-Colors", "Drinks-the-Tide"],
            "noble_surnames": ["of-the-Scales", "of-the-Swamp", "of-the-Hist", "Root-Walker", "Deep-Breather", "Shadow-Stalker"]
        },
        "commoner": {
            "male": ["Derkeethus", "Stands-In-Shadows", "Walks-Softly", "Madesi", "Talendri", "Beem-Ja", "Scouts-Many-Marshes", "Deep-In-His-Cups", "Haj-Ei", "Neet-Loh", "Reezus", "Jee-Lar", "Tsleeixth"],
            "female": ["Shahvee", "Keerava", "Deekus", "Wujeeta", "Reek-Neeus", "Gives-No-Fuss", "Watches-Waves", "Dives-Into-Reeds", "Sings-of-Stars", "Tail-of-Tides", "Bright-Throat"],
            "commoner_surnames": ["Reed-Runner", "Mud-Strider", "Stream-Swimmer", "Weed-Puller", "Egg-Watcher", "Creek-Digger"]
        }
    },
    "khajiit": {
        "noble": {
            "male": ["J'zargo", "Ma'iq", "Dro'marash", "Ra'virr", "Ri'saad", "Kharjo", "J'darr", "Ma'jhad", "Razum-dar", "Za'ji", "Jo'ran", "Ra'jirr", "Ka'zhar"],
            "female": ["Ahkari", "Razhinda", "Zaynabi", "Shavari", "Tsrava", "Ma'kara", "Atahbah", "Ri'zhaja", "Khali", "Shazara-Ta", "Tsabhi", "Ri'datta", "Za'jirra"],
            "noble_surnames": ["of-the- Sands", "of-the-Claw", "of-the-Dune", "Moon-Walker", "Star-Gazer", "Whisper-Wind"]
        },
        "commoner": {
            "male": ["M'aiq", "J'datharr", "Qa'jo", "Dro'shavir", "Kesh", "Vasha", "Ahjmal", "Zaymar", "Ra'khan", "Jo'dar", "S'jir", "Ma'zaka", "Ra'zhar"],
            "female": ["Shuravi", "Ra'kheran", "Dro'barri", "Tsrasuna", "Bahb-Bi", "S'kasha", "Ri'zala", "Za'darra", "Khayla", "S'rashi", "Ma'zabi", "Jo'vanni", "Ra'tesh"],
            "commoner_surnames": ["Sand-Runner", "Dune-Digger", "Moon-Singer", "Star-Weaver", "Claw-Sharpener", "Whisker-Twitch"]
        }
    },
    "undead_nord": {
        "noble": {
            "male": ["Ysgramor", "Torygg", "Ulfric", "Olaf", "Jurgen"],
            "female": ["Fura", "Ysmeine", "Hroki", "Ylva"],
            "noble_surnames": ["the-Restless", "of-the-Grave", "Frost-Bound", "Winter-Wail", "Iron-Shackle"]
        },
        "commoner": {
            "male": ["Olaf", "Jurgen", "Red Eagle", "Hrothgar", "Brynjar", "Sigurd", "Erlend"],
            "female": ["Hilda", "Ingrid", "Sigrun", "Freya", "Astrid"],
            "commoner_surnames": ["Grave-Walker", "Bone-Chiller", "Death-Caller", "Frost-Bringer", "Iron-Grasp"]
        }
    },
    "undead_skeleton": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Cursed Guardian", "Bone-Clatter Warrior", "Rattling Archer", "Skull-Sentry", "Withered Blade", "Dust-Warden"],
            "female": ["Decrepit Mage", "Bone-Sorceress", "Shattered Mystic", "Spectral Archer"],
            "commoner_surnames": ["Dust-Bringer", "Bone-Weaver", "Grave-Whisper", "Shadow-Claw", "Iron-Bone"]
        }
    },
    "spirit": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Fading Echo", "Wispmother's Attendant", "Shadowed Wraith", "Lost Wanderer", "Ethereal Guardian"],
            "female": ["Wailing Shade", "Lost Soul", "Mist-Warden", "Spectral Maiden", "Echoing Spirit"],
            "commoner_surnames": ["Mist-Walker", "Shadow-Singer", "Echo-Weaver", "Soul-Binder", "Ethereal-Grasp"]
        }
    },
    "falmer": {
        "noble": {
            "male": ["Nightprowler Alpha", "Gloomstalker Chieftain", "Shadowclaw Lord"],
            "female": ["Shadowseer Matriarch", "Chaurus-Queen", "Nightshade Oracle"],
            "noble_surnames": ["of-the-Deep", "of-the-Gloom", "Shadow-Binder", "Night-Caller", "Venom-Grasp"]
        },
        "commoner": {
            "male": ["Skulker Gloomdweller", "Chaurus-Tender Falmer", "Falmer Slave", "Blind Stalker", "Gloomlurker Scout"],
            "female": ["Chanter of the Depths", "Falmer Gloomlurker", "Shadowed Skulker", "Cave-Warden"],
            "commoner_surnames": ["Cave-Stalker", "Gloom-Weaver", "Deep-Whisper", "Shadow-Binder", "Venom-Spitter"]
        }
    },
    "dwemer_construct_race": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["CX-Series Guardian Unit 734", "Acutronic Spider MKIII", "Ballista Defense Unit 03", "Steam-Centurion Alpha", "Dwarven Enforcer 29", "Automatron Sentinel"],
            "female": [],
            "commoner_surnames": ["of-the-Gears", "of-the-Steam", "Iron-Clad", "Bronze-Shell", "Acutronic"]
        }
    },
    "wolf_creature": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Dire Wolf Alpha", "Ice Wolf Pack Leader", "Timber Wolf Veteran", "Frostfang Patriarch", "Shadowpelt Leader"],
            "female": ["Alpha Female Wolf", "Shadow Wolf Matriarch", "Snowfang Matron", "Moonhowl Mother"],
            "commoner_surnames": ["of-the-Pack", "Snow-Fang", "Shadow-Pelt", "Moon-Howler", "Timber-Claw"]
        }
    },
    "bear_creature": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Grizzled Cave Bear Patriarch", "Snow Bear Elder", "Giant Forest Bear", "Ironclaw Patriarch", "Frostfur Titan"],
            "female": ["Cave Bear Matriarch", "Protective Mother Bear", "Snowclaw Matron", "Great Ursine Queen"],
            "commoner_surnames": ["Cave-Claw", "Snow-Fur", "Forest-Walker", "Iron-Grasp", "Frost-Bringer"]
        }
    },
    "spider_creature": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Venomfang Broodfather", "Giant Frostbite Spider Patriarch", "Shadowweb Sire", "Toxic Broodlord"],
            "female": ["Venomfang Broodmother", "Ancient Frostbite Spider Queen", "Nightweb Matriarch", "Poisonspit Queen"],
            "commoner_surnames": ["Venom-Spitter", "Frost-Bite", "Shadow-Weaver", "Toxic-Bringer", "Night-Stalker"]
        }
    },
    "chaurus_creature": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Chaurus Reaper Prime", "Chaurus Hunter Alpha", "Tunneler Prime", "Venomclaw Alpha"],
            "female": ["Chaurus Queen", "Chitin Matriarch", "Burrower Queen"],
            "commoner_surnames": ["Chitin-Claw", "Tunnel-Weaver", "Venom-Spitter", "Reaper-Grasp", "Hunter-Stalker"]
        }
    },
    "thalmor_justiciar_interrogator": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Anoriath", "Estormo", "Rulindil", "Ondolemar"],
            "female": ["Elenwen", "Niranye", "Taarie", "Linwe"],
            "commoner_surnames": ["of-the- Dominion", "of-the-Thalmor", "of-the-Sun", "of-the-Stars", "of-the-Moon"]
        }
    },
    "khajiit_traveler_frightened": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["J'zargo", "Kharjo", "Ra'virr", "Ma'jhad"],
            "female": ["Ahkari", "Shavari", "Zaynabi", "Tsrava"],
            "commoner_surnames": ["of-the-Road", "of-the- Caravan", "of-the-Sands", "of-the-Dunes", "of-the-Moon"]
        }
    },
    "markarth_city_guard_general": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Degaine", "Raerek", "Thongvor", "Yngvar"],
            "female": ["Sondyne", "Rorlund", "Faleen", "Kerah"],
            "commoner_surnames": ["of-Markarth", "Silver-Blood", "Stone-Fist", "Iron-Grasp", "of-the-Reach"]
        }
    },
    "markarth_informant": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Eltrys", "Thongvor", "Nepos", "Betrid"],
            "female": ["Hroki", "Lisbet", "Muiri", "Frabbi"],
            "commoner_surnames": ["of-the-Shadows", "of-the-Whispers", "Stone-Ear", "Silver-Tongue", "of-the-Reach"]
        }
    },
    "ratway_fence": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Vex", "Delvin", "Brynjolf", "Cynric"],
            "female": ["Tonilia", "Dirge", "Niranye", "Sapphire"],
            "commoner_surnames": ["of-the-Ratway", "Shadow-Claw", "Silver-Tongue", "Iron-Grasp", "of-the-Thieves"]
        }
    },
    "markarth_jarl": {
        "noble": {
            "male": ["Igmund", "Thongvor"],
            "female": [],
            "noble_surnames": ["of-Markarth", "Silver-Blood", "Stone-Fist", "Iron-Grasp", "of-the-Reach"]
        },
        "commoner": {}
    },
    "falkreath_priest_arkay": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Runil", "Kust"],
            "female": [],
            "commoner_surnames": ["of-Arkay", "Grave-Walker", "Bone-Chiller", "Death-Caller", "of-Falkreath"]
        }
    },
    "vengeful_spirit_kael": {
        "noble": {
          "male": [],
          "female": [],
          "noble_surnames": []
        },
        "commoner": {
            "male": ["Kael"],
            "female": [],
            "commoner_surnames": ["of-Vengeance", "Shadow-Walker", "Grave-Wail", "Spirit-Caller", "of-the-Grave"]
        }
    }
}
# Add a unique ID to each NPC name in NAME_POOLS for tracking purposes (from original)
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

        # Assign unique_id for this NPC instance (from original)
        if name is None:
            gender = random.choice(["male", "female"])
            name_type = "noble" if self.role in NOBLE_ROLES else "commoner"

            race_name_pool_data = NAME_POOLS.get(self.race)
            if not race_name_pool_data:
                UI.print_system_message(f"DEBUG: NPC Init - No name pool found for race '{self.race}'. Falling back to 'nord'.") # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                race_name_pool_data = NAME_POOLS.get("nord")

            specific_name_pool = race_name_pool_data.get(name_type)
            if not specific_name_pool:
                UI.print_system_message(f"DEBUG: NPC Init - No '{name_type}' name pool for race '{self.race}'. Falling back to 'commoner'.") # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                specific_name_pool = race_name_pool_data.get("commoner")

            gender_specific_pool = specific_name_pool.get(gender)
            if not gender_specific_pool:
                UI.print_system_message(f"DEBUG: NPC Init - No '{gender}' names for '{name_type}' '{self.race}'. Falling back to generic 'unknown_npc'.") # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                gender_specific_pool = [f"unknown_npc_{random.randint(10,99)}"] # Final fallback

            chosen_id_from_pool = random.choice(gender_specific_pool)
            first_name = chosen_id_from_pool.split('_')[0].capitalize() # Display name is first part of ID
            self.unique_id = chosen_id_from_pool # Use the full ID from NAME_POOLS

            # Add surname if available for the race
            if self.race in NAME_POOLS and (
                "noble_surnames" in specific_name_pool or "commoner_surnames" in specific_name_pool
            ):
                surname_pool = specific_name_pool.get("noble_surnames") or specific_name_pool.get("commoner_surnames")
                if surname_pool:
                    surname = random.choice(surname_pool)
                    self.name = f"{first_name} {surname}"
                else:
                    self.name = first_name  # Just use the first name if no surnames
            else:
                self.name = first_name

        else: # If a specific name is provided (e.g., for quest givers)
            self.name = name
            # Generate a unique ID for this specific named NPC
            self.unique_id = f"{self.name.lower().replace(' ', '_')}_{self.role.lower().replace(' ', '_')}_{random.randint(100,999)}"

        # Stats and Skills (from original - unchanged)
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
        self.skills = {}
        base_skill_val = 5

        role_l = self.role.lower()
        if any(s_role in role_l for s_role in ["mage", "scholar", "priest", "shaman", "necromancer", "cultist", "healer"]):
            self.skills["destruction"] = random.randint(15, 30) + self.level * 2
            self.skills["restoration"] = random.randint(15, 30) + self.level * 2
            self.skills["alteration"] = random.randint(10, 25) + self.level
            self.skills["conjuration"] = random.randint(10, 25) + self.level if "mage" in role_l or "necromancer" in role_l else base_skill_val
            self.skills["illusion"] = random.randint(10, 20) + self.level if "mage" in role_l or "illusionist_role" in role_l else base_skill_val
        elif any(s_role in role_l for s_role in ["warrior", "guard", "bandit", "companion", "forsworn", "soldier", "legionnaire", "thug", "raider", "mercenary", "thalmor_justiciar"]): # Added thalmor
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

        race_mods = RACES.get(self.race, {})
        for attr, mod_val in race_mods.items():
            if attr.endswith("_mod") and hasattr(self.stats, attr.replace("_mod","")):
                 stat_name = attr.replace("_mod","")
                 setattr(self.stats, stat_name, getattr(self.stats, stat_name) + mod_val)
            elif attr.endswith("_resist") and hasattr(self.stats, attr):
                 setattr(self.stats, attr, getattr(self.stats, attr) + mod_val)
            elif attr == "magicka_mod" and hasattr(self.stats, "max_magicka"):
                self.stats.max_magicka += mod_val
            elif attr.endswith("_skill"):
                skill_name = attr.replace("_skill","")
                self.skills[skill_name] = self.skills.get(skill_name, base_skill_val) + mod_val

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

        # CORRECTED: These methods should be called on self after they are defined within the class
        self.greeting = self._generate_greeting() 
        self.purpose = self._generate_purpose()

    def __str__(self):
        return f"{self.name} ({self.role.replace('_',' ').capitalize()}, Level {self.level})"

    @property
    def full_name(self):
        return self.name

    def add_tag(self, category, key, value):
        if category not in self.tags:
            self.tags[category] = {}
        self.tags[category][key] = value

    # MOVED _generate_greeting INSIDE THE CLASS
    def _generate_greeting(self):
        """Generate comprehensive, lore-friendly greetings based on role, race, disposition, and context"""
        attitude = self.tags.get("npc", {}).get("attitude", "neutral")
        role_lower = self.role.lower()
        # race_lower = self.race.lower() # This line was unused, removed for now
        disposition = self.disposition
        
        # Hostile greetings - always prioritize if hostile attitude
        if attitude == "hostile" or disposition < 20:
            hostile_greetings = {
                "bandit": [
                    "Hand over your coin, or I'll take it from your corpse!",
                    "Wrong place, wrong time, stranger. This is bandit territory!",
                    "You've walked into the wrong camp, fool. Prepare to die!",
                    "Your purse or your life! Choose quickly!"
                ],
                "forsworn": [
                    "Another Imperial dog comes to defile our sacred lands!",
                    "The old gods demand your blood, outlander!",
                    "You trespass on Forsworn territory. The Reach will have its revenge!",
                    "By Hircine's bloody hunt, you will not leave here alive!"
                ],
                "thalmor": [
                    "Another inferior being seeks audience with their betters.",
                    "You dare approach an agent of the Aldmeri Dominion so brazenly?",
                    "Your very presence offends the natural order, mortal.",
                    "State your business quickly, before I lose what little patience I have."
                ],
                "vampire": [
                    "You reek of mortality... how deliciously fragile you are.",
                    "Another warm-blooded fool wanders into my domain.",
                    "Your blood calls to me, mortal. Resist if you can.",
                    "The living should not disturb the eternal. You will regret this."
                ],
                "necromancer": [
                    "You interrupt my communion with death itself!",
                    "Another soul to add to my collection... willing or not.",
                    "The dark arts have shown me your fate, fool.",
                    "Life is but a fleeting moment before eternal servitude!"
                ],
                "default": [
                    "You picked the wrong person to cross!",
                    "Get away from me before I do something we'll both regret!",
                    "I don't have time for your kind!",
                    "Move along before this gets ugly!"
                ]
            }
            
            for role_key in hostile_greetings:
                if role_key in role_lower:
                    return random.choice(hostile_greetings[role_key])
            return random.choice(hostile_greetings["default"])
        
        # Unfriendly but not hostile (20-40 disposition)
        elif disposition < 40:
            unfriendly_greetings = {
                "guard": [
                    "Keep moving, citizen. Nothing to see here.",
                    "State your business and make it quick.",
                    "I've got my eye on you, stranger.",
                    "Don't give me a reason to arrest you."
                ],
                "merchant": [
                    "I suppose you want something. Coin first, questions later.",
                    "My prices aren't negotiable, so don't waste my time haggling.",
                    "What do you want? I'm busy running a business here.",
                    "If you're not buying, then you're Browse. Don't touch anything."
                ],
                "noble": [
                    "Do you have an appointment? No? Then this conversation is over.",
                    "I don't associate with commoners without good reason.",
                    "Your presence here is... unexpected. And unwelcome.",
                    "Speak quickly. My time is far more valuable than yours."
                ],
                "priest": [
                    "The gods test my patience with visitors like you.",
                    "State your need for divine guidance... if you're worthy.",
                    "Even the Divines grow weary of those who lack faith.",
                    "What brings you to disturb my meditation?"
                ],
                "default": [
                    "What do you want?",
                    "Make it quick, I haven't got all day.",
                    "I suppose you need something from me.",
                    "This better be important."
                ]
            }
            
            for role_key in unfriendly_greetings:
                if role_key in role_lower:
                    return random.choice(unfriendly_greetings[role_key])
            return random.choice(unfriendly_greetings["default"])
        
        # Neutral greetings (40-60 disposition)
        elif disposition < 60:
            neutral_greetings = {
                "innkeeper": [
                    "Welcome to my establishment. Room or board?",
                    "What can I get for you today?",
                    "Take a seat wherever you like. I'll be with you shortly.",
                    "We've got food, drink, and beds. What's your pleasure?"
                ],
                "merchant": [
                    "Browse my wares if you like. Prices are fair.",
                    "I've got quality goods at reasonable prices.",
                    "Looking for anything in particular today?",
                    "Take a look around. I'm sure we can make a deal."
                ],
                "guard": [
                    "Citizen. Keep your nose clean while you're in town.",
                    "Just remember to follow the laws while you're here.",
                    "Move along, nothing to see here.",
                    "Keep the peace, and we won't have any problems."
                ],
                "blacksmith": [
                    "I work with steel and iron. What do you need forged?",
                    "My forge burns hot and my hammer rings true.",
                    "Looking for weapons or armor? You've come to the right place.",
                    "Quality smithwork takes time. What can I craft for you?"
                ],
                "farmer": [
                    "Another traveler passes through our humble lands.",
                    "The soil here is good, but the work is hard.",
                    "Are you here about the crops, or just passing through?",
                    "Times are tough for farmers, but we manage."
                ],
                "miner": [
                    "Long days in the mines make for short conversations.",
                    "The deeper you dig, the more dangers you find.",
                    "Mining's honest work, if you can handle the darkness.",
                    "These mountains hold more secrets than gold."
                ],
                "hunter": [
                    "The wilds provide for those who respect them.",
                    "Game's been scarce lately. Something's got them spooked.",
                    "A hunter learns to read the signs the land provides.",
                    "These forests hold both bounty and danger in equal measure."
                ],
                "scholar": [
                    "Knowledge is the greatest treasure of all.",
                    "I seek understanding in the written word.",
                    "Ancient lore holds answers to modern questions.",
                    "Learning never ends for those who truly seek wisdom."
                ],
                "bard": [
                    "Every person has a story worth telling.",
                    "Music and tales lighten even the darkest days.",
                    "I collect stories like others collect coin.",
                    "Would you care to hear a song, or perhaps share a tale?"
                ],
                "default": [
                    "Hello there.",
                    "Can I help you with something?",
                    "What brings you here?",
                    "Good to see another traveler."
                ]
            }
            
            for role_key in neutral_greetings:
                if role_key in role_lower:
                    return random.choice(neutral_greetings[role_key])
            return random.choice(neutral_greetings["default"])
        
        # Friendly greetings (60-80 disposition)
        elif disposition < 80:
            friendly_greetings = {
                "innkeeper": [
                    "Welcome, welcome! Come warm yourself by the fire!",
                    "Well met, traveler! The finest ale in the hold awaits you!",
                    "A friendly face! Please, make yourself at home here.",
                    "By the Eight and One, it's good to see a new face! What can I do for you?"
                ],
                "merchant": [
                    "Ah, a discerning customer! I have just the thing for you!",
                    "Welcome, friend! My wares are the finest you'll find anywhere!",
                    "Excellent timing! I just received a new shipment you'll want to see.",
                    "A shrewd buyer knows quality when they see it. Take a look around!"
                ],
                "guard": [
                    "Well met, citizen. Always good to see law-abiding folk.",
                    "Greetings! Your timing is good - the roads are safe today.",
                    "Welcome to our fair city. May your stay be peaceful and profitable.",
                    "A friendly face in these troubled times. How can I assist you?"
                ],
                "priest": [
                    "The Divines bless this meeting, child. How may I serve?",
                    "May Akatosh's light guide your path, traveler.",
                    "Welcome to this sacred place. The gods smile upon the faithful.",
                    "Peace be with you, friend. What spiritual guidance do you seek?"
                ],
                "blacksmith": [
                    "Ah, someone who appreciates fine metalwork! Welcome to my forge!",
                    "Well met! I take pride in every piece that leaves my workshop.",
                    "A fellow admirer of steel and flame! What can I craft for you?",
                    "The ring of hammer on anvil calls to all true warriors. How can I help?"
                ],
                "noble": [
                    "Greetings, citizen. Your reputation precedes you.",
                    "Well met! It's refreshing to encounter someone of quality.",
                    "A person of distinction, I see. How may I be of service?",
                    "Welcome! Your presence brings honor to my hall."
                ],
                "farmer": [
                    "Well met, friend! The harvest has been kind this season.",
                    "Welcome to our lands! Honest work makes for honest folk.",
                    "Good to see a friendly traveler! The road treats you well, I hope.",
                    "By Kynareth's grace, another good soul crosses our path!"
                ],
                "hunter": [
                    "Well met, fellow wanderer! The wilds have been good to me lately.",
                    "Greetings! A kindred spirit who appreciates nature's bounty.",
                    "Welcome, friend! The forest provides for those who respect her.",
                    "Good hunting to you! May your aim be true and your quarry plentiful."
                ],
                "scholar": [
                    "Greetings, fellow seeker of knowledge! What wisdom do you pursue?",
                    "Well met! A mind that questions is a mind that grows.",
                    "Welcome! Perhaps we might share discoveries over scholarly discourse?",
                    "Ah, another who values learning! What brings you to seek knowledge?"
                ],
                "bard": [
                    "Well met, friend! Would you care to hear a tale of distant lands?",
                    "Greetings! Every new face brings new stories to collect.",
                    "A warm welcome to you! Music and merriment lift all spirits.",
                    "Hail and well met! Perhaps you have a song or story to share?"
                ],
                "mage": [
                    "Well met, traveler! The arcane arts reveal much about one's character.",
                    "Greetings! I sense you have an appreciation for the mystical.",
                    "Welcome! Knowledge of the magical arts is always worth sharing.",
                    "Well encountered! The weave of magic connects all things."
                ],
                "default": [
                    "Well met, friend!",
                    "Greetings, traveler! Good to see you!",
                    "Welcome! What brings you our way?",
                    "A friendly face! How can I help you today?"
                ]
            }
            
            for role_key in friendly_greetings:
                if role_key in role_lower:
                    return random.choice(friendly_greetings[role_key])
            return random.choice(friendly_greetings["default"])
        
        # Very friendly/admiring greetings (80+ disposition)
        else:
            admiring_greetings = {
                "innkeeper": [
                    "My friend! Welcome back to the finest establishment in all Skyrim!",
                    "By the gods, if it isn't my most valued patron! Your usual table awaits!",
                    "The hero graces my humble inn once more! Tonight, the ale flows freely!",
                    "Welcome, welcome! Your legendary reputation brightens these halls!"
                ],
                "merchant": [
                    "My most esteemed customer returns! I've saved my finest wares just for you!",
                    "The realm's greatest hero honors my shop! Everything is at your disposal!",
                    "By Zenithar's golden scales! Take whatever you need, my friend!",
                    "Your patronage brings prosperity to my business and honor to my name!"
                ],
                "guard": [
                    "An honor to serve alongside someone of your caliber, hero!",
                    "The people sleep safely knowing heroes like you walk among us!",
                    "By Stendarr's mercy, our city is blessed by your presence!",
                    "Your deeds will be remembered for generations, champion!"
                ],
                "priest": [
                    "The Divines themselves must have guided you to this sacred place!",
                    "Blessed are we to receive one so favored by the gods!",
                    "Your righteous deeds echo through the halls of Aetherius itself!",
                    "May the Nine Divines continue to bless your noble quest!"
                ],
                "blacksmith": [
                    "The legendary hero graces my forge! What weapon shall I craft for your next great deed?",
                    "By Talos's hammer! Working steel for a true champion is a smith's greatest honor!",
                    "Every blade I forge pales beside the legend you've already written!",
                    "Your patronage makes my humble craft legendary by association!"
                ],
                "noble": [
                    "My lord/lady! Your presence brings honor to my entire bloodline!",
                    "The realm's greatest champion graces my halls! You are always welcome here!",
                    "By my ancestors' honor, serving you is the privilege of a lifetime!",
                    "Your legendary deeds have earned you a place in the songs of our bards!"
                ],
                "scholar": [
                    "The living legend seeks knowledge! What wisdom can this humble scholar provide?",
                    "Your deeds will be studied by generations of historians yet unborn!",
                    "To share knowledge with one so renowned is a scholar's ultimate achievement!",
                    "History itself bends around your actions, shaping the fate of empires!"
                ],
                "bard": [
                    "The hero of legend walks among us! Your deeds surpass even the greatest epics!",
                    "Every song I sing pales before the reality of your adventures!",
                    "Bards across the realm compose verses about your magnificent deeds!",
                    "To meet the subject of so many tales in person... what an honor!"
                ],
                "default": [
                    "My friend! Always a pleasure to see you!",
                    "The legendary hero returns! How may I serve?",
                    "Your reputation precedes you, champion!",
                    "By the gods, what an honor to speak with you again!"
                ]
            }
            
            for role_key in admiring_greetings:
                if role_key in role_lower:
                    return random.choice(admiring_greetings[role_key])
            return random.choice(admiring_greetings["default"])

    # MOVED _generate_purpose INSIDE THE CLASS
    def _generate_purpose(self):
        """Generate comprehensive, lore-friendly purpose descriptions based on role, race, and context"""
        role_lower = self.role.lower()
        race_lower = self.race.lower()
        disposition = self.disposition
        
        # Comprehensive purpose descriptions organized by role
        purpose_descriptions = {
            "innkeeper": [
                "provide weary travelers with warm beds, hot meals, and cold ale in these troubled times",
                "keep this establishment running smoothly, ensuring every guest feels welcome and safe",
                "offer refuge to those who walk the dangerous roads of Skyrim, sharing news and stories",
                "maintain a place where all folk can rest, regardless of the civil war raging outside",
                "serve the finest food and drink in the hold while keeping ears open for useful information",
                "create a haven where merchants, adventurers, and locals can gather in peace",
                "honor the old traditions of hospitality that have kept inns sacred since the First Era"
            ],
            
            "merchant": [
                "trade in goods both common and rare, connecting distant markets across the Empire",
                "seek profit through honest commerce, following the blessed path of Zenithar",
                "provide essential supplies to settlements that would otherwise go without",
                "maintain trade routes that keep gold flowing and communities prosperous",
                "deal in exotic wares from distant provinces, bringing the world to Skyrim's doorstep",
                "negotiate fair prices while ensuring my family's prosperity for generations to come",
                "preserve the ancient mercantile traditions that built the great trading companies"
            ],
            
            "guard": [
                "protect the innocent and uphold the laws of this hold, whatever the personal cost",
                "maintain order in these chaotic times, when brother fights brother across Skyrim",
                "serve the people with honor, following the righteous path of Stendarr",
                "keep the peace while navigating the treacherous politics of civil war",
                "defend this settlement against bandits, monsters, and worse threats from the wild",
                "enforce justice fairly, regardless of race, creed, or political allegiance",
                "stand as a beacon of stability when the very foundations of the Empire shake"
            ],
            
            "blacksmith": [
                "forge weapons and armor worthy of the heroes who will shape Skyrim's destiny",
                "work the sacred metals with hammer and flame, following techniques passed down through ages",
                "craft tools of war and peace that will outlast those who wield them",
                "maintain the ancient traditions of metalworking that built the Nordic civilization",
                "create blades that sing with the strength of the earth and the fury of dragon fire",
                "honor the craft taught by the Dwemer and perfected by generations of Nordic smiths",
                "ensure that warriors have the steel they need to face the darkness ahead"
            ],
            
            "priest": [
                "serve the Nine Divines and guide the faithful through these dark and troubled times",
                "offer spiritual counsel to those whose souls are burdened by war and loss",
                "maintain the sacred traditions that connect mortals to the realm of Aetherius",
                "heal both body and spirit through the blessed power of divine magic",
                "preserve the ancient teachings while adapting to a world where Talos is forbidden",
                "provide sanctuary to all who seek the gods' mercy, regardless of their past sins",
                "stand as a bulwark against the forces of darkness that would corrupt Tamriel"
            ],
            
            "scholar": [
                "delve into the mysteries of the past to better understand our troubled present",
                "preserve knowledge that would otherwise be lost to the ravages of time and war",
                "study the ancient texts that hold the keys to forgotten magics and lost wisdom",
                "seek truth in the written word while others seek it with sword and flame",
                "document the events of our time so future generations might learn from our mistakes",
                "unravel the secrets of Dwemer technology and Ayleid magic for the betterment of all",
                "maintain the great libraries that are civilization's true treasures"
            ],
            
            "bard": [
                "preserve the songs and stories that define our people's identity and history",
                "bring joy and inspiration to hearts heavy with the burden of these dark times",
                "carry news and tales between settlements, connecting distant communities through story",
                "honor the traditions of the Bards College while creating new legends for future ages",
                "use music and verse to heal the divisions that tear our land asunder",
                "document the deeds of heroes whose names should echo through eternity",
                "keep alive the old songs that remember when dragons ruled the skies"
            ],
            
            "farmer": [
                "work the sacred soil to feed the people of this hold, following Kynareth's eternal cycle",
                "maintain the agricultural traditions that have sustained Nordic civilization for millennia",
                "coax sustenance from the harsh northern earth through backbreaking labor and ancient wisdom",
                "provide the foundation upon which all civilization rests - food for the hungry masses",
                "preserve the farming techniques passed down through generations of my bloodline",
                "endure the hardships of rural life while supporting the great cities and their grand ambitions",
                "honor the old compact between farmer and land, giving back as much as I take"
            ],
            
            "hunter": [
                "track game through the wilds while respecting the ancient laws of the hunt",
                "provide meat and pelts for my community while maintaining nature's delicate balance",
                "read the signs of forest and field that speak of dangers both natural and supernatural",
                "follow the path of Hircine while honoring Kynareth's dominion over the natural world",
                "venture into the deep woods where few dare tread, bringing back both bounty and warnings",
                "preserve the hunting traditions that kept the Nords alive during their first harsh winters",
                "serve as a bridge between civilization and the untamed wilderness beyond"
            ],
            
            "miner": [
                "delve deep into the earth's bones, seeking the precious metals that fuel civilization",
                "follow veins of ore through dangerous tunnels where cave-ins and worse things lurk",
                "extract the wealth hidden in Skyrim's mountains while respecting the spirits of the deep",
                "endure the darkness and danger of the mines to provide the raw materials for progress",
                "work alongside my brothers in the dangerous depths where only trust keeps us alive",
                "honor the ancient mining traditions while adapting to new techniques and deeper shafts",
                "risk my life daily in the hope that my children might know a better future"
            ],
            
            "mage": [
                "study the fundamental forces that shape reality itself, wielding power beyond mortal ken",
                "explore the mysteries of magic while respecting the dangerous forces I command",
                "advance the understanding of the arcane arts for the betterment of all Tamriel",
                "maintain the balance between the mortal world and the chaotic realm of Oblivion",
                "preserve magical knowledge while training the next generation of spellcasters",
                "serve as guardian against supernatural threats that mundane weapons cannot touch",
                "seek to unlock the secrets of creation itself through careful study and experimentation"
            ],
            
            "noble": [
                "govern my lands and people with wisdom befitting my ancient bloodline",
                "navigate the treacherous politics of court while serving the true needs of my subjects",
                "maintain the old traditions of nobility - protection, justice, and responsible leadership",
                "balance loyalty to the Empire with the growing demands of Nordic independence",
                "preserve my family's honor while adapting to a rapidly changing political landscape",
                "serve as a bridge between the common folk and the distant machinations of power",
                "uphold the sacred duties of my station, whatever the personal cost may be"
            ],
            
            # Hostile/Criminal roles
            "bandit": [
                "take what this harsh world owes me, since honest work brings only suffering",
                "prey upon the wealthy travelers who flaunt their gold while others starve",
                "survive in a world that offers nothing to those born without title or privilege",
                "claim my share of Skyrim's wealth through strength and cunning rather than birthright",
                "live free from the laws that serve only the rich and powerful",
                "make the roads dangerous for those who would exploit the common folk",
                "build my own kingdom in the wilderness, far from the corruption of civilization"
            ],
            
            "thief": [
                "redistribute wealth from those who have too much to those who have nothing",
                "practice the ancient art of stealth and cunning in a world ruled by brute force",
                "survive by my wits in a society that offers no legitimate opportunities for advancement",
                "follow the shadowy path that leads to secrets and treasures others cannot reach",
                "serve the Guild's ancient codes while profiting from the chaos of civil war",
                "prove that skill and intelligence matter more than inherited privilege",
                "operate in the spaces between law and chaos where true freedom exists"
            ],
            
            "forsworn": [
                "reclaim the ancient lands of the Reach that were stolen by Nordic invaders",
                "serve the old gods who demand blood vengeance for generations of oppression",
                "preserve the true heritage of the Reachmen against Imperial and Nordic corruption",
                "wage eternal war against the usurpers who drove my people into the wilderness",
                "honor the ancient pacts with Hagravens and the spirits of the wild",
                "prove that the Reach will never be tamed by foreign laws and foreign gods",
                "carry on the struggle that began when the first Nord set foot in our sacred lands"
            ],
            
            "vampire": [
                "embrace the eternal night that frees me from mortal concerns and limitations",
                "feed upon the living while building power that spans centuries rather than mere decades",
                "serve the will of Molag Bal while maintaining my facade among the cattle of mortality",
                "accumulate knowledge and influence across the ages that mortals cannot comprehend",
                "prove that undeath is evolution, not curse, despite what the living might believe",
                "maintain the ancient bloodlines while adapting to a world that grows ever more hostile",
                "rule from the shadows, manipulating mortal affairs like pieces on a grand game board"
            ],
            
            "necromancer": [
                "explore the forbidden arts that reveal death as merely another beginning",
                "command the restless dead who serve more faithfully than any living follower",
                "study the boundaries between life and death that lesser minds fear to examine",
                "accumulate power through means that squeamish mortals refuse to consider",
                "serve the will of the Daedric Princes who understand the true nature of existence",
                "prove that the conventional morality of the masses is merely ignorance and weakness",
                "build an undying empire where death has no meaning and power knows no limits"
            ],
            
            # Faction-specific roles
            "stormcloak_soldier": [
                "fight for Skyrim's independence from the corrupt and weakened Empire",
                "serve Ulfric Stormcloak's vision of a free Nordic homeland ruled by Nordic traditions",
                "oppose the Thalmor's cultural imperialism and their outlawing of Talos worship",
                "preserve the ancient ways of the Nords against foreign influence and corruption",
                "prove that Nordic strength and honor can overcome Imperial politics and Elven manipulation",
                "reclaim Skyrim's destiny from those who would sell it for temporary peace",
                "fight for the right to worship Talos and maintain our ancestral traditions"
            ],
            
            "imperial_soldier": [
                "maintain unity within the Empire during its darkest hour of division",
                "serve the greater good even when it requires difficult compromises and sacrifices",
                "protect the peace that the Empire has maintained for centuries across Tamriel",
                "oppose the chaos and bloodshed that Nordic independence would unleash",
                "preserve the rule of law against the primitive tribalism of Stormcloak rebels",
                "serve as a bulwark against the Thalmor's true agenda while maintaining necessary alliances",
                "protect the common people from the devastation that civil war brings to all"
            ],
            
            "thalmor_justiciar": [
                "enforce the terms of the White-Gold Concordat for the good of all Tamriel",
                "root out the heretical worship of Talos that corrupts the natural order",
                "serve the Aldmeri Dominion's mission to restore proper hierarchy to the world",
                "investigate threats to the carefully maintained peace between Empire and Dominion",
                "protect Altmer superiority against the jealous violence of lesser races",
                "maintain surveillance over the primitive humans who cannot govern themselves",
                "advance the Thalmor's righteous agenda through law, diplomacy, and necessary force"
            ],
            
            # Creature/Undead roles
            "draugr": [
                "guard the ancient tombs and sacred barrows of my Nordic ancestors",
                "serve in undeath as I served in life - protecting what must be protected",
                "maintain the eternal vigil over treasures and secrets that must not be disturbed",
                "honor the ancient oaths that bind me even beyond the grave",
                "punish those who would defile the resting places of heroes and kings",
                "preserve the old ways through endless, tireless guardianship",
                "serve the dragon priests and ancient powers that commanded my loyalty in life"
            ]
        }
        
        # Racial modifiers for purposes
        racial_modifiers = {
            "nord": [
                "while honoring the ancient traditions of my Nordic ancestors",
                "following the path laid down by Ysgramor and the Five Hundred Companions",
                "with the strength and determination that flows in Nordic blood",
                "serving Skyrim and her people above all other loyalties"
            ],
            "imperial": [
                "while maintaining the civilized order that the Empire represents",
                "following the diplomatic traditions that built the greatest empire in history",
                "with the administrative skill that has kept the Empire strong for centuries",
                "serving the greater unity that transcends provincial boundaries"
            ],
            "dunmer": [
                "while adapting the ancient wisdom of Morrowind to these northern lands",
                "following the complex traditions of the Great Houses and their endless intrigues",
                "with the cunning and resilience that helped my people survive the Red Year",
                "serving the interests of Dunmer refugees while respecting our hosts"
            ],
            "altmer": [
                "while maintaining the superior standards befitting the Aldmeri heritage",
                "following the ancient wisdom preserved in the Summerset Isles for millennia",
                "with the refined skill and knowledge that comes from centuries of study",
                "serving the cause of proper order and hierarchy in this chaotic world"
            ],
            "redguard": [
                "while honoring the warrior traditions of Hammerfell and the Way of the Sword",
                "following the code of honor that has defined Redguard culture for ages",
                "with the martial skill and personal integrity that flows in Yokudan blood",
                "serving the cause of honor and justice wherever it may lead"
            ],
            "khajiit": [
                "while following the moonpaths that guide all children of Elsweyr",
                "adapting to northern customs while maintaining the wisdom of the Khajiit",
                "with the curiosity and cunning that serves Khajiit well in foreign lands",
                "serving the greater tapestry that connects all things under Jone and Jode"
            ],
            "argonian": [
                "while following the guidance of the Hist even in these distant marshless lands",
                "adapting the ancient wisdom of Black Marsh to the challenges of the north",
                "with the patience and resilience that flows from the deep swamps of home",
                "serving the mysterious purposes that only the Hist truly understand"
            ],
            "orc": [
                "while maintaining the strength and honor that defines the Orsimer people",
                "following the Code of Malacath even when surrounded by those who misunderstand it",
                "with the forge-skill and warrior's heart that flows in Orcish blood",
                "serving the cause of strength and honest labor in a world full of weaklings"
            ],
            "breton": [
                "while balancing the practical wisdom of High Rock with mystical understanding",
                "following the merchant traditions that have made Bretons successful across Tamriel",
                "with the magical heritage and political acumen that defines my people",
                "serving the cause of profitable cooperation and mutual advancement"
            ],
            "bosmer": [
                "while respecting the Green Pact and the natural order even in these northern forests",
                "following the ancient ways of Valenwood adapted to Skyrim's harsh environment",
                "with the woodland wisdom and keen senses that flow in Bosmer blood",
                "serving the balance between civilization and the wild that sustains all life"
            ]
        }
        
        # Select appropriate purpose based on role
        base_purposes = []
        for role_key in purpose_descriptions:
            if role_key in role_lower:
                base_purposes = purpose_descriptions[role_key]
                break
        
        # Fallback for unspecified roles
        if not base_purposes:
            generic_purposes = [
                "make my way in this world as best I can during these troubled times",
                "serve my community while pursuing my own interests and ambitions",
                "navigate the complexities of life in Skyrim during an age of civil war",
                "maintain my livelihood while staying true to my principles and beliefs",
                "contribute to society while protecting what matters most to me",
                "find my place in a world that seems to grow more dangerous each day",
                "pursue my goals while respecting the ancient traditions of this land"
            ]
            base_purposes = generic_purposes
        
        # Select base purpose
        base_purpose = random.choice(base_purposes)
        
        
        # Add racial modifier if applicable (30% chance)
        if race_lower in racial_modifiers and random.random() < 0.3:
            racial_addition = random.choice(racial_modifiers[race_lower])
            base_purpose += f", {racial_addition}"
        
        # Add disposition-based modifiers
        if disposition >= 80:
            enthusiasm_modifiers = [
                "with great passion and dedication",
                "knowing that I serve a noble and worthy cause",
                "with the satisfaction that comes from meaningful work",
                "while building lasting relationships with those I serve"
            ]
            if random.random() < 0.4:
                base_purpose += f", {random.choice(enthusiasm_modifiers)}"
        
        elif disposition <= 30:
            cynical_modifiers = [
                "though I sometimes question whether it's worth the effort",
                "despite the lack of appreciation I receive for my efforts",
                "while dealing with more fools and ingrates than any person should",
                "though the pay barely covers my expenses and the risks"
            ]
            if random.random() < 0.3:
                base_purpose += f", {random.choice(cynical_modifiers)}"
        
        return base_purpose

    def dialogue(self, player, current_location) -> None:
        UI.clear_screen()
        player.add_talked_to_npc(self.unique_id)

        UI.slow_print(f"You approach {self.name} ({self.role.replace('_',' ').capitalize()}). Disposition: {self.disposition}")
    
        UI.slow_print(f"{self.purpose.capitalize()}")
    
        UI.slow_print(f'"{self.greeting}"')
        previous_dialogue = ""
    
        options_texts = []
        quests_to_turn_in = player.quest_log.get_quests_for_turn_in(self.unique_id)

        if quests_to_turn_in:
            options_texts.append("Turn in a completed quest")

        options_texts.append("Ask for rumors or work")
        options_texts.append("Ask about your work/purpose")
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
                # ... (rest of the turn-in logic remains the same)
                action_taken = True

            elif chosen_option_text == "Ask for rumors or work":
                self.share_rumor(player, current_location) # This method handles its own quest chance (20%)
                action_taken = True

            elif chosen_option_text == "Ask about your work/purpose":
                current_dialogue = self.purpose
                if current_dialogue == previous_dialogue:
                    UI.slow_print(UI.capitalize_dialogue(f'"As I said, {self.purpose}"'))
                else:
                    UI.slow_print(UI.capitalize_dialogue(f'"{self.purpose}"'))
                previous_dialogue = current_dialogue
                if self.disposition > 60 and "merchant" in self.role.lower():
                    UI.slow_print(UI.capitalize_dialogue(f'"Perhaps you\'re looking to buy or sell, {player.full_name}? I have a few things that might interest you, or I might be interested in what you have to offer."'))
                elif self.disposition > 55 and "guard" in self.role.lower():
                    UI.slow_print(UI.capitalize_dialogue(f'"Just try to stay out of trouble. That makes my job easier."'))

                # MODIFIED PART for work/purpose quest chance
                if not self.has_offered_quest and random.random() < 0.1: # 10% chance
                     UI.slow_print(UI.capitalize_dialogue(f'"Actually, since you\'re asking, there is something that\'s been bothering me about my work..."'))
                     # CORRECTED CALL to generate_location_appropriate_quest
                     quest_to_offer = generate_location_appropriate_quest(player.stats.level, current_location, self.unique_id)
                     if quest_to_offer and not player.quest_log.get_quest_by_id(quest_to_offer.quest_id):
                         self._offer_quest(player, quest_to_offer)
                     else:
                         UI.slow_print(UI.capitalize_dialogue(random.choice(['"But perhaps it\'s best not to burden you with my troubles."', '"Nevermind, I\'ll handle it myself."'])))
                action_taken = True

            elif chosen_option_text == "Discuss this place":
                self._discuss_place(current_location)
                action_taken = True

            elif chosen_option_text == "Farewell":
                farewell_messages = [
                    'Farewell, traveler.',
                    'May your path be clear.',
                    'Until next time.'
                ]
                chosen_farewell = random.choice(farewell_messages)
                formatted_farewell = f'"{chosen_farewell}"'
                UI.slow_print(UI.capitalize_dialogue(formatted_farewell))
                return # Exit dialogue
            else:
                UI.slow_print("A clear answer is expected, traveler.")

            if action_taken:
                UI.press_enter()
                UI.clear_screen()
                # Re-display initial NPC info after an action before showing menu again
                UI.slow_print(f"You are speaking with {self.name}. Disposition: {self.disposition}")
                # No need to repeat greeting and purpose unless it's a fresh interaction
                # UI.slow_print(f'"{self.greeting} {self.purpose}"') # Consider if this should be here or only on first entry

    def share_rumor(self, player, current_location) -> None:
        """Modified rumor sharing to handle quest offering properly"""
        if self.disposition < 35:
            UI.slow_print(UI.capitalize_dialogue(f'"{random.choice(["I have no time for idle gossip.", "Find someone else to bother with your trivial questions."])}"'))
            return

        rumor_output = generate_rumor(player.level, current_location, self.unique_id)
        rumor_text = rumor_output["text"]
        quest_data = rumor_output.get("quest_data")

        UI.slow_print(f'"{rumor_text}"')

         # Logic for offering quest if rumor generates one
        if quest_data: # A quest was potentially generated by generate_rumor (which has a 20% chance)
            if player.quest_log.get_quest_by_id(quest_data.quest_id):
                UI.slow_print(UI.capitalize_dialogue(f"“It seems you're already familiar with that matter, {player.full_name}.”"))
            elif not self.has_offered_quest: # Check if this NPC has already successfully offered a quest
                self._offer_quest(player, quest_data) # If not, proceed to offer this one
        # If self.has_offered_quest is True, this NPC has already made its one quest offer.
        # The rumor is still shared, but no new quest offer is made.

    def _offer_quest(self, player, quest: Quest, from_rumor: bool = False) -> None:
        """Modified quest offering to prevent duplicate dialogue"""
        # Only show the introductory line if this isn't from a rumor
        if not from_rumor:
            UI.slow_print(f'"And speaking of such things... I\'ve heard there\'s a need for someone to {quest.description.lower().split(".")[0]}."')
            if quest.initial_flavor_text:
                UI.slow_print(f'"{quest.initial_flavor_text}"')

        UI.print_line('-')
        UI.print_info(f"Quest: {quest.title}")
        UI.print_info(f"Objective: {quest.description}")
        UI.print_info(f"Current Stage Tasks:")
        current_stage_objectives = quest.current_stage.get("objectives", []) if quest.current_stage else []
        for obj in current_stage_objectives:
            UI.print_info(f"  - {obj.get('note', 'A task awaits.')}")

        reward_parts = []
        if isinstance(quest.reward, dict): # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
            for r_type, r_value in quest.reward.items(): # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                if isinstance(r_value, Item): # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                    reward_parts.append(f"{r_value.name} (Item)")
                else:
                    reward_parts.append(f"{r_value} {r_type.capitalize()}")
        else:
            reward_parts.append(str(quest.reward))
        reward_display_str = ", ".join(reward_parts) if reward_parts else "a token of my gratitude"
        UI.print_info(f"Reward: {reward_display_str}") # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
        UI.print_line('-')

        while True:
            quest_action_prompt = UI.print_prompt("Your response? [1] Accept [2] Decline [3] Consider it further").strip()
            if quest_action_prompt == "1":
                if player.quest_log.add_quest(quest): # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/quests.py
                    UI.slow_print(UI.capitalize_dialogue(f"“Excellent! I knew I could count on you, {player.full_name}. The details are in your journal.”")) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                    self.disposition = min(100, self.disposition + random.randint(3, 7))
                else:
                    UI.slow_print(UI.capitalize_dialogue("“It seems you already have this task, or your journal is full. A pity.”")) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                self.has_offered_quest = True
                break
            elif quest_action_prompt == "2":
                UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['A pity. I had hoped for assistance.', 'Very well. The task will fall to another, then.', 'Understandable. Not all are suited for such endeavors.'])}”")) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                self.disposition = max(0, self.disposition - random.randint(1, 4))
                self.has_offered_quest = True
                break
            elif quest_action_prompt == "3":
                UI.slow_print(UI.capitalize_dialogue(f"“{random.choice(['As you wish. The opportunity may not last indefinitely.', 'Do not tarry too long if you intend to help.', 'Consider it, then. But time is often a factor.'])}”")) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
                break
            else:
                UI.slow_print("A clear answer is expected, traveler.")

    def _discuss_place(self, current_location) -> None:
        """Provides a tag/flavor related answer when asked about the location."""
        loc_name = current_location.get("name", "this place")
        loc_tags = current_location.get("tags", [])

        class DummyLocationForFlavor:
            def __init__(self, tags_list):
                self.tags = {"location": {}}
                for tag_type, possible_values in TAGS["LOCATIONS"].items():
                    found_tags = [t for t in tags_list if t in possible_values]
                    if found_tags:
                        self.tags["location"][tag_type] = found_tags

        dummy_loc_entity = DummyLocationForFlavor(loc_tags)
        flavor_vignettes = flavor.get_flavor(dummy_loc_entity) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/flavor.py

        if flavor_vignettes:
            chosen_flavor = random.choice(flavor_vignettes)
            UI.slow_print(UI.capitalize_dialogue(f"“Ah, {loc_name}. {chosen_flavor}”")) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
        else:
            comments = []
            if "city" in loc_tags: comments.append("It's a major hub, always something happening, for better or worse.")
            if "town" in loc_tags: comments.append("A decent enough place. Quieter than the big cities, which suits some folk.")
            if "village" in loc_tags: comments.append("A small, tight-knit community. We look out for each other here.")
            if "tavern" in loc_tags or "inn" in loc_tags: comments.append("A good place to rest your feet, share a drink, and hear the latest news... or tall tales.")
            if "mountain" in loc_tags: comments.append("The air here is thin, and the peaks are unforgiving. Beautiful, but dangerous.")
            if "forest" in loc_tags: comments.append("The woods are deep and old here. Many secrets, and many dangers, lie within.")
            if "mine" in loc_tags: comments.append("Many fortunes have been made and lost in these mines. A hard life, but honest work.")

            if comments:
                UI.slow_print(UI.capitalize_dialogue(f"“Ah, {loc_name}. {random.choice(comments)}”")) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
            else:
                UI.slow_print(UI.capitalize_dialogue(f"“{loc_name}... It is what it is. Not much else to say about it, really.”")) # cite: ojflavours/tamriel-adventure/Tamriel-Adventure-7faa3d32903fe8bf60c6bcfc42234676e0ead1bf/npc.py
