# Installation

```{raw} html
<nav class="ce-journey" aria-label="Learning journey, step 1 of 5"><ol><li aria-current="step"><a href="installation.html"><span class="ce-journey-n">1</span>Install</a></li><li><a href="quickstart.html"><span class="ce-journey-n">2</span>First explanation</a></li><li><a href="../foundations/how-to/interpret_explanations.html"><span class="ce-journey-n">3</span>Read it</a></li><li><a href="apply-to-your-data.html"><span class="ce-journey-n">4</span>Your data</a></li><li><a href="../practitioner/evaluate_ce.html"><span class="ce-journey-n">5</span>Evaluate</a></li></ol></nav>
```

**Learning journey, step 1 of 5 · about 2 minutes.** Install CE, check that
it imports, then continue with the {doc}`Quickstart <quickstart>`.

Calibrated Explanations is published on PyPI and conda-forge. Install the base
package first, then add extras that unlock plotting, notebook examples, or
contributor tooling.

Calibrated Explanations requires Python 3.10 or later and is tested on
Python 3.10 to 3.13.

## PyPI

```bash
pip install calibrated-explanations
```

Extras are opt-in so you only pull the dependencies you need:

| Extra | Purpose | Install command |
| ----- | ------- | --------------- |
| `viz` | Matplotlib-based plotting and PlotSpec adapters. | `pip install "calibrated-explanations[viz]"` |
| `narrative` | PyYAML for YAML narrative templates used by `to_narrative()`. | `pip install "calibrated-explanations[narrative]"` |
| `perf` | `cachetools` backend for the opt-in calibrator cache; without it an in-package fallback is used (see {doc}`../foundations/how-to/tune_runtime_performance`). | `pip install "calibrated-explanations[perf]"` |
| `notebooks` | Jupyter notebook tutorials with pinned dependencies. | `pip install "calibrated-explanations[notebooks]"` |
| `dev` | Full development toolchain (linters, docs, tests). | `pip install "calibrated-explanations[dev]"` |
| `external-plugins` | In-tree optional FAST explanation and interval dependencies. | `pip install "calibrated-explanations[external-plugins]"` |

The {doc}`Python tutorials <../tutorials/index>` draw explanation plots, so
install the `viz` extra before running them; without Matplotlib, CE raises an
error that names this extra when a plot is requested.

Published-study environments and reproduction dependencies are maintained in
the
[Calibrated Explanations Studies](https://github.com/kristinebergs/calibrated-explanations-studies)
repository, not as a core package extra.

## conda-forge

```bash
conda install -c conda-forge calibrated-explanations
```

If you rely on extras from PyPI inside a conda environment, install the base
package via conda and then add the relevant extras with `pip`.

## Verifying your environment

```bash
python -c "import calibrated_explanations; print(calibrated_explanations.__version__)"
```

This prints the version selected by your package manager (`1.0.0` or later).

**Next in the learning journey (step 2 of 5):**
{doc}`Quickstart: your first explanation <quickstart>` (about 10 minutes).

<span id="optional-contributor-fast-path"></span>

## For contributors: development install

For repository development, `pip` remains the canonical fallback:

```bash
python -m pip install -e .[dev] -c constraints.txt
```

If you already use `uv`, you can install the editable development environment
with the same CI constraints:

```bash
uv pip install -e .[dev] -c constraints.txt
```

This `uv` command is optional and constraint-based. The project does not treat
`uv.lock` as an authoritative dependency lockfile.
