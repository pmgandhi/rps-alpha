from fabric.api import abort, cd, env, roles, run, settings, task
from fabric.api import show, hide, put
from fabric.api import fastprint

dev_domain     = 'redundency-payments.alpha.service.gov.uk'

dev_jump            = "37.26.89.67"
dev1                = "37.26.89.67"

env.roledefs = {
    # Preview environment - For Alpha
    'ci':             [ dev1 ]
}

def roles_for_host(host_query):
    return [role for role,hosts in env.roledefs.items() if host_query in hosts]

JENKINS_HOSTS = {
    'alpha': 'ci.%s' % dev_domain
}

JUMP_HOSTS = {
    'alpha': dev1
}

def fetch_artifact(puppet_env, job, artifact, dest, build_number='lastSuccessfulBuild'):
    url = 'https://{root}/job/{job}/{build_number}/artifact/{artifact}'.format(
        root=JENKINS_HOSTS.get(puppet_env),
        job=job,
        artifact=artifact,
        build_number=build_number)

    cmd = "curl -sk -u '{user}:{key}' '{url}' > {dest}".format(
        user=env.jenkins_user,
        key=env.jenkins_key,
        url=url,
        dest=dest)

    run(cmd)


@task
def bootstrap_jenkins(deploy_env):
    role = roles_for_host(env.host_string)[0]
    if role is not "ci":
        abort("Only CI boxes can be bootstrapped")
    else:
        put('../puppet/puppet.tgz', '/tmp/puppet.tgz')
        put('../../puppet-secrets/puppet-secrets.tgz', '/tmp/puppet-secrets.tgz')
        run('mkdir -p /tmp/puppet')
        with cd('/tmp/puppet'):
            run('tar zxf /tmp/puppet.tgz')
            run('tar zxf /tmp/puppet-secrets.tgz')
            run('sudo -i FACTER_role={role} '
                'sh -c "cd \'$PWD\'; ./bin/puppet apply '
                '--environment={deploy_env} '
                '--verbose '
                '--confdir=. '
                '--modulepath modules:vendor/modules '
                'manifests/site.pp"'.format(role=role, deploy_env=deploy_env))
    run('sudo rm -rf /tmp/puppet /tmp/puppet.tgz /tmp/puppet-secrets.tgz')

@task
def puppet(deploy_env):
    env.gateway = JUMP_HOSTS.get(deploy_env, None)
    role = roles_for_host(env.host_string)[0]
    if role is None:
        abort('No Puppet role defined, exiting.')
    with settings(warn_only=True):
        fetch_artifact(deploy_env, 'puppet', 'puppet.tgz', '~/puppet.tgz')
        fetch_artifact(deploy_env, 'puppet-secrets', 'puppet-secrets.tgz', '~/puppet-secrets.tgz')
        run('mkdir puppet')
        with cd('puppet'):
            run('tar zxf ~/puppet.tgz')
            run('tar zxf ~/puppet-secrets.tgz')
            run('sudo -i FACTER_role={role} '
                'sh -c "cd \'$PWD\'; ./bin/puppet apply '
                '--environment={deploy_env} '
                '--verbose '
                '--confdir=. '
                '--modulepath modules:vendor/modules '
                'manifests/site.pp"'.format(role=role, deploy_env=deploy_env))
    run('sudo rm -rf puppet puppet.tgz puppet-secrets.tgz')


