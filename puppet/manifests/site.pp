stage { 'init':
    before => Stage['main']
}

class { 'baseconfig':
    stage => 'init'
}

class { 'mongodb':
      enable_10gen => true,
}

include baseconfig, git, vim, python_tools, mongodb

