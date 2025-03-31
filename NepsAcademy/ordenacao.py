#Ordenação de Três Números
#https://neps.academy/br/exercise/151

numeros = []

for i in range(3):
    numeros.append(int(input()))

ordenada = sorted(numeros)

for numero in ordenada:
    print(numero)
