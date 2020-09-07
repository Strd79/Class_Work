class Team:

# Attributes
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

# Methods
    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        for play in self.players:
            if play == player:
                return True
        return False

    def play_game(self, game_result):
        won = True
        lose = False
        if game_result == True:
            self.points += 3
