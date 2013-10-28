dev-box
=======

Quickstart development environment with Vagrant and Puppet

## Windows and OSX

### Requirements

- Install git (http://git-scm.com/downloads) - if you are on Windows also install git-bash when asked
- and VirtualBox (https://www.virtualbox.org/wiki/Downloads)

### How to make it work

- Open a new terminal windows (use git-bash on windows) and navigate 
  to where you have downloaded or cloned this repo.
- Run `vagrant up`... Vagrant should create a new virtual machine and puppet should provision it
- Run `vagrant ssh` to ssh into the newly created virtual machine
- Run `cd /vagrant` to see the files mirrored from your host machine to your VM
- Run `make puppet` and then `make bootstrap` in order to run the second step of provisioning
