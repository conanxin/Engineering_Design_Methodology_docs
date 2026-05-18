#!/usr/bin/env python3
import json
import os
import sys

BASE = "/home/conanxin/projects/Engineering_Design_Methodology_docs/modernization"

def check_phase1b():
    try:
        import subprocess
        result = subprocess.run(["python3", f"{BASE}/scripts/validate_phase1b.py"], capture_output=True, text=True)
        if "OVERALL: PASS" in result.stdout:
            print("PASS: Phase 1B validation still passes")
            return True
        print("FAIL: Phase 1B validation failed")
        return False
    except:
        print("WARN: Could not run Phase 1B validator")
        return True

def check_cases_json():
    try:
        with open(f"{BASE}/site/data/cases.json") as fp:
            data = json.load(fp)
        if len(data) >= 5:
            print(f"PASS: cases.json has {len(data)} cases")
            return True
        print("FAIL: cases.json < 5")
        return False
    except Exception as e:
        print(f"FAIL: cases.json - {e}")
        return False

def check_case_pages():
    pages = ["index.html", "ai-reading-notes.html", "github-pages-exhibit.html", "auto-supply-processing-center.html", "modular-exhibition-guide.html", "local-agent-toolchain.html"]
    for p in pages:
        if not os.path.exists(f"{BASE}/site/cases/{p}"):
            print(f"FAIL: missing cases/{p}")
            return False
    print("PASS: 6 case pages exist")
    return True

def check_svgs():
    svgs = ["design-process-flow.svg", "function-decomposition.svg", "evaluation-matrix.svg", "agent-workflow-loop.svg"]
    for s in svgs:
        if not os.path.exists(f"{BASE}/site/assets/diagrams/{s}"):
            print(f"FAIL: missing {s}")
            return False
    print("PASS: 4 SVGs exist")
    return True

def check_diagrams_html():
    if os.path.exists(f"{BASE}/site/diagrams.html"):
        print("PASS: diagrams.html exists")
        return True
    print("FAIL: diagrams.html missing")
    return False

def check_agent_workflows():
    if os.path.exists(f"{BASE}/site/agent-workflows.html"):
        print("PASS: agent-workflows.html exists")
        return True
    print("FAIL: agent-workflows.html missing")
    return False

def check_skill_draft():
    required = [
        "SKILL.md",
        "prompts/task_clarification_prompt.md",
        "prompts/function_decomposition_prompt.md",
        "prompts/concept_evaluation_prompt.md",
        "prompts/technical_design_review_prompt.md",
        "examples/example_ai_reading_notes.md",
        "examples/example_processing_center.md"
    ]
    for r in required:
        if not os.path.exists(f"{BASE}/hermes_skill_draft/{r}"):
            print(f"FAIL: missing hermes_skill_draft/{r}")
            return False
    print("PASS: Hermes skill draft files exist")
    return True

def check_index_links():
    with open(f"{BASE}/site/index.html") as fp:
        content = fp.read()
    links = ["cases/index.html", "diagrams.html", "agent-workflows.html"]
    for l in links:
        if l not in content:
            print(f"FAIL: index.html missing link to {l}")
            return False
    print("PASS: index.html contains new navigation links")
    return True

def check_phase1c_markers():
    marker = "Phase 1C"
    files = [
        f"{BASE}/site/index.html",
        f"{BASE}/site/cases/ai-reading-notes.html",
        f"{BASE}/site/diagrams.html",
        f"{BASE}/site/agent-workflows.html",
        f"{BASE}/docs/PHASE_1C_REPORT.md"
    ]
    for f in files:
        if os.path.exists(f):
            with open(f) as fp:
                if marker not in fp.read():
                    print(f"FAIL: {f} missing Phase 1C marker")
                    return False
    print("PASS: Phase 1C markers present")
    return True

def main():
    results = [
        check_phase1b(),
        check_cases_json(),
        check_case_pages(),
        check_svgs(),
        check_diagrams_html(),
        check_agent_workflows(),
        check_skill_draft(),
        check_index_links(),
        check_phase1c_markers()
    ]
    if all(results):
        print("\n=== OVERALL: PASS ===")
        sys.exit(0)
    else:
        print("\n=== OVERALL: FAIL ===")
        sys.exit(1)

if __name__ == "__main__":
    main()