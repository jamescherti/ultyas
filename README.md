# Ultyas - UltiSnips to YASnippet Conversion Tool

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

Copyright (C) 2023-2024 [James Cherti](https://www.jamescherti.com)

Distributed under terms of the GNU General Public License version 3.

## Links

- [Ultyas @PyPI](https://pypi.org/project/ultyas/)
- [Ultyas @GitHub](https://github.com/jamescherti/ultyas/)
