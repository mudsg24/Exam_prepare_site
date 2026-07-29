import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/ncku_cases_all28_dual_nlm_output.json', 'r') as f:
    nlm_data = json.load(f)

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_成大_Cases_(重點轉化).json', 'r') as f:
    db_data = json.load(f)

# Collect nlm responses
nlm_map = {}
for item in nlm_data:
    q_id = item['q_id']
    if q_id not in nlm_map:
        nlm_map[q_id] = item
    else:
        # handle suffix
        pass
        
for item in nlm_data:
    qid_full = item['q_id']
    q_id = qid_full.split('_run')[0]
    run_idx = qid_full.split('_run')[1]
    if q_id not in nlm_map:
        nlm_map[q_id] = {}
    nlm_map[q_id][f'run{run_idx}'] = item

q_list = [f"2026_成大_Cases_Q{str(i).zfill(2)}" for i in range(1, 11)]

output = []
for q in q_list:
    run1_text = nlm_map.get(q, {}).get('run1', {}).get('raw_response', '')
    run2_text = nlm_map.get(q, {}).get('run2', {}).get('raw_response', '')
    output.append({
        'q_id': q,
        'run1': run1_text[:300], # just a snippet to find the answer determination
        'run2': run2_text[:300]
    })

print(json.dumps(output, ensure_ascii=False, indent=2))
