#Copa do Mundo (OBI 2010)

contador = 0
resultadosN = []
resultadosM = []
oitavas = []
quartas = []
semifinal = []
final = ''

# Entrada
while True:
    contador += 1
    N, M = map(int, input().split())
    resultadosN.append(N)
    resultadosM.append(M)
    if contador == 14:
        break

# Processamento das oitavas
for i in range(0, 7):
    if resultadosN[0] > resultadosM[0] and 'A' not in oitavas:
        oitavas.append('A')
    elif resultadosN[0] < resultadosM[0] and 'B' not in oitavas:
        oitavas.append('B')
    if resultadosN[1] > resultadosM[1] and 'C' not in oitavas:
        oitavas.append('C')
    elif resultadosN[1] < resultadosM[1] and 'D' not in oitavas:
        oitavas.append('D')
    if resultadosN[2] > resultadosM[2] and 'E' not in oitavas:
        oitavas.append('E')
    elif resultadosN[2] < resultadosM[2] and 'F' not in oitavas:
        oitavas.append('F')
    if resultadosN[3] > resultadosM[3] and 'G' not in oitavas:
        oitavas.append('G')
    elif resultadosN[3] < resultadosM[3] and 'H' not in oitavas:
        oitavas.append('H')
    if resultadosN[4] > resultadosM[4] and 'I' not in oitavas:
        oitavas.append('I')
    elif resultadosN[4] < resultadosM[4] and 'J' not in oitavas:
        oitavas.append('J')
    if resultadosN[5] > resultadosM[5] and 'K' not in oitavas:
        oitavas.append('K')
    elif resultadosN[5] < resultadosM[5] and 'L' not in oitavas:
        oitavas.append('L')      
    if resultadosN[6] > resultadosM[6] and 'M' not in oitavas:
        oitavas.append('M')
    elif resultadosN[6] < resultadosM[6] and 'N' not in oitavas:
        oitavas.append('N')
    if resultadosN[7] > resultadosM[7] and 'O' not in oitavas:
        oitavas.append('O')
    elif resultadosN[7] < resultadosM[7] and 'P' not in oitavas:
        oitavas.append('P')

# Processamento das quartas
for j in range(8, 11):
    if resultadosN[8] > resultadosM[8] and oitavas[0] == 'A' and 'A' not in quartas:
        quartas.append('A')
    elif resultadosN[8] > resultadosM[8] and oitavas[0] == 'B' and 'B' not in quartas:
        quartas.append('B')
    elif resultadosN[8] < resultadosM[8] and oitavas[1] == 'C' and 'C' not in quartas:
        quartas.append('C')
    elif resultadosN[8] < resultadosM[8] and oitavas[1] == 'D' and 'D' not in quartas:
        quartas.append('D')
    if resultadosN[9] > resultadosM[9] and oitavas[2] == 'E' and 'E' not in quartas:
        quartas.append('E')
    elif resultadosN[9] > resultadosM[9] and oitavas[2] == 'F':
        quartas.append('F')
    elif resultadosN[9] < resultadosM[9] and oitavas[3] == 'G' and 'G' not in quartas:
        quartas.append('G')
    elif resultadosN[9] < resultadosM[9] and oitavas[3] == 'H' and 'H' not in quartas:
        quartas.append('H')
    if resultadosN[10] > resultadosM[10] and oitavas[4] == 'I' and 'I' not in quartas:
        quartas.append('I')
    elif resultadosN[10] > resultadosM[10] and oitavas[4] == 'J' and 'J' not in quartas:
        quartas.append('J')
    elif resultadosN[10] < resultadosM[10] and oitavas[5] == 'K' and 'K' not in quartas:
        quartas.append('K')
    elif resultadosN[10] < resultadosM[10] and oitavas[5] == 'L' and 'L' not in quartas:
        quartas.append('L')
    if resultadosN[11] > resultadosM[11] and oitavas[6] == 'M' and 'M' not in quartas:
        quartas.append('M')
    elif resultadosN[11] > resultadosM[11] and oitavas[6] == 'N' and 'N' not in quartas:
        quartas.append('N')
    elif resultadosN[11] < resultadosM[11] and oitavas[7] == 'O' and 'O' not in quartas:
        quartas.append('O')
    elif resultadosN[11] < resultadosM[11] and oitavas[7] == 'P' and 'P' not in quartas:
        quartas.append('P')

