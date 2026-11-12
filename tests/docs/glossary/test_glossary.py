"""Structural tests for the unified CE glossary (``docs/glossary/``).

The glossary rules come from the approved L06 glossary architecture (decisions G-1 to G-5):

* one hub with two category pages and a static combined A-Z index (T-1);
* one canonical definition per term: no headword or alias on both pages (T-2);
* exactly one onward link per entry, into the allowed target set for its category (T-3);
* short entries: at most 60 words, or 10 words for parameter-reference pointers (T-4);
* ``parameter-reference.md`` keeps ownership of its five parameters (T-5);
* the glossary is reachable from the homepage sidebar and footer, and the old
  Terminology change note keeps its page under Migration.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs"
GLOSSARY = DOCS / "glossary"
HUB = GLOSSARY / "index.md"
CATEGORY_PAGES = {"S": GLOSSARY / "science.md", "T": GLOSSARY / "software.md"}

GLOSSARY_BLOCK = re.compile(r"```\{glossary\}\n(.*?)```", re.DOTALL)
LINK_LINE = re.compile(r"^\*\*(Learn more|API|Defined in):\*\* \{doc\}`(?:[^`<]*<)?([^`>]+)>?`")
DOC_ROLE = re.compile(r"\{doc\}`(?:[^`<]*<)?([^`>]+)>?`")
AZ_TERM = re.compile(r"^- \{term\}`([^`]+)` · \*\*([ST])\*\*$")
AZ_ALIAS = re.compile(r"^- (.+?) · see \{term\}`([^`]+)`$")

PARAMETER_REFERENCE_NAMES = {
    "threshold",
    "low_high_percentiles",
    "confidence_level",
    "confidence",
    "significance",
}
POINTER_MAX_WORDS = 10
DEFINITION_MAX_WORDS = 60

# Allowed onward-link targets, resolved relative to docs/ (approved proposal §3.5).
SCIENCE_TARGETS = {
    "get-started/ml-foundations",
    "get-started/ce-tasks-and-modes",
    "foundations/index",
    "foundations/concepts/calibrated_interval_semantics",
    "foundations/concepts/calibration_methods",
    "foundations/how-to/interpret_explanations",
    "foundations/concepts/alternatives",
    "foundations/concepts/guarded_explanations",
    "foundations/concepts/probabilistic_regression",
    "foundations/how-to/conditional_calibration",
    "compare",
}
SOFTWARE_TARGET_PREFIXES = (
    "get-started/installation",
    "foundations/concepts/architecture",
    "foundations/concepts/parameter-reference",
    "foundations/concepts/explanation_structures",
    "foundations/concepts/error_handling",
    "foundations/concepts/telemetry",
    "foundations/how-to/",
    "foundations/reference/api",
    "plugins",
    "api/",
    "schema_v1",
)


@dataclass(frozen=True)
class Entry:
    category: str
    names: tuple[str, ...]
    body: tuple[str, ...]

    @property
    def headword(self) -> str:
        return self.names[0]


def _resolve(target: str) -> str:
    """Resolve a {doc} target written on a glossary page to a docs-relative path."""
    return (Path("glossary") / target).as_posix().replace("glossary/../", "")


def _entries(category: str) -> list[Entry]:
    text = CATEGORY_PAGES[category].read_text(encoding="utf-8")
    entries: list[Entry] = []
    for block in GLOSSARY_BLOCK.findall(text):
        names: list[str] = []
        body: list[str] = []
        for line in block.splitlines():
            if not line.strip() or line.startswith(":"):
                continue
            if line.startswith((" ", "\t")):
                body.append(line.strip())
            else:
                if body:
                    entries.append(Entry(category, tuple(names), tuple(body)))
                    names, body = [], []
                names.append(line.strip())
        if names:
            entries.append(Entry(category, tuple(names), tuple(body)))
    return entries


def all_entries() -> list[Entry]:
    return _entries("S") + _entries("T")


def _hub_lines() -> list[str]:
    return [line.strip() for line in HUB.read_text(encoding="utf-8").splitlines()]


def test_category_pages_have_entries() -> None:
    for category in CATEGORY_PAGES:
        assert _entries(category), f"no glossary entries found for category {category}"


def test_az_index_lists_every_headword_exactly_once_with_its_category() -> None:
    """T-1: the static combined A-Z index matches both category pages."""
    listed = [m.groups() for m in map(AZ_TERM.match, _hub_lines()) if m]
    expected = sorted((e.headword, e.category) for e in all_entries())
    assert sorted(listed) == expected


def test_az_index_aliases_point_to_their_headword() -> None:
    expected = sorted(
        (alias, e.headword) for e in all_entries() for alias in e.names[1:]
    )
    listed = sorted(m.groups() for m in map(AZ_ALIAS.match, _hub_lines()) if m)
    assert listed == expected


def test_az_index_is_alphabetical() -> None:
    keys = []
    for line in _hub_lines():
        term = AZ_TERM.match(line)
        alias = AZ_ALIAS.match(line)
        if term or alias:
            keys.append((term or alias).group(1).casefold())
    assert keys == sorted(keys)


def test_no_term_is_defined_twice() -> None:
    """T-2: one canonical definition per term, across both category pages."""
    seen: dict[str, str] = {}
    for entry in all_entries():
        for name in entry.names:
            key = name.casefold()
            assert key not in seen, f"{name!r} defined in {seen[key]} and {entry.category}"
            seen[key] = entry.category


@pytest.mark.parametrize("entry", all_entries(), ids=lambda e: f"{e.category}:{e.headword}")
def test_entry_has_one_allowed_onward_link(entry: Entry) -> None:
    """T-3: exactly one Learn more / API / Defined in line, into the category's targets."""
    links = [m for m in map(LINK_LINE.match, entry.body) if m]
    assert len(links) == 1, f"{entry.headword}: expected one onward link, got {len(links)}"
    target = _resolve(links[0].group(2))
    assert (DOCS / f"{target}.md").is_file(), f"{entry.headword}: missing page {target}"
    if entry.category == "S":
        assert target in SCIENCE_TARGETS, f"{entry.headword}: {target} not a theory page"
    else:
        assert target.startswith(SOFTWARE_TARGET_PREFIXES), (
            f"{entry.headword}: {target} not a software or API page"
        )


