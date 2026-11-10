#!/usr/bin/env python
#
# Project description: Ultisnips to YASnippet Conversion Tool
# URL: https://github.com/jamescherti/ultyas
#
# Copyright (C) 2023-2026 James Cherti
#
# Distributed under terms of the GNU General Public License version 3.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Tests for the ultyas command-line tool."""

import sys
from pathlib import Path

import pytest

from ultyas import command_line_interface


def test_missing_file_reports_clean_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Missing input file errors cleanly without leaking errno to stdout."""
    missing = tmp_path / "does-not-exist.snippets"
    out_dir = tmp_path / "yasnippet-dir"
    monkeypatch.setattr(
        sys, "argv", ["ultyas", str(missing), "-o", str(out_dir)]
    )
    with pytest.raises(SystemExit) as exc_info:
        command_line_interface()
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "does-not-exist.snippets" in captured.err
    assert captured.out.strip() == ""
