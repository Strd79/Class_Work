class GearBox:

    def __init__(self, type, number_of_gears):
        self.type = type
        self.number_of_gears = number_of_gears
        self.current_gear = "N"

    def change_gear(self, gear):
        self.current_gear = gear