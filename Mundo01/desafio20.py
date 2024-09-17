#  Ordem aleatória (escolha um dos métodos)
import random
lista = []
for i in range(1,5):
    # inserir itens em uma lista
    lista.append(str(input('Escreva o nome {}: '.format(i))))   
    i + 1
ordem = random.sample(lista, k = 4)
print('Ordem embaralhada: ')
print(ordem)

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista2 = [n1,n2,n3,n4]
random.shuffle(lista2)
print('Ordem embaralhada: ')
print(lista2)