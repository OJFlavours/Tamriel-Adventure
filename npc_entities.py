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

# ... (NOBLE_ROLES, COMMONER_ROLES, HOSTILE_ROLES sets remain here) ...
NOBLE_ROLES = {...}
COMMONER_ROLES = {...}
HOSTILE_ROLES = {...}
FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES


class NPC:
    def __init__(self, name: str, race: str, role: str, level: int, disposition: int = 50, gold: int = 0, patrol_route: List[str] = None, location_context: dict = None):
        self.race = race.lower() if race else "nord"
        self.role = role
        self.level = max(1, level)
        self.disposition = disposition
        self.gold = gold
        self.location_context = location_context # <-- STORE LOCATION CONTEXT
        # ... (rest of __init__ is the same) ...
        self.has_offered_quest = False
        # ...
        self._generate_name_and_id(name)
        # ... (rest of __init__ calls) ...

    def _generate_name_and_id(self, name: str):
        if name is None:
            gender = random.choice(["male", "female"])
            name_type = "noble" if self.role in NOBLE_ROLES else "commoner"
            
            # This part for getting first name remains largely the same
            race_name_pool_data = NAME_POOLS.get(self.race, NAME_POOLS.get("nord", {}))
            specific_name_pool = race_name_pool_data.get(name_type, race_name_pool_data.get("commoner", {}))
            gender_specific_pool = specific_name_pool.get(gender, [])
            if not gender_specific_pool:
                gender_specific_pool = [f"unknown_npc_{random.randint(10,99)}"]

            self.unique_id = random.choice(gender_specific_pool)
            first_name_base = self.unique_id.split('_')[0].capitalize()

            # --- REVISED SURNAME LOGIC ---
            final_surname = ""
            if self.race == "nord":
                # Use location context to find the right surname pool
                hold_name = self.location_context.get("hold_name", "generic") if self.location_context else "generic"
                surname_pool = NORD_SURNAMES.get(hold_name, NORD_SURNAMES["generic"])
                if surname_pool:
                    final_surname = random.choice(surname_pool)
            
            if final_surname:
                self.name = f"{first_name_base} {final_surname}"
            else:
                self.name = first_name_base
            # --- END OF REVISED LOGIC ---
        else:
            self.name = name
            self.unique_id = f"{self.name.lower().replace(' ', '_')}_{self.role.lower().replace(' ', '_')}_{random.randint(100,999)}"

    # ... (Rest of the NPC class methods remain unchanged) ...