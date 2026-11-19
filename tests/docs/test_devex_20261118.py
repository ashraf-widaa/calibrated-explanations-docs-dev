"""Guards for the 2026-11-18 developer-experience changes.

The homepage links to the Quick Start; the Quick Start is step 2 of Get started;
each Get started page carries a progress bar; the comparison and SHAP/LIME pages answer the
adoption question without a superiority claim; and the API reference starts from
WrapCalibratedExplainer with exceptions and the get_rules() keys documented as the
library behaves.
"""

from __future__ import annotations

import re
import warnings
from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[2] / "docs"
JOURNEY_PAGES = [
    "what-is-ce.md",
    "get-started/try-in-browser.md",
    "get-started/installation.md",
    "foundations/how-to/interpret_explanations.md",
    "get-started/apply-to-your-data.md",
]


def _text(rel: str) -> str:
    return (DOCS / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def test_homepage_routes_readers_without_code_or_figures() -> None:
    # Owner decision 2026-11-18: no code blocks and no figures on the homepage.
    page = _text("index.md")
    intro = page.split("## Learn Calibrated Explanations", 1)[0]
    assert "{button-ref} get-started/try-in-browser" in intro
    fences = [line for line in page.splitlines() if line.startswith("```{") is False and line.startswith("```") and line.strip() != "```"]
    assert fences == [], fences
    assert "{figure}" not in page and "<img" not in page


@pytest.mark.parametrize(("page", "step"), [(page, i + 1) for i, page in enumerate(JOURNEY_PAGES)])
def test_journey_pages_carry_a_progress_bar_with_the_current_step(page: str, step: int) -> None:
    text = _text(page)
    nav = re.search(r'<nav class="ce-journey" aria-label="Get started, step (\d) of 5"><ol>(.*?)</ol></nav>', text)
    assert nav, page
    assert int(nav.group(1)) == step
    items = re.findall(r"<li( aria-current=\"step\")?><a href=\"([^\"]+)\">", nav.group(2))
    assert len(items) == 5
    assert [i for i, (current, _) in enumerate(items) if current] == [step - 1]
    assert f"step {step} of 5 · about" in " ".join(text.split())


def test_comparison_page_answers_the_question_without_ranking() -> None:
    text = " ".join(_text("compare.md").split())
    assert "## Which method answers your question?" in text and "## Side by side" in text
    for method in ("SHAP", "LIME", "Counterfactual methods", "Conformal prediction"):
        assert method in text, method
    assert "SR-06" in text and "not a performance ranking" in text
    assert '<span id="calibrated-explanations-comparisons-ce-first"></span>' in text


def test_shap_lime_page_maps_calls_and_states_the_differences() -> None:
    text = " ".join(_text("get-started/coming-from-shap-lime.md").split())
    for call in ("WrapCalibratedExplainer(model)", "explain_factual", "factual.plot()", "explore_alternatives", "uq_interval=True"):
        assert call in text, call
    assert "labelled held-out data" in text and "do not add up" in text
    assert "−0.069" in text and "−0.069" in _text("get-started/ce-by-example.md")


def test_api_reference_starts_from_the_wrapper_and_lists_exceptions() -> None:
    index = _text("api/index.md")
    assert "**Start here:**" in index and "\nexceptions\n" in index
    api = _text("api/calibrated_explainer.md")
    assert api.index("### WrapCalibratedExplainer (start here)") < api.index("### CalibratedExplainer (advanced)")


def test_documented_get_rules_keys_exist() -> None:
    pytest.importorskip("sklearn")
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from calibrated_explanations import WrapCalibratedExplainer

    api = _text("api/calibrated_explainer.md")
    table = api.split("**What `get_rules()` returns.**", 1)[1].split("\n\n", 2)[1]
    documented = set(re.findall(r"`([a-z_]+)`", table))
    X, y = load_breast_cancer(return_X_y=True)
    explainer = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=10, random_state=0))
    explainer.fit(X[:300], y[:300])
    explainer.calibrate(X[300:450], y[300:450])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rules = explainer.explain_factual(X[450:451])[0].get_rules()
    assert documented and documented <= set(rules), sorted(documented - set(rules))


def test_exceptions_page_matches_library_behaviour() -> None:
    pytest.importorskip("sklearn")
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from calibrated_explanations import WrapCalibratedExplainer
    from calibrated_explanations.utils import exceptions as ce_exceptions

    page = _text("api/exceptions.md")
    for name in re.findall(r"^\| `([A-Za-z]+Error)` \|", page, re.MULTILINE):
        assert issubclass(getattr(ce_exceptions, name), Exception), name

    X, y = load_breast_cancer(return_X_y=True)
    wrapper = WrapCalibratedExplainer(RandomForestClassifier(n_estimators=10, random_state=0))
    with pytest.raises(ce_exceptions.NotFittedError, match="must be fitted before predicting"):
        wrapper.predict(X[:1])
    with pytest.raises(ce_exceptions.NotFittedError, match="must be fitted before calibration"):
        wrapper.calibrate(X[:50], y[:50])
    wrapper.fit(X[:300], y[:300])
    with pytest.raises(ce_exceptions.NotFittedError, match="must be calibrated before explaining"):
        wrapper.explain_factual(X[:1])
    with pytest.warns(UserWarning, match="must be calibrated to get calibrated probabilities"):
        wrapper.predict_proba(X[:1])
    with pytest.raises(ce_exceptions.DataShapeError):
        wrapper.calibrate(X[300:400], y[300:350])
    code, published = re.search(r"```python\n(.*?)```\n\n```text\n(.*?)```", page, re.DOTALL).groups()
    import contextlib
    import io

    printed = io.StringIO()
    with contextlib.redirect_stdout(printed):
        exec(compile(code, "api/exceptions.md", "exec"), {})
    assert printed.getvalue() == published
    for quoted in ("must be fitted before predicting", "must be fitted before calibration",
                   "must be calibrated before explaining", "must be calibrated to get calibrated probabilities"):
        assert quoted in page, quoted
