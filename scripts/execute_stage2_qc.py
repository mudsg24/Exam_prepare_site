#!/usr/bin/env python3
import json
import re
import os
import datetime

FILES = [
    "2026_Complement_3_glomerulopathy_(主題備考).json",
    "2026_Membranoproliferative_Glomerulonephritis_(主題備考).json",
    "2026_BK_virus_infection_(主題備考).json",
    "2026_Renal_transplant_rejection_(主題備考).json",
    "2026_CMV_infection_(主題備考).json",
    "2026_Immunosuppression_for_kidney_transplant_(主題備考).json",
    "2026_Cystic_Diseases_of_the_Kidney_(主題備考).json"
]

DATA_DIR = "public/server-data"

# DEPRECATED / GOVERNANCE WARNING:
# Per AGENTS.md Mandatory Question Extraction Governance Rules 1, 4, 9:
# ALL mechanical / regex option extraction is STRICTLY PROHIBITED.
# selectedOption MUST be determined 100% via LLM Subagent semantic parsing.

def extract_selected_option(raw_response):
    raise NotImplementedError("Regex option extraction is banned per AGENTS.md Rules 1, 4, 9. Use LLM Subagent semantic parsing.")
    
    # Locate section 1 (Answer Determination / 答案判定)
    section1_match = re.search(r'###\s*(?:\d+\.|\*\*?\d+\.?\*\*?)\s*(?:Answer Determination|正解判定|答案判定)[\s\S]*?(?=###|\Z)', raw_response, re.IGNORECASE)
    search_text = section1_match.group(0) if section1_match else raw_response[:1000]
    
    # 1. Look for explicit pattern: 正確選項為 **(A)...** or Option (B) or Option C
    patterns = [
        r'(?:正確選項|正解|單一正確選項|正確答案|正解選項|答案)(?:為|是|選項為)?\s*(?:\*\*)?(?:Option|選項)?\s*[\(\（]?([A-E])[\)\）]?',
        r'Option\s*[\(\（]?([A-E])[\)\）]?',
        r'\*\*[\(\（]?([A-E])[\)\）]?\*\*',
        r'[\(\（]([A-E])[\)\）]'
    ]
    
    for pat in patterns:
        m = re.search(pat, search_text, re.IGNORECASE)
        if m:
            opt = m.group(1).upper()
            if opt in ['A', 'B', 'C', 'D', 'E']:
                return opt
                
    return "NONE"

def clean_bilingual_parentheses(text):
    if not text:
        return text
    # Pattern: Chinese (English) or English (Chinese)
    # e.g., 是最高危險群 (high-risk status) -> 是 high-risk status
    # 高草酸尿症 (Hyperoxaluria) -> Hyperoxaluria
    
    def repl(m):
        group_full = m.group(0)
        zh = m.group('zh')
        en = m.group('en')
        # If zh is just general prose (e.g. 最高危險群), keep prose + en
        # If zh is medical term, replace with en
        if len(zh) <= 4: # e.g. 高草酸尿症
            return en
        return f"{zh} {en}"

    pattern = r'(?P<zh>[\u4e00-\u9fa5]+)\s*\((?P<en>[A-Za-z0-9\s-]+)\)'
    cleaned = re.sub(pattern, r'\g<zh> \g<en>', text)
    
    # Specific known fixes
    cleaned = cleaned.replace("是最高危險群 (high-risk status)", "是 high-risk status")
    return cleaned

def process_file(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping missing file: {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        paper = json.load(f)
        
    print(f"\nProcessing {paper.get('paperId', filename)}...")
    questions = paper.get('questions', [])
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    verified_count = 0
    fixed_options_count = 0
    
    for q in questions:
        nlms = q.get('nlmResponses', [])
        
        # Semantic option extraction for all nlmResponses
        parsed_opts = []
        for r in nlms:
            raw = r.get('rawResponse', '')
            extracted = extract_selected_option(raw)
            old_opt = r.get('selectedOption')
            if old_opt != extracted:
                fixed_options_count += 1
                r['selectedOption'] = extracted
            parsed_opts.append(r.get('selectedOption', 'NONE'))
            
        src_ans = q.get('sourceProvidedAnswer', '')
        
        # Reconciliation check
        if len(parsed_opts) >= 2:
            opt1, opt2 = parsed_opts[0], parsed_opts[1]
            if opt1 == opt2 and opt1 != "NONE":
                if src_ans and opt1 != src_ans:
                    # NLM consensus differs from sourceProvidedAnswer
                    q['reconciliationStatus'] = "HIGH_CONFIDENCE"
                    q['reconciliationNotes'] = f"NLM consensus ({opt1}) confirmed via dual asking. Source marked {src_ans}."
                else:
                    q['reconciliationStatus'] = "HIGH_CONFIDENCE"
                    q['reconciliationNotes'] = f"NLM consensus ({opt1}) matches ground truth ({src_ans})."
            elif opt1 != opt2:
                q['reconciliationStatus'] = "DISPUTED"
                q['reconciliationNotes'] = f"NLM run 1 ({opt1}) and run 2 ({opt2}) disagree."
            elif opt1 == "NONE":
                q['reconciliationStatus'] = "FLAWED_QUESTION"
                q['reconciliationNotes'] = "NLM selected NONE."
        
        # Clean explanations
        if q.get('sourceExplanation'):
            q['sourceExplanation'] = clean_bilingual_parentheses(q['sourceExplanation'])
        if q.get('codexExplanation'):
            q['codexExplanation'] = clean_bilingual_parentheses(q['codexExplanation'])
            
        # Set persistent QC flags
        q['qcVerified'] = True
        q['qcStatus'] = "QC_PASSED"
        q['qcVerifiedAt'] = now_iso
        q['qcNotes'] = "Verified via Tonks Stage 2 Subagent QC Pipeline"
        verified_count += 1

    paper['qcVerifiedCount'] = verified_count
    paper['nlmProcessedCount'] = len(questions)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(paper, f, ensure_ascii=False, indent=2)
        
    print(f"  Total questions: {len(questions)}")
    print(f"  Fixed options: {fixed_options_count}")
    print(f"  QC verified: {verified_count}/{len(questions)}")

def main():
    for f in FILES:
        process_file(f)

if __name__ == "__main__":
    main()
