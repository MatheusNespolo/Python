nasc = int(input('Digite o ano do seu nascimento: '))
atual = 2024
if (atual - nasc) < 18 and (atual - nasc) > 0:
    print('Você ainda não tem idade para servir o tiro de guerra.')
elif (atual - nasc) == 18:
    print('Você deve alistar-se esse ano.')
elif (atual - nasc) > 18:
    print('Você já serviu, foi dispensado ou está em débito com a pátria.')
else:
    print('Data de nascimento inválida.')