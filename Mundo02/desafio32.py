ano = input('Digite um ano para saber se é bissexto: ')
final = int(ano[2:])
if final%4 == 0:
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto.')
