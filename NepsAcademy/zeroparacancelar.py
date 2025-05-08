# Zero para Cancelar
# https://neps.academy/br/exercise/1486

N = int(input())
vendas = []

# Pequeno conceito de fila
for i in range(N):
    X = int(input())
    if X == 0:
        vendas.pop()
    else:
        vendas.append(X)

print(sum(vendas))
