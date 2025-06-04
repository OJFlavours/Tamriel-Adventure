# npc_roles.py

# Define roles that imply noble or commoner status
NOBLE_ROLES = {"noble", "jarl", "thane", "baron", "lady", "duke", "duchess", "court_mage", "advisor"}
COMMONER_ROLES = {
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand",
    "stormcloak_supporter", "imperial_citizen", "mage_apprentice", "warrior",
    "thief_lookout", "pickpocket", "guild_rogue", "db_initiate",
    "explorer", "sailor", "dock_worker", "ship_captain_ashore", "fishmonger", "acolyte", "temple_guardian",
    "stall_owner", "shop_assistant", "city_guard", "mine_foreman", "farmer_spouse",
    "server", "cook", "beggar", "elder"
}

# Define roles that are typically hostile
HOSTILE_ROLES = {
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "vampire", "vampire_thrall", "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thief",
    "draugr", "skeleton", "ghost",
    "bear", "wolf", "spider",
    "dwarven_sphere", "falmer", "chaurus",
    "mage", "cultist", "thalmor_justiciar"
}

FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES