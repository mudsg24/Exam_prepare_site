import json, re

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_高長_(重點轉化).json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_ids = [f"2026_高長_Q{i}" for i in range(12, 23)]
for q in data.get("questions", []):
    if q.get("id") in q_ids:
        print(f"\n================ {q.get('id')} ================")
        valid_resps = []
        seen = set()
        for r in q.get("nlmResponses", []):
            raw = r.get("rawResponse", "")
            if len(raw) >= 200 and raw not in seen:
                seen.add(raw)
                valid_resps.append(r)
        
        if len(valid_resps) == 1:
            valid_resps.append(valid_resps[0])
        elif len(valid_resps) == 0:
            print("ERROR NO VALID RESPS")
            
        valid_resps = valid_resps[:2]
        for i, r in enumerate(valid_resps):
            raw = r.get("rawResponse", "")
            match = re.search(r"(?:1\.\s*)?(?:Answer Determination|正解判定|解答判定|答案判定|正解).*?(?=\n\s*(?:2\.|### 2\.|Distractor|Rationale|##|\n\n\n))", raw, re.DOTALL | re.IGNORECASE)
            ans = match.group(0).strip() if match else raw[:500]
            print(f"--- NLM {i} ---")
            print(ans)
