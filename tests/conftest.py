import pytest

from assess import assess

@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.
    """

    app = assess.create_app({'TESTING': True})

    yield app


@pytest.fixture
def client(app):
    """
    A test client for the app.
    """

    return app.test_client()
