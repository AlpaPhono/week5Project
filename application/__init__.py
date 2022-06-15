from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

app = Flask(__name__)

# Code below is database configuration

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRETKEY')

# Code below is instantiating db object.
db = SQLAlchemy(app)

from application.models import Artist


from application import routes

login_manager = LoginManager()
login_manager.login_view = 'music'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return Artist.query.get(int(id))