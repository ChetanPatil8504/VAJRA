from datetime import datetime

def get_current_context():
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        time_of_day = "morning"
    elif 12 <= hour < 17:
        time_of_day = "afternoon"
    elif 17 <= hour < 22:
        time_of_day = "evening"
    else:
        time_of_day = "night"

    return {
        "time_of_day": time_of_day,
        "hour": hour
    }
