# Divisão do Tesouro
# https://neps.academy/br/exercise/976

A = int(input())
# Número de moedas na arca
N = int(input())
# Número de marinheiros (sem contar o capitão)
CapitaoOlhoRoxo = 0
premioMarinheiro = (A / N)
while CapitaoOlhoRoxo < (2 * premioMarinheiro):
    premioMarinheiro -= 1
    CapitaoOlhoRoxo += 1
