# CE Software & Integration

Understand how the CE library is built, installed, integrated, extended and
maintained.

For guarantees, assumptions and non-guarantees, see
{doc}`../foundations/concepts/calibrated_interval_semantics`.

For short definitions of library terms, see the {doc}`Software & Technical Glossary <../glossary/software>`.

## Software Foundations

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Software Overview & Versions
:link: ../sections/software-overview-versions
:link-type: doc

Current release, supported Python versions, release notes and changelog.
:::

:::{grid-item-card} Installation & Configuration
:link: ../get-started/installation
:link-type: doc

Canonical installation and setup.
:::

:::{grid-item-card} Internal Software Architecture
:link: ../foundations/concepts/architecture
:link-type: doc
:class-card: sd-outline-primary
:shadow: md

Implementation components and boundaries, distinct from the stable public API.
:::
::::

## Development & Integration

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} API & Technical Reference
:link: ../api/index
:link-type: doc

Public API reference.
:::

:::{grid-item-card} Model & Pipeline Integration
:link: ../foundations/how-to/integrate_with_pipelines
:link-type: doc

Integrate CE with an existing model or pipeline.
:::

:::{grid-item-card} Extensions & Customization
:link: ../plugins
:link-type: doc

Plugins and extension points.
:::
::::

## Configuration & Operations

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Runtime Configuration
:link: ../foundations/how-to/configure_runtime
:link-type: doc

Configure runtime behaviour through the configuration manager.
:::

:::{grid-item-card} Safe Defaults for Production
:link: ../foundations/how-to/safe-defaults
:link-type: doc

Recommended settings for production deployments.
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
::::

## Maintenance & Support

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Troubleshooting & Upgrades
:link: ../get-started/troubleshooting
:link-type: doc

Common installation and runtime problems.
:::

:::{grid-item-card} Upgrades & Migration
:link: ../upgrade/index
:link-type: doc

Checklists for upgrading between CE versions.
:::

:::{grid-item-card} Source Code and Tests
:link: https://github.com/Moffran/calibrated_explanations/tree/main
:link-type: url

The library source (`src/calibrated_explanations`) and its test suite (`tests/`) on GitHub.
:::
::::

Entry-point tier: Tier 3.
