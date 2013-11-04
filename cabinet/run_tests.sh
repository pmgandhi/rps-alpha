#!/usr/bin/env bash

set -e

PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python -m unittest discover $PROJECT_ROOT
