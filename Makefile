# Makefile for this bootstrappy spike
#
.PHONY: help clean tests puppet

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  box             bring the vagrant box up"
	@echo "  tests           run the frontend tests"
	@echo "  puppet          collect puppet dependancies"
	@echo "  clean           start from a clean download/vm"

clean:
	cd puppet-bootstrap; make clean
	vagrant destroy -f

puppet:
	cd puppet-bootstrap; make librarian

box: puppet
	vagrant up

tests: box
	vagrant ssh --c "/vagrant/frontend/run-tests.sh"

