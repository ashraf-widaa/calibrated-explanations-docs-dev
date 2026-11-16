# 09 — Release readiness and decision register

## 1. Candidate

| Item | Value |
|---|---|
| Branch | `beta/next-docs-enhancement` (local; worktree in the session scratchpad) |
| Base | `73048761` (published integrated candidate) |
| Commits | `85142a5d` WP-6 · `d4328061` WP-13 · `a7d41423` WP-14 · reports commit (this folder) |
| Validation | `07`: both strict builds with 0 warnings, 0 broken links, 365 tests passing, 36 responsive views clean |
| Publication | **BLOCKED** for the agent: `git push*` is denied in `.claude/settings.json`, and RTD activation needs a login or a new, securely supplied token. The exposed token was not used |
| Preview URL | Expected `https://calibrated-explanations-beta.readthedocs.io/en/beta-next-docs-enhancement/`. The slug rule `beta/x` → `beta-x` was observed for the four existing versions; this one is **not yet verified** |

## 2. Steps for the PO to publish the experimental preview

These steps change neither `main` nor `latest`. PowerShell, repository root.

```powershell
Set-Location "D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations"
git rev-parse beta/next-docs-enhancement     # the reports commit on top of a7d41423
git push docs-dev beta/next-docs-enhancement
```

Then, in the RTD dashboard (`calibrated-explanations-beta` → *Versions*),
activate `beta-next-docs-enhancement`. Leave the default version as `latest`.
The agent will then use only public endpoints to verify:
- the build state and commit;
- the URLs and the link crawl;
- 390/1440 px in light and dark;
- the Beta banner.

## 3. Release blockers

| For | Blockers |
|---|---|
| Experimental preview | None |
| Promotion of this candidate to Beta `latest` | None technical. Needs the published preview and PO review first |
| Official CE site | SR-01, SR-02, SR-03, SR-06, SR-15, N-01, N-07 and N-08 unresolved; official publication never approved |

## 4. Recommendation

1. Now: promote `73048761` to `latest` with the plan in `00` (D-24).
2. Publish this candidate as an experimental version (D-26) and review it
   against `beta-integrated-candidate`.
3. If accepted, promote it the same way. It is a fast-forward of
   `73048761`, so the `00` procedure applies with the new commit id; rollback
   is the same restore-tree commit.

## 5. Decisions required from the PO

| ID | Decision | Recommendation | Status |
|---|---|---|---|
| D-24 | Promote `73048761` to Beta `latest` | Approve; plan and tested rollback in `00` | PENDING PRODUCT OWNER APPROVAL |
| D-26 | Push `beta/next-docs-enhancement` and activate its RTD version | Approve | PENDING PRODUCT OWNER APPROVAL |
| D-27 | Dependabot PRs on the Beta repository (RTD previews 2026-11-16): #11 `create-pull-request` 8.1.3 ✓, #12 numpydoc 1.11.0 ✓, #14 myst-parser 4.0.1 ✓, #13 pydata-sphinx-theme 0.19.0 ✗ (needs Sphinx ≥ 8), #15 Sphinx 8.1.3 ✗ (myst-parser 3.0.1 needs Sphinx < 8) | Do not merge #13 or #15 alone; test one combined branch (Sphinx 8.1.3 + myst-parser 4.0.1 + theme 0.19.0) with the strict build first; keep the old `dependabot-…-8` RTD version inactive. Note that RTD pull-request previews are enabled and public | PENDING PRODUCT OWNER APPROVAL |
| D-28 | Accept the two sidebar relabels ("Regulation Context (EU AI Act)", "Guarantees by Mode") and the reordered groups | Accept (as in plan `02`/`15`) | PENDING PRODUCT OWNER APPROVAL |
| D-29 | Notebook environment: the default `python3` Jupyter kernel is an old session venv (scikit-learn 1.9.1, pandas 3.1.1) | Provide a kernel on the docs interpreter (or a dedicated venv) and rerun the two quickstart notebooks | PENDING PRODUCT OWNER APPROVAL |
| D-23 | Sync Beta `src/` with official `main` (`371bd806`, one-sided endpoints) on an isolated branch | Approve as a separate package, then rerun all gates; fixes N-09 | PENDING PRODUCT OWNER APPROVAL |
| D-25 | New pages: calibration intuition (V-7), explainable AI (V-2) | Approve before WP-2/WP-3 | PENDING PRODUCT OWNER APPROVAL |
| — | Send the updated author register (`05`, N-06…N-11 new) to the CE authors | Approve | PENDING AUTHOR REVIEW |
| — | Revoke the exposed RTD token | Required | PENDING PRODUCT OWNER ACTION |
