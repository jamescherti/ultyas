# Ultyas - UltiSnips to YASnippet Conversion Tool
![License](https://img.shields.io/github/license/jamescherti/ultyas)

Ultyas is a command-line tool that simplifies the process of converting code snippets from **UltiSnips** (Vim/Neovim) to **YASnippet** format (Emacs).

Transitioning from Vim/Neovim to Emacs can be difficult. Ultyas addresses this issue by offering a straightforward solution for converting your existing UltiSnips snippets into the YASnippet format.

Ultyas can be used for the following purposes:
- Migrating your snippets from UltiSnips to YASnippet format.
- **Maintaining consistent snippets across both Vim/Neovim and Emacs.** (For instance, the author of Ultyas effortlessly switches between Vim and Emacs depending on the machine and environment, ensuring that the same snippets are accessible in both editors.)

**NOTE:** Emacs users are recommended to install the [ultisnips-mode](https://github.com/jamescherti/ultisnips-mode.el) package, which provides a major mode for editing Ultisnips snippet files (*.snippets). This mode includes syntax highlighting to simplify and improve the editing of Ultisnips snippets.

## Installation

Here is how to install Ultyas locally to `~/.local/bin/ultyas` using [pip](https://pypi.org/project/pip/):
```
pip install --user ultyas
```

The command above will install Ultyas in the local directory: `~/.local/bin/ultyas`.

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
  ultisnips_file        The UltiSnips .snippets file
                        (e.g. '~/.vim/UltiSnips/python.snippets')

options:
  -h, --help            show this help message and exit
  -o YASNIPPET_DIR, --yasnippet-dir YASNIPPET_DIR
                        The YASnippet snippets major mode directory
                        (e.g. '~/.emacs.d/snippets/python-mode/')
  -i {auto,fixed,nothing}, --yas-indent-line {auto,fixed,nothing}
                        Add one of the following comments to the YASnippet
                        snippets that will be generated:
                        "# expand-env: ((yas-indent-line 'fixed))" or
                        "# expand-env: ((yas-indent-line 'auto))".
  -t CONVERT_TABS_TO, --convert-tabs-to CONVERT_TABS_TO
                        Convert the tabs that are in the generated
                        snippets to the string passed to this
                        option (Default: The indentation marker '$>')
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

## Frequently Asked Questions

### How does the author use Ultyas?

The author maintains all snippets in the original UltiSnips format for Vim and uses [Ultyas](https://github.com/jamescherti/ultyas) to convert them automatically to Yasnippet format for Emacs.

He uses [ultisnips-mode.el](https://github.com/jamescherti/ultisnips-mode.el) in Emacs to edit snippets, providing syntax highlighting and code folding through **hs-minor-mode**.

This workflow allows editing and storing a single set of snippets while making them available in Vim and Emacs.

(The author wrote a shell script that automatically scans the UltiSnips directory and generates the corresponding Yasnippet files whenever snippets are updated, ensuring synchronization between Vim and Emacs.)

## License

The `ultyas` Emacs package has been written by [James Cherti](https://www.jamescherti.com/) and is distributed under terms of the GNU General Public License version 3, or, at your choice, any later version.

Copyright (C) 2023-2026 James Cherti

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.

## Links

- [Ultyas @GitHub](https://github.com/jamescherti/ultyas/)
- [Ultyas @PyPI](https://pypi.org/project/ultyas/)
- Syntax highlighting: [ultisnips-mode.el @GitHub](https://github.com/jamescherti/ultisnips-mode.el), an Emacs major mode for editing Ultisnips snippet files. This mode provides syntax highlighting to facilitate editing Ultisnips snippets.

Other Emacs packages by the same author:
- [minimal-emacs.d](https://github.com/jamescherti/minimal-emacs.d): This repository hosts a minimal Emacs configuration designed to serve as a foundation for your vanilla Emacs setup and provide a solid base for an enhanced Emacs experience.
- [compile-angel.el](https://github.com/jamescherti/compile-angel.el): **Speed up Emacs!** This package guarantees that all .el files are both byte-compiled and native-compiled, which significantly speeds up Emacs.
- [outline-indent.el](https://github.com/jamescherti/outline-indent.el): An Emacs package that provides a minor mode that enables code folding and outlining based on indentation levels for various indentation-based text files, such as YAML, Python, and other indented text files.
- [easysession.el](https://github.com/jamescherti/easysession.el): Easysession is lightweight Emacs session manager that can persist and restore file editing buffers, indirect buffers/clones, Dired buffers, the tab-bar, and the Emacs frames (with or without the Emacs frames size, width, and height).
- [vim-tab-bar.el](https://github.com/jamescherti/vim-tab-bar.el): Make the Emacs tab-bar Look Like Vim’s Tab Bar.
- [elispcomp](https://github.com/jamescherti/elispcomp): A command line tool that allows compiling Elisp code directly from the terminal or from a shell script. It facilitates the generation of optimized .elc (byte-compiled) and .eln (native-compiled) files.
- [tomorrow-night-deepblue-theme.el](https://github.com/jamescherti/tomorrow-night-deepblue-theme.el): The Tomorrow Night Deepblue Emacs theme is a beautiful deep blue variant of the Tomorrow Night theme, which is renowned for its elegant color palette that is pleasing to the eyes. It features a deep blue background color that creates a calming atmosphere. The theme is also a great choice for those who miss the blue themes that were trendy a few years ago.
- [dir-config.el](https://github.com/jamescherti/dir-config.el): Automatically find and evaluate .dir-config.el Elisp files to configure directory-specific settings.
- [flymake-bashate.el](https://github.com/jamescherti/flymake-bashate.el): A package that provides a Flymake backend for the bashate Bash script style checker.
- [flymake-ansible-lint.el](https://github.com/jamescherti/flymake-ansible-lint.el): An Emacs package that offers a Flymake backend for ansible-lint.
- [inhibit-mouse.el](https://github.com/jamescherti/inhibit-mouse.el): A package that disables mouse input in Emacs, offering a simpler and faster alternative to the disable-mouse package.
- [quick-sdcv.el](https://github.com/jamescherti/quick-sdcv.el): This package enables Emacs to function as an offline dictionary by using the sdcv command-line tool directly within Emacs.
- [enhanced-evil-paredit.el](https://github.com/jamescherti/enhanced-evil-paredit.el): An Emacs package that prevents parenthesis imbalance when using *evil-mode* with *paredit*. It intercepts *evil-mode* commands such as delete, change, and paste, blocking their execution if they would break the parenthetical structure.
- [stripspace.el](https://github.com/jamescherti/stripspace.el): Ensure Emacs Automatically removes trailing whitespace before saving a buffer, with an option to preserve the cursor column.
- [persist-text-scale.el](https://github.com/jamescherti/persist-text-scale.el): Ensure that all adjustments made with text-scale-increase and text-scale-decrease are persisted and restored across sessions.
- [pathaction.el](https://github.com/jamescherti/pathaction.el): Execute the pathaction command-line tool from Emacs. The pathaction command-line tool enables the execution of specific commands on targeted files or directories. Its key advantage lies in its flexibility, allowing users to handle various types of files simply by passing the file or directory as an argument to the pathaction tool. The tool uses a .pathaction.yaml rule-set file to determine which command to execute. Additionally, Jinja2 templating can be employed in the rule-set file to further customize the commands.
- [kirigami.el](https://github.com/jamescherti/kirigami.el): The *kirigami* Emacs package offers a unified interface for opening and closing folds across a diverse set of major and minor modes in Emacs, including `outline-mode`, `outline-minor-mode`, `outline-indent-mode`, `org-mode`, `markdown-mode`, `vdiff-mode`, `vdiff-3way-mode`, `hs-minor-mode`, `hide-ifdef-mode`, `origami-mode`, `yafolding-mode`, `folding-mode`, and `treesit-fold-mode`. With Kirigami, folding key bindings only need to be configured **once**. After that, the same keys work consistently across all supported major and minor modes, providing a unified and predictable folding experience.
