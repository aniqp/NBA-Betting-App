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

colours_dict = {
    1610612755: [0, 107, 182], # 76ers
    1610612749: [0, 71, 27], # Bucks
    1610612741: [206, 17, 65], # Bulls
    1610612739: [134, 0, 56], # Cavaliers
    1610612738: [0, 122, 51], # Celtics
    1610612746: [200, 16, 46], # Clippers
    1610612763: [93, 118, 169], # Grizzlies
    1610612737: [225, 68, 52], # Hawks
    1610612748: [152, 0, 46], # Heat
    1610612766: [29, 17, 96], # Hornets
    1610612762: [0, 43, 92], # Jazz 
    1610612758: [91, 43, 130], # Kings
    1610612752: [0, 107, 182], # Knicks
    1610612747: [85, 37, 130], # Lakers
    1610612753: [0, 125, 197], # Magic
    1610612742: [0, 83, 188], # Mavericks
    1610612751: [0, 0, 0], # Nets
    1610612743: [13, 34, 64], # Nuggets
    1610612754: [0, 45, 98], # Pacers
    1610612740: [0, 22, 65], # Pelicans
    1610612765: [200, 16, 46], # Pistons
    1610612761: [206, 17, 65], # Raptors
    1610612745: [206, 17, 65], # Rockets
    1610612759: [196, 206, 211], # Spurs
    1610612756: [229, 95, 32], # Suns
    1610612760: [0, 125, 195], # Thunder
    1610612750: [12, 35, 64], # Timberwolves
    1610612757: [224, 58, 62], # Trail Blazers
    1610612744: [29, 66, 138], # Warriors
    1610612764: [0, 43, 92], # Wizards
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


def get_team_colour(team_id):
    try:
        colour = colours_dict[team_id]
        return colour
    except:
        return "id not found"
