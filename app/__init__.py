from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.secret_key = "v5mqvgwj"
# tell program where DB is located
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# define app to use with database
db.init_app(app)

from app import views, auth

# import models file to define class before we initialize the database
from .models import User, Bet

def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

create_database(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# by default, look for primary key to specify a user upon login
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


