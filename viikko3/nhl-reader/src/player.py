class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.total = self.goals + self.assists
    
    def __str__(self):
        return f'{self.name:20} {self.team:5} {self.goals} + {self.assists} = {self.goals + self.assists}'