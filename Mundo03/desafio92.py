import datetime
pessoas = {
    'nome':'',
    'idade':'',
    'carteira':'',
    'anoContra':'',
    'salario':'',
    'aposentadoria':''
}
pessoas['nome'] = str(input('Digite o nome: '))
anoNasc = int(input('Digite o ano de nascimento: '))
pessoas['idade'] = datetime.date.today().year - anoNasc
pessoas['carteira'] = str(input('Possui CPTS? (S/N) '))
if pessoas['carteira'] != 'Nn':
    anoContra = int(input('Digite o ano de contratação: '))
    pessoas['anoContra'] = anoContra
    pessoas['aposentadoria'] = (anoContra + 35) - anoNasc
    pessoas['salario'] = int(input('Digite o salário: '))
for k, v in pessoas.items():
    print(f'{k}: {v}')
