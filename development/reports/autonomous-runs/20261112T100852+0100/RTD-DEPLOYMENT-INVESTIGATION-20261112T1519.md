# Read the Docs deployment investigation

**Timestamp:** 2026-11-12 15:19 (Europe/Stockholm)
**Method:** public Read the Docs API (v3 projects, builds, versions; v2 build log), `git ls-remote`, public page fetches.

**Access:**
- **Unauthenticated.** No Read the Docs credentials are available to the agent, so dashboard-only settings (webhooks, automation rules, the build-cancel actor) could not be read.
- `git push` is denied in this environment (B-01).

## 1. Project identities

| Field | Calibrated Explanations — Beta | calibrated-explanations-docs-dev |
|---|---|---|
| Slug | `calibrated-explanations-beta` | `calibrated-explanations-docs-dev` |
| Public URL | https://calibrated-explanations-beta.readthedocs.io/en/latest/ | https://calibrated-explanations-docs-dev.readthedocs.io/en/latest/ |
| Repository | `https://github.com/ashraf-widaa/calibrated-explanations-docs-dev.git` | **the same repository** |
| Default branch | `main` | `docs-dev/l05-stage2d` |
| Active versions | `latest` → branch `main` (built) | `latest` → branch `docs-dev/l05-stage2d` (built) |
| Created | 2026-11-09 18:54 UTC | 2026-11-09 17:06 UTC (1 h 48 min earlier) |
| Privacy | public | public |
| Beta banner | yes (`docs/conf.py` keys it to `READTHEDOCS_PROJECT == "calibrated-explanations-beta"`) | **no** (the slug does not match) |
| Latest build | #35840928, 2026-11-12 14:11 UTC, **Cancelled**, commit `b0b2cdc6` | #35764599, 2026-11-09 19:16 UTC, Finished/success, commit `3cc1ffe7` |
| Latest **successful** (served) commit | `e964a79c` (#35823055, 2026-11-11 21:05 UTC) | `3cc1ffe7` |
| Automatic builds | **Yes, evidenced:** #35840928 was created ≈ 3 min after the push of `b0b2cdc6`, with no manual trigger recorded. Webhook settings themselves were not readable without authentication | Builds only its own branch; that branch has not moved since 2026-11-09 (`git ls-remote`: `docs-dev/l05-stage2d` = `3cc1ffe7`) |
| In use? | **Yes**: the canonical Beta URL, referenced across the run records, homepage banner logic and reports | **No**: its branch is fully merged (`3cc1ffe7` is an ancestor of `b0b2cdc6`); referenced only in `learning-reports/L05-stage2D-implementation-report.md` |

**Why two projects exist (from the evidence):**
- `calibrated-explanations-docs-dev` was created first, to preview the L05 Stage 2D feature branch.
- The Beta project was created 1 h 48 min later to publish `main` under the Beta URL, with the Beta banner tied to its slug.
- The staging project's last builds (2026-11-09 18:35–19:16) coincide with the L05 Stage 2D work. It has not been needed since that branch was merged.

## 2. Build #35840928

| Field | Value |
|---|---|
| State | **Cancelled** (`success: false`; error empty) |
| Created / finished | 14:11:27 / 14:12:58 UTC (91 s) |
| Commit / version | `b0b2cdc67bce75413674ce08c8dccd7b0bda98db` / `latest` (`main`) |

**Steps (v2 build log):**

| # | Step | Exit |
|---|---|---|
| 1 | clone | 0 |
| 2 | fetch `main` | 0 |
| 3 | checkout (`HEAD is now at b0b2cdc chore(reports): final validation…`) | 0 |
| 4 | `cat .readthedocs.yaml` | 0 |
| 5 | Python 3.11.15 | 0 |
| 6 | virtualenv | 0 |
| 7 | pip upgrade | 0 |
| 8 | sphinx install | 0 |
| 9 | `pip install -r docs/requirements-doc.txt` (Sphinx downgraded to the pinned 7.4.7) | 0 |
| 10 | `cat docs/conf.py` | 0 |
| 11 | `python -m sphinx -T -j auto -b html …` | **never started** (no start time, no output, exit null) |

**Cause:**
- **Not a repository or configuration failure.** Every step that uses the repository succeeded, and the build was cancelled before Sphinx began.
- **No superseding build exists:** #35840928 is the newest build in the project.
- The API does not record *who or what* cancelled it. A manual cancel in the dashboard, or a platform-side cancellation, are both possible. **Unverified without authenticated dashboard access.**
- The same `.readthedocs.yaml`, `docs/requirements-doc.txt` and Sphinx pins built `e964a79c` successfully (#35823055).
- Locally, `b0b2cdc6` builds strictly (`-W`) with 0 warnings in both Beta and standard mode (Stage 12).

## 3. Is `b0b2cdc6` live?

**No.** The Beta site still serves `e964a79c` (the last successful build), verified on the live pages at 15:1x:

| Check | Expected after `b0b2cdc6` | Live |
|---|---|---|
| `/en/latest/glossary/index.html` | 200 | **404** |
| Homepage "Commercial Services" section | present | absent (Grejna still listed under Project & Resources) |
| Footer "CE Beta Documentation" | present | absent (only the top banner "Beta Documentation") |
| Project & Resources entries | Project, Glossary, GitHub, License | Project, GitHub, License, Contact Grejna AB |
| Sidebar "Overview" entries | 5 | 0 |
| Resources sidebar | Glossary | Terminology |

## 4. Problems found

| ID | Problem | Scope | Status |
|---|---|---|---|
| D-1 | Build of `b0b2cdc6` cancelled before Sphinx ran; the site is stale | Read the Docs platform/dashboard | **Open.** Needs a rebuild (authenticated) or a new push |
| D-2 | Two Read the Docs projects build the same repository; the older one serves an obsolete branch publicly without the Beta banner | Read the Docs account | Recommendation below; no change made (deletion and disabling are prohibited) |
| D-3 | Agent cannot trigger builds | Access | Blocker: no Read the Docs token; `git push` denied (B-01) |

## 5. Changes made and validation

- **No repository change was needed.** The repository configuration is correct, and the cancellation happened outside it.
- Validation evidence for `b0b2cdc6` (Stage 12):
  - strict Beta and standard Sphinx builds, 0 warnings;
  - 262 docs tests passed;
  - 0 broken internal links on 150 pages.
- This report and the run-status updates are committed locally only (not pushed, B-01).

## 6. Recommendation: canonical project

**Keep `calibrated-explanations-beta` as the single canonical Beta project:**
- it builds `main` from the correct repository;
- it publishes to the expected Beta URL;
- its slug drives the Beta banner;
- automatic builds on push are evidenced;
- all existing public links point to it.

**PO action to publish `b0b2cdc6` (either one):**
1. Read the Docs dashboard → *Calibrated Explanations — Beta* → Builds → **Rebuild** `latest`; or
2. push any new commit to `main`. For example, push the local commit that contains this report: `git push docs-dev docs-dev/autonomous-20261112:main`. This also triggers a build.

**After the build, verify:**
1. the build state is *Finished/success* for the new commit;
2. `/en/latest/glossary/index.html` returns 200;
3. the homepage shows Commercial Services and the "CE Beta Documentation" footer;
4. the sidebar shows five "Overview" entries.

**If the build is cancelled again,** open that build in the dashboard: Read the Docs shows a cancellation notice there, which the public API omits. Check the project's concurrency and plan notifications.

## 7. Recommendation: second project

`calibrated-explanations-docs-dev` is **redundant**:
- its only version tracks a merged feature branch (`docs-dev/l05-stage2d`, last commit 2026-11-09);
- its content is contained in `main`;
- it serves an obsolete, banner-less copy that could be mistaken for current Beta documentation.

**Recommended (PO decision, not performed):**
- first, **deactivate its `latest` version or set it to hidden**, or add a redirect to the Beta URL, so that existing links keep resolving;
- later, delete the project once no references remain. The only known reference is `learning-reports/L05-stage2D-implementation-report.md`.

## 8. Unresolved

| Item | Why unresolved |
|---|---|
| Who or what cancelled #35840928 | Not exposed by the public API; needs dashboard access |
| Webhook and automation-rule settings for both projects | Needs authenticated Read the Docs access |
| Live verification of `b0b2cdc6` | Waits for a successful build after a PO-triggered rebuild or push |
