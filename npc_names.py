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
# This structure can be expanded for other races (e.g., IMPERIAL_SURNAMES).

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
    # ... other races remain the same, without surname lists ...
    "imperial": {
        "noble": { "male": [...], "female": [...] },
        "commoner": { "male": [...], "female": [...] }
    },
    # etc.
}

# Assign unique IDs to first names
def assign_unique_npc_ids(name_pools):
    for race_data in name_pools.values():
        if "noble_surnames" in race_data: del race_data["noble_surnames"] # Clean up old keys if they exist
        if "commoner_surnames" in race_data: del race_data["commoner_surnames"]
        for name_type_data in race_data.values():
            for gender_name_list in name_type_data.values():
                if isinstance(gender_name_list, list):
                    for i in range(len(gender_name_list)):
                        original_name = gender_name_list[i].split('_')[0] # Ensure we work with a clean name
                        unique_id = f"{original_name.lower().replace(' ', '_')}_{random.randint(100, 999)}"
                        gender_name_list[i] = unique_id

assign_unique_npc_ids(NAME_POOLS)