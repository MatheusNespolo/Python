#Matryoshka

N = int(input())

m = list(map(int, input().split()))

recolher = 0

for i in m:
    if i > (i + 1):
        recolher += 1
    else:
        break

# Não finalizado