# Sorteio
import random
lista = ['','','','','','','','','','','']
for i in range(1,11):
    lista[i] = str(input('Escreva o nome {}: '.format(i)))
    i + 1

sorte = random.choice(lista)
print('O nome escolhido foi {}!'.format(sorte))