numeros = []
cont = 0
cinco = 0
while True:
    num = numeros.append(int(input('Digite um número: ')))
    cont += 1
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'Nn':
        print('Fim das adições.')
        break
    elif esc in 'Ss':
        print('Adicone mais valores.')
print(f'A) Foram digitados {cont} números.')
print(f'B) Ordem decrescente: {sorted(numeros, reverse=True)}')
print(f'C) O número 5 foi digitado {numeros.count(5)} vezes e está na lista.')