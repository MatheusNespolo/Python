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
contador = voos

#Processamento
while aeroportos != 0 and voos != 0:
    aeroporto1, aeroporto2 = map(int, input().split())
    voosPorAeroporto[aeroporto1] += 1
    voosPorAeroporto[aeroporto2] += 1
    contador -= 1
    if contador == 0:
        testes += 1
        aeroportos, voos = entrada()
        contador = voos

for j in voosPorAeroporto:
    print(voosPorAeroporto[j])
 
#Saída
for k in range(testes):
    print(f'Teste {k + 1}')
    print(aeroportosCongestionados[k])
