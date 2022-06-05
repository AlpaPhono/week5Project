
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators 



class SignupForm(FlaskForm):
    stage_name = StringField('Stage Name', [validators.length(min=1, max=25), validators.DataRequired()])
    email_ = StringField('Email', [validators.Email(), validators.DataRequired()]) # single trailing underscore to avoid conflict with python key words
    password = PasswordField('New Password',[validators.DataRequired(),validators.EqualTo('confirm',message = 'Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Confirm Sign up')

class LoginForm(FlaskForm):
     stage_name = StringField('Stage Name', [validators.length(min=1, max=25), validators.DataRequired()])
     password = PasswordField('Password',[validators.DataRequired()])
     submit = SubmitField('Log In')

    