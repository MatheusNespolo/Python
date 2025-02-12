#Pares ou com Último Algarismo Igual a 5

X = int(input())
Y = int(input())
Z = int(input())

pares = 0
finais = 0

def par(num):
    if num % 2 == 0:
        pares += 1
    return pares

def final5(num):
    if num % 5 == 0:
        finais += 1
    return finais

par(X)
par(Y)
par(Z)
final5(X)
final5(Y)
final5(Z)

print(pares + finais)
