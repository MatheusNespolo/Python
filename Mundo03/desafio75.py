num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))
tupla = (num1, num2, num3, num4)
print('A)', tupla.count(9))
print('B)', tupla.index(3))
for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print('C)', tupla[cont])
        cont += 1
