"""Structural tests for the L07 Beta homepage (``docs/index.md``).

They pin the approved information architecture: hero with one Quick Start action, four
documentation cards, the STD-004 semantics pointer below the cards, four Project &
Resources links, a separate Commercial Services section, and the footer metadata
(Beta marker on Beta builds only, STD-004 tier label last).
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INDEX = ROOT / "docs" / "index.md"
CSS = ROOT / "docs" / "_static" / "ce-home.css"

CARDS = [
    ("sections/what-and-why.html", "Why uncertainty-aware explanations matter and what CE adds."),
    ("sections/how-ce-works.html", "The theory, methods and key concepts behind CE."),
    ("sections/in-practice.html", "Interactive demos, task guides and practical playbooks."),
    (
        "sections/software-integration.html",
        "Installation, Python API and integration with models and pipelines.",
    ),
]
RESOURCES = [
    ("sections/project-evolution.html", "Research, publications, roadmap and community."),
    ("glossary/index.html", "Scientific and software terms, A–Z."),
    ("https://github.com/Moffran/calibrated_explanations", "Source code, issues and contributions."),
    (
        "https://github.com/Moffran/calibrated_explanations/blob/main/LICENSE",
        "Open-source license and usage terms.",
    ),
]
GREJNA = "https://grejna.ai/#kontakt"


def text() -> str:
    return INDEX.read_text(encoding="utf-8")


def section(name: str) -> str:
    """Return the page text from ``## name`` up to the next level-2 heading."""
    body = text().split(f"\n## {name}\n", 1)[1]
    return re.split(r"\n## ", body, maxsplit=1)[0]


def hrefs(fragment: str, css_class: str) -> list[str]:
    return re.findall(rf'<a class="{css_class}[^"]*" href="([^"]+)"', fragment)


def test_hero_keeps_identity_message_and_one_primary_action() -> None:
    page = text()
    hero = page.split("\n## Documentation\n", 1)[0]
    assert page.startswith("# Calibrated Explanations [(CE)]{.ce-accent}")
    assert (
        "Understand machine-learning predictions through calibrated, "
        "uncertainty-aware explanations." in hero
    )
    assert hero.count("{button-ref}") == 1
    assert "```{button-ref} get-started/index" in hero
    assert "New to CE? Learn the essentials and try your first example." in hero


def test_four_documentation_cards_in_order_with_approved_descriptions() -> None:
    docs = section("Documentation")
    assert "Choose the section that matches your goal." in docs
    assert hrefs(docs, "ce-section-card") == [href for href, _ in CARDS]
    for _, description in CARDS:
        assert f'<span class="ce-section-desc">{description}</span>' in docs


def test_semantics_pointer_sits_below_the_cards() -> None:
    """STD-004 §5.2: Tier 1 pages carry a short, mode-specific semantics pointer."""
    docs = section("Documentation")
    pointer = "Guarantees are mode-specific. See {doc}`Calibrated interval semantics"
    assert pointer in docs
    assert docs.index("</nav>") < docs.index(pointer)
    assert text().count("calibrated_interval_semantics>`") == 1


def test_project_and_resources_has_exactly_four_links() -> None:
    resources = section("Project & Resources")
    assert "Explore the research, terminology and open-source project." in resources
    assert hrefs(resources, "ce-foot-item") == [href for href, _ in RESOURCES]
    # Word joiners (&#8288;) around the dash keep "A–Z" on one line; layout only.
    plain = resources.replace("&#8288;", "")
    for _, description in RESOURCES:
        assert f'<span class="ce-foot-sub">{description}</span>' in plain
    assert GREJNA not in resources


def test_commercial_services_is_a_separate_section_after_resources() -> None:
    page = text()
    assert page.index("\n## Project & Resources\n") < page.index("\n## Commercial Services\n")
    commercial = section("Commercial Services")
    assert hrefs(commercial, "ce-foot-item") == [GREJNA]
    assert (
        "For customized CE solutions and commercial support, separate from the "
        "open-source library and its license." in commercial
    )


def test_footer_metadata_beta_marker_and_tier_label_last() -> None:
    """STD-004 §4.5: the tier label stays at the bottom of the page."""
    page = text().rstrip()
    assert page.endswith("Entry-point tier: Tier 1.\n\n:::")
    meta = page.rsplit(":::{container} ce-meta", 1)[1]
    assert "```{only} ce_beta\nCE Beta Documentation\n```" in meta
    assert page.count("Entry-point tier:") == 1


def test_homepage_has_no_audit_wording_or_undefined_icons() -> None:
    page = text()
    for phrase in ("unverified", "Interim", "need reconciliation", "Upgrading?"):
        assert phrase not in page
    used = set(re.findall(r"var\((--ce-i-[a-z]+)\)", page))
    defined = set(re.findall(r"(--ce-i-[a-z]+):", CSS.read_text(encoding="utf-8")))
    assert used <= defined, f"undefined icon tokens: {sorted(used - defined)}"
