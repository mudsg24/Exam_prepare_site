import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/q11_q20_raw.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Semantic mapping based on analysis
# Q11: A, A -> HIGH_CONFIDENCE (source A)
# Q12: A, A -> HIGH_CONFIDENCE (source A)
# Q13: NONE, NONE -> HIGH_CONFIDENCE (source NONE)
# Q14: A, NONE -> DISPUTED (source NONE)
# Q15: NONE, NONE -> HIGH_CONFIDENCE (source NONE)
# Q16: A, A -> HIGH_CONFIDENCE (source A)
# Q17: NONE, NONE -> DISPUTED (source C)
# Q18: D, D -> HIGH_CONFIDENCE (source D)
# Q19: NONE, NONE -> HIGH_CONFIDENCE (source NONE)
# Q20: C, C -> HIGH_CONFIDENCE (source C)

mapping = {
    '2026_成大_Cases_Q11': {'run1': 'A', 'run2': 'A', 'status': 'HIGH_CONFIDENCE'},
    '2026_成大_Cases_Q12': {'run1': 'A', 'run2': 'A', 'status': 'HIGH_CONFIDENCE'},
    '2026_成大_Cases_Q13': {'run1': 'NONE', 'run2': 'NONE', 'status': 'HIGH_CONFIDENCE'},
    '2026_成大_Cases_Q14': {'run1': 'A', 'run2': 'NONE', 'status': 'DISPUTED'},
    '2026_成大_Cases_Q15': {'run1': 'NONE', 'run2': 'NONE', 'status': 'HIGH_CONFIDENCE'},
    '2026_成大_Cases_Q16': {'run1': 'A', 'run2': 'A', 'status': 'HIGH_CONFIDENCE'},
    '2026_成大_Cases_Q17': {'run1': 'NONE', 'run2': 'NONE', 'status': 'DISPUTED'},
    '2026_成大_Cases_Q18': {'run1': 'D', 'run2': 'D', 'status': 'HIGH_CONFIDENCE'},
    '2026_成大_Cases_Q19': {'run1': 'NONE', 'run2': 'NONE', 'status': 'HIGH_CONFIDENCE'},
    '2026_成大_Cases_Q20': {'run1': 'C', 'run2': 'C', 'status': 'HIGH_CONFIDENCE'}
}

output_data = []

for q in raw_data:
    qid = q['id']
    m = mapping.get(qid)
    if not m: continue
    
    # Validation of sufficiency
    run1_raw = q.get('run1_raw') or ''
    run2_raw = q.get('run2_raw') or ''
    
    run1_suff = 'INSUFFICIENT' if 'INSUFFICIENT_DATABASE_EVIDENCE' in run1_raw else 'SUFFICIENT'
    run2_suff = 'INSUFFICIENT' if 'INSUFFICIENT_DATABASE_EVIDENCE' in run2_raw or not run2_raw else 'SUFFICIENT'

    qc_batch_q = {
        'id': qid,
        'reconciliationStatus': m['status'],
        'nlmResponses': [
            {
                'selectedOption': m['run1'],
                'rawResponse': run1_raw,
                'databaseSufficiency': run1_suff,
                'qcStatus': 'PASSED',
                'qcReason': None
            },
            {
                'selectedOption': m['run2'],
                'rawResponse': run2_raw,
                'databaseSufficiency': run2_suff,
                'qcStatus': 'PASSED',
                'qcReason': None
            }
        ]
    }
    output_data.append(qc_batch_q)

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_2.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("Batch 2 processed and saved to scratch/qc_batch_2.json")
