cont = 1
nomes = []
sexos = []
mulheres = []
idades = []
acima = []
cadastros = []

cadastro = {
    'Nome': '',
    'Sexo': '',
    'Idade': ''
}

while True:
    nome = str(input('Digite o nome: '))
    nomes.append(nome)
    sexo = str(input('Digite o sexo: (F/M) '))
    sexos.append(sexo)
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Digite a idade: '))
    idades.append(idade)
    resp = str(input('Continuar? (S/N) '))
    cont += 1
    if resp in 'Nn':
        print('Cadastro finalizado!')
        break

media = (sum(idades) / cont)

for nome in range nomes:
    cadastro['Nome'] = nomes[nome]
    cadastros.append(cadastro.items)

for j in idades:
    if j > media:
        acima.append(j)

print(f'Pessoas cadastradas: {cont-1}')
print(f'Média de idade: {media}')
print(f'Mulheres: {mulheres}')
print(f'Idades acima da média: {acima}')
print(cadastros)
