class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)
    
    def has_player(self, name):
        player_exists = False
        for player in self.players:
            if player == name:
                player_exists = True
        return player_exists

    def play_game(self, has_team_won):
        if has_team_won == True:
            self.points += 3