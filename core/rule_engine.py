def apply_rules(query, context):
    query = query.lower()
    time_of_day = context.get("time_of_day")

    # Food suggestion logic
    if "what" in query and "eat" in query:
        if time_of_day == "morning":
            return "You can have something light like poha or upma."
        elif time_of_day == "afternoon":
            return "A simple dal-rice or roti-sabzi would be good."
        elif time_of_day == "evening":
            return "You could make something quick like aloo bhaji or omelette."
        else:
            return "At night, keep it light. Maybe soup or curd rice."

    # Study suggestion logic
    if "study" in query:
        if time_of_day == "morning":
            return "Morning is best for tough subjects like maths or coding."
        elif time_of_day == "evening":
            return "Revise what you studied earlier or do light practice."
        else:
            return "Night is better for revision, not heavy study."

    return "I need a bit more context to answer that."
