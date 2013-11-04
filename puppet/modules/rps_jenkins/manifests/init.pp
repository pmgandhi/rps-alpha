# == Class: rps-jenkins
#
# Base class for CI environment
#
class rps_jenkins {

        include jenkins

        package {'ssl-cert':
            ensure  => '1.0.28ubuntu0.1',
            require => Class['apt::update'],
        }

        class {'nginx::server':
        }

        nginx::vhost::proxy  { 'jenkins-nginx':
            ssl            => true,
            ssl_redirect   => true,
            isdefaultvhost => true,
            servername     => "ci.rps-alpha.co.uk",
            serveraliases  => "10.0.0.1",
        }

        sshkey { 'github.com':
            ensure => present,
            type   => 'ssh-rsa',
            key    => 'AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==',
        }

        $jenkins_home = "/home/jenkins"

        file {"${jenkins_home}":
          ensure  => directory,
          owner   => 'jenkins',
          group   => 'jenkins',
        }

        file {"${jenkins_home}/.ssh":
          ensure  => directory,
          owner   => 'jenkins',
          group   => 'jenkins',
          mode    => '0700',
          require => File["${jenkins_home}"],
        }

        $private_key = "${jenkins_home}/.ssh/id_rsa"
        exec { 'Creating key pair for jenkins':
          command => "ssh-keygen -t rsa -C 'Provided by Puppet for jenkins' -N '' -f ${private_key}",
          creates => $private_key,
          user    => 'jenkins',
          require => File["${jenkins_home}/.ssh"],
        }

        file {"${jenkins_home}/.gitconfig":
          ensure  => 'present',
          owner   => 'jenkins',
          group   => 'nogroup',
          mode    => '0644',
          source  => 'puppet:///modules/rps_jenkins/jenkins-dot-gitconfig',
          require => File["${jenkins_home}"],
        }

}
