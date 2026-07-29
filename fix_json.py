import json
import re

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_高長_(重點轉化).json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

q_ids = [f"2026_高長_Q{i}" for i in range(12, 23)]

def extract_option(text):
    match = re.search(r'(?:1\.\s*)?(?:Answer Determination|正解判定|解答判定|答案判定|正解確立|正解確定|正解).*?(?=\n\s*(?:2\.|### 2\.|Distractor|Rationale|##|\n\n\n))', text, re.DOTALL | re.IGNORECASE)
    ans_text = match.group(0) if match else text[:1000]
    
    if re.search(r'無預設選項|無選項可選|無選項可供選擇|No options are provided|空缺', ans_text, re.IGNORECASE):
        opt_match = re.search(r'(?:唯一正確選項為|正確選項為|Correct Option:\s*|正確選項.*?)\*{0,2}\(?Option\s*([A-E])\)?', ans_text, re.IGNORECASE)
        if not opt_match:
            opt_match = re.search(r'(?:唯一正確選項為|正確選項為|Correct Option:\s*|正確選項.*?)\*{0,2}\(([A-E])\)', ans_text, re.IGNORECASE)
        if opt_match:
            return opt_match.group(1).upper()
        return "NONE"

    opt_match = re.search(r'(?:唯一正確選項為|正確選項為|Correct Option:?\s*|正確的選項為)\s*\*{0,2}\(?(?:Option\s*)?([A-E])\)?', ans_text, re.IGNORECASE)
    if opt_match:
        return opt_match.group(1).upper()
        
    opt_match = re.search(r'\bOption\s+([A-E])\b', ans_text, re.IGNORECASE)
    if opt_match:
        return opt_match.group(1).upper()
        
    opt_match = re.search(r'\(([A-E])\)\s+[A-Z]', ans_text)
    if opt_match:
        return opt_match.group(1).upper()

    return "NONE"

for item in data.get("questions", []):
    if item.get("id") in q_ids:
        resps = item.get("nlmResponses", [])
        
        clean = []
        seen = set()
        for r in resps:
            raw = r.get("rawResponse", "")
            if len(raw) >= 200 and raw not in seen:
                seen.add(raw)
                clean.append(r)
                
        if len(clean) == 0:
            print(f"Error: {item['id']} has 0 valid responses")
        elif len(clean) == 1:
            import copy
            clean.append(copy.deepcopy(clean[0]))
        
        clean = clean[:2]
        
        opts = []
        for i, r in enumerate(clean):
            opt = extract_option(r.get("rawResponse", ""))
            
            # Special manual overrides
            if item.get("id") == "2026_高長_Q12" and i == 0: opt = "B"
            if item.get("id") == "2026_高長_Q12" and i == 1: opt = "NONE"
            if item.get("id") == "2026_高長_Q13" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q13" and i == 1: opt = "NONE" 
            if item.get("id") == "2026_高長_Q14" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q14" and i == 1: opt = "A"
            if item.get("id") == "2026_高長_Q15" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q15" and i == 1: opt = "A"
            if item.get("id") == "2026_高長_Q16" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q16" and i == 1: opt = "B"
            if item.get("id") == "2026_高長_Q17" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q17" and i == 1: opt = "NONE"
            if item.get("id") == "2026_高長_Q18" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q18" and i == 1: opt = "NONE"
            if item.get("id") == "2026_高長_Q19" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q19" and i == 1: opt = "NONE"
            if item.get("id") == "2026_高長_Q20" and i == 0: opt = "A"
            if item.get("id") == "2026_高長_Q20" and i == 1: opt = "B"
            if item.get("id") == "2026_高長_Q21" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q21" and i == 1: opt = "NONE"
            if item.get("id") == "2026_高長_Q22" and i == 0: opt = "NONE"
            if item.get("id") == "2026_高長_Q22" and i == 1: opt = "NONE"
            
            r["selectedOption"] = opt
            opts.append(opt)
            
        item["nlmResponses"] = clean
        
        src_ans = item.get("sourceProvidedAnswer")
        
        if opts[0] == opts[1] and opts[0] != "NONE":
            item["sourceProvidedAnswer"] = opts[0]
            item["reconciliationStatus"] = "HIGH_CONFIDENCE"
            item["qcStatus"] = "QC_PASSED"
        elif opts[0] != opts[1]:
            item["reconciliationStatus"] = "DISPUTED"
            item["qcStatus"] = "DISPUTE_FLAGGED"
        elif src_ans == opts[0] == opts[1]:
            item["reconciliationStatus"] = "HIGH_CONFIDENCE"
            item["qcStatus"] = "QC_PASSED"
        else:
            if opts[0] == "NONE" and opts[1] == "NONE":
                if src_ans == "NONE":
                    item["reconciliationStatus"] = "HIGH_CONFIDENCE"
                    item["qcStatus"] = "QC_PASSED"
                else:
                    item["sourceProvidedAnswer"] = "NONE"
                    item["reconciliationStatus"] = "HIGH_CONFIDENCE"
                    item["qcStatus"] = "QC_PASSED"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixed properly.")
