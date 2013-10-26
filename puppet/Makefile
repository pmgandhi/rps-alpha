# Makefile for this bootstrappy spike
#
.PHONY: help librarian

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  omnibus_deb     build deb omni-puppet deb file for precise64"
	@echo "  clean           start from a clean download/vm"

clean:
	bundle exec librarian-puppet clean

librarian:
	bundle exec librarian-puppet install
