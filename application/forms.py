
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, SelectField 



class SignupForm(FlaskForm):
    stage_name = StringField('Stage Name', [validators.length(min=1, max=25), validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()]) 
    password = PasswordField('New Password',[validators.DataRequired(),validators.EqualTo('confirm',message = 'Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Confirm Sign up')

class LoginForm(FlaskForm):
     stage_name = StringField('Stage Name', [validators.length(min=1, max=25), validators.DataRequired()])
     password = PasswordField('Password',[validators.DataRequired()])
     submit = SubmitField('Log In')

class SongForm(FlaskForm):
    song_name = StringField('Name of your Song', [validators.length(min =1, max=25), validators.DataRequired()])
    song_Link = StringField('Song Link',[validators.length(min=1, max=40)])
    song_genre = SelectField('Genre', choices= ['RAP','RNB','SOUL','Afrobeats','POP','COUNTRY','COUNTRY','JAZZ'])
    #artist_id = StringField('AUTO COMPLETED', [validators.length(min=1,max=25),validators.DataRequired()])
    submit = SubmitField('Submit')

class UpdateSongForm(FlaskForm):
    song_name = StringField('Name of your Song', [validators.length(min =1, max=25), validators.DataRequired()])
    #artist_id = StringField('AUTO COMPLETED', [validators.length(min=1,max=25),validators.DataRequired()])
    submit = SubmitField('Submit')