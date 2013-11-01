class shell {

  # A string from hiera used to customise the shell prompt, e.g.
  # "production", "staging", etc.
  $shell_prompt_string = hiera('shell_prompt_string', '')

  file { '/etc/bash.bashrc':
    content => template('shell/bashrc.erb'),
  }

  # Remove default user .bashrc
  #
  # The above system-wide bashrc will work just fine even if users don't have
  # their own .bashrc
  file { '/etc/skel/.bashrc':
    ensure => 'absent',
  }

}
