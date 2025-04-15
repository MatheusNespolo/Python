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
inicios.remove(inicios[0])

#Processamento
def marcar_consultas(inicios, terminos):
    consultas = 1
    for i in range(len(inicios)):
        if inicios[i] >= terminos[i-1]:
            consultas += 1
    print(inicios)
    print(terminos)

    return consultas

#Saída
print(marcar_consultas(inicios, terminos))
