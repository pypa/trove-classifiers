import ast
import sys

from natsort import natsorted


def _test_sort(elements, _type):
    values = [e.value for e in elements]
    for wrong, right in zip(values, natsorted(values)):
        if wrong != right:
            print(f"{_type} is not sorted, {right!r} should come before {wrong!r}")
            return True
    return False


if len(sys.argv) == 1:
    print("Usage: sort.py [filename]")
    sys.exit(1)


with open(sys.argv[1]) as f:
    contents = f.read()

fail = False

for node in ast.walk(ast.parse(contents)):
    if type(node) == ast.List:
        fail = _test_sort(node.elts, "List") or fail
    if type(node) == ast.Set:
        fail = _test_sort(node.elts, "Set") or fail
    if type(node) == ast.Dict:
        fail = _test_sort(node.keys, "Dict") or fail

sys.exit(fail)
