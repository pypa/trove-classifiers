import argparse
import os
import datetime

from jinja2 import Template

from classifiers import classifiers

parser = argparse.ArgumentParser()
parser.add_argument(
    "--output", default=os.path.join("trove_classifiers", "__init__.py")
)
args = parser.parse_args()

this_dir, _ = os.path.split(__file__)

with open(os.path.join(this_dir, "templates", "__init__.py.jinja2")) as f:
    template = Template(f.read())

template.globals["now"] = datetime.datetime.utcnow

with open(args.output, "w") as f:
    all_classifiers = classifiers.generate()
    classifiers = [c for c in all_classifiers if not c.deprecated]
    deprecated_classifiers = [c for c in all_classifiers if c.deprecated]
    f.write(
        template.render(
            classifiers=classifiers, deprecated_classifiers=deprecated_classifiers
        )
    )
