# Makefile for this bootstrappy spike
#
.PHONY: help librarian clean tests

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  omnibus_deb     build deb omni-puppet deb file for precise64"
	@echo "  clean           start from a clean download/vm"

clean:
	vagrant destroy -f

box:
	vagrant up

tests:
	vagrant ssh --c "/vagrant/frontend/run-tests.sh"

