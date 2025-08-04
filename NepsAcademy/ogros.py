# Ogros
# https://neps.academy/br/exercise/261

# Entrada
N, M = map(int, input().split())
    # N = faixas de premiações
    # M = ogros

limites = [(input(). split())]
premiacoes = [(input().split())]
forcas = [(input().split())]

premiacoes_por_forca = []

# Processamento
for i in range(M):
    if forcas[i] <= limites[0]:
        premiacoes_por_forca.append(premiacoes[i])

# Saída
for j in limites:
    print(j)
for j in premiacoes:
    print(j)
for j in forcas:
    print(j)
print(*premiacoes_por_forca)