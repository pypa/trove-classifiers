"""test_cli.py - Tests to confirm that the CLI works and that both running the module and
calling the entry point produce equivalent output.
"""

import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path
from typing import Optional

import pytest


def _get_entry_point() -> Optional[str]:
    exe = shutil.which("trove-classifiers")
    if exe:
        return exe
    candidates = [
        Path(sysconfig.get_path("scripts")),
        Path(sys.executable).parent,
        Path(sys.executable).parent / "Scripts",
        Path(sys.executable).parent / "bin",
    ]
    for candidate_dir in candidates:
        exe = shutil.which("trove-classifiers", path=str(candidate_dir))
        if exe:
            return exe
    return None


def test_module_run():
    """Simple test for no error when running the module. Output is not validated."""
    subprocess.check_call([sys.executable, "-m", "trove_classifiers"])


def test_entry_point():
    """Simple test for no error when calling the entry point. Output is not validated."""
    entry_point = _get_entry_point()
    if not entry_point:
        pytest.skip(
            "trove-classifiers CLI entry point not found in PATH or scripts directory"
        )
    subprocess.check_call([entry_point])


def test_module_run_is_entry_point():
    """Compare that module run output is the same as entry point output."""
    entry_point = _get_entry_point()
    if not entry_point:
        pytest.skip(
            "trove-classifiers CLI entry point not found in PATH or scripts directory"
        )
    module_run_proc = subprocess.run(
        [sys.executable, "-m", "trove_classifiers"],
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    entry_point_proc = subprocess.run(
        [entry_point],
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    assert module_run_proc.stdout == entry_point_proc.stdout
