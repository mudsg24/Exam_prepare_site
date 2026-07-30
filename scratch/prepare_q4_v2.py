import json

q4_v2_run1 = {
    "id": "2026_Anti-GBM_disease_(主題備考)_q4_run1",
    "stem": "A 25-year-old male active smoker with confirmed anti-GBM disease presents with acute onset of dyspnea and hemoptysis. Chest X-ray demonstrates bilateral pulmonary alveolar infiltrates. Which pulmonary function test finding is characteristically observed during active pulmonary alveolar hemorrhage in Goodpasture syndrome?",
    "options": [
        {"id": "A", "text": "Decreased total lung capacity with normal FEV1/FVC ratio"},
        {"id": "B", "text": "Increased diffusing capacity of carbon monoxide (DLCO)"},
        {"id": "C", "text": "Severe obstructive ventilatory defect with reduced FEV1"},
        {"id": "D", "text": "Isolated reduction in arterial oxygen saturation without parenchymal changes"}
    ]
}

q4_v2_run2 = {
    "id": "2026_Anti-GBM_disease_(主題備考)_q4_run2",
    "stem": "A 25-year-old male active smoker with confirmed anti-GBM disease presents with acute onset of dyspnea and hemoptysis. Chest X-ray demonstrates bilateral pulmonary alveolar infiltrates. Which pulmonary function test finding is characteristically observed during active pulmonary alveolar hemorrhage in Goodpasture syndrome?",
    "options": [
        {"id": "A", "text": "Decreased total lung capacity with normal FEV1/FVC ratio"},
        {"id": "B", "text": "Increased diffusing capacity of carbon monoxide (DLCO)"},
        {"id": "C", "text": "Severe obstructive ventilatory defect with reduced FEV1"},
        {"id": "D", "text": "Isolated reduction in arterial oxygen saturation without parenchymal changes"}
    ]
}

payload = [q4_v2_run1, q4_v2_run2]

output_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/q4_v2_input.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Created Q4 v2 payload at {output_path}")
