from enum import Enum
import random

class Race(Enum):
    IMPERIAL = "imperial"
    NORD = "nord"
    REDGUARD = "redguard"
    BRETON = "breton"
    DUNMER = "dunmer"
    ALTMER = "altmer"
    BOSMER = "bosmer"
    ORC = "orc"
    ARGONIAN = "argonian"
    KHAJIIT = "khajiit"

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

# ### Imperial

# Male Names - Commoner
IMPERIAL_MALE_NAMES_COMMONER = [
    "Flavius", "Aulus", "Titus", "Adrius", "Bastian", "Corvus", "Decianus", "Gallus", "Jens", "Marcurio",
    "Pavo", "Valgus", "Severus", "Roderic", "Garrus"
]

# Male Names - Noble
IMPERIAL_MALE_NAMES_NOBLE = [
    "Gaius", "Lucius", "Marcus", "Septimus", "Valerius", "Aquillius", "Cassian", "Constantine", "Ignatius",
    "Regulus", "Silus", "Tiber", "Varian", "Atticus", "Tullius"
]

# Female Names - Commoner
IMPERIAL_FEMALE_NAMES_COMMONER = [
    "Aurelia", "Drusilla", "Livia", "Alessia", "Caelia", "Fausta", "Gisella", "Justina", "Lucia", "Ria",
    "Serena", "Viola", "Valentina", "Sabina", "Octavia"
]

# Female Names - Noble
IMPERIAL_FEMALE_NAMES_NOBLE = [
    "Octavia", "Tullia", "Valeria", "Poppaea", "Messalina", "Aelia", "Camilla", "Domitia", "Flavia", "Junia",
    "Lavinia", "Marcella", "Porphyria", "Ulpia", "Vipsania"
]

# Surnames - Commoner
IMPERIAL_SURNAMES_COMMONER = [
    "Antonius", "Aurelius", "Aco", "Carius", "Maro", "Vinius", "Accius", "Gratius"
]

# Surnames - Noble
IMPERIAL_SURNAMES_NOBLE = [
    "Flavius", "Julius", "Licinius", "Octavius", "Valerius", "Vilius", "Aemilius", "Claudius",
    "Cornelius", "Horatius", "Septimius", "Tullius"
]

# ### Nord

# Male Names - Commoner
NORD_MALE_NAMES_COMMONER = [
    "Bjorn", "Torvin", "Harald", "Angar", "Falk", "Gunnar", "Hrolf", "Joric", "Sten", "Vigge",
    "Yngvar", "Arinbjorn", "Benor", "Cosnach", "Filnjar"
]

# Male Names - Noble
NORD_MALE_NAMES_NOBLE = [
    "Leif", "Erik", "Ragnar", "Sven", "Ulf", "Balimund", "Eorlund", "Galmar", "Kodlak", "Olaf",
    "Skjor", "Torbjorn", "Ulfric", "Vignar", "Brynjolf"
]

# Female Names - Commoner
NORD_FEMALE_NAMES_COMMONER = [
    "Astrid", "Freya", "Ingrid", "Birgit", "Dagny", "Gerdur", "Hilde", "Olava", "Sigrun", "Tova",
    "Yrsa", "Anja", "Fastred", "Grelka", "Lydia"
]

# Female Names - Noble
NORD_FEMALE_NAMES_NOBLE = [
    "Liv", "Solveig", "Sigrid", "Helga", "Gunnhild", "Elisif", "Gerda", "Idgrod", "Laila", "Maven",
    "Rikke", "Sybille", "Thane", "Ysolda", "Jordis"
]

# Surnames - Commoner
NORD_SURNAMES_COMMONER = [
    "Battle-Born", "Gray-Mane", "Black-Briar", "Cruel-Sea", "Shatter-Shield", "Silver-Blood", "Vile-Man",
    "the Tall"
]

# Surnames - Noble
NORD_SURNAMES_NOBLE = [
    "Ice-Veins", "Snow-Shod", "Stormcloak", "War-Bear", "Winter-Gate", "Stone-Fist", "Fire-Mane",
    "Law-Giver", "the Unflinching", "the Fair", "Red-Hand", "White-Estrid"
]

