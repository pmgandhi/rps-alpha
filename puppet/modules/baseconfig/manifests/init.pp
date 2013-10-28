# basic setup - update apt-get and move os level configs into place

class baseconfig {
    exec { 'apt-get update':
        command => '/usr/bin/apt-get update';
    }

    file { '/home/vagrant/.bashrc':
        owner   => 'vagrant',
        group   => 'vagrant',
        mode    => '0644',
        source  => 'puppet:///modules/baseconfig/bashrc';
    }

    package { 'make':
        ensure => present;
    }
}

