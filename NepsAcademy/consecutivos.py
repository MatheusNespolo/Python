#Consecutivos
lista = []
consec = 0
N = int(input())
X = input()
for i in range(0,N):
    X = lista.append(int(input()))
    if lista[i] == lista[i + 1]:
        consec += 1
