import json

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_成大_Cases_(重點轉化).json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# The manual mapping based on my semantic reading of the texts
updates = {
    15: ("NONE", "NONE"),
    16: ("A", "A"),
    17: ("C", "C"),
    18: ("D", "D"),
    19: ("NONE", "NONE"),
    20: ("C", "C"),
    21: ("B", "B"),
    22: ("NONE", "NONE"),
    23: ("A", "A"),
    24: ("C", "C"),
    25: ("NONE", "NONE"),
    26: ("C", "C"),
    27: ("E", "E"),
    28: ("D", "NONE")
}

for q in data.get("questions", []):
    if "id" in q and q["id"].startswith("2026_成大_Cases_Q"):
        q_num_str = q["id"].split("_")[-1][1:]
        try:
            q_num = int(q_num_str)
        except:
            continue
            
        if 15 <= q_num <= 28:
            # 1. Deduplicate/clean nlmResponses
            valid_nlms = [nlm for nlm in q.get("nlmResponses", []) if len(nlm.get("rawResponse", "")) >= 200]
            # Keep exactly 2
            q["nlmResponses"] = valid_nlms[:2]
            
            # 2. Update selectedOption
            ans1, ans2 = updates[q_num]
            q["nlmResponses"][0]["selectedOption"] = ans1
            q["nlmResponses"][1]["selectedOption"] = ans2
            
            # 3. Re-evaluate reconciliationStatus
            orig = q.get("sourceProvidedAnswer")
            if ans1 == ans2:
                if orig != ans1:
                    # NLM 1 & NLM 2 agree with each other but differ from sourceProvidedAnswer
                    # -> update sourceProvidedAnswer to NLM choice, reconciliationStatus: "HIGH_CONFIDENCE", qcStatus: "QC_PASSED"
                    q["sourceProvidedAnswer"] = ans1
                q["reconciliationStatus"] = "HIGH_CONFIDENCE"
                q["qcStatus"] = "QC_PASSED"
            else:
                # NLM 1 != NLM 2
                q["reconciliationStatus"] = "DISPUTED"
                q["qcStatus"] = "DISPUTE_FLAGGED"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully updated Q15 to Q28 in the JSON file.")
