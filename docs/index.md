# Calibrated Explanations [(CE)]{.ce-accent}

<div class="ce-topbar"><span class="ce-topbar-label">Documentation</span><form class="ce-search" action="search.html" method="get" role="search"><label class="ce-sr" for="ce-q">Search the documentation</label><input id="ce-q" name="q" type="search" placeholder="Search documentation" autocomplete="off"></form></div>

:::::{container} ce-hero

::::{container} ce-hero-copy

Understand machine-learning predictions through calibrated, uncertainty-aware explanations.

:::{container} ce-hero-actions

```{button-ref} get-started/index
:ref-type: doc
:color: primary

Quick Start
```

:::

::::

:::::

(companion-projects)=

## Documentation

Explore CE through five focused sections.

<nav class="ce-sections" aria-label="Documentation sections"><a class="ce-section-card ce-s1" href="sections/what-and-why.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">CE: What &amp; Why</span><span class="ce-section-desc">The problem, the solution, and the value of CE.</span><span class="ce-section-explore">Explore section</span></a><a class="ce-section-card ce-s2" href="sections/how-ce-works.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">How CE Works: The Theory Behind It</span><span class="ce-section-desc">The theory, methods, and key concepts behind CE.</span><span class="ce-section-explore">Explore section</span></a><a class="ce-section-card ce-s3" href="sections/in-practice.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">CE in Practice: Explore &amp; Apply</span><span class="ce-section-desc">Real use cases, examples, and hands-on guidance.</span><span class="ce-section-explore">Explore section</span></a><a class="ce-section-card ce-s4" href="sections/software-integration.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">CE Software &amp; Integration</span><span class="ce-section-desc">Install CE, use the Python API, and integrate with models.</span><span class="ce-section-explore">Explore section</span></a><a class="ce-section-card ce-s5" href="sections/project-evolution.html"><span class="ce-tile" aria-hidden="true"></span><span class="ce-section-title">CE Project, Vision &amp; Evolution</span><span class="ce-section-desc">The project's background, goals, and future direction.</span><span class="ce-section-explore">Explore section</span></a></nav>

<div class="ce-foot"><a class="ce-foot-item" href="https://github.com/Moffran/calibrated_explanations"><svg class="ce-foot-gh" viewBox="0 0 16 16" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg><span><span class="ce-foot-title">GitHub Repository</span><span class="ce-foot-sub">Source code, issues and contributions.</span></span></a><a class="ce-foot-item" href="https://github.com/Moffran/calibrated_explanations/blob/main/LICENSE"><span class="ce-foot-icon" style="--ce-i:var(--ce-i-scale)" aria-hidden="true"></span><span><span class="ce-foot-title">BSD-3-Clause License</span><span class="ce-foot-sub">Open-source, permissive license.</span></span></a><a class="ce-foot-item" href="https://grejna.ai/#kontakt"><span class="ce-foot-icon" style="--ce-i:var(--ce-i-mail)" aria-hidden="true"></span><span><span class="ce-foot-title">Contact Grejna AB</span><span class="ce-foot-sub">For customized CE solutions.</span></span></a></div>

```{toctree}
:hidden:

Home <self>
```

```{toctree}
:hidden:

Quick Start <get-started/index>
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

```{toctree}
:hidden:
:maxdepth: 1
:caption: Resources

Terminology <foundations/concepts/terminology>
Parameter Reference <foundations/concepts/parameter-reference>
```

:::{container} ce-note

Semantics are mode-specific; see {doc}`foundations/concepts/calibrated_interval_semantics`.
Upgrading? Use the {doc}`upgrade guides <upgrade/index>` and {doc}`migration guides <migration/index>`.
Grejna's commercial services are separate from the open-source library and its license.

Entry-point tier: Tier 1.

:::
