from dli_engine import process_query

queries = [
    "What should I eat today?",
    "What should I study now?",
    "Tell me something random"
]

for q in queries:
    result = process_query(q)
    print(f"❓ Query: {q}")
    print(f"🧠 VAJRA: {result}")
    print("-" * 40)
