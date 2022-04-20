import requests
import pandas as pd
import numpy as np

def determine_bet_outcome(data_dictionary):
    game_id = data_dictionary.get('game_id')
    box_score_url = 'https://cdn.nba.com/static/json/liveData/boxscore/boxscore_' + game_id + '.json' #0022101190 = gameId
    
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

    # homeTeam = response['game']['homeTeam']
    # awayTeam = response['game']['awayTeam']

    count = 0
    team = response['game'][data_dictionary.get('team')]
    players = team['players']
    array = []
    large_array = []

    for player in players:
        statistics = []
        statistics.append(players[count]['name'])
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
        'REB',
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
        "REB"
        ]
    ]

    player_df = nba_df_imp[nba_df_imp['NAME'] == data_dictionary.get('name')]
    
    stat_to_compare = player_df[data_dictionary.get('statistic')].values[0]
    
    
    compare_boxscore_to_avg = (stat_to_compare > round(data_dictionary.get('num_stats')))

    game_status = response['game']['gameStatusText']

    outcome_stat_dict = {}
    if compare_boxscore_to_avg == False:
        if game_status == 'Final':
            outcome_stat_dict.update({
                'bet_outcome': compare_boxscore_to_avg == data_dictionary.get('over_statistic'),
                'num_stats': stat_to_compare
            })
            return outcome_stat_dict
        else:
            return "The game isn't over yet, " + data_dictionary['name'] + " has " + stat_to_compare + " " + data_dictionary['statistic']
    else:
        outcome_stat_dict.update({
            'bet_outcome': compare_boxscore_to_avg == data_dictionary.get('over_statistic'),
            'num_stats': stat_to_compare
        })
        return outcome_stat_dict
        
    # return compare_bet_to_boxscore == data_dictionary.get('over_statistic')

data_dict = {
    'game_id':"0042100152",
    'team': 'homeTeam',
    'name': 'Ja Morant',
    'statistic': 'PTS',
    'num_stats': 21,
    'over_statistic': True
}

print(determine_bet_outcome(data_dict))



