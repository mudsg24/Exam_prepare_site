import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_10.json", "r") as f:
    data = json.load(f)

for item in data:
    print(f"--- Q_ID: {item['q_id']} ---")
    print("RESP1:", item.get("resp1", "")[:800])
    print("RESP2:", item.get("resp2", "")[:800])
    print()
