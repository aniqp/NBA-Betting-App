from get_best_player import *
from todays_games import todays_games

class BetCardPoints:
    def __init__(self, name, points):
        # get best player from whichever team the user picks
        self.name = name
        self.points = points

today_games = todays_games()

aniqpremji = BetCardPoints(
    get_best_player(today_games['0022101218']['away_team'], 'PTS')['player'], 
    get_best_player(today_games['0022101218']['away_team'], 'PTS')['points']
)

# print("Will " + str(aniqpremji.name) + " score more or less than " + str(round(aniqpremji.points)) + " points?")

ethanluk = BetCardPoints(
    get_best_player(today_games['0022101218']['home_team'], 'PTS')['player'],
    get_best_player(today_games['0022101218']['home_team'], 'PTS')['points']
)

# print("Will " + str(ethanluk.name) + " score more or less than " + str(round(ethanluk.points)) + " points?")

class BetCardAssists:
    def __init__(self, name, assists):
        # get best player from whichever team the user picks
        self.name = name
        self.assists = assists

ethan = BetCardAssists(
    get_best_player(today_games['0022101218']['away_team'], 'AST')['player'],
    get_best_player(today_games['0022101218']['away_team'], 'AST')['assists']
)


class BetCardRebounds:
    def __init__(self, name, rebounds):
        # get best player from whichever team the user picks
        self.name = name
        self.rebounds = rebounds

ethan = BetCardRebounds(
    get_best_player(today_games['0022101218']['home_team'], 'REB')['player'],
    get_best_player(today_games['0022101218']['home_team'], 'REB')['rebounds']
)

# print("Will " + str(ethan.name) + " get more or less than " + str(round(ethan.rebounds)) + " rebounds?")


class BetCardSteals:
    def __init__(self, name, steals):
        # get best player from whichever team the user picks
        self.name = name
        self.steals = steals

ethan = BetCardSteals(
    get_best_player(today_games['0022101218']['home_team'], 'STL')['player'],
    get_best_player(today_games['0022101218']['home_team'], 'STL')['steals']
)

# print("Will " + str(ethan.name) + " get more or less than " + str(round(ethan.steals)) + " steal(s)?")


class BetCardBlocks:
    def __init__(self, name, blocks):
        # get best player from whichever team the user picks
        self.name = name
        self.blocks = blocks

ethan = BetCardBlocks(
    get_best_player(today_games['0022101218']['away_team'], 'BLK')['player'],
    get_best_player(today_games['0022101218']['away_team'], 'BLK')['blocks']
)

# print("Will " + str(ethan.name) + " get more or less than " + str(round(ethan.blocks)) + " block(s)?")

class BetCardTurnovers:
    def __init__(self, name, turnovers):
        # get best player from whichever team the user picks
        self.name = name
        self.turnovers = turnovers

ethan = BetCardTurnovers(
    get_best_player(today_games['0022101218']['away_team'], 'TOV')['player'],
    get_best_player(today_games['0022101218']['away_team'], 'TOV')['turnovers']
)

print("Will " + str(ethan.name) + " get more or less than " + str(round(ethan.turnovers)) + " turnovers?")

class BetCardWinner:
    def __init__(self, home_team_win):
        self.home_team_win = home_team_win

ethan = BetCardWinner(False)

