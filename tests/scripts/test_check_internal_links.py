from __future__ import annotations

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "docs" / "check_internal_links.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_internal_links", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_site(root: Path) -> None:
    (root / "sub").mkdir(parents=True)
    (root / "index.html").write_text(
        '<a href="sub/page.html#here">ok</a>'
        '<a href="missing.html">missing page</a>'
        '<a href="sub/page.html#nowhere">missing anchor</a>'
        '<a href="https://example.org/">external</a>',
        encoding="utf-8",
    )
    (root / "sub" / "page.html").write_text(
        '<h1 id="here">Page</h1><a href="../index.html">back</a>', encoding="utf-8"
    )


def test_reports_missing_pages_and_anchors_only(tmp_path: Path) -> None:
    module = load_module()
    write_site(tmp_path)
    broken = module.broken_links(tmp_path)
    assert sorted(href for _, href in broken) == ["missing.html", "sub/page.html#nowhere"]


def test_exit_status_reflects_broken_links(tmp_path: Path) -> None:
    module = load_module()
    write_site(tmp_path)
    assert module.main([str(tmp_path)]) == 1
    (tmp_path / "index.html").write_text('<a href="sub/page.html#here">ok</a>', encoding="utf-8")
    assert module.main([str(tmp_path)]) == 0
