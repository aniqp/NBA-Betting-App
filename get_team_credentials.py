names_dict = {
    '76ers': 1610612755,
    'Bucks': 1610612749,
    'Bulls': 1610612741,
    'Cavaliers': 1610612739,
    'Celtics': 1610612738,
    'Clippers': 1610612746,
    'Grizzlies': 1610612763,
    'Hawks': 1610612737,
    'Heat': 1610612748,
    'Hornets': 1610612766,
    'Jazz': 1610612762,
    'Kings': 1610612758,
    'Knicks': 1610612752,
    'Lakers': 1610612747,
    'Magic': 1610612753, 
    'Mavericks': 1610612742,
    'Nets': 1610612751,
    'Nuggets': 1610612743,
    'Pacers': 1610612754,
    'Pelicans': 1610612740,
    'Pistons': 1610612765,
    'Raptors': 1610612761,
    'Rockets': 1610612745,
    'Spurs': 1610612759,
    'Suns': 1610612756,
    'Thunder': 1610612760,
    'Timberwolves': 1610612750,
    'Trail Blazers': 1610612757,
    'Warriors': 1610612744,  
    'Wizards': 1610612764,

}

def get_team_name(team_id):
    for key, value in names_dict.items():
        if team_id == value:
            return key
    
    return "key doesn't exist"

def get_id(team_name):
    try:
        id = names_dict[team_name]
        return id
    except:
        return "id not found"

print(get_id('Raptors'))
print(get_team_name(1610612755))