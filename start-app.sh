#!/bin/bash

# If you're not already in a virtualenv and you're using virtualenvwrapper
if [ -z "$VIRTUAL_ENV" -a -n "$WORKON_HOME" ]; then
  basedir=$(dirname $0)
  venvdir=$WORKON_HOME/$(basename $(cd $(dirname $0) && pwd -P))

  if [ ! -d "$venvdir" ]; then
    virtualenv $venvdir
  fi

  source "$venvdir/bin/activate"
elif [ -z "$VIRTUAL_ENV" ]; then
  echo "You must have WORKON_HOME set, say to venv or ~/virtualenvs"
  exit 1
fi

pip install -r requirements.txt

python start.py $*
