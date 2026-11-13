# Beta version register

**Updated:** 2026-11-13 20:54 (+01:00). Base of all candidates: `917a04e2`
(WP-1 checkpoint), which is a descendant of the published Beta `main`
`a55c7e9d`.

| Version | Branch | Commit | Purpose | Main changes | Validation (local) | Known issues | Published RTD URL | Publication status | Review status |
|---|---|---|---|---|---|---|---|---|---|
| Beta (live) | `main` | `a55c7e9d` | Current public Beta | Quick Start v3 + visuals pass | RTD build 35848974 success (2026-11-12) | Pre-WP-1 | https://calibrated-explanations-beta.readthedocs.io/en/latest/ | **Published** (verified via RTD API) | PO-approved earlier |
| Beta V1 — Reference | `beta/v1-reference` | `917a04e2` | Approved WP-1 baseline | Code-free Quick Start hub, CE by example, Python tutorials group | Both builds 0 warnings; 316 docs tests; 42 tutorial/API/guarded tests; 158 pages, 0 broken links (WP-1 acceptance) | Two QS phone tables (fixed in V3) | expected `/en/beta-v1-reference/` | **Not published** — push blocked (see below) | WP-1 accepted |
| Beta V2 — Correctness & learning | `beta/v2-learning` | `1e487429` | Audit corrections | One-sided endpoints (version-aware), task-page wording, 6 code examples fixed by execution, guarded `confidence`, version statement, master audit, author sheet | Both builds 0 warnings; 333 docs tests; 42 tutorial/API/guarded tests; 0 broken links | Fragment pages still untested (D-13) | expected `/en/beta-v2-learning/` | **Not published** | Pending PO |
| Beta V3 — Visual learning | `beta/v3-visual` | `f06061b9` | Visual hypothesis | V-6 output-types figure on the guarantees page; phone-friendly tables (no QS table scrolls at 390 px) | Both builds 0 warnings; 323 docs tests; 0 broken links; Playwright 390 px checks | — | expected `/en/beta-v3-visual/` | **Not published** | Pending PO |
| Beta Candidate — Integrated | `beta/integrated-candidate` | `944942cd` (merge of V2 + V3) | Recommended combination | V2 + V3 | Validated in its own worktree: both builds 0 warnings; 369 tests (all docs + guarded + Quick API); 158 pages, 0 broken links | — | expected `/en/beta-integrated-candidate/` | **Not published**; local preview http://127.0.0.1:8002/ | Pending PO |

## Publication blocker and the exact steps for the PO

The agent cannot push: `.claude/settings.json` denies `git push*`, and using
another tool (for example `gh api`) to create branches would bypass that
policy, which CLAUDE.md forbids. Read the Docs version activation also needs
an RTD login or API token, which the agent does not have.

1. Push the four branches (PowerShell, repository root):

   ```powershell
   Set-Location "D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations"
   git push docs-dev beta/v1-reference beta/v2-learning beta/v3-visual beta/integrated-candidate
   ```

   This creates new remote branches only; `main` and the `latest` version are
   untouched.
2. In the Read the Docs dashboard of `calibrated-explanations-beta` →
   *Versions*, activate `beta-v1-reference`, `beta-v2-learning`,
   `beta-v3-visual` and `beta-integrated-candidate` (RTD creates them as
   inactive versions for pushed branches, as it did for the existing
   `docs-dev-*` branches). Leave the default version as `latest`.
3. Tell the agent; it will verify each build via the public RTD API and each
   URL, and update this register with the real URLs and build ids.

The expected URL pattern follows RTD's slug rule observed on this project
(`docs-dev/quickstart-beta` → `docs-dev-quickstart-beta`); it is **not yet
verified** for these branches.
