import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Hyperphosphatemia_(主題備考).json", "r") as f:
    data = json.load(f)

questions = data.get("questions", [])
target_qs = [q for q in questions if 16 <= int(q["number"]) <= 20]

import re

def determine_option(text):
    # Quick regex fallback for python extraction if needed, but the prompt says 0% regex for LLM.
    # Wait, the prompt says *I* (the QC Subagent) must use natural language reasoning.
    # Let me just dump the JSON for Q16-Q20 so I can read it and reason.
    pass

with open("q16_20.json", "w") as f:
    json.dump(target_qs, f, indent=2, ensure_ascii=False)
