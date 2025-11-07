class Player:
    def __init__(self, data: dict):
        self.name = data['name']
        self.team = data['team']
        self.nationality = data['nationality']
        self.assists = int(data['assists'])
        self.goals = int(data['goals'])

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals:>2} + {self.assists:>2} = {self.points:>2}"
