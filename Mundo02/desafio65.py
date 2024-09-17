numeros = []
nums = 0
m = 0
exec = bool = True
while exec:
    n = int(input('Digite um número inteiro: '))
    numeros.append(n)
    op = str(input('Deseja continuar? (S/N): '))
    if op in 'Nn':
        exec == 0
        break
    elif op in 'Ss':
        m += n
        nums += 1
        maior = (max(numeros))
        menor = (min(numeros))
print(f'O maior valor é {maior} e o menor é {menor}. A média entre eles é igual a {m/nums}')