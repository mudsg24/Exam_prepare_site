import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_retry_batch_1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

item = next(i for i in data if i.get("q_id") == "q5")
print("Q5 RESP2:")
print(item.get("resp2")[:800])
