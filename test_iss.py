import pytest
import requests
from unittest.mock import patch
from times import iss_passes

# Sample mock response data
mock_response_data = {
    "passes": [
        {"startUTC": 1609459200, "endUTC": 1609459800},
        {"startUTC": 1609462800, "endUTC": 1609463400}
    ]
}

@patch('times.requests.get')
def test_iss_passes(mock_get):
    # Configure the mock to return a response with our mock data
    mock_get.return_value.json.return_value = mock_response_data
    
    api_key = "test_api_key"
    lat = 56
    lon = 0
    result = iss_passes(api_key, lat, lon)
    
    expected = [
        ("2021-01-01 00:00:00", "2021-01-01 00:10:00"),
        ("2021-01-01 01:00:00", "2021-01-01 01:10:00")
    ]
    
    assert result == expected
