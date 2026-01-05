import pytest
import requests
from src.currency_converter import get_exchange_rate, convert_currency, cache


# MockResponse class to simulate the response from requests.ge
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        print("MockResponse.json() called")
        return self.json_data

    def raise_for_status(self):
        print(f"MockResponse.raise_for_status() called. Status code: {self.status_code}")
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f"{self.status_code} Client Error")


# Fixture to clear the cache before each test
@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()


# Fixture to mock the requests.get method
@pytest.fixture
def mock_requests_get(monkeypatch):
    def _mock_get(*args, **kwargs):
        return MockResponse({"rates": {"EUR": 0.85}, "time_last_updated": 1609459200}, 200)
    monkeypatch.setattr("requests.get", _mock_get)


# Test to check if get_exchange_rate returns the correct rate and timestamp
def test_get_exchange_rate_success(mock_requests_get):
    rate, timestamp = get_exchange_rate('USD', 'EUR')
    assert rate == 0.85
    assert timestamp == 1609459200


# Test to check if get_exchange_rate raises a ValueError for an invalid currency code
def test_get_exchange_not_found(mock_requests_get):
    with pytest.raises(ValueError):
        get_exchange_rate('USD', 'XYZ')


# Test to check if get_exchange_rate raises an HTTPError for a failed request
def test_get_exchange_rate_failure(monkeypatch):
    def mock_get_failure(*args, **kwargs):
        return MockResponse({}, 400)
    monkeypatch.setattr("requests.get", mock_get_failure)
    
    with pytest.raises(requests.exceptions.HTTPError):
        get_exchange_rate('USD', 'EUR')


# Test to check if convert_currency returns the correct converted amount
def test_convert_currency(mock_requests_get):
    rate, timestamp = get_exchange_rate('USD', 'EUR')
    amount = convert_currency(100, rate)
    assert amount == 85.0