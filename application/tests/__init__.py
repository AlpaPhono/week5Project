'''
from flask_testing import TestCase
from application import app, db


class TestBase(TestCase):
  def create_app(self):
    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///",
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True,
        WTF_CSRF_ENABLED=False
    )
    return app

  def setUp(self):
    #is run before each unit test, adds dummy data to the database
        db.create_all()
        #adding an artist to the db
        artist1 = Artist(stage_name = '50Cent')
        db.sesson.add(artist1)
        db.session.commit()
        # adding songs to the db
        song1 = Songs(
            song_name = 'InDaClub',
            song_link = 'https://www.youtube.com/watch?v=5qm8PH4xAss',
            song_genre = 'RAP',
            artist_id = 1
            )

  def tearDown(self):
    db.session.remove()
    db.drop_all()

'''