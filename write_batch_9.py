import json

output_data = {
  "batch_id": "batch_9",
  "status": "COMPLETED",
  "processed_count": 19,
  "results": [
    {
      "file": "2026_water_treatment_system_in_hemodialysis_(主題備考).json",
      "question_id": "2026_water_treatment_system_in_hemodialysis_(主題備考)_q9",
      "nlm_answers": ["A", "A"],
      "truth": "A",
      "reconciliationStatus": "HIGH_CONFIDENCE"
    },
    {
      "file": "2026_北榮_(重點轉化).json",
      "question_id": "q24",
      "nlm_answers": ["NONE", "A"],
      "truth": "A",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_奇美_(重點轉化).json",
      "question_id": "Q16",
      "nlm_answers": ["NONE", "NONE"],
      "truth": "D",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q02",
      "nlm_answers": ["NONE", "NONE"],
      "truth": "B",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q03",
      "nlm_answers": ["C", "C"],
      "truth": "C",
      "reconciliationStatus": "HIGH_CONFIDENCE"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q13",
      "nlm_answers": ["NONE", "A"],
      "truth": "A",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q15",
      "nlm_answers": ["A", "A"],
      "truth": "A",
      "reconciliationStatus": "HIGH_CONFIDENCE"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q17",
      "nlm_answers": ["NONE", "NONE"],
      "truth": "C",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q19",
      "nlm_answers": ["NONE", "B"],
      "truth": "B",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q22",
      "nlm_answers": ["NONE", "NONE"],
      "truth": "D",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q26",
      "nlm_answers": ["NONE", "C"],
      "truth": "C",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_成大_Cases_(重點轉化).json",
      "question_id": "2026_成大_Cases_Q28",
      "nlm_answers": ["NONE", "D"],
      "truth": "D",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_高醫__基礎_(重點轉化).json",
      "question_id": "q_13",
      "nlm_answers": ["NONE", "NONE"],
      "truth": "A",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_高醫__基礎_(重點轉化).json",
      "question_id": "q_24",
      "nlm_answers": ["B", "B"],
      "truth": "B",
      "reconciliationStatus": "HIGH_CONFIDENCE"
    },
    {
      "file": "2026_高醫__基礎_(重點轉化).json",
      "question_id": "q_25",
      "nlm_answers": ["C", "C"],
      "truth": "C",
      "reconciliationStatus": "HIGH_CONFIDENCE"
    },
    {
      "file": "2026_高醫__基礎_(重點轉化).json",
      "question_id": "q_26",
      "nlm_answers": ["NONE", "NONE"],
      "truth": "D",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_高長_(重點轉化).json",
      "question_id": "2026_高長_Q09",
      "nlm_answers": ["B", "NONE"],
      "truth": "B",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_高長_(重點轉化).json",
      "question_id": "2026_高長_Q10",
      "nlm_answers": ["NONE", "C"],
      "truth": "C",
      "reconciliationStatus": "DISPUTED"
    },
    {
      "file": "2026_高長_(重點轉化).json",
      "question_id": "2026_高長_Q18",
      "nlm_answers": ["NONE", "A"],
      "truth": "A",
      "reconciliationStatus": "DISPUTED"
    }
  ]
}

with open("/Users/yuan/.gemini/antigravity/brain/60908ade-a9fb-4a5c-8793-5ff5f706b791/scratch/qc_stage2_batch_9.json", "w") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)
