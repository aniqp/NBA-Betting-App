from app import app
from flask import render_template, request, flash
from app.functions.todays_games import *
from app.functions.get_team_credentials import *
from app.functions.get_best_player import *

@app.route("/")
def index():
    game = todays_games()
    games = {}
    for key, value in game.items():
        games.update({ key : {
            'away_team': get_team_name(value['away_team']),
            'home_team': get_team_name(value['home_team'])
        } })

    return render_template("index.html", games = games)


@app.route("/games/<string:game_id>/")
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


    return render_template(
        "game.html",
        away_pts = away_pts, 
        home_pts = home_pts, 
        away_rebounds = away_rebounds, 
        home_rebounds = home_rebounds, 
        away_assists = away_assists, 
        home_assists = home_assists,
        home_team = home_team,
        away_team = away_team
    )

@app.route("/sign-up", methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email length must be greater than 3 characters.', category = 'error')
        elif len(firstName) < 2:
            flash('First name length must be greater than 1 character.', category = 'error')
        elif len(lastName) < 2:
            flash('Last name length must be greater than 1 character.', category = 'error')           
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:
            flash('Account created!', category='success')


    return render_template("sign_up.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    return "<p>Logout</p>"