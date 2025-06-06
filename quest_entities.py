# quest_entities.py
import random
from typing import List, Dict, Any, Optional
import json

import flavor # Used in Quest.__str__
from items import Item # Used in Quest.__str__
from ui import UI # Used for system messages and warnings
from quest_proxies import LocationProxy, StageProxy, QuestProxy # Used in Quest class

class Quest:
    def __init__(self, title: str, description: str, reward: Dict[str, Any], level_requirement: int,
                 location: Dict[str, Any], # This will be wrapped by LocationProxy
                 stages: List[Dict[str, Any]], # Stages will be wrapped by StageProxy
                 quest_id: str | None = None, status: str = "active", turn_in_npc_id: str | None = None,
                 tags: Dict[str, Any] | None = None,
                 initial_flavor_text: str = ""
                 ):
        self.quest_id = quest_id or f"quest_{random.randint(1000, 9999)}"
        self.title = title
        self.description = description
        self.reward = reward
        self.level_requirement = level_requirement
        # Wrap location dictionary in LocationProxy if it's a dict
        self.location = LocationProxy(location) if isinstance(location, dict) else location
        self.stages = stages # List of dictionaries, StageProxy is used on demand
        self.current_stage_index = 0
        self.status = status # e.g., "active", "completed", "failed"
        self.turn_in_npc_id = turn_in_npc_id
        self.tags = tags if tags else {}
        self.initial_flavor_text = initial_flavor_text
        self.current_stage_progress: Dict[str, Any] = {} # Tracks progress of objectives in current stage
        self._initialize_stage_progress()
        self.add_tag("quest", "type", "generic") # Default tag
        self.quest_proxy = QuestProxy(self)
        self.unique_items: List[str] = []
        self.abilities: List[str] = []

    def add_tag(self, tag_category: str, tag_type: str, tag_value: str) -> None:
        if tag_category not in self.tags:
            self.tags[tag_category] = {}
        if tag_type not in self.tags[tag_category]:
            self.tags[tag_category][tag_type] = []
        self.tags[tag_category][tag_type].append(tag_value)

    def _initialize_stage_progress(self) -> None:
        self.current_stage_progress.clear()
        if self.current_stage_index < len(self.stages):
            current_stage_dict = self.stages[self.current_stage_index]
            for obj in current_stage_dict.get("objectives", []):
                actual_obj_dict = obj.get("objective") if obj.get("type") == "optional" else obj
                obj_id = actual_obj_dict.get("id", f"obj_{random.randint(1,100000)}")
                actual_obj_dict["id"] = obj_id
                if obj.get("type") == "optional":
                    obj["id"] = obj.get("id", f"opt_wrapper_{obj_id}")
                self.current_stage_progress[obj_id] = {"met": False, "current_count": 0}

    @property
    def current_stage(self) -> Optional[StageProxy]:
        if 0 <= self.current_stage_index < len(self.stages):
            stage_dict = self.stages[self.current_stage_index]
            return StageProxy(stage_dict, self.quest_id)
        return None

    def check_objective_met(self, objective_wrapper: Dict[str, Any], player: Any) -> bool:
        try:
            is_optional_wrapper = objective_wrapper.get("type") == "optional"
            actual_objective = objective_wrapper.get("objective") if is_optional_wrapper else objective_wrapper
            
            obj_type = actual_objective["type"]
            obj_id = actual_objective.get("id")

            if not obj_id:
                UI.print_warning(f"Objective missing ID: {actual_objective.get('note', 'Unknown objective')}")
                return False
                
            if obj_id not in self.current_stage_progress:
                self.current_stage_progress[obj_id] = {"met": False, "current_count": 0}

            if self.current_stage_progress[obj_id]["met"]:
                return True

            met_this_check = False
            if obj_type == "kill":
                target_id = actual_objective["target_id"]
                required_count = actual_objective["count"]
                current_count = getattr(player, "defeated_enemies_tracker", {}).get(target_id, 0)
                self.current_stage_progress[obj_id]["current_count"] = current_count
                if current_count >= required_count:
                    met_this_check = True
            elif obj_type == "collect_item":
                item_key = actual_objective["item_key"]
                required_count = actual_objective["count"]
                current_count = sum(1 for item_obj in player.stats.inventory if item_obj.name.lower().replace(' ', '_') == item_key.lower().replace(' ', '_'))
                self.current_stage_progress[obj_id]["current_count"] = current_count
                if current_count >= required_count:
                    met_this_check = True
            elif obj_type == "reach_location":
                location_name = actual_objective["location_name"]
                if (player.current_location_obj and player.current_location_obj["name"].lower() == location_name.lower()) or \
                   any(loc_obj["name"].lower() == location_name.lower() for loc_obj in player.known_locations_objects):
                    met_this_check = True
            elif obj_type == "talk_to_npc":
                npc_id = actual_objective["npc_id"]
                if npc_id in getattr(player, "talked_to_npcs", set()):
                    met_this_check = True
            elif obj_type == "kill_specific_enemy":
                enemy_id = actual_objective["enemy_id"]
                required_count = actual_objective["count"]
                current_count = getattr(player, "defeated_enemies_tracker", {}).get(enemy_id, 0)
                self.current_stage_progress[obj_id]["current_count"] = current_count
                if current_count >= required_count:
                    met_this_check = True
            elif obj_type == "collect_specific_item":
                item_id = actual_objective["item_id"]
                required_count = actual_objective["count"]
                current_count = sum(1 for item_obj in player.stats.inventory if item_obj.item_id == item_id)
                self.current_stage_progress[obj_id]["current_count"] = current_count
                if current_count >= required_count:
                    met_this_check = True
            elif obj_type == "reach_specific_location":
                location_id = actual_objective["location_id"]
                if player.current_location_obj and player.current_location_obj["id"] == location_id:
                    met_this_check = True
            elif obj_type in ["skill_check", "choice", "protect", "destroy", "craft", "confront", "track", "investigate", "use_item", "repair", "sell_item", "event_trigger", "solve_puzzle"]:
                met_this_check = self.current_stage_progress[obj_id]["met"]
            
            if met_this_check:
                self.current_stage_progress[obj_id]["met"] = True
            return met_this_check
        except Exception as e:
            UI.print_warning(f"Error checking objective: {e}")
            return False

    def mark_objective_met(self, objective_id: str, met_status: bool = True):
        if objective_id in self.current_stage_progress:
            self.current_stage_progress[objective_id]["met"] = met_status
            if met_status:
                 UI.print_system_message(f"Objective updated: '{objective_id}' marked as completed.")
        else:
            found = False
            current_stage_val = self.current_stage # Use the property
            if current_stage_val: # Check if current_stage is not None
                for obj_wrapper in current_stage_val.get("objectives", []):
                    actual_obj = obj_wrapper.get("objective") if obj_wrapper.get("type") == "optional" else obj_wrapper
                    if actual_obj.get("id") == objective_id:
                        self.current_stage_progress[objective_id] = {"met": met_status, "current_count": actual_obj.get("count",0) if met_status else 0}
                        if met_status:
                            UI.print_system_message(f"Objective updated: '{objective_id}' marked as completed.")
                        found = True
                        break
            if not found:
                UI.print_warning(f"Attempted to mark unknown objective ID: {objective_id}")

    def check_all_current_stage_objectives_met(self, player: Any) -> bool:
        current_stage_val = self.current_stage
        if not current_stage_val:
            return False
        
        all_primary_met = True
        for obj_wrapper in current_stage_val.get("objectives", []):
            if obj_wrapper.get("type") == "optional":
                self.check_objective_met(obj_wrapper, player) 
            continue 
            
            if not self.check_objective_met(obj_wrapper, player):
                all_primary_met = False
        
        return all_primary_met

    def advance_quest_stage(self) -> bool:
        try:
            advanced = self.quest_proxy.advance_to_next_stage()
            if self.status == "completed":
                # Give unique items and unlock abilities
                # Assuming player object is accessible somehow
                # player.inventory.extend(self.unique_items) # This needs to be adapted to your game's logic
                # player.abilities.extend(self.abilities) # This needs to be adapted to your game's logic
                UI.print_system_message(f"You have received: {', '.join(self.unique_items)}")
                UI.print_system_message(f"You have unlocked: {', '.join(self.abilities)}")
            return advanced
        except Exception as e:
            UI.print_warning(f"Error advancing quest stage: {e}")
            return False

    def fail_quest(self, reason: str = "unknown") -> None:
        self.status = "failed"
        UI.print_system_message(f"Quest '{{self.title}}' has FAILED due to: {reason}.")

    def __str__(self) -> str:
        reward_str_parts = []
        for key, value in self.reward.items():
            if isinstance(value, Item): # Item class from items.py
                reward_str_parts.append(f"{value.name} (Item)")
            else:
                reward_str_parts.append(f"{value} {key.capitalize()}")
        reward_display = ", ".join(reward_str_parts) if reward_str_parts else "None specified"

        objectives_display = []
        current_stage_data = self.current_stage # Uses StageProxy
        if current_stage_data:
            for obj_wrapper in current_stage_data.objectives: # Access objectives via StageProxy property
                is_optional = obj_wrapper.get("type") == "optional"
                actual_obj = obj_wrapper.get("objective") if is_optional else obj_wrapper
                
                obj_id = actual_obj.get("id")
                obj_note = actual_obj.get("note", f"Complete {actual_obj['type']} objective.")
                progress_str = ""
                
                status_prefix = "[ ]"
                if obj_id and self.current_stage_progress.get(obj_id, {}).get("met"):
                    status_prefix = "[X]"
                    progress_str = " (Completed)"
                
                if obj_id and not self.current_stage_progress.get(obj_id, {}).get("met"):
                    if "count" in actual_obj and (actual_obj.get("type") == "kill" or actual_obj.get("type") == "collect_item"):
                        current_count = self.current_stage_progress.get(obj_id, {}).get("current_count", 0)
                        progress_str = f" ({current_count}/{actual_obj['count']})"

                if is_optional:
                    status_prefix += " (Optional)"
                
                objectives_display.append(f"  {status_prefix} {obj_note}{progress_str}")
        
        flavor_texts = flavor.get_flavor(self) if hasattr(flavor, 'get_flavor') else []
        flavor_display = f"\n  Lore: {' '.join(flavor_texts)}" if flavor_texts else ""
        
        status_display = self.status.capitalize()
        if self.status == "completed" and self.turn_in_npc_id:
            turn_in_npc_name = self.turn_in_npc_id.split('_')[0].capitalize()
            status_display += f" (Ready for Turn-in to {turn_in_npc_name})"
        elif self.status == "completed":
             status_display += " (Completed)"

        location_name_str = self.location.name if self.location and self.location.name else "Unknown Location"

        full_description = f"Quest[{self.quest_id}] {self.title} (Lvl {self.level_requirement}) at {location_name_str}\n" \
                           f"Status: {status_display} | Stage: {self.current_stage_index + 1}/{len(self.stages) if self.stages else 1}\n" \
                           f"Overall: {self.description}\n"
        if self.initial_flavor_text:
            full_description += f"'{self.initial_flavor_text}'\n"
        full_description += f"Current Tasks:\n" + "\n".join(objectives_display) + \
                            f"\nReward: {reward_display}" + \
                            flavor_display
        
        if self.unique_items:
            full_description += f"\nUnique Items: {', '.join(self.unique_items)}"
        if self.abilities:
            full_description += f"\nAbilities Unlocked: {', '.join(self.abilities)}"
        
        return full_description

    def to_json(self) -> str:
        """
        Serializes the Quest object to a JSON string.
        """
        return json.dumps(self.__dict__, indent=4, default=str)

    @classmethod
    def from_json(cls, json_str: str) -> 'Quest':
        """
        Deserializes a Quest object from a JSON string.
        """
        data = json.loads(json_str)
        return cls(**data)

