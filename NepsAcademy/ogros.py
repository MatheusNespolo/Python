# Ogros
# https://neps.academy/br/exercise/261

# Entrada
N, M = map(int, input().split())
    # N = faixas de premiações
    # M = ogros

limites = list(map(int, input().split()))
premiacoes = list(map(int, input().split()))
forcas = list(map(int, input().split()))
premiacao_ogro = {}

# Processamento
for i in range(M):
    for j in range(N):
        if limites[j] <= forcas[i]:
            premiacao_ogro[forcas[i]] = premiacoes[j]
            break

# Saída
print(limites)
print(premiacoes)
print(forcas)
print(premiacao_ogro)
