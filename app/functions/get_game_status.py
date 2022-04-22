import requests
import pandas as pd

def get_game_status(game_id):

    game_url = 'https://cdn.nba.com/static/json/liveData/boxscore/boxscore_' + game_id + '.json'

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

    response = requests.get(url = game_url, headers = headers).json()

    game_status = response['game']['gameStatus']

    return game_status
