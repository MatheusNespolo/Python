#1071 - Soma de Impares Consecutivos I
X = int(input())
Y = int(input())
soma = 0

if X > Y:
    X, Y = Y, X

for i in range(X+1,Y):
    if i % 2 != 0:
        soma += i

print(soma)
