import json
import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# Initialize client. Assumes GEMINI_API_KEY is in environment.
client = genai.Client()

class ProcessedQuestion(BaseModel):
    extracted_nlm0: str = Field(description="Exact option selected by NLM 0 (A, B, C, D, NONE, ALL)")
    extracted_nlm1: str = Field(description="Exact option selected by NLM 1 (A, B, C, D, NONE, ALL)")
    sourceExplanation: str = Field(description="Cleaned sourceExplanation")
    codexExplanation: str = Field(description="Cleaned codexExplanation")
    reconciliationNotes: str = Field(description="Cleaned reconciliationNotes")

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Membranous_nephropathy_(主題備考).json') as f:
    data = json.load(f)

questions = data['questions'][:5]
out_questions = []

prompt_template = """
You are a QC expert. 
Here is a question object with its NLM responses.
Determine the exact option (A, B, C, D, NONE, ALL) selected by NLM 0 and NLM 1 in `1. Answer Determination` or `Correct Option`. 
INSUFFICIENT Header False-NONE Guard: If NLM complains about INSUFFICIENT evidence but still selects a clear option based on medical consensus (e.g. Option C), you MUST extract `C`, not `NONE`.
Distractor Analysis Collision Guard: Only extract from the main determination section. Do not extract from distractor analysis.

Also enforce STRICT LANGUAGE RULES for "sourceExplanation", "codexExplanation", and "reconciliationNotes":
They must use Traditional Chinese narrative, but ALL medical terms MUST be purely English (e.g., no "膜性腎病變", must be "Membranous nephropathy"; no bilingual brackets). Clean them if needed. Keep None if it was originally None or empty.

Here is the data:
sourceExplanation: {sourceExplanation}
codexExplanation: {codexExplanation}
reconciliationNotes: {reconciliationNotes}

NLM 0:
{nlm0}

NLM 1:
{nlm1}
"""

for i, q in enumerate(questions):
    nlm0 = q.get('nlmResponses', [{}])[0].get('rawResponse', '')
    nlm1 = q.get('nlmResponses', [{}, {}])[1].get('rawResponse', '')
    
    prompt = prompt_template.format(
        sourceExplanation=q.get('sourceExplanation', ''),
        codexExplanation=q.get('codexExplanation', ''),
        reconciliationNotes=q.get('reconciliationNotes', ''),
        nlm0=nlm0,
        nlm1=nlm1
    )
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ProcessedQuestion,
        ),
    )
    
    res_obj = json.loads(response.text)
    
    # Update fields
    q['nlmResponses'][0]['selectedOption'] = res_obj['extracted_nlm0']
    q['nlmResponses'][1]['selectedOption'] = res_obj['extracted_nlm1']
    
    if q.get('sourceExplanation'):
        q['sourceExplanation'] = res_obj['sourceExplanation']
    if q.get('codexExplanation'):
        q['codexExplanation'] = res_obj['codexExplanation']
    if q.get('reconciliationNotes'):
        q['reconciliationNotes'] = res_obj['reconciliationNotes']
        
    source_ans = q.get('sourceProvidedAnswer')
    
    if res_obj['extracted_nlm0'] == res_obj['extracted_nlm1'] and res_obj['extracted_nlm0'] == source_ans:
        q['reconciliationStatus'] = "HIGH_CONFIDENCE"
        q['qcStatus'] = "QC_PASSED"
        q['qcNotes'] = "NLM responses match source provided answer. Medical terms cleaned."
    else:
        q['reconciliationStatus'] = "DISPUTED"
        q['qcStatus'] = "QC_DISPUTED"
        q['qcNotes'] = f"NLM responses (0: {res_obj['extracted_nlm0']}, 1: {res_obj['extracted_nlm1']}) differ from source ({source_ans}). Medical terms cleaned."
        
    q['qcVerified'] = True
    
    out_questions.append(q)

out_file = "/Users/yuan/.gemini/antigravity/brain/4909a022-7bf3-4406-8274-12c81220761e/scratch/qc_2026_Membranous_nephropathy_(主題備考).json_0_4.json"
with open(out_file, 'w') as f:
    json.dump(out_questions, f, ensure_ascii=False, indent=2)

print(f"Processed 5 questions and saved to {out_file}")
