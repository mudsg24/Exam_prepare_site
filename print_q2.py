import json
import re

with open("q15_28_extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data:
    valid_nlms = [nlm for nlm in q['nlmResponses'] if len(nlm.get('rawResponse', '')) >= 200][:2]
    print(f"[{q['id']}] Source: {q['sourceProvidedAnswer']}")
    for i, nlm in enumerate(valid_nlms):
        text = nlm['rawResponse']
        
        # Print a short prefix to manually inspect
        print(f" NLM {i+1}:")
        print(text[:800].replace('\n', ' '))
    print("-" * 40)
