import colorama

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(colorama.Back.RED + 'ERRO! Digite um número inteiro válido.' + colorama.Style.RESET_ALL)
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(colorama.Fore.BLUE + f'Você acabou de digitar o número {n}.' + colorama.Style.RESET_ALL)
