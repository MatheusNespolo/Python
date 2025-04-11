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
for j in range(1, N):
    if inicios[j] >= terminos[j-1]:
        consultas += 1
    if inicios[j] < terminos[j-1]:
        inicios.remove(inicios[j])
        terminos.remove(terminos[j])
        consultas = consultas

#Saída
print(inicios)
print(terminos)
print(consultas)
