import pytest
import users
#import json

@pytest.fixture
def app():
  return users.app

@pytest.fixture
def client(app):
  return app.test_client()

def test_user(client):
  # DADO un servicio web
  # CUANDO acceda a la url GET /users
  # ENTONCES obtenga un listado de usuarios del sistema
  response = client.get('/users') #,follow_redirects=True)
  #print(response.data)
  assert "root" in response.data #.decode("utf-8")
  #assert 0
