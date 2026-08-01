import json

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

print(f"Paper Title: {paper.get('title')}")
print(f"Total Questions: {len(paper.get('questions', []))}")

stage1_failures = []
stage2_targets = []

for q in paper.get('questions', []):
    qid = q.get('id')
    nlm_resps = q.get('nlmResponses', [])
    num_resps = len(nlm_resps)
    
    tech_fail = False
    if num_resps < 2:
        tech_fail = True
    else:
        for r in nlm_resps:
            raw_len = len(r.get('rawResponse', ''))
            has_err = r.get('error') is not None
            if raw_len < 200 or has_err:
                tech_fail = True
                break
                
    if tech_fail:
        stage1_failures.append(q)
    else:
        stage2_targets.append(q)

print(f"Stage 1 Technical Failures (need NLM re-ask): {len(stage1_failures)}")
print(f"Stage 2 Subagent Review Scope: {len(stage2_targets)}")

for q in stage1_failures:
    print(f"  Stage 1 fail Q{q.get('number')}: nlmCount={len(q.get('nlmResponses', []))}")
    for idx, r in enumerate(q.get('nlmResponses', [])):
        print(f"    - NLM {idx+1}: len={len(r.get('rawResponse', ''))}, err={r.get('error')}, suff={r.get('databaseSufficiency')}")
