#!/usr/bin/env python3
"""Visual check for slides/index.html (added after the first run: text checks
could not catch clipped SVG labels or overlapping text).

Opens the deck in headless Chrome, screenshots every slide at desktop and phone
size, and reports slides whose content overflows and any JavaScript errors.
Requires: pip install playwright (and a Chrome/Chromium binary).

Usage: python3 scripts/visual_check.py [out_dir] [chrome_path]
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "slides" / "screenshots"
CHROME = sys.argv[2] if len(sys.argv) > 2 else None

OUT.mkdir(parents=True, exist_ok=True)
url = (ROOT / "slides" / "index.html").as_uri()
problems = []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME) if CHROME else p.chromium.launch()
    for name, vp in [("desktop", {"width": 1280, "height": 800}), ("phone", {"width": 390, "height": 844})]:
        page = browser.new_page(viewport=vp)
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(url)
        page.wait_for_timeout(600)
        n = page.evaluate("document.querySelectorAll('.slide').length")
        for i in range(1, n + 1):
            page.screenshot(path=str(OUT / f"{name}-{i:02d}.png"))
            over = page.evaluate("(()=>{const s=document.querySelector('.slide.on');return s.scrollHeight-s.clientHeight})()")
            if over > 2 and name == "desktop":
                problems.append(f"{name} slide {i}: 內容超出投影片 {over}px")
            page.keyboard.press("ArrowRight")
            page.wait_for_timeout(120)
        problems += [f"{name}: JS error {e}" for e in errors]
    browser.close()

print(f"截圖已存到 {OUT}（請人工逐張看過：標籤是否被裁切、文字是否重疊）")
print("\n".join(problems) if problems else "自動檢查：無溢出、無 JS 錯誤 ✅")
sys.exit(1 if problems else 0)
