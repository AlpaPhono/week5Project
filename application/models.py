from application import db

# Code below is  Creating database Models
class Artist(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    stage_name=db.Column(db.String(30))
    email = db.Column(db.String(30))
    password = db.Column(db.String(16))
    songs = db.relationship('Songs', backref = 'artistbr')


class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(30))
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