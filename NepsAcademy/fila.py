#Fila (OBI2014)

N = int(input())
fila = list(map(int, input().split()))
M = int(input())
desistentes = list(map(int, input().split()))
filaFinal = ''

for i in range(0,len(desistentes)):
    fila.remove(desistentes[i])

for restantes in fila:
    filaFinal += str(restantes) + ' '

print(filaFinal)
