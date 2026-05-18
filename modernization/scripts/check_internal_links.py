#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

BASE = Path("/home/conanxin/projects/Engineering_Design_Methodology_docs/docs")

def find_html_files():
    return list(BASE.rglob("*.html"))

def extract_links(html_file):
    content = html_file.read_text(encoding="utf-8")
    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    return links

def is_external(link):
    return link.startswith(("http://", "https://", "mailto:", "#"))

def check_link(base_file, link):
    if is_external(link):
        return True
    target = (base_file.parent / link).resolve()
    return target.exists()

def main():
    broken = []
    html_files = find_html_files()
    for html in html_files:
        for link in extract_links(html):
            if not check_link(html, link):
                broken.append(f"{html.relative_to(BASE)} -> {link}")
    if broken:
        print("BROKEN LINKS:")
        for b in broken:
            print(f"  {b}")
        sys.exit(1)
    else:
        print("INTERNAL_LINKS: PASS")
        sys.exit(0)

if __name__ == "__main__":
    main()