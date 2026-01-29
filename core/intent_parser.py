def extract_intent(command_text):
    command_text = command_text.lower()

    # Volume control intents
    if "volume" in command_text or "sound" in command_text:

        if "unmute" in command_text:
            return {"intent": "VOLUME", "action": "unmute"}

        elif "mute" in command_text:
            return {"intent": "VOLUME", "action": "mute"}

        elif "increase" in command_text or "up" in command_text:
            return {"intent": "VOLUME", "action": "up"}

        elif "decrease" in command_text or "down" in command_text:
            return {"intent": "VOLUME", "action": "down"}
        

    # Automation intents
    if "study mode" in command_text:
        return {"intent": "AUTOMATION", "name": "study_mode"}

    if "focus mode" in command_text:
        return {"intent": "AUTOMATION", "name": "focus_mode"}


    # App control intents
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

    return {"intent": "UNKNOWN"}