# Ogros
# https://neps.academy/br/exercise/261

# Entrada
N, M = map(int, input().split())
    # N = faixas de premiações
    # M = ogros

limites = [(input(). split())]
premiacoes = [(input().split())]
forcas = [(input().split())]
premiacao_ogro = []

# Processamento
for i in range(M):
    for j in range(N):
        if int(limites[j][0]) <= int(forcas[i][0]) <= int(limites[j][1]):
            premiacao_ogro.append(int(premiacoes[j][1]))

# Saída
for j in limites:
    print(j)
for j in premiacoes:
    print(j)
for j in forcas:
    print(j)
for j in premiacao_ogro:
    print(j, end=' ')
