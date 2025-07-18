#Aeroporto
#https://neps.academy/br/exercise/290

#Entrada
A, V = map(int, input().split())
contador = V
# A = Quantidade de aeroportos
# V = Quantidade de voos
voosPorAeroporto = {}
testes = 0
for i in range(1, A):
    voosPorAeroporto[i] = 0

#Processamento
while A != 0 and V != 0:
    aeroporto1, aeroporto2 = map(int, input().split())
    voosPorAeroporto[aeroporto1] += 1
    voosPorAeroporto[aeroporto2] += 1
    contador -= 1
    if contador == 0:
        testes += 1
        break
    
#Saída
for j in range(testes):
    print(f'Teste {j+1}')
print(voosPorAeroporto)
