# Contributing
How to contributing to this package.

## Running tests
Run `make tests`. This checks whether the auto-generated list of classifiers
matches the input source.

## Running linting
Run `make lint`.

## Rebuilding the auto-generated list of classifiers
Run `make build`.

## Adding a new classifier
To add a new classifier, edit `_internal/classifiers.py`, then rebuild the
compiled list of classifiers with `make build`.

## Deprecating a classifier
To deprecate a classifier, move it from `classifiers` to
`deprecated_classifiers` in `_internal/classifiers.py`, and list any new
classifiers that may replace it.
