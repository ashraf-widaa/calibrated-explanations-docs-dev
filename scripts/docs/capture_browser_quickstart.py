"""Capture the Expert Hub screenshots used by the browser Quick Start (manual tool).

The Quick Start (``docs/get-started/try-in-browser.md``) shows real, dated screenshots of
the online CE demo. This script re-creates the five Expert Hub screenshots by driving the
live application with Playwright, so they can be refreshed when the application changes.

It is **not** part of the Sphinx build or of the documentation test suite. Run it by hand:

    python -m pip install playwright pillow
    python -m playwright install chromium
    python scripts/docs/capture_browser_quickstart.py --out-dir _build/screenshots-new

Then compare the new images with ``docs/_static/screenshots/`` and copy the ones you
approve. The script never overwrites existing files unless ``--overwrite`` is given, and
it stops with a message naming the failed step when a label in the application changes.

What is deterministic. The Expert Hub's built-in demos (Diabetes, California Housing)
use a fixed split and model, so test row 0 gave identical numbers in repeated runs on
19 November 2026 (Diabetes P(Y=positive) = 0.7448 [0.7273, 0.7959]; Housing
Y = 0.5170 [0.3087, 0.7948]; P(Y <= 3) = 0.9986 [0.9986, 1.0000]). If they change, the
captions on the Quick Start must be checked.

Decision Lab screenshots are not automated: each Mission Control session and each
Precision Works recipe gives different numbers. Capture them by hand:

1. Open https://games.grejna.ai/learn/explanations-alternatives and select
   "Open guided exercise". Select "WHY?" and take a screenshot of the mission file,
   the assistant assessment and the WHY panel (``dl-mc-why.png``). Choose "GO" and take
   a screenshot of the outcome line and the next mission (``dl-mc-feedback.png``).
2. Open https://games.grejna.ai/games/precision-works and select "Enter factory".
   Choose the FORECAST order ("Where will hardness land?"), select "Assess recipe" and
   crop the Process Advisor panel (``dl-pw-forecast.png``). Repeat with the LIMIT order
   ("Will it reach the minimum?") for ``dl-pw-limit.png``.
3. Use a 1366 x 900 desktop window, update the capture date in the Quick Start captions,
   and recheck the callout positions in ``try-in-browser.md``.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EXPERT_HUB = "https://calibrated-explanations-demo.ju.se/expert"
VIEWPORT = {"width": 1366, "height": 900}
# Crop boxes (left, top, right, bottom) in pixels of the full-page capture at VIEWPORT.
SIDEBAR = 250
CROPS = {
    "eh-project.png": (SIDEBAR, 0, 1366, 720),
    "eh-factual.png": (SIDEBAR, 540, 1366, 2040),
    "eh-alternatives.png": (SIDEBAR, 540, 1366, 1690),
    "eh-interval.png": (SIDEBAR, 830, 1366, 1750),
    "eh-threshold.png": (SIDEBAR, 830, 1366, 1490),
}


class StepError(RuntimeError):
    """Raised when an expected label or control is not found in the application."""


def _step(name, action):
    try:
        action()
    except Exception as exc:  # noqa: BLE001 - report any Playwright failure by step name
        raise StepError(
            f"step '{name}' failed: the application UI may have changed ({exc})"
        ) from exc


def _dismiss_feedback(page):
    button = page.get_by_text("Not now", exact=True)
    if button.count():
        button.first.click()


def _open_project(page, dataset_regex, before_choice=None):
    _step("open Expert Hub", lambda: page.goto(EXPERT_HUB, wait_until="networkidle", timeout=60000))
    page.wait_for_timeout(2500)
    if before_choice is not None:
        page.screenshot(path=str(before_choice), full_page=True)
    _step(
        f"choose demo dataset {dataset_regex}",
        lambda: page.get_by_text(re.compile(dataset_regex)).first.click(timeout=15000),
    )
    page.wait_for_timeout(3000)


def _calibrate_and_explain(page, wait_ms):
    _step(
        "Next: Prepare & Calibrate",
        lambda: page.get_by_text("Next: Prepare & Calibrate", exact=True).first.click(
            timeout=15000
        ),
    )
    page.wait_for_timeout(2500)
    _step(
        "Prepare Random Forest + Calibrate",
        lambda: page.get_by_text("Prepare Random Forest + Calibrate", exact=True).first.click(
            timeout=15000
        ),
    )
    page.wait_for_timeout(wait_ms)
    _step(
        "Next: Explain",
        lambda: page.get_by_text("Next: Explain", exact=True).first.click(timeout=30000),
    )
    page.wait_for_timeout(5000)


def _select_row(page, row):
    _step(f"select test row {row}", lambda: page.locator("tbody tr").nth(row).click(timeout=15000))
    page.wait_for_timeout(15000)
    _dismiss_feedback(page)
    page.wait_for_timeout(8000)  # let the Plotly charts finish rendering


def capture(out_dir: Path, overwrite: bool) -> list[Path]:
    from PIL import Image
    from playwright.sync_api import sync_playwright

    out_dir.mkdir(parents=True, exist_ok=True)
    existing = [out_dir / name for name in CROPS if (out_dir / name).exists()]
    if existing and not overwrite:
        raise SystemExit(
            f"refusing to overwrite {len(existing)} existing file(s) in {out_dir}; "
            "use another --out-dir or pass --overwrite"
        )
    raw = out_dir / "raw"
    raw.mkdir(exist_ok=True)
    shots: dict[str, Path] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)

        shots["eh-project.png"] = raw / "project.png"
        _open_project(page, r"^Diabetes \(Binary", before_choice=shots["eh-project.png"])
        _calibrate_and_explain(page, wait_ms=15000)
        _select_row(page, 0)
        shots["eh-factual.png"] = raw / "factual.png"
        page.screenshot(path=str(shots["eh-factual.png"]), full_page=True)
        _step(
            "open Alternatives tab",
            lambda: page.get_by_text(re.compile(r"^Alternatives")).first.click(timeout=15000),
        )
        page.wait_for_timeout(15000)
        _dismiss_feedback(page)
        shots["eh-alternatives.png"] = raw / "alternatives.png"
        page.screenshot(path=str(shots["eh-alternatives.png"]), full_page=True)

        _open_project(page, r"^California Housing")
        _calibrate_and_explain(page, wait_ms=25000)
        _select_row(page, 0)
        shots["eh-interval.png"] = raw / "interval.png"
        page.screenshot(path=str(shots["eh-interval.png"]), full_page=True)
        _step(
            "switch on Use Threshold (probabilistic regression)",
            lambda: page.get_by_role("switch").nth(1).click(timeout=15000),
        )
        page.wait_for_timeout(2000)

        def _type_threshold():
            box = page.locator("input:visible").nth(0)
            box.fill("3", timeout=15000)  # 3 = $300,000; the target is in units of $100,000
            box.press("Tab")

        _step("type threshold 3", _type_threshold)
        page.wait_for_timeout(2000)
        _select_row(page, 0)
        shots["eh-threshold.png"] = raw / "threshold.png"
        page.screenshot(path=str(shots["eh-threshold.png"]), full_page=True)
        browser.close()

    written = []
    for name, source in shots.items():
        image = Image.open(source).convert("RGB")
        left, top, right, bottom = CROPS[name]
        image.crop((left, top, min(right, image.width), min(bottom, image.height))).save(
            out_dir / name, optimize=True
        )
        written.append(out_dir / name)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--out-dir",
        type=Path,
        required=True,
        help="directory for the new screenshots (never docs/_static/screenshots)",
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="replace existing files in --out-dir"
    )
    args = parser.parse_args(argv)
    if args.out_dir.resolve() == (
        Path(__file__).resolve().parents[2] / "docs" / "_static" / "screenshots"
    ):
        parser.error("write to a separate directory and copy approved images by hand")
    try:
        written = capture(args.out_dir, args.overwrite)
    except ImportError as exc:
        print(
            f"missing dependency: {exc}. Install with: python -m pip install playwright pillow "
            "&& python -m playwright install chromium",
            file=sys.stderr,
        )
        return 2
    except StepError as exc:
        print(f"capture stopped: {exc}", file=sys.stderr)
        return 1
    for path in written:
        print("wrote", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
