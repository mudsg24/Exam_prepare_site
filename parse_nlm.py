import json
import re

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_高長_(重點轉化).json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_ids = [f"2026_高長_Q{i}" for i in range(12, 23)]

def get_answer_determination(text):
    match = re.search(r'(?:1\.\s*)?(?:Answer Determination|正解判定|解答判定|答案判定|正解).*?(?=\n\s*(?:2\.|### 2\.|Distractor|Rationale|##|\n\n\n))', text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(0).strip()
    return text[:500]

for item in data.get("questions", []):
    if item.get("id") in q_ids:
        print(f"\n================ {item.get('id')} ================")
        responses = [r for r in item.get("nlmResponses", []) if len(r.get("rawResponse", "")) >= 200][:2]
        for i, r in enumerate(responses):
            ans_text = get_answer_determination(r.get("rawResponse", ""))
            print(f"NLM {i} default selectedOption: {r.get('selectedOption')}")
            print(f"--- NLM {i} Text ---")
            print(ans_text)
