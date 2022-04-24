def get_top_five_users(user_list):
    sorted_list = []
    for i in range(len(user_list)):
        temp_user_amount = {user_list[i]: user_list[i].swishcoins}
        for j in range (len(user_list)):
            if user_list[j].swishcoins >= temp_user_amount.get(list(temp_user_amount.keys())[0]):
                if user_list[j] not in sorted_list:
                    temp_user_amount = {user_list[j]: user_list[j].swishcoins}
                    print(user_list[j])
        sorted_list.append(list(temp_user_amount.keys())[0])
        # user_list.remove(list(temp_user_amount.keys())[0])

    print(sorted_list)