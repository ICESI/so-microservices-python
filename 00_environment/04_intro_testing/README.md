### Introducción a pruebas unitarias con pytest
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Introducción a pruebas unitarias con pytest  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Conocer tecnologías para la creación de pruebas unitarias
* Crear pruebas unitarias para validar servicios web

### Introducción
TDD (Test Driven Development) es un proceso de desarrollo de software que se basa en la repetición de ciclos
cortos de desarrollo (implementación de funcionalidades). Los requerimientos constituyen casos de prueba específicos y el software es mejorado en cada iteración para pasar las pruebas.

Pytest es un framework de python para la escritura de pruebas. Pytest tiene características como:
descubrimiento de archivos con pruebas, soporte para diferentes versiones de python, definir porciones de código que se ejecutan antes o después de una prueba (a nivel de módulos, clases y funciones) y soporte para para plugins.

### Caracteristicas de pytest

#### Instalación
Para instalar pytest puede emplear el gestor de paquetes **pip**

```
# su python_user
$ cd ~/envs
$ . flask_env/bin/activate
$ pip install pytest
```

#### Ejemplo simple
Pytest permite la escritura de pruebas desde simples hasta complejas

Cree un directorio para almacenar los archivos del ejemplo

```
$ mkdir -p intro_testing/01_intro_pytest/
$ cd intro_testing/01_intro_pytest
```

Cree un archivo con el código fuente, de nombre **operation.py**

```python
def add(x,y):
  return x+y
```

Cree un archivo con la prueba, de nombre **test_operation.py**

```python
from operation import add

def test_add():
  assert add(2,4) == 6
```

Ejecute el comando py.test para obtener el resultado de la prueba. Ejecute el comando desde el directorio donde almaceno los archivos **operation.py** y **test_operation.py**

```
.../01_intro_pytest$ py.test -v
```

```
============================= test session starts ==============================
platform linux2 -- Python 2.7.12+, pytest-2.9.2, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
cachedir: .cache
rootdir: /home/python_user/intro_testing/01_intro_pytest, inifile:
collected 1 items

test_operation.py::test_add PASSED

=========================== 1 passed in 0.03 seconds ===========================
```

#### Auto-Discovery
Pytest puede encontrar en una estructura de directorios los archivos que contengan pruebas. Estos archivos deben tener la palabra **test** al principio o al final de su nombre. Al ejecutar el comando para ejecutar las pruebas desde afuera del directorio 01_intro_pytest, los resultados son los mismos.

```
.../intro_testing$ py.test -v
```

```
============================= test session starts ==============================
platform linux2 -- Python 2.7.12+, pytest-2.9.2, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
cachedir: .cache
rootdir: /home/python_user/intro_testing/01_intro_pytest, inifile:
collected 1 items

test_operation.py::test_add PASSED

=========================== 1 passed in 0.03 seconds ===========================
```

En caso de existir otros directorios o subdirectorios con archivos de prueba, pytest los ejecutará.

#### Fixtures
Pytest permite definir porciones de código que se ejecutan antes, después ó que permiten inicializar datos ú objetos para la realización de una prueba

**operation.py**
```python
def add(x,y):
  return x+y
```

**test_operation.py**
```python
from operation import add
import pytest

@pytest.fixture
def message(request):
  print('\n[start] start testing')
  def fin():
    print('\n[end] end testing')
  request.addfinalizer(fin)

@pytest.fixture
def input_data():
  data = {'a': 2, 'b':4}
  return data

def test_add(input_data,message):
  assert add(input_data['a'],input_data['b']) == 6
```

Ejecute el comando py.test para obtener el resultado de la prueba.

```
.../02_intro_fixtures$ py.test -v -s
```

```
================================================= test session starts =================================================
platform linux2 -- Python 2.7.12+, pytest-2.9.2, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
cachedir: .cache
rootdir: /home/python_user/intro_testing/02_intro_fixtures, inifile:
collected 1 items

test_operation.py::test_add
[start] start testing
PASSED
[end] end testing
============================================== 1 passed in 0.01 seconds ===============================================
```

