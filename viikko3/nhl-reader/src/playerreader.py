import requests
from player import Player


class PlayerReader:

    def __init__(self, url):
        self.url = url
        self.players = []

    def get_players(self):

        response = requests.get(self.url).json()


        for player_dict in response:
            if player_dict['nationality'] == "FIN":
                player = Player(
                    player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists']
                )

                self.players.append(player)
        return self.players
        
  
