import requests
import pandas as pd


def get_best_player(team_id):

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

    nba_df = nba_df[nba_df['TEAM_ID'] == team_id].sort_values(by=['PTS'], ascending= False)[['NAME','PTS']]

    row1 = nba_df.iloc[0]


    player_name = {
        'player': row1['NAME'],
        'points': row1['PTS']
    }

    return player_name

    # nba_df_imp.to_csv('traditional_stats.csv', index = False)

get_best_player(1610612761)