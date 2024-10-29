#print(input.__doc__)

#help(input)

def contador(i, f, p):
    """ Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}' , end='')
        c += p
    print('Fim!')

contador(2, 10, 2)

#help(contador)

def somar(a = 0, b = 0, c = 0): # Parâmetros opcionais
    """ Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor da soma
    :param b: segundo valor da soma
    :param c: terceiro valor da soma
    Função criada por Matheus Nespolo.
    """
    s = a + b + c
    print(f'A soma vale {s}.')

somar(2, 3, 5)
somar(8, 4)
somar(a=3, b=4, c=6)

def somar2(a = 0, b = 0, c = 0): # Parâmetros opcionais
    """ Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor da soma
    :param b: segundo valor da soma
    :param c: terceiro valor da soma
    Função criada por Matheus Nespolo.
    """
    s = a + b + c
    return s # Função retorna um resultado na variável que chama a função

r1 = somar2(2, 3, 5) # Variáveis chamando a função 'somar2'
r2 = somar2(1, 7)
r3 = somar2(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

#Escopo de variáveis
#n = variável global
#x = variável local
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')

#Programa principal
n = 2
print(f'No programa principal, n vale {n}.')

def teste(b):
    global a #variável 'a' se torna global mesmo dentro da função
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
