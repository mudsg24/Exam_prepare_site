import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Gordon_syndrome_(主題備考).json", "r") as f:
    data = json.load(f)

for q in data.get("questions", [])[:5]:
    print(f"{q['id']}")
    for i, resp in enumerate(q.get("nlmResponses", [])):
        text = resp.get("rawResponse", "")
        # Try to find the line with "Answer Determination" or "正解" or "Correct Option"
        first_few_lines = '\n'.join(text.split('\n')[:15])
        print(f"Resp {i}:")
        print(first_few_lines)
        print("-------")
