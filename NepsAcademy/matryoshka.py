#Matryoshka

N = int(input())
tamanhos = list(map(int, input().split()))

sequencia_correta = sorted(tamanhos)
bonecas_recolher = []

for i in range(N):
    if tamanhos[i] != sequencia_correta[i]:
        bonecas_recolher.append(tamanhos[i])

bonecas_recolher.sort()

print(len(bonecas_recolher))
if bonecas_recolher:
    print(' '.join(map(str, bonecas_recolher)))
