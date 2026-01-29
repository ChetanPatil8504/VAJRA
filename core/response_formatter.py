def format_response(raw_response, context):
    time_of_day = context.get("time_of_day")

    if time_of_day == "morning":
        prefix = "Good morning. "
    elif time_of_day == "afternoon":
        prefix = "This afternoon, "
    elif time_of_day == "evening":
        prefix = "Since it’s evening, "
    else:
        prefix = "At this time, "

    return prefix + raw_response
