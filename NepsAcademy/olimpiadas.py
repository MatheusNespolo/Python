#Olimpíadas

N, M = map(int, input().split())
# N = número de países, M = número de modalidades
medalhasPorModalidade = []

for _ in range(M):
    O, P, B = map(int, input().split())
    medalhasPorModalidade.append((O, P, B))

for i in range(N):
    medalhasPorPais = []
    for j in range(M):
        medalhasPorPais.append(medalhasPorModalidade[j][i])
    print(medalhasPorPais)
