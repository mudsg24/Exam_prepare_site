import json

with open("q15_28_extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data:
    valid_nlms = [nlm for nlm in q['nlmResponses'] if len(nlm.get('rawResponse', '')) >= 200][:2]
    print(f"\n==============================")
    print(f"[{q['id']}] Source: {q['sourceProvidedAnswer']}")
    for i, nlm in enumerate(valid_nlms):
        text = nlm['rawResponse']
        print(f"\n--- NLM {i+1} ---")
        # Find where '1. Answer Determination' ends
        lines = text.split('\n')
        for line in lines[:20]:
            print(line.strip())
