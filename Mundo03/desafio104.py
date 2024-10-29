import colorama

def leiaInt(num):
    if type(num) == int:
        print(f'Você acabou de digitar o número {num}.')
    else:
        print('ERRO! Digite um número válido.')

n = leiaInt('Digite um número: ')
