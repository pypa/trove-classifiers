BINDIR = $(PWD)/.state/env/bin

.state/env/pyvenv.cfg: requirements/dev.txt
	rm -rf .state/env
	python -m venv .state/env

	# install/upgrade general requirements
	$(BINDIR)/python -m pip install --upgrade pip setuptools wheel

	# install various types of requirements
	$(BINDIR)/python -m pip install -r requirements/dev.txt

test: .state/env/pyvenv.cfg
	$(BINDIR)/pytest
	$(BINDIR)/python -m tests.lib

lint: .state/env/pyvenv.cfg
	$(BINDIR)/black --check tests trove_classifiers
	$(BINDIR)/python bin/sort.py trove_classifiers/__init__.py

reformat: .state/env/pyvenv.cfg
	$(BINDIR)/black tests trove_classifiers

.PHONY: build test lint reformat
