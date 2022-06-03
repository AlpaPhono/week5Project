from application import db

# Code below is  Creating database Models
class Artist(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    stage_name=db.Column(db.String(30))
    email = db.Column(db.String(30))
    songs = db.relationship('Song', backref = 'artistbr')

class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(30))
    song_genre = db.Column(db.String(30))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.user_id'), nullable = False)