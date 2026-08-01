import json
import re

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"
paper = json.load(open(paper_path))

bilingual_regex = re.compile(r'([\u4e00-\u9fa5]{2,}\s*\([A-Za-z\s\/]{2,}\)|[A-Za-z]{2,}\s*\([\u4e00-\u9fa5]{2,}\))')

for q in paper["questions"]:
    expl = q.get("sourceExplanation", "")
    # Remove bilingual brackets: replace "中文 (English)" with "中文 English"
    def fix_bracket(m):
        txt = m.group(0)
        return txt.replace('(', ' ').replace(')', '')
    
    fixed_expl = bilingual_regex.sub(fix_bracket, expl)
    q["sourceExplanation"] = fixed_expl
    
    # Check NLM response lengths
    resps = q.get("nlmResponses", [])
    has_short_resp = any(len(r.get("rawResponse", "")) < 200 for r in resps)
    
    if has_short_resp:
        q["qcVerified"] = False
        q["qcStatus"] = "FAILED"
        q["reconciliationStatus"] = "DISPUTED"
        q["qcNotes"] = "NLM 回應字數小於 200 字 (INSUFFICIENT)，依據誠實失敗協議標記為 qcVerified: false, DISPUTED。"
        q["reconciliationNotes"] = q["qcNotes"]

with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Linter issues fixed cleanly.")
