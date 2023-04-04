#!/usr/bin/env python
"""The entry-point of the ultyas command-line tool."""

import sys
import os
import argparse

from .ultisnips import UltisnipsSnippetsFile, UltisnipsParseError


def parse_args():
    usage = ("%(prog)s <ultisnips-file> -o <yasnippet-major-mode-dir>")
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
        help="The directory of the major mode YASnippet snippets (e.g. "
        "'~/.emacs.d/snippets/python-mode/')"
    )

    parser.add_argument(
        "-m",
        "--mkdir",
        default=False,
        action="store_true",
        required=False,
        help="Ensure that the directory passed to "
        "the --yasnippet-dir flag exists",
    )

    return parser.parse_args()


def command_line_interface():
    """The command-line interface."""
    args = parse_args()

    ultisnips_snippet = UltisnipsSnippetsFile()
    try:
        ultisnips_snippet.load(args.ultisnips_file)
        if args.mkdir:
            os.makedirs(args.yasnippet_dir, exist_ok=True)

        if not os.path.isdir(args.yasnippet_dir):
            print(f"Error: The directory does not exist: {args.yasnippet_dir}",
                  file=sys.stderr)
            sys.exit(1)

        list_yasnippet_files = ultisnips_snippet.convert_to_yasnippet(
            args.yasnippet_dir,
        )

        for yasnippet_file in list_yasnippet_files:
            print(yasnippet_file)
    except UltisnipsParseError as err:
        print(f"Parse error: {err}", file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    command_line_interface()
