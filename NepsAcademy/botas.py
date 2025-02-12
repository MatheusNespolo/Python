# Botas Trocadas - Versão Aprimorada

N = int(input())
tamanhosD = {}  
tamanhosE = {}  # Dicionários para contar botas

for _ in range(N):
    tamanho, pe = input().split()
    tamanho = int(tamanho)
    
    if pe == 'D':
        tamanhosD[tamanho] = tamanhosD.get(tamanho, 0) + 1
    elif pe == 'E':
        tamanhosE[tamanho] = tamanhosE.get(tamanho, 0) + 1

# Contagem de pares
pares = 0
for tamanho in tamanhosD:
    if tamanho in tamanhosE:
        pares += min(tamanhosD[tamanho], tamanhosE[tamanho])

print(pares)
