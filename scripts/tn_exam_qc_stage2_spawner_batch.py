import json

with open("scratch/stage2_tasks.json", "r") as f:
    tasks = json.load(f)

# Flatten into a list of (filename, q_id)
all_questions = []
for task in tasks:
    for q_id in task["qIds"]:
        all_questions.append((task["file"], q_id))

BATCH_SIZE = 25
subagents = []

for i in range(0, len(all_questions), BATCH_SIZE):
    batch = all_questions[i:i+BATCH_SIZE]
    
    # group by file in this batch
    file_map = {}
    for filename, q_id in batch:
        if filename not in file_map:
            file_map[filename] = []
        file_map[filename].append(q_id)
        
    targets_str = ""
    for filename, q_ids in file_map.items():
        targets_str += f"- `/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{filename}`: {', '.join(q_ids)}\n"
        
    prompt = f"""You are the QC Subagent for Phase 2 Semantic Verification.
Your target files and questions are:
{targets_str}

GOVERNANCE & EXTRACTOR RULES:
1. USE HIGH REASONING EFFORT. 0% REGEX & 0% STRING MATCHING. Read the full NLM response text and use natural language reasoning to determine the exact option (A, B, C, D, NONE, ALL) selected by NLM in `1. Answer Determination` or `Correct Option`. 
2. INSUFFICIENT Header False-NONE Guard: If NLM complains about INSUFFICIENT evidence but still selects a clear option based on medical consensus (e.g. Option C), you MUST extract `C`, not `NONE`.
3. Distractor Analysis Collision Guard: Only extract from the main determination section. Do not extract from distractor analysis.
4. For each specified question in each file:
   - Examine `q.nlmResponses[0].rawResponse`: determine the selected option. Set `q.nlmResponses[0].selectedOption`.
   - Examine `q.nlmResponses[1].rawResponse`: determine the selected option. Set `q.nlmResponses[1].selectedOption`.
   - Determine `q.reconciliationStatus`: "HIGH_CONFIDENCE" if NLM1 and NLM2 match and also match `sourceProvidedAnswer`. Else "DISPUTED".
   - Set `q.qcVerified` to true, `q.qcStatus` to "QC_PASSED" or "QC_DISPUTED", and write a brief `qcNotes`.
5. Output the finalized processed question objects as a dictionary keyed by filename, and save it to `/Users/yuan/.gemini/antigravity/brain/60908ade-a9fb-4a5c-8793-5ff5f706b791/scratch/qc_stage2_batch_{i//BATCH_SIZE}.json` using write_to_file.
Format: {{"file1.json": [{{processed_q1}}, {{processed_q2}}], "file2.json": [...]}}
DO NOT modify the main JSON directly to avoid race conditions.
"""
    subagents.append({
        "TypeName": "self",
        "Role": f"QC Batch {i//BATCH_SIZE}",
        "Prompt": prompt,
        "Model": "pro"
    })

payload = {"Subagents": subagents}
with open("scratch/stage2_payload_batch.json", "w") as f:
    json.dump(payload, f, indent=2)

print(f"Generated {len(subagents)} subagents in scratch/stage2_payload_batch.json")
