import json
import os

AUTOMATION_FILE = os.path.join("core", "automations", "profiles.json")

def load_automations():
    with open(AUTOMATION_FILE, "r") as f:
        return json.load(f)

def run_automation(name, execute_action):
    automations = load_automations()

    if name not in automations:
        print(f"❌ Automation '{name}' not found.")
        return

    print(f"⚙️ Running automation: {name}")

    for step in automations[name]:
        # 🔑 Normalize step format
        intent_data = step.copy()
        intent_data["intent"] = intent_data.pop("type")

        execute_action(intent_data)
