# from package import db object
from enum import unique
from sqlalchemy import UniqueConstraint
from . import db
from flask_login import UserMixin
# func gets current date and time and will store that as the default date/time
from sqlalchemy.sql import func

class Bet(db.Model):
    __table_args__ = (
        db.UniqueConstraint('game_id', 'team', 'player_name', 'statistic', 'num_stats', 'user_id'),
    )
    id = db.Column(db.Integer, primary_key = True)
    game_id = db.Column(db.String(50))
    team = db.Column(db.String(100))
    player_name = db.Column(db.String(500))
    statistic = db.Column(db.String(100))
    over_statistic = db.Column(db.Boolean, default = False, nullable = False)
    num_stats = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    w_or_l = db.Column(db.Boolean, default = None, nullable = True)
    game_status = db.Column(db.Integer, nullable = True)
    stats_actual = db.Column(db.Integer, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    

# when you want to make a new database model (store a different type of object), have it inherit from db.model
# usermixin just for user model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    # no user can have the same email as another user
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    # Can access all of user's bets with this field
    bets = db.relationship('Bet')