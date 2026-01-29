from context_manager import get_current_context
from rule_engine import apply_rules
from response_formatter import format_response
from memory_manager import update_memory

def process_query(query):
    context = get_current_context()

    raw_response = apply_rules(query, context)

    # Update lightweight memory
    if "eat" in query:
        update_memory("last_topic", "food")
    elif "study" in query:
        update_memory("last_topic", "study")

    final_response = format_response(raw_response, context)
    return final_response
