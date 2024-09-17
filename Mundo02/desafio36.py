casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
mensal = casa / (anos * 12)
if mensal <= (salario * 0.3):
    print('É viável fazer o financiamento.')
else:
    print('Não é viável fazer o financiamento.')