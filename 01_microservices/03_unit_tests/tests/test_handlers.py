import pytest
import mock
import connexion
from gm_analytics import handlers


@pytest.fixture(scope='module')
def client():
    flask_app = connexion.FlaskApp(__name__)
    with flask_app.app.test_client() as c:
        yield c

@pytest.fixture()
def user_role():
    return 'collaborator'

def test_get_health(client):
    # GIVEN no query parameters or payload
    # WHEN I access to the url GET /health
    # THEN the HTTP response is 404 not found
    response = client.get('/health')
    assert response.status_code == 404

def test_get_user_info():
    # GIVEN not query parameters or payload
    # WHEN I access to the url GET /users/john.doe
    # THEN the information for the user must be returned
    user_info = handlers.get_user_info('john.doe')
    assert user_info['username'] == 'john.doe'
    assert user_info['id'] == '123'
    assert user_info['role'] == 'admin'
    assert len(user_info) == 3

def test_get_user_info_with_patch(mocker, user_info):
    # GIVEN not query parameters or payload
    # WHEN I access to the url GET /users/john.doe
    # THEN the information for the user must be returned
    mocker.patch.object(handlers, 'query_role', return_value=user_role)
    user_info = handlers.get_user_info('john.doe')
    assert user_info['username'] == 'john.doe'
    assert user_info['id'] == '123'
    assert user_info['role'] == 'collaborator'
    assert len(user_info) == 3