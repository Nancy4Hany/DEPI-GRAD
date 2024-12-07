import pytest
from unittest.mock import patch
from app import app  # Ensure this path is correct


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@patch('app.Redis')  # Mocking Redis in the vote.app module
def test_hello_post(mock_redis, client):
    # Simulate a successful response from Redis
    mock_redis.return_value.rpush.return_value = None
    # Simulate successful rpush

    response = client.post('/', data={'vote': 'Cats'})

    assert response.status_code == 200
    assert b'Cats' in response.data
    # Check that 'Cats' is in the response
    assert b'Dogs' in response.data
    # Check that 'Dogs' is also in the response


@patch('app.Redis')
def test_hello_get(mock_redis, client):
    response = client.get('/')

    assert response.status_code == 200
    assert b'Cats' in response.data
    # Check that option_a is in the response
    assert b'Dogs' in response.data
    # Check that option_b is in the response
