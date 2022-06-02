from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Code below is database configuration

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")    #"sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Code below is instantiating db object.
db = SQLAlchemy(app)

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

# Code below deletes all exsisting tables and creates the ones defined in the Models 
#(this will probably be changed becasue we dont want to delete existing data in database)
db.drop_all()
db.create_all()

#Creating web pages

@app.route('/')
@app.route('/home')
def home():
    return 'This is home page/ login page'

@app.route('/signUp')
def signUp():
    return 'This is sign up page'

@app.route('/viewMusic')
def viewMusic():
    return 'This is View music page'


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)