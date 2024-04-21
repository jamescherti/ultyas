# Ultyas - Ultisnips to YASnippet Conversion Tool

Ultyas is a command-line tool designed to simplify the process of converting code snippets from Ultisnips (Vim) to YASnippet format (Emacs).

With Ultyas, you can effortlessly migrate your code snippets to the YASnippet format, saving you valuable time and effort.

## Installation

Here is how to install Ultyas locally to `~/.local/bin/ultyas` using pip:
```
pip install --user ultyas
```

## Command usage example

```
~/.local/bin/ultyas ~/.vim/UltiSnips/python.snippets -o ~/.emacs.d/snippets/python-mode/
```

## Options and flags

```
usage: ultyas <file.snippets> -o <yasnippet-major-mode-dir>

A command-line tool for converting code snippets from Ultisnips to YASnippet format.

positional arguments:
  ultisnips_file        The Ultisnips .snippets file (e.g. '~/.vim/UltiSnips/python.snippets')

options:
  -h, --help            show this help message and exit
  -o YASNIPPET_DIR, --yasnippet-dir YASNIPPET_DIR
                        The YASnippet snippets major mode directory (e.g. '~/.emacs.d/snippets/python-mode/')
  -i {auto,fixed,nothing}, --yas-indent-line {auto,fixed,nothing}
                        Add one of the following comments to the YASnippet snippets that will be generated: "# expand-env: ((yas-indent-line 'fixed))" or "# expand-env: ((yas-indent-line
                        'auto))". For more information on 'yas-indent-line', visit: https://joaotavora.github.io/yasnippet/snippet-reference.html#yas-indent-line
  -t CONVERT_TABS_TO, --convert-tabs-to CONVERT_TABS_TO
                        Convert the tabs that are in the generated snippets to the string passed to this option (Default: The indentation marker '$>')
  -m, --mkdir           Ensure that the directory passed to the --yasnippet-dir flag exists
  -v, --verbose         Verbose mode
  -q, --quiet           Quiet mode
```

## License

Copyright (c) [James Cherti](https://www.jamescherti.com)

Distributed under terms of the GNU General Public License version 3.

## Links

- [Ultyas @PyPI](https://pypi.org/project/ultyas/)
- [Ultyas @GitHub](https://github.com/jamescherti/ultyas/)
