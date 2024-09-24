numeros = []
pares = []
impares = []
while True:
    num = numeros.append(int(input('Digite um número: ')))
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'Nn':
        print('Fim das adições.')
        break
    elif esc in 'Ss':
        print('Adicone mais valores.')
for novas in numeros:
    if novas % 2 == 0:
        pares.append(novas)
    else:
        impares.append(novas)
print(numeros.sort())
print(pares)
print(impares)