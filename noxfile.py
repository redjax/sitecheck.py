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
import platform
import glob

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

OS_TYPE = platform.system()


def install_uv_project(session: nox.Session, external: bool = False) -> None:
    """Method to install uv and the current project in a nox session."""
    log.info("Installing uv in session")
    session.install("uv")

    log.info("Syncing uv project")
    session.run("uv", "sync", external=external, env={"PYTHON_VERSION": session.python})


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


@nox.session(name="compile-pex", tags=["pex"])
def compile_pex(session: nox.Session) -> None:
    """Compile script into a pex file (self-contained executable)."""
    if OS_TYPE == "Windows":
        log.warning("Compiling to .pex is not compatible with Windows.")

        return

    install_uv_project(session)

    SCRIPT_PATH: Path = Path("./sitecheck.py")
    SCRIPT_NAME: str = SCRIPT_PATH.stem
    PEX_OUTPUT: Path = Path("./dist/sitecheck.pex")

    if not PEX_OUTPUT.parent.exists():
        try:
            PEX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            msg = f"({type(exc)}) Error creating path '{PEX_OUTPUT.parent}'. Details: {exc}"
            log.error(msg)

            return

    log.info("Compiling script into .pex file")
    session.run("uv", "run", "pex", ".", "-m", SCRIPT_NAME, "-o", PEX_OUTPUT)


@nox.session(name="build-compile-pex", tags=["pex"])
def build_compile_pex(session: nox.Session) -> None:
    """Compile script into a pex file (self-contained executable)."""
    if OS_TYPE == "Windows":
        log.warning("Compiling to .pex is not compatible with Windows.")
        return

    install_uv_project(session)
    log.info(f"Install Python {platform.python_version()}")
    session.run("uv", "python", "install", platform.python_version())
    log.info("Building project before compiling to .pex")
    session.run("uv", "build")
    log.info("Ensure pex is installed")
    session.install("pex")

    PEX_MODULE_STR: str = "sitecheck:main"
    PEX_OUTPUT: Path = Path("./release/sitecheck.pex")

    if not PEX_OUTPUT.parent.exists():
        try:
            PEX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            msg = f"({type(exc)}) Error creating path '{PEX_OUTPUT.parent}'. Details: {exc}"
            log.error(msg)
            return

    log.info("Compiling script into .pex file")
    try:
        # Use glob to find all .whl files in the dist directory
        whl_files = glob.glob("dist/*.whl")
        if not whl_files:
            log.error("No .whl files found in the dist directory.")
            return

        session.run("pex", *whl_files, "-o", str(PEX_OUTPUT), "-m", PEX_MODULE_STR)
    except Exception as exc:
        msg = f"({type(exc)}) Error compiling script to .pex file. Details: {exc}"
        log.error(msg)


@nox.session(name="vulture-check", tags=["coverage", "quality"])
def vulture_check(session: nox.Session):
    install_uv_project(session)

    log.info("Installing vulture for dead code checking")
    session.install("vulture")

    log.info("Running vulture")
    session.run("vulture")
