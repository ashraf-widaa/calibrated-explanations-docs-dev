"""The five-step Get started path stays continuous: each step says where it is and links onward.

Path (2026-11-19 redesign): What CE is -> Quick Start (browser, no installation) ->
Installation -> Read your first explanation -> Apply CE to your own data -> Next steps.
The Python quickstart, CE by example (no code) and the Python walkthrough are generated
or Practitioner Hub pages outside the numbered path; the generator owns their text.
"""

from __future__ import annotations

from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[2] / "docs"
JOURNEY = [
    ("what-is-ce.md", 1, "get-started/try-in-browser"),
    ("get-started/try-in-browser.md", 2, "<installation>"),
    ("get-started/installation.md", 3, "interpret_explanations"),
    ("foundations/how-to/interpret_explanations.md", 4, "get-started/apply-to-your-data"),
    ("get-started/apply-to-your-data.md", 5, "quick-start-next"),
]


@pytest.mark.parametrize(("page", "step", "next_target"), JOURNEY)
def test_each_step_states_its_position_and_links_onward(page: str, step: int, next_target: str) -> None:
    text = " ".join((DOCS / page).read_text(encoding="utf-8").split())
    assert f"step {step} of 5" in text, page
    assert next_target in text, (page, next_target)


def test_generator_owns_the_journey_text_of_generated_pages() -> None:
    generator = (DOCS.parent / "scripts" / "docs" / "build_quickstart_walkthrough.py").read_text(encoding="utf-8")
    assert "**Without code.**" in generator
    assert "**Python tutorial, in depth.**" in generator
    assert "Learning journey" not in generator
    for page in ("ce-by-example.md", "quickstart_walkthrough.md"):
        text = (DOCS / "get-started" / page).read_text(encoding="utf-8")
        assert "Learning journey" not in text, page
