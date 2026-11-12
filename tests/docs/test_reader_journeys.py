"""Reader journeys: each step's page must link to the next step (run 2, stage 07).

Journeys follow the master instruction:
- Beginner: Homepage -> Quick Start -> first example -> interpretation -> further learning.
- Practitioner: Homepage -> CE in Practice -> task guide -> example notebook -> API.
- Researcher: Homepage -> How CE Works -> foundations -> references -> source code.
- Developer: Homepage -> Software & Integration -> installation -> API -> source and tests.
"""

from __future__ import annotations

from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parents[2] / "docs"
GITHUB = "https://github.com/Moffran/calibrated_explanations/"

JOURNEYS = {
    "beginner": [
        ("index.md", "get-started/index"),
        ("get-started/index.md", "quickstart_walkthrough"),
        ("get-started/quickstart_walkthrough.md", "## 7. The factual explanation of our case"),
        ("get-started/quickstart_walkthrough.md", "../foundations/how-to/interpret_explanations.md"),
        ("get-started/quickstart_walkthrough.md", "../foundations/concepts/ce_workflow.md"),
    ],
    "practitioner": [
        ("index.md", "sections/in-practice.html"),
        ("sections/in-practice.md", "../tasks/index"),
        ("tasks/index.md", "classification"),
        ("tasks/classification.md", GITHUB + "blob/main/notebooks/core_demos/"),
        ("tasks/classification.md", "../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer"),
    ],
    "researcher": [
        ("index.md", "sections/how-ce-works.html"),
        ("sections/how-ce-works.md", "../foundations/concepts/ce_workflow"),
        ("foundations/concepts/ce_workflow.md", "calibration_methods"),
        ("foundations/concepts/ce_workflow.md", "calibrated_interval_semantics"),
        ("foundations/concepts/ce_workflow.md", "citing"),
        ("foundations/concepts/ce_workflow.md", GITHUB + "blob/main/src/calibrated_explanations/"),
    ],
    "developer": [
        ("index.md", "sections/software-integration.html"),
        ("sections/software-integration.md", "../get-started/installation"),
        ("sections/software-integration.md", "../api/index"),
        ("api/calibrated_explainer.md", "../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer"),
        ("sections/software-integration.md", GITHUB + "tree/main"),
    ],
}


@pytest.mark.parametrize("journey", sorted(JOURNEYS))
def test_each_step_links_to_the_next(journey: str) -> None:
    for page, target in JOURNEYS[journey]:
        text = (DOCS / page).read_text(encoding="utf-8")
        assert target in text, f"{journey}: {page} does not lead to {target!r}"
