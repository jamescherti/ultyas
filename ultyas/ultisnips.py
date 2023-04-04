#!/usr/bin/env python
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

    def convert_to_yasnippet(self,
                             directory: os.PathLike,
                             convert_tab_to: str = "$>") -> List[str]:
        header_expand_fixed = "# expand-env: ((yas-indent-line 'fixed))\n" \
            if convert_tab_to == "$>" else ""

        result = []
        for snippet_name, snippet_data in self.snippets.items():
            snippet_path = Path(directory).joinpath(snippet_name)
            result.append(str(snippet_path))

            header = ("# -*- mode: snippet -*-\n"
                      f"# name: {snippet_name}\n"
                      f"# key: {snippet_name}\n"  # Used to expand
                      f"{header_expand_fixed}"
                      "# --\n")
            content = ((header + snippet_data.content.rstrip("\n"))
                       .replace("\t", convert_tab_to))
            if snippet_path.is_file():
                content_md5sum = hashlib.md5(content.encode()).hexdigest()
                if content_md5sum == md5sum_file(snippet_path):
                    continue

            with open(snippet_path, "w", encoding="utf-8") as fhandler:
                fhandler.write(content)

        return result
