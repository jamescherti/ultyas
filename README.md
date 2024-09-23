# Ultyas - UltiSnips to YASnippet Conversion Tool
![License](https://img.shields.io/github/license/jamescherti/ultyas)

Ultyas is a command-line tool designed to simplify the process of converting code snippets from UltiSnips (Vim) to YASnippet format (Emacs).

With Ultyas, you can effortlessly migrate your code snippets to the YASnippet format, saving you valuable time and effort.

## Installation

Here is how to install Ultyas locally to `~/.local/bin/ultyas` using pip:
```
pip install --user ultyas
```

## Command usage example

To use Ultyas, simply run the command with the appropriate input and output files. Here is a basic example:

```
~/.local/bin/ultyas ~/.vim/UltiSnips/python.snippets -o ~/.emacs.d/snippets/python-mode/
```

This command takes an UltiSnips file `python.snippets` and converts it to a directory that contains YASnippet snippets at `~/.emacs.d/snippets/python-mode/`.

## Options and flags

```
usage: ultyas <file.snippets> -o <yasnippet-major-mode-dir>

A command-line tool for converting code snippets from UltiSnips to YASnippet format.

positional arguments:
  ultisnips_file        The UltiSnips .snippets file (e.g. '~/.vim/UltiSnips/python.snippets')

options:
  -h, --help            show this help message and exit
  -o YASNIPPET_DIR, --yasnippet-dir YASNIPPET_DIR
                        The YASnippet snippets major mode directory (e.g. '~/.emacs.d/snippets/python-mode/')
  -i {auto,fixed,nothing}, --yas-indent-line {auto,fixed,nothing}
                        Add one of the following comments to the YASnippet snippets that will be generated: "# expand-env: ((yas-indent-line 'fixed))" or "# expand-env: ((yas-indent-line
                        'auto))". For more information on 'yas-indent-line', visit: https://joaotavora.github.io/yasnippet/snippet-reference.html#yas-indent-line
  -t CONVERT_TABS_TO, --convert-tabs-to CONVERT_TABS_TO
                        Convert the tabs that are in the generated snippets to the string passed to this option (Default: The indentation marker '$>')
  -v, --verbose         Verbose mode
  -q, --quiet           Quiet mode
```

## Example of an UltiSnips snippet that could be converted to Yasnippet

Here is an example of an UltiSnips snippet that can be converted by Ultyas from the UltiSnips format to the Yasnippet format:
```
priority 50

snippet if
if ${1:True}:
	${2:pass}
endsnippet

snippet for
for ${1:_} in ${2:[]}:
	${3:pass}
endsnippet

snippet while
while ${1:True}:
	${2:pass}
endsnippet
```

## License

The `ultyas` Emacs package has been written by [James Cherti](https://www.jamescherti.com/) and is distributed under terms of the GNU General Public License version 3, or, at your choice, any later version.

Copyright (C) 2023-2024 [James Cherti](https://www.jamescherti.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.

## Links

- [Ultyas @GitHub](https://github.com/jamescherti/ultyas/)
- [Ultyas @PyPI](https://pypi.org/project/ultyas/)

Other Emacs packages by the same author:
- [minimal-emacs.d](https://github.com/jamescherti/minimal-emacs.d): This repository hosts a minimal Emacs configuration designed to serve as a foundation for your vanilla Emacs setup and provide a solid base for an enhanced Emacs experience.
- [vim-tab-bar.el](https://github.com/jamescherti/vim-tab-bar.el): Make the Emacs tab-bar Look Like Vim’s Tab Bar.
- [outline-indent.el](https://github.com/jamescherti/outline-indent.el): An Emacs package that provides a minor mode that enables code folding and outlining based on indentation levels for various indentation-based text files, such as YAML, Python, and other indented text files.
- [easysession.el](https://github.com/jamescherti/easysession.el): Easysession is lightweight Emacs session manager that can persist and restore file editing buffers, indirect buffers/clones, Dired buffers, the tab-bar, and the Emacs frames (with or without the Emacs frames size, width, and height).
- [elispcomp](https://github.com/jamescherti/elispcomp): A command line tool that allows compiling Elisp code directly from the terminal or from a shell script. It facilitates the generation of optimized .elc (byte-compiled) and .eln (native-compiled) files.
- [tomorrow-night-deepblue-theme.el](https://github.com/jamescherti/tomorrow-night-deepblue-theme.el): The Tomorrow Night Deepblue Emacs theme is a beautiful deep blue variant of the Tomorrow Night theme, which is renowned for its elegant color palette that is pleasing to the eyes. It features a deep blue background color that creates a calming atmosphere. The theme is also a great choice for those who miss the blue themes that were trendy a few years ago.
- [dir-config.el](https://github.com/jamescherti/dir-config.el): Automatically find and evaluate .dir-config.el Elisp files to configure directory-specific settings.
- [flymake-bashate.el](https://github.com/jamescherti/flymake-bashate.el): A package that provides a Flymake backend for the bashate Bash script style checker.
- [flymake-ansible-lint.el](https://github.com/jamescherti/flymake-ansible-lint.el): An Emacs package that offers a Flymake backend for `ansible-lint`.
