from argparse import ArgumentParser
from typing import Optional, Sequence

from trove_classifiers import sorted_classifiers


def cli(argv: Optional[Sequence[str]] = None) -> None:
    parser = ArgumentParser(
        prog="trove-classifiers",
        description="List all valid trove classifiers, one per line.",
    )
    parser.parse_args(argv)
    for classifier in sorted_classifiers:
        print(classifier)


if __name__ == "__main__":
    cli()
