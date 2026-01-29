import json
import os

MEMORY_FILE = os.path.join("core", "memory", "user_memory.json")

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory_data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_data, f, indent=2)

def update_memory(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def get_memory(key):
    memory = load_memory()
    return memory.get(key)
