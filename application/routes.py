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
    return redirect(url_for('/home'))


@app.route('/music', methods = ['GET','POST'])
#@login_required
def music():

    message = ''
    form = SongForm()

    if request.method == 'POST' and form.validate_on_submit():
        pass

   

       

    return render_template('music.html', form = form, message = message, artist = current_user)

