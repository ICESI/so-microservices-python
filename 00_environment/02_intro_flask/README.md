
### Introducción al microframework Flask
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Introducción a servicios web con Python  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Crear servicios web por medio de Python
* Realizar pruebas sobre servicios web

### Introducción
Flask es un micro web framework escrito en Python y basado en la especificación WSGI de Werkzeug y el motor de templates Jinja2. Tiene licencia BSD.

#### Instalación de Flask

Cree un ambiente de nombre flask_environment, si no se activa automáticamente, actívelo.

```
$ mkvirtualenv flask_environment
$ workon flask_environment
```

Instale la libreria Flask

```
$ pip install Flask
```

#### Exportando librerias

El gestor de paquetes **pip** permite exportar las librerias instaladas junto con su versión.

```
pip freeze > requirements.txt
```

El archivo exportado permite instalar las librerias empleadas para un proyecto en otros ambientes de trabajo. _No es necesario ejecutar el siguiente comando debido a que las librerías ya se encuentran instaladas, solo se incluye con fines ilustrativos_

```
pip install -r requirements.txt
```

#### Ejemplo básico

Cree un directorio para alojar los ejemplos

```
$ cd ~/
$ mkdir -p flask_examples/01_ejemplo_basico
$ cd flask_examples/01_ejemplo_basico
```

Cree un archivo de nombre **hello.py**

``` python
from flask import Flask
app = Flask(__name__)

@app.route("/greeting")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run('0.0.0.0')
```

```
$ python hello.py
```

Para cancelar la ejecución presione la combinación de teclas **CTRL** y la tecla **C**

#### Contrato REST

Descripción de las URIs

| | POST | GET | PUT | DELETE |
|---	|--- 	|---	|---	|---	|
| /users | Inserta un usuario | Retorna los datos de todos los usuarios | No aplica | Elimina todos los usuarios |
| /users/daniel | No aplica | Retorna los datos del usuario daniel | Actualiza el usuario daniel | Elimina el usuario daniel |
| /users?group=root&lastlog=30&commands | No aplica | Retorna los usuarios del grupo root, que se autenticaron hace menos de 30 minutos, todos los comandos que ejecutaron  | No aplica | No aplica	|
| /users/recently_logged | No aplica	| Retorna los usuarios que se autenticaron recientemente	|  No aplica 	| No aplica |
| /users/daniel/commands | ¿No aplica? | Retorna los comandos ejecutados por daniel | No aplica | No aplica

Descripción de los formatos de envío de las solicitudes

|	| POST | GET | PUT | DELETE	|
|---	|---	|---	|---	|---	|
| /users | JSON | No aplica | No aplica	| No aplica	|
| /users/daniel	| No aplica | No aplica	| JSON | No aplica	|
| /users?group=root&lastlog=30&commands	| No aplica | No aplica | No aplica | No aplica |
| /users/recently_logged | No aplica	| No aplica | No aplica | No aplica |
| /users/daniel/commands | No aplica | No aplica | No aplica | No aplica |

Descripción de los formatos de respuesta de las solicitudes

|	| POST | GET | PUT | DELETE	|
|---	|---	|---	|---	|---	|
| /users | HTTP 201 CREATED | JSON | HTTP 404 NOT FOUND	| HTTP 200 OK	|
| /users/daniel	| HTTP 404 NOT FOUND | JSON	| HTTP 200 OK | HTTP 200 OK	|
| /users?group=root&lastlog=30&commands	| HTTP 404 NOT FOUND | JSON | HTTP 404 NOT FOUND | HTTP 404 NOT FOUND |
| /users/recently_logged | HTTP 404 NOT FOUND	| JSON | HTTP 404 NOT FOUND | HTTP 404 NOT FOUND |
| /users/daniel/commands | HTTP 404 NOT FOUND | JSON | HTTP 404 NOT FOUND | HTTP 404 NOT FOUND |

#### Objeto JSON

Ejemplo de objeto en JSON

```json
{
  "username": "icesi",
  "password": "mipassword"
}
```

```json
{
  "users": [
    "root",
    "operativos",
    "postgres",
    "jenkins"
  ]
}
```

#### Ejemplo REST

Cree un archivo de nombre **users.py**

```python
from flask import Flask, abort
app = Flask(__name__)

api_url = '/v1.0'

@app.route(api_url+'/users',methods=['POST'])
def create_user():
  return 'create one user'

@app.route(api_url+'/users',methods=['GET'])
def read_user():
  return 'read all users'

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  abort(404)

@app.route(api_url+'/users',methods=['DELETE'])
def delete_user():
  return 'delete all users'

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,debug='True')
```

