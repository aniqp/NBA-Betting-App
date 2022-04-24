def update_user_swishcoins(current_amount, wagered_amount, result):
    if result == True:
        current_amount = current_amount + 2 * wagered_amount
    return current_amount