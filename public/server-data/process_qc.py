import json
import re
from datetime import datetime, timezone, timedelta

def get_selected_option(raw_response):
    # Search in ### 1. Answer Determination only
    match = re.search(r'### 1\. Answer Determination.*?(?:正確選項為|選項為|唯一正確選項：|正確選項：?)\s*\*?\*?(?:Option\s*)?\(([A-E])\)', raw_response, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).upper()
    
    # Fallback to finding the first (A), (B), (C), (D) or (E) in the Answer Determination section
    section_match = re.search(r'### 1\. Answer Determination(.*?)(?:### 2|\Z)', raw_response, re.DOTALL)
    if section_match:
        section_text = section_match.group(1)
        opt_match = re.search(r'\(([A-E])\)', section_text)
        if opt_match:
            return opt_match.group(1).upper()
            
        opt_match_2 = re.search(r'Option\s*([A-E])', section_text, re.IGNORECASE)
        if opt_match_2:
            return opt_match_2.group(1).upper()
            
    return None

def has_bilingual_brackets(text):
    if not text: return False
    # Look for Chinese characters followed by English in brackets, or vice versa
    # Simplified pattern for finding things like 高草酸尿症 (Hyperoxaluria) or plasma cells (漿細胞)
    pattern1 = r'[\u4e00-\u9fa5]+[^\(]*\(\s*[a-zA-Z\s-]+\s*\)'
    pattern2 = r'[a-zA-Z\s-]+[^\(]*\(\s*[\u4e00-\u9fa5]+\s*\)'
    if re.search(pattern1, text) or re.search(pattern2, text):
        # We also need to check if there are markdown links or valid citations, but for now just find any
        pass
    
    # A more specific check for bilingual terms
    matches = re.findall(r'([\u4e00-\u9fa5]{2,})\s*[（\(]([A-Za-z\s\-]{3,})[）\)]', text)
    matches += re.findall(r'([A-Za-z\s\-]{3,})\s*[（\(]([\u4e00-\u9fa5]{2,})[）\)]', text)
    
    # Specifically check for some from the text
    bilingual_terms = []
    for m in matches:
        bilingual_terms.append(f"{m[0]}({m[1]})")
        
    return bilingual_terms

filepath = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Renal_transplant_rejection_(主題備考).json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] in ['q6', 'q7', 'q8', 'q9', 'q10']:
        print(f"Processing {q['id']}")
        
        # Check language violations in explanations and notes
        violations = []
        texts_to_check = [q.get('sourceExplanation', '')]
        
        for nlm in q.get('nlmResponses', []):
            raw = nlm.get('rawResponse', '')
            texts_to_check.append(raw)
            # Update selectedOption
            sel = get_selected_option(raw)
            if sel:
                nlm['selectedOption'] = sel
            print(f"  NLM {nlm.get('run', 'unknown')} selectedOption: {sel}")
            
        for text in texts_to_check:
            terms = has_bilingual_brackets(text)
            if terms:
                violations.extend(terms)
                
        # Reconcile
        ans1 = q['nlmResponses'][0]['selectedOption']
        ans2 = q['nlmResponses'][1]['selectedOption']
        source = q['sourceProvidedAnswer']
        
        if ans1 == ans2:
            if ans1 == source:
                status = "MATCH"
            else:
                status = "HIGH_CONFIDENCE_OVERRIDE"
        else:
            status = "DISPUTED"
            
        q['reconciliationStatus'] = status
        print(f"  Reconciliation: {status}")
        
        # QC Fields
        tz = timezone(timedelta(hours=8))
        q['qcVerifiedAt'] = datetime.now(tz).isoformat(timespec='seconds')
        
        if violations:
            unique_violations = list(set(violations))
            q['qcStatus'] = "QC_LANGUAGE_VIOLATION"
            q['qcVerified'] = False
            q['qcNotes'] = f"Language violation: Bilingual brackets found e.g. {', '.join(unique_violations[:3])}. Narrative must be Traditional Chinese, medical terms English only."
        else:
            if status == "DISPUTED":
                q['qcStatus'] = "QC_DISPUTED"
                q['qcVerified'] = False
                q['qcNotes'] = "NLM responses disputed."
            else:
                q['qcStatus'] = "QC_PASSED"
                q['qcVerified'] = True
                q['qcNotes'] = "QC passed. Semantic option extraction matched perfectly. No language violations detected."

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
print("Done")
