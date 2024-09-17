import random
numpc = random.randint(0,999)
derrota = bool = False
escolha = vitoria = 0
while not derrota:
    escolha = int(input('1 - Ímpar\n2 - Par\nEscolha par ou ímpar: '))
    numjog = int(input('Escolha um número: '))
    if escolha == 1:
        if ((numpc + numjog)%2) != 0:
            vitoria += 1
            print('Você venceu! Siga jogando.')
        else:
            print('Você perdeu!')
            derrota = False
            break
    elif escolha == 2:
        if ((numpc + numjog)%2) == 0:
            vitoria += 1
            print('Você venceu! Siga jogando.')
        else:
            print('Você perdeu!')
            derrota = False
            break
if vitoria > 0:
    print(f'Você venceu {vitoria} vezes.')