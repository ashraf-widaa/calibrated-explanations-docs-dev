"""Executable examples on concept pages must run and print what the page shows.

Each ``python`` block is executed in page order in one namespace. When a ``text`` block
follows a ``python`` block, the printed output must match it exactly (after stripping
trailing whitespace). ``{code-block} python`` fragments are illustrations and are skipped.
"""

from __future__ import annotations

import contextlib
import io
import re
import warnings
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[4]
PAGES = [
    "docs/foundations/concepts/probabilistic_regression.md",
    "docs/foundations/concepts/alternatives.md",
    "docs/practitioner/evaluate_ce.md",
]
FENCE = re.compile(r"```(python|text)\n(.*?)```", re.DOTALL)


def blocks(page: str) -> list[tuple[str, str | None]]:
    found = FENCE.findall((ROOT / page).read_text(encoding="utf-8"))
    pairs: list[tuple[str, str | None]] = []
    for index, (kind, body) in enumerate(found):
        if kind != "python":
            continue
        expected = None
        if index + 1 < len(found) and found[index + 1][0] == "text":
            expected = found[index + 1][1]
        pairs.append((body, expected))
    return pairs


@pytest.mark.parametrize("page", PAGES)
def test_examples_run_and_match_shown_output(page: str) -> None:
    matplotlib = pytest.importorskip("matplotlib")
    matplotlib.use("Agg")
    namespace: dict = {}
    pairs = blocks(page)
    assert pairs, page
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for index, (source, expected) in enumerate(pairs):
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                exec(compile(source, f"{page}#block{index}", "exec"), namespace)
            if expected is not None:
                shown = [line.rstrip() for line in expected.strip("\n").splitlines()]
                printed = [line.rstrip() for line in buffer.getvalue().strip("\n").splitlines()]
                assert printed == shown, f"{page} block {index}"
