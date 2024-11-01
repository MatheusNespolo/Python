#Xadrez
L = int(input())
C = int(input())
linhab = []
linhap = []
tabuleiro = []

for i in range(L):
    i += 1
    if i % 2 == 0:
        linhab.append(0)
    else:
        linhab.append(1)

for f in range(L):
    if f % 2 == 0:
        linhap.append(0)
    else:
        linhap.append(1)

for c in range(C):
    c += 1
    if c % 2 == 0:
        tabuleiro.append(linhap[:])
    else:
        tabuleiro.append(linhab[:])

if tabuleiro[C-1][L-1] == 1:
    print(1)
else:
    print(0)
