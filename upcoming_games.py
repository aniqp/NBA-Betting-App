import requests
import pandas as pd

def upcoming_games():

    gameIDs = []

    game_id_url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

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

    response = requests.get(url = game_id_url, headers = headers).json()

    games = response['scoreboard']['games']

    print("Today's Games")
    count = 0
    for game in games:
        gameIDs.append(games[count]['gameId'])
        awayTeam = games[count]['awayTeam']['teamName']
        homeTeam = games[count]['homeTeam']['teamName']
        print(str('GameID: ' + gameIDs[count] + '  ' + awayTeam + ' @ ' + homeTeam))
        count += 1

upcoming_games()