class rps_postgres::hstore {
    class {'postgresql::server::contrib': }

    exec {'add hstore to the rps_alpha database':
        command => "/usr/bin/psql rps_alpha -c 'create extension if not exists hstore;'",
        user    => 'postgres',
        require => Class['postgresql::server::contrib']
    }
}