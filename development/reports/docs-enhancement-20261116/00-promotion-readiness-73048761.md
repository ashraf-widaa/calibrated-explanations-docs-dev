# 00 — Promotion readiness of `beta/integrated-candidate` (`73048761`) and the promotion/rollback plan

**Date:** 2026-11-16 (Stockholm). **For:** the Product Owner.
**PO decisions in force:** candidate `73048761` accepted as the preferred Beta
release candidate; no merge into `main` and no change to `latest` without
explicit approval; the four experimental versions stay; the `dependabot`
RTD version stays inactive; the exposed RTD token is not reused.

## 1. Verdict

| Question | Answer | Status |
|---|---|---|
| Is the candidate technically ready to become Beta `latest`? | Yes. Every technical check below passed; nothing blocks promotion. | **COMPLETED** (verified) |
| Are its scientific statements author-approved? | No. Contested wording is either marked *under review* on the page or was inherited unchanged from the official docs. None is presented as settled. | **PENDING AUTHOR REVIEW** |
| Is it ready for the official CE site? | No. Official publication was never approved, and SR-01…SR-16 and N-01…N-05 are still open. | **PENDING PRODUCT OWNER APPROVAL** |

## 2. Verified technical results (evidence, 2026-11-16)

| Check | Result | Evidence |
|---|---|---|
| Branch head | `beta/integrated-candidate` = `docs-dev/beta/integrated-candidate` = `730487619b86…` | `git rev-parse` |
| Published build | RTD build 35878656, success, commit `73048761` | public RTD API v3 |
| Live page | Candidate semantics page loads, with the Beta banner, the V-6 figure and *under review* notes | WebFetch of `/en/beta-integrated-candidate/…/calibrated_interval_semantics.html` |
| `latest` untouched | `latest` = `a55c7e9d` (build 35878420); default version `latest`; project public | RTD API v3 |
| Fast-forward | `a55c7e9d` is an ancestor of `73048761` (9 commits, 35 docs files) | `git merge-base --is-ancestor` |
| Strict build (rebuilt locally today) | exit 0, 0 warnings (`-W --keep-going`) | worktree at `73048761`, Sphinx 7.4.7, Python 3.13.7 |
| Docs tests | 335 passed, 0 failed | `pytest tests/docs` |
| Internal links | 158 pages, 0 broken | `scripts/docs/check_internal_links.py` |
| Official reference | `upstream/main` still `371bd806`; nothing new to reconcile | `git fetch upstream` |
| Overlap with open dependency PRs | None (the candidate does not touch `docs/requirements-doc.txt` or workflows) | `git diff --name-only` |

## 3. Review of outstanding items

**Scientific author-review questions.** 16 SR items and 5 N items, all open;
the full register, with new items N-06…N-11, is in `05-scientific-review.md`.
In the candidate:
- Corrections it made (N-02, N-04, N-05, SR-07/SR-08 neutral wording, V-6 with
  its SR-15 marker) are conservative and evidence-based.
- 37 *under review* markers across 16 files flag the open questions.

**Navigation consistency.**
- The seven homepage entry points are present.
- Quick Start paths A/B/C cross-link correctly:
  - Card A opens A2 (`why-ce`), which sends newcomers back to A1.
  - B names A as its prerequisite.
  - C1 names path A.
- Three orphan pages are intentional:
  - `getting_started_60s` is a redirect stub.
  - `telemetry` and `multiclass_all_classes_gap_analysis` are orphans in the official docs too.

**Learning-path completeness.**
- A1 → A2 → B → C1 → C2 → Python tutorials is complete and linked both ways.
- Known gaps need new pages that the PO has not approved (D-25):
  - a calibration-intuition page (WP-3, figure V-7);
  - an explainable-AI page (WP-2, figure V-2);
  - the internal-mechanism figure V-4 (WP-4).

**Release-blocking issues for Beta `latest`.** None found. Non-blocking items
are listed below; none of them came from the candidate.

