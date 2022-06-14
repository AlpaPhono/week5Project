from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Code below is database configuration

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRETKEY')

# Code below is instantiating db object.
db = SQLAlchemy(app)

from application import routes