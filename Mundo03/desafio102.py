def fatorial(num=1, show=True):
    """ Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    if s == 1:
        show = True
    elif s == 2:
        show = False
    if show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            if c == 1:
                print(f'{c}', end='')
                break
            print(f'{c} x ', end='')
        print(f' = {f}')

n = int(input('Digite um número para o fatorial: '))
s = int(input('Deseja mostrar a multiplicação? \n(1 - Sim/ 2 - Não): '))
fat = fatorial(n)
if s == 2:
    print(fat)
