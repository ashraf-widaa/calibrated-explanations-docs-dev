# Contribute in 4 steps

<span id="contributor-hub"></span><span id="core-path"></span>

This page is the starting point for contributing code, tests or
documentation to Calibrated Explanations. It summarizes the existing
contribution policy in
[`CONTRIBUTING.md`](https://github.com/Moffran/calibrated_explanations/blob/main/CONTRIBUTING.md)
and the {doc}`pull request guide <../foundations/governance/pr_guide>`; those
remain the authoritative sources.

The authoritative public source, issue tracker, releases, changelog and
published documentation belong to
[`Moffran/calibrated_explanations`](https://github.com/Moffran/calibrated_explanations).
Develop on a branch in your own fork and open pull requests against that
repository.

(contribute-step-setup)=
## 1. Set up a development environment

Fork and clone the repository, then install the development extras with the
pinned constraints and the pre-commit hooks (shown for Windows PowerShell; on
macOS or Linux activate with `source .venv/bin/activate`):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -e .[dev] -c constraints.txt
pre-commit install
```

Add `.[viz]` to run the plotting tests and examples, or `.[notebooks]` to
work on notebooks.

(contribute-step-change)=
## 2. Choose and make a change

- **Find or open an issue** in the
  [issue tracker](https://github.com/Moffran/calibrated_explanations/issues),
  using the bug report, feature request or plugin publication template.
  Agreeing on the change in the issue first saves rework.
- **Make the change on a branch.** Add or update tests for new or changed
  behaviour, and update the documentation when public behaviour changes.
- **Know where your change belongs:** the {doc}`architecture <../foundations/concepts/architecture>`
  describes the components; {doc}`extension points and plugin contracts <plugin-contract>`
  describe how to extend CE without changing its core.

(contribute-step-checks)=
## 3. Run the checks

```powershell
make quick             # inner-loop checks while editing
make test-core         # fast core test run
make local-checks-pr   # blocking PR-scope preflight before you open a PR
```

For documentation changes, also build the docs with warnings treated as
errors, as the CI does:

```powershell
python -m sphinx -W --keep-going -b html docs docs/_build/html
```

The {doc}`documentation test policy <../foundations/governance/test_policy>`
and the {doc}`notebook policy <notebook_policy>` describe what the
documentation and notebook checks verify.

(contribute-step-pr)=
## 4. Open a pull request

Open the pull request against `Moffran/calibrated_explanations` and complete
the pull request template. Before you submit, check that:

1. tests for new behaviour are added and pass locally;
2. mypy passes for changed modules, and Ruff and Markdown lint pass;
3. documentation is updated when public behaviour changes;
4. breaking changes have migration notes, and the changelog is updated when
   applicable;
5. commits carry a DCO sign-off (`git commit -s`).

The full checklist is in the {doc}`pull request guide <../foundations/governance/pr_guide>`.

## Go further

| Topic | Page |
|---|---|
| Detailed setup, extras and test workflows | [`CONTRIBUTING.md`](https://github.com/Moffran/calibrated_explanations/blob/main/CONTRIBUTING.md) |
| Pull requests and review | {doc}`Pull request guide <../foundations/governance/pr_guide>` |
| Documentation and notebooks | {doc}`Notebook policy <notebook_policy>`, {doc}`documentation test policy <../foundations/governance/test_policy>` |
| Extensions and plugins | {doc}`Plugin contract <plugin-contract>`, {doc}`extending guides <extending/guides/index>`, {doc}`advanced plugin wiring <extending/plugin-advanced-contract>` |
| Architecture and execution flow | {doc}`Architecture <../foundations/concepts/architecture>` |
| Performance work | {doc}`Performance harness <performance_harness>` |
| Governance, releases and support | {doc}`Governance & support <../foundations/governance/index>`, {doc}`release checklist <../foundations/governance/release_checklist>` |
| Working with AI coding agents | {doc}`Agent skill catalogue <agent_skills>`, {doc}`CE-first agent guide <../get-started/ce_first_agent_guide>`, {doc}`AI agent setup <../get-started/copilot-setup>` |

Contributor-facing semantics: every claim about a range or guarantee must
match {doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.

```{toctree}
:maxdepth: 1
:hidden:

Plugin Contract <plugin-contract>
Extending Guides <extending/guides/index>
Advanced Plugin Wiring <extending/plugin-advanced-contract>
Advanced Contributor Tooling <extending/advanced>
Notebook Policy <notebook_policy>
Performance Harness <performance_harness>
Reject Policy Usage <reject_policy_usage>
Agent Skill Catalogue <agent_skills>
CE-First Agent Guide <../get-started/ce_first_agent_guide>
AI Agent Setup <../get-started/copilot-setup>
```
