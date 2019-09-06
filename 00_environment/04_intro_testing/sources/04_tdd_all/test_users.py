import pytest
import users
import unittest

@pytest.fixture
def client():
  return users.app.test_client()

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
