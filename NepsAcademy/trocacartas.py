#Troca de Cartas
#https://neps.academy/br/exercise/278

# Entrada

A, B = map(int, input().split())
cartasAlice = list(map(int, input().split()))
cartasBeatriz = list(map(int, input().split()))
cartasTrocadas = []
trocas = 0

# Processamento

menorConjunto = min(A, B)

for i in range(menorConjunto):
    if cartasAlice[i] not in cartasBeatriz and cartasAlice[i] not in cartasTrocadas:
        cartasTrocadas.append(cartasAlice[i])
        trocas += 1

#Saída

print(trocas)
