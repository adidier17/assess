import pytest

from flask import json

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_predict(client):
    response = client.get('/predict/')
    d = json.loads(response.data)
    assert "predictions" in d
    assert "text_extracted" in d
    assert "references" in d
