import json

with open("q15_28_extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for q in data:
    q_num = int(q['id'].split("_")[-1][1:])
    if q_num in [19, 22, 28]:
        for i, nlm in enumerate(q['nlmResponses'][:2]):
            print(f"Q{q_num} NLM {i+1} section 1 full:", nlm['rawResponse'][:600])
            print("---")
