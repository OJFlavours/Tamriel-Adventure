import random
from dialogue_greeting_data import (
    HOSTILE_GREETINGS,
    UNFRIENDLY_GREETINGS,
    NEUTRAL_GREETINGS,
    FRIENDLY_GREETINGS,
    ADMIRING_GREETINGS
)
from dialogue_purpose_data import (
    PURPOSE_DESCRIPTIONS,
    RACIAL_MODIFIERS,
    GENERIC_PURPOSES,
    ENTHUSIASM_MODIFIERS,
    CYNICAL_MODIFIERS
)

# --- UTILITY FUNCTIONS ---
def get_npc_context(npc, player, game_events):
    """
    Retrieves relevant context information about the NPC, player, and game events.
    """
    context = {
        "npc": {
            "name": npc.name,
            "role": npc.role,
            "race": npc.race,
            "disposition": npc.disposition,
            "attitude": npc.tags.get("npc", {}).get("attitude", "neutral"),
        },
        "player": {
            "name": player.name,
            "level": player.level,
            "reputation": player.reputation,
        },
        "game_events": game_events,
    }
    return context

def apply_template(template, context):
    """
    Applies a dialogue template by replacing placeholders with values from the context.
    """
    try:
        return template.format(**context["npc"], **context["player"], **context["game_events"])
    except KeyError as e:
        print(f"Error: Missing key in template context: {e}")
        return "I have nothing to say."

# --- GREETING GENERATION ---
def generate_greeting(npc, player, game_events) -> str:
    """Generate comprehensive, lore-friendly greetings based on NPC, player, and game events."""
    context = get_npc_context(npc, player, game_events)
    attitude = context["npc"]["attitude"]
    role_lower = context["npc"]["role"].lower()
    disposition = context["npc"]["disposition"]

    # Hostile greetings - always prioritize if hostile attitude
    if attitude == "hostile" or disposition < 20:
        # Prioritize specific hostile greetings based on role
        for role_key in HOSTILE_GREETINGS:
            if role_key in role_lower:
                return random.choice(HOSTILE_GREETINGS[role_key])
        # Fallback to a more generic hostile greeting
        return random.choice(HOSTILE_GREETINGS["default"])

    # Unfriendly but not hostile (20-40 disposition)
    elif disposition < 40:
        for role_key in UNFRIENDLY_GREETINGS:
            if role_key in role_lower:
                return random.choice(UNFRIENDLY_GREETINGS[role_key])
        return random.choice(UNFRIENDLY_GREETINGS["default"])

    # Neutral greetings (40-60 disposition)
    elif disposition < 60:
        for role_key in NEUTRAL_GREETINGS:
            if role_key in role_lower:
                return random.choice(NEUTRAL_GREETINGS[role_key])
        return random.choice(NEUTRAL_GREETINGS["default"])

    # Friendly greetings (60-80 disposition)
    elif disposition < 80:
        for role_key in FRIENDLY_GREETINGS:
            if role_key in role_lower:
                return random.choice(FRIENDLY_GREETINGS[role_key])
        return random.choice(FRIENDLY_GREETINGS["default"])

    # Very friendly/admiring greetings (80+ disposition)
    else:
        for role_key in ADMIRING_GREETINGS:
            if role_key in role_lower:
                return random.choice(ADMIRING_GREETINGS[role_key])
        return random.choice(ADMIRING_GREETINGS["default"])

# --- PURPOSE GENERATION ---
def generate_purpose(npc, player, game_events) -> str:
    """Generate comprehensive, lore-friendly purpose descriptions based on NPC, player, and game events."""
    context = get_npc_context(npc, player, game_events)
    role_lower = context["npc"]["role"].lower()
    race_lower = context["npc"]["race"].lower()
    disposition = context["npc"]["disposition"]

    # Ensure all purpose descriptions end with punctuation
    # This is done here to keep data files clean and focused on raw data
    # and to ensure dynamic modifications are handled correctly.
    processed_purpose_descriptions = {}
    for role_key, p_list in PURPOSE_DESCRIPTIONS.items():
        processed_purpose_descriptions[role_key] = [
            p + "." if not p.endswith(('.', '!', '?')) else p for p in p_list
        ]

    processed_racial_modifiers = {}
    for race_key, m_list in RACIAL_MODIFIERS.items():
        processed_racial_modifiers[race_key] = [
            m + "." if not m.endswith(('.', '!', '?')) else m for m in m_list
        ]
    
    processed_generic_purposes = [
        gp + "." if not gp.endswith(('.', '!', '?')) else gp for gp in GENERIC_PURPOSES
    ]


    base_purposes = []
    for role_key_iter in processed_purpose_descriptions:
        if role_key_iter in role_lower:
            base_purposes = processed_purpose_descriptions[role_key_iter]
            break

    if not base_purposes:
        base_purposes = processed_generic_purposes

    base_purpose = random.choice(base_purposes)

    if race_lower in processed_racial_modifiers and random.random() < 0.3:
        racial_addition = random.choice(processed_racial_modifiers[race_lower]).strip()
        base_purpose = base_purpose.rstrip('.') + f", {racial_addition}"

    if disposition >= 80:
        if random.random() < 0.4:
            modifier_text = random.choice(ENTHUSIASM_MODIFIERS).strip()
            # Ensure modifier_text itself ends with punctuation if it doesn't already
            if not modifier_text.endswith(('.', '!', '?')):
                modifier_text += "."
            base_purpose = base_purpose.rstrip('.') + f", {modifier_text}"

    elif disposition <= 30:
        if random.random() < 0.3:
            modifier_text = random.choice(CYNICAL_MODIFIERS).strip()
            # Ensure modifier_text itself ends with punctuation if it doesn't already
            if not modifier_text.endswith(('.', '!', '?')):
                modifier_text += "."
            base_purpose = base_purpose.rstrip('.') + f", {modifier_text}"

    base_purpose = base_purpose.strip()
    if not base_purpose.endswith(('.', '!', '?')):
        base_purpose += "."
            
    return base_purpose

# --- CUSTOM TEMPLATES ---
def generate_dialogue_from_template(npc, player, game_events, template):
    """
    Generates dialogue from a custom template, incorporating NPC, player, and game event context.
    """
    context = get_npc_context(npc, player, game_events)
    dialogue = apply_template(template, context)
    return dialogue

# --- TEMPLATE EFFECTS ---
def trigger_template_effect(effect_name, context):
    """
    Triggers an effect based on the given effect name and context.
    """
    effects = {
        "modify_disposition": modify_disposition,
        "start_quest": start_quest,
        # Add more effects here
    }

    if effect_name in effects:
        effects[effect_name](context)
    else:
        print(f"Error: Unknown template effect: {effect_name}")

def modify_disposition(context):
    """
    Modifies the NPC's disposition based on the template context.
    """
    npc = context["npc"]
    # Implement logic to modify disposition based on player actions or dialogue
    print(f"Modifying disposition of {npc['name']}")

def start_quest(context):
    """
    Starts a quest based on the template context.
    """
    player = context["player"]
    # Implement logic to start a quest for the player
    print(f"Starting quest for {player['name']}")