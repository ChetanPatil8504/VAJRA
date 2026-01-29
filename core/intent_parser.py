def extract_intent(command_text):
    command_text = command_text.lower()

    if "open" in command_text:
        return {
            "intent": "OPEN_APP",
            "target": command_text.replace("open", "").strip()
        }

    elif "close" in command_text or "exit" in command_text:
        return {
            "intent": "CLOSE_APP",
            "target": command_text.replace("close", "").replace("exit", "").strip()
        }

    else:
        return {
            "intent": "UNKNOWN",
            "target": None
        }
