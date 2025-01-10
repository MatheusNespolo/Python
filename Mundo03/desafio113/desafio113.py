import colorama

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(colorama.Back.RED + 'ERRO! Digite um número inteiro válido.' + colorama.Style.RESET_ALL)
        n = str(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        if ok:
            break
    return valor

def leiaFloat(msg):
    okF = False
    valorF = 0
    while True:
        try:
            m = float(input(msg))
        except (ValueError, TypeError):
            print(colorama.Back.RED + 'ERRO! Digite um número real válido.' + colorama.Style.RESET_ALL)
        m = str(msg)
        if m.isnumeric():
            valorF = float(m)
            okF = True
        if okF:
            break
    return valorF

n = leiaInt('Digite um inteiro: ')
m = leiaFloat('Digite um real: ')
# print(colorama.Fore.BLUE + f'Você acabou de digitar o número {n}.' + colorama.Style.RESET_ALL)
