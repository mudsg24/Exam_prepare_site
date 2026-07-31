import json
import re

with open('/Users/yuan/.gemini/antigravity/brain/48b5db70-6fe4-4ebe-ad75-db0022514ac7/scratch/batch_2.json', 'r') as f:
    batch = json.load(f)

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Diabetes_Insipidus_(主題備考).json', 'r') as f:
    exam = json.load(f)

q_map = {q['id']: q for q in exam['questions']}
res = []

def extract_option(text):
    match = re.search(r'(?:Option|選項)\s*[\(（]?([A-E])[\)）]?', text, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    match2 = re.search(r'\(([A-E])\)', text[:200])
    if match2:
        return match2.group(1).upper()
    if 'ALL' in text[:200]: return 'ALL'
    if 'NONE' in text[:200]: return 'NONE'
    return 'UNKNOWN'

for q_id in ['di_006', 'di_007', 'di_008', 'di_009', 'di_010']:
    if q_id not in batch:
        continue
    runs = batch[q_id]
    r1 = runs.get('run1', {}).get('raw_response', '')
    r2 = runs.get('run2', {}).get('raw_response', '')
    
    o1 = extract_option(r1)
    o2 = extract_option(r2)
    
    source_ans = q_map[q_id]['sourceProvidedAnswer']
    
    status = ""
    notes = ""
    consensus = source_ans
    
    if o1 == o2 == source_ans:
        status = "HIGH_CONFIDENCE"
        notes = ""
    elif o1 == o2 and o1 != source_ans:
        status = "HIGH_CONFIDENCE"
        notes = "Corrected by dual NLM consensus"
        consensus = o1
    elif o1 != o2:
        status = "DISPUTED"
        notes = "Discrepancy between NLM run 1 and run 2"
        consensus = source_ans
        
    out_q = q_map[q_id].copy()
    out_q['selectedOption'] = consensus
    out_q['sourceProvidedAnswer'] = consensus
    out_q['reconciliationStatus'] = status
    out_q['reconciliationNotes'] = notes
    out_q['nlmResponses'] = [runs.get('run1', {}), runs.get('run2', {})]
    
    res.append(out_q)

with open('/Users/yuan/.gemini/antigravity/brain/48b5db70-6fe4-4ebe-ad75-db0022514ac7/scratch/parsed_batch_2.json', 'w') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)

for r in res:
    print(f"{r['id']}: R1={extract_option(runs.get('run1',{}).get('raw_response',''))}, R2={extract_option(runs.get('run2',{}).get('raw_response',''))}, Source={q_map[r['id']]['sourceProvidedAnswer']} -> Final={r['selectedOption']}, Status={r['reconciliationStatus']}")
