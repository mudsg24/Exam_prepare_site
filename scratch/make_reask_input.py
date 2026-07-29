import json

with open('scratch/nlm_input_questions.json') as f:
    questions = json.load(f)

# Select questions that need re-asking to reach 2 valid SUFFICIENT runs
needed_ids = ["2026_Inherited_RTA_Q03", "2026_Inherited_RTA_Q05", "2026_Inherited_RTA_Q14", "2026_Inherited_RTA_Q15", "2026_Inherited_RTA_Q16", "2026_Inherited_RTA_Q17", "2026_Inherited_RTA_Q18", "2026_Inherited_RTA_Q19", "2026_Inherited_RTA_Q20"]

reask_input = []
for q in questions:
    if q['id'] in needed_ids:
        # Simplify/clean stem slightly to avoid size limit or refusal pattern triggering
        stem = q['stem']
        # For Q03
        if q['id'] == "2026_Inherited_RTA_Q03":
            stem = "A 4-year-old child presents with growth retardation, severe hypokalemic metabolic acidosis, and bilateral medullary nephrocalcinosis. Urine pH remains > 6.0 during systemic acidosis. Hearing is normal. Genetic testing identifies a homozygous mutation in ATP6V0A4. Why is hearing preserved in patients with ATP6V0A4 mutations compared to ATP6V1B1 mutations?"
        elif q['id'] == "2026_Inherited_RTA_Q05":
            stem = "A 45-year-old male receiving IV Amphotericin B for invasive fungal infection develops hyperchloremic metabolic acidosis with hypokalemia and urine pH 6.5. Which mechanism best distinguishes Amphotericin B-induced distal RTA from Lithium-induced distal RTA?"
        elif q['id'] == "2026_Inherited_RTA_Q19":
            stem = "Which principle accurately contrasts the therapeutic management of Proximal RTA (Type 2 pRTA) versus Classic Distal RTA (Type 1 dRTA)?"

        q1 = dict(q)
        q1['id'] = f"{q['id']}_reask_run1"
        q1['stem'] = stem
        reask_input.append(q1)

        q2 = dict(q)
        q2['id'] = f"{q['id']}_reask_run2"
        q2['stem'] = stem
        reask_input.append(q2)

with open('scratch/reask_input.json', 'w', encoding='utf-8') as f:
    json.dump(reask_input, f, ensure_ascii=False, indent=2)

print(f"Created reask input with {len(reask_input)} items.")
