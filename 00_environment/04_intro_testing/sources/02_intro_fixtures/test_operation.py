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
