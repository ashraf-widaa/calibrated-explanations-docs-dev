"""Check changed public pages without modifying their content or assets."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument("--base", default="http://127.0.0.1:8771/")
parser.add_argument("--out", default="reports/verification/docs-focused-20261116")
args = parser.parse_args()
out = Path(args.out)
out.mkdir(parents=True, exist_ok=True)
changed = subprocess.check_output(
    ["git", "diff", "--name-only", "481ee05b", "--", "docs"],
    text=True, encoding="utf-8",
).splitlines()
pages = sorted({p.removeprefix("docs/").removesuffix(".md") + ".html"
                for p in changed if p.endswith(".md")}
               | {"index.html", "get-started/index.html", "get-started/ce-by-example.html"})
measure = """() => {
 const article=document.querySelector('article')||document.querySelector('main');
 const images=[...article.querySelectorAll('img')];
 return {
  overflow_px:Math.max(0,document.documentElement.scrollWidth-innerWidth),
  broken_images:images.filter(i=>!(i.complete&&i.naturalWidth>0)).map(i=>i.currentSrc),
  missing_alt:images.filter(i=>!i.getAttribute('alt')).map(i=>i.src),
  math_errors:document.querySelectorAll('mjx-merror').length,
  unrendered_math:article.querySelectorAll('.math:not(:has(mjx-container))').length,
  rendered_math:article.querySelectorAll('mjx-container').length,
  beta_banner:/Beta Documentation/.test(document.querySelector('.announcement')?.innerText||''),
  background:getComputedStyle(document.body).backgroundColor
 };
}"""
rows = []
with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    for width in (390, 1440):
        for scheme in ("light", "dark"):
            context = browser.new_context(viewport={"width":width,"height":900}, color_scheme=scheme)
            page = context.new_page()
            for rel in pages:
                response = page.goto(args.base.rstrip("/")+"/"+rel, wait_until="load")
                page.evaluate("async () => { await document.fonts.ready; if(window.MathJax?.startup?.promise) await window.MathJax.startup.promise; }")
                page.wait_for_timeout(300)
                row = page.evaluate(measure)
                row.update(page=rel,width=width,scheme=scheme,status=response.status)
                rows.append(row)
                if rel in ("get-started/ml-foundations.html","compare.html",
                           "foundations/concepts/ce_workflow.html"):
                    if rel.endswith("ce_workflow.html"):
                        page.locator("#how-an-explanation-is-built").scroll_into_view_if_needed()
                    name=rel.replace("/","-").removesuffix(".html")
                    page.screenshot(path=str(out/f"layout-{name}-{width}-{scheme}.png"))
            context.close()
            (out/"layout.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
            print(f"{len(rows)} scenarios checked",flush=True)
    browser.close()
bad=[r for r in rows if r["status"]!=200 or r["overflow_px"] or r["broken_images"]
     or r["missing_alt"] or r["math_errors"] or r["unrendered_math"] or not r["beta_banner"]]
print(json.dumps({"pages":len(pages),"scenarios":len(rows),"issues":bad}),flush=True)
raise SystemExit(bool(bad))
