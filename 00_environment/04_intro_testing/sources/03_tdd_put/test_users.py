import pytest
import users
import unittest

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
