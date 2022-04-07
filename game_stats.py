import requests
import pandas as pd

# Network -> boxscore_{ gameId }.json

gameId = '0022101193'

game_stats_url = 'https://cdn.nba.com/static/json/liveData/boxscore/boxscore_' + gameId + '.json' #0022101190 = gameId

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

response = requests.get(url = game_stats_url, headers = headers).json()

home_players = response['game']['homeTeam']['players']
away_players = response['game']['awayTeam']['players']

print()
print('Home Team')
print()
count = 0
for player in home_players:
    print(str(home_players[count]['firstName']) + " " + str(home_players[count]['familyName']) + " Points: " + str(home_players[count]['statistics']['points']))
    count += 1

print()
print('Away Team')
print()

count = 0
for player in away_players:
    print(str(away_players[count]['firstName']) + " " + str(away_players[count]['familyName']) + " Points: " + str(away_players[count]['statistics']['points']))
    count += 1

