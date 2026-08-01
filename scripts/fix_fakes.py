import json
import os

server_dir = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/"
files = [
    "2026_hypophosphatemia_(主題備考).json",
    "2026_Hyperphosphatemia_(主題備考).json",
    "2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"
]

for filename in files:
    path = os.path.join(server_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    changed = False
    fakes = []
    for q in data.get("questions", []):
        if len(q.get("nlmResponses", [])) == 2:
            resp1 = (q["nlmResponses"][0].get("rawResponse") or "").strip()
            resp2 = (q["nlmResponses"][1].get("rawResponse") or "").strip()
            if len(resp1) > 50 and resp1 == resp2:
                q["qcVerified"] = False
                q["qcStatus"] = "PENDING_RETRY"
                q["reconciliationStatus"] = "UNRESOLVED_NEEDS_RETRY"
                q["qcNotes"] = "FAKED NLM RESPONSE DETECTED! Account 1 and Account 2 rawResponse are 100% identical."
                changed = True
                fakes.append(q["number"])
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Fixed fakes in {filename}: Q{fakes}")

