#Dentista
#https://neps.academy/br/exercise/248

#Bibliotecas
from collections import deque

#Entrada
inicios = deque()
terminos = deque()
N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    inicios.append(X)
    terminos.append(Y)
inicios.popleft()

#Processamento
def marcar_consultas(inicios, terminos):
    consultas = N
    for inicio in inicios:
        for termino in terminos:
            if inicio >= termino:
                consultas += 1
            if (inicio - termino) < 0:
                inicios.popleft()
    return consultas

#Saída
print(marcar_consultas(inicios, terminos))
