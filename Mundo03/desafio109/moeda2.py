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
