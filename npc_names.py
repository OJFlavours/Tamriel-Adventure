# npc_names.py
import random

# Expanded NAME_POOLS dictionary
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
            "female": ["Niruin", "Grelka", "Nimphaneth", "Caminda", "Eridor", "Finna", "Anori", "Lirien", "Selvyn", "Aralindel"]
        },
        "commoner": {
            "male": ["Faendal", "Anoriath", "Valindor", "Elrindir", "Ma'randru-jo", "Gwilin", "Eothram", "Pavo", "Thalindra", "Beron", "Faelar", "Cirdir", "Lorcalin"],
            "female": ["Nimrodel", "Gilfre", "Indara", "Ardwen", "Drynea", "Elrinde", "Lirienwe", "Celmine", "Anoriel", "Selvynia", "Faelindra", "Thalindra", "Vindrel"]
        }
    },
    "orsimer": {
"noble": {
            "male": ["Ghorbash", "Urag", "Yashnag", "Burguk", "Larak", "Murob", "Gularzob", "Ogol", "Dushnamub", "Yamarz", "Gorzod", "Shuftharz", "Bazrag"],
            "female": ["Mogakh", "Shel", "Borba", "Batul", "Gharol", "Ugor", "Shuftharz", "Lashgra", "Bagrak", "Gul", "Atub", "Sharamph", "Urgarlag"],
            "noble_surnames": ["gro-Dushnikh", "gro-Shub", "gro-Yazguul", "gro-Bol", "gro-Largash", "gro-Batul", "gro-Bagol", "gra-Dushnikh", "gra-Yazguul", "gra-Uzg", "gra-Sharob", "gra-Lagash", "gra-Shamub", "gra-Larguk", "gro-Nar", "gro-Fel"]
        },
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
            "female": ["From-Deepest-Fathoms", "Scales-of-Steel", "Druja", "Wanan-To", "Sheer-Meedish", "Pale-Heart-Washes", "Neetrenaza", "Waves-of-Dusk", "Sees-All-Colors", "Drinks-the-Tide"]
        },
        "commoner": {
            "male": ["Derkeethus", "Stands-In-Shadows", "Walks-Softly", "Madesi", "Talendri", "Beem-Ja", "Scouts-Many-Marshes", "Deep-In-His-Cups", "Haj-Ei", "Neet-Loh", "Reezus", "Jee-Lar", "Tsleeixth"],
            "female": ["Shahvee", "Keerava", "Deekus", "Wujeeta", "Reek-Neeus", "Gives-No-Fuss", "Watches-Waves", "Dives-Into-Reeds", "Sings-of-Stars", "Tail-of-Tides", "Bright-Throat"]
        }
    },
    "khajiit": {
        "noble": {
            "male": ["J'zargo", "Ma'iq", "Dro'marash", "Ra'virr", "Ri'saad", "Kharjo", "J'darr", "Ma'jhad", "Razum-dar", "Za'ji", "Jo'ran", "Ra'jirr", "Ka'zhar"],
            "female": ["Ahkari", "Razhinda", "Zaynabi", "Shavari", "Tsrava", "Ma'kara", "Atahbah", "Ri'zhaja", "Khali", "Shazara-Ta", "Tsabhi", "Ri'datta", "Za'jirra"]
        },
        "commoner": {
            "male": ["M'aiq", "J'datharr", "Qa'jo", "Dro'shavir", "Kesh", "Vasha", "Ahjmal", "Zaymar", "Ra'khan", "Jo'dar", "S'jir", "Ma'zaka", "Ra'zhar"],
            "female": ["Shuravi", "Ra'kheran", "Dro'barri", "Tsrasuna", "Bahb-Bi", "S'kasha", "Ri'zala", "Za'darra", "Khayla", "S'rashi", "Ma'zabi", "Jo'vanni", "Ra'tesh"]
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
    },
    "spirit_wolf": { # For summoned Spectral Wolf
        "commoner": { # Summons don't really have noble/commoner distinction
            "male": ["Spectral Packmate", "Ghostly Hunter", "Spirit Hound"], # Names for variety if needed
            "female": [], # Typically genderless
            "commoner_surnames": [] # No surnames
        }
    }
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