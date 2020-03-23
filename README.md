Cannonical source for classifiers on [PyPI](https://pypi.org).

## Usage
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
