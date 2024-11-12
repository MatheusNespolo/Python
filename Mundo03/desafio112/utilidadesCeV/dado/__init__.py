import colorama

def aumentar(n, por):
    aumento = (por / 100) * n
    return aumento + n

def diminuir(n, por):
    queda = (por / 100) * n
    return n - queda

def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def aumentar(n, por, formata = True):
    aumento = (por / 100) * n
    n = aumento + n
    if formata == True:
        n = int(n)
        n = str(n)
        n = 'R$'+n+',00'
    return n

def diminuir(n, por, formata = True):
    queda = (por / 100) * n
    n = n - queda
    if formata == True:
        n = int(n)
        n = str(n)
        n = 'R$'+n+',00'
    return n

def dobro(n, formata = True):
    n = n * 2
    if formata == True:
        n = int(n)
        n = str(n)
        n = 'R$'+n+',00'
    return n

def metade(n, formata = True):
    n = n / 2
    if formata == True:
        n = int(n)
        n = str(n)
        n = 'R$'+n+',00'
    return n

def moeda(n):
    n = int(n)
    n = str(n)
    n = 'R$'+n+',00'
    return n

def leiaMoeda():
    n = str(input('Digite o preço: R$'))
    if n.isdigit():
        return float(n)
    else:
        while n.isdigit() == False:
            print(colorama.Back.RED + f'Entrada inválida! {n} não é um número.' + colorama.Style.RESET_ALL)
            n = str(input('Digite o preço: R$'))
            if n.isdigit():
                return float(n)
