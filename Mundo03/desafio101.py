
def voto(a):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - a
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 18 <= idade < 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print('Ano de nascimento inválido.')

ano = int(input('Em que ano você nasceu? '))
voto(ano)
