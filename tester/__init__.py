class InvalidClassifier(Exception):
    pass


def trove_tester(classifiers, deprecated_classifiers):
    # Check the classifiers
    for classifier in classifiers:
        split = classifier.split(" :: ")

        # Check if this is an invalid top-level classifier
        if len(split) == 1:
            raise InvalidClassifier(f"Top-level classifier {classifier!r} is invalid")

        # Check if all parent classifiers are specified
        for i in range(2, len(split)):
            parent = " :: ".join(split[:i])
            if parent not in classifiers:
                raise InvalidClassifier(f"Classifier {parent!r} is missing")

        # Check the sub-classifiers
        for sub in split:

            # Check for whitespace
            if sub.strip().rstrip() != sub:
                raise InvalidClassifier(
                    "Classifiers starting or ending with whitespace are invalid"
                )

            # Check for private classifiers
            if sub.lower().startswith("private"):
                raise InvalidClassifier(
                    "Classifiers starting with 'Private' are invalid"
                )

            # Check for stray colons
            if ":" in sub:
                raise InvalidClassifier("Classifiers containing ':' are invalid")

    # Check the deprecated classifiers
    for deprecated_classifier, deprecated_by in deprecated_classifiers.items():

        # Check if the classifier is in both lists
        if deprecated_classifier in classifiers:
            raise InvalidClassifier(
                f"Classifier {deprecated_classifier!r} in both valid and deprecated classifiers"
            )

        # Check if all deprecated_by classifiers exist
        for new_classifier in deprecated_by:
            if new_classifier not in classifiers:
                raise InvalidClassifier(f"Classifier {new_classifier!r} does not exist")

    print("All classifiers passed :)")
