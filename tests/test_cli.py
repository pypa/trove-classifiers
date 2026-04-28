"""test_cli.py - Tests to confirm that the CLI works and that both running the module and
calling the entry point produce equivalent output.
"""

import subprocess
import sys
from pathlib import Path

BINDIR = Path(sys.executable).parent


def test_module_run():
    """Simple test for no error when running the module. Output is not validated."""
    subprocess.check_call([sys.executable, "-m", "trove_classifiers"])


def test_entry_point():
    """Simple test for no error when calling the entry point. Output is not validated."""
    subprocess.check_call(f"{BINDIR}/trove-classifiers")


def test_module_run_is_entry_point():
    """Compare that module run output is the same as entry point output."""
    module_run_proc = subprocess.run(
        [sys.executable, "-m", "trove_classifiers"],
        capture_output=True,
        encoding="utf-8",
    )
    entry_point_proc = subprocess.run(
        f"{BINDIR}/trove-classifiers", capture_output=True, encoding="utf-8"
    )
    assert module_run_proc.stdout == entry_point_proc.stdout
