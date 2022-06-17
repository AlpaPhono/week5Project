from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Artist, Songs
from application.forms import SignupForm, LoginForm, SongForm, UpdateSongForm
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        #defines the flask configuration for the duration of the test
        app.config.update(
            SQLALCHEMY_DATABASE_URI = "sqlite:///",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED = False
        )
        return app
    
    def teardown(self):
        db.session.remove()
        db.drop_all()
    
        # is run after each unit test. wipes the test database to prevent data from previous tests persisting and causing false positives

    def setUp(self):
        #is run before each unit test, adds dummy data to the database
        db.create_all()
        #adding an artist to the db
        artist1 = Artist(stage_name ='50cent', email = '50Cent@Gunit.com', password = 'getrich')
        db.session.add(artist1)
        db.session.commit()
        # adding songs to the db
        song1 = Songs(
            song_name = 'InDaClub',
            song_link = 'https://www.youtube.com/watch?v=5qm8PH4xAss',
            song_genre = 'RAP',
            artist_id = 1
            )
        
    def teardown(self):
        db.session.remove()
        db.drop_all()
    
        # is run after each unit test. wipes the test database to prevent data from previous tests persisting and causing false positives


class TestAdd(TestBase):
    def test_add_artist(self):
        # test artist addition
        response = self.client.post(url_for('signUp'),
            data =dict(stage_name = 'Skepta', email ='skepta@skepta.com',password='bbk', confirm = 'bbk'), # this is for your forms variables not your models.
            follow_redirects = True )
        
        #assert Artist.query.filter_by(stage_name ='Skepta').id == 2
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'Skepta',response.data)
        self.assertIn(b'skepta@skepta.com',response.data)
        self.assertIn(b'bbk',response.data)    #I had to cut this out for it to work? Why?
    
    

class TestAddSong(TestBase):
    pass

class TestRead(TestBase):
        pass

class TestDeleteSong(TestBase):
    pass

class TestUpdateSongName(TestBase):
    pass



