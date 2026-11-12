"""The task quickstarts must run as written and print what the pages show.

Every ``python`` block of each page is executed in page order in one namespace, so a
change in CE's public API that breaks a published example fails this test. When a
``python`` block is directly followed by a ``text`` block, that text block is the
block's published output and must equal what the block prints.
"""

from __future__ import annotations

import contextlib
import io
import re
import warnings
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
PAGES = [
    "docs/get-started/quickstart_classification.md",
    "docs/get-started/quickstart_regression.md",
    "docs/get-started/quickstart_guarded.md",
    "docs/get-started/apply-to-your-data.md",
]
FENCE = re.compile(r"```python\n(.*?)```(?:\n\n```text\n(.*?)```)?", re.DOTALL)


@pytest.mark.parametrize("page", PAGES)
def test_quickstart_blocks_execute_in_order(page: str) -> None:
    matplotlib = pytest.importorskip("matplotlib")
    matplotlib.use("Agg")
    text = (ROOT / page).read_text(encoding="utf-8").replace("\r\n", "\n")
    blocks = FENCE.findall(text)
    assert blocks, f"{page} has no python blocks"
    namespace: dict = {}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for index, (code, published) in enumerate(blocks):
            printed = io.StringIO()
            with contextlib.redirect_stdout(printed):
                exec(compile(code, f"{page}#block{index}", "exec"), namespace)
            if published:
                assert printed.getvalue() == published, (
                    f"{page} block {index}: printed output differs from the page"
                )


@pytest.mark.parametrize("page", PAGES)
def test_quickstart_pages_show_real_output(page: str) -> None:
    text = (ROOT / page).read_text(encoding="utf-8").replace("\r\n", "\n")
    published = [out for _, out in FENCE.findall(text) if out]
    assert len(published) >= 2, f"{page} should show the output of its examples"
    assert "OUTPUT" not in published, f"{page} still has a placeholder output"
