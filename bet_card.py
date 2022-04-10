from get_best_player import *
from todays_games import todays_games

class BetCardPoints:
    def __init__(self, name, points):
        # get best player from whichever team the user picks
        self.name = name
        self.points = points

today_games = todays_games()

aniqpremji = BetCardPoints(
    get_best_player(today_games['0022101214']['away_team'])['player'], 
    get_best_player(today_games['0022101214']['away_team'])['points']
)

print("Will " + str(aniqpremji.name) + " score more or less than " + str(round(aniqpremji.points)) + " points?")

ethanluk = BetCardPoints(
    get_best_player(today_games['0022101214']['home_team'])['player'],
    get_best_player(today_games['0022101214']['home_team'])['points']
)

print("Will " + str(ethanluk.name) + " score more or less than " + str(round(ethanluk.points)) + " points?")

