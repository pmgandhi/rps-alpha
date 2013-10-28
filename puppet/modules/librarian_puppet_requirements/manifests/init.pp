# install requirements for librarian puppet

class librarian_puppet_requirements {
    package { 'bundle':
        ensure      => present,
        provider    => gem,
    }

    exec { 'bundle install librarian-puppet':
        command => '/opt/vagrant_ruby/bin/bundle install librarian-puppet',
        require => Package['bundle'],
    }
}

