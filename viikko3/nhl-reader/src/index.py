import requests
from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    print("ok")
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:

        if player_dict['nationality'] == "FIN":

            player = Player(
                player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists']
            )

            players.append(player)

    print("Oliot:")

    players.sort(key=lambda x: x.total, reverse=True)

    for player in players:
        print(player)

    

if __name__ == "__main__":
    print ("Start")
    main()