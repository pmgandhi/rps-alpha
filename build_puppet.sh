#!/bin/bash

set -eu

status () {
  echo "---> ${@}" >&2
  }

cd puppet/

bundle exec librarian-puppet install
