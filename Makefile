BINDIR = $(PWD)/.state/env/bin

.state/env/pyvenv.cfg: requirements/dev.txt
	rm -rf .state/env
	python -m venv .state/env

	# install/upgrade general requirements
	$(BINDIR)/python -m pip install --upgrade pip setuptools wheel

	# install various types of requirements
	$(BINDIR)/python -m pip install -r requirements/dev.txt

test: .state/env/pyvenv.cfg
	$(BINDIR)/python -m pip install .
	$(BINDIR)/pytest
	$(BINDIR)/python -m tests.lib

lint: .state/env/pyvenv.cfg
	$(BINDIR)/black --check bin setup.py src tests
	$(BINDIR)/python bin/sort.py src/trove_classifiers/__init__.py
	$(BINDIR)/mypy src

reformat: .state/env/pyvenv.cfg
	$(BINDIR)/black tests src

.PHONY: build test lint reformat
