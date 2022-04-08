import requests
import pandas as pd

gameId = '0022101195'

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

players = []
count = 0
for player in awayTeam:
    players.append(awayTeam['players'][count]['nameI'])
    count += 1

print(players)

statistics = awayTeam['players'][0]['statistics']
print(statistics)

# columns_list = [
#     'teamId'
#     'teamName',
#     'teamCity',
#     'teamTricode',
#     'score',
#     'inBonus',
#     'timeoutsRemaining',
#     'players["name"]'
# ]

# nba_df = pd.DataFrame(awayTeam, columns = columns_list, index = [0])


# print(nba_df)