class rps_postgres::hstore {
    class {'postgresql::server::contrib': }

    exec {'add hstore to the template database':
        command => "/usr/bin/psql template1 -c 'create extension if not exists hstore;'",
        user    => 'postgres',
        require => Class['postgresql::server::contrib']
    }
}