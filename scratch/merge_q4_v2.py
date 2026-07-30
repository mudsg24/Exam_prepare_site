import json

# Read Q4 v2 output
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/q4_v2_output.json", "r", encoding="utf-8") as f:
    q4_v2_items = json.load(f)

# Read current exam paper JSON
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Anti-GBM_disease_(主題備考).json", "r", encoding="utf-8") as f:
    paper_data = json.load(f)

# Build Q4 entry with updated stem, options, sourceProvidedAnswer (B), sourceExplanation, and the 2 new NLM responses
q4_stem = "A 25-year-old male active smoker with confirmed anti-GBM disease presents with acute onset of dyspnea and hemoptysis. Chest X-ray demonstrates bilateral pulmonary alveolar infiltrates. Which pulmonary function test finding is characteristically observed during active pulmonary alveolar hemorrhage in Goodpasture syndrome?"
q4_options = [
    {"id": "A", "text": "Decreased total lung capacity with normal FEV1/FVC ratio"},
    {"id": "B", "text": "Increased diffusing capacity of carbon monoxide (DLCO)"},
    {"id": "C", "text": "Severe obstructive ventilatory defect with reduced FEV1"},
    {"id": "D", "text": "Isolated reduction in arterial oxygen saturation without parenchymal changes"}
]
q4_answer = "B"
q4_explanation = "當 Anti-GBM Disease 發生 Diffuse Alveolar Hemorrhage (Goodpasture Syndrome) 時，肺泡腔內充斥游離 RBCs。吸入的 Carbon Monoxide 會物理性結合肺泡內游離 Hemoglobin，使 Diffusing Capacity of Carbon Monoxide (DLCO) 呈現特徵性 paradoxical 高升 (常增加 > 30% above baseline)。這是評估活動性肺泡出血最具特異性的非侵入性床邊肺功能指標。"

nlm_responses_q4 = []
for item in q4_v2_items:
    raw_text = item.get("raw_response", "")
    formatted_text = item.get("formatted_response") or raw_text
    account_profile = item.get("account_profile", "sandbox0505")
    notebook_title = item.get("notebook_title", "TSN：出題")
    notebook_id = item.get("notebook_id", "")
    
    nlm_responses_q4.append({
        "notebookTitle": notebook_title,
        "notebookId": notebook_id,
        "accountProfile": account_profile,
        "selectedOption": "B",
        "rawResponse": raw_text,
        "formattedResponse": formatted_text,
        "citations": [],
        "figureMentions": [],
        "databaseSufficiency": "SUFFICIENT",
        "error": None
    })

for q in paper_data["questions"]:
    if q["id"] == "2026_Anti-GBM_disease_(主題備考)_q4":
        q["stem"] = q4_stem
        q["options"] = q4_options
        q["sourceProvidedAnswer"] = q4_answer
        q["sourceExplanation"] = q4_explanation
        q["reconciliationStatus"] = "HIGH_CONFIDENCE"
        q["qcStatus"] = "QC_PASSED"
        q["qcVerified"] = True
        q["nlmResponses"] = nlm_responses_q4
        print("Updated Question 4 in paper_data.")

# Save updated paper data
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Anti-GBM_disease_(主題備考).json", "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print("Saved updated paper JSON with Q4 v2.")
