#!/usr/bin/env python3
"""Check the generated HTML slides against the wiki (AGENTS.md §7).

Checks, per <section class="slide">:
  1. has a data-wiki attribute (except cover) and every referenced wiki page exists
  2. every number with a unit (%, 倍, ×) or large number (e.g. 200,000) in the slide text
     appears in at least one of the referenced wiki pages
  3. glossary terms: the FIRST time a glossary term appears in the deck it must be
     wrapped in <abbr title="..."> so beginners get a Chinese explanation

Usage: python3 scripts/check_slides.py [slides/index.html]
Exit code 0 = pass, 1 = problems found.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

# English terms that need a Chinese explanation on first use (subset of wiki/glossary.md)
TERMS = ["LLM", "Agent", "Workflow", "Tool use", "Context window", "Token", "ReAct",
         "ACI", "Orchestrator", "Guardrail", "Prompt injection", "Hallucination",
         "Chain of Thought", "Embedding", "Handoff", "LLM-as-judge"]


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.depth = [], None, 0
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "slide" in (a.get("class") or "").split():
            self.cur = {"id": a.get("id", f"#{len(self.slides)+1}"), "wiki": a.get("data-wiki"),
                        "text": [], "abbr": [], "html": []}
            self.depth = 1
            return
        if self.cur is not None:
            if tag == "section":
                self.depth += 1
            if tag in ("script", "style"):
                self.skip += 1
            if tag == "abbr" and a.get("title"):
                self.cur["abbr_open"] = True
            self.cur["html"].append(self.get_starttag_text() or "")

    def handle_endtag(self, tag):
        if self.cur is None:
            return
        if tag in ("script", "style"):
            self.skip -= 1
        if tag == "abbr":
            self.cur["abbr_open"] = False
        if tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.slides.append(self.cur)
                self.cur = None

    def handle_data(self, data):
        if self.cur is not None and not self.skip:
            self.cur["text"].append(data)
            if self.cur.get("abbr_open"):
                self.cur["abbr"].append(data.strip())


NUM_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(%|倍|×)|(\d{1,3}(?:,\d{3})+)")


def number_in(text, num, unit):
    if unit is None:
        return num in text
    units = {"%": ["%"], "倍": ["倍", "×"], "×": ["倍", "×"]}[unit]
    return any(re.search(re.escape(num) + r"\s*" + re.escape(u), text) for u in units)


def main():
    html_path = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "slides/index.html")
    p = SlideParser()
    p.feed(html_path.read_text(encoding="utf-8"))
    problems, rows, seen_terms = [], [], set()

    for i, s in enumerate(p.slides, 1):
        text = " ".join(" ".join(s["text"]).split())
        refs = [r.strip() for r in (s["wiki"] or "").split(",") if r.strip()]
        status = "OK"
        if i > 1 and not refs:
            problems.append(f"slide {i}: 缺少 data-wiki")
            status = "缺 data-wiki"
        wiki_text = ""
        for r in refs:
            f = WIKI / r
            if not f.exists():
                problems.append(f"slide {i}: data-wiki 指向不存在的頁面 {r}")
                status = "引用失效"
            else:
                wiki_text += f.read_text(encoding="utf-8")
        nums = []
        for m in NUM_RE.finditer(text):
            num, unit = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), None)
            nums.append(num + (unit or ""))
            if refs and not number_in(wiki_text, num, unit):
                problems.append(f"slide {i}: 數字「{num}{unit or ''}」在引用的 wiki 頁面中找不到")
                status = "數字無出處"
        abbrs = " ".join(s["abbr"])
        for t in TERMS:
            if t in seen_terms:
                continue
            if re.search(r"(?<![A-Za-z])" + re.escape(t) + r"(?![A-Za-z])", text, re.I):
                seen_terms.add(t)
                if not re.search(re.escape(t), abbrs, re.I):
                    problems.append(f"slide {i}: 術語「{t}」第一次出現但沒有 <abbr title> 中文解釋")
                    if status == "OK":
                        status = "術語未解釋"
        rows.append((i, s["id"], ", ".join(refs) or "—", ", ".join(nums) or "—", status))

    print("| # | slide id | data-wiki | 數字 | 狀態 |\n|---|---|---|---|---|")
    for r in rows:
        print("| " + " | ".join(str(x) for x in r) + " |")
    print()
    if problems:
        print(f"## 問題（{len(problems)}）\n")
        for pr in problems:
            print("- " + pr)
        return 1
    print("全部通過 ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
