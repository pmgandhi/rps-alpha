#!/usr/bin/env bash

set -oe pipefail

PATH=$PATH:$(pwd)

#python -m unittest discover .

behave -q --tags=-wip --stop feature_tests/
