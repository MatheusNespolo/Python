#Toca do Saci
#https://neps.academy/br/exercise/57

#Entrada
N, M = map(int, input().split())
toca = []
colunaEmilia = 0
linhaEmilia = 0

for i in range(N):
    linha = list(map(int, input().split()))
    if 2 in linha:
        colunaEmilia = linha.index(2)
        linhaEmilia = i
    else:
        colunaEmilia = colunaEmilia
    toca.append(linha)

#Processamento
salasVisitadas = deque()
distancia = 1
salasVisitadas.append((linhaEmilia, colunaEmilia))
while salasVisitadas:
    linha, coluna = salasVisitadas.popleft()
    if toca[linha][coluna] == 1: #Verifica se é um vizinho válido
        salasVisitadas.append((linha, coluna))
        distancia += 1
        toca[linha][coluna] = 0
    elif toca[linha][coluna] == 3:
        distancia += 1
        break

#Saída
print(distancia)
