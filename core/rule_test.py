from context_manager import get_current_context
from rule_engine import apply_rules

context = get_current_context()

queries = [
    "What should I eat today?",
    "What should I study now?"
]

for q in queries:
    response = apply_rules(q, context)
    print(f"❓ Query: {q}")
    print(f"🧠 VAJRA: {response}")
    print("-" * 40)
