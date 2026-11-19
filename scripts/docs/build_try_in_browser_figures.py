"""Build the annotated figures of ``docs/get-started/first-explanation-python.md``.

The page was formerly part of the browser Quick Start (``try-in-browser.md``); the
images keep their ``try_assets/`` names so existing links stay valid.

The script executes the page's own ``python`` blocks in order (reading the data
from ``tests/data`` instead of GitHub, the same files), so the figures come from
exactly the explanations the page prints. It then renders CE's own factual and
alternative plots, removes the file-name title CE adds, and draws numbered
callouts that match the numbered keys under each figure on the page.

Run from the repository root::

    PYTHONPATH=src python scripts/docs/build_try_in_browser_figures.py [name ...]

Pass figure names (for example try-thr-factual) to rebuild only those figures.

Callout positions are fractions of the cropped image (x from the left, y from
the top). If CE's plot layout changes, check the figures and adjust ``CALLOUTS``.
"""

from __future__ import annotations

import os
import re
import sys
import tempfile
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.image as mpimg  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "docs" / "get-started" / "first-explanation-python.md"
ASSETS = PAGE.parent / "try_assets"
URL_LITERAL = (
    '("https://raw.githubusercontent.com/Moffran/"\n'
    '        "calibrated_explanations/main/tests/data/")'
)
FENCE = re.compile(r"```python\n(.*?)```", re.DOTALL)

# name -> (explanation variable, plot keyword arguments, crop of the top in pixels as a fraction)
FIGURES = {
    "try-cls-factual": ("c_factual", {"uncertainty": True}),
    "try-reg-factual": ("r_factual", {"uncertainty": True}),
    "try-cls-alternatives": ("c_alts", {"filter_top": None}),
    "try-reg-alternatives": ("r_alts", {"filter_top": None}),
    "try-thr-factual": ("t_factual", {"uncertainty": True}),
}

# name -> list of (number, x, y) in fractions of the cropped image.
CALLOUTS: dict[str, list[tuple[int, float, float]]] = {
    # 1 prediction, 2 axis, 3 weight bar, 4 weight range, 5 instance values, 6 grey band
    "try-cls-factual": [(1, 0.640, 0.067), (2, 0.528, 0.271), (3, 0.680, 0.363),
                        (4, 0.606, 0.571), (5, 0.959, 0.322), (6, 0.512, 0.883)],
    # 1 prediction, 2 axis, 3 weight bar, 4 weight range, 5 instance values
    "try-reg-factual": [(1, 0.582, 0.076), (2, 0.411, 0.218), (3, 0.567, 0.351),
                        (4, 0.388, 0.498), (5, 0.947, 0.233)],
    # 1 current prediction, 2 axis, 3 one alternative, 4 instance values
    "try-cls-alternatives": [(1, 0.552, 0.065), (2, 0.416, 0.884), (3, 0.391, 0.221),
                             (4, 0.887, 0.077)],
    "try-reg-alternatives": [(1, 0.579, 0.066), (2, 0.375, 0.881), (3, 0.719, 0.763),
                             (4, 0.893, 0.058)],
    # 1 event probability, 2 axis, 3 weight raising, 4 weight lowering, 5 instance values
    "try-thr-factual": [(1, 0.889, 0.089), (2, 0.516, 0.254), (3, 0.505, 0.341),
                        (4, 0.272, 0.599), (5, 0.949, 0.310)],
}
TITLE_CROP = 0.07  # fraction of the image height holding CE's file-name title
ACCENT = "#6d28d9"
ONLY = set(sys.argv[1:])


def run_page() -> dict:
    namespace: dict = {}
    local = repr((ROOT / "tests" / "data").as_posix() + "/")
    text = PAGE.read_text(encoding="utf-8").replace("\r\n", "\n")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for code in FENCE.findall(text):
            code = code.replace(URL_LITERAL, local)
            code = re.sub(r"^.*\.plot\(.*\)$", "", code, flags=re.MULTILINE)
            sys.stdout, saved = open(os.devnull, "w"), sys.stdout
            try:
                exec(compile(code, str(PAGE), "exec"), namespace)
            finally:
                sys.stdout.close()
                sys.stdout = saved
    return namespace


def render(namespace: dict, workdir: Path) -> dict[str, Path]:
    paths = {}
    cwd = Path.cwd()
    os.chdir(workdir)  # CE saves plots below ./plots/
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for name, (var, kwargs) in FIGURES.items():
                if ONLY and name not in ONLY:
                    continue
                namespace[var].plot(show=False, filename=f"{name}.png", **kwargs)
                paths[name] = workdir / "plots" / f"{name}0.png"
    finally:
        os.chdir(cwd)
    return paths


def annotate(name: str, source: Path, target: Path) -> None:
    image = mpimg.imread(source)
    top = int(image.shape[0] * TITLE_CROP)
    image = image[top:]
    height, width = image.shape[:2]
    dpi = 200
    fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.imshow(image)
    ax.set_axis_off()
    radius = max(width, height) * 0.0135
    for number, x, y in CALLOUTS[name]:
        cx, cy = x * width, y * height
        ax.add_patch(plt.Circle((cx, cy), radius, color=ACCENT, zorder=5))
        ax.text(cx, cy, str(number), color="white", ha="center", va="center",
                fontsize=radius * 72 / dpi * 1.15, fontweight="bold", zorder=6)
    fig.savefig(target, dpi=dpi)
    plt.close(fig)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    namespace = run_page()
    with tempfile.TemporaryDirectory() as tmp:
        for name, path in render(namespace, Path(tmp)).items():
            annotate(name, path, ASSETS / f"{name}.png")
            print("wrote", (ASSETS / f"{name}.png").relative_to(ROOT))


if __name__ == "__main__":
    main()
