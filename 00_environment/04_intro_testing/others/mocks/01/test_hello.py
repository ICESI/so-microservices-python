MOCK_ENCODING = "mock-encoding"

def test_encoding_header(test_client, mock_encoding_request):
  """
  GIVEN: A flask hello app
         A mock request handler
  WHEN: I GET the /hacerk_news_encoding route
  THEN: The response should be the expected Content-Encoding
  """
  response = test_client.get("/hacker_news_encoding")
  assert response.data.decode("utf-8") == MOCK_ENCODING

class MockEncodingResponse:
  def __init__(self):
    self.headers = ("Content-Encoding": MOCK_ENCODING)

  def _mock_get(url):
    assert url = "https://news.ycombinator.com"
    return MockEncodingResponse()

@pytest.fixture
def mock_encoding_request(monkeypatch):
  monkeypatch.setattr("request.get", mock_get)
