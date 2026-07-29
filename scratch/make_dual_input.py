import json

with open('scratch/nlm_input_questions.json') as f:
    questions = json.load(f)

dual_input = []
for q in questions:
    q1 = dict(q)
    q1['id'] = f"{q['id']}_run1"
    dual_input.append(q1)
    
    q2 = dict(q)
    q2['id'] = f"{q['id']}_run2"
    dual_input.append(q2)

with open('scratch/inherited_rta_dual_input.json', 'w', encoding='utf-8') as f:
    json.dump(dual_input, f, ensure_ascii=False, indent=2)

print(f"Created dual input with {len(dual_input)} items (20 questions x 2 runs).")
