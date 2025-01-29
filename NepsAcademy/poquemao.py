#Po que mão

N = int(input())

X = int(input())
Y = int(input())
Z = int(input())

doces_necessarios = [X, Y, Z]

# Ordena a lista para tentar evoluir as pô-que-mãos que precisam de menos doces primeiro
doces_necessarios.sort()

pode_evoluir = 0

for i in doces_necessarios:
    if N >= i:
        N -= i
        pode_evoluir += 1
    else:
        break

print(pode_evoluir)
