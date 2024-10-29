from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até o {f} de {p} em {p}.')
    print('-='*20)
    sleep(2.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) #flush impede a bufferização da contagem
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True) #flush impede a bufferização da contagem
            sleep(0.5)
            cont -= p
        print('Fim!')
    print('-='*20)

contador(1, 10, 1)

contador(10, 0, 2)

print('Agora personalize a contagem: ')
ini = int(input('Insira o início da contagem: '))
fim = int(input('Insira o final da contagem: '))
pas = int(input('Insira o passo da contagem: '))
contador(ini, fim, pas)
