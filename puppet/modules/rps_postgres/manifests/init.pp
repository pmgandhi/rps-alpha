class rps_postgres {
    class {'postgresql::server': }

    # These resources are needed so that we can compile psycopg2 and
    # friends on the machine.  Long term, we should be distributing .whl
    # files (which are pre-compiled binaries) but for now, just put this
    # everywhere that we put postgres
    class {'postgresql::lib::devel': }
    class {'postgresql::server::contrib': }
    package {'build-essential': }
    package {'python-dev': }

    # FIXME: This is to simplify the configuration for development
    postgresql::server::pg_hba_rule {'allow unix socket connections to access anything':
        type        => 'local',
        database    => 'all',
        user        => 'all',
        auth_method => 'peer'
    }

    postgresql::server::role { 'vagrant': }

    postgresql::server::database_grant {'give vagrant rps_alpha':
        privilege => 'ALL',
        db        => 'rps_alpha',
        role      => 'vagrant',
        require   => [
            Postgresql::Server::Role['vagrant'],
            Postgresql::Server::Database['rps_alpha']
        ]
    }

    postgresql::server::database { 'rps_alpha': }

    exec {'add hstore to the template table':
        command => "/usr/bin/psql template1 -c 'create extension hstore;'",
        user    => 'postgres',
        require => Class['postgresql::server::contrib']
    }

}