from email import message
from flask import render_template, request
from application import app, db
from application.forms import LoginForm, SignupForm, SongForm
from application.models import Artist, Songs

#Creating web pages

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = LoginForm()
    message = ''
    return render_template('index.html', form = form, message = message)

@app.route('/signup', methods = ['GET','POST'])
def signUp():

    message = ''
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        
        artist1 = Artist(stage_name = form.stage_name.data, email = form.email_.data,password = form.confirm.data)
        db.session.add(artist1)
        db.session.commit()
        message = f'thank you {artist1.stage_name}'
    

    return  render_template('signup.html', form = form, message = message)

'''
@app.route('/viewMusic', methods = ['GET','POST'])
def viewMusic():
    
    message = ''
    form = SongForm()

    if request.method == 'POST' and form.validate_on_submit():
        # not finished
        # i am tring to make an algorithim that checks who is uploading the song and 
        
        for name in Artist.stage_name():
            if 
        artist_id =
        song1 = Songs(song_name = form.song_name.data(), song_Link = form.song_Link.data())

        

        return render_template(),  'This is View music page'

'''
