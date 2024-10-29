import random
from time import sleep

numeros = list()

def linha():
    print('-='*20)

def timer():
    sleep(0.3)

def sorteia(lista):
    linha()
    for cont in range(0, 5):
        lista.append(random.randint(0, 100))
    print(f'Números sorteados: {numeros}.', flush=True)
    timer()

def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Soma dos números pares: {soma}.')
    timer()
    linha()

sorteia(numeros)
somaPar(numeros)
