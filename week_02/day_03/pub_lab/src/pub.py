class Pub:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = []

    def increase_till_amount(self, amount):
        self.till += amount

    def add_drink(self, pub, drink):
        self.drinks.append(drink)
        