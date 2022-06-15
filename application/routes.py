from email import message
from flask import render_template, request, url_for, redirect
from application import app, db
from application.forms import LoginForm, SignupForm, SongForm
from application.models import Artist, Songs
from flask_login import login_user, login_required, logout_user, current_user

#Creating web pages

@app.route('/')
@app.route('/home', methods = ['GET','POST'])
def home():
    form = LoginForm()
    message = ''

    if request.method == 'POST' and form.validate_on_submit:
        stage_name = form.stage_name.data
        password = form.password.data
        log_artist = Artist.query.filter_by(stage_name = stage_name).first()
        if log_artist:

            if log_artist.password == password:
                message ='logged in successfully'
                login_user(log_artist)
                return redirect(url_for('music'))
            else:
                message = 'Incorrect Password'

        else:
            message = 'No Such User'

    return render_template('index.html', form = form, message = message, artist = current_user)

@app.route('/signup', methods = ['GET','POST'])
def signUp():

    message = ''
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():

        email = form.email_.data
        password = form.password.data
        stage_name = form.stage_name.data
        artist = Artist.query.filter_by(email = email).first()
        if artist:
            message = 'Email or Stage Name Already Exists'
        else:    

            new_artist = Artist(stage_name = form.stage_name.data, email = form.email_.data,password = form.confirm.data)
            db.session.add(new_artist)
            db.session.commit()
            message = f'thank you {new_artist.stage_name}'
    

    return  render_template('signup.html', form = form, message = message)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/music', methods = ['GET','POST'])
@login_required
def music():

    message = ''
    form = SongForm()
    link = form.song_Link.data
    user_id = current_user.user_id
    all_songs = Songs.query.all()


    if request.method == 'POST' and form.validate_on_submit():
        song = Songs.query.filter_by(song_link = link).first()
        print(song)
        if song:
            message = "Can't have multiple songs with the same link" 
            return redirect(url_for('music'))
        else:
            new_song = Songs(song_name = form.song_name.data, song_link = form.song_Link.data, song_genre = form.song_genre.data, artist_id = user_id)
       
            db.session.add(new_song)
            db.session.commit()
            message = f'We have added {new_song.song_name}'
    
            print(new_song.song_name)

    return render_template('music.html', form = form, message = message, current_artist = current_user, all_songs = all_songs, song_name = Songs().song_name)

