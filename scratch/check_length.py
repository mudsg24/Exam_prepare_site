import json

with open("scratch/nlm_reask_output.json") as f:
    data = json.load(f)

for q in data:
    for r in q.get("nlmResponses", []):
        text = r.get("rawResponse", "")
        print(f"{q['id']}: len = {len(text)}")
