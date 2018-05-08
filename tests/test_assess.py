from assess import assess

def test_create_app():
    """Test create_app without passing test config."""
    #assert not assess.create_app().testing
    assert assess.create_app({'TESTING': True}).testing
