# pylint: disable=redefined-outer-name, line-too-long, no-member, unused-argument

"""This test the homepage"""

from flask import current_app

from app import db, User


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_registration(client):
    """Testing user registraiton"""
    with current_app.app_context():
        db.drop_all()
        db.create_all()
    response = client.post('/register', data={
        'email': 'steve@test.com',
        'password': 'password',
        'confirm': 'password'
    }, follow_redirects=True)

    with current_app.app_context():
        assert db.session.query(User).count() == 1

    assert response.status_code == 200
    assert response.request.path == '/login'


def test_login(client, application, add_user):
    response = client.post('/login', data={
        'email': 'test@test.com',
        'password': 'testtest',
    }, follow_redirects=True)
    assert response.status_code == 200
    response = client.get('/dashboard')
    assert response.status_code == 200


def test_registeristration_password_not_satisfied(client):
    # Testing registering with password not meeting requirements (min 6 characters)
    response = client.post("/register", data={"email": "steve@test.com", "password": "aaa", "confirm": "aaa"})
    # there should be no redirection
    assert response.status_code == 200
    assert b"Password" in response.data


def test_registeristration_email_wrong_format(client):
    # Testing registering with wrong email format
    response = client.post("/register", data={"email": "steve", "password": "aaaaa", "confirm": "aaaaa"})
    # there should be no redirection
    assert response.status_code == 200
    assert b"Email" in response.data


def test_register_with_mismatched_passwords(client):
    # Testing registration fail when passwords dont match
    response = client.post("/register", data={"email": "steve@joe.com", "password": "aaaaaa", "confirm": "bbbbbb"},
                           follow_redirects=True)
    # no redirection should happen
    assert response.status_code == 200
    assert b"Passwords must match" in response.data
