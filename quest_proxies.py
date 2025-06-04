from typing import List, Dict, Any, Optional

# Helper class to proxy dictionary access to attribute access for location data
class LocationProxy:
    def __init__(self, loc_dict: Optional[Dict[str, Any]]):
        self._loc_dict = loc_dict if loc_dict else {}

    @property
    def name(self) -> Optional[str]:
        return self._loc_dict.get('name')

    @property
    def id(self) -> Optional[str]:
        return self._loc_dict.get('id')

    @property
    def tags(self) -> List[str]:
        return self._loc_dict.get('tags', [])

    # Add other common location attributes as properties if needed by flavor.py
    # For example:
    # @property
    # def description(self) -> Optional[str]:
    #     return self._loc_dict.get('desc')

    def get(self, key: str, default: Any = None) -> Any:
        return self._loc_dict.get(key, default)

    def __getitem__(self, key: str) -> Any:
        if not self._loc_dict: # Should not happen if initialized with {} for None
            raise KeyError(f"Location data is None, cannot get key: {key}")
        return self._loc_dict[key] # Allows dict-style access, e.g., location['name']

    def __contains__(self, key: str) -> bool:
        return key in self._loc_dict

    def __str__(self) -> str:
        return str(self._loc_dict)

    def __repr__(self) -> str:
        return f"LocationProxy({self._loc_dict!r})"


class StageProxy:
    def __init__(self, stage_dict: Optional[Dict[str, Any]], quest_id: str = None):
        self._stage_dict = stage_dict if stage_dict is not None else {}
        self.quest_id = quest_id

    @property
    def name(self) -> Optional[str]:
        return self._stage_dict.get('stage_name')

    @property
    def objectives(self) -> List[Dict[str, Any]]:
        return self._stage_dict.get('objectives', [])

    @property
    def on_completion_dialogue(self) -> Optional[str]:
        return self._stage_dict.get('on_completion_dialogue')
    
    @property
    def reward_modifier(self) -> Optional[Dict[str, Any]]:
        return self._stage_dict.get('reward_modifier')

    @property
    def next_stage(self) -> Optional[str]:
        return self._stage_dict.get('next_stage')

    @property
    def is_final_stage(self) -> bool:
        return self._stage_dict.get('is_final_stage', False)

    def get(self, key: str, default: Any = None) -> Any:
        return self._stage_dict.get(key, default)

    def __getitem__(self, key: str) -> Any:
        if not self._stage_dict: # Should not happen if initialized with {} for None
            raise KeyError(f"Stage data is None, cannot get key: {key}")
        return self._stage_dict[key]

    def __contains__(self, key: str) -> bool:
        return key in self._stage_dict

    def __str__(self) -> str:
        return str(self._stage_dict)

    def __repr__(self) -> str:
        return f"StageProxy({self._stage_dict!r})"

class QuestProxy:
    def __init__(self, quest):
        self.quest = quest

    def start_quest(self):
        # Initialization logic here
        pass

    def advance_to_next_stage(self):
        return self.quest.advance_quest_stage()

    def is_quest_complete(self):
        return self.quest.status == "completed"