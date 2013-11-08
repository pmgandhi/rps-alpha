#!/usr/bin/env bash

set -oe pipefail

PATH=$PATH:$(pwd)

./ensure_clean_tables

behave -q --tags=-wip --stop feature_tests/
