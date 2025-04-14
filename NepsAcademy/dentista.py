#Dentista
#https://neps.academy/br/exercise/248

#Entrada
inicios = []
terminos = []
consultas = 0
N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    inicios.append(X)
    terminos.append(Y)

#Processamento
def marcar_consultas(inicios, terminos):
    inicios.remove(inicios[0])
    consultas = 1
    for inicio in inicios:
        if consultas == N:
                break
        for termino in terminos:
            if consultas == N:
                break
            if inicio >= termino:
                consultas += 1
            if inicio < termino:
                break
    return consultas

#Saída
print(marcar_consultas(inicios, terminos))
