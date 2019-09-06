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
  # CUANDO acceda a la url GET /users.py
  # ENTONCES obtenga un listado de usuarios del sistema
  assert 0

