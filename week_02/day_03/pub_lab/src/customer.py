class Customer:
    
    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet

    def remove_from_customer_wallet(self, amount):
        self.wallet -= amount