@pytest.mark.parametrize("entry", all_entries(), ids=lambda e: f"{e.category}:{e.headword}")
def test_entry_is_concise(entry: Entry) -> None:
    """T-4: definitions stay short; teaching belongs on the linked page."""
    definition = " ".join(line for line in entry.body if not LINK_LINE.match(line))
    limit = (
        POINTER_MAX_WORDS
        if entry.headword in PARAMETER_REFERENCE_NAMES
        else DEFINITION_MAX_WORDS
    )
    assert len(definition.split()) <= limit, f"{entry.headword}: over {limit} words"


def test_parameter_reference_parameters_are_pointers_only() -> None:
    """T-5: parameter-reference.md stays the canonical owner of its five parameters."""
    for entry in all_entries():
        if PARAMETER_REFERENCE_NAMES & set(entry.names):
            assert entry.category == "T"
            links = [m for m in map(LINK_LINE.match, entry.body) if m]
            assert links and links[0].group(1) == "Defined in"
            assert _resolve(links[0].group(2)) == "foundations/concepts/parameter-reference"


def test_category_pages_link_to_each_other_and_the_hub() -> None:
    for page in CATEGORY_PAGES.values():
        targets = {_resolve(t) for t in DOC_ROLE.findall(page.read_text(encoding="utf-8"))}
        assert {"glossary/index", "glossary/science", "glossary/software"} - {
            "glossary/" + page.stem
        } <= targets


def test_hub_toctree_contains_both_categories() -> None:
    text = HUB.read_text(encoding="utf-8")
    toctree = re.search(r"```\{toctree\}\n(.*?)```", text, re.DOTALL)
    assert toctree is not None
    assert "<science>" in toctree.group(1)
    assert "<software>" in toctree.group(1)


def test_homepage_links_to_glossary_in_sidebar_and_footer() -> None:
    """G-2b: Resources sidebar entry plus a visible Project & Resources link."""
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    assert "Glossary <glossary/index>" in index
    foot = index.split("## Project & Resources", 1)[1].split("```", 1)[0]
    assert 'href="glossary/index.html"' in foot
    assert 'class="ce-section-card' not in foot
    assert index.count('class="ce-section-card') == 4, "no fifth documentation card"


def test_terminology_change_note_moved_to_migration() -> None:
    """G-5: the change note leaves the Resources sidebar but keeps its page."""
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    assert "<foundations/concepts/terminology>" not in index
    migration = (DOCS / "migration" / "index.md").read_text(encoding="utf-8")
    assert "../foundations/concepts/terminology>" in migration
    assert (DOCS / "foundations" / "concepts" / "terminology.md").is_file()


@pytest.mark.parametrize("page", [HUB, *CATEGORY_PAGES.values()], ids=lambda p: p.name)
def test_glossary_pages_carry_tier_footer(page: Path) -> None:
    assert page.read_text(encoding="utf-8").rstrip().endswith("Entry-point tier: Tier 3.")
