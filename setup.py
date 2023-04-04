#!/usr/bin/env python
"""A setuptools based setup module."""

from setuptools import setup, find_packages

setup(
    name="ultyas",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ultyas=ultyas.__init__:command_line_interface",
        ],
    },
)