# ### Redguard

# Male Names - Commoner
REDGUARD_MALE_NAMES_COMMONER = [
    "Kematu", "Nazir", "Azzin", "Ahlam", "Fihada", "Isran", "Jalil", "Nazeem", "Razan", "Saadia",
    "Virkmund", "Wayn", "Brenuin", "Kayd", "Talsgar"
]

# Male Names - Noble
REDGUARD_MALE_NAMES_NOBLE = [
    "Kasim", "Husni", "Mustafa", "Yusuf", "Malik", "Aziz", "Farid", "Hanan", "Jibril", "Nabil",
    "Qasim", "Samir", "Tariq", "Zayn", "Jawanan"
]

# Female Names - Commoner
REDGUARD_FEMALE_NAMES_COMMONER = [
    "Zariya", "Ayana", "Jamila", "Dalia", "Iman", "Layla", "Nadia", "Salma", "Shavari", "Yasmin",
    "Zahra", "Farah", "Anwen", "Lamiya", "Saadia"
]

# Female Names - Noble
REDGUARD_FEMALE_NAMES_NOBLE = [
    "Naima", "Safiya", "Aaliyah", "Fatima", "Samira", "Aisha", "Halima", "Karima", "Rania", "Sabina",
    "Soraya", "Thania", "Zainab", "Zafira", "Shada"
]

# Surnames
REDGUARD_SURNAMES = [
    "Iman", "Serrano", "Sali", "At-Tarik", "Benam", "Omar", "Hassan", "Zahra", "al-Alim", "al-Hassan",
    "al-Jabir", "al-Qam", "al-Walid", "Ben-Youssef", "ibn-Hasan", "ibn-Rashid"
]

# ### Breton

# Male Names - Commoner
BRETON_MALE_NAMES_COMMONER = [
    "Jean", "Luc", "Pierre", "Arnol", "Cosnach", "Enmon", "Gaston", "Julien", "Maurice", "Pascal",
    "Rochus", "Simon", "Belrand", "Herve", "Odfel"
]

# Male Names - Noble
BRETON_MALE_NAMES_NOBLE = [
    "Alain", "Thierry", "Gilles", "Remy", "Etienne", "Amaund", "Delacroix", "Francois", "Guillaume",
    "Matthieu", "Philippe", "Sebastien", "Tristan", "Vard", "Anton"
]

# Female Names - Commoner
BRETON_FEMALE_NAMES_COMMONER = [
    "Sophie", "Nathalie", "Isabelle", "Antoinette", "Babette", "Colette", "Genevieve", "Jolie", "Lisette",
    "Odette", "Simone", "Veronique", "Anise", "Fianna", "Susanna"
]

# Female Names - Noble
BRETON_FEMALE_NAMES_NOBLE = [
    "Camille", "Celine", "Margot", "Amelie", "Manon", "Adeline", "Eleonore", "Ffion", "Genevieve",
    "Helene", "Isolde", "Jacqueline", "Madeleine", "Seraphine", "Vivienne"
]

# Surnames - Commoner
BRETON_SURNAMES_COMMONER = [
    "Beaufort", "Dupont", "Aubin", "Bernard", "Leonce", "Motte", "Liric", "Rane"
]

# Surnames - Noble
BRETON_SURNAMES_NOBLE = [
    "Gauthier", "Lambert", "Moreau", "Renaud", "Vincent", "Leclerc", "Aumont", "Chastel", "Montclair",
    "Rochelle", "Valois", "de Savin"
]

# ### Dark Elf (Dunmer)

# Male Names - Commoner
DARK_ELF_MALE_NAMES_COMMONER = [
    "Ravan", "Varvur", "Arvel", "Athis", "Brand-Shei", "Dravynea", "Erandur", "Garyn", "Lleril", "Revyn",
    "Slitter", "Tythis", "Faryl", "Romlyn", "Teldryn"
]

