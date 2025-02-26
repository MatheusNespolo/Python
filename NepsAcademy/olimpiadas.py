# Olimpíadas

N, M = map(int, input().split())
# N = número de países, M = número de modalidades

paises = list(range(1, N + 1))
medalhas = []

for j in range(M):
    O, P, B = map(int, input().split())
    medalhas.append([O, P, B])

# Contar medalhas por país
contagem_medalhas = {}
for O, P, B in medalhas:
    if O not in contagem_medalhas:
        contagem_medalhas[O] = [0, 0, 0]
    if P not in contagem_medalhas:
        contagem_medalhas[P] = [0, 0, 0]
    if B not in contagem_medalhas:
        contagem_medalhas[B] = [0, 0, 0]
    contagem_medalhas[O][0] += 1  # Ouro
    contagem_medalhas[P][1] += 1  # Prata
    contagem_medalhas[B][2] += 1  # Bronze

# Ordenar países por medalhas (ouro, prata, bronze) e ordem original
paises_ordenados = sorted(contagem_medalhas.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], list(range(1, N + 1)).index(x[0])))

# Imprimir classificação
for pais, medalhas in paises_ordenados:
    print(pais, end=' ')
