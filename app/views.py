from asyncio.windows_events import NULL
from tracemalloc import Statistic
from app import app
from . import db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Bet
from werkzeug.security import generate_password_hash, check_password_hash
from app.functions.todays_games import *
from app.functions.get_team_credentials import *
from app.functions.get_best_player import *
from app.functions.string_to_boolean_converter import *

@app.route("/")
@login_required
def index():
    game = todays_games()
    games = {}
    for key, value in game.items():
        games.update({ key : {
            'away_team': get_team_name(value['away_team']),
            'home_team': get_team_name(value['home_team'])
        } })

    return render_template("index.html", games = games, user = current_user)


@app.route("/games/<string:game_id>/", methods = ['GET', 'POST'])
def games(game_id):
    teams = teams_from_game_id(game_id)
    home_team = get_team_name(teams['home_team'])
    away_team = get_team_name(teams['away_team'])

    away_pts = create_points_card_away(game_id)
    home_pts = create_points_card_home(game_id)

    away_rebounds = create_rebounds_card_away(game_id)
    home_rebounds = create_rebounds_card_home(game_id)

    away_assists = create_assists_card_away(game_id)
    home_assists = create_assists_card_home(game_id)

    if request.method == 'POST':

        home_pts_user_bet = request.form.get('bet1')
        away_pts_user_bet = request.form.get('bet2')

        home_rebounds_user_bet = request.form.get('bet3')
        away_rebounds_user_bet = request.form.get('bet4')

        home_assists_user_bet = request.form.get('bet5')
        away_assists_user_bet = request.form.get('bet6')

        bet_list = [
         {home_pts: home_pts_user_bet},
         {away_pts: away_pts_user_bet},
         {home_rebounds: home_rebounds_user_bet},
         {away_rebounds: away_rebounds_user_bet},
         {home_assists: home_assists_user_bet},
         {away_assists: away_assists_user_bet}
        ]
  
        # count = 0
        # for bet in bet_list:
        #     if bet.get(list(bet.keys())[count]) is not None:
        #         print(type(convert_string_to_boolean(bet.get(list(bet.keys())[count]))))
        # count +=1

        for bet in bet_list:
            if bet.get(list(bet.keys())[0]) is not None:
                db.session.add(Bet(
                game_id = game_id,
                player_name = list(bet.keys())[0].name,
                statistic = list(bet.keys())[0].statistic,
                over_statistic = convert_string_to_boolean((bet.get(list(bet.keys())[0]))),
                num_stats = list(bet.keys())[0].num_stats,
                user_id = current_user.id
                ))
                db.create_all
                db.session.commit()
        flash('Bet(s) made!', category = 'success')

    return render_template(
        "game.html",
        away_pts = away_pts, 
        home_pts = home_pts, 
        away_rebounds = away_rebounds, 
        home_rebounds = home_rebounds, 
        away_assists = away_assists, 
        home_assists = home_assists,
        home_team = home_team,
        away_team = away_team,
        user = current_user
    )

@app.route("/my-bets")
def my_bets():
    return render_template("user_bets.html", user = current_user)

@app.route("/sign-up", methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category = 'error')
        elif len(email) < 4:
            flash('Email length must be greater than 3 characters.', category = 'error')
        elif len(first_name) < 2:
            flash('First name length must be greater than 1 character.', category = 'error')
        elif len(last_name) < 2:
            flash('Last name length must be greater than 1 character.', category = 'error')           
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:
            new_user = User(email=email, first_name= first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = True)
            flash('Account created!', category='success')
            return redirect(url_for('index'))

    return render_template("sign_up.html", user=current_user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # first returns the first result
        user = User.query.filter_by(email=email).first()
        # if a user is found, check if password they typed in exists in the database
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'success')
                # remembers that user is logged in until they clear their cache
                login_user(user, remember = True)
                return redirect(url_for('index'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')
        
    return render_template("login.html", user = current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# for col in Bet.__table__.columns:
#     print(col)