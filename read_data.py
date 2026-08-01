import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_retry_batch_1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    print(f"Q_ID: {item.get('q_id')}")
    r1 = item.get("resp1", "")
    r2 = item.get("resp2", "")
    print("RESP1:")
    # print first 500 characters
    print(r1[:500])
    print("RESP2:")
    print(r2[:500])
    print("="*40)
