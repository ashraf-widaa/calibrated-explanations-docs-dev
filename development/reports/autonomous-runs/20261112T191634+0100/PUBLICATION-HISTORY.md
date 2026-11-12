# Publication history — Quick Start v3

| Commit | Content |
|---|---|
| `e44bb875` | Workflow figure; used in How CE Works → The CE workflow |
| `5763d7d2` | Three-path landing, `why-ce`, A1 retitle, C1, C5, 60-second stub, tier map, README, continuity tests |
| `c31189f0` | Walkthrough generator (Path B) and regenerated page and notebook |
| `501911e1` | Quickstarts C2–C4 with real output; output-match test |
| *(reports commit)* | This run directory |

All commits are on local branch `docs-dev/autonomous-20261112`, on top of
`e5fe7c23` (run 2, live on the Beta site).

## Push

**Not pushed.** Blocker: the repository's Claude Code permission policy
(`.claude/settings.json`) denies `git push*`; the agent does not bypass it.
The live Beta site therefore still shows run 2 (`e5fe7c23`), and **no
deployment of Quick Start v3 is claimed.**

Push command for the Project Owner (PowerShell, from the repository root):

```powershell
Set-Location "D:\Jönkoping\CE-Documentation-Redesign\calibrated_explanations"
git push docs-dev docs-dev/autonomous-20261112:main
```

Then check the build on Read the Docs (project `calibrated-explanations-beta`)
and open
<https://calibrated-explanations-beta.readthedocs.io/en/latest/get-started/index.html>:
the page title should be "Quick Start — Understand, Explore and Apply CE" with
the workflow figure and three path cards. Also check that
`.../getting_started_60s.html` redirects to
`.../get-started/ce-tasks-and-modes.html#choosing-your-workflow`.
