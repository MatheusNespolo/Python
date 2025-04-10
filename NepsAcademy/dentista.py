#Dentista
#https://neps.academy/br/exercise/248

#Entrada
horarios = []
duracao = []
consultas = 1
N = int(input())

for i in range(N):
    inicio, termino = map(int, input().split())
    duracao.append(termino - inicio)
    horarios.append(inicio)
    horarios.append(termino)

#Processamento
for j in range(N*2):
    if j % 2 == 0:
        if horarios[j] >= horarios[j-1]:
            consultas += 1
        if horarios[j] < horarios[j-1]:
            horarios.remove(horarios[j])
            consultas = consultas

#Saída
print(consultas)