# Male Names - Noble
DARK_ELF_MALE_NAMES_NOBLE = [
    "Balen", "Faron", "Rolis", "Taron", "Neloth", "Adril", "Gothren", "Indoril", "Malur", "Nelvayn",
    "Soris", "Theron", "Veleth", "Zathrian", "Divayth"
]

# Female Names - Commoner
DARK_ELF_FEMALE_NAMES_COMMONER = [
    "Aryni", "Bralen", "Feleth", "Brelyna", "Dinya", "Ildari", "Jenassa", "Llavela", "Niluva", "Sosia",
    "Voldsea", "Avrusa", "Aduri", "Ildene", "Suvaris"
]

# Female Names - Noble
DARK_ELF_FEMALE_NAMES_NOBLE = [
    "Mirri", "Rilen", "Teleri", "Varona", "Alvela", "Arara", "Bralsa", "Dreyla", "Ildene", "Malsa",
    "Nenya", "Sulvi", "Tilse", "Voldrani", "Karliah"
]

# Surnames - Commoner
DARK_ELF_SURNAMES_COMMONER = [
    "Andrethi", "Baloren", "Hlaalu", "Maryon", "Sadri", "Ulen", "Atheron", "Sarys"
]

# Surnames - Noble
DARK_ELF_SURNAMES_NOBLE = [
    "Darethi", "Nerethi", "Sarethi", "Uvarethi", "Velethi", "Andas", "Dren", "Hleran", "Rethan",
    "Telvanni", "Indarys", "Redoran"
]

# ### High Elf (Altmer)

# Male Names - Commoner
HIGH_ELF_MALE_NAMES_COMMONER = [
    "Ancano", "Elenwen", "Ondolemar", "Linwe", "Melaran", "Nirion", "Orion", "Rulindil", "Taen", "Voranil",
    "Aicantar", "Volanaro", "Nelacar", "Runil", "Vingalmo"
]

# Male Names - Noble
HIGH_ELF_MALE_NAMES_NOBLE = [
    "Thoron", "Talsgar", "Eridor", "Ulfgar", "Calcelmo", "Ario", "Estormo", "Faendal", "Mannimarco",
    "Quaranir", "Runil", "Vingalmo", "Anarion", "Pelidil", "Ocato"
]

# Female Names - Commoner
HIGH_ELF_FEMALE_NAMES_COMMONER = [
    "Elenwen", "Irileth", "Laranthir", "Faralda", "Linwe", "Miniel", "Nenya", "Seren", "Syndorie", "Tavari",
    "Viarmo", "Elenya", "Niranye", "Taarie", "Viola"
]

# Female Names - Noble
HIGH_ELF_FEMALE_NAMES_NOBLE = [
    "Niranye", "Talsgar", "Eridor", "Ulfgar", "Calcelmo", "Almalexia", "Ayrenn", "Curwe", "Lathenil",
    "Morgwen", "Nirniel", "Taarie", "Vanrie", "Elenari", "Emeric"
]

# Surnames - Commoner
HIGH_ELF_SURNAMES_COMMONER = [
    "Alinor", "Cloudrest", "Aurelion", "Indoril", "Silorn", "Valerius", "Lloran", "Sildar"
]

# Surnames - Noble
HIGH_ELF_SURNAMES_NOBLE = [
    "Elenwen", "Lillandril", "Silverlode", "Sunhold", "Winterhold", "Wintermoon", "Arana", "Camo",
    "Marayn", "Othela", "Soran", "Tarmia"
]

# ### Wood Elf (Bosmer)

# Male Names - Commoner
WOOD_ELF_MALE_NAMES_COMMONER = [
    "Faelar", "Glarthir", "Hircine", "Aengoth", "Celegorn", "Faen", "Gwildin", "Malborn", "Niron", "Thran",
    "Valen", "Aeran", "Faendal", "Grelod", "Valindor"
]

