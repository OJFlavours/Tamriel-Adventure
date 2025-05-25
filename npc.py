import random
from stats import Stats, RACES # Import RACES directly from stats
from items import generate_random_item
from ui import UI
from quests import generate_location_appropriate_quest
from tags import TAGS, get_tags # Import TAGS and get_tags function
import flavor

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
            "male": ["Titus", "Valerius", "Cassius", "Hadrian", "Septimus"],
            "female": ["Serana", "Valeria", "Aurelia", "Livia", "Octavia"]
        },
        "commoner": {
            "male": ["Gaius", "Marcus", "Tiber", "Lucius", "Rufus"],
            "female": ["Claudia", "Julia", "Fausta", "Silvia", "Vespasia"]
        }
    },
    "breton": {
        "noble": {
            "male": ["Gaston", "Didier", "Armand", "Guillaume", "Thierry"],
            "female": ["Genevieve", "Isabelle", "Marguerite", "Annette", "Elodie"]
        },
        "commoner": {
            "male": ["Pierre", "Jean", "Louis", "François", "Antoine"],
            "female": ["Marie", "Sophie", "Jeanne", "Claire", "Nicole"]
        }
    },
    "redguard": {
        "noble": {
            "male": ["Ahmad", "Jamal", "Khalid", "Rashid", "Zafir"],
            "female": ["Zafira", "Yasmina", "Samira", "Layla", "Aisha"]
        },
        "commoner": {
            "male": ["Cyrus", "Nazir", "Kematu", "Sadir", "Malik"],
            "female": ["Imani", "Sana", "Nadia", "Zara", "Amina"]
        }
    },
    "dunmer": {
        "noble": {
            "male": ["Indoril", "Redoran", "Telvanni", "Dres", "Hlaalu"],
            "female": ["Morwen", "Fjola", "Jenassa", "Brelyna", "Aranea"]
        },
        "commoner": {
            "male": ["Brand-Shei", "Revyn", "Adril", "Malborn", "M'aiq"],
            "female": ["Jenassa", "Fethis", "Mogrul", "Nilene", "Revyn"]
        }
    },
    "altmer": {
        "noble": {
            "male": ["Ancano", "Ondolemar", "Elenwen", "Rulindil", "Estormo"],
            "female": ["Elenwen", "Ancano", "Rulindil", "Estormo", "Ondolemar"]
        },
        "commoner": {
            "male": ["Faralda", "Calcelmo", "Entir", "Runil", "Ursa"],
            "female": ["Faralda", "Calcelmo", "Entir", "Runil", "Ursa"]
        }
    },
    "bosmer": {
        "noble": {
            "male": ["Gat", "Faelan", "Niruin", "Borvir", "Maluril"],
            "female": ["Niruin", "Borvir", "Maluril", "Gat", "Faelan"]
        },
        "commoner": {
            "male": ["Faendal", "Hadvar", "Ralof", "Sven", "Alvor"],
            "female": ["Camilla", "Sigrid", "Gerdur", "Hroki", "Idgrod"]
        }
    },
    "orc": {
        "noble": {
            "male": ["Ghorbash", "Urag", "Yashnag", "Burguk", "Dushnikh"],
            "female": ["Urag", "Yashnag", "Burguk", "Dushnikh", "Ghorbash"]
        },
        "commoner": {
            "male": ["Grogmar", "Muzgon", "Shagrol", "Urzoga", "Yamorz"],
            "female": ["Urzoga", "Yamorz", "Grogmar", "Muzgon", "Shagrol"]
        }
    },
    "argonian": {
        "noble": {
            "male": ["J'zargo", "Derkeethus", "Stands-In-Shadows", "Walks-Softly", "Hides-His-Eyes"],
            "female": ["Shahvee", "Keerava", "From-Deepest-Fathoms", "Scales-of-Steel", "Swims-In-Deep-Waters"]
        },
        "commoner": {
            "male": ["J'zargo", "Derkeethus", "Stands-In-Shadows", "Walks-Softly", "Hides-His-Eyes"],
            "female": ["Shahvee", "Keerava", "From-Deepest-Fathoms", "Scales-of-Steel", "Swims-In-Deep-Waters"]
        }
    },
    "khajiit": {
        "noble": {
            "male": ["J'zargo", "Ma'iq", "Dro'marash", "Ra'virr", "Ri'saad"],
            "female": ["Ahkari", "Kharjo", "Razhinda", "Zaynabi", "Shavari"]
        },
        "commoner": {
            "male": ["J'zargo", "Ma'iq", "Dro'marash", "Ra'virr", "Ri'saad"],
            "female": ["Ahkari", "Kharjo", "Razhinda", "Zaynabi", "Shavari"]
        }
    },
}


