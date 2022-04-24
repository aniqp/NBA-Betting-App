def get_top_five_users(user_list):
    sorted_list = sorted(user_list, key=lambda x: x.swishcoins, reverse=True)
    if len(user_list) < 5:
        return sorted_list[:len(user_list)]
    else:
        return sorted_list[:5]