# == Class: base
#
# Installs a basic set of packages meant for all servers. Define the "packages"
# data item in Hiera as an array of package names that will be merged across
# the hierarchy with hiera_array().
#
class base {

  # Make sure apt-get update is run before any package operations
  if defined(Class['apt::update']) {
    Class['apt::update'] -> Package <|
      provider != pip and
      provider != gem and
      ensure != absent and
      ensure != purged and
      title != 'python-software-properties'
    |>
  }

  $packages = hiera_array('packages', [])
  package { $packages:
    ensure => present,
    # Put a Before clause here to ensure packages are installed before any actions
  }

}
