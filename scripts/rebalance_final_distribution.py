import json
import re

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"
paper = json.load(open(paper_path))

# Q11: Swap A and B
q11 = paper["questions"][10]
q11["options"][0], q11["options"][1] = q11["options"][1], q11["options"][0]
q11["options"][0]["id"], q11["options"][1]["id"] = "A", "B"
q11["sourceProvidedAnswer"] = "B"
q11["nlmResponses"][0]["selectedOption"] = "B"
q11["nlmResponses"][1]["selectedOption"] = "B"

# Q14: Swap A and C
q14 = paper["questions"][13]
q14["options"][0], q14["options"][2] = q14["options"][2], q14["options"][0]
q14["options"][0]["id"], q14["options"][2]["id"] = "A", "C"
q14["sourceProvidedAnswer"] = "C"
q14["nlmResponses"][0]["selectedOption"] = "C"
q14["nlmResponses"][1]["selectedOption"] = "C"

# Q18: Swap A and D
q18 = paper["questions"][17]
q18["options"][0], q18["options"][3] = q18["options"][3], q18["options"][0]
q18["options"][0]["id"], q18["options"][3]["id"] = "A", "D"
q18["sourceProvidedAnswer"] = "D"
q18["nlmResponses"][0]["selectedOption"] = "D"
q18["nlmResponses"][1]["selectedOption"] = "D"

dist = {}
for q in paper["questions"]:
    ans = q["sourceProvidedAnswer"]
    dist[ans] = dist.get(ans, 0) + 1

print(f"Rebalanced Final Distribution: {dist}")
with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Saved rebalanced paper cleanly.")
