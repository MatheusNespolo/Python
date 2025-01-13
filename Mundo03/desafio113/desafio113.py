import colorama

def leiaInt(msg):
    ok = False
    while True:
        try:
            n = int(input(msg))
            if isinstance(n, int):
                ok = True
        except (ValueError, TypeError):
            print(colorama.Back.RED + 'ERRO! Digite um número inteiro válido.' + colorama.Style.RESET_ALL)
        if ok:
            break

def leiaFloat(msg):
    ok = False
    while True:
        try:
            m = float(input(msg))
            if isinstance(m, float):
                ok = True
        except (ValueError, TypeError):
            print(colorama.Back.RED + 'ERRO! Digite um número real válido.' + colorama.Style.RESET_ALL)
        if ok:
            break

n = leiaInt('Digite um inteiro: ')
m = leiaFloat('Digite um real: ')
# print(colorama.Fore.BLUE + f'Você acabou de digitar o número {n}.' + colorama.Style.RESET_ALL)
