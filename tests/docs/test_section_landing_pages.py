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


@pytest.mark.parametrize("page", sorted(p.name for p in SECTIONS.glob("*.md")))
def test_landing_pages_have_no_audit_wording(page: str) -> None:
    text = (SECTIONS / page).read_text(encoding="utf-8")
    for phrase in AUDIT_WORDING:
        assert phrase not in text, f"{page}: {phrase!r}"


def test_in_practice_cards_point_to_verified_destinations() -> None:
    text = (SECTIONS / "in-practice.md").read_text(encoding="utf-8")
    links = re.findall(r"^:link: (\S+)$", text, flags=re.MULTILINE)
    assert links == [
        "../tutorials/index",
        "https://calibrated-explanations-demo.ju.se/",
        "https://calibrated-explanations-demo.ju.se/expert",
        "https://games.grejna.ai/",
        "../foundations/how-to/integrate_with_pipelines",
        "https://github.com/Moffran/calibrated_explanations/tree/main/notebooks",
        "../practitioner/evaluate_ce",
        "../tasks/index",
        "../practitioner/index",
        "../compare",
    ]
    assert "Decision Labs" not in text
    assert "not real-world guarantees" in text


def test_api_overview_links_rendered_signatures_instead_of_broken_autodoc() -> None:
    """Run stage 09: the six inline autodoc blocks never rendered (single-backtick fence).

    Each class section now links its generated ``_autosummary`` page instead.
    """
    api = (ROOT / "docs" / "api" / "calibrated_explainer.md").read_text(encoding="utf-8")
    assert "`{eval-rst}\n.. autoclass" not in api
    assert ".. autoclass::" not in api
    targets = re.findall(r"API reference <\.\./_autosummary/([^>]+)>", api)
    assert len(targets) == 6
    for target in targets:
        assert (ROOT / "docs" / "_autosummary" / f"{target}.rst").is_file(), target


def test_software_versions_page_states_release_and_python() -> None:
    text = (SECTIONS / "software-overview-versions.md").read_text(encoding="utf-8")
    assert "**Latest release:** 1.0.2" in text
    assert "**Python:** 3.10 or later" in text
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'requires-python = ">=3.10"' in pyproject


def test_project_landing_routes_to_readme_and_feedback() -> None:
    text = (SECTIONS / "project-evolution.md").read_text(encoding="utf-8")
    assert "No dedicated page yet" not in text
    assert ":link: https://github.com/Moffran/calibrated_explanations#readme" in text
    assert ":link: https://github.com/Moffran/calibrated_explanations/issues" in text
    assert "https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/issues" in text


LANDING = ["what-and-why", "how-ce-works", "in-practice", "software-integration", "project-evolution"]


@pytest.mark.parametrize("name", LANDING)
def test_landing_pages_are_sidebar_overviews_not_orphans(name: str) -> None:
    """Run stage 11: each homepage card's landing page is the first entry of its sidebar group."""
    index = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    assert re.search(rf':caption: "[^"]+"\n\nOverview <sections/{name}>\n', index), name
    page = (SECTIONS / f"{name}.md").read_text(encoding="utf-8")
    assert not page.startswith("---\norphan: true")
