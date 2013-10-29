# RPS Exemplar Puppet Modules

Here are the Puppet modules for the RPS Exemplar projects.

We intend to reuse code from GOV.UK, ERTP, HMRC and IDA teams, and to share back as
much as possible.

## Guidelines

### Use [Hiera] [1] for external data

There is a hieradata directory for storing data which is read in the following
order:

  - hostname (e.g. rpsdev1)
  - server role (e.g. app-server, web-proxy, etc.)
  - environment (e.g. development, staging, production, etc.)
  - common.yaml (catch-all for basic configuration data)

If you're ever tempted to create a params.pp manifest, chances are you're
creating data that should go in a relevant YAML file under ../hieradata. Please
get in touch if you're not sure how to go about this.

[1]: https://github.com/puppetlabs/hiera "Hiera"

### Write a suitable spec for the module using [rspec-puppet] [2]

This can be seen as unnecessary for very simple modules (such as the typical
"package -> config -> service" series), but if your module starts to get
complex, please consider creating some specs for it. This really helps further
down the road when the module's behaviour may need to be modified. 

[2]: http://rspec-puppet.com/tutorial/ "rspec-puppet"

### Always check your code with puppet-lint before committing

This prevents lots of useless "typo" commits, and can be done easily with the
enclosed Rake task "rake lint". A pre-commit hook script is in the tools
folder.
