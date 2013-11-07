#!/usr/bin/env bash

set -oe pipefail

PATH=$PATH:$(pwd)

nosetests --exe --with-xunit

behave -q --tags=-wip --stop feature_tests/
