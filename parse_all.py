import json
import re

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_高長_(重點轉化).json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_ids = [f"2026_高長_Q{i}" for i in range(12, 23)]

for item in data.get("questions", []):
    if item.get("id") in q_ids:
        print(f"{item.get('id')}")
        responses = [r for r in item.get("nlmResponses", []) if len(r.get("rawResponse", "")) >= 200][:2]
        for i, r in enumerate(responses):
            raw = r.get("rawResponse", "")
            match = re.search(r'(?:1\.\s*)?(?:Answer Determination|正解判定|解答判定|答案判定|正解).*?(?=\n\s*(?:2\.|### 2\.|Distractor|Rationale|##|\n\n\n))', raw, re.DOTALL | re.IGNORECASE)
            ans = match.group(0).strip() if match else raw[:300]
            # Try to find A, B, C, D, E, NONE
            print(f"  NLM {i}: {ans[:150].replace(chr(10), ' ')}")
