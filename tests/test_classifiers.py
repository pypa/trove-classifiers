import pytest

from _internal.models import ClassifierRoot, ClassifierNode
from _internal.exceptions import InvalidClassifier


def test_nested_prefixes():
    root = ClassifierRoot(
        children=[
            ClassifierNode(
                "Foo",
                children=[ClassifierNode("Bar", children=[ClassifierNode("Baz")])],
            )
        ]
    )

    assert root.generate() == [
        ClassifierNode("Foo"),
        ClassifierNode("Foo :: Bar"),
        ClassifierNode("Foo :: Bar :: Baz"),
    ]


def test_skip():
    root = ClassifierRoot(
        children=[
            ClassifierNode(
                "Foo",
                skip=True,
                children=[ClassifierNode("Bar", children=[ClassifierNode("Baz")])],
            )
        ]
    )

    assert root.generate() == [
        ClassifierNode("Foo :: Bar"),
        ClassifierNode("Foo :: Bar :: Baz"),
    ]


def test_bad_deprecation_failure():
    with pytest.raises(InvalidClassifier) as excinfo:
        ClassifierNode("blah", deprecated_by=["spam"])

    assert excinfo.value.args == (
        "Using deprecated_by, but not marking the classifier as deprecated",
    )
