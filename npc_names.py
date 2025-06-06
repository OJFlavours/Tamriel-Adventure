# npc_names.py
import random

# Surnames are now nested under hold keys. 'generic' is a fallback.
# Hold keys should match the 'name' from your top-level location data, but lowercased with spaces as underscores.
NORD_SURNAMES = {
    "eastmarch": ["Shatter-Shield", "Snow-Shod", "Stone-Fist"],
    "whiterun_hold": ["Battle-Born", "Gray-Mane", "War-Bear"],
    "the_rift": ["Black-Briar"],
    "haafingar": ["Cruel-Sea"],
    "the_reach": ["Silver-Blood"],
    "generic": ["Icestorm", "Rime-Gazer", "Wind-Caller", "Oath-Breaker", "Rune-Carver", "Ice-Veins"]
}

# The main NAME_POOLS dictionary contains the first names. Surnames are now handled separately.
NAME_POOLS = {
    "nord": {
        "noble": {
            "male": ["Ulfric", "Torvald", "Jarlson", "Rolfrick", "Stahlund", "Brynjolf", "Kodlak", "Skjor", "Galmar", "Harkon", "Vignar", "Balgruuf", "Korir", "Thongvor", "Dengeir", "Siddgeir", "Igmund", "Arngeir"],
            "female": ["Brynhild", "Elfarra", "Sofira", "Hildrun", "Thyra", "Laila", "Astrid", "Elisif", "Maven", "Rikke", "Freyja", "Ingjard", "Idgrod", "Skald", "Frida", "Jonna", "Miraak"],
        },
        "commoner": {
            "male": ["Ragnar", "Bjorn", "Sven", "Eirik", "Sigurd", "Hadvar", "Ralof", "Vilkas", "Farkas", "Stenvar", "Benor", "Cosnach", "Vorstag", "Hod", "Torvar", "Athis", "Njada", "Ria", "Skuli", "Torsten"],
            "female": ["Astrid", "Freya", "Ylva", "Ingrid", "Solveig", "Gerdur", "Sigrid", "Mjoll", "Lydia", "Uthgerd", "Annekke", "Sylgja", "Temba", "Hroki", "Hilde", "Gunmar", "Aela", "Jorunn", "Bodil", "Greta"],
        }
    },
    "imperial": {
        "noble": {
            "male": ["Titus", "Valerius", "Cassius", "Hadrian", "Septimus", "Tullius", "Proventus", "Quentin", "Maro", "Atticus", "Lucan", "Vittorio", "Caius", "Marcellus", "Flavius", "Aventus"],
            "female": ["Serana", "Valeria", "Aurelia", "Livia", "Octavia", "Rikke", "Vittoria", "Elissia", "Claudia", "Antonia", "Marcia", "Aeliana", "Flavia", "Cornelia", "Licinia"],
        },
        "commoner": {
            "male": ["Gaius", "Marcus", "Tiber", "Lucius", "Rufus", "Marcurio", "Belrand", "Severio", "Amaund", "Quintus", "Adrian", "Silus", "Festus", "Pavo", "Nura", "Vinius"],
            "female": ["Claudia", "Julia", "Fausta", "Silvia", "Vespasia", "Carlotta", "Wilmuth", "Herminia", "Gisli", "Alessia", "Camilla", "Lucia", "Sabina", "Minerva", "Petra"],
        }
    },
    "breton": {
        "noble": {
            "male": ["Gaston", "Didier", "Armand", "Guillaume", "Thierry", "Farengar", "Ainethach", "Gallus", "Mercer", "Alain", "Etienne", "Tristan", "Jorunn", "Roland", "Benoit"],
            "female": ["Genevieve", "Isabelle", "Marguerite", "Annette", "Elodie", "Sybille", "Tonilia", "Muiri", "Lisette", "Vivienne", "Cecile", "Aurore", "Giselle", "Madeleine", "Seraphine"],
        },
        "commoner": {
            "male": ["Pierre", "Jean", "Louis", "François", "Antoine", "Belethor", "Enthir", "Delvin", "Orthus", "Pascal", "Luc", "Mathieu", "Claude", "Remy", "Sebastien", "Michel"],
            "female": ["Marie", "Sophie", "Jeanne", "Claire", "Nicole", "Colette", "Ysolda", "Lisbet", "Sorine", "Amelie", "Brigitte", "Eloise", "Laurentia", "Celeste", "Valerie"],
        }
    },
    "redguard": {
        "noble": {
            "male": ["Ahmad", "Jamal", "Khalid", "Rashid", "Zafir", "Isran", "Nazir", "Sayyid", "Kematu", "A'tor", "Hassim", "Tariq", "Malik", "Ibrahim", "Yusuf"],
            "female": ["Zafira", "Yasmina", "Samira", "Layla", "Aisha", "Iman", "Anora", "Rayya", "Faleen", "Nura", "Fatima", "Amira", "Safiya", "Lamia", "Zahra"],
        },
        "commoner": {
            "male": ["Cyrus", "Nazir", "Kematu", "Sadir", "Malik", "Nazeem", "Brenuin", "Revus", "Ahlam", "Hassan", "Omar", "Jalal", "Faris", "Karim", "Salih"],
            "female": ["Imani", "Sana", "Nadia", "Zara", "Amina", "Saadia", "Shiri", "Safia", "Umana", "Laila", "Halima", "Rania", "Jamila", "Soraya", "Mina"],
        }
    },
    "dunmer": {
        "noble": {
            "male": ["Nerevar", "Drathis", "Aryon", "Aralen", "Othral", "Neloth", "Savos", "Jiub", "Adril", "Brandyl", "Theryn", "Voryn", "Falen", "Ravyn", "Galyn"],
            "female": ["Morwen", "Fjola", "Jenassa", "Brelyna", "Aranea", "Karliah", "Irileth", "Lythandas", "Vendil", "Almalexia", "Drasa", "Selveni", "Vevrana", "Nisswo", "Milore"],
        },
        "commoner": {
            "male": ["Brand-Shei", "Revyn", "Adril", "Malborn", "Erandur", "Romlyn", "Tythis", "Garyn", "Belyn", "Fethis", "Drovas", "Talen", "Ralen", "Velyn", "Nerano"],
            "female": ["Jenassa", "Fethis", "Mogrul", "Nilene", "Brelyna", "Suvaris", "Dravynea", "Avrusa", "Mirri", "Eldrin", "Selvura", "Nirya", "Vaynelle", "Idesa", "Talmoro"],
        }
    },
    "altmer": {
        "noble": {
            "male": ["Ancano", "Ondolemar", "Rulindil", "Estormo", "Vingalmo", "Naarifin", "Mannimarco", "Quaranir", "Ocato", "Alandro", "Calindil", "Tandilwe", "Lorcalin", "Faelar", "Eldrin"],
            "female": ["Elenwen", "Niranye", "Taarie", "Linwe", "Alwinarwe", "Ayrenn", "Nalime", "Celmire", "Liriel", "Arandil", "Sinderion", "Valinwe", "Elanwe", "Merildor", "Alandra"],
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
    "orc": {
        "noble": {
            "male": ["Ghorbash", "Urag", "Yashnag", "Burguk", "Larak", "Murob", "Gularzob", "Ogol", "Dushnamub", "Yamarz", "Gorzod", "Shuftharz", "Bazrag"],
            "female": ["Mogakh", "Shel", "Borba", "Batul", "Gharol", "Ugor", "Shuftharz", "Lashgra", "Bagrak", "Gul", "Atub", "Sharamph", "Urgarlag"],
        },
        "commoner": {
            "male": ["Grogmar", "Muzgonk", "Shagrol", "Urzog", "Yamorz", "Gat", "Oglub", "Durak", "Bazgrol", "Ulag", "Garoth", "Malkus", "Durgash"],
            "female": ["Urzoga", "Yatul", "Bagrak", "Gharol", "Uglarz", "Borgakh", "Dulug", "Lash", "Sharamph", "Gul", "Borzog", "Orzoga", "Murgol"],
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
}

# Add a unique ID to each NPC name in NAME_POOLS for tracking purposes
def assign_unique_npc_ids(name_pools):
    for race_data in name_pools.values():
        for name_type_data in race_data.values():
            for gender_name_list in name_type_data.values():
                if isinstance(gender_name_list, list):
                    for i in range(len(gender_name_list)):
                        original_name = gender_name_list[i].split('_')[0]
                        unique_id = f"{original_name.lower().replace(' ', '_')}_{random.randint(100, 999)}"
                        gender_name_list[i] = unique_id