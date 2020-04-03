Canonical source for [classifiers](https://pypi.org/classifiers/) on
[PyPI](https://pypi.org). Classifiers [categorize
projects](https://packaging.python.org/specifications/core-metadata/#classifier-multiple-use)
per [PEP 301](https://www.python.org/dev/peps/pep-0301/). Use this
package to validate classifiers in packages for PyPI upload or
download.

## Usage

To install [from PyPI](https://pypi.org/project/trove-classifiers/):

```
> pip install trove-classifiers
```

This package's API is two importable objects:

### Classifiers (`trove_classifiers.classifiers`)
A `set` containing classifiers (as strings). Useful for determining membership

Example - determine if a classifier is valid:

```python
>>> from trove_classifiers import classifiers
>>> 'License :: OSI Approved' in classifiers
True
>>> 'Fuzzy :: Wuzzy :: Was :: A :: Bear' in classifiers
False
>>>
```

### Deprecated classifiers (`trove_classifiers.deprecated_classifiers`)
A `dict`, mapping a deprecated classifier (string) to a list of classifiers
which replaces it (strings).

Example - determine if a classifier is deprecated:

```python
>>> from trove_classifiers import deprecated_classifiers
>>> 'License :: OSI Approved' in deprecated_classifiers
False
>>> 'Natural Language :: Ukranian' in deprecated_classifiers
True
>>> deprecated_classifiers["Natural Language :: Ukranian"]
['Natural Language :: Ukrainian']
```
