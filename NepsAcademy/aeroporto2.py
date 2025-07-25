#Aeroporto
#https://neps.academy/br/exercise/290

testes = 0
resultados = []

#Entrada
def entrada():
    return map(int, input().split())

#Processamento
while True:
    A, V = entrada()
    if A == 0 and V == 0:
        break

    testes += 1
    voosPorAeroporto = {i: 0 for i in range(1, A + 1)}

    for _ in range(V):
        aeroporto1, aeroporto2 = entrada()
        voosPorAeroporto[aeroporto1] += 1
        voosPorAeroporto[aeroporto2] += 1

    max_voos = max(voosPorAeroporto.values())
    congestionados = [str(aeroporto) for aeroporto, voos in voosPorAeroporto.items() if voos == max_voos]
    resultados.append(congestionados)

#Saída
for i, aeroportos in enumerate(resultados, start=1):
    print(f'Teste {i}')
    print(' '.join(aeroportos))
    print()
