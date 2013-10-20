# install and configure vim - a console based text editor

class vim {
    package { 'vim':
        ensure => present;
    }

    file { '/home/vagrant/.vimrc':
        owner   => 'vagrant',
        group   => 'vagrant',
        mode    => '0644',
        source  => 'puppet:///modules/vim/vimrc';
    }
}

