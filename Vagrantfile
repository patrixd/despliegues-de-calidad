# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_version = "20170313.0.7"
  config.vm.network "forwarded_port", guest: 8000, host: 8002
  config.vm.synced_folder ".", "/home/vagrant"
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update

    echo
    echo "Installing Python, PostgreSQL 9.3..."
    sudo apt-get install -y libpq-dev python-dev
    sudo apt-get install -y python-pip
    sudo apt-get install -y postgresql postgresql-contrib
    echo
    echo "Installing the Python required dependencies from requirements.txt..."
    sudo pip install -r requirements.txt    
    echo
    sudo -u postgres -i <<HERE
    echo "Setting postgres password..."
    psql postgres -c "ALTER ROLE postgres WITH PASSWORD 'postgres';"
    echo "postgres password set."
    echo "Migrating database..."
    python /home/vagrant/manage.py migrate
  SHELL
end
