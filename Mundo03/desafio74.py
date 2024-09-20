import random
num1 = random.randint(0,999)
num2 = random.randint(0,999)
num3 = random.randint(0,999)
num4 = random.randint(0,999)
num5 = random.randint(0,999)

tupla = (num1, num2, num3, num4, num5)
print(sorted(tupla))
print(f'O maior valor é: {max(tupla)}')
print(f'O menor valor é: {min(tupla)}')