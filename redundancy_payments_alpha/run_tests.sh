#!/usr/bin/env bash

set -oe pipefail

PATH=$PATH:$(pwd)

nosetests --exe

behave -q --tags=-wip --stop feature_tests/
