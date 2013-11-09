class rps_python {
  class {'python':
    version    => 'system',
    dev        => true,
    gunicorn   => true,
    pip        => true,
    virtualenv => true,
  }

  package { ['libxml2-dev', 'libxslt-dev']:
    ensure    => present,
  }

}
