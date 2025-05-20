# Ogros
# https://neps.academy/br/exercise/261

N, M = map(int, input().split())
# N = quantidade de faixas de premiações
# M = quantidade de ogros

limites = list(map(int, input().split()))

premiacoes = list(map(int, input().split()))

forcas = list(map(int, input().split()))

for forca in forcas:
    if forca >= 0 and forca >= 5:
        pontuacao = 10
    elif forca >= 6 and forca <= 10:
        pontuacao = 30
