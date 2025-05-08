# O Problema 3n + 1
# https://neps.academy/br/exercise/259

N = int(input())
contador = 0

# Pequeno conceito de recursão
while N != 1:
    if N % 2 == 0:
        N = N // 2
        contador += 1
    else:
        N = 3 * N + 1
        contador += 1

print(contador)
