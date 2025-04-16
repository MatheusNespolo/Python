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
    marcadas = N
    desmarcadas = 0
    for inicio in inicios:
        if marcadas == N:
                break
        if inicio < terminos[0]:
            desmarcadas += 1
        for termino in terminos:
            if inicio >= termino:
                marcadas += 1

    return marcadas - desmarcadas

#Saída
print(marcar_consultas(inicios, terminos))
