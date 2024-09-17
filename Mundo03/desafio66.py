n = s= 0
cont = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    cont += 1
    s += n
s -= 999
print(f'Foram digitados {cont} números e a soma deles é {s}')