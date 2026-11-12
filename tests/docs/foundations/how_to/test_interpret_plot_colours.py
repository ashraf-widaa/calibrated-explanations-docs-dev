"""The colour description in the interpretation guide must match the renderer.

``utils/configurations/plot_config.ini`` defines the default ``positive``/``negative``
colours; ``viz/matplotlib_adapter.py`` swaps them for plain regression
(``_regression_sign_colors``). The guide describes exactly that.
"""

from __future__ import annotations

import configparser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
GUIDE = ROOT / "docs" / "foundations" / "how-to" / "interpret_explanations.md"
CONFIG = ROOT / "src" / "calibrated_explanations" / "utils" / "configurations" / "plot_config.ini"
ADAPTER = ROOT / "src" / "calibrated_explanations" / "viz" / "matplotlib_adapter.py"


def test_default_colours_are_red_and_blue() -> None:
    config = configparser.ConfigParser()
    config.read(CONFIG, encoding="utf-8")
    assert config["colors"]["positive"] == "red"
    assert config["colors"]["negative"] == "blue"


def test_regression_swaps_the_colours_in_the_renderer() -> None:
    source = ADAPTER.read_text(encoding="utf-8")
    assert 'pos_color = colors_cfg.get("negative")' in source
    assert 'neg_color = colors_cfg.get("positive")' in source


def test_guide_describes_the_rendered_colours() -> None:
    text = " ".join(GUIDE.read_text(encoding="utf-8").split())
    assert "raise the prediction in red and those that lower it in blue" in text
    assert "plain regression plots swap the two" in text
    assert "green" not in text.lower()
    assert "purple" not in text.lower()
