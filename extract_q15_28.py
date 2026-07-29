import json

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_成大_Cases_(重點轉化).json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

extracted = []
for q in data.get("questions", []):
    if "id" in q and q["id"].startswith("2026_成大_Cases_Q"):
        q_num_str = q["id"].split("_")[-1][1:]
        try:
            q_num = int(q_num_str)
            if 15 <= q_num <= 28:
                # Just extract what we need to read
                responses = []
                for nlm in q.get("nlmResponses", []):
                    responses.append({
                        "selectedOption": nlm.get("selectedOption"),
                        "rawResponse": nlm.get("rawResponse")
                    })
                extracted.append({
                    "id": q["id"],
                    "sourceProvidedAnswer": q.get("sourceProvidedAnswer"),
                    "reconciliationStatus": q.get("reconciliationStatus"),
                    "qcStatus": q.get("qcStatus"),
                    "nlmResponses": responses
                })
        except:
            pass

with open("q15_28_extract.json", "w", encoding="utf-8") as f:
    json.dump(extracted, f, ensure_ascii=False, indent=2)

print("Extracted", len(extracted), "questions")
