from app import app
from flask import render_template, request
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