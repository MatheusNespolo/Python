#Copa do Mundo (OBI 2010)

contador = 0
resultadosN = []
resultadosM = []
oitavas = []
quartas = []
semifinal = []

# Entrada
while True:
    N, M = map(int, input().split())
    resultadosN.append(N)
    resultadosM.append(M)
    contador += 1
    if contador == 15:
        break

# Processamento das oitavas
for i in range(1, 8):
    if resultadosN[1] > resultadosM[1] and 'A' not in oitavas:
        oitavas.append('A')
    elif resultadosN[1] < resultadosM[1] and 'B' not in oitavas:
        oitavas.append('B')
    if resultadosN[2] > resultadosM[2] and 'C' not in oitavas:
        oitavas.append('C')
    elif resultadosN[2] < resultadosM[2] and 'D' not in oitavas:
        oitavas.append('D')
    if resultadosN[3] > resultadosM[3] and 'E' not in oitavas:
        oitavas.append('E')
    elif resultadosN[3] < resultadosM[3] and 'F' not in oitavas:
        oitavas.append('F')
    if resultadosN[4] > resultadosM[4] and 'G' not in oitavas:
        oitavas.append('G')
    elif resultadosN[4] < resultadosM[4] and 'H' not in oitavas:
        oitavas.append('H')
    if resultadosN[5] > resultadosM[5] and 'I' not in oitavas:
        oitavas.append('I')
    elif resultadosN[5] < resultadosM[5] and 'J' not in oitavas:
        oitavas.append('J')
    if resultadosN[6] > resultadosM[6] and 'K' not in oitavas:
        oitavas.append('K')
    elif resultadosN[6] < resultadosM[6] and 'L' not in oitavas:
        oitavas.append('L')      
    if resultadosN[7] > resultadosM[7] and 'M' not in oitavas:
        oitavas.append('M')
    elif resultadosN[7] < resultadosM[7] and 'N' not in oitavas:
        oitavas.append('N')
    if resultadosN[8] > resultadosM[8] and 'O' not in oitavas:
        oitavas.append('O')
    elif resultadosN[8] < resultadosM[8] and 'P' not in oitavas:
        oitavas.append('P')

# Processamento das quartas
for j in range(9, 12):
    if resultadosN[9] > resultadosM[9] and oitavas[0] == 'A' and 'A' not in quartas:
        quartas.append('A')
    elif resultadosN[9] > resultadosM[9] and oitavas[0] == 'B' and 'B' not in quartas:
        quartas.append('B')
    elif resultadosN[9] < resultadosM[9] and oitavas[1] == 'C' and 'C' not in quartas:
        quartas.append('C')
    elif resultadosN[9] < resultadosM[9] and oitavas[1] == 'D' and 'D' not in quartas:
        quartas.append('D')
    if resultadosN[10] > resultadosM[10] and oitavas[2] == 'E' and 'E' not in quartas:
        quartas.append('E')
    elif resultadosN[10] > resultadosM[10] and oitavas[2] == 'F':
        quartas.append('F')
    elif resultadosN[10] < resultadosM[10] and oitavas[3] == 'G' and 'G' not in quartas:
        quartas.append('G')
    elif resultadosN[10] < resultadosM[10] and oitavas[3] == 'H' and 'H' not in quartas:
        quartas.append('H')
    if resultadosN[11] > resultadosM[11] and oitavas[4] == 'I' and 'I' not in quartas:
        quartas.append('I')
    elif resultadosN[11] > resultadosM[11] and oitavas[4] == 'J' and 'J' not in quartas:
        quartas.append('J')
    elif resultadosN[11] < resultadosM[11] and oitavas[5] == 'K' and 'K' not in quartas:
        quartas.append('K')

print(quartas)
