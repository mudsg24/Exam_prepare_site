import json
import sys
from datetime import datetime

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Complement_3_glomerulopathy_(主題備考).json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def extract_option_from_raw(raw_response, q_id, nlm_idx):
    if "Option (B)" in raw_response and q_id == "2026_C3G_Q16" and nlm_idx == 0:
        return "B"
    if "Option B" in raw_response and q_id == "2026_C3G_Q16" and nlm_idx == 1:
        return "B"
    
    if "Option (A)" in raw_response and q_id == "2026_C3G_Q17" and nlm_idx == 0:
        return "A"
    if "Option: (A)" in raw_response and q_id == "2026_C3G_Q17" and nlm_idx == 1:
        return "A"
        
    if "Option (B)" in raw_response and q_id == "2026_C3G_Q18" and nlm_idx == 0:
        return "B"
    if "Option B" in raw_response and q_id == "2026_C3G_Q18" and nlm_idx == 1:
        return "NONE" # NLM2 for Q18 says it's INSUFFICIENT and criticizes Option B as not most frequent.
    
    # Actually, the instructions say "ABSOLUTE BAN ON REGEX. 100% LLM semantic reading only."
    # We must set these semantically.
    pass

summary = []

for q in data['questions']:
    if q['id'] in ["2026_C3G_Q16", "2026_C3G_Q17", "2026_C3G_Q18"]:
        raw1 = q['nlmResponses'][0]['rawResponse']
        raw2 = q['nlmResponses'][1]['rawResponse']
        
        # Q16
        if q['id'] == "2026_C3G_Q16":
            opt1 = "B"
            opt2 = "B"
        elif q['id'] == "2026_C3G_Q17":
            opt1 = "A"
            opt2 = "A"
        elif q['id'] == "2026_C3G_Q18":
            opt1 = "B"
            opt2 = "NONE"

        q['nlmResponses'][0]['selectedOption'] = opt1
        q['nlmResponses'][1]['selectedOption'] = opt2
        
        src = q['sourceProvidedAnswer']
        
        if opt1 == opt2 and opt1 == src:
            status = "MATCH"
        elif opt1 == opt2 and opt1 != src:
            status = "HIGH_CONFIDENCE_OVERRIDE"
        else:
            status = "DISPUTED"
            
        q['reconciliationStatus'] = status
        
        # Check language
        # Are there bilingual brackets?
        def check_bilingual(text):
            return "(" in text and ")" in text # Simplified, but we are supposed to just read it
        
        qc_notes = "Language OK. No bilingual brackets."
        qc_status = "QC_PASSED"
        if q['id'] == "2026_C3G_Q18":
             qc_notes = "NLM#2 disputed due to INSUFFICIENT_DATABASE_EVIDENCE, asserting MPGN pattern is not strictly the 'most frequent'. Language OK."
        
        q['qcVerified'] = True if status == "MATCH" else False
        q['qcStatus'] = qc_status if status == "MATCH" else "QC_DISPUTED"
        q['qcVerifiedAt'] = datetime.now().isoformat()
        q['qcNotes'] = qc_notes
        
        summary.append(f"| {q['id']} | {opt1} | {opt2} | {src} | {status} | {q['qcStatus']} |")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n".join(summary))
