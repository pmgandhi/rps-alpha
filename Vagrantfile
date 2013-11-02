VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = 'precise64'
    config.vm.box_url = 'http://files.vagrantup.com/precise64.box'

    config.vm.define "development", primary: true do |development|
      development.vm.network "forwarded_port", guest: 8000, host: 8000
      development.vm.provision :shell,
                    path: "vagrant-bootstrap.sh",
                    args: "localdev localdev"
      development.ssh.forward_agent = true
    end

    config.vm.define "jenkins", primary: true do |jenkins|
      jenkins.vm.network "forwarded_port", guest: 8000, host: 8000
      jenkins.vm.provision :shell,
                    path: "vagrant-bootstrap.sh",
                    args: "jenkins localdev"

    end

end

