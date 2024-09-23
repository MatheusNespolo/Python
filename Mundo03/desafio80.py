numeros = []
for cont in range(0,5):
    if cont == 0:
        num = int(input('Digite um número: '))
        numeros.append(num)
    else:
        num = int(input('Digite um número: '))
        if num > max(numeros):
            numeros.insert(4, num)
            print(f'Número {num} adicionado na última posição.')
        elif num < min(numeros):
            numeros.insert(0, num)
            print(f'Número {num} adicionado na primeira posição.')
        elif num > min(numeros) and num < max(numeros):
            numeros.insert(1, num)
            print(f'Número {num} adicionado na posição 1 da lista.')
print(numeros)