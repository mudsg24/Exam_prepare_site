import json, re, sys

tutorial_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials/2026_Membranous_nephropathy_(主題備考)_tutorial.json'
mcq_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Membranous_nephropathy_(主題備考).json'
manifest_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/exams_manifest.json'

with open(tutorial_path, 'r', encoding='utf-8') as f:
    tut = json.load(f)

with open(mcq_path, 'r', encoding='utf-8') as f:
    mcq = json.load(f)

with open(manifest_path, 'r', encoding='utf-8') as f:
    man = json.load(f)

errors = []

# 1. Tutorial Check
if len(tut.get('sections', [])) < 3:
    errors.append(f"Tutorial sections count {len(tut.get('sections', []))} < 3")

for idx, sec in enumerate(tut.get('sections', [])):
    if not sec.get('title') or not sec.get('content'):
        errors.append(f"Tutorial section {idx} missing title or content")
    if len(sec.get('diagrams', [])) < 2:
        errors.append(f"Tutorial section {idx} has fewer than 2 diagrams")

# 2. MCQ Check
if mcq.get('questionCount') != 18 or len(mcq.get('questions', [])) != 18:
    errors.append(f"MCQ count {len(mcq.get('questions', []))} != 18")

for idx, q in enumerate(mcq.get('questions', [])):
    if len(q.get('nlmResponses', [])) != 2:
        errors.append(f"Question {q['id']} nlmResponses count {len(q.get('nlmResponses', []))} != 2")
    if not q.get('qcVerified'):
        errors.append(f"Question {q['id']} qcVerified is not true")
    if q.get('qcStatus') != 'PASSED':
        errors.append(f"Question {q['id']} qcStatus {q.get('qcStatus')} != PASSED")
    if not isinstance(q.get('options'), list) or len(q.get('options')) != 4:
        errors.append(f"Question {q['id']} options schema invalid")

# 3. Manifest Check
item = next((i for i in man if i.get('id') == '2026_Membranous_nephropathy_(主題備考)'), None)
if not item:
    errors.append("Manifest missing 2026_Membranous_nephropathy_(主題備考)")
elif item.get('sourceCategory') != '2026 GN':
    errors.append(f"Manifest sourceCategory {item.get('sourceCategory')} != '2026 GN'")

if errors:
    print("VERIFICATION FAILED:")
    for err in errors:
        print(" -", err)
    sys.exit(1)
else:
    print("ALL HARD INVARIANTS 100% PASSED!")
