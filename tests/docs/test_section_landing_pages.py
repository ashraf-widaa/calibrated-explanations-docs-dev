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
    # 2026-11-19 redesign: Quick Start, Decision Lab, Expert Lab, Practitioner Hub, in order;
    # the Quick Start card leads to the same canonical page as Get started.
    assert links == [
        "../get-started/try-in-browser",
        "try-decision-lab",
        "qs-expert-lab",
        "../practitioner/index",
    ]
    assert re.findall(r"^:::\{grid-item-card\} (.+)$", text, flags=re.MULTILINE) == [
        "1. Quick Start", "2. Decision Lab", "3. Expert Hub", "4. Practitioner Hub",
    ]
    assert "Expert Hub" in text, "the demo's own label is named once"
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


def test_v1_stability_statement_is_restored_as_version_specific() -> None:
    """Batch 2: the official 1.0.0 stable-API notice returns, scoped to its release line."""
    text = " ".join((SECTIONS / "software-overview-versions.md").read_text(encoding="utf-8").split())
    assert "stable as of `1.0.0`" in text
    assert "historical, version-specific statement about the 1.0.x release line" in text
    assert "does not establish that development revisions" in text
    assert "../upgrade/v1.0.0-upgrade-checklist" in text
    assert "../schema_v1" in text


def test_compare_page_has_one_descriptive_label() -> None:
    index = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    practice = (SECTIONS / "in-practice.md").read_text(encoding="utf-8")
    what = (SECTIONS / "understand-ce.md").read_text(encoding="utf-8")
    assert "Comparison with Other Methods <../compare>" in what
    assert "The Explainability Gap" not in index + what
    assert "{doc}`Comparison with other methods <../compare>`" in practice


def test_project_landing_routes_to_readme_and_feedback() -> None:
    text = (SECTIONS / "project-evolution.md").read_text(encoding="utf-8")
    assert "No dedicated page yet" not in text
    assert "(https://github.com/Moffran/calibrated_explanations#readme)" in text
    assert "(https://github.com/Moffran/calibrated_explanations/issues)" in text
    # Project order (2026-11-19 redesign) ends with the license and commercial services.
    headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    assert headings == [
        "Research and publications", "How to cite CE", "Roadmap",
        "Governance and support", "License", "Commercial services",
    ]
    assert "https://grejna.ai/#kontakt" in text
    assert "https://github.com/ashraf-widaa/calibrated-explanations-docs-dev/issues" in text


LANDING = ["understand-ce", "in-practice", "software-integration", "project-evolution"]


@pytest.mark.parametrize("name", LANDING)
def test_landing_pages_are_sidebar_overviews_not_orphans(name: str) -> None:
    """Each homepage card's landing page is a root sidebar entry that parents its own pages."""
    index = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    root = re.search(r"```\{toctree\}\n(.*?)```", index, re.DOTALL).group(1)
    assert re.search(rf"^[^\n<]+ <sections/{name}>$", root, re.MULTILINE), name
    assert "```{toctree}" in (SECTIONS / f"{name}.md").read_text(encoding="utf-8"), name
    page = (SECTIONS / f"{name}.md").read_text(encoding="utf-8")
    assert not page.startswith("---\norphan: true")
