"""The Quick API page's minimal example must run as written and print what the page shows (WP-6)."""

from __future__ import annotations

import contextlib
import io
import re
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAGE = ROOT / "docs/get-started/quick_api.md"
EXAMPLE = re.compile(r"## A complete minimal example\n.*?```python\n(.*?)```\n\n```text\n(.*?)```", re.DOTALL)


def _page() -> str:
    return PAGE.read_text(encoding="utf-8").replace("\r\n", "\n")


def test_minimal_example_prints_the_published_output() -> None:
    match = EXAMPLE.search(_page())
    assert match, "quick_api.md must keep a minimal example followed by its output"
    code, published = match.groups()
    printed = io.StringIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with contextlib.redirect_stdout(printed):
            exec(compile(code, "quick_api.md#minimal", "exec"), {})
    assert printed.getvalue() == published


def test_minimal_example_matches_the_walkthrough_case() -> None:
    walkthrough = (ROOT / "docs/get-started/quickstart_walkthrough.md").read_text(encoding="utf-8")
    assert "0.286" in walkthrough and "[0.167, 0.333]" in walkthrough
    assert "P(benign) = 0.286  range [0.167, 0.333]" in _page()


def test_page_answers_the_entry_questions_and_links_onward() -> None:
    text = _page()
    for question in (
        "What do I import?",
        "Which model?",
        "Which data?",
        "What are the minimum steps?",
        "Which call for my task?",
        "What comes back?",
    ):
        assert question in text
    assert "{doc}`troubleshooting`" in text
    assert "calibrated_interval_semantics" in text
    assert "not a confidence interval" in text
    for call in ("fit", "calibrate", "predict", "predict_proba", "explain_factual", "explore_alternatives"):
        assert f"{{py:meth}}`{call} <calibrated_explanations.core.WrapCalibratedExplainer.{call}>`" in text
    assert "ce_agent_utils" not in text
