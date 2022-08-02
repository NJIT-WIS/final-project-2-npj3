import logging
import os
from pprint import pprint

from sqlalchemy import func

from app import db
from app.db.models import User, Song


# testing links for songs only appear for logged-in users
def test_request_main_menu_links_authenticated(client, client_authenticated):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/songs/upload"' in response.data
    assert b'href="/songs"' in response.data


# testing that an authenticated user can access songs
def test_browse_songs_authenticated(client, client_authenticated):
    response = client.get("/songs")
    assert response.status_code == 200


# testing that uploads require an authenticated users
def test_upload_authenticated(client, client_authenticated):
    response = client.get("/songs/upload")
    assert response.status_code == 200


# testing that songs is not accessible by unauthenticated users
def test_browse_songs_unauthenticated(client):
    response = client.get("/songs")
    assert response.status_code == 302


# testing that upload is not accessible by unauthenticated users

def test_upload_unauthenticated(client):
    response = client.get("/songs/upload")
    assert response.status_code == 302


# testing that songs can be added in the database directly
def test_adding_song(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        db.session.add(song)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        song = Song.query.filter_by(artist="Keith").first()
        # asserting that the user retrieved is correct
        assert song.title == 'Great song'
        # this is how you get a related record ready for insert


# testing that songs can be deleted
def test_deleting_song(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        db.session.add(song)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        song = Song.query.filter_by(artist="Keith").first()
        # asserting that the user retrieved is correct
        assert song.title == 'Great song'
        # this is how you delete the song
        db.session.delete(song)
        assert db.session.query(Song).count() == 0


# testing that songs can be related to a users
def test_relate_song_to_user(application, add_user):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        user = User.query.filter_by(email='test@test.com').first()
        user.songs.append(song)
        db.session.add(user)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        assert len(user.songs) == 1
        # asserting that the user retrieved is correct
        # this is how you delete the song


# testing update of a song title
def test_update_song(application, add_user):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        song = Song(artist="Keith", title="Great song")
        # add it to get ready to be committed
        db.session.add(song)
        # call the commit
        db.session.commit()

        # just update the title and add it again.
        song.title = "Updated Great Song"
        db.session.add(song)
        db.session.commit()
        song_from_query = Song.query.filter_by(artist="Keith").first()
        assert song_from_query.title == "Updated Great Song"


# A count of songs by artists
def test_song_artist_count(application, client, client_authenticated):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    file = os.path.join(BASE_DIR, "test_data", "my_music.csv")
    data = {
        'file': (open(file, 'rb'), file)
    }
    response = client.post('/songs/upload', data=data)

    with application.app_context():
        result = db.session.query(func.count(Song.artist), Song.artist).group_by(Song.artist).all()
    pprint(result)
