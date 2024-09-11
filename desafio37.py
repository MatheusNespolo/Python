print('-*'*20)
num = int(input('Digite um número inteiro: '))
base = (input('Escolha a base de conversão:\n[1] - Binário;\n[2] - Octal;\n[3] - Hexadecimal.\n[X] - Sair\nBase: '))
if base == '1':
    print(bin(num))
elif base == '2':
    print(oct(num))
elif base == '3':
    print(hex(num))
elif base == 'X' or 'x':
    print('Fim da conversão.')
else:
    print('Digite uma base válida.')