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
    desmarcadas = 0
    for inicio in inicios:
        for termino in terminos:
            if inicio >= termino:
                consultas += 1
            if (inicio - termino) < 0:
                desmarcadas += 1
    return consultas - desmarcadas

#Saída
print(marcar_consultas(inicios, terminos))
