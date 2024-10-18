#!/usr/bin/env python
#
# Project description: Ultisnips to YASnippet Conversion Tool
# URL: https://github.com/jamescherti/ultyas
#
# Copyright (C) 2023-2024 James Cherti
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
import platform
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
        current_block = ""
        line_num = 0
        current_snippet_name = ""
        block_content = ""

        with open(snippet_file, "r", encoding="utf-8") as fhandler:
            for line in fhandler.readlines():
                line_num += 1
                line_strip = re.sub(r"#.*$", "", line.strip())

                if current_block:
                    if line_strip == f"end{current_block}":
                        if current_block == "snippet":
                            self.snippets[current_snippet_name] = \
                                Snippet(name=current_snippet_name,
                                        content=block_content)

                        current_block = ""
                        current_snippet_name = ""

                        # Ignore other blocks (e.g., global)
                        continue
                    else:
                        block_content += line
                        continue

                new_block_found = False
                for block_name in ("snippet", "global"):
                    if re.search(r"^" + re.escape(block_name) + r"\s",
                                 line_strip):
                        current_block = block_name
                        block_content = ""
                        new_block_found = True

                        if block_name == "snippet":
                            try:
                                current_snippet_name = \
                                    re.split(r"\s+", line)[1]
                            except IndexError:
                                line = line.rstrip("\n")
                                err = (f"Snippet name not specified: "
                                       f"{snippet_file}: {line_num}: '{line}'")
                                raise UltisnipsParseError(err) from IndexError

                        break

                if new_block_found:
                    continue

                one_liner_found = False
                for one_liner in ("priority", "post_jump", "context"):
                    if re.search(r"^\s*" + re.escape(one_liner) + r"\s",
                                 line_strip):
                        one_liner_found = True
                        break

                if one_liner_found:
                    continue

                # Error
                if line_strip != "":
                    line = line.rstrip("\n")
                    err = f"{snippet_file}: {line_num}: '{line}'"
                    raise UltisnipsParseError(err)

        if current_block:
            line = line.rstrip("\n")
            err = \
                f"{snippet_file}: {line_num}: Unable to find the " \
                f"end of {current_block}"
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
            snippet_path = \
                Path(directory).joinpath(self._sanitize_filename(snippet_name))
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
            elif current_char == "\\":
                # Preserve the escaping of strings that are already escaped.
                result += string[index]
                index += 1
            elif previous_char != "\\":
                # Escape strings that are not yet escaped.
                if current_char == "$":
                    if next_char in numbers:
                        inside_item = "$n"
                    elif next_char == "{" and after_next_char in numbers:
                        inside_item = "${n:}"
                        # Skip the bracket '{'
                        result += string[index]
                        index += 1
                    else:
                        # Escape the current character because it does not
                        # resemble the patterns '$1' or '${1:}'
                        # (e.g $any_string).
                        result += "\\"
                elif current_char == "\\":
                    if next_char not in ["{", "}", "\\"]:
                        # Escape the backslash \ because it is not escaping a
                        # special character such as {}\
                        result += "\\"
                elif current_char == "`":
                    result += "\\"

            # Add the character
            result += string[index]
            index += 1

        return result

    @staticmethod
    def _sanitize_filename(filename: str) -> str:
        """
        Remove invalid characters from a filename to ensure it is valid for
        most file systems.

        Parameters:
            filename: The original filename that may contain invalid
            characters.

        Returns:
            A sanitized version of the filename without invalid characters.
        """
        invalid_chars = {'/', '\0'}

        if platform.system() == "Windows":
            invalid_chars = {'/', '\\', ':', '*', '?', '"', '<', '>', '|'}
            for index in range(0, 32):
                invalid_chars.add(chr(index))

        sanitized_filename = ""
        for char in filename:
            if char in invalid_chars:
                sanitized_filename += hex(ord(char))
            else:
                sanitized_filename += char

        return sanitized_filename
