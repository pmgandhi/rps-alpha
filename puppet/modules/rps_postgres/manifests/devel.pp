class rps_postgres::devel {
    # These resources are needed so that we can compile psycopg2 and
    # friends on the machine.  Long term, we should be distributing .whl
    # files (which are pre-compiled binaries) but for now, just put this
    # everywhere that we put postgres
    class {'postgresql::lib::devel': }
}
