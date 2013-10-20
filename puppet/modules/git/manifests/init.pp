# install git - a source control tool

class git {
    package { 'git':
        ensure => present;
    }
}

