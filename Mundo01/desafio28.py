import random
num = random.randrange(0,10,1)
tent = int(input('Adivinhe qual o número entre 0 e 10: '))
if num != tent:
    tent = int(input('Adivinhe qual o número entre 0 e 10: '))
print('Parabéns! Você adivinhou.')