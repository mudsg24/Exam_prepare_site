import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_retry_batch_15.json', 'r') as f:
    data = json.load(f)

for item in data:
    q_id = item['q_id']
    print(f"--- {q_id} ---")
    resp1 = item.get('resp1', '')
    resp2 = item.get('resp2', '')
    
    # Just print the first 250 chars of resp1 and resp2 to see the chosen option
    print(f"resp1: {resp1[:250]}")
    print(f"resp2: {resp2[:250]}")
    print()
