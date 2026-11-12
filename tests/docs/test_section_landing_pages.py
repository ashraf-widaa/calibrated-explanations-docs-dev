"""Guards for the section landing pages behind the homepage cards.

Public landing pages must describe their destinations to readers: no internal
audit wording, and the CE in Practice resources point to verified destinations.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = ROOT / "docs" / "sections"
AUDIT_WORDING = ("unverified", "Interim", "need reconciliation", "not necessarily benchmarks")


# Widened stage by stage in the autonomous run; stage 10 switches to every page.
CLEANED = ["how-ce-works.md", "in-practice.md", "what-and-why.md"]


@pytest.mark.parametrize("page", CLEANED)
def test_landing_pages_have_no_audit_wording(page: str) -> None:
    text = (SECTIONS / page).read_text(encoding="utf-8")
    for phrase in AUDIT_WORDING:
        assert phrase not in text, f"{page}: {phrase!r}"


def test_in_practice_cards_point_to_verified_destinations() -> None:
    text = (SECTIONS / "in-practice.md").read_text(encoding="utf-8")
    links = re.findall(r"^:link: (\S+)$", text, flags=re.MULTILINE)
    assert links == [
        "https://calibrated-explanations-demo.ju.se/",
        "https://calibrated-explanations-demo.ju.se/expert",
        "https://games.grejna.ai/",
        "../foundations/how-to/integrate_with_pipelines",
        "https://github.com/Moffran/calibrated_explanations/tree/main/notebooks",
        "../tasks/index",
        "../practitioner/playbooks/index",
        "../practitioner/index",
        "../compare",
    ]
    assert "Decision Labs" not in text
    assert "not real-world guarantees" in text
