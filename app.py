from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")    #"sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

db.drop_all()
db.create_all()

if __name__ == '__name__':
    app.run(debug = True, host='0.0.0.0')