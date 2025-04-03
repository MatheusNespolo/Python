#Soma de Casas
#https://neps.academy/br/exercise/255

#Entrada
N = int(input())
casas = [int(input()) for _ in range(N)]
K = int(input())

#Processamento + Saída
valores_vistos = set()
for num in casas:
    complemento = K - num
    #Cria a variável complemento que é o número que falta para chegar a K
    if complemento in valores_vistos:
        print(complemento, num)
    valores_vistos.add(num)
