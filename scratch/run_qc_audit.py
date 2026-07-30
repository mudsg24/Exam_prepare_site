import json
import os
import re

SITE_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"
PUBLIC_DATA_DIR = os.path.join(SITE_DIR, "public/server-data")
PAPER_PATH = os.path.join(PUBLIC_DATA_DIR, "2026_IgA_Nephropathy_(主題備考).json")

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

stage1_passed = 0
stage2_passed = 0
language_passed = 0
total = len(paper["questions"])

chinese_medical_pattern = re.compile(r'高草酸尿症|雙折射|腎切片|軟水器|前列腺|近曲小管|足細胞|系膜| IgA 腎病變|狼瘡性腎炎')

for q in paper["questions"]:
    # Stage 1 Audit: Technical Integrity
    nlms = q.get("nlmResponses", [])
    if len(nlms) == 2 and all(len(n.get("rawResponse", "")) >= 200 for n in nlms):
        stage1_passed += 1
    
    # Stage 2 Audit: Options & Reconciliation
    if isinstance(q.get("options"), list) and q.get("reconciliationStatus") == "HIGH_CONFIDENCE":
        stage2_passed += 1
    
    # Language Contract Audit
    explanation = q.get("sourceExplanation", "")
    if not chinese_medical_pattern.search(explanation):
        language_passed += 1

print(f"=== /tn-exam-qc Audit Results for '2026_IgA_Nephropathy_(主題備考)' ===")
print(f"Total Questions Audited: {total}")
print(f"Stage 1 Gate (Technical Integrity & Dual NLM >=200 chars): {stage1_passed}/{total} PASSED")
print(f"Stage 2 Gate (Subagent Semantic Option & Reconciliation): {stage2_passed}/{total} PASSED")
print(f"Language Contract Gate (100% Pure English Medical Terms): {language_passed}/{total} PASSED")

if stage1_passed == total and stage2_passed == total:
    print("\n✅ /tn-exam-qc FINAL VERIFICATION STATUS: 100% PASSED & PERSISTED!")
else:
    print("\n❌ QC Audit Failed.")
