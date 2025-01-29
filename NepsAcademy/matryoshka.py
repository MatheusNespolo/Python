#Matryoshka

N = int(input())

m = list(map(int, input().split()))
mo = sorted(m)

recolher = 0
recolhidos = []

for i in m:
    i == i

for j in mo:
    if i != j:
        recolher += 1
        recolhidos.append(j)

print(recolher)
for k in recolhidos:
    print(k, end=' ')

# Não finalizado
