import json
import os

APP_PATH = os.path.join(os.environ.get("HOME"), ".TODO/todo.json")

data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False
}

with open(APP_PATH, "w") as f:
    json.dump(data, f, indent=4)
