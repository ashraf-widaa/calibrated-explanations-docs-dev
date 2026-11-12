"""The task quickstarts must run as written.

Every ``python`` block of each page is executed in page order in one namespace, so a
change in CE's public API that breaks a published example fails this test.
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
]
FENCE = re.compile(r"```python\n(.*?)```", re.DOTALL)


@pytest.mark.parametrize("page", PAGES)
def test_quickstart_blocks_execute_in_order(page: str) -> None:
    matplotlib = pytest.importorskip("matplotlib")
    matplotlib.use("Agg")
    blocks = FENCE.findall((ROOT / page).read_text(encoding="utf-8"))
    assert blocks, f"{page} has no python blocks"
    namespace: dict = {}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for index, block in enumerate(blocks):
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(block, f"{page}#block{index}", "exec"), namespace)