```
$ python users.py
```

#### Pruebas del servicio web (REST)

Instale la extensión postman
![][1]

A continuación se muestran las pruebas al servicio web empleando la extensión postman. Tambien se muestra como crear una colección con las peticiones lo que permite realizar futuras pruebas

Prueba de la URI con GET
![][2]
![][3]

Prueba de la URI con POST
![][4]
![][5]

Prueba de la URI con PUT
![][6]
![][7]

Prueba de la URI con DELETE
![][8]
![][9]

Las colecciones se pueden exportar para ser usadas en otros equipos

#### Desactivar un ambiente virtual

Desactive el ambiente desde cualquier ubicación

```
$ deactivate
```

#### Implementación del contrato para /users

Comandos a emplear por el servicio web a implementar

```
grep /bin/bash /etc/passwd | awk -F ':' ' {print $1}'
sudo adduser --password password username
sudo userdel -r username
```

Edite el archivo sudoers como el usuario **root*

```
# visudo
User_Alias RESTUSERS = operativos
Cmnd_Alias MANAGEUSERS = /usr/sbin/adduser, /usr/sbin/userdel, /usr/bin/passwd
RESTUSERS    ALL=NOPASSWD: MANAGEUSERS
```

Actualice el archivo de nombre **users.py**

```python
from flask import Flask, abort, request
import json

from user_commands import get_all_users, add_user, remove_user

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['POST'])
def create_user():
  content = request.get_json(silent=True)
  username = content['username']
  password = content['password']
  if not username or not password:
    return "empty username or password", 400
  if username in get_all_users():
    return "user already exist", 400
  if add_user(username,password):
    return "user created", 201
  else:
    return "error while creating user", 400

@app.route(api_url+'/users',methods=['GET'])
def read_user():
  list = {}
  list["users"] = get_all_users()
  return json.dumps(list), 200

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not found", 404

@app.route(api_url+'/users',methods=['DELETE'])
def delete_user():
  error = False
  for username in get_all_users():
    if not remove_user(username):
        error = True

  if error:
    return 'some users were not deleted', 400
  else:
    return 'all users were deleted', 200

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
```

Cree un archivo de nombre **users_commands.py**

```python
from subprocess import Popen, PIPE

def get_all_users():
  grep_process = Popen(["grep","/bin/bash","/etc/passwd"], stdout=PIPE, stderr=PIPE)
  user_list = Popen(["awk",'-F',':','{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,user_list)

def add_user(username,password):
  add_process = Popen(["sudo","adduser","--password",password,username], stdout=PIPE, stderr=PIPE)
  add_process.wait()
  return True if username in get_all_users() else False

def remove_user(username):
  vip = ["operativos","jenkins","postgres","root"]
  if username in vip:
    return True
  else:
    remove_process = Popen(["sudo","userdel","-r",username], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if username in get_all_users() else True
```

Recuerde activar el ambiente antes de ejecutar el script

```
$ (flask_env) python users.py
```

Prueba de la uri con POST y enviando un JSON

![][10]

Puede consultar el código fuente del ejercicio en el repositorio de github del curso

### Actividades

1. Investigue acerca de la utilidad del comando visudo. Indique el propósito de usar visudo en esta guía

2. Implemente las funcionalidades del contrato restantes

3. Define un contrato para un servicio que permita realizar el escaneo de los puertos abiertos en una red desde un servidor. Define e implemente como mínimo las peticiones para GET (/scans,/scans/ip_address).

4. Configure los servicios web implementados de tal forma que se ejecuten desde el inicio del sistema operativo.

5. Adicione autentación por medio de tokens a los endpoints desarrollados

**Nota:** Se sugiere la instalación de nmap en el servidor. Tenga en cuenta que nmap cuenta con opciones para generar la salida en xml pero no json.

### Referencias
https://www.w3.org/Protocols/HTTP/HTRESP.html
http://stackoverflow.com/questions/31143486/virtualenvwrapper-centos7

[1]: images/01_postman.png
[2]: images/02_get_uri.png
[3]: images/03_get_into_collection.png
[4]: images/04_post_uri_save_as.png
[5]: images/05_post_into_collection.png
[6]: images/06_put_uri_save_as.png
[7]: images/07_put_into_collection.png
[8]: images/08_delete_uri_save_as.png
[9]: images/09_delete_into_collection.png
[10]: images/10_post_uri_json.png
