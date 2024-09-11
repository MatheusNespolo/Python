import random
acerto = 0
num = random.randrange(0,999,1)
tent = int(input('Adivinhe qual o número entre 0 e 999: '))
while not acerto:
    tent = int(input('Adivinhe qual o número entre 0 e 999: '))
    if tent == num:
        acerto = 1
        break
print('Parabéns! Você adivinhou.')