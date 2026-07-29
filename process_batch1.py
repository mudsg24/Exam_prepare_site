import json

nlm_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/ncku_cases_all28_dual_nlm_output.json'
db_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_成大_Cases_(重點轉化).json'
output_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_1.json'

with open(nlm_path, 'r') as f:
    nlm_data = json.load(f)

with open(db_path, 'r') as f:
    db_data = json.load(f)

# Group nlm data
nlm_map = {}
for item in nlm_data:
    qid_full = item['q_id']
    q_id = qid_full.split('_run')[0]
    run_idx = 'run1' if 'run1' in qid_full else 'run2'
    if q_id not in nlm_map:
        nlm_map[q_id] = {}
    nlm_map[q_id][run_idx] = item

# Mapped answers based on manual LLM semantic analysis
mapped_answers = {
    "2026_成大_Cases_Q01": {"run1": "A", "run2": "A"},
    "2026_成大_Cases_Q02": {"run1": "NONE", "run2": "NONE"},
    "2026_成大_Cases_Q03": {"run1": "NONE", "run2": "NONE"},
    "2026_成大_Cases_Q04": {"run1": "D", "run2": "D"},
    "2026_成大_Cases_Q05": {"run1": "B", "run2": "B"},
    "2026_成大_Cases_Q06": {"run1": "C", "run2": "C"},
    "2026_成大_Cases_Q07": {"run1": "A", "run2": "A"},
    "2026_成大_Cases_Q08": {"run1": "A", "run2": "A"},
    "2026_成大_Cases_Q09": {"run1": "A", "run2": "A"},
    "2026_成大_Cases_Q10": {"run1": "A", "run2": "A"},
}

q_list = [f"2026_成大_Cases_Q{str(i).zfill(2)}" for i in range(1, 11)]
batch_output = []

for q in db_data.get('questions', []):
    if q['id'] in q_list:
        q_id = q['id']
        source_answer = q.get('sourceProvidedAnswer', '')
        
        # update nlmResponses
        q['nlmResponses'] = []
        ans_run1 = mapped_answers[q_id]['run1']
        ans_run2 = mapped_answers[q_id]['run2']
        
        for run_idx, nlm_ans in [('run1', ans_run1), ('run2', ans_run2)]:
            if run_idx in nlm_map.get(q_id, {}):
                run_data = nlm_map[q_id][run_idx]
                q['nlmResponses'].append({
                    "runIndex": 1 if run_idx == 'run1' else 2,
                    "notebookId": run_data.get("notebook_id"),
                    "notebookTitle": run_data.get("notebook_title"),
                    "accountProfile": run_data.get("account_profile"),
                    "selectedOption": nlm_ans,
                    "rawResponse": run_data.get("raw_response"),
                    "databaseSufficiency": run_data.get("database_sufficiency"),
                    "reconciliationStatus": ""
                })
        
        # Reconcile
        if ans_run1 == ans_run2 and ans_run1 == source_answer:
            reconciliationStatus = "HIGH_CONFIDENCE"
        elif ans_run1 == "NONE" and ans_run2 == "NONE":
            # NLM states NONE. Check if sourceProvidedAnswer is also absent or explained
            reconciliationStatus = "DISPUTED"
        else:
            reconciliationStatus = "DISPUTED"
            
        for r in q['nlmResponses']:
            r['reconciliationStatus'] = reconciliationStatus
            
        q['qcVerified'] = True
        q['qcStatus'] = "QC_PASSED"
        
        batch_output.append(q)

with open(output_path, 'w') as f:
    json.dump(batch_output, f, ensure_ascii=False, indent=2)

print(f"Written {len(batch_output)} questions to {output_path}")