# Male Names - Noble
WOOD_ELF_MALE_NAMES_NOBLE = [
    "Ollar", "Orion", "Oron", "Orundil", "Owin", "Cindelin", "Eldamir", "Faelian", "Galathil", "Maenor",
    "Orthelon", "Rinon", "Saelorn", "Tauriel", "Aerendel"
]

# Female Names - Commoner
WOOD_ELF_FEMALE_NAMES_COMMONER = [
    "Aeri", "Owaen", "Orin", "Aela", "Cairine", "Elphina", "Glathriel", "Larethia", "Nivriel", "Saeldia",
    "Thaelen", "Anoriath", "Caminda", "Gilfre", "Nimphaneth"
]

# Female Names - Noble
WOOD_ELF_FEMALE_NAMES_NOBLE = [
    "Orynn", "Othari", "Owen", "Owinori", "Owinril", "Aranniel", "Cindiri", "Elanil", "Gwen", "Laenafil",
    "Nirrine", "Seren", "Thelama", "Elara", "Lyra"
]

# Surnames - Commoner
WOOD_ELF_SURNAMES_COMMONER = [
    "Aerion", "Camoran", "Green-Pact", "Heartwood", "Shadow-Walker", "Wild-Runner", "Black-Briar",
    "Swift-Arrow"
]

# Surnames - Noble
WOOD_ELF_SURNAMES_NOBLE = [
    "Elenwen", "Faelar", "Glarthir", "Orion", "Oron", "Orundil", "Arroway", "Black-Arrow", "Green-Leaf",
    "Swift-Elk", "Thorn-Stalker", "Whisper-Wind"
]

# ### Orc (Orsimer)

# Male Names - Commoner
ORC_MALE_NAMES_COMMONER = [
    "Gat gro-Shargak", "Ugak gra-Mogakh", "Yatul gro-Gnash", "Bashuk", "Durzod", "Ghorbash", "Larak",
    "Murbul", "Ogrul", "Shagrol", "Urag", "Yamarz", "Gat", "Ghorza", "Mogrul"
]

# Male Names - Noble
ORC_MALE_NAMES_NOBLE = [
    "Burz gro-Kharbush", "Lagdub gro-Gaturn", "Mog gro-Korgnak", "Oglub gro-Dum", "Shagdub gro-Ular",
    "Ghorak", "Kharag", "Lurog", "Mogdurz", "Ornag", "Sharamph", "Ulgush", "Yargol", "Borgakh", "Grommok"
]

# Female Names - Commoner
ORC_FEMALE_NAMES_COMMONER = [
    "Borgakh Steel-Heart", "Durbul gro-Gamurz", "Ghob gra-Magul", "Atub", "Bagrak", "Gharol", "Lash",
    "Mog", "Shuftharz", "Ugor", "Yatul", "Garakh", "Bashnag", "Sharn", "Uglarz"
]

# Female Names - Noble
ORC_FEMALE_NAMES_NOBLE = [
    "Maz gro-Kilav", "Olub gra-Gaturn", "Shuftharz gra-Gaturn", "Tug gra-Mogakh", "Urzoga gra-Batul",
    "Batul", "Dura", "Ghorza", "Mazoga", "Oglub", "Sharn", "Urzoga", "Yashnag", "Borba", "Shel"
]

# Surnames - Commoner
ORC_SURNAMES_COMMONER = [
    "gro-Bagrat", "gra-Bashnag", "gro-Shurkul", "gra-Bumph", "gro-Khazun", "gra-Sharob", "gro-Largash",
    "gra-Dushnikh"
]

# Surnames - Noble
ORC_SURNAMES_NOBLE = [
    "gro-Demnik", "gra-Gaturn", "gro-Ghorza", "gra-Kharbush", "gro-Mogakh", "gra-Muzgob", "gro-Dushnikh",
    "gra-Largash", "gro-Mor-Khazgur", "gra-Narzulbur", "gro-Yazgul", "gra-Dush"
]

# ### Argonian

