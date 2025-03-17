#Copa do Mundo (OBI 2010)

#Entrada
placar = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0}
resultadosN = []
resultadosM = []

for i in range(0, 15):
    N, M = map(int, input().split())
    resultadosN.append(N)
    resultadosM.append(M)

#Processamento
for i in range(0, 15):
    if resultadosN[i] > resultadosM[i]:
        