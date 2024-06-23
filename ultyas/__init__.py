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
"""The entry-point of the ultyas command-line tool."""

import argparse
import os
import sys
from pathlib import Path

from .ultisnips import UltisnipsParseError, UltisnipsSnippetsFile


def parse_args():
    usage = ("%(prog)s <file.snippets> "
             "-o <yasnippet-major-mode-dir>")
    parser = argparse.ArgumentParser(
        description=("A command-line tool for converting code snippets "
                     "from Ultisnips to YASnippet format."),
        usage=usage,
    )

    parser.add_argument(
        "ultisnips_file",
        type=str,
        help="The Ultisnips .snippets file (e.g. "
        "'~/.vim/UltiSnips/python.snippets')",
    )

    parser.add_argument(
        "-o",
        "--yasnippet-dir",
        required=True,
        help="The YASnippet snippets major mode directory (e.g. "
        "'~/.emacs.d/snippets/python-mode/')"
    )

    parser.add_argument(
        "-i",
        "--yas-indent-line",
        default="nothing",
        choices=["auto", "fixed", "nothing"],
        required=False,
        help=("Add one of the following comments to the "
              "YASnippet snippets that will be generated: "
              "\"# expand-env: ((yas-indent-line 'fixed))\" or "
              "\"# expand-env: ((yas-indent-line 'auto))\". "
              "For more information on 'yas-indent-line', visit: "
              "https://joaotavora.github.io/yasnippet/snippet-reference.html"
              "#yas-indent-line"),
    )

    parser.add_argument(
        "-t",
        "--convert-tabs-to",
        default="$>",
        required=False,
        help=("Convert the tabs that are in the generated snippets to "
              "the string passed to this option "
              "(Default: The indentation marker '$>')"),
    )

    parser.add_argument(
        "-m",
        "--mkdir",
        default=False,
        action="store_true",
        required=False,
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        required=False,
        help="Verbose mode",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        default=False,
        action="store_true",
        required=False,
        help="Quiet mode",
    )

    return parser.parse_args()


def command_line_interface():
    """The command-line interface."""
    args = parse_args()

    ultisnips_file = Path(args.ultisnips_file)
    yasnippet_dir = Path(args.yasnippet_dir)

    ultisnips_snippet = UltisnipsSnippetsFile()
    try:
        ultisnips_snippet.load(ultisnips_file)
        if not yasnippet_dir.parent.is_dir():
            print(f"Error: The parent directory of {yasnippet_dir} "
                  "does not exist", file=sys.stderr)
            sys.exit(1)

        os.mkdir(yasnippet_dir)

        if not os.path.isdir(yasnippet_dir):
            print(f"Error: The directory does not exist: {yasnippet_dir}",
                  file=sys.stderr)
            sys.exit(1)

        list_yasnippet_files = ultisnips_snippet.convert_to_yasnippet(
            directory=yasnippet_dir,
            convert_tabs_to=args.convert_tabs_to,
            yas_indent_line=args.yas_indent_line,
        )

        if not args.quiet:
            if args.verbose:
                for yasnippet_file in list_yasnippet_files:
                    print(yasnippet_file)

                print()

            print(f"Successfully converted '{ultisnips_file}' to "
                  f"'{yasnippet_dir}'.")
    except UltisnipsParseError as err:
        print(f"Parse error: {err}", file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"Error: {err.filename}: {err}", file=sys.stderr)
        print(err.errno)
        sys.exit(1)


if __name__ == '__main__':
    command_line_interface()
