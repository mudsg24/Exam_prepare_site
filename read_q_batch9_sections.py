import json

targets = {
    "2026_water_treatment_system_in_hemodialysis_(主題備考).json": ["2026_water_treatment_system_in_hemodialysis_(主題備考)_q9"],
    "2026_北榮_(重點轉化).json": ["q24"],
    "2026_奇美_(重點轉化).json": ["Q16"],
    "2026_成大_Cases_(重點轉化).json": ["2026_成大_Cases_Q02", "2026_成大_Cases_Q03", "2026_成大_Cases_Q13", "2026_成大_Cases_Q15", "2026_成大_Cases_Q17", "2026_成大_Cases_Q19", "2026_成大_Cases_Q22", "2026_成大_Cases_Q26", "2026_成大_Cases_Q28"],
    "2026_高醫__基礎_(重點轉化).json": ["q_13", "q_24", "q_25", "q_26"],
    "2026_高長_(重點轉化).json": ["2026_高長_Q09", "2026_高長_Q10", "2026_高長_Q18"]
}

for filename, qids in targets.items():
    filepath = f"/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{filename}"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        for q in data.get("questions", []):
            if q["id"] in qids:
                print(f"\n======== FILE: {filename} | QID: {q['id']} | TRUTH: {q.get('sourceProvidedAnswer')} ========")
                for idx, nlm in enumerate(q.get("nlmResponses", [])):
                    text = nlm.get('rawResponse', '')
                    # We want to extract just the part about Answer Determination or Clinical Consensus
                    # Let's split by "###" and print the first few sections.
                    sections = text.split("###")
                    extracted = ""
                    for s in sections:
                        if "Answer Determination" in s or "正解判定" in s or "答案判定" in s or "共識" in s or "Correct Option" in s:
                            extracted += "###" + s
                    if not extracted:
                        # Fallback
                        extracted = text[:500]
                    print(f"\n--- NLM{idx+1} ---\n{extracted.strip()}")
    except Exception as e:
        pass
