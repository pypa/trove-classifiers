class ClassifierRoot:
    def __init__(self, children):
        self.children = children
        self.skip = True

    def generate(self):
        def recurse(classifier):
            if not classifier.skip:
                yield classifier
            for child in classifier.children:
                yield from recurse(child)

        return sorted(recurse(self), key=lambda c: c.full_name)


class ClassifierNode:
    def __init__(
        self,
        short_name,
        children=None,
        deprecated=False,
        deprecated_by=None,
        skip=False,
    ):
        if deprecated_by and not deprecated:
            raise Exception(
                "Using deprecated_by, but not marking the classifier as deprecated"
            )

        self.short_name = short_name
        self.prefix_list = []
        self.deprecated = deprecated
        self.deprecated_by = deprecated_by if deprecated_by else []
        self.children = children if children else []
        self.skip = skip

        for child in self.children:
            child.add_prefix(self.full_name)

    def __repr__(self):
        if self.deprecated:
            return f'Classifier(full_name="{self.full_name}", short_name="{self.short_name}", deprecated={self.deprecated}, deprecated_by={self.deprecated_by})'
        return (
            f'Classifier(full_name="{self.full_name}", short_name="{self.short_name}")'
        )

    @property
    def full_name(self):
        return " :: ".join(self.prefix_list + [self.short_name])

    def add_prefix(self, prefix):
        self.prefix_list = [prefix] + self.prefix_list
        for child in self.children:
            child.add_prefix(prefix)

    def __eq__(self, other):
        return all(
            [
                self.full_name == other.full_name,
                self.deprecated == other.deprecated,
                self.deprecated_by == other.deprecated_by,
            ]
        )
