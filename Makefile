BINDIR = $(PWD)/.state/env/bin

.state/env/pyvenv.cfg: requirements/dev.txt
	rm -rf .state/env
	python -m venv .state/env

	# install/upgrade general requirements
	$(BINDIR)/python -m pip install --upgrade pip setuptools wheel

	# install various types of requirements
	$(BINDIR)/python -m pip install -r requirements/dev.txt

build: .state/env/pyvenv.cfg
	$(BINDIR)/python _internal/generator.py

test: .state/env/pyvenv.cfg
	$(BINDIR)/pytest
	$(eval TMPDIR := $(shell mktemp -d))
	$(BINDIR)/python _internal/generator.py --output $(TMPDIR)/test.py
	diff trove_classifiers/__init__.py $(TMPDIR)/test.py

lint: .state/env/pyvenv.cfg
	$(BINDIR)/black --check _internal tests

reformat: .state/env/pyvenv.cfg
	$(BINDIR)/black _internal tests

.PHONY: build test lint reformat
