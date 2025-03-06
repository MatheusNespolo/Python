#Copa do Mundo (OBI 2010)

placar = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
         'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
         'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
         'P': 0}

jogos = [
    ['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'],
    ['B', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'D'],
    ['C', 'E'], ['D', 'E'], ['F', 'G'], ['F', 'H'],
    ['F', 'I'], ['F', 'J'], ['G', 'H'], ['G', 'I'],
    ['G', 'J'], ['H', 'I'], ['H', 'J'], ['I', 'J'],
    ['P', 'K'], ['P', 'L'], ['P', 'M'], ['P', 'N'],
    ['K', 'L'], ['K', 'M'], ['K', 'N'], ['L', 'M'],
    ['L', 'N'], ['M', 'N']
]

resultadosM = []
resultadosN = []

for i in range(0, len(placar) - 1):
    m, n = map(int, input().split())
    resultadosM.append(m)
    resultadosN.append(n)

    time1 = jogos[i][0]
    time2 = jogos[i][1]

    if resultadosM[i] > resultadosN[i]:
        placar[time1] += 3  # Time 1 vence
    elif resultadosM[i] < resultadosN[i]:
        placar[time2] += 3  # Time 2 vence

campeao = max(placar, key=placar.get)
print(campeao)
