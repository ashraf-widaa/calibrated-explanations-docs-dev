# CE Software & Integration

Install CE, use it with your own model and calibration data, integrate it
into a pipeline, and find the API, configuration and plugin references.

For short definitions of library terms, see the {doc}`Software & Technical Glossary <../glossary/software>`.

Read this section in order. Readers who have not used CE yet can start with
the {doc}`browser Quick Start <../get-started/try-in-browser>`, which needs
no installation.

<span id="software-foundations"></span>

## 1. Install and troubleshoot

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Installation
:link: ../get-started/installation
:link-type: doc

Canonical installation with pip or conda, optional extras and a check that it works. (Step 1 of the learning journey in *Get Started*.)
:::

:::{grid-item-card} Troubleshooting
:link: ../get-started/troubleshooting
:link-type: doc

Common installation and runtime problems.
:::

:::{grid-item-card} Software Overview & Versions
:link: ../sections/software-overview-versions
:link-type: doc

Current release, supported Python versions, release notes and changelog.
:::
::::

<span id="development-integration"></span>

## 2. Use CE with your model and calibration data

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Quick API
:link: ../get-started/quick_api
:link-type: doc

The main calls of `WrapCalibratedExplainer` at a glance, by mode.
:::

:::{grid-item-card} Apply CE to Your Own Data
:link: ../get-started/apply-to-your-data
:link-type: doc

Split off calibration data, wrap your model, calibrate, explain, check and save.
:::

:::{grid-item-card} Quickstart in Python
:link: ../get-started/quickstart
:link-type: doc

One classification example, step by step, in about 10 minutes.
:::
::::

## 3. Integrate with pipelines

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Model & Pipeline Integration
:link: ../foundations/how-to/integrate_with_pipelines
:link-type: doc

Integrate CE with an existing model, preprocessing or pipeline.
:::

:::{grid-item-card} Safe Defaults for Production
:link: ../foundations/how-to/safe-defaults
:link-type: doc

Recommended settings for production deployments.
:::
::::

<span id="configuration-operations"></span>

## 4. API, configuration and plugins

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} API & Technical Reference
:link: ../api/index
:link-type: doc

Public API reference, starting from `WrapCalibratedExplainer`.
:::

:::{grid-item-card} Runtime Configuration
:link: ../foundations/how-to/configure_runtime
:link-type: doc

Configure runtime behaviour through the configuration manager.
:::

:::{grid-item-card} Extensions & Plugins
:link: ../plugins
:link-type: doc

Plugins and extension points.
:::

:::{grid-item-card} Performance Tuning
:link: ../foundations/how-to/tune_runtime_performance
:link-type: doc

Opt-in caching and parallel execution.
:::

:::{grid-item-card} Telemetry
:link: ../foundations/how-to/configure_telemetry
:link-type: doc

Optional telemetry and provenance records.
:::

:::{grid-item-card} Internal Software Architecture
:link: ../foundations/concepts/architecture
:link-type: doc

Implementation components and boundaries, distinct from the stable public API.
:::
::::

## Maintenance & support

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Upgrade Guides
:link: ../upgrade/index
:link-type: doc

Checklists for upgrading between CE versions.
:::

:::{grid-item-card} Migration Guides
:link: ../migration/index
:link-type: doc

Breaking changes between major releases, deprecations and terminology updates.
:::

:::{grid-item-card} Source Code and Tests
:link: https://github.com/Moffran/calibrated_explanations/tree/main
:link-type: url

The library source (`src/calibrated_explanations`) and its test suite (`tests/`) on GitHub.
:::
::::

**Next:** {doc}`Project & Resources <project-evolution>` (glossary, research,
citation and community).

```{toctree}
:hidden:
:maxdepth: 2

Installation <../get-started/installation>
Troubleshooting <../get-started/troubleshooting>
Software Overview & Versions <software-overview-versions>
Quick API <../get-started/quick_api>
Apply CE to Your Own Data <../get-started/apply-to-your-data>
Model & Pipeline Integration <../foundations/how-to/integrate_with_pipelines>
Safe Defaults for Production <../foundations/how-to/safe-defaults>
API & Technical Reference <../api/index>
Runtime Configuration <../foundations/how-to/configure_runtime>
Extensions & Plugins <../plugins>
Performance Tuning <../foundations/how-to/tune_runtime_performance>
Telemetry <../foundations/how-to/configure_telemetry>
Internal Software Architecture <../foundations/concepts/architecture>
Upgrade Guides <../upgrade/index>
Migration Guides <../migration/index>
```
