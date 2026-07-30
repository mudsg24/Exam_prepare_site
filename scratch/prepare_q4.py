import json

# Update Q4 to align with Brenner 11e terminology so NotebookLM can find it cleanly
q4_run1 = {
    "id": "2026_Anti-GBM_disease_(主題備考)_q4_run1",
    "stem": "A 25-year-old male active smoker presents with dyspnea, hemoptysis, and acute renal failure. Which non-invasive pulmonary function parameter shows a characteristically elevated diffusing capacity due to intra-alveolar hemoglobin binding in active pulmonary alveolar hemorrhage?",
    "options": [
        {"id": "A", "text": "High-resolution computed tomography (HRCT) of the chest without contrast"},
        {"id": "B", "text": "Arterial blood gas (ABG) showing acute metabolic acidosis"},
        {"id": "C", "text": "Sputum cytology showing eosinophils and Charcot-Leyden crystals"},
        {"id": "D", "text": "Diffusing capacity of carbon monoxide (DLCO) increased by > 30% above baseline"}
    ]
}

q4_run2 = {
    "id": "2026_Anti-GBM_disease_(主題備考)_q4_run2",
    "stem": "A 25-year-old male active smoker presents with dyspnea, hemoptysis, and acute renal failure. Which non-invasive pulmonary function parameter shows a characteristically elevated diffusing capacity due to intra-alveolar hemoglobin binding in active pulmonary alveolar hemorrhage?",
    "options": [
        {"id": "A", "text": "High-resolution computed tomography (HRCT) of the chest without contrast"},
        {"id": "B", "text": "Arterial blood gas (ABG) showing acute metabolic acidosis"},
        {"id": "C", "text": "Sputum cytology showing eosinophils and Charcot-Leyden crystals"},
        {"id": "D", "text": "Diffusing capacity of carbon monoxide (DLCO) increased by > 30% above baseline"}
    ]
}

q4_payload = [q4_run1, q4_run2]

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/q4_input.json", "w", encoding="utf-8") as f:
    json.dump(q4_payload, f, ensure_ascii=False, indent=2)

print("Created Q4 payload.")
