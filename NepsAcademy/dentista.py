#Dentista
#https://neps.academy/br/exercise/248

#Entrada
inicios = []
terminos = []
consultas = 1
N = int(input())

inicio, termino = map(int, input().split())
inicios.append(inicio)
terminos.append(termino)

#Processamento
for j in range(1, N):
    if inicios[j] >= terminos[j-1]:
        consultas += 1
    if inicios[j] < terminos[j-1]:
        inicios.remove(inicios[j])
        terminos.remove(terminos[j])

#Saída
print(inicios)
print(terminos)
