#Aeroporto
#https://neps.academy/br/exercise/290

#Entrada
A, V = map(int, input().split())
contador = V
# A = Quantidade de aeroportos
# V = Quantidade de voos
voosPorAeroporto = {}
testes = 0
aeroportosCongestionados = []
for i in range(1, A + 1):
    voosPorAeroporto[i] = 0

#Processamento
while A != 0 and V != 0:
    aeroporto1, aeroporto2 = map(int, input().split())
    voosPorAeroporto[aeroporto1] += 1
    voosPorAeroporto[aeroporto2] += 1
    contador -= 1
    if contador == 0:
        testes += 1
        for j in voosPorAeroporto:
            if voosPorAeroporto[j] == max(voosPorAeroporto.values()):
                aeroportosCongestionados.append(j)
        break
    
#Saída
for k in range(testes):
    print(f'Teste {k + 1}')
    print(aeroportosCongestionados[k])
