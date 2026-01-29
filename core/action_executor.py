import subprocess
import os

APP_PATHS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

def execute_action(intent_data):
    intent = intent_data.get("intent")
    target = intent_data.get("target")

    if intent == "OPEN_APP":
        if target in APP_PATHS:
            app_path = APP_PATHS[target]
            print(f"🚀 Opening {target}...")
            subprocess.Popen(app_path)
        else:
            print(f"❌ App '{target}' is not supported yet.")

    else:
        print("⚪ No executable action for this intent.")
