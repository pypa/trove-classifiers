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
	$(BINDIR)/python -m tester

lint: .state/env/pyvenv.cfg
	$(BINDIR)/black --check tests tester trove_classifiers

reformat: .state/env/pyvenv.cfg
	$(BINDIR)/black tests tester trove_classifiers

.PHONY: build test lint reformat
