#Copa do Mundo (OBI 2010)

contador = 0
resultadosN = []
resultadosM = []
oitavas = []

# Entrada
while True:
    N, M = map(int, input().split())
    resultadosN.append(N)
    resultadosM.append(M)
    contador += 1
    if contador == 15:
        break

for i in range(15):
    if resultadosN[1] > resultadosM[1]:
        oitavas.append('A')
    else:
        oitavas.append('B')
    resultadosN.pop(0)
    resultadosM.pop(0)
    if resultadosN[2] > resultadosM[2]:
        oitavas.append('C')
    else:
        oitavas.append('D')
    resultadosN.pop(0)    