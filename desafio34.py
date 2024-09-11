salario = float(input('Digite seu salário: '))
if salario > 1250:
    aumento = salario * 0.1
    print('Com o aumento, seu salário será de:', salario + aumento)
elif salario <= 1250:
    aumento = salario * 0.15
    print('Com o aumento, seu salário será de:', salario + aumento)
