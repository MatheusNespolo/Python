#Dentista
#https://neps.academy/br/exercise/248

#Entrada
consultas = 1
inicios = []
terminos = []
N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    inicios.append(X)
    terminos.append(Y)

#Processamento
inicios.pop(0)
for j in range(0, len(inicios)-1):
    if inicios[j] < terminos[j-1]:
        consultas = consultas

for k in range(0, len(inicios)-1):
    if inicios[k] >= terminos[k-1]:
        consultas += 1

#Saída
print(inicios)
print(terminos)
print(consultas)
