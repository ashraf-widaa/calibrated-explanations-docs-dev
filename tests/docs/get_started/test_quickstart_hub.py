"""Get Started hub (formerly Quick Start; WP-1, PO decisions D-16 to D-21, revised 2026-11-18).

The hub stays code-free and links to the browser Quick Start and Python
learning journey. The code-free "CE by example" page quotes numbers produced
by the Python walkthrough.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs"
GET_STARTED = DOCS / "get-started"
INDEX = GET_STARTED / "index.md"

QUICK_START_TOCTREE = [
    ("What CE Is", "../what-is-ce"),
    ("Quick Start", "try-in-browser"),
    ("Your First CE Explanation in Python", "first-explanation-python"),
    ("Installation", "installation"),
    ("Read Your First Explanation", "../foundations/how-to/interpret_explanations"),
    ("Apply CE to Your Own Data", "apply-to-your-data"),
    ("Coming from SHAP or LIME", "coming-from-shap-lime"),
    ("CE by Example (No Code)", "ce-by-example"),
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


def test_get_started_toctree_puts_the_browser_quick_start_before_installation() -> None:
    assert _toctree(_text(INDEX)) == QUICK_START_TOCTREE


@pytest.mark.parametrize("page", ["index", *CODE_FREE_PAGES])
def test_quick_start_pages_have_no_code_or_derivations(page: str) -> None:
    text = _text(GET_STARTED / f"{page}.md")
    fences = [line for line in text.splitlines() if line.startswith("```") and line.strip() != "```"]
    code_fences = [line for line in fences if not ALLOWED_FENCES.match(line)]
    assert code_fences == [], f"{page}: code blocks {code_fences}"
    for marker in ("{code-block}", "{code-cell}", ".. code-block::", "{math}", "$$", "{eval-rst}"):
        assert marker not in text, f"{page}: {marker}"


def test_next_steps_route_to_theory_browser_python_and_integration_and_one_glossary() -> None:
    text = _text(INDEX)
    section = text.split("## Next steps", 1)[1].split("```{toctree}", 1)[0]
    for target in (
        "../sections/understand-ce",
        "try-decision-lab",
        "qs-expert-lab",
        "../sections/in-practice",
        "../practitioner/index",
        "../sections/software-integration",
        "../sections/project-evolution",
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
