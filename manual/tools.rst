Tools
=====

Development
###########

Python Language
---------------

We use Python as it is a modern well structured and intuitive general purpose programming language with good library
see [link] for further details.

Language Choice
```````````````
    .. include:: codechoice.rst

**Style Guidence**

* http://www.python.org/dev/peps/pep-0008/
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
* http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

**Introductory Materials**

* http://docs.python-guide.org/en/latest/
* http://www.youtube.com/watch?v-g7V89K8QfgQ

VirtualEnv and pip
------------------

We use virtualenv and pip to manage the versioning, download and installation of library dependencies for Python projects.

**Documentation**

* http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
* http://www.pip-installer.org/en/latest/index.html#
* http://www.virtualenv.org/en/latest/

Flask
-----

We use Flask as the web application framework for building web applications and services. Flask follows the Model View
Controller Pattern.

**Documentation**

* http://flask.pocoo.org/
* http://flask.pocoo.org/docs/
* http://flask.pocoo.org/docs/api/

**Model View Controller**

* http://c2.com/cgi/wiki?ModelViewController
* http://www.codinghorror.com/blog/2008/05/understanding-model-view-controller.html
* http://martinfowler.com/eaaDev/uiArchs.html

WTForms
-------

We use WTForms as a validation library for web-forms. We use FlaskWTF as a simple integration with Flask.

**Documentation**

* https://wtforms.readthedocs.org/en/latest/
* https://flask-wtf.readthedocs.org/en/latest/

Behave
------

We use behave as an acceptance testing framework for our application. Behave follows the Behaviour Driven Development
pattern.

**Documentation**

* http://pythonhosted.org/behave/

**Behaviour Driven Development**

* http://dannorth.net/introducing-bdd/
* http://skillsmatter.com/podcast/agile-testing/introduction-to-bdd

Nosetests
---------

We use nose as tool for running unit tests that we write to support our code.

**Documentation**

* http://nose.readthedocs.org/en/latest/
* http://nose.readthedocs.org/en/latest/testing.html


Source Control & Tools
######################

Git SCM
-------

We use Git as a source control management system.

**Documentation**

* http://git-scm.com/
* http://rogerdudler.github.io/git-guide/
* http://git-scm.com/book

**Fun Torvalds Talk on subject**

* http://www.youtube.com/watch?v-4XpnKHJAok8


Github.com
----------

We use Gihub.com as a centralised Git server and collaboration platform for code review.

**Documentation**

* https://github.com/about
* https://help.github.com/articles/using-pull-requests
* https://help.github.com/

Travis
------

We use Travis to give us quick feedback when we push a change to GitHub. It will run tests against feature branches
and notify us if there is a problem.

**Documentation**

* http://about.travis-ci.org/

Sphinx
------

We use Sphinx as a tool for building the manual containing technical information about the project. Sphinx uses
ReStructuredText as a markup format.

**Documentation**

* http://sphinx-doc.org/
* http://docutils.sourceforge.net/rst.html
* http://sphinx-doc.org/rest.html

Infrastructure
##############

Vagrant
-------

We use Vagrant to give us a consistent runtime environment between development laptops and producton. Vagrant is a
wrapper around VirtualBox which allows us to automate the setup of local development environments using the same
tools as production.

**Documentation**

* http://docs.vagrantup.com/v2/

Jenkins
-------

We use Jenkins to run tests against release candidate branches and carry out deployment and testing of the production
system.

**Documentation**

* https://wiki.jenkins-ci.org/display/JENKINS/Meet+Jenkins

Ubuntu 12.04
------------

We use Ubuntu 12.04 as a runtime platform for application code in development and production for alpha.

**Documentation**

* https://wiki.ubuntu.com/LTS
* http://en.wikipedia.org/wiki/Linux

Puppet
------

We use Puppet to manage the configuration of Ubuntu servers. We also use it via vagrant to ensure we have a production
like development environment.

**Documentation**

* http://docs.puppetlabs.com/learning/#contents
* http://docs.puppetlabs.com/references/latest/type.html
* http://docs.puppetlabs.com/puppet/3/reference/
* http://docs.puppetlabs.com/references/glossary.html

Hiera
-----

We use Hiera as a configuration layer for Puppet as certain aspects of Puppet's out of the box configuration layer are
problematic and deficient.

**Documentation**

* http://projects.puppetlabs.com/projects/hiera
