
##Run Vagrant Development Environment

Install VirtualBox and Vagrant. Then run in the project root:
`vagrant up`
`vagrant ssh`
`python manage.py runserver 0.0.0.0:8000 --settings=app.settings_vagrant`

User/Password: vagrant/vagrant

If you add modify the shell code for provisioning, stop the machine with `vagrant halt` and run `vagrant up --provision`.
Open the app in the browser with http://localhost:8002/.

##Run Docker Development Environment

Install Docker Composer. 
Run in the project root:

`docker-compose up`

Open the app in the browser with http://localhost:8001/.
