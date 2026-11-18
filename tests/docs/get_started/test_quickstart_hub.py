"""Get Started hub (formerly Quick Start; WP-1, PO decisions D-16 to D-21, revised 2026-11-18).

The hub page itself stays code-free (no code blocks, no derivations). Since the
2026-11-18 DevEx review its sidebar holds the five learning-journey steps, including
the executable Quickstart and Apply pages; the other tutorials keep living under
Python Tutorials. The hub links all other homepage entry points, and the code-free
"CE by example" page only quotes numbers produced by the Python walkthrough.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs"
GET_STARTED = DOCS / "get-started"
INDEX = GET_STARTED / "index.md"

# 2026-11-18 DevEx review: the Get Started sidebar is the learning journey in order,
# followed by the no-code example and the SHAP/LIME mapping.
QUICK_START_TOCTREE = [
    ("Installation", "installation"),
    ("Quickstart", "quickstart"),
    ("Read Your First Explanation", "../foundations/how-to/interpret_explanations"),
    ("Apply CE to Your Own Data", "apply-to-your-data"),
    ("Evaluate CE", "../practitioner/evaluate_ce"),
    ("CE by Example (No Code)", "ce-by-example"),
    ("Coming from SHAP or LIME", "coming-from-shap-lime"),
]
CODE_FREE_PAGES = ["ml-foundations", "why-ce", "ce-by-example", "ce-tasks-and-modes", "apply-overview"]
EXECUTABLE_PAGES = [
    "quickstart_walkthrough",
    "quickstart_classification",
    "quickstart_regression",
    "quickstart_guarded",
]
# MyST directives that are not code: figures, raw HTML figures, toctrees, admonitions, diagrams.
ALLOWED_FENCES = re.compile(r"^```\{(figure|raw|toctree|admonition|mermaid)\}")


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _toctree(text: str) -> list[tuple[str, str]]:
    block = re.search(r"```\{toctree\}\n(.*?)```", text, re.DOTALL).group(1)
    return re.findall(r"^(.+?) <([^>]+)>$", block, re.MULTILINE)


def test_quick_start_toctree_is_paths_a_b_c_only() -> None:
    assert _toctree(_text(INDEX)) == QUICK_START_TOCTREE


@pytest.mark.parametrize("page", ["index", *CODE_FREE_PAGES])
def test_quick_start_pages_have_no_code_or_derivations(page: str) -> None:
    text = _text(GET_STARTED / f"{page}.md")
    fences = [line for line in text.splitlines() if line.startswith("```") and line.strip() != "```"]
    code_fences = [line for line in fences if not ALLOWED_FENCES.match(line)]
    assert code_fences == [], f"{page}: code blocks {code_fences}"
    for marker in ("{code-block}", "{code-cell}", ".. code-block::", "{math}", "$$", "{eval-rst}"):
        assert marker not in text, f"{page}: {marker}"


def test_landing_links_the_six_other_entry_points_and_one_glossary() -> None:
    text = _text(INDEX)
    section = text.split("## Where should I go next?", 1)[1].split("```{toctree}", 1)[0]
    for target in (
        "../sections/what-and-why",
        "../sections/how-ce-works",
        "../sections/in-practice",
        "../sections/software-integration",
        "../sections/project-evolution",
        "https://grejna.ai/#kontakt",
    ):
        assert target in section, target
    assert len(re.findall(r"glossary/(index|science|software)", text)) == 1


@pytest.mark.parametrize("slug", EXECUTABLE_PAGES)
def test_executable_pages_keep_their_url_and_move_to_python_tutorials(slug: str) -> None:
    assert (GET_STARTED / f"{slug}.md").is_file()
    hub = _toctree(_text(DOCS / "tutorials" / "index.md"))
    assert f"../get-started/{slug}" in [target for _, target in hub]


def test_tutorials_hub_and_quick_api_have_new_sidebar_homes() -> None:
    assert "Python Tutorials <../tutorials/index>" in _text(DOCS / "sections" / "in-practice.md")
    software = _toctree(_text(DOCS / "sections" / "software-integration.md"))
    assert ("Quick API", "../get-started/quick_api") in software
    assert (GET_STARTED / "quick_api.md").is_file()


def test_ce_by_example_numbers_come_from_the_walkthrough() -> None:
    example = _text(GET_STARTED / "ce-by-example.md").replace("−", "-")
    walkthrough = _text(GET_STARTED / "quickstart_walkthrough.md")
    numbers = set(re.findall(r"[+-]?\d+\.\d{3,4}", example))
    assert numbers, "no numbers found"
    missing = sorted(n for n in numbers if n not in walkthrough)
    assert missing == [], f"numbers not produced by the walkthrough: {missing}"


def test_walkthrough_extra_sections_do_not_collide_with_paths() -> None:
    for path in (GET_STARTED / "quickstart_walkthrough.md", ROOT / "scripts" / "docs" / "build_quickstart_walkthrough.py"):
        text = _text(path)
        assert not re.search(r"## Optional [ABC]\.", text), path.name
        assert "## Extra 1." in text and "## Extra 2." in text and "## Extra 3." in text


@pytest.mark.parametrize("page", ["ml-foundations", "why-ce", "ce-by-example", "ce-tasks-and-modes", "apply-overview"])
def test_quick_start_pages_keep_contextual_links_without_route_instructions(page: str) -> None:
    text = _text(GET_STARTED / f"{page}.md")
    links = re.findall(r"\{(?:doc|ref)\}`[^`]+`|\[[^\]]+\]\([^)]+\)", text)
    assert len(links) >= 2, page
    assert "**Next:**" not in text and "**Go deeper:**" not in text, page
