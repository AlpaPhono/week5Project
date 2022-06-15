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


@app.route('/music', methods = ['GET','POST'])
def music():

    message = ''
    form = SongForm()

    if request.method == 'POST' and form.validate_on_submit():
        pass

   

       

    return 'This is View music page'

