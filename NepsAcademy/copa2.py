#Copa do Mundo (OBI 2010)


teams = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
         'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
         'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0}

games = [
    ['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'],
    ['B', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'D'],
    ['C', 'E'], ['D', 'E'], ['F', 'G'], ['F', 'H'],
    ['F', 'I'], ['F', 'J'], ['G', 'H']
]

# Entrada

for i in range(15):
    m, n = map(int, input().split())
    team1 = games[i][0]
    team2 = games[i][1]

    if m > n:
        teams[team1] += 3  # Time 1 vence
    elif m < n:
        teams[team2] += 3  # Time 2 vence
    else:
        teams[team1] += 1  # Draw
        teams[team2] += 1  # Draw

champion = max(teams, key=teams.get)
print(champion)
