rps-alpha
=========

Follow these steps to setup a Quickstart development environment for working with the RPS Alpha project. 

## Quickstart Steps

### Windows Pre-reqs

- Install PyCharm Community Edition for Windows (http://www.jetbrains.com/pycharm/)
- Install Python 2.7.5 for Windows - Windows X86-64 MSI Installer (2.7.5) (http://www.python.org/download/releases/2.7.5/)
- Install Oracle Virtual Box for Windows (https://www.virtualbox.org/wiki/Downloads)
- Install git (http://git-scm.com/downloads) 
  - if you are on Windows also install git-bash when asked.
  - when prompted to choose conversion setting pick check out as-is, commit unix style (the middle option)
- Install Vagrant (http://www.vagrantup.com/)

### Post Install Tasks
- Configure SSH for GIT - Follow this guide (https://help.github.com/articles/generating-ssh-keys)

  Don't bother with a passphrase for alpha
- Clone the repository.  In GITBash `git clone git@github.com:InsolvencyService/rps-alpha.git`

### How to make it work

- Open a new terminal windows (use git-bash on windows) and navigate 
  to where you have downloaded or cloned this repo.
- Run `vagrant up`... Vagrant should create a new virtual machine and puppet should provision it
- Run `vagrant ssh` to ssh into the newly created virtual machine
- Run `cd /vagrant` to see the files mirrored from your host machine to your VM
