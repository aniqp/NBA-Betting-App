import requests
import pandas as pd
import numpy as np


gameId = '0022101215'

box_score_url = 'https://cdn.nba.com/static/json/liveData/boxscore/boxscore_' + gameId + '.json' #0022101190 = gameId

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

response = requests.get(url = box_score_url, headers = headers).json()

homeTeam = response['game']['homeTeam']
awayTeam = response['game']['awayTeam']

def get_box_score(team):
    count = 0
    players = team['players']
    array = []
    large_array = []

    for player in players:
        statistics = []
        statistics.append(players[count]['nameI'])
        array = players[count]['statistics']
        for key, value in array.items():
            statistics.append(value)
        large_array.append(statistics)
        count += 1 

    columns_list = [
        'NAME',
        'AST',
        'BLK',
        'BLKA',
        'FGA',
        'FGM',
        'FG%',
        'FD',
        'OF',
        'PF',
        'TF',
        'FTA',
        'FTM',
        'FT%',
        '-',
        'mins',
        'minsCalc',
        '+',
        '+/-',
        'PTS',
        'FBP',
        'PIP',
        'SCP',
        'DR',
        'OR',
        'TR',
        'STL',
        'FG3A',
        'FG3M',
        'FG3%',
        'TOV',
        'FG2A',
        'FG2M',
        'FG2%',
    ]

    nba_df = pd.DataFrame(large_array, columns = columns_list)

    nba_df_imp = nba_df[
    [   "NAME",
        "PTS",
        "AST",
        "TR",
        "BLK",
        "STL",
        "FG%",
        "FG3%",
        "TOV"
        ]
    ]

    print(nba_df_imp)

    #nba_df.to_csv('box_score.csv', index = False)

get_box_score(homeTeam)
print()
get_box_score(awayTeam)
