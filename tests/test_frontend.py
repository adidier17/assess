import pytest

def test_index(client):
    """Test index"""
    response = client.get('/')
    assert response.status_code == 200
