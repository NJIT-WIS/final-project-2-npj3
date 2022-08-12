"""This makes the test configuration setup"""


# pylint: disable=redefined-outer-name, line-too-long, no-member, unused-argument
def test_remove_meant_to_fail(client):
    """This makes the index page"""
    response = client.get("/nowork")
    assert response.status_code == 404