### Desarrollo

#### Cliente para pruebas
Flask cuenta con un método para la declaración de un objeto cliente el cual facilita la realización de las pruebas.

```python
import pytest
import users

@pytest.fixture
def client():
  return users.app.test_client()
```

Sobre el objeto retornado por **test_client()** se pueden invocar los distintos métodos HTTP para la realización de las pruebas. Para mayor información consulte las referencias al final de esta guía.

#### TDD para el método PUT
A continuación se muestra la prueba para el método PUT de la API **/v1.0/users/**

**test_users.py**
```python
import pytest
import users

@pytest.fixture
def client():
  return users.app.test_client()

def test_update_users(client):
  # GIVEN an user and a new password
  # WHEN I access to the url UPDATE /users
  # THEN user must have the new password
  response = client.put('/v1.0/users')
  assert "not implemented" in response.data.decode("utf-8")
  assert response.status_code == 501
```

**users.py**
```python
from flask import Flask

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not implemented", 501

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
```

Ejecute el comando py.test para obtener el resultado de  la prueba
```
.../03_tdd_put$ py.test -v
```

```
========================================== test session starts ==========================================
platform linux2 -- Python 2.7.12+, pytest-2.9.2, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
cachedir: .cache
rootdir: /home/python_user/intro_testing/03_tdd_put, inifile:
collected 1 items

test_users.py::test_update_users PASSED

======================================= 1 passed in 0.31 seconds ========================================
```

#### TDD caso general
A continuación se muestran las líneas de código escritas anteriormente para el método PUT junto con las líneas de código para los métodos restantes POST, GET y DELETE de la API **/v1.0/users/**.
Se deja como actividad al estudiante completar el código fuente que pasa todas la pruebas.

**user_commands.py**
```python
def get_all_users():
  return None

def add_user(username,password):
  return None

def remove_user(username):
  return None
```

**users.py**
```python
from flask import Flask
from user_commands import get_all_users, add_user, remove_user

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['POST'])
def create_user():
  return "not implemented", 501

@app.route(api_url+'/users',methods=['GET'])
def read_user():
  return "not implemented", 501

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not implemented", 501

@app.route(api_url+'/users',methods=['DELETE'])
def delete_user():
  return 'not implemented', 501

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
```

**test_users.py**
```python
import pytest
import users

@pytest.fixture
def app():
  return users.app

@pytest.fixture
def client(app):
  return app.test_client()

def test_post_users(client):
  # GIVEN a webservice and a username and password
  # WHEN I access to the url POST /users
  # THEN a user must be created
  user = {'username': 'myuser', 'password': 'mypasswd'}
  response = client.post('/v1.0/users',data = user)
  assert "user created" in response.data.decode("utf-8")
  assert response.status_code == 201

def test_get_users(client):
  # GIVEN a webservice
  # WHEN I access to the url GET /users
  # THEN a list of operating system users must be returned
  response = client.get('/v1.0/users') #,follow_redirects=True)
  assert "myuser" in response.data.decode("utf-8")
  assert response.status_code == 200

def test_update_users(client):
  # GIVEN an user and a new password
  # WHEN I access to the url UPDATE /users
  # THEN user must have the new password
  #user_info = {'username': 'myuser', 'password': 'mynewpasswd'}
  response = client.put('/v1.0/users')
  assert "not implemented" in response.data.decode("utf-8")
  assert response.status_code == 501

def test_delete_users(client):
  # GIVEN a webservice and a list of users
  # WHEN I access to the url DELETE /users
  # THEN all users must be deleted except the ones from the list
  response = client.delete('/v1.0/users')
  assert "all users were deleted" in response.data.decode("utf-8")
  assert response.status_code == 200
```

Ejecute el comando py.test para obtener el resultado de las pruebas. Observe como fallan 3 de los 4 casos de prueba.
```
.../04_tdd_all$ py.test -v
```

```
================================================= test session starts =================================================
platform linux2 -- Python 2.7.12+, pytest-2.9.2, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
cachedir: .cache
rootdir: /home/python_user/intro_testing/04_tdd_all, inifile:
collected 4 items

test_users.py::test_post_users FAILED
test_users.py::test_get_users FAILED
test_users.py::test_update_users PASSED
test_users.py::test_delete_users FAILED

====================================================== FAILURES =======================================================
___________________________________________________ test_post_users ___________________________________________________

client = <FlaskClient <Flask 'users'>>

    def test_post_users(client):
      # GIVEN a webservice and a username and password
      # WHEN I access to the url POST /users
      # THEN a user must be created
      user = {'username': 'myuser', 'password': 'mypasswd'}
      response = client.post('/v1.0/users',data = user)
>     assert "user created" in response.data.decode("utf-8")
E     assert 'user created' in 'not implemented'
E      +  where 'not implemented' = <built-in method decode of str object at 0x7fa83df1fed8>('utf-8')
E      +    where <built-in method decode of str object at 0x7fa83df1fed8> = 'not implemented'.decode
E      +      where 'not implemented' = <Response 15 bytes [501 NOT IMPLEMENTED]>.data

test_users.py:15: AssertionError
___________________________________________________ test_get_users ____________________________________________________

client = <FlaskClient <Flask 'users'>>

    def test_get_users(client):
      # GIVEN a webservice
      # WHEN I access to the url GET /users
      # THEN a list of operating system users must be returned
      response = client.get('/v1.0/users') #,follow_redirects=True)
>     assert "myuser" in response.data.decode("utf-8")
E     assert 'myuser' in 'not implemented'
E      +  where 'not implemented' = <built-in method decode of str object at 0x7fa83df1ff48>('utf-8')
E      +    where <built-in method decode of str object at 0x7fa83df1ff48> = 'not implemented'.decode
E      +      where 'not implemented' = <Response 15 bytes [501 NOT IMPLEMENTED]>.data

test_users.py:23: AssertionError
__________________________________________________ test_delete_users __________________________________________________

client = <FlaskClient <Flask 'users'>>

    def test_delete_users(client):
      # GIVEN a webservice and a list of users
      # WHEN I access to the url DELETE /users
      # THEN all users must be deleted except the ones from the list
      response = client.delete('/v1.0/users')
>     assert "all users were deleted" in response.data.decode("utf-8")
E     assert 'all users were deleted' in 'not implemented'
E      +  where 'not implemented' = <built-in method decode of str object at 0x7fa83de9a068>('utf-8')
E      +    where <built-in method decode of str object at 0x7fa83de9a068> = 'not implemented'.decode
E      +      where 'not implemented' = <Response 15 bytes [501 NOT IMPLEMENTED]>.data

test_users.py:40: AssertionError
========================================= 3 failed, 1 passed in 0.32 seconds ==========================================
```

### Actividades

1. Siguiendo un proceso de TDD, complete la implementación para las funciones restantes de la API **/v1.0/users**
2. Al completar el punto anterior responda a la pregunta: ¿Se han tenido en cuenta todos los casos posibles de prueba?, ¿Cuales casos faltarían por definir?
3. Investigue acerca de BDD y plantee alguno de los endpoints de la API **/v1.0/users** en dicho formato.

### Referencias
https://www.agilealliance.org/glossary/tdd/  
http://doc.pytest.org/en/latest/  
http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/  
http://www.slideshare.net/ereyes01/tdd-in-python-with-pytest-43671276  
http://werkzeug.pocoo.org/docs/0.10/test/#werkzeug.test.Client  
http://pythonhosted.org/behave/

<!--
https://github.com/nestorsalceda/mamba  
https://github.com/delfick/nose-of-yeti
py.test --genscript=mypytest
python -m pytest
-->
