somaidade = 0
mediaidade = 0
idade = 0
idadeh = 0
mulhermenor20 = 0
for p in range(1,5):
    nome = str(input('Digite o nome da pessoa {}: '.format(p)))
    idade = int(input('Digite a idade da pessoa {}: '.format(p)))
    sexo = input('Selecione o sexo - M ou F: ')
    somaidade =+ idade
    if p == 1 and sexo in 'Mm':
        nomeh = nome
        idadeh = idade
    if sexo in 'Mm' and idade > idadeh:
        idadeh = idade
        nomeh = nome
    else:
        nomeh = 'nenhum'
    if sexo in 'Ff' and idade < 20:
        mulhermenor20 += 1
    

mediaidade = somaidade/4
print('A média entre as idades é: {} anos.'.format(mediaidade))
print('O homem mais velho é: {}.'.format(nomeh))
print('O número de mulheres menores de 20 anos é: {}'.format(mulhermenor20))