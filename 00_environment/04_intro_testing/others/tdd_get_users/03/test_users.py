import pytest
import users

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
  response = client.get('/users')
  assert "root" in response.data.decode("utf-8")

