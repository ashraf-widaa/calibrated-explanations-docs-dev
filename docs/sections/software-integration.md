# Software Architecture & Integration

<span id="ce-software-integration"></span>

*How can I integrate CE into an application or understand and extend its
codebase?*

This section has two routes. Choose the one that matches your task; the two
are linked wherever a procedure or contract applies to both. Readers who have
not used CE yet can start with the
{doc}`Quick Start <../get-started/try-in-browser>`, which needs no
installation.

<span id="software-foundations"></span><span id="development-integration"></span><span id="configuration-operations"></span>

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Integrate CE
:link: integrate-ce
:link-type: ref

Public interfaces and application integration: the API, parameters, output
schema, CLI, runtime configuration, compatibility, troubleshooting,
migration and the changelog.
:::

:::{grid-item-card} Understand and extend CE
:link: extend-ce
:link-type: ref

Internal components and execution flow, extension points and plugin
contracts, and how to contribute: start with **Contribute in 4 steps**.
:::
::::

**Direct links:** {doc}`API Reference <../api/index>` ·
{doc}`Contribute in 4 steps <../contributor/index>`

<span id="install-and-troubleshoot"></span><span id="use-ce-with-your-model-and-calibration-data"></span><span id="integrate-with-pipelines"></span><span id="api-configuration-and-plugins"></span><span id="maintenance-support"></span>

(integrate-ce)=
## Integrate CE

Use CE's public interfaces from your own software.

| Task | Page |
|---|---|
| Install CE in your environment | {doc}`Installation <../get-started/installation>` |
| Pass CE output to another application as JSON | {doc}`Consume CE output from an application <../integrate/consume-output>` |
| See the main calls on one page | {doc}`Quick API <../get-started/quick_api>` |
| Look up a class, method or exception | {doc}`API Reference <../api/index>` |
| Check every parameter and its default | {doc}`Parameter reference <../foundations/concepts/parameter-reference>` |
| Read or validate the JSON output schema | {doc}`Explanation Schema v1 <../schema_v1>` |
| Run CE from the command line | {doc}`CLI reference <../api/cli>` |
| Configure runtime behaviour | {doc}`Runtime configuration <../foundations/how-to/configure_runtime>` and {doc}`Safe defaults for production <../foundations/how-to/safe-defaults>` |
| Fit CE into a scikit-learn pipeline | {doc}`Integrate with pipelines <../foundations/how-to/integrate_with_pipelines>` |
| Find a plugin | {doc}`Plugins and plugin catalog <../plugins>` |
| Check supported versions and compatibility | {doc}`Compatibility & versions <software-overview-versions>` |
| Handle errors and validation | {doc}`Errors and validation <../foundations/concepts/error_handling>` |
| Fix an installation or runtime problem | {doc}`Troubleshooting <../get-started/troubleshooting>` |
| Upgrade from an earlier version | {doc}`Upgrade & migration <../upgrade/index>`: one entry, with version-specific checklists |
| See what changed in a release | {doc}`Changelog and release references <../appendices/changelog_links>` |
| Look up a term | {doc}`Glossary <../glossary/index>` |

(extend-ce)=
## Understand and extend CE

Understand how the codebase works, where it can be extended, and how to
contribute a change.

| Task | Page |
|---|---|
| Make your first contribution | {doc}`Contribute in 4 steps <../contributor/index>` |
| Understand the components and execution flow | {doc}`Architecture <../foundations/concepts/architecture>` |
| Write or register a plugin | {doc}`Plugin contract <../contributor/plugin-contract>` and {doc}`extending guides <../contributor/extending/guides/index>` |
| Configure advanced plugin wiring | {doc}`Advanced plugin wiring <../contributor/extending/plugin-advanced-contract>` |
| Follow the pull request and test policy | {doc}`Pull request guide <../foundations/governance/pr_guide>` and {doc}`test policy <../foundations/governance/test_policy>` |
| Understand project governance | {doc}`Governance & support <../foundations/governance/index>` (under *Project*) |

The source (`src/calibrated_explanations`) and tests (`tests/`) are on
[GitHub](https://github.com/Moffran/calibrated_explanations/tree/main).

**Next section:** {doc}`Project <project-evolution>`.

```{toctree}
:hidden:
:maxdepth: 2

Consume CE Output <../integrate/consume-output>
Quick API <../get-started/quick_api>
API Reference <../api/index>
Parameter Reference <../foundations/concepts/parameter-reference>
Output Schema (v1) <../schema_v1>
Plugins <../plugins>
Compatibility & Versions <software-overview-versions>
Errors & Validation <../foundations/concepts/error_handling>
Troubleshooting <../get-started/troubleshooting>
Upgrade & Migration <../upgrade/index>
Glossary <../glossary/index>
Contribute in 4 Steps <../contributor/index>
Architecture <../foundations/concepts/architecture>
```
