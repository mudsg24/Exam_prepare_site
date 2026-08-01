import json

TARGET_PAPERS = [
    "2026_Albright_hereditary_osteodystrophy_(主題備考)",
    "2026_Hearing_loss_in_nephrology_(主題備考)",
    "2026_Inherited_RTA_(主題備考)",
    "2026_Membranous_nephropathy_(主題備考)",
    "2026_Minimal_change_disease_(主題備考)",
    "2026_Nephrotic_Syndrome_(主題備考)",
    "2026_Renal_vein_thrombosis_in_nephrotic_syndrome_(主題備考)",
    "2026_Thrombotic_Microangiopathy_(主題備考)",
    "2026_slit_diaphragm_(主題備考)"
]

with open("scripts/stage1_anomalous_input.json", "r", encoding="utf-8") as f:
    anomalous = json.load(f)

payload = []
for item in anomalous:
    if item.get("paperId") not in TARGET_PAPERS:
        continue
    payload.append({
        "id": item["q_id"],
        "paperId": item["paperId"],
        "title": item["paperTitle"],
        "number": item.get("number", ""),
        "stem": item.get("stem", ""),
        "options": item.get("options", [])
    })

with open("scratch/questions_input.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Prepared payload with {len(payload)} questions.")
