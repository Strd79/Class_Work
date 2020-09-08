class Customer:

# Attributes   
    def __init__(self, input_name, input_cash):
        self.name = input_name
        self.cash = input_cash
        self.pets = []

# Methods
    def pet_count(self):
        return len(self.pets)

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_total_value_of_pets(self):
        total = 0
        for pet in self.pets:
            total += pet.price
        return total