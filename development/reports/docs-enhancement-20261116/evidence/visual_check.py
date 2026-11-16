"""Responsive check of changed pages: 390/1440 px, light/dark, from a local build (file://)."""
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

BUILD = Path(sys.argv[1])
OUT = Path(sys.argv[2])
PAGES = [
    "sections/what-and-why.html",
    "what-is-ce.html",
    "sections/how-ce-works.html",
    "foundations/concepts/ce_workflow.html",
    "foundations/concepts/calibration_methods.html",
    "foundations/how-to/interpret_explanations.html",
    "get-started/quick_api.html",
    "get-started/troubleshooting.html",
    "get-started/apply-to-your-data.html",
]
JS = """() => {
  const doc = document.documentElement;
  const tables = [...document.querySelectorAll('article table')];
  const wide = tables.filter(t => {
    const box = t.closest('.table-wrapper') || t.parentElement;
    return t.scrollWidth > box.clientWidth + 1;
  }).length;
  const imgs = [...document.querySelectorAll('article img')];
  const broken = imgs.filter(i => !(i.complete && i.naturalWidth > 0)).length;
  return {
    page_overflow_px: Math.max(0, doc.scrollWidth - doc.clientWidth),
    tables: tables.length, tables_scrolling: wide,
    images: imgs.length, broken_images: broken,
    beta_banner: /Beta Documentation/.test(document.body.innerText),
    math_errors: document.querySelectorAll('mjx-merror').length,
  };
}"""
results = []
with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    for width in (390, 1440):
        for scheme in ("light", "dark"):
            ctx = browser.new_context(viewport={"width": width, "height": 900}, color_scheme=scheme)
            page = ctx.new_page()
            for rel in PAGES:
                page.goto((BUILD / rel).as_uri(), wait_until="load")
                page.wait_for_timeout(400)
                r = page.evaluate(JS)
                r.update(page=rel, width=width, scheme=scheme)
                results.append(r)
            ctx.close()
    browser.close()
OUT.write_text(json.dumps(results, indent=1), encoding="utf-8")
bad = [r for r in results if r["page_overflow_px"] or r["broken_images"] or r["math_errors"]]
scroll = [(r["page"], r["width"], r["tables_scrolling"]) for r in results if r["tables_scrolling"] and r["scheme"] == "light"]
print("views", len(results), "| views with page overflow/broken images/math errors:", len(bad))
for r in bad:
    print("  BAD", r)
print("scrolling tables (light only):", scroll)
print("beta banner on all views:", all(r["beta_banner"] for r in results))
