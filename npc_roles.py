# npc_roles.py

# This file defines the various roles NPCs can have in the world,
# categorized for use by the NPC generation system.

# --- Roles for Random Generation ---
# These sets are used to create generic, unnamed NPCs to populate the world.
# Unique, high-status roles (like Jarl, Emperor) are excluded here and should
# only be assigned to specific characters in fixed_npc_data.py.

NOBLE_ROLES = {
    "noble",
    "thane",
    "steward",
    "court_wizard",
    "advisor",
}

COMMONER_ROLES = {
    # Basic Professions
    "merchant", "guard", "farmer", "hunter", "priest", "adventurer", "blacksmith", "healer",
    "innkeeper", "bard", "scholar", "miner", "laborer", "citizen", "traveler", "farm_hand",
    "alchemist", "fletcher", "lumberjack", "woodcutter", "ferryman", "carriage_driver",
    "pawnbroker", "shopkeeper", "beggar", "elder", "child", "courier", "executioner",

    # Faction-Specific (Non-Hostile)
    "companion", "college_mage", "blade", "greybeard", "vigilant_of_stendarr",
    "penitus_oculatus", "thieves_guild_member", "dark_brotherhood_member",
    "imperial_soldier", "stormcloak_soldier", "orc_stronghold_member",

    # Misc Roles
    "mercenary", "pilgrim", "refugee"
}

HOSTILE_ROLES = {
    # Humanoid Enemies
    "bandit", "bandit_raider", "bandit_scout", "bandit_thug", "bandit_archer", "bandit_leader",
    "necromancer", "warlock", "conjurer", "illusionist", "pyromancer",
    "vampire", "vampire_thrall", "vampire_lord",
    "forsworn_raider", "forsworn_shaman", "forsworn_briarheart",
    "thalmor_justiciar", "thalmor_soldier", "reaver", "cultist", "silver_hand",

    # Undead
    "draugr", "draugr_wight", "draugr_scourge", "draugr_deathlord",
    "skeleton", "ghost", "wraith", "dragon_priest",

    # Creatures
    "wolf", "ice_wolf", "bear", "cave_bear", "snow_bear",
    "spider", "frostbite_spider", "troll", "frost_troll",
    "hagraven", "spriggan", "wisp", "wispmother", "ice_wraith",
    "giant", "mammoth",

    # Daedra & Constructs
    "dremora", "atronach_flame", "atronach_frost", "atronach_storm",
    "dwarven_sphere", "dwarven_spider", "dwarven_centurion",

    # Subterranean
    "falmer", "falmer_shaman", "chaurus", "chaurus_hunter"
}

# Combined set for all non-hostile NPCs, calculated automatically
FRIENDLY_ROLES = COMMONER_ROLES.union(NOBLE_ROLES) - HOSTILE_ROLES