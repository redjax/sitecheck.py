# sitecheck.py

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/redjax/sitecheck.py/nox-sessions.yml?style=for-the-badge&label=tests)

A script to check availability of a remote site. Uses only `stdlib` packages. You should be able to just copy/paste the contents of [`sitecheck.py`](./sitecheck.py) into a script on your local machine to run (no need to clone the whole repository).

The project is managed with [`astral uv`](https://astral.sh/uv). This is just for linting & tests, the script itself does not require dependency installation. `uv` is only for development.
