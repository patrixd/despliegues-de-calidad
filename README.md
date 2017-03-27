
##Entorno de Desarrollo con Vagrant

Instala VirtualBox y Vagrant. 
Ejecuta en la raíz del proyecto lo siguiente:
`vagrant up`
`vagrant ssh`
`python manage.py runserver 0.0.0.0:8000 --settings=app.settings_vagrant`

Usuario/Password: vagrant/vagrant

Si modificas el código de provision, para la máquina con `vagrant halt` y ejecuta `vagrant up --provision`.
Abre la aplicación en el navegador http://localhost:8002/.

Ejecuta los tests con `python manage.py test --settings=app.settings_vagrant`


##Entorno de Desarrollo con Docker

Instala Docker Composer. 
Ejecuta en la raíz del proyecto lo siguiente:

`docker-compose up`

Abre la aplicación en el navegador http://localhost:8001/.
Si necesitas ejecutar en la máquina algún comando pon como prefijo:

`docker-compose run <service>`

Ejemplo: `docker-compose run web python manage.py migrate`

Ejecuta los tests con `docker-compose run web python manage.py test --settings=app.settings_docker`