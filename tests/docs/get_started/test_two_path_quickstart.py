"""Guards for the two-path Quick Start (browser or local Python), 2026-11-19.

The Quick Start stays a short first experience: one conceptual figure, task and path
cards in HTML, real dated application screenshots for Path A, and no Python code. The
complete executable tutorial lives on ``first-explanation-python.md`` (Path B), which
keeps the anchors of the former in-page steps.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[3] / "docs"
QS = DOCS / "get-started" / "try-in-browser.md"
PY = DOCS / "get-started" / "first-explanation-python.md"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def test_quick_start_has_no_code_and_one_conceptual_figure() -> None:
    text = _text(QS)
    assert "```python" not in text
    figures = set(re.findall(r"_static/figures/([\w-]+?)(?:-narrow)?\.svg", text))
    assert figures == {"ce-adds-to-workflow"}, figures
    assert "{figure}" not in text


def test_both_paths_are_offered_side_by_side_before_the_walkthroughs() -> None:
    text = _text(QS)
    path_a = text.index(":::{grid-item-card} Path A")
    path_b = text.index(":::{grid-item-card} Path B")
    assert abs(path_a - path_b) < 1200, "the two path cards share one grid"
    assert path_b < text.index("(qs-path-a)=")
    assert ":link: first-explanation-python" in text


def test_path_a_has_separate_expert_hub_and_decision_lab_routes() -> None:
    text = _text(QS)
    expert = text.split("(qs-expert-lab)=", 1)[1].split("(try-decision-lab)=", 1)[0]
    lab = text.split("(try-decision-lab)=", 1)[1].split("(qs-python)=", 1)[0]
    assert "https://calibrated-explanations-demo.ju.se/expert" in expert
    assert "https://games.grejna.ai/learn/explanations-alternatives" in lab
    assert "https://games.grejna.ai/games/precision-works" in lab
    assert "Calibrated Explanations Enterprise" in lab
    assert "P(Y > 58)" in lab and "P(Y ≤ t)" in lab
    assert "type **3**, not\n300000" in expert


@pytest.mark.parametrize(
    "anchor",
    [
        "try-ce-in-your-browser",
        "quick-start-try-ce-in-your-browser",
        "qs-predictive-task",
        "ce-in-four-steps-train-calibrate-explain-interpret",
        "qs-worked-cases",
        "expert-hub-one-classification-and-one-regression-example-side-by-side",
        "decision-lab-decide-then-reconsider",
        "run-ce-locally",
        "try-step-1",
        "try-step-2",
        "try-step-3",
        "try-step-4",
        "try-step-5",
        "try-step-6",
    ],
)
def test_former_anchors_still_resolve_on_the_quick_start(anchor: str) -> None:
    assert f'id="{anchor}"' in _text(QS)


@pytest.mark.parametrize(
    "label",
    [
        "qs-workflow",
        "qs-task-mode-capability",
        "qs-expert-lab",
        "try-decision-lab",
        "qs-python",
        "qs-uncertainty",
        "qs-checkpoint",
    ],
)
def test_former_labels_still_exist_on_the_quick_start(label: str) -> None:
    assert f"({label})=" in _text(QS)


def test_screenshots_are_real_files_with_alt_text_and_a_capture_date() -> None:
    text = _text(QS)
    images = re.findall(
        r'<img src="\.\./_static/screenshots/([\w-]+\.png)"[^>]*alt="([^"]+)"', text
    )
    assert len(images) >= 6
    for name, alt in images:
        assert (DOCS / "_static" / "screenshots" / name).is_file(), name
        assert len(alt) > 60, name
    assert text.count('class="ce-shot-date"') == len(images)


def test_python_page_keeps_the_former_step_labels_and_installation() -> None:
    text = _text(PY)
    for n in range(1, 7):
        assert f"(try-step-{n})=" in text
    assert 'python -m pip install "calibrated-explanations[viz]"' in text
    assert "python -m venv .venv" in text
    steps = re.findall(r"^## Step (\d+)\.", text, flags=re.MULTILINE)
    assert [int(s) for s in steps] == list(range(1, 14))


def test_start_here_navigation_opens_the_page_and_links_both_paths() -> None:
    text = _text(QS)
    nav = text.index('<nav class="ce-start-here" aria-label="Start here">')
    assert nav < text.index("(qs-workflow)=")
    line = text[nav : text.index("</nav>", nav)]
    assert 'href="#qs-path-a">Explore CE in your browser</a>' in line
    assert 'href="#qs-python">Install CE locally</a>' in line
