import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def save_stopwatch_state(state):
    with open("stopwatch_state.json", "w") as file:
        json.dump(state, file, cls=DateTimeEncoder)

def read_stopwatch_state():
    try:
        with open("stopwatch_state.json", "r") as file:
            state = json.load(file)
            return state
    except FileNotFoundError:
        return None
