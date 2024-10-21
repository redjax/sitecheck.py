"""Nox sessions definition file.

Description:
    ['nox'](https://astral.sh) is a task runner like `tox`. `nox` sessions are written in
    regular Python code, making the session API familiar & extremely flexible.
    
    Sessions are cross-platform, meaning they can be run on Windows, Linux, Mac, even CI pipelines
    like Github Actions.
    
Usage:
    - List available sessions with `nox -l`
    - Run all sessions defined in `nox.sessions` list
    - Run a specific `nox` sessions with `nox -s <session-name>`
"""

from __future__ import annotations

import importlib.util
import logging
from pathlib import Path

log: logging.Logger = logging.getLogger(__name__)

import nox

## Set nox options
if importlib.util.find_spec("uv"):
    nox.options.default_venv_backend = "uv|virtualenv"
else:
    nox.options.default_venv_backend = "virtualenv"
nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_external_run = False
nox.options.error_on_missing_interpreters = False
# nox.options.report = True

## Define sessions to run when no session is specified
nox.sessions = ["lint", "tests"]

## Define versions to test
PY_VERSIONS: list[str] = ["3.12", "3.11"]

## Set paths to lint with the lint session
LINT_PATHS: list[str] = ["sitecheck.py", "tests"]


def install_uv_project(session: nox.Session, external: bool = False) -> None:
    """Method to install uv and the current project in a nox session."""
    log.info("Installing uv in session")
    session.install("uv")

    log.info("Syncing uv project")
    session.run("uv", "sync", external=external, env={"PYTHON_VERSION": session.python})

    log.info("Installing project")
    session.run(
        "uv",
        "pip",
        "install",
        ".",
        external=external,
        env={"PYTHON_VERSION": session.python},
    )


@nox.session(name="dev-environment", tags=["setup"])
def setup_dev_environment(session: nox.Session) -> None:
    """Creates the `uv` environment, setting up a `.venv` and installing dependencies."""
    install_uv_project(session=session)


@nox.session(name="lint", tags=["quality"])
def run_linter(session: nox.Session) -> None:
    """Run session to lint & format code."""
    install_uv_project(session=session)

    log.info("Linting code")

    ## Loop directories in LINT_PATHS variable
    for d in LINT_PATHS:
        if not Path(d).exists():
            ## lint path not found
            log.warning(f"Skipping lint path '{d}', could not find path")
            pass
        else:
            lint_path: Path = Path(d)

            ## Sort import statements
            log.info(f"Running ruff imports sort on '{d}'")
            session.run(
                "ruff",
                "check",
                lint_path,
                "--select",
                "I",
                "--fix",
            )

            ## Lint code with ruff
            log.info(f"Running ruff checks on '{d}' with --fix")
            session.run(
                "ruff",
                "check",
                lint_path,
                "--fix",
            )

    ## Always lint noxfile.py
    log.info("Linting noxfile.py")
    session.run(
        "ruff",
        "check",
        f"{Path('./noxfile.py')}",
        "--fix",
    )


@nox.session(python=PY_VERSIONS, name="tests", tags=["test", "quality"])
def run_tests(session: nox.Session) -> None:
    """Run pytest tests with `pytest-xdist` for concurrent test execution."""
    install_uv_project(session=session)

    ## Ensure pytest-xdist is installed
    log.info("Install pytest-xdist for concurrent test execution")
    session.install("pytest-xdist")

    ## Run tests with pytest-xdist, running multiple tests at once
    log.info("Running Pytest tests")
    session.run(
        "uv",
        "run",
        "pytest",
        "-n",
        "auto",
        "--tb=native",
        "-v",
        "-rasXxfP",
    )
