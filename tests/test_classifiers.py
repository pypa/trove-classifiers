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

    assert [node.full_name for node in root.generate()] == [
        "Foo",
        "Foo :: Bar",
        "Foo :: Bar :: Baz",
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

    assert [node.full_name for node in root.generate()] == [
        "Foo :: Bar",
        "Foo :: Bar :: Baz",
    ]


def test_bad_deprecation_failure():
    with pytest.raises(InvalidClassifier) as excinfo:
        ClassifierNode("blah", deprecated_by=["spam"])

    assert excinfo.value.args == (
        "Using deprecated_by, but not marking the classifier as deprecated",
    )


@pytest.mark.parametrize(
    "parent, child",
    [("Private", "Foo"), ("private", "Foo"), ("Foo", "Private"), ("Foo", "private"),],
)
def test_private_classifier_failure(parent, child):
    with pytest.raises(InvalidClassifier) as excinfo:
        ClassifierNode(
            parent, children=[ClassifierNode(child)],
        )

    assert excinfo.value.args == ("Classifiers starting with 'Private' are invalid",)
