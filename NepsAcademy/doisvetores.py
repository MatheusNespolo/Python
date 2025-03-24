#Dois Vetores: Pares e Ímpares
#https://neps.academy/br/exercise/194

pares = []
impares = []

for i in range(10):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

for numero in pares:
    print(numero, end=' ')
print()
for numero in impares:
    print(numero, end=' ')
