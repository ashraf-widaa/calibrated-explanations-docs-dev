from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import venv
from pathlib import Path

import matplotlib
import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer, make_regression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split

from calibrated_explanations import CalibratedExplainer, WrapCalibratedExplainer

pytestmark = [pytest.mark.integration, pytest.mark.viz]

matplotlib.use("Agg")

_README_PATH = Path("README.md")
_QUICK_API_PATH = Path("docs/get-started/quick_api.md")
_API_REFERENCE_PATH = Path("docs/api/calibrated_explainer.md")
_DEPRECATIONS_PATH = Path("docs/migration/deprecations.md")
_USE_PLUGINS_PATH = Path("docs/practitioner/advanced/use_plugins.md")


def test_should_execute_interpretation_fragments_with_public_payloads() -> None:
    """Exercise the documented rule/prediction distinction (ADR-021, SR-14)."""
    context = _build_classification_context()
    wrapper = context["explainer"]
    wrapper.fit(context["x_proper"], context["y_proper"])
    wrapper.calibrate(context["x_cal"], context["y_cal"])
    assert wrapper.fitted and wrapper.calibrated
    context["x_test"] = context["X_te"][2:3]
    page = Path("docs/foundations/how-to/interpret_explanations.md")
    for block in _python_blocks(page):
        exec(compile(block, str(page), "exec"), context)  # noqa: S102
    factual = context["factual"]
    alternative = context["alternative"]
    assert isinstance(factual.get_rules(), dict)
    factual_core = context["factual_payload"]["core"]
    alternative_core = context["alternative_payload"]["core"]
    assert factual_core["prediction"]["value"] == factual.predict
    assert factual.predict == pytest.approx(0.286, abs=0.0005)
    rules = factual.get_rules()
    feature_pos = rules["feature"].index(27)  # worst concave points, worked case 2
    assert rules["weight"][feature_pos] == pytest.approx(-0.190, abs=0.0005)
    metadata = next(
        row for row in context["factual_payload"]["metadata"]["feature_rules"]
        if row["feature_index"] == 27
    )["prediction_uncertainty"]
    assert (metadata["lower_bound"], metadata["upper_bound"]) == factual.prediction_interval
    alternative_rules = alternative.get_rules()
    scenario = next(
        i for i, feature in enumerate(alternative_rules["feature"])
        if feature == 27 and abs(alternative_rules["predict"][i] - 0.476) < 0.0005
    )
    assert rules["weight_low"][feature_pos] == pytest.approx(
        factual.predict - alternative_rules["predict_high"][scenario]
    )
    assert rules["weight_high"][feature_pos] == pytest.approx(
        factual.predict - alternative_rules["predict_low"][scenario]
    )
    assert alternative_core["kind"] == "alternative"
    assert factual_core["feature_rules"] and alternative_core["feature_rules"]
    assert "weight" in factual_core["feature_rules"][0]
    assert "prediction" in alternative_core["feature_rules"][0]
    assert [row["prediction"]["value"] for row in alternative_core["feature_rules"]] == pytest.approx(
        alternative.get_rules()["predict"]
    )
    assert "uncertainty" in factual.to_telemetry()


def _python_blocks(path: Path) -> list[str]:
    return re.findall(r"```python\n(.*?)```", path.read_text(encoding="utf-8"), re.S)


def _build_classification_context() -> dict[str, object]:
    data = load_breast_cancer()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data,
        data.target,
        test_size=0.2,
        stratify=data.target,
        random_state=42,
    )
    x_proper, x_cal, y_proper, y_cal = train_test_split(
        x_train,
        y_train,
        test_size=0.25,
        stratify=y_train,
        random_state=42,
    )
    model = RandomForestClassifier(random_state=42)
    fitted_model = RandomForestClassifier(random_state=42).fit(x_proper, y_proper)
    explainer = WrapCalibratedExplainer(RandomForestClassifier(random_state=42))
    return {
        "CalibratedExplainer": CalibratedExplainer,
        "WrapCalibratedExplainer": WrapCalibratedExplainer,
        "RandomForestClassifier": RandomForestClassifier,
        "d": data,
        "explainer": explainer,
        "feature_names": data.feature_names,
        "fitted_model": fitted_model,
        "gender_col_index": 0,
        "model": model,
        "np": np,
        "X_cal": x_cal,
        "X_pr": x_proper,
        "X_proper": x_proper,
        "X_query": x_test[:3],
        "X_sample": x_test[:3],
        "X_te": x_test,
        "X_tr": x_train,
        "load_breast_cancer": load_breast_cancer,
        "train_test_split": train_test_split,
        "x_cal": x_cal,
        "x_proper": x_proper,
        "y_cal": y_cal,
        "y_pr": y_proper,
        "y_proper": y_proper,
        "y_te": y_test,
        "y_tr": y_train,
    }


def _venv_python(venv_path: Path) -> Path:
    if sys.platform.startswith("win"):
        return venv_path / "Scripts" / "python.exe"
    return venv_path / "bin" / "python"


def _build_regression_context() -> dict[str, object]:
    x, y = make_regression(n_samples=240, n_features=6, noise=0.5, random_state=42)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    x_proper, x_cal, y_proper, y_cal = train_test_split(
        x_train,
        y_train,
        test_size=0.25,
        random_state=42,
    )
    explainer = WrapCalibratedExplainer(RandomForestRegressor(random_state=42))
    explainer.fit(x_proper, y_proper)
    explainer.calibrate(x_cal, y_cal)
    return {
        "explainer": explainer,
        "X_sample": x_test[:3],
        "low_high_percentiles": (5, 95),
        "np": np,
        "threshold": 120.0,
        "x_cal": x_cal,
        "x_proper": x_proper,
        "y_cal": y_cal,
        "y_proper": y_proper,
    }