| Item | Origin | Why not blocking | Action |
|---|---|---|---|
| EU AI Act playbook: "Covered" verdicts, "coverage on the calibration set", "certifiable bound", Art. 50 labelled "right to explanation" | Identical in the official docs | Already live on `latest`; legal reading | Authors/PO (N-01, N-07, N-08) |
| `reject-policy` "Confidence Level Selection" | Identical in the official docs | Already live | Authors (SR-16) |
| Release notes stop at v0.10.2 (CHANGELOG has v1.0.2) | Identical in the official docs | Already live | WP-11 |
| Dependabot PR previews #13 and #15 fail on RTD | Dependency-pin conflict | Not on any branch RTD serves | Do not merge alone (`09`, D-27) |
| Exposed RTD token | Earlier session | Not reused | **Revoke** (PO) |

## 4. Promotion plan (not executed; needs explicit PO approval)

The agent cannot push (`git push*` is denied in `.claude/settings.json`), so
the PO runs these steps. PowerShell, repository root.

```powershell
Set-Location "D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations"
git fetch docs-dev

# 0. Preconditions: each line must print the expected value.
git rev-parse docs-dev/main                      # a55c7e9d…
git rev-parse docs-dev/beta/integrated-candidate # 73048761…
git merge-base --is-ancestor docs-dev/main 73048761; $LASTEXITCODE   # 0 = fast-forward

# 1. Safety tag on the current live commit (additive; RTD lists tags as inactive versions).
git tag -a beta-latest-pre-promotion-20261116 a55c7e9d -m "Beta latest before promotion of 73048761"
git push docs-dev beta-latest-pre-promotion-20261116

# 2. Promote: fast-forward main to the candidate. A plain push (no --force) is
#    refused if main moved, so it cannot overwrite unexpected work.
git push docs-dev 73048761:refs/heads/main
```

**3. Verify** (the agent can do this with public, read-only endpoints):
- RTD API v3 builds: a new `latest` build with commit `73048761` and `success: true`.
- The default version is still `latest`.
- The 17 pages and 5 assets checked on 2026-11-13 return HTTP 200 under `/en/latest/`.
- The internal-link crawl shows 0 broken links.
- The Beta banner is present.
- 390/1440 px and light/dark checks pass on the homepage, Quick Start and the semantics page.

The four experimental versions are untouched by this plan.

## 5. Rollback plan (reversible, no force push)

**Fast mitigation (dashboard only, seconds).** In the RTD dashboard, activate
the version `beta-latest-pre-promotion-20261116` (the tag from step 1) and
make it the default version. To undo, set the default back to `latest`.

**Full rollback (git, keeps history).** This makes a new commit on top of
`main` whose files are exactly those of `a55c7e9d`. It was **dry-run on
2026-11-16**: the resulting tree hash equals `a55c7e9d`'s
(`5c0bcc3ec7a4…`), and the commit fast-forwards from `73048761`, so no force
push is needed.

```powershell
git fetch docs-dev
git worktree add --detach ..\ce-rollback docs-dev/main
Set-Location ..\ce-rollback
git read-tree -u --reset a55c7e9d
git commit -m "revert(beta): restore Beta latest content to a55c7e9d"
git diff --quiet a55c7e9d HEAD; $LASTEXITCODE    # 0 = identical content
git push docs-dev HEAD:refs/heads/main
Set-Location ..\calibrated_explanations
git worktree remove ..\ce-rollback
```

The history-rewriting alternative
(`git push --force-with-lease=main:73048761 docs-dev a55c7e9d:refs/heads/main`)
is **not recommended**, and needs separate explicit approval.

## 6. Recommendation

Promote `73048761` to Beta `latest` with the plan above. The next candidate,
`beta/next-docs-enhancement` (`08`, `09`), should first get its own published
preview and PO review. It can then be promoted the same way, also as a fast-forward.
