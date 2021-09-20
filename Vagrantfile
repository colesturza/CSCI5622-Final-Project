# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.provider "virtualbox" do |v|
    v.memory = 5120
    v.cpus = 4
  end

  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # require plugin https://github.com/leighmcculloch/vagrant-docker-compose
  config.vagrant.plugins = "vagrant-docker-compose"

  # install docker and docker-compose
  config.vm.provision :docker
  config.vm.provision :docker_compose

  config.vm.provision "file", source: "./docker-compose.yaml", destination: "$HOME/docker-compose.yaml"
  config.vm.provision "file", source: "./Dockerfile", destination: "$HOME/Dockerfile"
  config.vm.provision "file", source: "./requirements.txt", destination: "$HOME/requirements.txt"
  config.vm.provision "file", source: "./src", destination: "$HOME/src"
end