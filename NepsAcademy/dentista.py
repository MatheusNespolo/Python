#Dentista
#https://neps.academy/br/exercise/248

#Entrada
consultas = {'inicio':[], 'fim':[]}
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    consultas['inicio'].append(x)
    consultas['fim'].append(y)
consultas['inicio'].remove(consultas['inicio'][0])

#Processamento
for i in range(len(consultas['inicio'])):
    if consultas['inicio'][i] >= consultas['fim'][i]:
        consultas['inicio'].remove(consultas['inicio'][i])
        consultas['fim'].remove(consultas['fim'][i])
        N -= 1
    if consultas['inicio'][i] < consultas['fim'][i]:
        consultas['inicio'].remove(consultas['inicio'][i])
        consultas['fim'].remove(consultas['fim'][i])

#Saída
print()
