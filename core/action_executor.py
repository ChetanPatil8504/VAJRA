import subprocess
import psutil
from system_controller import change_volume

APP_PATHS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

APP_PROCESS_NAMES = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calculator.exe"
}

def close_app(process_name):
    closed = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            proc.terminate()
            closed = True
    return closed

def execute_action(intent_data):
    intent = intent_data.get("intent")

    # Volume actions
    if intent == "VOLUME":
        action = intent_data.get("action")
        change_volume(action)
        return

    # Open app
    if intent == "OPEN_APP":
        target = intent_data.get("target")
        if target in APP_PATHS:
            print(f"🚀 Opening {target}...")
            subprocess.Popen(APP_PATHS[target])
        else:
            print(f"❌ App '{target}' is not supported yet.")
        return

    # Close app
    if intent == "CLOSE_APP":
        target = intent_data.get("target")
        if target in APP_PROCESS_NAMES:
            print(f"🛑 Closing {target}...")
            was_closed = close_app(APP_PROCESS_NAMES[target])
            if was_closed:
                print(f"✅ {target} closed successfully.")
            else:
                print(f"⚪ {target} is not running.")
        else:
            print(f"❌ App '{target}' is not supported yet.")
        return

    print("⚪ No executable action for this intent.")
