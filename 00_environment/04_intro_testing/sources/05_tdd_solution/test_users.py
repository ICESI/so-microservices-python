import pytest
import users
import unittest
#import json

@pytest.fixture
def app():
  return users.app

@pytest.fixture
def client(app):
  return app.test_client()

def test_post_users(client):
  # DADO un servicio web e informacion de un usuario
  # CUANDO acceda a la url POST /users
  # ENTONCES se debe crear un usuario en el sistema operativo con la informacion enviada
  user = {'username': 'myuser', 'password': 'mypasswd'}
  response = client.post('/v1.0/users',data = user)
  assert b"user created" in response.data
  assert response.status_code == 201

def test_get_users(client):
  # DADO un servicio web
  # CUANDO acceda a la url GET /users
  # ENTONCES obtenga un listado de usuarios del sistema
  response = client.get('/v1.0/users') #,follow_redirects=True)
  assert "myuser" in response.data #.decode("utf-8")
  assert response.status_code == 200

def test_update_users(client):
  # DADO un usuario existente e informacion a actualizar
  # CUANDO acceda a la url UPDATE /users
  # ENTONCES actualice el usuario existente con la informacion enviada
  response = client.update('/v1.0/users')
  assert "not implemented" in response.data
  assert response.status_code == 501

def test_delete_users(client):
  # DADO un servicio web y una lista de usuarios
  # CUANDO acceda a la url DELETE /users
  # ENTONCES eliminar todos los usuarios excepto los de la lista
  response = client.delete('/v1.0/users')
  assert "all users were deleted" in response.data
  assert response.status_code == 200
