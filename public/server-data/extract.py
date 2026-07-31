import json

with open("2026_Renal_transplant_rejection_(主題備考).json", "r") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["id"] in ["q8", "q9", "q10", "q11", "q12"]:
        print(f"--- {q['id']} ---")
        print("Explanation:", q.get("sourceExplanation", ""))
        print("Reconciliation:", q.get("reconciliationNotes", ""))
