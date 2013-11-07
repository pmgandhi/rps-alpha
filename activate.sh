#!/usr/bin/env bash

VENVNAME=rps-dev

if [ -z "$VIRTUAL_ENV" -a -n "$WORKON_HOME" ]; then

   venvdir=$WORKON_HOME/$VENVNAME

   if [ ! -d "$venvdir" ]; then
     virtualenv $venvdir
   fi

   source "$venvdir/bin/activate"

   # meh - see https://github.com/pypa/pip/issues/56
   pip install -r redundancy_payments_alpha/requirements.dev.txt
   pip install -r birmingham_cabinet/requirements.dev.txt

fi
