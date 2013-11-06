
class baseconfig {
    file { '/home/vagrant/.bashrc':
        owner   => 'vagrant',
        group   => 'vagrant',
        mode    => '0644',
        source  => 'puppet:///modules/baseconfig/bashrc';
    }

  class { 'python':
        version    => 'system',
        dev        => true,
        virtualenv => true,
        gunicorn   => true,
    }

}

