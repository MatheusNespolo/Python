#Dentista
#https://neps.academy/br/exercise/248

#Entrada
inicios = []
terminos = []
N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    inicios.append(X)
    terminos.append(Y)

#Processamento
def marcar_consultas(inicios, terminos):
    consultas = 1
    for j in range(len(inicios)):
        if inicios[j] >= terminos[j-1]:
            consultas += 1
        if inicios[j] < terminos[j-1]:
            consultas = consultas

    return consultas

#Saída
print(marcar_consultas(inicios, terminos))
