peso = list()
dado = list()
cadastro = 0
while True:
    dado.append(str(input('Nome: ')))
    peso.append(int(input('Peso: ')))
    cadastro += 1
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'Nn':
        print('Fim dos cadastros.')
        break
    elif esc in 'Ss':
        print('Cadastre mais pessoas.')
print(f'Ao todo, você cadastrou {cadastro} pessoas.')
print(f'O maior peso foi de {max(peso)}Kg. Peso de {dado[peso.index(max(peso))]}')
print(f'O menor peso foi de {min(peso)}Kg. Peso de {dado[peso.index(min(peso))]}')
