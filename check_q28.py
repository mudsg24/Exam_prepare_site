import json
with open("q15_28_extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for q in data:
    q_num = int(q['id'].split("_")[-1][1:])
    if q_num == 28:
        for i, nlm in enumerate(q['nlmResponses'][:2]):
            print(f"NLM {i+1} mentions Option (D):", "Option (D)" in nlm['rawResponse'] or "Option D" in nlm['rawResponse'] or "(D)" in nlm['rawResponse'])
