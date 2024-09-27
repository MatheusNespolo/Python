lista = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Nota 1: ')))
    lista.append(int(input('Nota 2: ')))
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'Nn':
        print('='*30)
        break
for i, pessoas in enumerate(lista):
    print(i, pessoas)