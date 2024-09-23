numeros = []
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Valor duplicado não adicionado.')
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'Nn':
        print('Fim das adições.')
        break
    elif esc in 'Ss':
        print('Adicone mais valores.')
numeros.sort()
print(numeros)