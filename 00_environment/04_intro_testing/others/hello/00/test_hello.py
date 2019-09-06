from my_flask_app import create_app

@pytest.fixture
def app():
  app = create_app("test")
  return app

@pytest.fixture
def app_client(app):
  client = app.test_client()
  return client

# GIVEN: app_client
def test_hello_route(app_client):
  
  # WHEN:
  reply = app_client.get("/hello")

  # THEN:
  assert reply.data == "Hello World"

"""
GIVEN: A flask hello app
WHEN: I GET the hello/ route
THEN: The response should be "hello world"
"""
