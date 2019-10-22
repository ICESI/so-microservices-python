### Introducción a los ambientes virtuales en python
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Introducción a los ambientes virtuales en python  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Crear ambientes virtuales con python

### Introducción
Por medio de los ambientes virtuales de python es posible ejecutar múltiples proyectos con versiones de librerías distintas.
Virtualenvwrapper es un wrapper para virtualenv el cual permite la activación de ambientes virtuales desde cualquier lugar del path del sistema operativo

### Requerimientos
Maquina Virtual de CentOS7

### Instalación CentOS7 y Python2
Ingrese los comandos que se describen a continuación

```
# adduser microservices
# passwd microservices
# yum install -y wget
# wget https://bootstrap.pypa.io/get-pip.py -P /tmp
# python /tmp/get-pip.py
# pip install virtualenv
# su microservices
$ pip install --user virtualenvwrapper
```
Para iniciar virtualenvwrapper al autenticarse como el usuario microservices editamos el archivo **.bashrc**
```
$ vi ~/.bashrc
export WORKON_HOME=~/.virtualenvs
source ~/.local/bin/virtualenvwrapper.sh
```
Para activar los cambios sin necesidad de cerrar la sesión del usuario python_user se debe ejecutar el siguiente comando
```
$ source ~/.bashrc
```

### Instalación CentOS7 y Python3

Estos son los pasos para la instalación
```
# yum install epel-release
# yum install python34
# yum install python34-pip
# adduser flaskdev
# passwrd flaskdev
# su flaskdev
$ cd ~/
$ pip install --user virtualenvwrapper
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
$ vi ~/.bashrc
# User specific aliases and functions
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
$ source ~/.bashrc
```

Con estos pasos puede validar la instalación
```
$ mkvirtualenv flaskdev
$ pip install flask
$ pip install pyyaml
$ pip install pygithub
$ deactivate
$ workon flaskdev
```

### Instalacion múltiples versiones de Python en MacOS (Mojave)

```
brew install readline xz zlib pyenv
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/sqlite/lib/pkgconfig"
eval "$(pyenv init -)"
pyenv install 3.7.3
pyenv global 3.7.3

vi ~/.zshrc
eval "$(pyenv init -)"
eval "$(rbenv init -)"
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_PYTHON=$HOME/.pyenv/shims/python
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.pyenv/versions/3.7.3/bin/virtualenv
source $HOME/.pyenv/versions/3.7.3/bin/virtualenvwrapper.sh
```

### Activación automática de ambientes (not working)

```
sudo apt install direnv
```

vi ~/.direnvrc
```
layout_virtualenv() {
  local venv_path="$1"
  source ${venv_path}/bin/activate
}

layout_virtualenvwrapper() {
  local venv_path="${WORKON_HOME}/$1"
  layout_virtualenv $venv_path
}
```

Cree un directorio para su proyecto y un ambiente virtual
```
mkdir dir my-project
cd my-project
mkvirtualenv my-project-env
```

Cree un archivo con las configuraciones necesarias
```
vi .envrc
export FOO='BAR'
layout virtualenvwrapper my-awesome-project

```

Apruebe los cambios
```
direnv allow
```

Para probar ejecute las siguientes instrucciones
```
echo $FOO
cd ..
echo $FOO
```

### Desarrollo

Practique los comandos que se muestran en la tabla a continuación

| Comando | Descripción |
|---	|---	|
| mkvirtualenv test	| Crea el ambiente virtual llamado test	|
| deactivate	| Si un ambiente virtual esta activo, lo desactiva	|
| workon test	| Activa el ambiente virtual llamado test	|
| pip install Flask	| Si el ambiente esta activo, instala la libreria Flask en el ambiente	|
| rmvirtualenv test	| Elimina el ambiente virtual llamado test	|
| lsvirtualenv | Lista los ambientes virtuales |

### Actividades

* Cree al menos tres ambientes que tengan la misma librería de python pero en versiones distintas

### Referencias

https://github.com/pyenv/pyenv/issues/692  
https://github.com/jiansoung/issues-list/issues/13  
https://weknowinc.com/blog/running-multiple-python-versions-mac-osx  
https://github.com/pyenv/pyenv-virtualenvwrapper
