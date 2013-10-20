class python_tools {
    package { 'python-pip':
        ensure => present
    }

    package { ['virtualenv', 'virtualenvwrapper']:
        ensure => present,
        provider => pip,
        require => Package['python-pip'],
    }
}

