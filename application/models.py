from application import db
from flask_login import UserMixin

# Code below is  Creating database Models
class Artist(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    stage_name=db.Column(db.String(30), unique = True)
    email = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(16))
    songs = db.relationship('Songs', backref = 'artistbr')

    def get_id(self):
        return (self.user_id)


class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(30))
    song_link = db.Column(db.String(50), unique = True)
    song_genre = db.Column(db.String(30),)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.user_id'), nullable = False)

'''
class Artist(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    stage_name=db.Column(db.String(30))
    email = db.Column(db.String(30))
    songs = db.relationship('Song', backref = 'artistbr')
    def __init__(self,stageName,eMail):
        self.stage_name = stageName
        self.email = eMail
        
'''''