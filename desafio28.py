import random
num = random.randrange(0,999,1)
tent = int(input('Adivinhe qual o número entre 0 e 999: '))
if num != tent:
    tent = int(input('Adivinhe qual o número entre 0 e 999: '))
print('Parabéns! Você adivinhou.')