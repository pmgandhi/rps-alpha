Tools
=====

Python Language
---------------

We use Python as it is a modern well structured and intuitive general purpose programming language with good library
see [link] for further details.

    Language Choice
    ```````````````
    .. include:: codechoice.rst

* http://www.python.org/dev/peps/pep-0008/
* http://www.youtube.com/watch?v-g7V89K8QfgQ
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
* http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
* http://docs.python-guide.org/en/latest/

VirtualEnv and pip
------------------

We use virtualenv and pip to manage the versioning, download and installation of library dependencies for Python projects.

* http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
* http://www.pip-installer.org/en/latest/index.html#
* http://www.virtualenv.org/en/latest/

Flask
-----

We use Flask as the web application framework for building web applications and services. Flask follows the Model View
Controller Pattern.

* http://flask.pocoo.org/
* http://flask.pocoo.org/docs/
* http://flask.pocoo.org/docs/api/

* http://c2.com/cgi/wiki?ModelViewController
* http://www.codinghorror.com/blog/2008/05/understanding-model-view-controller.html
* http://martinfowler.com/eaaDev/uiArchs.html

WTForms
-------

We use WTForms as a validation library for web-forms. We use FlaskWTF as a simple integration with Flask.

* https://wtforms.readthedocs.org/en/latest/
* https://flask-wtf.readthedocs.org/en/latest/

Behave
------

We use behave as an acceptance testing framework for our application. Behave follows the Behaviour Driven Development
pattern.

* http://pythonhosted.org/behave/

* http://dannorth.net/introducing-bdd/
* http://skillsmatter.com/podcast/agile-testing/introduction-to-bdd

Nosetests
---------

We use nose as tool for running unit tests that we write to support our code.

* http://nose.readthedocs.org/en/latest/
* http://nose.readthedocs.org/en/latest/testing.html

Sphinx
------

We use Sphinx as a tool for building the manual containing technical information about the project. Sphinx uses
ReStructuredText as a markup format.

* http://sphinx-doc.org/
* http://docutils.sourceforge.net/rst.html
* http://sphinx-doc.org/rest.html

Git SCM
-------

We use Git as a source control management system.

* http://git-scm.com/
* http://rogerdudler.github.io/git-guide/
* http://www.youtube.com/watch?v-4XpnKHJAok8
* http://git-scm.com/book


Github.com
----------

We use Gihub.com as a centralised Git server and collaboration platform for code review.

* https://github.com/about
* https://help.github.com/articles/using-pull-requests
* https://help.github.com/

Travis
------

We use Travis to give us quick feedback when we push a change to GitHub. It will run tests against feature branches
and notify us if there is a problem.

* http://about.travis-ci.org/

Vagrant
-------

We use Vagrant to give us a consistent runtime environment between development laptops and producton. Vagrant is a
wrapper around VirtualBox which allows us to automate the setup of local development environments using the same
tools as production.

* http://docs.vagrantup.com/v2/

Jenkins
-------

We use Jenkins to run tests against release candidate branches and carry out deployment and testing of the production
system.

* https://wiki.jenkins-ci.org/display/JENKINS/Meet+Jenkins

Ubuntu 12.04
------------

We use Ubuntu 12.04 as a runtime platform for application code in development and production for alpha.

* https://wiki.ubuntu.com/LTS
* http://en.wikipedia.org/wiki/Linux

Puppet
------

We use Puppet to manage the configuration of Ubuntu servers. We also use it via vagrant to ensure we have a production
like development environment.

* http://docs.puppetlabs.com/learning/#contents
* http://docs.puppetlabs.com/references/latest/type.html
* http://docs.puppetlabs.com/puppet/3/reference/
* http://docs.puppetlabs.com/references/glossary.html

Hiera
-----

We use Hiera as a configuration layer for Puppet as certain aspects of Puppet's out of the box configuration layer are
problematic and deficient.

* http://projects.puppetlabs.com/projects/hiera
