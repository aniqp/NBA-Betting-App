import requests
from get_team_credentials import *

def get_winner(game_id):

    game_url = 'https://cdn.nba.com/static/json/liveData/boxscore/boxscore_' + game_id + '.json' 

    headers  = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'S~ec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = requests.get(url = game_url, headers = headers).json()

    home_score = response['game']['homeTeam']['score']
    away_score = response['game']['awayTeam']['score']

    if home_score > away_score:
        print(response['game']['homeTeam']['teamId'], 'won' )
    else:
       print(response['game']['awayTeam']['teamId'], 'won' )

get_winner('0022101213')