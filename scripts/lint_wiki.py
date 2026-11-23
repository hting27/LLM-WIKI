#!/usr/bin/env python3
"""Lint the LLM Wiki according to AGENTS.md §8.

Usage:  python3 scripts/lint_wiki.py [--report wiki/lint-report.md]
Exit code 0 = no errors (warnings allowed), 1 = errors found.
"""
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
AGENTS = ROOT / "AGENTS.md"

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+\.md)(#[^)]*)?\)")
SRC_TAG_RE = re.compile(r"\[(S\d+(?:\s*[,，、]\s*S\d+)*)\]")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def registered_sources():
    text = AGENTS.read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*(S\d+)\s*\|", text, re.M))


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def paragraphs(body):
    """Yield content paragraphs (skip headings, tables, code, blank, links-only lines)."""
    in_code = False
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if b.startswith("```"):
            in_code = not in_code if b.count("```") == 1 else in_code
            continue
        if in_code or not b or b.startswith("#") or b.startswith("|") or b.startswith(">"):
            continue
        yield b


def main():
    report_path = None
    if "--report" in sys.argv:
        report_path = ROOT / sys.argv[sys.argv.index("--report") + 1]

    known_src = registered_sources()
    pages = sorted(p for p in WIKI.rglob("*.md") if p.name != "lint-report.md")
    rel = {p: p.relative_to(WIKI).as_posix() for p in pages}
    inbound = {r: set() for r in rel.values()}
    errors, warnings = [], []

    index_text = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""

    for p in pages:
        r = rel[p]
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if r in ("index.md", "log.md"):
            fm = fm or {}
        elif fm is None:
            errors.append(f"[frontmatter] {r}: 缺少 frontmatter")
            fm = {}
        else:
            for key in ("title", "type", "sources", "updated"):
                if key not in fm:
                    errors.append(f"[frontmatter] {r}: 缺少欄位 `{key}`")

        # declared sources registered?
        declared = set(re.findall(r"S\d+", fm.get("sources", "")))
        for s in declared - known_src:
            errors.append(f"[source] {r}: frontmatter 使用未登錄的來源 {s}")

        # links
        for m in LINK_RE.finditer(text):
            target = (p.parent / m.group(1)).resolve()
            try:
                tr = target.relative_to(WIKI.resolve()).as_posix()
            except ValueError:
                tr = None
            if not target.exists():
                errors.append(f"[link] {r}: 失效連結 → {m.group(1)}")
            elif tr in inbound and tr != r:
                inbound[tr].add(r)

        # inline source tags
        used = set()
        for m in SRC_TAG_RE.finditer(text):
            used |= set(re.findall(r"S\d+", m.group(1)))
        for s in used - known_src:
            errors.append(f"[source] {r}: 內文使用未登錄的來源標註 [{s}]")
        if fm.get("type") == "concept":
            undeclared = used - declared
            if undeclared:
                warnings.append(f"[source] {r}: 內文引用 {sorted(undeclared)} 但 frontmatter sources 沒列")
            body = FM_RE.sub("", text, count=1)
            paras = list(paragraphs(body))
            def link_only(block):
                # a block whose every line is just a markdown link (+ optional short note)
                return all(re.match(r"^(- )?\[[^\]]*\]\([^)]*\)", ln.strip()) for ln in block.splitlines())
            untagged = [x for x in paras if not SRC_TAG_RE.search(x) and "[整理]" not in x
                        and not link_only(x) and len(x) > 40]
            if paras and len(untagged) / len(paras) > 0.3:
                warnings.append(f"[citation] {r}: {len(untagged)}/{len(paras)} 個段落沒有來源標註")

        # index coverage
        if r not in ("index.md",) and r not in index_text:
            errors.append(f"[index] index.md 沒有列出 {r}")

    for r, srcs in inbound.items():
        if r in ("index.md", "log.md", "glossary.md"):
            continue
        others = srcs - {"index.md"}
        if not others:
            warnings.append(f"[orphan] {r}: 除了 index 以外沒有任何頁面連到它")

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"# Lint report ({stamp})", "",
             f"- 頁面數：{len(pages)}",
             f"- 錯誤：{len(errors)}",
             f"- 警告：{len(warnings)}", ""]
    if errors:
        lines += ["## 錯誤", ""] + [f"- {e}" for e in errors] + [""]
    if warnings:
        lines += ["## 警告", ""] + [f"- {w}" for w in warnings] + [""]
    if not errors and not warnings:
        lines += ["全部通過 ✅", ""]
    out = "\n".join(lines)
    print(out)
    if report_path:
        report_path.write_text(
            "---\ntitle: Lint report\ntype: meta\nsources: []\nupdated: "
            + datetime.now().strftime("%Y-%m-%d") + "\n---\n\n" + out, encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
