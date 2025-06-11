#Dentista
#https://neps.academy/br/exercise/248

def resolver_dentista():
    #Entrada
    N = int(input())

    consultas = []
    for _ in range(N):
        x, y = map(int, input().split())
        consultas.append((y, x))

    #Processamento
    consultas_ordenadas = sorted(consultas) #Ordenar consultas por ordem de término

    consultas_atendidas = 0
    ultimo_atendimento = 0

    for y, x in consultas_ordenadas:
        if x >= ultimo_atendimento:
            consultas_atendidas += 1
            ultimo_atendimento = y

    #Saída
    print(consultas_atendidas)

#Chamada
resolver_dentista()
