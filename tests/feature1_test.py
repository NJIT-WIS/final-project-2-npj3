def test_remove_meant_to_fail(client):
    """This makes the index page"""
    response = client.get("/nowork")
    assert response.status_code == 200