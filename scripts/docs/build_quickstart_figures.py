"""Build the explanation plots shown on the Path C quickstart pages.

Each page's ``python`` blocks are executed in order (as in
``tests/docs/get_started/test_quickstart_examples_execute.py``). The plot calls
listed in ``FIGURES`` are then made exactly as a reader would make them, with a
non-interactive matplotlib backend, and the resulting figure is saved. Every
figure therefore comes from the code its page shows.

Run from the repository root:

    PYTHONPATH=src python scripts/docs/build_quickstart_figures.py

Outputs go to ``docs/get-started/quickstart_assets/``. ``*.png`` is listed in
``.gitignore``, so commit new figures with ``git add -f``.
"""

from __future__ import annotations

import contextlib
import io
import re
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "get-started" / "quickstart_assets"
FENCE = re.compile(r"```python\n(.*?)```", re.DOTALL)

# page -> list of (output file, plot call evaluated in the page namespace)
FIGURES = {
    "quickstart_classification.md": [
        ("classification-factual-case1.png", "factual.plot(1, uncertainty=True)"),
    ],
    "quickstart_guarded.md": [
        ("guarded-factual-case0.png", "guarded_factual.plot(0, uncertainty=True, filter_top=6)"),
    ],
    "apply-to-your-data.md": [
        ("apply-factual-case3.png", "factual.plot(0, uncertainty=True, filter_top=6)"),
    ],
}


def run_page(page: str) -> dict:
    text = (ROOT / "docs" / "get-started" / page).read_text(encoding="utf-8").replace("\r\n", "\n")
    namespace: dict = {}
    for index, block in enumerate(FENCE.findall(text)):
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(block, f"{page}#block{index}", "exec"), namespace)
    return namespace


def main() -> None:
    OUT.mkdir(exist_ok=True)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for page, figures in FIGURES.items():
            namespace = run_page(page)
            for name, call in figures:
                saved: list[Path] = []

                def save_instead_of_show(*_args, _target=OUT / name, _saved=saved, **_kwargs) -> None:
                    # CE calls plt.show() and then closes the figure; save it at that moment.
                    plt.gcf().savefig(_target, dpi=110, bbox_inches="tight")
                    _saved.append(_target)

                original_show = plt.show
                plt.show = save_instead_of_show
                try:
                    plt.close("all")
                    eval(call, namespace)  # noqa: S307 - fixed, repository-local calls
                finally:
                    plt.show = original_show
                    plt.close("all")
                if not saved:
                    raise RuntimeError(f"{page}: {call} produced no figure")
                print("wrote", name)


if __name__ == "__main__":
    main()
