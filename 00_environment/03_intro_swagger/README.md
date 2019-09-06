### Introducción al lenguaje Python
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Introducción a Swagger  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Conocer la importancia de la iniciativa OpenAPI
* Documentar servicios web RESTful por medio de swagger

### Introducción
Swagger es un framework de código abierto para el diseño, construcción, documentación y consumo de APIs RESTful.

### Instalación

En esta guía se asume que cuenta con una máquina virtual con el sistema operativos CentOS 7.x instalado. Las versiones de CentOS incluyen Python por defecto.

### Desarrollo

#### Virtualenvwrapper

Virtualenvwrapper es un wrapper para virtualenv el cual permite la activación de ambientes virtuales desde cualquier lugar del path del sistema operativo. Es posible configurar múltiples ambientes virtuales cada uno con librerías específicas dependiendo de los requerimientos de cada proyecto.

Para esta guía se creará un usuario llamado **python_user** y se ejecutarán los scripts a implementar como dicho usuario.

```
# yum install python-pip
# pip install virtualenvwrapper
# adduser python_user
# su python_user
```

Para iniciar virtualenvwrapper automáticamente editamos el archivo **.bashrc**

```
vi ~/bashrc
```

Y adicionamos las siguientes líneas al final del archivo

```
export WORKON_HOME=~/.virtualenvs
source /usr/bin/virtualenvwrapper.sh
```

Para usar virtualenvwrapper inmediatamente ejecutamos el siguiente comando desde el usuario python_user

```
source ~/.bashrc
```

Algunos comandos útiles son:

| Comando | Descripción |
|---	|---	|
| mkvirtualenv test	| Crea el ambiente virtual llamado test	|
| deactivate	| Si un ambiente virtual esta activo, lo desactiva	|
| workon test	| Activa el ambiente virtual llamado test	|
| pip install Flask	| Si el ambiente esta activo, instala la libreria Flask en el ambiente	|
| rmvirtualenv test	| Elimina el ambiente virtual llamado test	|
| ls ~/.virtualenvs/ | Lista los ambientes virtuales |

#### Creando ambiente e instalando dependencias

Ejecute los siguientes comandos como el usuario python_user, para crear un ambiente virtual e instalar las librerías a emplear en esta guía.

```
$ mkvirtualenv flask_env
$ pip install flask
$ pip install flask_restplus
```

**Nota:** Al crear un ambiente virtual con virtualenvwrapper, el ambiente creado es automáticamente activado. Esto se puede verificar al observar el nombre del ambiente a la izquierda del prompt ($)

Crear un directorio para el código fuente

```
(flask_env) $ cd ~/
(flask_env) $ mkdir flask_example
(flask_env) $ cd flask_example
```

#### Introducción a flask-restplus

Cree un archivo de nombre **hello.py** con el siguiente código

``` python
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8088,debug='True')
```

Para ejecutar el script ejecute el siguiente comando

```
(flask_env) $ python users.py
```

Abra un navegador en la dirección **http://127.0.0.1:8088**, podrá visualizar la documentación para el endpoint correspondiente a la url **http://127.0.0.1:8088/demo** para el método http **GET**. Cancele la ejecución del script presionando la combinación de teclas **CTRL+C**.

#### Gestión de usuarios con flask_restplus

En esta sección se realizarán modificaciones sobre el ejemplo del tema anterior **introducción a flask**. Modifique el archivo de nombre **users.py** de acuerdo con el siguiente código

``` python
import json
from flask import Flask, abort, request
from flask_restplus import Resource, Api
from flask_restplus import fields

from users_commands import get_all_users, add_user, remove_user

app = Flask(__name__)
api = Api(app,version='1.0', title='API for users management', description='A demonstration of a Flask RestPlus powered API')

os_user = api.model('User', {
    'username': fields.String(required=True, description='username to be created', example='operativos'),
    'password': fields.String(required=True, description='password for the username', example='mysecurepass'),
})

ns = api.namespace('v1.0/users', description='Operations related to create users')

@ns.route('/')
#@api.route('/v1.0/users')
class UserCollection(Resource):
    @api.response(200, 'List of users successfully returned.')
    def get(self):
        """ returns a list of users """
        list = {}
        list["users"] = get_all_users()
        return json.dumps(list), 200

    @api.response(201, 'User successfully created.')
    @api.expect(os_user)
    def post(self):
        """ creates a user """
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

    @api.response(501, 'Not implemented.')
    def put(self):
        """ not implemented """
        return "not implemented", 501 # Not found

    @api.response(201, 'All users were deleted.')
    @api.response(400, 'Some users were not deleted.')
    def delete(self):
        """ deletes a user """
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

Para ejecutar el script ejecute el siguiente comando

```
(flask_env) $ python users.py
```

Abra un navegador en la dirección **http://127.0.0.1:8088**, podrá visualizar la documentación para los endpoints implementados. Cancele la ejecución del script presionando la combinación de teclas **CTRL+C**.

### Actividades
1. Investigue acerca de la iniciativa OpenAPI, ¿Cúal es su objetivo?, ¿Quienes la conforman?, ¿Cúal es su relación con swagger?
2. Adicione endpoints de ejemplos para el manejo de parámetros en el path **/users/<username:string>** y parámetros tipo query **/users?group=root**
3. Investigue como exportar en un archivo con formato **yaml** la documentación obtenida al usar **flask_restplus**

### Enlaces sugeridos
How to add Swagger OpenAPI to your REST API documentation - https://www.youtube.com/watch?v=wC5hxY0RItQ  
Documentación de flask_restplus - https://flask-restplus.readthedocs.io/en/stable/   
Ejemplo petstore - http://petstore.swagger.io/
