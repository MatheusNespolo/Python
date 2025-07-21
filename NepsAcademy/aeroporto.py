#Aeroporto
#https://neps.academy/br/exercise/290

testes = 0
aeroportosCongestionados = []
voosPorAeroporto = {}
def entrada():
    A, V = map(int, input().split())
    # A = Quantidade de aeroportos
    # V = Quantidade de voos
    for i in range(1, A + 1):
        voosPorAeroporto[i] = 0
    return A, V
aeroportos, voos = entrada()

#Processamento
if aeroportos != 0 and voos != 0:
    aeroporto1, aeroporto2 = map(int, input().split())
    voosPorAeroporto[aeroporto1] += 1
    voosPorAeroporto[aeroporto2] += 1
    testes += 1

for j in voosPorAeroporto:
    if voosPorAeroporto[j] == max(voosPorAeroporto.values()):
        aeroportosCongestionados.append(j)
 
#Saída
for k in range(testes):
    print(f'Teste {k + 1}')
    print(aeroportosCongestionados[k])
