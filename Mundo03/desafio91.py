import random
import time
final = []
resulFin = []
resultados = {
    'jogador1': random.randint(1,6),
    'jogador2': random.randint(1,6),
    'jogador3': random.randint(1,6),
    'jogador4': random.randint(1,6)
}
for k, v in resultados.items():
    print(f'{k} tirou {v}')
    time.sleep(1)
print('Ranking dos jogadores')
for i in sorted(resultados, key = resultados.get):
    final.append(i)
    resulFin.append(resultados[i])
print(f'1º Lugar: {final[3]} com {resulFin[3]}')
print(f'2º Lugar: {final[2]} com {resulFin[2]}')
print(f'3º Lugar: {final[1]} com {resulFin[1]}')
print(f'4º Lugar: {final[0]} com {resulFin[0]}')
