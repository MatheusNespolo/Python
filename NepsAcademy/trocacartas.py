#Troca de Cartas
#https://neps.academy/br/exercise/278

# Entrada
A, B = map(int, input().split())
cartasAlice = set(map(int, input().split()))
cartasBeatriz = set(map(int, input().split()))
trocas = 0

# Processamento

exclusivasAlice = cartasAlice - cartasBeatriz
exclusivasBeatriz = cartasBeatriz - cartasAlice

trocas = min(len(exclusivasAlice) , len(exclusivasBeatriz))

#Saída
print(trocas)
