#Dentista
#https://neps.academy/br/exercise/248

def resolver_dentista():
    #Entrada
    N = int(input())

    consultas = []
    for _ in range(N):
        inicio, fim = map(int, input().split())
        consultas.append((fim, inicio))

    #Processamento
    consultas_ordenadas = sorted(consultas) #Ordenar consultas por ordem de término

    consultas_atendidas = 0
    ultimo_atendimento = 0

    for fim, inicio in consultas_ordenadas:
        if inicio >= ultimo_atendimento:
            consultas_atendidas += 1
            ultimo_atendimento = fim

    #Saída
    print(consultas_atendidas)

#Chamada
resolver_dentista()
