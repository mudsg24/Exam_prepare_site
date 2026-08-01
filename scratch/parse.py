import json
with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_17.json', 'r') as f:
    data = json.load(f)
for q in data:
    q_id = q.get('q_id')
    r1 = q.get('resp1', '')[:600]
    r2 = q.get('resp2', '')[:600]
    print(f"Q_ID: {q_id}")
    print(f"R1: {r1}")
    print(f"R2: {r2}")
    print("="*40)
