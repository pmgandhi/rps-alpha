#!/bin/bash

cd puppet/

role=jenkins
env=localenv

sudo FACTER_role="$role" build/bin/puppet apply \
    --environment=${env} \
    --confdir=. \
    --modulepath=modules:vendor/modules \
    manifests/site.pp
