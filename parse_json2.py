import json

with open("q16_20.json", "r") as f:
    qs = json.load(f)

for q in qs:
    print(f"=== Q{q['number']} ===")
    print(f"Source: {q.get('sourceProvidedAnswer')}")
    for i, nlm in enumerate(q.get("nlmResponses", [])):
        print(f"--- NLM {i+1} ---")
        lines = nlm["rawResponse"].split("\n")
        print("\n".join(lines[:10]))
