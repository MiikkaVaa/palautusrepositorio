import requests
from player import Player

class PlayerReader:
    def __init__(self,url: str):
        self._url = url

    def get_players(self):
        data = requests.get(self._url, timeout=10).json()
        return [Player(player_dict) for player_dict in data]

    def exusemua(self):
        print("plz")
