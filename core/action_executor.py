import subprocess
from system_controller import change_volume

APP_PATHS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

def execute_action(intent_data):
    intent = intent_data.get("intent")

    # Volume actions
    if intent == "VOLUME":
        action = intent_data.get("action")
        change_volume(action)
        return

    # App actions
    if intent == "OPEN_APP":
        target = intent_data.get("target")
        if target in APP_PATHS:
            print(f"🚀 Opening {target}...")
            subprocess.Popen(APP_PATHS[target])
        else:
            print(f"❌ App '{target}' is not supported yet.")

    else:
        print("⚪ No executable action for this intent.")
