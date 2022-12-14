from statistics_1 import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All, Not

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
        )   

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
