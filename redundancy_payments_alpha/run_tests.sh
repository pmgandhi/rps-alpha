set -o pipefail

nosetests

behave --stop feature_tests/