# Male Names - Commoner
ARGONIAN_MALE_NAMES_COMMONER = [
    "Derkeethus", "Hides-His-Heart", "Jaree-Ra", "Beem-Ja", "Chal-Ma", "Mee-Jur", "Nee-Sa", "Ree-Zish",
    "Skee-Tei", "Tal-Jei", "Vee-Daza", "Wee-Na", "Madesi", "Neetrenaza", "Teeba-Ei"
]

# Male Names - Noble
ARGONIAN_MALE_NAMES_NOBLE = [
    "Keerava", "Sky-Shimmer", "Teinaava", "Wujeeta", "Zaquarius", "Ashee-Meeko", "Chee-Sei", "Erh-Jee",
    "Haj-Maar", "Mee-See", "Peesh-Ja", "Ree-Nakal", "Sees-All-Colors", "Uka-Zei", "Veezara"
]

# Female Names - Commoner
ARGONIAN_FEMALE_NAMES_COMMONER = [
    "Deetum-Ja", "Hides-Her-Cache", "Jana-Millia", "Dee-Meese", "Gee-Ska", "Haj-Sira", "Kee-Rani",
    "Mee-To", "Paa-Ween", "Ree-Zishka", "See-Nee", "Tee-Wee", "Brand-Shei", "Shavee", "Wujeeta"
]

# Female Names - Noble
ARGONIAN_FEMALE_NAMES_NOBLE = [
    "Keerava", "Sky-Shimmer", "Teinaava", "Wujeeta", "Zaquarius", "An-Jeen", "Chee-Sa", "Ena-Mei",
    "Hee-Sa", "Jee-Mei", "Mee-Nee", "Ree-Neeus", "Shee-Mei", "Uta-Tei", "Zarain"
]

# Surnames - Commoner
ARGONIAN_SURNAMES_COMMONER = [
    "-Dar", "-Ei", "-Kaj", "-Ra", "-Sei", "-Zish", "-Ka", "-Tee"
]

# Surnames - Noble
ARGONIAN_SURNAMES_NOBLE = [
    "-Ja", "-Lei", "-Mei", "-Neeus", "-Qei", "-Teeus", "-Jee", "-Keeus", "-Nakal", "-Shei", "-Tee", "-Zul"
]

# ### Khajiit

# Male Names - Commoner
KHAJIIT_MALE_NAMES_COMMONER = [
    "J'zargo", "M'aiq the Liar", "Ri'saad", "Kharjo", "Ma'dran", "Ra'zhinda", "Shavir", "Tsarr", "Zayhad",
    "Dro'marash", "Jobasha", "Ra'jirr", "Ma'tasarr", "Ri'kasha", "Za'zhar"
]

# Male Names - Noble
KHAJIIT_MALE_NAMES_NOBLE = [
    "Dro'marash", "J'datharr", "M'dirr", "Ri'zakar", "Dro'shanji", "Ahzirr", "Do'rhen", "J'zhad", "Ma'jhad",
    "Q'a-jhan", "Ra'shad", "S'krivva", "Tesar", "Za'rabi", "J'Ghasta"
]

# Female Names - Commoner
KHAJIIT_FEMALE_NAMES_COMMONER = [
    "Ahkari", "Tsrava", "Zaynabi", "Atahbah", "Kishashi", "Ma'jida", "Ra'shida", "Shuravi", "Tsra'ni",
    "Zabani", "Ahjara", "Dro'bara", "Kishra", "Ra'ava", "Shavari"
]

# Female Names - Noble
KHAJIIT_FEMALE_NAMES_NOBLE = [
    "Adara", "Hadia", "Imani", "Kaliyah", "Safiya", "Abanji", "Ahnissi", "Do'rashi", "K'sharr",
    "M'raaj-Dar", "Ra'zana", "Shuzura", "Tslani", "Ziss'r", "Thjoto"
]

# Surnames - Commoner
KHAJIIT_SURNAMES_COMMONER = [
    "-Dar", "-Dro", "-Daro", "-Jasa", "-Kato", "-Sien", "-Dara", "-Jhad"
]

