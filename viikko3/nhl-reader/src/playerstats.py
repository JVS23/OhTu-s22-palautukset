from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, players):

        print("Players from FIN:")

        player_list = self.reader.get_players()
        
        player_list.sort(key=lambda x: x.total, reverse=True)
    
        return player_list