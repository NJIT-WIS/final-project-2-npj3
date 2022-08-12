"""This makes the test configuration setup"""

# pylint: disable=redefined-outer-name, line-too-long, no-member, unused-argument
import os.path
# from pprint import pprint

from app.db.models import Song


def test_upload_textfile(application, client):
    """This makes the test configuration setup"""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    file = os.path.join(base_dir, "test_data", "my_music.csv")
    data = {
        'file': (open(file, 'rb'), file)
    }
    response = client.post('/songs/upload', data=data)
    # check that the songs were added to the database
    with application.app_context():
        songs = Song.query.all()

    assert len(songs) == 0
    assert response.status_code == 302