#Processamento das semifinais
for k in range(12, 13):
    if resultadosN[12] > resultadosM[12] and quartas[0] == 'A' and 'A' not in semifinal:
        semifinal.append('A')
    elif resultadosN[12] > resultadosM[12] and quartas[0] == 'B' and 'B' not in semifinal:
        semifinal.append('B')
    elif resultadosN[12] < resultadosM[12] and quartas[0] == 'C' and 'C' not in semifinal:
        semifinal.append('C')
    elif resultadosN[12] < resultadosM[12] and quartas[0] == 'D' and 'D' not in semifinal:
        semifinal.append('D')
    if resultadosN[12] > resultadosM[12] and quartas[1] == 'E' and 'E' not in semifinal:
        semifinal.append('E')
    elif resultadosN[12] > resultadosM[12] and quartas[1] == 'F' and 'F' not in semifinal:
        semifinal.append('F')
    elif resultadosN[12] < resultadosM[12] and quartas[1] == 'G' and 'G' not in semifinal:
        semifinal.append('G')
    elif resultadosN[12] < resultadosM[12] and quartas[1] == 'H' and 'H' not in semifinal:
        semifinal.append('H')
    if resultadosN[13] > resultadosM[13] and quartas[2] == 'I' and 'I' not in semifinal:
        semifinal.append('I')
    elif resultadosN[13] > resultadosM[13] and quartas[2] == 'J' and 'J' not in semifinal:
        semifinal.append('J')
    elif resultadosN[13] < resultadosM[13] and quartas[2] == 'K' and 'K' not in semifinal:
        semifinal.append('K')
    elif resultadosN[13] < resultadosM[13] and quartas[2] == 'L' and 'L' not in semifinal:
        semifinal.append('L')
    elif resultadosN[13] > resultadosM[13] and quartas[3] == 'M' and 'M' not in semifinal:
        semifinal.append('M')
    elif resultadosN[13] > resultadosM[13] and quartas[3] == 'N' and 'N' not in semifinal:
        semifinal.append('N')
    elif resultadosN[13] < resultadosM[13] and quartas[3] == 'O' and 'O' not in semifinal:
        semifinal.append('O')
    elif resultadosN[13] < resultadosM[13] and quartas[3] == 'P' and 'P' not in semifinal:
        semifinal.append('P')

#Processamento da final
    if resultadosN[14] > resultadosM[14] and semifinal[0] == 'A' and final == '':
        final = 'A'
    elif resultadosN[14] > resultadosM[14] and semifinal[0] == 'B' and final == '':
        final = 'B'
    elif resultadosN[14] < resultadosM[14] and semifinal[0] == 'C' and 'C' not in final:
        final = 'C'
    elif resultadosN[14] < resultadosM[14] and semifinal[0] == 'D' and 'D' not in final:
        final = 'D'
    elif resultadosN[14] > resultadosM[14] and semifinal[1] == 'E' and 'E' not in final:
        final = 'E'
    elif resultadosN[14] > resultadosM[14] and semifinal[1] == 'F' and 'F' not in final:
        final = 'F'
    elif resultadosN[14] < resultadosM[14] and semifinal[1] == 'G' and 'G' not in final:
        final = 'G'
    elif resultadosN[14] < resultadosM[14] and semifinal[1] == 'H' and 'H' not in final:
        final = 'H'
    elif resultadosN[14] > resultadosM[14] and semifinal[2] == 'I' and 'I' not in final:
        final = 'I'
    elif resultadosN[14] > resultadosM[14] and semifinal[2] == 'J' and 'J' not in final:
        final = 'J'
    elif resultadosN[14] < resultadosM[14] and semifinal[2] == 'K' and 'K' not in final:
        final = 'K'
    elif resultadosN[14] < resultadosM[14] and semifinal[2] == 'L' and 'L' not in final:
        final = 'L'
    elif resultadosN[14] > resultadosM[14] and semifinal[3] == 'M' and 'M' not in final:
        final = 'M'
    elif resultadosN[14] > resultadosM[14] and semifinal[3] == 'N' and 'N' not in final:
        final = 'N'
    elif resultadosN[14] < resultadosM[14] and semifinal[3] == 'O' and 'O' not in final:
        final = 'O'
    elif resultadosN[14] < resultadosM[14] and semifinal[3] == 'P' and 'P' not in final:
        final = 'P'

#Saída
print(oitavas)

print(quartas)

print(semifinal)

print(final)
