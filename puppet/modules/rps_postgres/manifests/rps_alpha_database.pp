class rps_postgres::rps_alpha_database {
    postgresql::server::database { 'rps_alpha':
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

    postgresql::server::role { 'jenkins': }

    postgresql::server::database_grant {'give jenkins rps_alpha':
        privilege => 'ALL',
        db        => 'rps_alpha',
        role      => 'jenkins',
        require   => [
            Postgresql::Server::Role['jenkins'],
            Postgresql::Server::Database['rps_alpha']
        ]
    }
}
