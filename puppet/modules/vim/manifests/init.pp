# install and configure vim - a console based text editor

class vim {
    file { '/home/vagrant/.vimrc':
        owner   => 'vagrant',
        group   => 'vagrant',
        mode    => '0644',
        source  => 'puppet:///modules/vim/vimrc';
    }
}

