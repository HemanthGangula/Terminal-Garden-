import json
import os

class Storage:
    def __init__(self, filepath='garden_state.json'):
        self.filepath = filepath

    def save(self, plant):
        state = {
            'stage': plant.stage,
            'health': plant.health
        }
        try:
            with open(self.filepath, 'w') as f:
                json.dump(state, f)
            print("Garden state has been saved.")
        except IOError as e:
            print(f"Error saving garden state: {e}")

    def load(self):
        if not os.path.exists(self.filepath):
            print("No saved garden state found.")
            return None
        try:
            with open(self.filepath, 'r') as f:
                state = json.load(f)
            print("Garden state has been loaded.")
            return state
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading garden state: {e}")
            return None