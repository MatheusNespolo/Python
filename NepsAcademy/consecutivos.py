#Consecutivos
consec = 0
N = int(input())
X = input()
numeros = list(map(int, X.split()))
for i, m in enumerate(numeros):
    if numeros[i] == numeros[i-1]:
        consec += 1
    i += 1