#Pares ou com Último Algarismo Igual a 5

X = int(input())
Y = int(input())
Z = int(input())

final = 0

valores = [X, Y, Z]

for _ in range(len(valores)):
    if valores[_] % 2 == 0 or valores[_] % 5 == 0:
        final += 1

print(final)
