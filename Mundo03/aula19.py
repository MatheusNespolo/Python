pessoas = {
    'nome':'Matheus',
    'sexo':'M',
    'idade':22
}
pessoas['peso'] = 76.6
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k}: {v}')

estado1 = {
    'UF': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'UF': 'São Paulo',
    'sigla': 'SP'
}
brasil = []

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['UF'])

estado3 = {}
brazil = []
for c in range (0, 3):
    estado3['UF'] = str(input('Unidade Federativa: '))
    estado3['Sigla'] = str(input('Sigla: '))
    brazil.append(estado3.copy())
for e in brazil:
    for k, v in e.items():
        print(f'{k} corresponde a {v}')
