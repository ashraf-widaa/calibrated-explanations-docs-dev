"""Structural tests for the Beta homepage (``docs/index.md``).

They pin the homepage of the five-section redesign: the agreed one-sentence
definition followed directly by a single Quick Start action, the four
documentation cards (each with its own question), the STD-004 semantics
pointer, four Project & Resources links (Project, Contribute, Glossary,
GitHub), a separate Commercial Services section, and the footer metadata
(Beta marker on Beta builds only). The Beta notice itself is the site-wide
announcement set in ``conf.py``.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INDEX = ROOT / "docs" / "index.md"
CSS = ROOT / "docs" / "_static" / "ce-home.css"
CONF = ROOT / "docs" / "conf.py"

DEFINITION = (
    "Calibrated Explanations (CE) is an open-source Python library that provides\n"
    "uncertainty-aware explanations of individual predictions from supervised\n"
    "machine-learning models."
)
LEARN = "Learn Calibrated Explanations"
CARDS = [
    ("sections/understand-ce.html#ce-what-why", "CE: What &amp; Why",
     "What problem does CE address, and when is it useful?"),
    ("sections/understand-ce.html#how-ce-works", "How CE Works",
     "How does the workflow produce calibrated outputs and explanations, and what assumptions matter?"),
    ("sections/in-practice.html", "CE in Practice",
     "Where can I follow an example, try CE in my browser, or use it in Python?"),
    ("sections/software-integration.html", "CE Software Architecture &amp; Integration",
     "How can I integrate CE into an application or understand and extend its codebase?"),
]
RESOURCES = [
    ("sections/project-evolution.html", "Project"),
    ("contributor/index.html", "Contribute"),
    ("glossary/index.html", "Glossary"),
    ("https://github.com/Moffran/calibrated_explanations", "GitHub Repository"),
]
GREJNA = "https://grejna.ai/#kontakt"


def text() -> str:
    return INDEX.read_text(encoding="utf-8").replace("\r\n", "\n")


def section(name: str) -> str:
    """Return the page text from ``## name`` up to the next level-2 heading."""
    body = text().split(f"\n## {name}\n", 1)[1]
    return re.split(r"\n## ", body, maxsplit=1)[0]


def hrefs(fragment: str, css_class: str) -> list[str]:
    return re.findall(rf'<a class="{css_class}[^"]*" href="([^"]+)"', fragment)


def test_beta_notice_links_to_the_official_documentation() -> None:
    conf = CONF.read_text(encoding="utf-8")
    assert "<strong>Beta Documentation</strong>" in conf
    assert '<a href="https://calibrated-explanations.readthedocs.io/">' in conf


def test_definition_is_followed_directly_by_one_quick_start_action() -> None:
    page = text()
    hero = page.split(f"\n## {LEARN}\n", 1)[0]
    assert page.startswith("# Calibrated Explanations [(CE)]{.ce-accent}")
    assert DEFINITION in hero
    assert hero.count("{button-ref}") == 1
    after_definition = hero.split(DEFINITION, 1)[1]
    assert after_definition.lstrip().startswith(":::{container} ce-hero-actions")
    assert (
        "```{button-ref} get-started/try-in-browser\n:ref-type: doc\n:color: primary\n\n"
        "Quick Start\n```" in hero
    )
    assert "learn the CE workflow and read your first explanation" in hero
    assert "{doc}`Get started <get-started/index>`" in hero


def test_four_documentation_cards_each_answer_their_own_question() -> None:
    learn = section(LEARN)
    assert hrefs(learn, "ce-section-card") == [href for href, _, _ in CARDS]
    for _, title, question in CARDS:
        assert f'<span class="ce-section-title">{title}</span>' in learn
        assert f'<span class="ce-section-desc">{question}</span>' in learn


def test_semantics_pointer_sits_below_the_cards() -> None:
    """STD-004 §5.2: Tier 1 pages carry a short, mode-specific semantics pointer."""
    learn = section(LEARN)
    pointer = "Guarantees are mode-specific. See {doc}`Calibrated interval semantics"
    assert pointer in learn
    assert learn.index("</nav>") < learn.index(pointer)
    assert text().count("calibrated_interval_semantics>`") == 1


def test_project_and_resources_links_project_contribute_glossary_and_github() -> None:
    resources = section("Project & Resources")
    assert hrefs(resources, "ce-foot-item") == [href for href, _ in RESOURCES]
    for _, title in RESOURCES:
        assert f'<span class="ce-foot-title">{title}</span>' in resources
    assert GREJNA not in resources


def test_homepage_has_three_parts_and_commercial_services_comes_last() -> None:
    page = text()
    assert re.findall(r"^## (.+)$", page, flags=re.MULTILINE) == [
        LEARN,
        "Project & Resources",
        "Commercial Services",
    ]
    commercial = section("Commercial Services")
    assert hrefs(commercial, "ce-foot-item") == [GREJNA]
    assert (
        "For customized CE solutions and commercial support, separate from the "
        "open-source library and its license." in commercial
    )


def test_footer_metadata_keeps_beta_marker_without_learning_tiers() -> None:
    """The Beta marker remains; audience metadata is not reader-facing."""
    page = text().rstrip()
    assert page.endswith(":::")
    meta = page.rsplit(":::{container} ce-meta", 1)[1]
    assert "```{only} ce_beta\nCE Beta Documentation\n```" in meta
    assert "Entry-point tier:" not in page


def test_homepage_has_no_audit_wording_or_undefined_icons() -> None:
    page = text()
    for phrase in ("unverified", "Interim", "need reconciliation", "Upgrading?"):
        assert phrase not in page
    used = set(re.findall(r"var\((--ce-i-[a-z]+)\)", page))
    defined = set(re.findall(r"(--ce-i-[a-z]+):", CSS.read_text(encoding="utf-8")))
    assert used <= defined, f"undefined icon tokens: {sorted(used - defined)}"
