#Soma de Casas
#https://neps.academy/br/exercise/255

#Entrada
N = int(input())
casas = [int(input()) for _ in range(N)]
K = int(input())

#Processamento + Saída
for j in range(len(casas)):
    for k in range(j+1, len(casas)):
        if casas[j] + casas[k] == K:
            print(casas[j], casas[k])
            break
