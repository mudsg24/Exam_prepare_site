import json
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_retry_batch_14.json") as f:
    data = json.load(f)
for q in data:
    print(f"--- Q_ID: {q['q_id']} ---")
    print(f"RESP1 START: {q['resp1'][:300]}")
    if 'resp2' in q:
        print(f"RESP2 START: {q['resp2'][:300]}")
