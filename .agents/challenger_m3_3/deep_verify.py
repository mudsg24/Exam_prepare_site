import os
import re
import yaml
import json

SKILLS_DIR = os.path.expanduser("~/.gemini/config/skills")
EXAM_SKILLS = [
    "tn-exam-expert",
    "tn-exam-lecture-and-practice",
    "tn-exam-prepare",
    "tn-exam-producer",
    "tn-exam-qc",
    "tn-exam-query",
    "tn-exam-tutor"
]
PROJECT_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"

print("==================================================")
print("DEEP EMPIRICAL ANALYSIS OF ALL 7 SKILLS & PACKAGE.JSON")
print("==================================================\n")

# --- DETAIL CHECK 1: YAML Frontmatter & Detailed Structure ---
print("### 1. FRONTMATTER & STRUCTURE DETAILS ###")
for skill in EXAM_SKILLS:
    path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not fm_match:
        print(f"FAILED FRONTMATTER: {skill}")
        continue
    
    fm_text, body = fm_match.groups()
    data = yaml.safe_load(fm_text)
    
    print(f"[{skill}]")
    print(f"  Frontmatter keys: {list(data.keys())}")
    print(f"  Name: {data.get('name')}")
    print(f"  Description: {data.get('description')[:120]}...")
    
    # Extract headings
    h1 = re.findall(r"^#\s+(.+)$", body, re.M)
    h2 = re.findall(r"^##\s+(.+)$", body, re.M)
    h3 = re.findall(r"^###\s+(.+)$", body, re.M)
    print(f"  Headings: H1={len(h1)}, H2={len(h2)}, H3={len(h3)}")
    print(f"  H2 Sections: {h2}")
    print()

# --- DETAIL CHECK 2: Legacy Script Paths & Command References ---
print("### 2. LEGACY SCRIPT PATHS & SCRIPT REFERENCES ###")
for skill in EXAM_SKILLS:
    path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    script_refs = []
    npm_refs = []
    py_refs = []
    node_refs = []
    
    for idx, l in enumerate(lines, 1):
        if "scripts/" in l:
            script_refs.append((idx, l.strip()))
        if "npm run" in l:
            npm_refs.append((idx, l.strip()))
        if "python" in l and ".py" in l:
            py_refs.append((idx, l.strip()))
        if "node" in l and ".js" in l or ".mjs" in l:
            node_refs.append((idx, l.strip()))
    
    print(f"[{skill}]")
    print(f"  'scripts/' occurrences: {len(script_refs)}")
    for idx, l in script_refs:
        print(f"    Line {idx}: {l}")
    print(f"  'npm run' occurrences: {len(npm_refs)}")
    for idx, l in npm_refs:
        print(f"    Line {idx}: {l}")
    if py_refs:
        print(f"  direct python file execution refs: {len(py_refs)}")
        for idx, l in py_refs:
            print(f"    Line {idx}: {l}")
    if node_refs:
        print(f"  direct node file execution refs: {len(node_refs)}")
        for idx, l in node_refs:
            print(f"    Line {idx}: {l}")
    print()

# --- DETAIL CHECK 3: tn-exam-lecture-and-practice Dispatch Analysis ---
print("### 3. TN-EXAM-LECTURE-AND-PRACTICE DISPATCH LOGIC ###")
lap_path = os.path.join(SKILLS_DIR, "tn-exam-lecture-and-practice", "SKILL.md")
with open(lap_path, "r", encoding="utf-8") as f:
    lap_body = f.read()

print("Full text of execution steps in tn-exam-lecture-and-practice/SKILL.md:")
for line in lap_body.splitlines():
    if line.startswith("#") or "subagent" in line.lower() or "dispatch" in line.lower() or "pipeline" in line.lower():
        print(f"  {line}")

# Check if tn-exam-lecture-and-practice performs any direct generation or editing itself
direct_edit_terms = ["write_to_file", "replace_file_content", "fs.writeFileSync", "mkdir"]
found_direct = [term for term in direct_edit_terms if term in lap_body]
print(f"\nDirect file modification tool/func calls in tn-exam-lecture-and-practice: {found_direct}")

# --- DETAIL CHECK 4: tn-exam-expert QC References Analysis ---
print("### 4. TN-EXAM-EXPERT QC REFERENCES ###")
expert_path = os.path.join(SKILLS_DIR, "tn-exam-expert", "SKILL.md")
with open(expert_path, "r", encoding="utf-8") as f:
    expert_body = f.read()

expert_qc_matches = []
for idx, line in enumerate(expert_body.splitlines(), 1):
    if re.search(r"qc", line, re.IGNORECASE):
        expert_qc_matches.append((idx, line))

print(f"Total lines matching case-insensitive 'qc' in tn-exam-expert: {len(expert_qc_matches)}")
for line_no, text in expert_qc_matches:
    print(f"  Line {line_no}: {text}")

# Check if there are any actual QC execution calls or pipeline:qc in tn-exam-expert
qc_calls = [m for m in expert_qc_matches if "npm run pipeline:qc" in m[1] or "invoke_subagent" in m[1] or "/tn-exam-qc" in m[1] and not "不" in m[1] and not "NO QC" in m[1]]
print(f"Actual QC invocation calls in tn-exam-expert: {len(qc_calls)}")

# --- DETAIL CHECK 5: package.json vs SKILL references ---
print("\n### 5. PACKAGE.JSON PIPELINE COMMANDS & EXECUTION ###")
pkg_path = os.path.join(PROJECT_DIR, "package.json")
with open(pkg_path, "r", encoding="utf-8") as f:
    pkg = json.load(f)

scripts = pkg.get("scripts", {})
print("ALL scripts in package.json:")
for name, cmd in scripts.items():
    print(f"  \"{name}\": \"{cmd}\"")

# Collect all pipeline references across all 7 skills
skill_pipelines = {}
for skill in EXAM_SKILLS:
    path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r"npm run (pipeline:[\w:-]+)", content)
    skill_pipelines[skill] = set(matches)

print("\nPipeline script references by skill:")
all_referenced_pipelines = set()
for skill, refs in skill_pipelines.items():
    print(f"  {skill}: {refs}")
    all_referenced_pipelines.update(refs)

print(f"\nAll unique pipeline scripts referenced across 7 skills: {all_referenced_pipelines}")
pipeline_in_pkg = set(k for k in scripts.keys() if k.startswith("pipeline:"))
print(f"Pipeline scripts defined in package.json: {pipeline_in_pkg}")

missing = all_referenced_pipelines - pipeline_in_pkg
print(f"\nMISSING PIPELINE SCRIPTS IN PACKAGE.JSON: {missing}")

extra = pipeline_in_pkg - all_referenced_pipelines
print(f"PIPELINE SCRIPTS IN PACKAGE.JSON NOT REFERENCED IN SKILLS: {extra}")
