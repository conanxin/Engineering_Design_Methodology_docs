#!/usr/bin/env python3
import json
import os
import sys

BASE = "/home/conanxin/projects/Engineering_Design_Methodology_docs"

def check_files_exist():
    files = [
        "modernization/site/guide.html",
        "modernization/site/templates.html",
        "modernization/site/concepts.html",
        "docs/guide.html",
        "docs/templates.html",
        "docs/concepts.html"
    ]
    for f in files:
        if not os.path.exists(f"{BASE}/{f}"):
            print(f"FAIL: missing {f}")
            return False
    print("PASS: new pages exist")
    return True

def check_index_links():
    with open(f"{BASE}/docs/index.html") as fp:
        content = fp.read()
    links = ["guide.html", "templates.html", "concepts.html"]
    for l in links:
        if l not in content:
            print(f"FAIL: index.html missing link to {l}")
            return False
    print("PASS: index.html contains new page links")
    return True

def check_js_features():
    with open(f"{BASE}/docs/assets/js/app.js") as fp:
        content = fp.read()
    if "concepts.json" in content and ("copy-template" in content or "copy-command" in content):
        print("PASS: JS contains concept loading and copy functionality")
        return True
    print("FAIL: JS missing required features")
    return False

def check_css_features():
    with open(f"{BASE}/docs/assets/css/styles.css") as fp:
        content = fp.read()
    if "copy-template" in content or "concept" in content.lower():
        print("PASS: CSS contains template/concept styles")
        return True
    print("FAIL: CSS missing required styles")
    return False

def check_data_files():
    files = ["concepts.json", "chapters.json", "cases.json"]
    for f in files:
        try:
            with open(f"{BASE}/docs/data/{f}") as fp:
                data = json.load(fp)
            if f == "concepts.json" and len(data) < 20:
                print(f"FAIL: {f} has less than 20 concepts")
                return False
            if f == "chapters.json" and len(data) != 10:
                print(f"FAIL: {f} does not have 10 chapters")
                return False
            if f == "cases.json" and len(data) < 5:
                print(f"FAIL: {f} has less than 5 cases")
                return False
            print(f"PASS: {f} valid and sufficient")
        except Exception as e:
            print(f"FAIL: {f} - {e}")
            return False
    return True

def check_forbidden():
    forbidden = ["source_archive", "hermes_skill_draft", "/home/conanxin"]
    for item in forbidden:
        result = os.popen(f'grep -r "{item}" {BASE}/docs/ --exclude-dir=data 2>/dev/null | head -1').read()
        if result:
            print(f"FAIL: found forbidden content {item}")
            return False
    print("PASS: no forbidden content in docs")
    return True

def main():
    results = [
        check_files_exist(),
        check_index_links(),
        check_js_features(),
        check_css_features(),
        check_data_files(),
        check_forbidden()
    ]
    if all(results):
        print("\n=== OVERALL: PASS ===")
        sys.exit(0)
    else:
        print("\n=== OVERALL: FAIL ===")
        sys.exit(1)

if __name__ == "__main__":
    main()