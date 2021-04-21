#importing required functions from flask
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

#creating an object of type Flask and assigning to the variable named "app"
app = Flask(__name__)

app.config['SECRET_KEY'] = '007e6781df103d67942da98fcc6c6ccc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog.models import User, Post
from flaskblog import routes