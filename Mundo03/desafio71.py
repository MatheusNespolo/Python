print('-|'*30)
print('-|-'*7,'Caixa eletrônico','-|-'*7)
print('-|'*30)
print('Notas disponíveis:\nR$50\nR$20\nR$10\nR$1')
while True:
    saque = int(input('Qual será o valor do saque? '))
    nota50 = saque // 50
    nota20 = (saque - nota50 * 50) // 20
    nota10 = (saque - nota50 * 50 - nota20 * 20) // 10
    nota1 = (saque - nota50 * 50 - nota20 * 20 - nota10 * 10)
    print(f'Notas de R$50: {nota50}\nNotas de R$20: {nota20}\nNotas de R$10: {nota10}\nNotas de R$1: {nota1}')
    sair = str(input('Deseja fazer outro saque? (S/N) '))
    if sair in 'Nn':
        break
    else:
        saque = 0
        nota50 = 0
        nota20 = 0
        nota10 = 0
        nota1 = 0
