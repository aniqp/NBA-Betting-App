from app import app
from app.functions.get_top_five_users import get_top_five_users
from . import db
from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Bet
from werkzeug.security import generate_password_hash, check_password_hash
import json
from sqlalchemy.exc import IntegrityError
from app.functions.todays_games import *
from app.functions.get_team_credentials import *
from app.functions.get_best_player import *
from app.functions.determine_bet_outcome import *
from app.functions.string_to_boolean_converter import *
from app.functions.get_game_status import *
from app.functions.update_user_swishcoins import *

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
        home_pts_bet_value = request.form.get('slider1')
        away_pts_user_bet = request.form.get('bet2')
        away_pts_bet_value = request.form.get('slider2')

        home_rebounds_user_bet = request.form.get('bet3')
        home_rebounds_bet_value = request.form.get('slider3')
        away_rebounds_user_bet = request.form.get('bet4')
        away_rebounds_bet_value = request.form.get('slider4')

        home_assists_user_bet = request.form.get('bet5')
        home_assists_bet_value = request.form.get('slider5')
        away_assists_user_bet = request.form.get('bet6')
        away_assists_bet_value = request.form.get('slider6')

        bet_list = [
        {home_pts: home_pts_user_bet, 'bet_amount': home_pts_bet_value},
        {away_pts: away_pts_user_bet, 'bet_amount': away_pts_bet_value},
        {home_rebounds: home_rebounds_user_bet, 'bet_amount': home_rebounds_bet_value},
        {away_rebounds: away_rebounds_user_bet, 'bet_amount': away_rebounds_bet_value},
        {home_assists: home_assists_user_bet, 'bet_amount': home_assists_bet_value},
        {away_assists: away_assists_user_bet, 'bet_amount': away_assists_bet_value}
        ]
        bet_sum = []
        for bet in bet_list:
            if bet.get(list(bet.keys())[0]) is not None:
                db.session.add(Bet(
                game_id = game_id,
                team = list(bet.keys())[0].team,
                player_name = list(bet.keys())[0].name,
                statistic = list(bet.keys())[0].statistic,
                over_statistic = convert_string_to_boolean((bet.get(list(bet.keys())[0]))),
                wagered_amount = bet.get(list(bet.keys())[1]),
                num_stats = list(bet.keys())[0].num_stats,
                user_id = current_user.id
                ))
                bet_sum.append(int(bet.get(list(bet.keys())[1])))
                db.create_all
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()

        # bet_sum = user_bet_sum(home_pts_bet_value, away_pts_bet_value, home_rebounds_bet_value, away_rebounds_bet_value, home_assists_bet_value, away_assists_bet_value)
        user = current_user
        user.swishcoins = user.swishcoins - int(sum(bet_sum))
        db.session.commit()

        flash('Bet(s) made!', category = 'success')
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
    # outcome = "hi"
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
                'game_id': bet.game_id,
                'stats_actual': bet.stats_actual
            }

            bet.game_status = get_game_status(bet.game_id)
            db.session.commit()

            outcome = determine_bet_outcome(data_dictionary)
            if bet.game_status == 2:
                bet.stats_actual = int(outcome['num_stats'])
                db.session.commit()
                if outcome['bet_outcome'] == True and bet.over_statistic == True:
                    bet.w_or_l = outcome['bet_outcome']
                    try:
                        db.session.commit()
                    except IntegrityError:
                        db.session.rollback()
                elif outcome['bet_outcome'] == False and bet.over_statistic == False:
                    bet.w_or_l = outcome['bet_outcome']
                    try:
                        db.session.commit()
                    except IntegrityError:
                        db.session.rollback()                
            elif bet.game_status == 3:
                bet.w_or_l = outcome['bet_outcome']
                bet.stats_actual = int(outcome['num_stats'])
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
    if bet.claimed == False:                
        current_user.swishcoins = update_user_swishcoins(current_user.swishcoins, bet.wagered_amount, bet.w_or_l)
        bet.claimed = True
        db.session.commit()
    return render_template("user_bets.html", user = current_user)


@app.route('/leaderboard')
def leaderboard():
    users = User.query.all()
    sorted_users = get_top_five_users(users)
    return render_template("leaderboard.html", user = current_user, users = users)