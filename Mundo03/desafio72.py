cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
sele = int(input('Escolha um número de 0 a 20: '))
while True:
    if sele < 0 or sele > 20:
        sele = int(input('Escolha um número de 0 a 20: '))
    else:
        print(f'Número por extenso: {cont[sele]}')
        break