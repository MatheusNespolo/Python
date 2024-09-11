soma = 0
cont = 0
for c in range (1,7):
    n1 = int(input('Digite um número inteiro: '))
    if n1%2 == 0:
        soma =+ n1
        cont =+ 1
    else:
        print('Não é um número par.')
print('Você informou {} número(s) par(es) e a soma foi {}.'.format(cont, n1))
