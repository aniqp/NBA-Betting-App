import requests
import pandas as pd

# playerdashboardbyyearoveryearcombined --> https://www.nba.com/stats/ click on player --> Network
player_id = '1628415'

player_url = 'https://stats.nba.com/stats/playerdashboardbyyearoveryearcombined?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=' + player_id + '&PlusMinus=N&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&VsConference=&VsDivision='

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

response = requests.get(url = player_url, headers = headers).json()

ovr_base_info = response['resultSets'][0]['rowSet']
ovr_advanced_info = response['resultSets'][1]['rowSet'] 
ovr_misc_info = response['resultSets'][2]['rowSet']
ovr_scoring_info = response['resultSets'][3]['rowSet']
ovr_usage_info = response['resultSets'][4]['rowSet']  

by_base_info = response['resultSets'][5]['rowSet']  
by_advanced_info = response['resultSets'][6]['rowSet']  
by_misc_info = response['resultSets'][7]['rowSet']  
by_scoring_info = response['resultSets'][8]['rowSet']  
by_usage_info = response['resultSets'][9]['rowSet']  

columns_list = [
    'GROUP_SET',
    'GROUP_VALUE',
    'TEAM_ID',
    'TEAM_ABBREVIATION',
    'MAX_GAME_DATE',
    'GP',
    'W',
    'L',
    'W_PCT',
    'MIN',
    'FGM',
    'FGA',
    'FG_PCT',
    'FG3M',
    'FG3A',
    'FG3_PCT',
    'FTM',
    'FTA',
    'FT_PCT',
    'OREB',
    'DREB',
    'REB',
    'AST',
    'TOV',
    'STL',
    'BLK',
    'BLKA',
    'PF',
    'PFD',
    'PTS',
    'PLUS_MINUS',
    'NBA_FANTASY_PTS',
    'DD2',
    'TD3',
    'WNBA_FANTASY_PTS',
    'GP_RANK',
    'W_RANK',
    'L_RANK',
    'W_PCT_RANK',
    'MIN_RANK',
    'FGM_RANK',
    'FGA_RANK',
    'FG_PCT_RANK',
    'FG3M_RANK',
    'FG3A_RANK',
    'FG3_PCT_RANK',
    'FTM_RANK',
    'FTA_RANK',
    'FT_PCT_RANK',
    'OREB_RANK',
    'DREB_RANK',
    'REB_RANK',
    'AST_RANK',
    'TOV_RANK',
    'STL_RANK',
    'BLK_RANK',
    'BLKA_RANK',
    'PF_RANK',
    'PFD_RANK',
    'PTS_RANK',
    'PLUS_MINUS_RANK',
    'NBA_FANTASY_PTS_RANK',
    'DD2_RANK',
    'TD3_RANK',
    'WNBA_FANTASY_PTS_RANK',
]

nba_df = pd.DataFrame(ovr_base_info, columns = columns_list)

print(nba_df)