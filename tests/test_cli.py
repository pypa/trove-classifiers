"""test_cli.py - Tests to confirm that the CLI works and that both running the module and
calling the entry point produce equivalent output.
"""

import subprocess


def test_module_run():
    """Simple test for no error when running the module. Output is not validated."""
    subprocess.check_call(["python", "-m", "trove_classifiers"])


def test_entry_point():
    """Simple test for no error when calling the entry point. Output is not validated."""
    subprocess.check_call("trove-classifiers")


def test_module_run_is_entry_point():
    module_run_proc = subprocess.run(
        ["python", "-m", "trove_classifiers"], capture_output=True, encoding="utf-8"
    )
    entry_point_proc = subprocess.run(
        "trove-classifiers", capture_output=True, encoding="utf-8"
    )
    assert module_run_proc.stdout == entry_point_proc.stdout