# Surnames - Noble
KHAJIIT_SURNAMES_NOBLE = [
    "-Jo", "-Li", "-Ma", "-Ri", "-Sa", "-Zo", "-Jadd", "-Krin", "-Rava", "-Shav", "-Tani", "-Zar"
]

def get_random_name(race: Race, gender: Gender, tags: dict, name_type: str = None):
    if race == Race.IMPERIAL:
        if gender == Gender.MALE:
            names = IMPERIAL_MALE_NAMES_COMMONER + IMPERIAL_MALE_NAMES_NOBLE
        else:
            names = IMPERIAL_FEMALE_NAMES_COMMONER + IMPERIAL_FEMALE_NAMES_NOBLE
        surnames = IMPERIAL_SURNAMES_COMMONER + IMPERIAL_SURNAMES_NOBLE
    elif race == Race.NORD:
        if gender == Gender.MALE:
            names = NORD_MALE_NAMES_COMMONER + NORD_MALE_NAMES_NOBLE
        else:
            names = NORD_FEMALE_NAMES_COMMONER + NORD_FEMALE_NAMES_NOBLE
        surnames = NORD_SURNAMES_COMMONER + NORD_SURNAMES_NOBLE
    elif race == Race.REDGUARD:
        if gender == Gender.MALE:
            names = REDGUARD_MALE_NAMES_COMMONER + REDGUARD_MALE_NAMES_NOBLE
        else:
            names = REDGUARD_FEMALE_NAMES_COMMONER + REDGUARD_FEMALE_NAMES_NOBLE
        surnames = REDGUARD_SURNAMES
    elif race == Race.BRETON:
        if gender == Gender.MALE:
            names = BRETON_MALE_NAMES_COMMONER + BRETON_MALE_NAMES_NOBLE
        else:
            names = BRETON_FEMALE_NAMES_COMMONER + BRETON_FEMALE_NAMES_NOBLE
        surnames = BRETON_SURNAMES_COMMONER + BRETON_SURNAMES_NOBLE
    elif race == Race.DUNMER:
        if gender == Gender.MALE:
            names = DARK_ELF_MALE_NAMES_COMMONER + DARK_ELF_MALE_NAMES_NOBLE
        else:
            names = DARK_ELF_FEMALE_NAMES_COMMONER + DARK_ELF_FEMALE_NAMES_NOBLE
        surnames = DARK_ELF_SURNAMES_COMMONER + DARK_ELF_SURNAMES_NOBLE
    elif race == Race.ALTMER:
        if gender == Gender.MALE:
            names = HIGH_ELF_MALE_NAMES_COMMONER + HIGH_ELF_MALE_NAMES_NOBLE
        else:
            names = HIGH_ELF_FEMALE_NAMES_COMMONER + HIGH_ELF_FEMALE_NAMES_NOBLE
        surnames = HIGH_ELF_SURNAMES_COMMONER + HIGH_ELF_SURNAMES_NOBLE
    elif race == Race.BOSMER:
        if gender == Gender.MALE:
            names = WOOD_ELF_MALE_NAMES_COMMONER + WOOD_ELF_MALE_NAMES_NOBLE
        else:
            names = WOOD_ELF_FEMALE_NAMES_COMMONER + WOOD_ELF_FEMALE_NAMES_NOBLE
        surnames = WOOD_ELF_SURNAMES_COMMONER + WOOD_ELF_SURNAMES_NOBLE
    elif race == Race.ORC:
        if gender == Gender.MALE:
            names = ORC_MALE_NAMES_COMMONER + ORC_MALE_NAMES_NOBLE
        else:
            names = ORC_FEMALE_NAMES_COMMONER + ORC_FEMALE_NAMES_NOBLE
        surnames = ORC_SURNAMES_COMMONER + ORC_SURNAMES_NOBLE
    elif race == Race.ARGONIAN:
        if gender == Gender.MALE:
            names = ARGONIAN_MALE_NAMES_COMMONER + ARGONIAN_MALE_NAMES_NOBLE
        else:
            names = ARGONIAN_FEMALE_NAMES_COMMONER + ARGONIAN_FEMALE_NAMES_NOBLE
        surnames = ARGONIAN_SURNAMES_COMMONER + ARGONIAN_SURNAMES_NOBLE
    elif race == Race.KHAJIIT:
        if gender == Gender.MALE:
            names = KHAJIIT_MALE_NAMES_COMMONER + KHAJIIT_MALE_NAMES_NOBLE
        else:
            names = KHAJIIT_FEMALE_NAMES_COMMONER + KHAJIIT_FEMALE_NAMES_NOBLE
        surnames = KHAJIIT_SURNAMES_COMMONER + KHAJIIT_SURNAMES_NOBLE
    else:
        raise ValueError("Unknown race: {}".format(race))
    
    name = random.choice(names)
    surname = random.choice(surnames)
    return f"{name}{surname}" if surname.startswith('-') else f"{name} {surname}"

