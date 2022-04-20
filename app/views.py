from app import app
from . import db
from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Bet
from werkzeug.security import generate_password_hash, check_password_hash
import json
from app.functions.todays_games import *
from app.functions.get_team_credentials import *
from app.functions.get_best_player import *
from app.functions.determine_bet_outcome import *
from app.functions.string_to_boolean_converter import *

@app.route("/")
@login_required
def index():
    game = todays_games()
    games = {}
    for key, value in game.items():
        games.update({ key : {
            'away_team': {
                'name': get_team_name(value['away_team']),
                'colour': get_team_colour(value['away_team'])
            },
            'home_team': {
                'name': get_team_name(value['home_team']),
                'colour': get_team_colour(value['home_team'])
            }
        }})

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
                team = list(bet.keys())[0].team,
                player_name = list(bet.keys())[0].name,
                statistic = list(bet.keys())[0].statistic,
                over_statistic = convert_string_to_boolean((bet.get(list(bet.keys())[0]))),
                num_stats = list(bet.keys())[0].num_stats,
                user_id = current_user.id
                ))
                db.create_all
                db.session.commit()
        
        # flash('Bet(s) made!', category = 'success')
        return redirect('/')


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

@app.route('/delete-bet', methods = ['POST'])
def delete_bet():
    bet = json.loads(request.data)
    betID = bet['betID']
    bet = Bet.query.get(betID)
    if bet:
        if bet.user_id == current_user.id:
            db.session.delete(bet)
            db.session.commit()
    
    return jsonify({})

@app.route('/check-bet-status', methods = ['POST'])
def check_bet_status():
    bet = json.loads(request.data)
    betID = bet['betID']
    bet = Bet.query.get(betID)
    if bet:
        if bet.user_id == current_user.id:
            data_dictionary = {
                'name': bet.player_name,
                'team': bet.team,
                'statistic': bet.statistic,
                'num_stats': bet.num_stats,
                'over_statistic': bet.over_statistic,
                'game_id': bet.game_id
            }
        
        bet.w_or_l = determine_bet_outcome(data_dictionary)
        db.session.commit()

    return bet.w_or_l
    
