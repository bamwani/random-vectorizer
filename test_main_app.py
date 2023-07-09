import pytest
from main_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_random_vector(client):
    """
    Tests the /random_vector endpoint.

    Args:
        client: The Flask test client.

    Test Cases:
        - Valid request: Tests if a valid request returns a random vector with the correct format.
        - No sentence provided: Tests if an error is returned when no sentence is provided.
        - Security headers: Tests if the response contains the expected security headers.
    """
    # Test case: Valid request
    response = client.post('/random_vector', data={'sentence': 'This is a test sentence'})
    assert response.status_code == 200
    vector = response.get_json()
    assert isinstance(vector, list)
    assert len(vector) == 500
    print("Valid request test passed.")

    # Test case: No sentence provided
    response = client.post('/random_vector')
    assert response.status_code == 400
    error = response.get_json()
    assert 'error' in error
    assert error['error'] == 'No sentence provided.'
    print("No sentence provided test passed.")

    # Test case: Security headers
    response = client.post('/random_vector', data={'sentence': 'This is a test sentence'})
    assert response.status_code == 200
    headers = response.headers
    assert headers.get('Strict-Transport-Security') == 'max-age=31536000; includeSubDomains; preload'
    assert headers.get('X-Content-Type-Options') == 'nosniff'
    assert headers.get('X-Frame-Options') == 'SAMEORIGIN'
    assert headers.get('X-XSS-Protection') == '1; mode=block'
    assert headers.get('Content-Security-Policy') == "default-src 'self'"
    print("Security headers test passed.")
