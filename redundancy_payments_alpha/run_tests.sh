#!/usr/bin/env bash

set -oe pipefail

PATH=$PATH:$(pwd)

if [ -z "$VIRTUAL_ENV" -a -n "$WORKON_HOME" ]; then
  basedir=$(dirname $0)
  venvdir=$WORKON_HOME/$(basename $(cd $(dirname $0) && pwd -P))

  if [ ! -d "$venvdir" ]; then
    virtualenv $venvdir
  fi

  source "$venvdir/bin/activate"

  pip install -r requirements.dev.txt
fi

nosetests --exe --with-xunit

behave -q --tags=-wip --stop feature_tests/
