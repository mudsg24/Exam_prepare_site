import json

with open("scratch/qc_batch_6.json", "r") as f:
    data = json.load(f)

for item in data:
    qid = item.get("q_id")
    resp1 = item.get("resp1", "")[:300]
    resp2 = item.get("resp2", "")[:300]
    print(f"ID: {qid}")
    print(f"R1: {resp1}")
    print(f"R2: {resp2}")
    print("="*40)
