import random as rnd


def makeTwoTeams(players):
    n = len(players)
    if n % 2 == 1:
        return "Invalid"
    for i in range(n):
        pos1 = rnd.randint(0, n - 1)
        pos2 = rnd.randint(0, n - 1)
        players[pos1], players[pos2] = players[pos2], players[pos1]
    return [players[:n // 2], players[n // 2:]]


players = ["A", "B", "C", "D"]
teams = makeTwoTeams(players)
print(teams)
