import pytest

from flask import json
from unittest.mock import MagicMock

#TODO
def mock_tika_wrapper(buf):
    """Mock tika_wrapper"""
    return "mock"

def test_predict_get(client, monkeypatch):
    """Test predict using the GET method"""
    monkeypatch.setattr("assess.api.util.tika_wrapper.parse_from_buffer", mock_tika_wrapper)

    response = client.get('/predict/?text=test')
    d = json.loads(response.data)
    assert "predictions" in d
    assert "text_extracted" in d
    assert "references" in d


# def test_predict_post(client):
#     pass
