import time
import requests
from unittest.mock import patch
from mockplay import external_api_call, slow_function

@patch('mockplay.slow_function')
def test_get(mock_slow_function):
  mock_slow_function.return_value = 12
  response = external_api_call()
  assert response == 12