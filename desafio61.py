print('-*'*20)
print('Progressão aritmética')
print('-*'*20)
termo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da progressão: '))
start = bool
cont = 0
while start:
    if cont <= 10 and start:
        print(termo)
        termo = (termo + raz)
        cont = (cont + 1)
    else:
        start == 0
        break