import pytest

from trove_classifiers import classifiers_sorted
from tests.lib import trove_tester, InvalidClassifier


@pytest.mark.parametrize(
    "classifiers, deprecated_classifiers",
    [
        (
            {
                "Foo :: Bar",
                "Foo :: Bar :: Baz",
            },
            {},
        ),
        ({"Foo :: Bar"}, {"Biz :: Baz": ["Foo :: Bar"]}),
    ],
)
def test_success(classifiers, deprecated_classifiers):
    trove_tester(classifiers, deprecated_classifiers)


@pytest.mark.parametrize(
    "classifiers, deprecated_classifiers, expected",
    [
        (
            {"Foo", "Foo :: Bar"},
            {},
            "Top-level classifier 'Foo' is invalid",
        ),
        ({"Foo :: Bar :: Baz"}, {}, "Classifier 'Foo :: Bar' is missing"),
        (
            {
                "Foo :: Bar",
            },
            {"Biz :: Baz": ["Bing :: Bang"]},
            "Classifier 'Bing :: Bang' does not exist",
        ),
        (
            {
                "Foo :: Bar",
            },
            {"Foo :: Bar": []},
            "Classifier 'Foo :: Bar' in both valid and deprecated classifiers",
        ),
        ({"Private :: Foo"}, {}, "Classifiers starting with 'Private' are invalid"),
        ({"private :: Foo"}, {}, "Classifiers starting with 'Private' are invalid"),
        ({"Foo :: Private"}, {}, "Classifiers starting with 'Private' are invalid"),
        ({"Foo :: private"}, {}, "Classifiers starting with 'Private' are invalid"),
        (
            {" Foo :: Bar"},
            {},
            "Classifiers starting or ending with whitespace are invalid",
        ),
        (
            {"Foo :: Bar "},
            {},
            "Classifiers starting or ending with whitespace are invalid",
        ),
        (
            {"Foo: :: Bar"},
            {},
            "Classifiers containing ':' are invalid",
        ),
        (
            {"Foo :: B:ar"},
            {},
            "Classifiers containing ':' are invalid",
        ),
        (
            {"Foo :: Bar: Baz"},
            {},
            "Classifiers containing ':' are invalid",
        ),
    ],
)
def test_failure(classifiers, deprecated_classifiers, expected):
    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester(classifiers, deprecated_classifiers)

    assert excinfo.value.args == (expected,)


def test_sort():
    # Arrange
    # In lexicographical order: 3.1, 3.10, 3.2
    classifiers = {
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    }

    # Act
    output = classifiers_sorted(classifiers)

    # Assert
    # With sorted version numbers: 3.8, 3.9, 3.10
    assert output == [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
