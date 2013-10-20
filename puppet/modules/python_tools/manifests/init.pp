# install pip and use it to install some python tools

class python_tools {
    package { 'python-pip':
        ensure => present
    }

    package { ['virtualenv', 'virtualenvwrapper']:
        ensure      => present,
        provider    => pip,
        require     => Package['python-pip'],
    }
}

