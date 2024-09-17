nums = 0
n = 0
m = 0
start = bool = True
while start:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        start == 0
        break
    else:
        m += n
        nums += 1
print(f'Foram digitados {nums} números. A soma deles é igual a {m}')