class QuestLog:
    def __init__(self):
        self.active_quests: List[Quest] = []
        self.completed_quests: List[Quest] = []
        self.failed_quests: List[Quest] = []

    def add_quest(self, quest: Quest) -> bool:
        if quest.quest_id not in [q.quest_id for q in self.active_quests] and \
           quest.quest_id not in [q.quest_id for q in self.completed_quests] and \
           quest.quest_id not in [q.quest_id for q in self.failed_quests]:
            self.active_quests.append(quest)
            UI.print_system_message(f"New quest added: '{quest.title}'! Check your journal.")
            if quest.initial_flavor_text:
                UI.slow_print(f"'{quest.initial_flavor_text}'")
            return True
        UI.print_warning(f"Quest '{quest.title}' ({quest.quest_id}) already in log or completed/failed.")
        return False

    def remove_quest(self, quest_id: str) -> bool:
        quest_to_move = self.get_quest_by_id(quest_id)
        if not quest_to_move:
            return False

        if quest_to_move in self.active_quests:
            self.active_quests.remove(quest_to_move)
        
        if quest_to_move.status == "completed" and quest_to_move not in self.completed_quests:
            self.completed_quests.append(quest_to_move)
        elif quest_to_move.status == "failed" and quest_to_move not in self.failed_quests:
            self.failed_quests.append(quest_to_move)
        return True

    def get_quest_by_id(self, quest_id: str) -> Quest | None:
        for q_list in [self.active_quests, self.completed_quests, self.failed_quests]:
            for q in q_list:
                if q.quest_id == quest_id:
                    return q
        return None

    def list_quests(self) -> List[Quest]:
        return self.active_quests + self.completed_quests + self.failed_quests
    
    def get_active_quests_for_display(self) -> List[Quest]:
        return [q for q in self.active_quests]

    def get_completed_quests_for_display(self) -> List[Quest]:
        return [q for q in self.completed_quests]

    def get_failed_quests_for_display(self) -> List[Quest]:
        return [q for q in self.failed_quests]

    def get_quests_for_turn_in(self, npc_id: str) -> List[Quest]:
        return [q for q in self.active_quests if q.status == "completed" and q.turn_in_npc_id == npc_id]

def save_quest_log(quest_log: QuestLog, file_path: str) -> None:
    """
    Saves the quest log to a JSON file.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump({
                "active_quests": [json.loads(quest.to_json()) for quest in quest_log.active_quests],
                "completed_quests": [json.loads(quest.to_json()) for quest in quest_log.completed_quests],
                "failed_quests": [json.loads(quest.to_json()) for quest in quest_log.failed_quests]
            }, f, indent=4)
    except Exception as e:
        UI.print_warning(f"Error saving quest log: {e}")

def load_quest_log(file_path: str) -> QuestLog:
    """
    Loads the quest log from a JSON file.
    """
    quest_log = QuestLog()
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            quest_log.active_quests = [Quest.from_json(quest_json) for quest_json in data.get("active_quests", [])]
            quest_log.completed_quests = [Quest.from_json(quest_json) for quest_json in data.get("completed_quests", [])]
            quest_log.failed_quests = [Quest.from_json(quest_json) for quest_json in data.get("failed_quests", [])]
    except FileNotFoundError:
        UI.print_warning("Quest log file not found. Creating a new quest log.")
    except Exception as e:
        UI.print_warning(f"Error loading quest log: {e}")
    return quest_log