#!/usr/bin/env python
"""A setuptools based setup module."""

from setuptools import setup, find_packages
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).parent.resolve()
LONG_DESCRIPTION = \
    (CURRENT_DIRECTORY / "README.md").read_text(encoding="utf-8")

setup(
    name="ultyas",
    version="1.1.0",
    packages=find_packages(),
    description=("A tool for converting code snippets from "
                 "Ultisnips to YASnippet format"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/jamescherti/ultyas",
    author="James Cherti",
    python_requires=">=3.6, <4",
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Other",
        "Topic :: Text Editors :: Emacs",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "ultyas=ultyas.__init__:command_line_interface",
        ],
    },
)
