#!/usr/bin/env python
#
# Project description: Ultisnips to YASnippet Conversion Tool
# URL: https://github.com/jamescherti/ultyas
#
# Copyright (C) James Cherti
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
"""Ultisnips to YASnippet Conversion Tool."""

import hashlib
import os
import re
from pathlib import Path
from typing import List


def md5sum_file(filename):
    md5 = hashlib.md5()
    with open(filename, "rb") as fhandler:
        for chunk in iter(lambda: fhandler.read(1024), b""):
            md5.update(chunk)
    return md5.hexdigest()


class Snippet:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content


class UltisnipsParseError(Exception):
    """Parse error of an Ultisnips snippet."""


class UltisnipsSnippetsFile:
    def __init__(self):
        self.snippets = {}

    def load(self, snippet_file: os.PathLike):
        inside_snippet = False
        line_num = 0
        current_snippet_name = ""
        current_snippet_content = ""
        with open(snippet_file, "r", encoding="utf-8") as fhandler:
            line_num += 1
            for line in fhandler.readlines():
                line_strip = line.rstrip("\n").strip()

                if inside_snippet:
                    if line_strip == "endsnippet":
                        inside_snippet = False
                        self.snippets[current_snippet_name] = \
                            Snippet(name=current_snippet_name,
                                    content=current_snippet_content)
                    else:
                        current_snippet_content += line

                    # Success
                    continue

                if re.search(r"^snippet\s", line_strip):
                    try:
                        current_snippet_name = re.split(r"\s+", line)[1]
                    except IndexError:
                        line = line.rstrip("\n")
                        err = (f"Snippet name not specified: "
                               f"{snippet_file}: {line_num}: '{line}'")
                        raise UltisnipsParseError(err) from IndexError

                    current_snippet_content = ""
                    inside_snippet = True
                    continue  # Success

                if re.search(r"\s*priority\s", line):
                    # Ignore priority
                    continue

                line_strip = re.sub(r"#.*$", "", line_strip)  # Comment
                if line_strip != "":
                    line = line.rstrip("\n")
                    err = f"{snippet_file}: {line_num}: '{line}'"
                    raise UltisnipsParseError(err)

    def convert_to_yasnippet(self, directory: os.PathLike,
                             convert_tabs_to: str = "$>",
                             yas_indent_line: str = "") -> List[str]:
        if yas_indent_line and yas_indent_line not in ("auto", "fixed"):
            yas_indent_line = ""

        comment_yas_indent_line = (
            f"# expand-env: ((yas-indent-line '{yas_indent_line}))\n"
            if yas_indent_line
            else ""
        )

        result = []
        for snippet_name, snippet_data in self.snippets.items():
            snippet_path = Path(directory).joinpath(snippet_name)
            result.append(str(snippet_path))

            header = ("# -*- mode: snippet -*-\n"
                      f"# name: {snippet_name}\n"
                      f"# key: {snippet_name}\n"  # Used to expand
                      f"{comment_yas_indent_line}"
                      "# --\n")
            content = \
                ((header +
                  self._escape_snippet(snippet_data.content).rstrip("\n"))
                 .replace("\t", convert_tabs_to))
            if snippet_path.is_file():
                content_md5sum = hashlib.md5(content.encode()).hexdigest()
                if content_md5sum == md5sum_file(snippet_path):
                    continue

            with open(snippet_path, "w", encoding="utf-8") as fhandler:
                fhandler.write(content)

        return result

    @staticmethod
    def _escape_snippet(string: str):
        r"""Escape '\${}' except when they resemble '${1:}' / '$1'."""
        numbers = list(map(str, range(0, 10)))

        result = ""
        inside_item = None
        index = 0
        while index < len(string):
            current_char = string[index]
            previous_char = string[index - 1] if index > 0 else ""
            try:
                next_char = string[index + 1]
            except IndexError:
                next_char = ""

            try:
                after_next_char = string[index + 2]
            except IndexError:
                after_next_char = ""

            if inside_item:
                if inside_item == "${n:}":
                    if current_char == "}" and previous_char != "\\":
                        inside_item = None
                elif inside_item == "$n":
                    if current_char not in numbers:
                        inside_item = None
                else:
                    raise ValueError
            elif previous_char != "\\":
                if current_char == "$":
                    if next_char in numbers:
                        inside_item = "$n"
                    elif next_char == "{" and after_next_char in numbers:
                        inside_item = "${n:}"
                        result += string[index]
                        index += 1
                    else:
                        # Escape the current character because it does not
                        # resemble the patterns '$1' or '${1:}'
                        # (e.g $any_string).
                        result += "\\"
                elif current_char == "\\":
                    if next_char not in ["{", "}", "\\"]:
                        # Escape the backslash \ because it does not escape a
                        # special character such as {}\
                        result += "\\"
                elif current_char in ["{", "}"]:
                    # Escape '{}'
                    result += "\\"

            # Add the character
            result += string[index]
            index += 1

        return result
