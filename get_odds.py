import requests
import pandas as pd
from get_team_credentials import *


def get_odds():

    odds_url = 'https://cdn.nba.com/static/json/liveData/odds/odds_todaysGames.json'
    
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

    response = requests.get(url = odds_url, headers = headers).json()

    awayTeamID = response['games'][0]['awayTeamId']
    awayTeamName = get_team_name(str(awayTeamID))

    homeTeamID = response['games'][0]['homeTeamId']
    homeTeamName = get_team_name(str(homeTeamID))


    homeOdds = response['games'][0]['markets'][0]['books'][1]['outcomes'][0]['odds']
    awayOdds = response['games'][0]['markets'][0]['books'][1]['outcomes'][1]['odds']
    
    print(homeTeamName, homeOdds)
    print(awayTeamName, awayOdds)

get_odds()