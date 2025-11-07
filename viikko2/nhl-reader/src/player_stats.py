
class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        players_by_nationality = [player for player in players if player.nationality == nationality]
        players_by_nationality.sort(key=lambda p: p.points, reverse=True)
        return players_by_nationality

    def exusemua(self):
        print("plz")
