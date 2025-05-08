# Drone de Entrega
# https://neps.academy/br/exercise/14

# Dimensões da caixa
A = int(input())
B = int(input())
C = int(input())
caixa = [A, B, C]

# Dimensões da maior janela
H = int(input())
L = int(input())

# Dimensões da menor face da caixa
caixa.remove(max(caixa))

if caixa[0] <= H and caixa[1] <= L or caixa[0] <= L and caixa[1] <= H:
    print('S')
else:
    print('N')
