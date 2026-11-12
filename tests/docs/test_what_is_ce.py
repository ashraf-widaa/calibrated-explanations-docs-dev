"""Guards for the 'What CE is and what it adds' page (run 2, stage 02).

The page must explain CE's contribution without superiority claims, state the
non-guarantees, and keep the author-review marker on the disputed assumption wording.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "docs" / "what-is-ce.md"
SUPERIORITY = ("better than", "outperform", "superior", "more accurate than", "more stable")


def text() -> str:
    return " ".join(PAGE.read_text(encoding="utf-8").split())


def test_no_superiority_claims() -> None:
    lowered = text().lower()
    for phrase in SUPERIORITY:
        assert phrase not in lowered, phrase


def test_states_what_is_not_guaranteed() -> None:
    body = text()
    for phrase in (
        "A guarantee for any single individual case",
        "Guarantees after the data change",
        "Causal statements",
        "Formal per-feature guarantees for explanation ranges",
    ):
        assert phrase in body, phrase


def test_assumption_wording_is_marked_under_review() -> None:
    assert "under review by the CE authors" in text()


def test_page_is_reachable_from_sidebar_and_landing() -> None:
    index = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    landing = (ROOT / "docs" / "sections" / "what-and-why.md").read_text(encoding="utf-8")
    assert "What CE Is <what-is-ce>" in index
    assert ":link: ../what-is-ce" in landing
