import pytest

from tester import trove_tester, InvalidClassifier


def test_success():
    classifiers = {
        "Foo :: Bar",
        "Foo :: Bar :: Baz",
    }
    trove_tester(classifiers)


def test_top_level_failure():
    classifiers = {
        "Foo",
        "Foo :: Bar",
        "Foo :: Bar :: Baz",
    }

    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester(classifiers)

    assert excinfo.value.args == ("Top-level classifier 'Foo' is invalid",)


def test_high_level_classifier_missing_failure():
    classifiers = {
        "Foo :: Bar :: Baz",
    }

    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester(classifiers)

    assert excinfo.value.args == ("Classifier 'Foo :: Bar' is missing",)


def test_bad_deprecation_failure():
    classifiers = {
        "Foo :: Bar",
    }
    deprecated_classifiers = {"Biz :: Baz": ["Bing :: Bang"]}

    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester(classifiers, deprecated_classifiers)

    assert excinfo.value.args == ("Classifier 'Bing :: Bang' does not exist",)


def test_bad_deprecation_failure():
    classifiers = {
        "Foo :: Bar",
    }
    deprecated_classifiers = {"Foo :: Bar": []}

    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester(classifiers, deprecated_classifiers)

    assert excinfo.value.args == (
        "Classifier 'Foo :: Bar' in both valid and deprecated classifiers",
    )


@pytest.mark.parametrize(
    "classifier",
    ["Private :: Foo", "private :: Foo", "Foo :: Private", "Foo :: private"],
)
def test_private_classifier_failure(classifier):
    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester({classifier})

    assert excinfo.value.args == ("Classifiers starting with 'Private' are invalid",)


@pytest.mark.parametrize("classifier", [" Foo :: Bar", "Foo :: Bar "])
def test_whitespace_classifier_failure(classifier):
    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester({classifier})

    assert excinfo.value.args == (
        "Classifiers starting or ending with whitespace are invalid",
    )


@pytest.mark.parametrize(
    "classifier", ["Foo: :: Bar", "Foo :: B:ar", "Foo :: Bar: Baz"]
)
def test_colon_classifier_failure(classifier):
    with pytest.raises(InvalidClassifier) as excinfo:
        trove_tester({classifier})

    assert excinfo.value.args == ("Classifiers containing ':' are invalid",)
