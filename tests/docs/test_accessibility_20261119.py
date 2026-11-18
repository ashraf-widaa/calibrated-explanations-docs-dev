"""Accessibility guards for the 2026-11-19 navigation.

The sidebar is rendered inside a named navigation landmark, and the homepage
sidebar keeps one icon per documentation section after the move from caption
groups to root entries.
"""

from __future__ import annotations

from pathlib import Path

DOCS = Path(__file__).resolve().parents[2] / "docs"


def test_sidebar_tree_is_a_named_navigation_landmark() -> None:
    template = (DOCS / "_templates" / "sidebar" / "navigation.html").read_text(encoding="utf-8")
    assert '<nav class="sidebar-tree" aria-label="Documentation navigation">' in template
    assert "{{ furo_navigation_tree }}" in template


def test_homepage_sidebar_keeps_one_icon_per_section() -> None:
    css = (DOCS / "_static" / "ce-home.css").read_text(encoding="utf-8")
    for position, icon in ((3, "cube"), (4, "sigma"), (5, "bars"), (6, "code"), (7, "book")):
        assert f"li.toctree-l1:nth-child({position}) > .reference {{ --ce-mask: var(--ce-i-{icon}); }}" in css
