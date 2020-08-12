# Contributing
How to contributing to this package.

## Running tests
Run `make test`. This checks whether the auto-generated list of classifiers
matches the input source.

## Running linting
Run `make lint`.

## Adding a new classifier
To add a new classifier, add to the `classifiers` set in
`trove_classifiers/__init__.py`.

## Deprecating a classifier
To deprecate a classifier, move it from `classifiers` to
`deprecated_classifiers` in `trove_classifiers/__init__.py`, and list any new
classifiers that may replace it.
