import random

lista = []

def numAleatorio():
    for i in range (0,5):
        num = random.randint(0,999)
        lista.append(num)
    return lista

numAleatorio()
print(sorted(lista))
print(f'O maior valor é: {max(lista)}')
print(f'O menor valor é: {min(lista)}')
