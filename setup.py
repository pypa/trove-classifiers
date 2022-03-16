from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="trove-classifiers",
    description="Canonical source for classifiers on PyPI (pypi.org).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/trove-classifiers",
    author="The PyPI Admins",
    author_email="admin@pypi.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Typing :: Typed",
    ],
    keywords="classifiers",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={"": ["py.typed"]},
    use_calver=True,
    setup_requires=["calver"],
)
