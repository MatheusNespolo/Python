from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Em que ano nasceu a pessoa {}? '.format(c)))
    if atual - ano < 18 and atual - ano > 0 and atual - ano < 199:
        menor += 1
    elif atual - ano >= 18 and atual - ano < 199:
        maior += 1
    else:
        print('Digite uma data válida.')
if maior > 0 and menor > 0:
    print('{} pessoas são menores de idade. {} têm 18 anos ou mais.'.format(menor, maior))
else:
    print('Digite uma datas válidas.')