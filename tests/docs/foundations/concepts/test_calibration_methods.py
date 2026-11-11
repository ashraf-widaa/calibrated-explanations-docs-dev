"""Documentation tests for ``docs/foundations/concepts/calibration_methods.md`` (ADD-1 draft).

Two kinds of check, following ``docs/foundations/governance/test_policy.md``:

1. Every ``python`` code block on the page is executed verbatim, in page order, in one
   namespace. When a block is followed by a ``text`` block, the printed output must match it.
2. The hand-worked toy calculations shown in the page's tables and answers are recomputed
   with CE's dependencies (``venn_abers`` and ``crepes``), and each published number must
   appear on the page.
"""

from __future__ import annotations

import contextlib
import io
import re
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[4]
PAGE = ROOT / "docs" / "foundations" / "concepts" / "calibration_methods.md"
FENCE = re.compile(r"```(python|text)\n(.*?)```", re.DOTALL)

VA_SCORES = np.array([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95])
VA_LABELS = np.array([0, 0, 1, 0, 0, 1, 1, 0, 1, 1])
RESIDUALS = np.array(
    [-3.1, -2.4, -1.9, -1.5, -1.2, -0.9, -0.6, -0.4, -0.2, 0.0,
     0.1, 0.3, 0.5, 0.8, 1.0, 1.4, 1.7, 2.2, 3.0]
)  # fmt: skip


def page_text() -> str:
    return PAGE.read_text(encoding="utf-8")


def code_examples() -> list[tuple[str, str | None]]:
    """Return (python source, expected output or None) pairs in page order."""
    blocks = FENCE.findall(page_text())
    pairs = []
    for i, (kind, body) in enumerate(blocks):
        if kind != "python":
            continue
        following = blocks[i + 1] if i + 1 < len(blocks) else None
        expected = following[1] if following and following[0] == "text" else None
        pairs.append((body, expected))
    return pairs


def test_page_examples_run_verbatim_and_print_the_published_output():
    examples = code_examples()
    assert len(examples) == 4, (
        "expected the classification, reliability-table, simulation and regression examples"
    )
    namespace: dict = {}
    for source, expected in examples:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exec(source, namespace)  # noqa: S102 - executes the published docs example
        if expected is not None:
            assert buffer.getvalue() == expected, f"output differs for block:\n{source[:200]}"


def venn_abers_pair(score: float) -> tuple[float, float, float]:
    from venn_abers import VennAbers

    calibrator = VennAbers()
    calibrator.fit(np.c_[1 - VA_SCORES, VA_SCORES], VA_LABELS)
    merged, pair = calibrator.predict_proba(np.array([[1 - score, score]]))
    return float(pair[0, 0]), float(pair[0, 1]), float(merged[0, 1])


@pytest.mark.parametrize(
    ("score", "p0", "p1", "merged"),
    [(0.50, 0.25, 0.75, 0.50), (0.30, 0.25, 0.50, 0.40), (0.90, 0.60, 1.00, 0.7143)],
)
def test_venn_abers_toy_numbers(score, p0, p1, merged):
    got = venn_abers_pair(score)
    assert got == pytest.approx((p0, p1, merged), abs=5e-5)
    # The merge formula stated on the page reproduces the package's merged value.
    assert got[1] / (1 - got[0] + got[1]) == pytest.approx(got[2], abs=1e-9)


def test_cps_toy_numbers():
    import crepes

    cps = crepes.ConformalPredictiveSystem().fit(residuals=RESIDUALS)
    y_hat = np.array([10.0])
    low5, low50, high95, high50 = cps.predict(
        y_hat=y_hat, lower_percentiles=[5, 50], higher_percentiles=[95, 50]
    )[0]
    assert (low5, high95) == pytest.approx((6.9, 13.0))
    assert (low50 + high50) / 2 == pytest.approx(10.0)
    low10, high90 = cps.predict(y_hat=y_hat, lower_percentiles=[10], higher_percentiles=[90])[0]
    assert (low10, high90) == pytest.approx((7.6, 12.2))
    q11 = float(np.ravel(cps.predict(y_hat=y_hat, y=11.0, smoothing=False))[0])
    q9 = float(np.ravel(cps.predict(y_hat=y_hat, y=9.0, smoothing=False))[0])
    assert (q11, q9) == pytest.approx((0.80, 0.30))


def test_published_toy_numbers_appear_on_the_page():
    text = page_text()
    for number in ["p_0 = 0.25", "p_1 = 0.75", "0.40", "0.7143", "6.9", "13.0", "7.6", "12.2",
                   "(15 + 1)/20 = 0.80", "6/20 = 0.30", "(19 - 1)/20 = 0.90"]:  # fmt: skip
        assert number in text, f"{number!r} missing from {PAGE.name}"