def generate_npc_name(race: Race, gender: Gender, tags: dict, name_type: str = None):
    return get_random_name(race, gender, tags, name_type)

NAME_POOLS = {
    "imperial": {
        "noble": {
            "male": IMPERIAL_MALE_NAMES_NOBLE,
            "female": IMPERIAL_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": IMPERIAL_MALE_NAMES_COMMONER,
            "female": IMPERIAL_FEMALE_NAMES_COMMONER
        }
    },
    "nord": {
        "noble": {
            "male": NORD_MALE_NAMES_NOBLE,
            "female": NORD_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": NORD_MALE_NAMES_COMMONER,
            "female": NORD_FEMALE_NAMES_COMMONER
        }
    },
    "redguard": {
        "commoner": {
            "male": REDGUARD_MALE_NAMES_COMMONER,
            "female": REDGUARD_FEMALE_NAMES_COMMONER
        },
        "noble": {
            "male": REDGUARD_MALE_NAMES_NOBLE,
            "female": REDGUARD_FEMALE_NAMES_NOBLE
        }
    },
    "breton": {
        "noble": {
            "male": BRETON_MALE_NAMES_NOBLE,
            "female": BRETON_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": BRETON_MALE_NAMES_COMMONER,
            "female": BRETON_FEMALE_NAMES_COMMONER
        }
    },
    "dunmer": {
        "noble": {
            "male": DARK_ELF_MALE_NAMES_NOBLE,
            "female": DARK_ELF_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": DARK_ELF_MALE_NAMES_COMMONER,
            "female": DARK_ELF_FEMALE_NAMES_COMMONER
        }
    },
    "altmer": {
        "noble": {
            "male": HIGH_ELF_MALE_NAMES_NOBLE,
            "female": HIGH_ELF_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": HIGH_ELF_MALE_NAMES_COMMONER,
            "female": HIGH_ELF_FEMALE_NAMES_COMMONER
        }
    },
    "bosmer": {
        "noble": {
            "male": WOOD_ELF_MALE_NAMES_NOBLE,
            "female": WOOD_ELF_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": WOOD_ELF_MALE_NAMES_COMMONER,
            "female": WOOD_ELF_FEMALE_NAMES_COMMONER
        }
    },
    "orc": {
        "noble": {
            "male": ORC_MALE_NAMES_NOBLE,
            "female": ORC_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": ORC_MALE_NAMES_COMMONER,
            "female": ORC_FEMALE_NAMES_COMMONER
        }
    },
    "argonian": {
        "noble": {
            "male": ARGONIAN_MALE_NAMES_NOBLE,
            "female": ARGONIAN_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": ARGONIAN_MALE_NAMES_COMMONER,
            "female": ARGONIAN_FEMALE_NAMES_COMMONER
        }
    },
    "khajiit": {
        "noble": {
            "male": KHAJIIT_MALE_NAMES_NOBLE,
            "female": KHAJIIT_FEMALE_NAMES_NOBLE
        },
        "commoner": {
            "male": KHAJIIT_MALE_NAMES_COMMONER,
            "female": KHAJIIT_FEMALE_NAMES_COMMONER
        }
    }
}