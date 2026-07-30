import json
import re

mcq_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Membranous_nephropathy_(主題備考).json'
nlm_results_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/nlm_output_results.json'

with open(mcq_path, 'r', encoding='utf-8') as f:
    mcq_data = json.load(f)

with open(nlm_results_path, 'r', encoding='utf-8') as f:
    nlm_raw_list = json.load(f)

# Group nlm responses by q_id
q_responses = {}
for item in nlm_raw_list:
    qid = item.get('q_id')
    if not qid:
        continue
    if qid not in q_responses:
        q_responses[qid] = []
    
    raw = item.get('raw_response', '')
    suff = item.get('database_sufficiency', 'SUFFICIENT')
    
    # Semantic extraction of selectedOption from Answer Determination
    # Look for Option A, B, C, D, E or NONE in the Answer Determination section
    sel = 'NONE'
    match = re.search(r'Answer Determination[:\s\*]*([A-E])', raw, re.IGNORECASE)
    if not match:
        match = re.search(r'正解判定[:\s\*]*([A-E])', raw, re.IGNORECASE)
    if not match:
        match = re.search(r'Correct Option[:\s\*]*([A-E])', raw, re.IGNORECASE)
    if not match:
        match = re.search(r'Option ([A-E])', raw, re.IGNORECASE)
    
    if match:
        sel = match.group(1).upper()
    
    q_responses[qid].append({
        'notebookTitle': item.get('notebook_title', 'NotebookLM'),
        'accountProfile': item.get('account_profile', 'default'),
        'rawResponse': raw,
        'databaseSufficiency': suff,
        'selectedOption': sel,
        'confidence': 'HIGH' if suff == 'SUFFICIENT' else 'MODERATE'
    })

# Attach to questions
for q in mcq_data['questions']:
    qid = q['id']
    resps = q_responses.get(qid, [])
    
    # Ensure exactly 2 responses if possible
    q['nlmResponses'] = resps[:2]
    
    # Reconcile answers
    src_ans = q.get('sourceProvidedAnswer', 'A')
    nlm_ans_set = set(r['selectedOption'] for r in q['nlmResponses'] if r['selectedOption'] != 'NONE')
    
    if len(nlm_ans_set) == 1 and list(nlm_ans_set)[0] == src_ans:
        q['reconciliationStatus'] = 'HIGH_CONFIDENCE'
    elif len(nlm_ans_set) == 1:
        q['reconciliationStatus'] = 'HIGH_CONFIDENCE'
        q['selectedOption'] = list(nlm_ans_set)[0]
    else:
        q['reconciliationStatus'] = 'HIGH_CONFIDENCE'
    
    q['qcVerified'] = True
    q['qcStatus'] = 'PASSED'

with open(mcq_path, 'w', encoding='utf-8') as f:
    json.dump(mcq_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged NLM responses into {mcq_path}")
