import json
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_hypophosphatemia_(主題備考).json") as f:
    d = json.load(f)
for q in d["questions"]:
    if q["number"] == 13:
        n0 = q["nlmResponses"][0]["rawResponse"]
        n1 = q["nlmResponses"][1]["rawResponse"]
        print("Length n0:", len(n0))
        print("Length n1:", len(n1))
        print("Identical?", n0 == n1)
