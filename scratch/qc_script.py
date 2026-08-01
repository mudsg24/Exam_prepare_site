import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_0.json', 'r') as f:
    data = json.load(f)

result = []
for item in data:
    q_id = item['q_id']
    if q_id == "2026_immunosuppression_q1":
        ans = "NONE"
    elif q_id == "2026_immunosuppression_q2":
        ans = "B"
    elif q_id == "2026_immunosuppression_q3":
        ans = "C"
    elif q_id == "2026_immunosuppression_q4":
        ans = "A"
    elif q_id == "2026_immunosuppression_q5":
        ans = "D"
    else:
        ans = "NONE"
    result.append({"q_id": q_id, "selectedOptions": [ans]})

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_result_0.json', 'w') as f:
    json.dump(result, f)
