def get_top_five_users(user_list):
    sorted_list = sorted(user_list, key=lambda x: x.swishcoins, reverse=True)
    if len(user_list) < 5:
        return sorted_list[:len(user_list)]
    else:
        return sorted_list[:5]


def merge_sort_coins(arr):
    # print(arr[2].swishcoins)

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort_coins(left_arr)
        merge_sort_coins(right_arr)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):

            print(i)
            if left_arr[i].swishcoins < right_arr[j].swishcoins:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        