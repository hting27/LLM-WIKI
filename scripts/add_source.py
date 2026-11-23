#!/usr/bin/env python3
"""Sync a concept page after adding content from a new source.

Adds the source code to frontmatter `sources`, appends a link under `## 來源`,
and updates the page's row in wiki/index.md. (Created after lint round 2 showed
that this step was easy to forget when editing by hand.)

Usage: python3 scripts/add_source.py S4 wiki/concepts/tool-use.md [more pages...]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"


def source_page(code):
    hits = sorted((WIKI / "sources").glob(code.lower() + "-*.md"))
    if not hits:
        sys.exit(f"找不到 {code} 的來源頁（wiki/sources/{code.lower()}-*.md）")
    return hits[0].name


def key(s):
    return int(s[1:])


def main():
    code, pages = sys.argv[1].upper(), sys.argv[2:]
    src_file = source_page(code)
    index = (WIKI / "index.md").read_text(encoding="utf-8")
    for page in pages:
        p = (ROOT / page) if not Path(page).is_absolute() else Path(page)
        t = p.read_text(encoding="utf-8")
        # 1. frontmatter
        m = re.search(r"^sources: \[(.*?)\]$", t, re.M)
        codes = {c.strip() for c in m.group(1).split(",") if c.strip()} | {code}
        t = t[:m.start()] + "sources: [" + ", ".join(sorted(codes, key=key)) + "]" + t[m.end():]
        # 2. 來源 block
        link = f"- [{code}](../sources/{src_file})"
        if link not in t:
            t = t.rstrip("\n") + "\n" + link + "\n"
        p.write_text(t, encoding="utf-8")
        # 3. index row
        rel = p.relative_to(WIKI).as_posix()
        row_re = re.compile(r"^(\| \[" + re.escape(rel) + r"\].*\| )([S\d, ]+)( \|)$", re.M)
        rm = row_re.search(index)
        if rm:
            rc = {c.strip() for c in rm.group(2).split(",")} | {code}
            index = index[:rm.start(2)] + ", ".join(sorted(rc, key=key)) + index[rm.end(2):]
        print(f"synced {rel}: sources={sorted(codes, key=key)}")
    (WIKI / "index.md").write_text(index, encoding="utf-8")


if __name__ == "__main__":
    main()
