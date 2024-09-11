nome = list = ['','','','']
idade = list = ['','','','']
sexo = list = ['','','','']

for c in range(0,4):
    nome[c] = str(input('Digite o nome da pessoa {}: '.format(c+1)))
    idade[c] = int(input('Digite a idade da pessoa {}: '.format(c+1)))
    sexo[c] = input('Selecione o sexo - M ou F: ')
print('A média entre as idades é: {}'.format((sum(idade))/4))
print(nome[max(idade[0])])