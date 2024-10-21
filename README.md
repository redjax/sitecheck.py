# sitecheck.py

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/redjax/sitecheck.py/nox-sessions.yml?style=for-the-badge&label=tests)

A script to check availability of a remote site. Uses only `stdlib` packages. You should be able to just copy/paste the contents of [`sitecheck.py`](./sitecheck.py) into a script on your local machine to run (no need to clone the whole repository).

The project is managed with [`astral uv`](https://astral.sh/uv). This is just for linting & tests, the script itself does not require dependency installation. `uv` is only for development.

## Installation

### Clone repository

***WIP***

### Pex (Python executable)

```warning
----------------------------------------------------------------------------------------------------------------------
| !! Do not install the .pex file at release/sitecheck.pex until this notice is removed. Read below for more info !! |
----------------------------------------------------------------------------------------------------------------------

Until I create a pipeline and release through Github with auditable builds, I do not recommend downloading the pex file in the release/ directory. I am compiling this .pex file on my own machine using the nox session (in noxfile.py) "build-compile-pex".

However, I can't "prove" that this is how each release is built without a Github Action pipeline with auditable build steps, and an "official" release through Github.

You can build a .pex file from source on your own machine by cloning this repository and running "uv run nox -s build-compile-pex"

This message will remain up until that pipeline is finished.
```

- Download the [`sitecheck.pex`](./release/sitecheck.pex) file from [`release/`](./release/).
  - This is a compiled, static binary with a CLI, so you can use it from the command line.
  - `.pex` binaries only work on Unix systems, Windows support is fleeting & limited. The `.pex` file for this project most likely does not work on Windows.
- Run the `.pex` file like you would any other binary, i.e. `./sitecheck.pex --site https://www.google.com`.
- See a help menu with `./sitecheck.pex --help`
- Add it to your `$PATH` by placing the `.pex` somewhere on your `$PATH`
