sexo = str(input('Informe seu sexo: '))
informe = bool
while not informe:
    sexo = str(input('Informe seu sexo:  '))
    if sexo in 'MmFf':
        informe = 1
    else:
        informe = 0
        break