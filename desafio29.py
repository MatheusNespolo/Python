velo = float(input('Velocidade (Km/h): '))
if velo > 80.0:
    multa = (velo - 80) * 7
    print('Você foi multado em', multa, 'reais.')
else:
    print('Você está no limite.')