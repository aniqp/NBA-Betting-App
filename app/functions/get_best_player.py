from venv import create
import requests
import pandas as pd

from app.functions.todays_games import todays_games

def sort_by_stat(df, stat):
    return df.sort_values(by=[stat], ascending = False)

# get best player from a certain team
def get_best_player(team_id, stat):

    # stats.nba.com -> players -> traditional stats
    player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='

    headers  = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }


    response = requests.get(url = player_info_url, headers = headers).json()

    player_info = response['resultSets'][0]['rowSet']

    columns_list = response['resultSets'][0]['headers']

    nba_df = pd.DataFrame(player_info, columns = columns_list)
    nba_df = nba_df.rename(columns = {
        'PLAYER_NAME' : 'NAME',
        'TEAM_ABBREVIATION' : 'TEAM',
        'FG_PCT' : 'FG%',
        'FG3_PCT' : 'FG3%',
        'FT_PCT' : 'FT%',
        'PLUS_MINUS' : '+/-'
        })

    nba_df = nba_df[nba_df['TEAM_ID'] == team_id]
    # sort by stat passed by user
    nba_df = sort_by_stat(nba_df, stat)
    nba_df_imp = nba_df[[
        'NAME',
        'PTS',
        'AST',
        'REB',
        'STL',
        'BLK',
        'TOV',
        'PF'
    ]]

    row1 = nba_df_imp.iloc[0] # getting highest stat player


    player_name = {     # saving to dictionary
        'player': row1['NAME'],
        'points': row1['PTS'],
        'assists': row1['AST'],
        'rebounds': row1['REB'],
        'steals': row1['STL'],
        'blocks': row1['BLK'],
        'turnovers': row1['TOV'],
        'fouls': row1['PF']
    }

    return player_name

    # nba_df_imp.to_csv('traditional_stats.csv', index = False)

today_games = todays_games()
class BetCardPoints:
    def __init__(self, name, points):
        # get best player from whichever team the user picks
        self.name = name
        self.statistic = 'PTS'
        self.num_stats = points

class BetCardAssists:
    def __init__(self, name, assists):
        # get best player from whichever team the user picks
        self.name = name
        self.statistic = 'AST'
        self.num_stats = assists


class BetCardRebounds:
    def __init__(self, name, rebounds):
        # get best player from whichever team the user picks
        self.name = name
        self.statistic = 'REB'
        self.num_stats = rebounds


def create_points_card_away(game_id):
    obj = BetCardPoints(
        get_best_player(today_games[game_id]['away_team'], 'PTS')['player'],
        get_best_player(today_games[game_id]['away_team'], 'PTS')['points']
    )
    return obj

def create_points_card_home(game_id):
    obj = BetCardPoints(
        get_best_player(today_games[game_id]['home_team'], 'PTS')['player'],
        get_best_player(today_games[game_id]['home_team'], 'PTS')['points']
    )
    return obj

def create_rebounds_card_away(game_id):
    obj = BetCardRebounds(
        get_best_player(today_games[game_id]['away_team'], 'REB')['player'],
        get_best_player(today_games[game_id]['away_team'], 'REB')['rebounds']
    )
    return obj

def create_rebounds_card_home(game_id):
    obj = BetCardRebounds(
        get_best_player(today_games[game_id]['home_team'], 'REB')['player'],
        get_best_player(today_games[game_id]['home_team'], 'REB')['rebounds']
    )
    return obj

def create_assists_card_away(game_id):
    obj = BetCardAssists(
        get_best_player(today_games[game_id]['away_team'], 'AST')['player'],
        get_best_player(today_games[game_id]['away_team'], 'AST')['assists']
    )
    return obj

def create_assists_card_home(game_id):
    obj = BetCardAssists(
        get_best_player(today_games[game_id]['home_team'], 'AST')['player'],
        get_best_player(today_games[game_id]['home_team'], 'AST')['assists']
    )
    return obj

class BetCardSteals:
    def __init__(self, name, steals):
        # get best player from whichever team the user picks
        self.name = name
        self.steals = steals



class BetCardBlocks:
    def __init__(self, name, blocks):
        # get best player from whichever team the user picks
        self.name = name
        self.blocks = blocks


class BetCardTurnovers:
    def __init__(self, name, turnovers):
        # get best player from whichever team the user picks
        self.name = name
        self.turnovers = turnovers


class BetCardWinner:
    def __init__(self, home_team_win):
        self.home_team_win = home_team_win