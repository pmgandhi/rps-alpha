stage { 'init':
    before => Stage['main']
}

class { 'baseconfig':
    stage => 'init'
}

include baseconfig, git, vim, python_tools, librarian_puppet_requirements 

