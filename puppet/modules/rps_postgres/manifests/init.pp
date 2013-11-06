class rps_postgres {
    class {'::rps_postgres::install': } ->
    class {'::rps_postgres::devel': } ->
    class {'::rps_postgres::hstore': } ->
    class {'::rps_postgres::rps_alpha_database': }
}