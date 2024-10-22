boletim = {}
boletim['Nome'] = str(input('Insira seu nome: '))
boletim['Média'] = float(input('Digite sua média: '))
if boletim['Média'] >= 6:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'

print(f'O nome é {boletim["Nome"]}')
print(f'A média é {boletim["Média"]} e')
print(f'A situação é {boletim["Situação"]}')
