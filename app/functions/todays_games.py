import requests
import pandas as pd

def todays_games():

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

    # game_ids = {
    #     '00222345': {
    #         'home_team': 1610612755,
    #         'away_team': 1610612741
    #     },
    #     '003242342': {
    #         'home_team': 1610612748,
    #         'away_team': 1610612758
    #     },
    #     '001231231': {
    #         'home_team': 1610612738,
    #         'away_team': 1610612761
    #     }
    # }

    game_ids = {}

    count = 0
    for game in games:
        away_team_id = games[count]['awayTeam']['teamId']
        home_team_id = games[count]['homeTeam']['teamId']
        game_ids.update( { games[count]['gameId']: {'home_team': home_team_id, 'away_team': away_team_id }} )
        count += 1 
        
    return(game_ids)

def teams_from_game_id(game_id):
    today_games = todays_games()
    for k, v in today_games.items():
        if k == game_id:
            return v

