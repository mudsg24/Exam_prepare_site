import json
with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_17.json', 'r') as f:
    data = json.load(f)
for q in data:
    if q.get('q_id') == 'Q9':
        print(q.get('options'))
