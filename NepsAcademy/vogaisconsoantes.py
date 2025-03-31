#Vogais e Consoantes
#https://neps.academy/br/exercise/399

S = str(input())
vogais = []
consoantes = []

for letra in S:
    if letra in 'aeiou':
        vogais.append(letra)
    else:
        consoantes.append(letra)

print('Vogais:', end=' ')
for letra in vogais:
    print(letra)
print()
print('Consoantes:', end=' ')
for letra in consoantes:
    print(letra)
