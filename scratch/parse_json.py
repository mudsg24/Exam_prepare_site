import json

with open("qc_retry_batch_4.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data:
    print(f"==================================================")
    print(f"q_id: {q.get('q_id')}")
    
    resp1 = q.get("resp1", "")
    resp2 = q.get("resp2", "")
    
    print("resp1 start:", repr(resp1[:200]))
    print("resp2 start:", repr(resp2[:200]))
