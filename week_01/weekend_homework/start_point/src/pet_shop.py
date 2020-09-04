# WRITE YOUR FUNCTIONS HERE

import pdb

def get_pet_shop_name(shop_name):
    name = shop_name["name"]
    return name

def get_total_cash(pet_shop):
    total_cash = pet_shop["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash(pet_shop, num_1):
    current_total = get_total_cash(pet_shop)
    new_total = current_total + num_1
    pet_shop["admin"]["total_cash"] = new_total

def get_pets_sold(pet_shop):
    pets_sold = pet_shop["admin"]["pets_sold"]
    return pets_sold

def increase_pets_sold(pet_shop, num_1):
    pet_shop["admin"]["pets_sold"] += num_1

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_name):
    list_of_pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            list_of_pets_by_breed.append(pet_shop["pets"])
    return list_of_pets_by_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


# def remove_pet_by_name(pet_shop, pet_name):
#     pet_to_remove = find_pet_by_name(pet_shop, pet_name)
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_to_remove["name"]:
#             pet_shop["pets"].remove(pet)

def remove_pet_by_name(pet_shop, pet_name):
    pet_to_remove = find_pet_by_name(pet_shop, pet_name)
    pet_shop["pets"].remove(pet_to_remove)

def add_pet_to_stock(pet_shop, new_pet_to_add):
    pet_shop["pets"].append(new_pet_to_add)

def get_customer_cash(customer):
    customer_cash = customer["cash"]
    return customer_cash

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
        return len(customer["pets"])

def add_pet_to_customer(customer, pet_to_add):
    customer["pets"].append(pet_to_add)

def customer_can_afford_pet(customer, pet):
    if get_customer_cash(customer) >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    pdb.set_trace()
    if find_pet_by_name(pet_shop, pet) == True:
        if customer_can_afford_pet(customer, pet) == True:
            remove_pet_by_name(pet_shop, pet)
            increase_pets_sold(pet_shop, get_customer_pet_count(customer))
            add_pet_to_customer(customer, pet)
            remove_customer_cash(customer, amount)
            add_or_remove_cash(pet_shop, num_1)