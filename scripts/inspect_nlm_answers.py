import json
import re

p1 = json.load(open('/tmp/fresh_pass1.json'))
p2 = json.load(open('/tmp/fresh_pass2.json'))
paper = json.load(open('/tmp/fresh_paper_dual_nlm.json'))

p1_map = {x['q_id']: x for x in p1}
p2_map = {x['q_id']: x for x in p2}

for q in paper['questions']:
    qid = q['id']
    qnum = q['number']
    src = q['sourceProvidedAnswer']
    opts = q['options']
    opt_dict = {o['id']: o['text'] for o in opts}
    
    r1 = p1_map.get(qid, {}).get('raw_response', '')
    r2 = p2_map.get(qid, {}).get('raw_response', '')
    
    h1 = r1[:400] if r1 else "NONE"
    h2 = r2[:400] if r2 else "NONE"
    
    print(f"=== Q{qnum} (Ground Truth: {src} -> {opt_dict.get(src, '')[:40]}) ===")
    print(f"NLM1 Answer Header:\n{h1[:200]}\n")
    print(f"NLM2 Answer Header:\n{h2[:200]}\n")
