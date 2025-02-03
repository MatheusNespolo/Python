#Matryoshka

N = int(input())

m = list(map(int, input().split()))
mo = sorted(m)

recolher = 0
recolhidos = []

for i in range(0, len(m)):
    if i != mo[i]:
        recolher += 1
        recolhidos.append(m[i])
    elif i == mo[i]:
        recolher = recolher

print(recolher)
for k in recolhidos:
    print(k, end=' ')

# Não finalizado
