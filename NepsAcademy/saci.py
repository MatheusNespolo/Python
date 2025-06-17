#Toca do Saci
#https://neps.academy/br/exercise/57

def encontra_caminho_saci():
    #Entrada
    N, M = map(int, input().split())
    toca = []
    #Posição inicial da Emília
    colunaEmilia = 0
    linhaEmilia = 0

    #Preenchimento da matriz da toca
    for i in range(N):
        linha = list(map(int, input().split()))
        if 2 in linha:
            colunaEmilia = linha.index(2)
            linhaEmilia = i
        toca.append(linha)

    #Processamento

    #Posição inicial da Emília
    distancia = 1 #Emília já está na sala 2
    filaPosicoes = [(linhaEmilia, colunaEmilia)]
    salasVisitadas = set() #conjunto para controlar salas visitadas
    salasVisitadas.add((linhaEmilia, colunaEmilia))

    #Direções possíveis
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #Fila para BFS (Breadth-First Search) (linha, coluna e distancia inicial)
    fila = [(linhaEmilia, colunaEmilia, 1)]

    while fila:
        l, c, dist = fila.pop(0) #Simula uma fila
        if toca[l][c] == 3:
            print(dist)
            return #Termina a função se achar a saída
        
        for dl, dc in direcoes:
            vl, vc = l + dl, c + dc

            if 0 <= vl < N and 0 <= vc < M and \
                toca[vl][vc] in [1, 3] and \
                (vl, vc) not in salasVisitadas:
                salasVisitadas.add((vl, vc))
                fila.append((vl, vc, dist + 1))

    #Saída
    print(distancia)

#Chamada da função
encontra_caminho_saci()
