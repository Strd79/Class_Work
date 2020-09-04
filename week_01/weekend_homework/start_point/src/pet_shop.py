# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    name = shop_name["name"]
    return name

def get_total_cash(cash):
    total_cash = cash["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash(val_1, num_1):
    val_1["admin"]["total_cash"] += num_1

