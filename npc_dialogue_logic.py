# npc_dialogue_logic.py
import random
from typing import Any, List, Dict
from ui import UI
from quests import Quest, generate_location_appropriate_quest, process_quest_rewards
# NEW: Import the dialogue tree data
from dialogue_data import DIALOGUE_TREES
# ... other necessary imports ...

# --- NEW FUNCTION: To select the correct dialogue tree ---
def get_dialogue_tree_for_npc(npc: Any) -> Dict:
    """
    Finds the most appropriate dialogue tree for an NPC based on priority.
    Priority: Unique ID > Role > Generic Default
    """
    # 1. Check for a unique dialogue tree matching the NPC's ID
    unique_key = f"{npc.unique_id.upper()}_DIALOGUE" # Assumes a convention
    if unique_key in DIALOGUE_TREES:
        return DIALOGUE_TREES[unique_key]

    # 2. Check for a role-specific dialogue tree
    role_key = f"{npc.role.upper()}_DIALOGUE"
    if role_key in DIALOGUE_TREES:
        return DIALOGUE_TREES[role_key]
        
    # 3. Fallback to a generic tree based on disposition/attitude
    # (This part can be expanded with more generic types)
    attitude = npc.tags.get("npc", {}).get("attitude", "neutral")
    if attitude == "hostile":
        return DIALOGUE_TREES.get("GENERIC_HOSTILE", DIALOGUE_TREES["GENERIC_NEUTRAL"])
    elif attitude == "friendly":
        return DIALOGUE_TREES.get("GENERIC_FRIENDLY", DIALOGUE_TREES["GENERIC_NEUTRAL"])
    
    return DIALOGUE_TREES["GENERIC_NEUTRAL"] # Final fallback


# --- REVISED FUNCTION: The main handler now uses the new tree selector ---
def handle_npc_dialogue(npc: Any, player: Any, current_location: Any) -> None:
    """Main handler for NPC dialogue interactions, now using a priority system."""
    try:
        UI.clear_screen()
        player.add_talked_to_npc(npc.unique_id)

        # Get the appropriate dialogue tree for this NPC
        dialogue_tree = get_dialogue_tree_for_npc(npc)
        current_node_id = dialogue_tree.get("start_node", "start") # Fallback to "start"
        
        # Initial greeting from the node
        initial_node = dialogue_tree.get("nodes", {}).get(current_node_id, {})
        initial_greeting = initial_node.get("npc_line", "Greetings.")
        if isinstance(initial_greeting, list):
            initial_greeting = random.choice(initial_greeting)

        UI.slow_print(f"You approach {npc.name} ({npc.role.replace('_',' ').title()}). Disposition: {npc.disposition}")
        # Format the initial greeting with placeholders
        UI.slow_print(f'"{format_dialogue_text(initial_greeting, player, npc, current_location)}"')

        while True:
            current_node = dialogue_tree.get("nodes", {}).get(current_node_id, {})
            if not current_node:
                UI.print_warning("Dialogue error: Node not found. Ending conversation.")
                break

            # Build and display player response options
            available_responses = []
            for response in current_node.get("player_responses", []):
                # Here you would add logic to check conditions (e.g., skill checks, quest status)
                # For now, we assume all defined responses are available
                available_responses.append(response)

            if not available_responses:
                break # End conversation if no responses

            UI.print_menu([resp["text"] for resp in available_responses])
            choice_input = UI.print_prompt("Your response? (Enter number)").strip()

            if choice_input.isdigit() and 1 <= int(choice_input) <= len(available_responses):
                chosen_response = available_responses[int(choice_input) - 1]

                # Process action, disposition change, etc. before moving to the next node
                # (This logic would be expanded here)

                if chosen_response.get("ends_dialogue"):
                    # Handle a final NPC line if it exists before ending
                    farewell_node = dialogue_tree.get("nodes", {}).get(chosen_response["next_node_id"])
                    if farewell_node and farewell_node.get("npc_line"):
                         UI.slow_print(f'"{format_dialogue_text(get_npc_line(farewell_node), player, npc, current_location)}"')
                    break

                current_node_id = chosen_response["next_node_id"]
                next_node_data = dialogue_tree.get("nodes", {}).get(current_node_id, {})
                
                # Display the NPC's response from the new node
                npc_reply = get_npc_line(next_node_data)
                UI.slow_print(f'"{format_dialogue_text(npc_reply, player, npc, current_location)}"')
            else:
                UI.slow_print("Invalid choice.")
        
    except Exception as e:
        UI.print_failure(f"Error in handle_npc_dialogue: {e}")

# (Other helper functions like _handle_npc_share_rumor etc. would be called via the 'action' key in a response)
# The format_dialogue_text helper function from dialogue_data.py would also need to be moved here
# or imported to be used.

def get_npc_line(node):
    if isinstance(node.get("npc_line", ""), list):
        return random.choice(node["npc_line"])
    return node.get("npc_line", "...")

def format_dialogue_text(text, player, npc, current_location):
    # This is a simplified version; your actual function may be more complex
    return text.replace("[PlayerName]", player.full_name).replace("[LocationName]", current_location.get("name", "here"))