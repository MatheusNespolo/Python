from datetime import datetime

def voto(a):
    ano_atual = datetime.today().year
    idade = ano_atual - a
    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 18 < idade < 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade > 70:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print('Ano de nascimento inválido.')

ano = int(input('Em que ano você nasceu? '))
voto(ano)
