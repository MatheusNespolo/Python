n = int(input('Quantos termos você quer mostrar: '))
n1, n2 = 0, 1
count = 0
if n <= 0:
    print('Digite um valor inteiro positivo')
elif n == 1:
    print(n, 'primeiros termos da Sequência Fibonacci:')
    print(n1)
else:
    print('Sequência Fibonacci: ')
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1