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


def test_cli_lists_classifiers(capsys):
    """Calling the entry point without arguments lists the classifiers."""
    from trove_classifiers.__main__ import cli

    cli([])
    out, _ = capsys.readouterr()
    assert "Development Status :: 1 - Planning" in out.splitlines()


def test_cli_rejects_unexpected_arguments():
    """Unexpected arguments fail with a usage error instead of being ignored."""
    import pytest

    from trove_classifiers.__main__ import cli

    with pytest.raises(SystemExit) as excinfo:
        cli(["--bogus"])
    assert excinfo.value.code == 2
