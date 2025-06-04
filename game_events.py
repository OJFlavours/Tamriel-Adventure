from datetime import datetime

class GameEvent:
    """
    Represents a time-dependent event in the game.
    """
    def __init__(self, name, trigger_condition_func, action_func, description="", one_time=False, cooldown_hours=0):
        self.name = name
        self.trigger_condition_func = trigger_condition_func  # Args: game_time, player, current_location
        self.action_func = action_func  # Args: game_time, player, current_location, npc_registry, game_locations_map, ui
        self.description = description
        self.one_time = one_time
        self.has_triggered = False
        self.cooldown_hours = cooldown_hours # Cooldown in game hours
        self.last_triggered_time = None

    def can_trigger(self, game_time, player, current_location):
        """Checks if the event's conditions are met and it's not on cooldown or already triggered (if one_time)."""
        if self.one_time and self.has_triggered:
            return False

        if self.last_triggered_time and self.cooldown_hours > 0:
            time_since_last_trigger = game_time - self.last_triggered_time
            if time_since_last_trigger.total_seconds() < self.cooldown_hours * 3600: # 3600 seconds in an hour
                return False
        
        return self.trigger_condition_func(game_time, player, current_location)

    def trigger(self, game_time, player, current_location, npc_registry, game_locations_map, ui):
        """Executes the event's action and updates its state."""
        if self.description:
            ui.print_event_message(f"{self.description}") # Using a new UI method for event messages
        
        self.action_func(game_time, player, current_location, npc_registry, game_locations_map, ui)
        self.has_triggered = True
        self.last_triggered_time = game_time


# List to hold all registered game events
active_game_events = []

# --- Example Event Definitions ---

# Global state for shop (simplification for now)
# In a more complex system, this would be tied to specific locations or NPCs
SHOP_IS_OPEN = True 

def is_sunset(game_time, player, current_location):
    """Trigger condition for sunset message."""
    return game_time.hour == 18 and game_time.minute == 0

def sunset_action(game_time, player, current_location, npc_registry, game_locations_map, ui):
    """Action for sunset message."""
    # This message is now part of the event's description
    pass # Message is handled by event.description

def is_shop_closing_time(game_time, player, current_location):
    """Trigger condition for shop closing."""
    global SHOP_IS_OPEN
    return game_time.hour == 20 and game_time.minute == 0 and SHOP_IS_OPEN

def shop_closing_action(game_time, player, current_location, npc_registry, game_locations_map, ui):
    """Action for shop closing."""
    global SHOP_IS_OPEN
    SHOP_IS_OPEN = False
    # Message is handled by event.description
    # ui.slow_print("The local shops are now closing.") # Example of direct print if not using description

def is_shop_opening_time(game_time, player, current_location):
    """Trigger condition for shop opening."""
    global SHOP_IS_OPEN
    return game_time.hour == 8 and game_time.minute == 0 and not SHOP_IS_OPEN

def shop_opening_action(game_time, player, current_location, npc_registry, game_locations_map, ui):
    """Action for shop opening."""
    global SHOP_IS_OPEN
    SHOP_IS_OPEN = True
    # Message is handled by event.description
    # ui.slow_print("The local shops are opening for the day.")

# --- Event Registration ---

def initialize_game_events():
    """
    Initializes and registers all game events.
    Call this once when the game starts.
    """
    global active_game_events
    active_game_events = [] # Clear previous events if re-initializing

    sunset_event = GameEvent(
        name="Sunset",
        trigger_condition_func=is_sunset,
        action_func=sunset_action,
        description="The sun dips below the horizon, casting long, eerie shadows across the land.",
        cooldown_hours=23 # So it doesn't spam every minute of the 6 PM hour
    )
    active_game_events.append(sunset_event)

    shop_closes_event = GameEvent(
        name="Shops Close",
        trigger_condition_func=is_shop_closing_time,
        action_func=shop_closing_action,
        description="A bell tolls in the distance; the local shops are closing for the night.",
        cooldown_hours=23 
    )
    active_game_events.append(shop_closes_event)

    shop_opens_event = GameEvent(
        name="Shops Open",
        trigger_condition_func=is_shop_opening_time,
        action_func=shop_opening_action,
        description="The morning bustle begins as shopkeepers open their doors for the day.",
        cooldown_hours=23
    )
    active_game_events.append(shop_opens_event)

    # Add more events here
    # Example: Midnight event
    # def is_midnight(game_time, player, current_location):
    # return game_time.hour == 0 and game_time.minute == 0
    # def midnight_action(game_time, player, current_location, npc_registry, game_locations_map, ui):
    # ui.slow_print("The witching hour is upon you...")
    # midnight_event = GameEvent("Midnight Chimes", is_midnight, midnight_action, "A distant bell chimes midnight.", cooldown_hours=23)
    # active_game_events.append(midnight_event)


def check_and_trigger_events(game_time, player, current_location, npc_registry, game_locations_map, ui):
    """
    Checks all active game events and triggers them if their conditions are met.
    This should be called in the main game loop after time advances.
    """
    if not active_game_events:
        initialize_game_events() # Ensure events are initialized if list is empty

    for event in active_game_events:
        if event.can_trigger(game_time, player, current_location):
            event.trigger(game_time, player, current_location, npc_registry, game_locations_map, ui)