def test_readme_python_examples_execute_without_error() -> None:
    readme_blocks = _python_blocks(_README_PATH)
    assert len(readme_blocks) == 3

    quickstart_globals = _build_classification_context()
    exec(readme_blocks[0], quickstart_globals)
    assert "exp" in quickstart_globals

    snippet_globals = _build_classification_context()
    snippet_globals["explainer"].fit(snippet_globals["X_proper"], snippet_globals["y_proper"])
    snippet_globals["explainer"].calibrate(
        snippet_globals["X_cal"],
        snippet_globals["y_cal"],
        feature_names=snippet_globals["feature_names"],
    )
    exec(readme_blocks[1], snippet_globals)
    exec(readme_blocks[2], snippet_globals)


def test_quick_api_python_examples_execute_without_error() -> None:
    quick_api_blocks = _python_blocks(_QUICK_API_PATH)
    # Block 0 is the self-contained minimal example (its printed output is checked in
    # tests/docs/get_started/test_quick_api_example.py); blocks 1-4 are reference fragments.
    assert len(quick_api_blocks) == 5

    exec(quick_api_blocks[0], {})

    classification_globals = _build_classification_context()
    exec(quick_api_blocks[2], classification_globals)
    exec(quick_api_blocks[1], classification_globals)

    regression_globals = _build_regression_context()
    exec(quick_api_blocks[3], regression_globals)
    exec(quick_api_blocks[4], regression_globals)


def test_should_execute_api_reference_core_examples_without_error() -> None:
    api_text = _API_REFERENCE_PATH.read_text(encoding="utf-8")
    api_blocks = _python_blocks(_API_REFERENCE_PATH)

    assert len(api_blocks) >= 2
    assert ".explain(" not in api_text
    exec(api_blocks[0], {})
    exec(api_blocks[1], {})


def test_deprecations_guarded_examples_execute_without_error() -> None:
    deprecations_text = _DEPRECATIONS_PATH.read_text(encoding="utf-8")
    assert "explain_factual(guarded=True)" not in deprecations_text
    assert "explore_alternatives(guarded=True)" not in deprecations_text

    guarded_blocks = [
        block for block in _python_blocks(_DEPRECATIONS_PATH) if "GuardedOptions" in block
    ]
    assert guarded_blocks

    guarded_globals = _build_classification_context()
    guarded_globals["explainer"].fit(guarded_globals["X_proper"], guarded_globals["y_proper"])
    guarded_globals["explainer"].calibrate(
        guarded_globals["X_cal"],
        guarded_globals["y_cal"],
        feature_names=guarded_globals["feature_names"],
    )
    for block in guarded_blocks:
        exec(block, guarded_globals)

    assert "guarded_factual" in guarded_globals
    assert "guarded_alternatives" in guarded_globals


def test_use_plugins_fast_examples_execute_without_error() -> None:
    plugins_text = _USE_PLUGINS_PATH.read_text(encoding="utf-8")
    assert "explain_factual(x_test, fast=True)" not in plugins_text
    assert "explore_alternatives(x_test, fast=True)" not in plugins_text

    plugin_blocks = _python_blocks(_USE_PLUGINS_PATH)
    quick_start_block = next(block for block in plugin_blocks if "wrapped.calibrate" in block)
    fast_constructor_block = next(
        block for block in plugin_blocks if "fast_explainer = CalibratedExplainer" in block
    )

    wrapper_globals = _build_classification_context()
    exec(quick_start_block, wrapper_globals)
    assert wrapper_globals["fast_ready"] is True

    core_globals = _build_classification_context()
    core_globals["model"] = core_globals["fitted_model"]
    exec(fast_constructor_block, core_globals)
    assert core_globals["fast_enabled"] is True


def test_wheel_install_supports_importable_fast_helper_but_not_python_m_execution() -> None:
    with tempfile.TemporaryDirectory(prefix="ce-wheel-smoke-") as temp_dir:
        temp_path = Path(temp_dir)
        dist_dir = temp_path / "dist"
        subprocess.run(
            [sys.executable, "-m", "build", "--wheel", "--outdir", str(dist_dir)],
            check=True,
            cwd=Path.cwd(),
        )
        wheel_path = next(dist_dir.glob("*.whl"))

        venv_dir = temp_path / "venv"
        venv.EnvBuilder(with_pip=True, clear=True).create(venv_dir)
        venv_python = _venv_python(venv_dir)

        subprocess.run(
            [str(venv_python), "-m", "pip", "install", str(wheel_path)],
            check=True,
            cwd=temp_path,
        )
        smoke_code = """
from calibrated_explanations.plugins import find_explanation_plugin, find_interval_plugin
from external_plugins.fast_explanations import register

assert find_explanation_plugin("core.explanation.fast") is not None
assert find_interval_plugin("core.interval.fast") is not None
register()
print("wheel-smoke-ok")
"""
        result = subprocess.run(
            [str(venv_python), "-c", smoke_code],
            check=True,
            cwd=temp_path,
            capture_output=True,
            text=True,
        )
        assert "wheel-smoke-ok" in result.stdout
        module_result = subprocess.run(
            [str(venv_python), "-m", "external_plugins.fast_explanations", "register"],
            cwd=temp_path,
            capture_output=True,
            text=True,
        )
        assert module_result.returncode != 0
        assert "__main__" in module_result.stderr
