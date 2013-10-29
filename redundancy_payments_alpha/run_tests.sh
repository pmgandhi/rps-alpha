set -oe pipefail

PATH=$PATH:$(pwd)

nosetests --exe

behave --stop feature_tests/

