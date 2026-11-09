# Calibrated Explanations

## Explain machine-learning predictions with calibrated uncertainty

An open-source Python library combining calibrated predictive information with
factual and alternative explanations, helping users interpret model
predictions and their uncertainty.

[View the CE source repository](https://github.com/Moffran/calibrated_explanations)

```{admonition} 1.0.0 stable release
:class: important

The public API, plugin trust model, and visualization extension contract are
stable as of `1.0.0`; only patch-level defect fixes will be accepted against
these contracts going forward. Install with
`pip install calibrated-explanations`. Before adoption, review the
{doc}`v1.0.0 upgrade checklist <upgrade/v1.0.0-upgrade-checklist>`, the
{doc}`Explanation Schema v1 freeze <schema_v1>`, and the
[release notes](https://github.com/Moffran/calibrated_explanations/blob/main/CHANGELOG.md).
```

````{admonition} Open source, demo, and commercial solutions
:class: note

```{eval-rst}
Calibrated Explanations is an independent, BSD-licensed open-source project.
For optional commercial integration, operational deployment or pilot
discussions, `visit Grejna AB <https://grejna.ai/?utm_source=ce_docs&utm_medium=referral&utm_campaign=ce_ecosystem>`__.
These services are separate from the open-source library and its license.
```

For simulated learning scenarios, [explore Decision Labs](https://games.grejna.ai/).
````

## CE: What & Why

Understand how AI models work, why trusting their outputs is challenging and
what Calibrated Explanations contributes.

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Understanding AI Models

{bdg-secondary}`Planned` Educational content not yet available.
:::

:::{grid-item-card} Can We Trust AI Outputs?
:link: foundations/concepts/calibrated_interval_semantics
:link-type: doc

Mode-specific semantics, assumptions and non-guarantees.
:::

:::{grid-item-card} Trustworthy AI
:link: practitioner/playbooks/eu-ai-act-compliance
:link-type: doc

Responsible-practice context; not evidence of EU AI Act compliance.
:::

:::{grid-item-card} The Explainability Gap
:link: compare
:link-type: doc

Conventional explainability compared with CE's calibration-first approach.
:::

:::{grid-item-card} What Is CE & What Does It Add?
:link: tasks/capabilities
:link-type: doc

Supported capabilities, bounded by mode-specific semantics.
:::
::::

## How CE Works: The Theory Behind It

Explore the scientific foundations, statistical mechanisms and assumptions
behind calibrated explanations.

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Essential Foundations
:link: foundations/index
:link-type: doc

Prerequisites; general statistics are not fully covered.
:::

:::{grid-item-card} Calibration & Uncertainty
:link: foundations/concepts/calibrated_interval_semantics
:link-type: doc

Canonical semantics of calibrated uncertainty.
:::

:::{grid-item-card} Statistical Methods Behind CE
:link: foundations/concepts/probabilistic_regression
:link-type: doc

Probabilistic and interval regression; no isotonic tutorial yet.
:::

:::{grid-item-card} How CE Explanations Work
:link: foundations/how-to/interpret_explanations
:link-type: doc

Interpret factual and alternative explanations.
:::

:::{grid-item-card} Assumptions & Guarantees
:link: foundations/concepts/calibrated_interval_semantics
:link-type: doc

Canonical assumptions, guarantees and non-guarantees.
:::
::::

## CE in Practice: Explore & Apply

Discover applications, experience CE interactively, experiment with predictive
models and evaluate the results.

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} CE Examples for New Users
:link: https://calibrated-explanations-demo.ju.se/
:link-type: url

Illustrative external browser demo; runtime and data upload unverified.
:::

:::{grid-item-card} Explore Use-Case Examples
:link: https://games.grejna.ai/
:link-type: url

External Decision Labs simulations; CE integration unverified.
:::

:::{grid-item-card} Test CE with Your Own Data
:link: foundations/how-to/integrate_with_pipelines
:link-type: doc

Interim route: local Python workflow, not browser upload.
:::

:::{grid-item-card} Practical Workflows
:link: get-started/index
:link-type: doc

Get-started guides leading to task and practitioner routes.
:::

:::{grid-item-card} Evaluate & Compare
:link: compare
:link-type: doc

Comparison material; not necessarily benchmarks.
:::
::::

## CE Software & Integration

Understand how the CE library is built, installed, integrated, extended and
maintained.

### Software Foundations

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Software Overview & Versions
:link: sections/software-overview-versions
:link-type: doc

Capabilities and release references; version references need reconciliation.
:::

:::{grid-item-card} Installation & Configuration
:link: get-started/installation
:link-type: doc

Canonical installation and setup.
:::

:::{grid-item-card} Internal Software Architecture
:link: foundations/concepts/architecture
:link-type: doc
:class-card: sd-outline-primary
:shadow: md

Implementation components and boundaries, distinct from the stable public API.
:::
::::

### Development & Integration

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} API & Technical Reference
:link: api/index
:link-type: doc

Public API reference.
:::

:::{grid-item-card} Model & Pipeline Integration
:link: foundations/how-to/integrate_with_pipelines
:link-type: doc

Integrate CE with an existing model or pipeline.
:::

:::{grid-item-card} Extensions & Customization
:link: plugins
:link-type: doc

Plugins and extension points.
:::
::::

### Maintenance & Support

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Troubleshooting & Upgrades
:link: get-started/troubleshooting
:link-type: doc

Common problems, with migration and upgrade routes.
:::
::::

(companion-projects)=

## CE Project, Vision & Evolution

Learn about CE's origins, research contributions, development history, future
direction and ecosystem.

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Vision, Origins & History

{bdg-secondary}`No dedicated page yet` Interim source: [project README](https://github.com/Moffran/calibrated_explanations#readme).
:::

:::{grid-item-card} Research & Publications
:link: researcher/index
:link-type: doc

Researcher hub, citation and replication resources.
:::

:::{grid-item-card} Development & Roadmap
:link: ROADMAP
:link-type: doc

Public roadmap for CE development.
:::

:::{grid-item-card} Community & Contributions
:link: contributor/index
:link-type: doc

Contributor hub and contribution routes.
:::

:::{grid-item-card} CE Ecosystem
:link: plugins
:link-type: doc

Optional plugins; companion and commercial resources are separate.
:::
::::

## Guided learning paths

- **New to CE:** {doc}`Concepts <foundations/concepts/index>` ->
  [illustrative browser demo](https://calibrated-explanations-demo.ju.se/) ->
  {doc}`first example <get-started/quickstart_classification>`.
- **Practitioner:** {doc}`Applications and tasks <tasks/index>` ->
  {doc}`workflows <practitioner/index>` ->
  {doc}`integration <foundations/how-to/integrate_with_pipelines>`.
- **Researcher:** {doc}`theory <researcher/advanced/theory_and_literature>` ->
  {doc}`semantics <foundations/concepts/calibrated_interval_semantics>` ->
  {doc}`research hub <researcher/index>`.
- **Developer / Contributor:** {doc}`architecture <foundations/concepts/architecture>` ->
  {doc}`API <api/index>` ->
  {doc}`contributions <contributor/index>`.

## Documentation references

Semantics are mode-specific. Classification, interval regression and
probabilistic regression do not share one guarantee statement. For semantics,
assumptions and non-guarantees, use
{doc}`foundations/concepts/calibrated_interval_semantics`.

Upgrading from an earlier release? Use the {doc}`upgrade guides <upgrade/index>`
and {doc}`migration guides <migration/index>`.

```{toctree}
:hidden:

Home <self>
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: "CE: What & Why"

Trustworthy AI <practitioner/playbooks/eu-ai-act-compliance>
The Explainability Gap <compare>
What Is CE & What Does It Add? <tasks/capabilities>
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: "How CE Works: The Theory Behind It"

Essential Foundations <foundations/index>
Calibration & Uncertainty <foundations/concepts/calibrated_interval_semantics>
Statistical Methods Behind CE <foundations/concepts/probabilistic_regression>
How CE Explanations Work <foundations/how-to/interpret_explanations>
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: "CE in Practice: Explore & Apply"

Practical Workflows <get-started/index>
tasks/index
practitioner/index
foundations/how-to/index
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: "CE Software & Integration"

sections/software-foundations
sections/development-integration
sections/maintenance-support
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: "CE Project, Vision & Evolution"

Research & Publications <researcher/index>
citing
Development & Roadmap <ROADMAP>
Community & Contributions <contributor/index>
foundations/governance/index
appendices/rtd_tier_map
```

Entry-point tier: Tier 1.
