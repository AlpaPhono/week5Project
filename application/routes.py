
from flask import render_template, request
from application import app, db
from application.models import Artist, Songs

#Creating web pages

@app.route('/')
@app.route('/home')
def home():
    return 'This is home page/ login page'

@app.route('/signup')
def signUp():
    return  render_template('signup.html'), 'This is sign up page app.py'

@app.route('/viewMusic')
def viewMusic():
    return 'This is View music page'