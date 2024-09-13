import random
sair = bool
ale = random.randint(0,9999)
opcao = 0
while opcao != 5:
    val1 = int(input('Primeiro valor: '))
    val2 = int(input('Segundo valor: '))
    print('''    [ 1 ] - somar
    [ 2 ] - multiplicar
    [ 3 ] - maior
    [ 4 ] - novos números
    [ 5 ] - sair do programa''')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        print('A soma dos números é igual a {}.'.format(val1+val2))
    elif opcao == 2:
        print('A multiplicação dos números é igual a {}.'.format(val1*val2))
    elif opcao == 3:
        if val1 > val2:
            print('{} é maior que {} e {}.'.format(val1+1,val1,val2))
        elif val2 > val1:
            print('{} é maior que {} e {}.'.format(val2+1,val1,val2))
    elif opcao == 4:
        print('{} é diferente de {} e {}.'.format(ale,val1,val2))