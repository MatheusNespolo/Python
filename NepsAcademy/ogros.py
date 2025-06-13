# Ogros
# https://neps.academy/br/exercise/261

# Entrada
N, M = map(int, input().split())
    # N = faixas de premiações
    # M = ogros

limites = [(input(). split())]
premiacoes = [(input().split())]
forcas = [(input().split())]
forcas = sorted(forcas)
premiacao_ogro = []

# Processamento
for i in range(len(forcas)):
    if forcas[i] < limites[0]:
        premiacao_ogro.append(premiacoes[0])

# Saída
for j in limites:
    print(j)
for j in premiacoes:
    print(j)
for j in forcas:
    print(j)
for j in premiacao_ogro:
    print(j)
