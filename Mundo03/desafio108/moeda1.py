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

def moeda(n):
    n = int(n)
    n = str(n)
    n = 'R$'+n+',00'
    return n
