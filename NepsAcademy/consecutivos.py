#Consecutivos
lista = []
consec = 0
N = int(input())
lista.append(input().split())
len(lista) == N
def achar_consecutivos():
    for i in lista:
        if lista[0][i] == lista[0][i+1]:
            consec += 1
    return consec()
print(lista)
print(consec)