class NPC:
    """
    Represents a Non-Player Character in the Skyrim Adventure game.
    NPCs have stats, a role, disposition, and can engage in dialogue.
    """
    def __init__(self, name: str, race: str, role: str, level: int, disposition: int = 50, gold: int = 0):
        # Generate name if not provided
        if name is None:
            gender = random.choice(["male", "female"])
            # Determine if noble or commoner role based on role tag
            name_type = "noble" if role in NOBLE_ROLES else "commoner"
            # Get names for the specific race, default to Nord if race not found in NAME_POOLS
            race_names = NAME_POOLS.get(race.lower(), NAME_POOLS["nord"])
            name_pool = race_names.get(name_type, race_names["commoner"])
            self.name = random.choice(name_pool.get(gender, name_pool["male"])) # Default to male if gender pool missing
        else:
            self.name = name

        self.race = race
        self.role = role
        self.level = level
        self.disposition = disposition # How much they like the player (0-100)
        self.gold = gold

        # Initialize stats for the NPC
        self.stats = Stats(
            strength=random.randint(30, 60),
            intelligence=random.randint(30, 60),
            willpower=random.randint(30, 60),
            agility=random.randint(30, 60),
            speed=random.randint(30, 60),
            endurance=random.randint(30, 60),
            personality=random.randint(30, 60),
            luck=random.randint(30, 60),
            level=level,
            gold=gold
        )
        # Apply racial modifiers to NPC stats
        race_mods = RACES.get(race.lower(), {}) # Correctly access RACES imported from stats
        self.stats.strength += race_mods.get("strength_mod", 0)
        self.stats.intelligence += race_mods.get("intelligence_mod", 0)
        self.stats.willpower += race_mods.get("willpower_mod", 0)
        self.stats.agility += race_mods.get("agility_mod", 0)
        self.stats.speed += race_mods.get("speed_mod", 0)
        self.stats.endurance += race_mods.get("endurance_mod", 0)
        self.stats.personality += race_mods.get("personality_mod", 0)
        self.stats.luck += race_mods.get("luck_mod", 0)
        self.stats.poison_resist += race_mods.get("poison_resist", 0)
        self.stats.magic_resist += race_mods.get("magic_resist", 0)
        self.stats.frost_resist += race_mods.get("frost_resist", 0)
        self.stats.shock_resist += race_mods.get("shock_resist", 0)
        self.stats.fire_resist += race_mods.get("fire_resist", 0)

        # Update max health/magicka/fatigue based on new attributes
        self.stats.max_health = 100 + (self.stats.endurance * 2)
        self.stats.max_magicka = 50 + (self.stats.intelligence * 1.5)
        self.stats.max_fatigue = 100 + (self.stats.endurance * 1.5)
        self.stats.current_health = self.stats.max_health
        self.stats.current_magicka = self.stats.max_magicka
        self.stats.current_fatigue = self.stats.max_fatigue

        # Skills for NPCs (simplified, can be expanded based on role/class)
        self.skills = {}
        # Example: Bandits might have one_handed skill
        if self.role.lower() == "bandit":
            self.skills["one_handed"] = random.randint(20, 50)
            self.skills["light_armor"] = random.randint(15, 40)
        elif self.role.lower() == "mage":
            self.skills["destruction"] = random.randint(20, 50)
            self.skills["restoration"] = random.randint(15, 40)
        # Add more skill initialization based on NPC roles/classes

        self.inventory = self.stats.inventory # NPC inventory managed by Stats
        self.equipment = [] # NPCs can have equipment too
        self.status_effects = [] # List to hold StatusEffect objects

        # Tags for the NPC
        self.tags = {}
        self.add_tag("npc", "class", role)
        self.add_tag("npc", "race", race)
        self.add_tag("npc", "attitude", "hostile" if role in HOSTILE_ROLES else "friendly")
        # Add more tags based on NPC properties or randomly generated ones

        # Dialogue properties
        self.greeting = self._generate_greeting()
        self.purpose = self._generate_purpose()

    def __str__(self):
        return f"{self.name} ({self.role}, Level {self.level})"

    def add_tag(self, category, key, value):
        """Adds a tag to the NPC."""
        if category not in self.tags:
            self.tags[category] = {}
        self.tags[category][key] = value

    def _generate_greeting(self):
        """Generates a greeting based on disposition and role."""
        if self.disposition >= 70:
            return random.choice(["Greetings, friend!", "Well met!", "A pleasure to see you."])
        elif self.disposition >= 30:
            return random.choice(["Hello.", "What do you want?", "State your business."])
        else:
            return random.choice(["Stay out of my way.", "You're not welcome here.", "Hmph."])

    def _generate_purpose(self):
        """Generates a purpose based on role."""
        if self.role.lower() == "merchant":
            return random.choice(["buy and sell goods.", "trade with travelers.", "find rare wares."])
        elif self.role.lower() == "guard":
            return random.choice(["keep the peace.", "protect the city.", "enforce the law."])
        elif self.role.lower() == "bandit":
            return random.choice(["take what's mine.", "ambush travelers.", "cause trouble."])
        else:
            return random.choice(["do my duties.", "live my life.", "seek adventure."])

    def share_rumor(self, current_location) -> None:
        """Shares a rumor based on the NPC's disposition and location tags."""
        if self.disposition < 40:
            UI.slow_print(f"“I don't have time for idle chatter, adventurer.”") # Changed player_role_tag to adventurer
            return

        # Get relevant rumor topics from DIALOGUE tags
        rumor_topics = TAGS["DIALOGUE"]["topic"]
        available_rumors = [r for r in rumor_topics if r in ["gossip", "rumor", "lore"]]

        if not available_rumors:
            UI.slow_print("“I’ve heard nothing of interest lately.”")
            return

        chosen_topic = random.choice(available_rumors)
        # Use flavor vignettes related to the topic or location
        vignettes = flavor.DIALOGUE_FLAVORS.get("topic", {}).get(chosen_topic, []) # Corrected access to DIALOGUE_FLAVORS
        if not vignettes:
            vignettes = flavor.LOCATION_FLAVORS.get("environment", {}).get(random.choice(current_location.get("tags", ["urban"])), [])

        if vignettes:
            UI.slow_print(f"“{random.choice(vignettes)}”")
        else:
            UI.slow_print("“I’ve heard nothing of interest lately.”")

    def dialogue(self, player, current_location) -> None:
        """Handles dialogue interaction with the player."""
        UI.slow_print(f"You approach {self}. Disposition: {self.disposition}")
        UI.slow_print(f"“{self.greeting} I {self.purpose}”")
        options = ["[1] Rumor", "[2] Work", "[3] This Place", "[4] Quest", "[5] Farewell"]
        while True:
            for i, opt in enumerate(options, 1):
                print(f"[{i}] {opt}")
            choice = input("Choose: ")
            if choice == "1":
                self.share_rumor(current_location)
            elif choice == "2":
                UI.slow_print(f"“I {self.purpose}”")
            elif choice == "3":
                # Get location flavor based on tags
                location_tags = current_location.get("tags", [])
                environment_tags = [tag for tag in location_tags if tag in TAGS["LOCATIONS"]["environment"]]
                if environment_tags:
                    chosen_env_tag = random.choice(environment_tags)
                    vignettes = flavor.LOCATION_FLAVORS.get("environment", {}).get(chosen_env_tag, [])
                    if vignettes:
                        UI.slow_print(f"“{random.choice(vignettes)}”")
                    else:
                        UI.slow_print("“Just another place.”")
                else:
                    UI.slow_print("“Just another place.”")
            elif choice == "4":
                quest = generate_location_appropriate_quest(player.level, current_location.get("tags", []))
                UI.slow_print(f"“{quest.description}”")
                if hasattr(player, "quest_log") and player.quest_log is not None:
                    # In a real game, you'd ask the player if they accept the quest
                    player.quest_log.add_quest(quest) # Add quest directly to player's quest_log object
                    UI.slow_print("You have accepted a new quest!")
                else:
                    UI.slow_print("You have no way to track this quest.")
            elif choice == "5":
                UI.slow_print(f"“Farewell, {player.name}.”")
                break
            else:
                UI.slow_print("Your will wavers.")
