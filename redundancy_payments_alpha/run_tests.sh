set -oe pipefail

PATH=$PATH:$(pwd)

nosetests --exe

behave --tags=-wip --stop feature_tests/

