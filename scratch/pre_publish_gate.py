import json
import re
import sys

tutorial_path = 'public/server-data/tutorials/2026_Inherited_RTA_(主題備考)_tutorial.json'
paper_path = 'public/server-data/2026_Inherited_RTA_(主題備考).json'

print("=== Starting Hard Pre-Publishing Gate Inspection ===")

# 1. Tutorial Check
with open(tutorial_path, 'r', encoding='utf-8') as f:
    tutorial = json.load(f)

sections = tutorial.get('sections', [])
if len(sections) < 3:
    print(f"FAILED: Tutorial sections count is {len(sections)} (< 3)")
    sys.exit(1)
print(f"PASSED: Tutorial has {len(sections)} sections (>= 3)")

for i, sec in enumerate(sections):
    if not sec.get('content') or len(sec.get('content', '')) < 100:
        print(f"FAILED: Tutorial section {i} content is empty or too short")
        sys.exit(1)
    diagrams = sec.get('diagrams', [])
    types = [d.get('type') for d in diagrams]
    if 'micrograph' not in types or 'ai_illustration' not in types:
        print(f"FAILED: Tutorial section {i} missing micrograph or ai_illustration diagram")
        sys.exit(1)

# 2. Question Paper Check
with open(paper_path, 'r', encoding='utf-8') as f:
    paper = json.load(f)

questions = paper.get('questions', [])
if len(questions) < 15:
    print(f"FAILED: Question count is {len(questions)} (< 15)")
    sys.exit(1)
print(f"PASSED: Question bank has {len(questions)} questions (>= 15)")

option_letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

for idx, q in enumerate(questions):
    # Check options schema
    opts = q.get('options', [])
    if not isinstance(opts, list) or not all(isinstance(o, dict) and 'id' in o and 'text' in o for o in opts):
        print(f"FAILED: Question {q['id']} options schema invalid")
        sys.exit(1)
    
    ans = q.get('sourceProvidedAnswer', '')
    if ans in option_letters:
        option_letters[ans] += 1
    
    # Check nlmResponses count
    nlms = q.get('nlmResponses', [])
    if len(nlms) != 2:
        print(f"FAILED: Question {q['id']} nlmResponses count is {len(nlms)} (!= 2)")
        sys.exit(1)
    
    # Check sufficiency and qcStatus
    for r in nlms:
        if r.get('databaseSufficiency') != 'SUFFICIENT':
            print(f"FAILED: Question {q['id']} has INSUFFICIENT response")
            sys.exit(1)
        if r.get('qcStatus') != 'PASSED':
            print(f"FAILED: Question {q['id']} has QC FAILED response")
            sys.exit(1)
        if len(r.get('rawResponse', '')) < 200:
            print(f"FAILED: Question {q['id']} has rawResponse < 200 chars")
            sys.exit(1)
    
    if q.get('qcStatus') != 'PASSED':
        print(f"FAILED: Question {q['id']} qcStatus is not PASSED")
        sys.exit(1)

print("PASSED: Option distribution:", option_letters)
print("=== All Hard Pre-Publishing Gate Checks PASSED 100%! ===")
