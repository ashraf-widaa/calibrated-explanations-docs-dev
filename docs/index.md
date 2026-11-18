# Calibrated Explanations [(CE)]{.ce-accent}

<div class="ce-topbar"><span class="ce-topbar-label">Documentation</span><form class="ce-search" action="search.html" method="get" role="search"><label class="ce-sr" for="ce-q">Search the documentation</label><input id="ce-q" name="q" type="search" placeholder="Search documentation" autocomplete="off"></form></div>

:::::{container} ce-hero

::::{container} ce-hero-copy

Understand machine-learning predictions through calibrated, uncertainty-aware explanations.

**Calibrated Explanations (CE)** is an open-source Python library. Wrap your
scikit-learn-style classifier or regressor, calibrate it on labelled data it
has not seen, and get a calibrated prediction with a range, plus the feature
conditions behind it, each with its own range.

:::{container} ce-hero-actions

```{button-ref} get-started/quickstart
:ref-type: doc
:color: primary

Quickstart: 10 minutes
```

```{button-ref} get-started/ce-by-example
:ref-type: doc
:color: secondary
:outline:

See an example, no code
```

:::

:::{container} ce-hero-hint

New to CE? Follow the five-step journey on {doc}`Get started <get-started/index>`.

:::

::::

:::::

## Your first explanation

```bash
pip install "calibrated-explanations[viz]"
```

```python
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(model)      # your scikit-learn-style model
explainer.fit(X_proper, y_proper)               # train as usual
explainer.calibrate(X_cal, y_cal)               # labelled data the model has not seen
explainer.explain_factual(X_test[:1]).plot()    # calibrated explanation with ranges
```

```{figure} get-started/walkthrough_assets/walkthrough-figure-1.png
:alt: CE output for one breast-cancer case. Top: calibrated probability of benign 0.286 with its range from 0.167 to 0.333. Below: one bar per feature condition showing its weight range; worst concave points above 0.14 has the largest range, entirely below zero.
:width: 640px
:class: ce-home-figure

The result for one case of the {doc}`Quickstart <get-started/quickstart>`:
the calibrated probability with its range (top) and the conditions behind it,
each with a weight range (bars). The ranges describe the model's behaviour,
not causal effects.
```

| I am… | Start here |
|---|---|
| New to CE | {doc}`Quickstart <get-started/quickstart>`, then {doc}`how to read the result <foundations/how-to/interpret_explanations>` |
| Using SHAP or LIME today | {doc}`Coming from SHAP or LIME <get-started/coming-from-shap-lime>` and the {doc}`comparison of methods <compare>` |
| Putting CE into production | {doc}`Apply CE to your own data <get-started/apply-to-your-data>`, the {doc}`how-to guides <foundations/how-to/index>` and the {doc}`API reference <api/index>` |
| A researcher | {doc}`The CE workflow <foundations/concepts/ce_workflow>` and the {doc}`statistical methods <foundations/concepts/calibration_methods>` |

Every printed output in this documentation comes from a tested CE run.

## Documentation

Choose the section that matches your goal.

<nav class="ce-sections" aria-label="Documentation sections"><a class="ce-section-card ce-s1" href="sections/what-and-why.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">CE: What &amp; Why</span><span class="ce-section-desc">Why uncertainty-aware explanations matter and what CE adds.</span><span class="ce-section-explore">Explore section</span></a><a class="ce-section-card ce-s2" href="sections/how-ce-works.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">How CE Works: The Theory Behind It</span><span class="ce-section-desc">The theory, methods and key concepts behind CE.</span><span class="ce-section-explore">Explore section</span></a><a class="ce-section-card ce-s3" href="sections/in-practice.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">CE in Practice: Explore &amp; Apply</span><span class="ce-section-desc">Interactive demos, task guides and practical playbooks.</span><span class="ce-section-explore">Explore section</span></a><a class="ce-section-card ce-s4" href="sections/software-integration.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">CE Software &amp; Integration</span><span class="ce-section-desc">Installation, Python API and integration with models and pipelines.</span><span class="ce-section-explore">Explore section</span></a></nav>

:::{container} ce-note

Guarantees are mode-specific. See {doc}`Calibrated interval semantics <foundations/concepts/calibrated_interval_semantics>`.

Direct routes: {doc}`practitioners <practitioner/index>` ·
{doc}`researchers <researcher/index>` · {doc}`contributors <contributor/index>` ·
{doc}`foundations and concepts <foundations/index>`.

:::

## Project & Resources

Explore the research, terminology and open-source project.

<div class="ce-foot"><a class="ce-foot-item" href="sections/project-evolution.html"><span class="ce-foot-icon" style="--ce-i:var(--ce-i-flag)" aria-hidden="true"></span><span><span class="ce-foot-title">CE Project, Vision &amp; Evolution</span><span class="ce-foot-sub">Research, publications, roadmap and community.</span></span></a><a class="ce-foot-item" href="glossary/index.html"><span class="ce-foot-icon" style="--ce-i:var(--ce-i-book)" aria-hidden="true"></span><span><span class="ce-foot-title">Glossary</span><span class="ce-foot-sub">Scientific and software terms, A&#8288;–&#8288;Z.</span></span></a><a class="ce-foot-item" href="https://github.com/Moffran/calibrated_explanations"><svg class="ce-foot-gh" viewBox="0 0 16 16" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg><span><span class="ce-foot-title">GitHub Repository</span><span class="ce-foot-sub">Source code, issues and contributions.</span></span></a><a class="ce-foot-item" href="https://github.com/Moffran/calibrated_explanations/blob/main/LICENSE"><span class="ce-foot-icon" style="--ce-i:var(--ce-i-scale)" aria-hidden="true"></span><span><span class="ce-foot-title">BSD-3-Clause License</span><span class="ce-foot-sub">Open-source license and usage terms.</span></span></a></div>

```{toctree}
:hidden:
:maxdepth: 2

Home <self>
Get Started <get-started/index>
CE: What & Why <sections/what-and-why>
How CE Works <sections/how-ce-works>
CE in Practice <sections/in-practice>
CE Software & Integration <sections/software-integration>
Project & Resources <sections/project-evolution>
```

## Commercial Services

<div class="ce-commercial"><a class="ce-foot-item" href="https://grejna.ai/#kontakt"><span class="ce-foot-icon" style="--ce-i:var(--ce-i-mail)" aria-hidden="true"></span><span><span class="ce-foot-title">Contact Grejna AB</span><span class="ce-foot-sub">For customized CE solutions and commercial support, separate from the open-source library and its license.</span></span></a></div>

:::{container} ce-meta

```{only} ce_beta
CE Beta Documentation
```


:::
