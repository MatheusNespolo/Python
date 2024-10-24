cont = 1
nomes = []
sexos = []
mulheres = []
idades = []
acima = []
cadastros = []

pessoa = {}

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['Sexo'] = str(input('Digite o sexo: (F/M) ')).upper()[0]
        sexos.append(pessoa['Sexo'])
        if pessoa['Sexo'] == 'F':
            mulheres.append(pessoa['Nome'])
        if pessoa['Sexo'] in 'FM':
            break
        print('ERRO! Digite F ou M para o sexo.')
    pessoa['Idade'] = int(input('Digite a idade: '))
    idades.append(pessoa['Idade'])
    cadastros.append(pessoa.copy())
    resp = str(input('Continuar? (S/N) ')).upper()[0]
    cont += 1
    if resp in 'Nn':
        print('Cadastro finalizado!')
        break
print('-='*30)
media = (sum(idades) / cont)

for j in idades:
    if j > media:
        acima.append(j)

print(f'Pessoas cadastradas: {cont-1}')
print(f'Média de idade: {media}')
print(f'Mulheres: {mulheres}')
print(f'Idades acima da média: {acima}')
print(cadastros)
